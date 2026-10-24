# Preflight: readiness (upgrade)

Generated 2026-10-24T16:02:10Z from `upgrade/`. No model calls; this stage only reads files.

## Customer answers

Read from `upgrade/kestra-assessment/your-input/answers.yaml`. The export cannot answer these. 0 of 9 are open, and every later stage carries them as open items.

**Q1. Is this export the whole vRO estate? If not, what is missing, and how many vRO nodes or clusters does the estate run on?** (answered)

> answer for q1-scope

Why it matters: Every count in Assess and Brief is only as complete as the export. A partial export hides callers and callees. Read by: assess: unexported calls; brief: retire candidates, waves.

**Q2. What starts these workflows from outside vRO? Two ways to answer, and they can be combined: put the vRA content export (a .vra-ng from Build Tools) in the export folder, and the tool reads its catalog items, cloud templates and event broker subscriptions; and list in your-input/entry-points.yaml whatever that export does not hold, or everything if there is no export: vRO scheduled tasks and policies, the ITSM (for example ServiceNow), and scripts calling the vRO REST API. Set complete: true there once the list is whole.** (answered)

> answer for q2-external-callers

Why it matters: None of these are in a vRO package. Without them every workflow nobody calls in the export looks like an entry point or dead code, and the two cannot be told apart. Read by: brief: retire pass, entry points, rebuild outcome.

**Q3. For each system the tool found (SSH hosts), is there a non-production instance a converted flow can run against? Name any other system the workflows reach.** (answered)

Found by the tool: SSH hosts (from the workflows' code).

> answer for q3-non-production-targets

Why it matters: A wave that writes to a target cannot be verified without somewhere safe to write. Read-only waves can go first either way. Read by: brief: wave entry criteria.

**Q4. Is anything in this export off limits for this migration (owned by another team, frozen, vendor supplied, or due to be replaced)?** (answered)

> answer for q4-off-limits

Why it matters: Off-limits workflows are dropped from the waves, and whatever calls them keeps a dependency on vRO. Read by: brief: waves, blocked list.

**Q5. Has anyone tried to migrate or rewrite any of this before? What happened?** (answered)

> answer for q5-prior-attempts

Why it matters: A previous attempt usually found the hard part already. It belongs in the brief's risks. Read by: brief: risks.

**Q6. Who owns each functional area (for example load balancing, network provisioning, tenant onboarding)? Name a person or team per area.** (answered)

> answer for q6-owners

Why it matters: Open questions, retire candidates and wave approvals need someone to answer them. The brief lists open questions by area. Read by: brief: open questions, approval.

**Q7. Can you export twelve months of workflow run history (vRO workflow tokens, or the vRA deployment history), with workflow ID, start time and result?** (answered)

> answer for q7-execution-history

Why it matters: The retire rule is 'no executions in twelve months'. Without history it cannot be tested, only guessed from the call graph. Read by: brief: retire pass.

**Q8. The code uses these vRO plugins: HTTP-REST plugin (built in), SSH, the plugin of type AD. Is that the list? Correct it if not, and add the installed version per node and any custom or in-house plugin.** (answered)

Found by the tool: HTTP-REST plugin (built in) (REST requests built in callRest, launchJobTemplate, postSlackMessage, postTeamsMessage and 1 more); SSH (calls such as SSHSession.connectWithPassword, calls such as SSHSession.connectWithPasswordOrIdentity, calls such as SSHSession.disconnect, calls such as SSHSession.executeCommand); the plugin of type AD (object type AD:OrganizationalUnit, object type AD:UserGroup).

> HTTP-REST plugin (built in), SSH, the plugin of type AD

Why it matters: A plugin object type Kestra cannot reach blocks every workflow that uses it. The export only records plugins by name where dunes-meta-inf lists them. Read by: assess: target inventory.

**Q9. If vRA starts any of these workflows: will it stay as the front end, with its catalog items and subscriptions calling Kestra, or be replaced, with Kestra Apps and flows taking over its catalog items, cloud templates and subscriptions? Answer keep, replace, or replace with a bridge until then (vRA's subscriptions call Kestra through webhooks while the Apps and flows are built, then vRA is switched off).** (not applicable)

> No vRA content on record, so nothing to keep or replace.

Why it matters: The trigger plan differs: kept, every subscription calls a Kestra webhook (and a blocking one waits for the result); replaced, each catalog item becomes a Kestra App and each cloud template a flow whose steps are the old lifecycle events; replaced with a bridge, the converted flows run behind webhooks first and vRA goes once the replacement is ready. Unanswered, the brief shows both. Read by: brief: trigger plan, wave entry criteria.

## Scope

The export holds 15 workflows. Assess and Brief work on every workflow and action in this estate.

## Checks

| Check | Status | Found | What to do |
|---|---|---|---|
| Formats | ready | 2 raw-xml across 2 input(s); all read with 0 failures |  |
| Element counts | ready | 1 ConfigurationElement, 9 ScriptModule, 15 Workflow |  |
| Execution history | missing | none in the export | Export run history (Q7). Until then the retire rule is untestable. |
| Source vRO version | gap | none (from dunes-meta-inf); no version recorded for detection, triage | Confirm the version per node (Q1, Q8). Sources built from source control carry no version. |
| Plugins declared | gap | none declared in dunes-meta-inf; other plugins are only visible from object types in the XML | Confirm installed plugins (Q8). |
| Entry points | missing | no vRA export and nothing in entry-points.yaml: no catalog items, subscriptions, scheduled tasks or policies | Add the .vra-ng to the estate folder, or fill in entry-points.yaml (Q2). Until then, entry points are guessed from the call graph. |
| Input forms | gap | 0 workflow(s) ship a separate input form; presentation is otherwise read from the workflow XML |  |
| Sanitized copy for sharing | ready | 3 values redacted, 3 secret or configuration values dropped, 0 left in place as unsure; copy in data/0-preflight/sanitized/ | Review redaction-report.md before anything leaves the network. |
| Customer answers | ready | 9 of 9 answered in your-input/answers.yaml | Fill in upgrade/kestra-assessment/your-input/answers.yaml. |

## Sources

| Input | Format | Signed | vRO version | Plugins declared | Elements |
|---|---|---|---|---|---|
| detection | raw-xml | no | not recorded | none | 1 ConfigurationElement, 7 ScriptModule, 4 Workflow |
| triage | raw-xml | no | not recorded | none | 2 ScriptModule, 11 Workflow |

0 source(s) record a build host in dunes-meta-inf. The value is not repeated here.

## Entry points

What starts these workflows from outside vRO (Q2): read from 0 vRA export(s) and from `upgrade/kestra-assessment/your-input/entry-points.yaml` (0 hand-written entries). Workflow references are matched to the package by vRO workflow ID. The normalized list is in `entry-points.json`.

## Verdict per stage

| Stage | Verdict | Why |
|---|---|---|
| /vro-assess | Ready | Needs only the export. Target reach for plugins not listed in dunes-meta-inf is read from object types. |
| /vro-brief | Ready | 0 preflight question(s) open. The retire pass is untestable without history, and wave entry criteria keep the open items as gates. |
| convert (not built yet) | Not ready | Needs an approved brief, and a non-production instance for every target a wave writes to (Q3). |

## Most important gap

No execution history and no external entry points (Q2, Q7). Without them the brief cannot say which workflows are unused, only which ones nothing in the export calls.
