# Wrappers and libraries

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

## Wrapper workflows

A wrapper is one call to something else (a nested workflow, an action, or one target operation) with at most three lines of its own logic and no decisions. The Avi plugin's session plumbing (initVroWorkflow, finishVroWorkflow, getAviVroClient) is not counted as a call.

| Workflow | Why |
|---|---|
| Lab - Create Tenant | one call (nested workflow 'Lab - Find or Create Tenant'), 0 line(s) of its own logic, no decisions |

## Actions that are clients for a target

5 of 9 actions call a target system. 25 of 44 action lines are in them.

| Action | Target | Lines | Operations | Called | Wrapper |
|---|---|---|---|---|---|
| `com.example.detect/callRest` | rest-host | 6 | 1 | yes |  |
| `com.example.detect/launchJobTemplate` | rest-host | 3 | 2 | yes |  |
| `com.example.detect/postSlackMessage` | rest-host | 6 | 1 | yes |  |
| `com.example.detect/postTeamsMessage` | rest-host | 7 | 1 | yes |  |
| `com.example.detect/queueRun` | rest-host | 3 | 1 | yes |  |

## Other actions

| Action | Lines | Called | Same code as |
|---|---|---|---|
| `com.example.detect/createSecurityGroup` | 10 | yes |  |
| `com.example.detect/endpoint` | 3 | yes |  |
| `com.example.lab/createVRAPoolObj` | 5 | yes |  |
| `com.example.lab/listControllers` | 1 | yes |  |
