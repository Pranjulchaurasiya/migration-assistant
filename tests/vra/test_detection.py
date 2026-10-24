"""
Systems 1.0.0 did not name, named from the sanitized copy (1.1.0): Ansible Tower and Terraform Enterprise by the
paths their callers pass, Teams and Slack webhooks by the host Sanitize saw behind a value it replaced (and Teams by
its MessageCard body), and Active Directory by the vRO AD plugin's types and singleton.

The estate is tests/vra/conformance/detection/ (built by its build.py; every name and value in it is invented), run
the way a customer runs it, with no model: Sanitize, Preflight, Assess and Brief.
"""
from __future__ import annotations

import json
import os

import pytest

from kestra_migration_assistant.vra.stages import targets as T


@pytest.fixture(scope="module")
def detection(conformance_stages):
    stages = conformance_stages("detection")
    read = lambda *p: json.load(open(os.path.join(stages, "data", *p)))
    return {"stages": stages, "assess": read("1-assess", "assess.json"), "brief": read("3-brief", "brief.json"),
            "redaction": read("0-preflight", "redaction-report.json")}


def _ops(a: dict, key: str) -> list[str]:
    t = a["targets"][key]
    return [o["op"] for o in t["operations"]] + list(t["action_only_operations"])


def test_each_system_is_named(detection):
    a = detection["assess"]
    assert {"ansible-tower", "terraform-enterprise", "ms-teams", "slack", "active-directory"} <= set(a["targets"])
    assert "POST /api/v2/job_templates/{templateId}/launch/" in _ops(a, "ansible-tower")
    assert "POST /api/v2/runs" in _ops(a, "terraform-enterprise")
    assert _ops(a, "ms-teams") == ["POST "] and _ops(a, "slack") == ["POST "]
    ad = _ops(a, "active-directory")
    assert {"ActiveDirectory.searchExactMatch", "AD:OrganizationalUnit.createUserGroup",
            "AD:UserGroup.setAttribute"} <= set(ad)
    assert not [o for o in ad if "indexOf" in o]            # string work on a property is not an operation
    rest = a["targets"].get("rest-host") or {}
    assert not [o for o in rest.get("operations") or [] if "/api/v2/" in o["op"] or o["op"] == "POST "]


def test_webhooks_are_named_from_what_sanitize_saw_never_from_a_value(detection):
    seen = detection["redaction"]["systems_seen"]
    assert seen["teamsWebhookUrl"] == "ms-teams" and seen["slackWebhookUrl"] == "slack"
    assert "towerUrl" not in seen                           # a host no signature knows names nothing
    for dp, _d, fs in os.walk(detection["stages"]):
        for f in fs:
            if f.endswith((".json", ".md", ".html", ".yaml", ".csv")):
                text = open(os.path.join(dp, f), encoding="utf-8", errors="replace").read()
                assert "hooks.slack.com" not in text and "webhook.office.com" not in text, f


def test_coverage_names_the_plugin_task_or_says_the_pattern_is_not_covered(detection):
    rows = {r["key"]: r for r in detection["assess"]["plugin_coverage"]["rows"]}
    assert [m["task"] for m in rows["ms-teams"]["task_map"]] == ["io.kestra.plugin.microsoft365.teams.TeamsIncomingWebhook"]
    assert [m["task"] for m in rows["slack"]["task_map"]] == ["io.kestra.plugin.slack.notifications.SlackIncomingWebhook"]
    assert rows["ms-teams"]["status"] == rows["slack"]["status"] == "plugin"
    for k in ("ansible-tower", "terraform-enterprise"):
        assert rows[k]["status"] == "partial" and rows[k]["unmatched_ops"] and rows[k]["pattern_gap"]
    ad = rows["active-directory"]
    assert {m["task"].rsplit(".", 1)[1] for m in ad["task_map"]} >= {"Search", "Add", "Modify"}


def test_translation_text_does_not_overclaim(detection):
    at = {t["name"]: t for t in detection["brief"]["action_triage"].values()}
    tower = at["launchJobTemplate"]
    assert tower["outcome"] == "Plugin-covered library"
    assert "Ansible Tower / AWX" in tower["reason"] and "no task that launches a Tower or AWX job template" in tower["reason"]
    assert "Terraform Cloud / Enterprise API" in at["queueRun"]["reason"] or "runs API" in at["queueRun"]["reason"]
    assert "TeamsIncomingWebhook" in at["postTeamsMessage"]["reason"]
    assert "SlackIncomingWebhook" in at["postSlackMessage"]["reason"]
    for t in at.values():
        assert "client for ," not in t["reason"] and "plugin for ()" not in t["reason"], t["reason"]


def test_a_client_of_unnamed_rest_hosts_reads_as_an_http_client():
    from kestra_migration_assistant.vra.stages import triage as TR
    a = {"uid": "a", "key": "k", "wrapper": False, "library_for": ["rest-host"], "calls_actions": [], "called": True,
         "ops": [{"op": "POST /iaas/api/login", "target": "rest-host"}],
         "all_ops": [{"op": "POST /iaas/api/login", "target": "rest-host"}]}
    t = TR.triage_action(a, {"rest-host": {"reach": "plugin", "name": "REST hosts"}}, None)
    assert t["outcome"] == "Plugin-covered library"
    assert t["reason"].startswith("hand-written HTTP client") and "io.kestra.plugin.core.http.Request" in t["reason"]


def test_name_rest_target_from_paths_bodies_and_seen_hosts():
    T.load_plugin_map()
    assert T.name_rest_target(["/api/v2/job_templates/{id}/launch/"])[0] == "ansible-tower"
    assert T.name_rest_target(["/api/v2/workspaces/{id}/vars"])[0] == "terraform-enterprise"
    assert T.name_rest_target(["MessageCard", ""])[0] == "ms-teams"
    T.SEEN_SYSTEMS.clear()
    T.SEEN_SYSTEMS.update({"<URL-07>": "slack"})
    try:
        tgt, why = T.name_rest_target(["<URL-07>", ""])
        assert tgt == "slack" and why == ["host behind <URL-07>"]
    finally:
        T.SEEN_SYSTEMS.clear()
    assert T.name_rest_target(["/api/v2/runs", "/api/v2/jobs/1/"])[0] == "rest-host"   # two systems: not named
    assert T.host_target("hooks.slack.com") == "slack" and T.host_target("acme.webhook.office.com") == "ms-teams"
    assert T.host_target("tower.example.net") is None
