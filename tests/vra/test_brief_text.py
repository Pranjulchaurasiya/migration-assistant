"""
The brief's text bugs found on a 46-workflow test estate (1.1.0), each checked on a conformance estate run the way a
customer runs it (no model; the committed specs stand in for the model's):

- the opening sentence, when catalog items are named for what they do ("This estate provisions an add user to AD
  group");
- code missing from the export, which read "Missing." once per piece in "What we need from you";
- the first of a kind, cut to the words the names don't share ("Create is the first of a kind", "LB - Create");
- the status line, which asked to confirm retire candidates corrections.yaml had already settled;
- retire candidates, which no page listed.
"""
from __future__ import annotations

import os
import re
import shutil

import pytest

from kestra_migration_assistant.vra.stages import common as C


def _configure(stages: str) -> None:
    estate = os.path.basename(stages)
    C.configure(estate, source_dir=os.path.join(os.path.dirname(os.path.dirname(stages)), "sources", estate),
                stages_dir=stages)


def _brief(stages: str) -> tuple[dict, dict, str]:
    from kestra_migration_assistant.vra.stages import front as F
    _configure(stages)
    a = C.read_json(os.path.join(stages, "data", "1-assess", "assess.json"))
    b = C.read_json(os.path.join(stages, "data", "3-brief", "brief.json"))
    return a, b, "\n".join(F.markdown(a, b))


@pytest.fixture(scope="module")
def triage(conformance_stages):
    return _brief(conformance_stages("triage"))


def test_code_missing_from_the_export_is_one_line_naming_each_piece(triage):
    _a, _b, md = triage
    assert "**Missing.**" not in md
    line = next(x for x in md.splitlines() if "of code the export does not have" in x)
    assert line.startswith("- **Two pieces of code the export does not have**")
    assert "waitTaskEnd (called by Lab - Enable Override)" in line
    assert "purgeOrphanedVolumes (called by Lab - Purge Volumes)" in line
    assert "sources/<estate>" not in md


def test_the_first_of_a_kind_is_named_in_full(triage):
    a, _b, md = triage
    names = {w["name"] for w in a["workflows"].values()}
    firsts = re.findall(r"(?:\*\* |\. )([^.*]+?) is the first of a kind", md)
    assert firsts and all(f in names for f in firsts), firsts


def test_retire_candidates_are_listed_until_settled(triage, conformance_stages, tmp_path):
    a, b, md = triage
    cands = sorted(a["workflows"][x["uid"]]["name"] for x in b["retire_candidates"])
    assert cands
    line = next(x for x in md.splitlines() if "nothing starts**" in x)
    assert all(n in line for n in cands[:5]) and "corrections.yaml" in line and "entry-points.yaml" in line
    # the workflow page says it too
    from kestra_migration_assistant.vra.stages import visuals as V
    page = V.workflow_page(b["retire_candidates"][0]["uid"], a, b)
    assert "Retire candidate:" in page

    # an owner settles every candidate in corrections.yaml: the status stops asking, and the brief stops listing
    stages = str(tmp_path / "stages" / "triage")
    shutil.copytree(conformance_stages("triage"), stages)
    shutil.copytree(os.path.join(os.path.dirname(os.path.dirname(conformance_stages("triage"))), "sources"),
                    str(tmp_path / "sources"))
    _configure(stages)
    os.makedirs(os.path.dirname(C.CORRECTIONS), exist_ok=True)
    with open(C.CORRECTIONS, "w", encoding="utf-8") as f:
        f.write("outcomes:\n" + "".join(f"  {x['uid']}:\n    outcome: Retire\n    reason: unused\n"
                                        for x in b["retire_candidates"]))
    from kestra_migration_assistant.vra.stages import brief, status
    old = os.environ.get("VRO_NO_MODEL")
    os.environ["VRO_NO_MODEL"] = "1"
    try:
        brief.run()
    finally:
        if old is None:
            os.environ.pop("VRO_NO_MODEL", None)
    a2, b2, md2 = _brief(stages)
    assert b2["retire_candidates"] and all(b2["triage"][x["uid"]]["outcome"] == "Retire" for x in b2["retire_candidates"])
    assert not any("Confirm or reject" in t for t in status.collect()["todo"])
    assert "nothing starts**" not in md2


def test_action_named_catalog_items_open_the_estate_paragraph_as_requests(conformance_stages):
    from kestra_migration_assistant.vra.stages import front as F
    a, b, _md = _brief(conformance_stages("helpers"))
    cats = a["entry_points"]["model"]["catalog_items"]
    assert cats
    noun = F.estate_paragraph(a, b)
    assert noun.startswith("This estate provisions ")
    cats[:] = [dict(cats[0], name=n) for n in ("Add User to AD Group", "Create AD Security Group", "Create DNS Record",
                                               "Reserve Static IP", "Standard Linux Server")]
    said = F.estate_paragraph(a, b)
    assert "provisions an add user" not in said and "This estate provisions" not in said
    assert said.startswith(f"Users request {F.word(len(cats))} Service Broker catalog items, such as "
                           "Add User to AD Group, Create AD Security Group and Create DNS Record.")
    assert "A user requests it from" not in said


def test_client_actions_for_other_systems_counts_every_system_it_holds():
    """The merged row counted only the systems a signature named, so REST-host clients (vRA's own API on the test
    estate) made "five other systems" of a row holding more."""
    from kestra_migration_assistant.vra.stages import front as F
    keys = ["infoblox", "servicenow", "powershell-host", "ssh-host", "mail"]
    assess = {"targets": {k: {"name": k, "short_name": k} for k in keys}, "actions": []}
    brief = {"action_triage": {}}
    x = {"key": ("client", "others", "Direct"), "others": True, "how": "Direct", "systems": set(keys),
         "rows": [{"id": "a-client-1", "systems": ["infoblox"], "items": []},
                  {"id": "a-client-2", "systems": [], "items": []}]}
    label, _ = F._say(x, assess, brief, {}, False, 4, False)
    assert label == "Client actions for six other systems"
    x["rows"] = x["rows"][:1]
    assert F._say(x, assess, brief, {}, False, 4, False)[0] == "Client actions for five other systems"


def test_the_recommendation_says_how_much_conversion_work_is_its_own():
    from kestra_migration_assistant.vra.stages import front as F
    outs = ["Convert"] * 26 + ["Needs owner input"] * 2 + ["Near-duplicate"] * 7 + ["Wrapper"] * 4
    brief = {"triage": {str(i): {"outcome": o} for i, o in enumerate(outs)}}
    assert F._own_conversions(brief, 39) == (" 28 of the 39 need a conversion of their own: seven are near-duplicates "
                                             "that follow their first of a kind and four are wrappers, whose callers "
                                             "call what they call directly.")
    # nothing to say when every workflow that converts is its own work (the load balancer sample)
    assert F._own_conversions({"triage": {str(i): {"outcome": "Convert"} for i in range(4)}}, 4) == ""
