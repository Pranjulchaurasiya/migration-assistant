# Parse inventory

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

15 workflows parsed with 0 failures. Every workflow in the estate is listed and assessed.

`first task` columns: the first task in the file, and the first task the run actually reaches from `root-name`. Where they differ, a converter that walks the file in order starts in the wrong place.

| Workflow | Source | Items | Script lines | Item types | Root | First task in file | First task run | Differs | Colour |
|---|---|---|---|---|---|---|---|---|---|
| Detect - Apply Segment | detection | 2 | 4 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Detect - Create Group | detection | 2 | 5 | end 1, task 1 | item1 | item1 | item1 |  | red |
| Detect - Notify | detection | 2 | 5 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Detect - Patch Linux | detection | 2 | 4 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Lab - Change Password | triage | 2 | 4 | end 1, task 1 | item1 | item1 | item1 |  | red |
| Lab - Create Admin | triage | 2 | 4 | end 1, task 1 | item1 | item1 | item1 |  | green |
| Lab - Create Pool | triage | 2 | 6 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Lab - Create Tenant | triage | 2 | 0 | end 1, link 1 | item1 |  |  |  | amber |
| Lab - Delete Tenant | triage | 2 | 4 | end 1, task 1 | item1 | item1 | item1 |  | green |
| Lab - Enable Override | triage | 2 | 6 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Lab - Find or Create Tenant | triage | 2 | 6 | end 1, task 1 | item1 | item1 | item1 |  | green |
| Lab - Forget Controller | triage | 2 | 3 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Lab - Purge Volumes | triage | 2 | 5 | end 1, task 1 | item1 | item1 | item1 |  | amber |
| Lab - Run Remote Command | triage | 7 | 23 | condition 1, end 1, task 5 | item6 | item2 | item6 | yes | red |
| Process Tenant Notification | triage | 4 | 5 | end 1, link 2, switch 1 | item1 |  |  |  | amber |

## Actions

| Action | Source | Lines | Called by workflows | Called by actions | In forms (OGNL) |
|---|---|---|---|---|---|
| `com.example.detect/callRest` | detection | 6 | 0 | 2 | 0 |
| `com.example.detect/createSecurityGroup` | detection | 10 | 1 | 0 | 0 |
| `com.example.detect/endpoint` | detection | 3 | 0 | 3 | 0 |
| `com.example.detect/launchJobTemplate` | detection | 3 | 1 | 0 | 0 |
| `com.example.detect/postSlackMessage` | detection | 6 | 1 | 0 | 0 |
| `com.example.detect/postTeamsMessage` | detection | 7 | 1 | 0 | 0 |
| `com.example.detect/queueRun` | detection | 3 | 1 | 0 | 0 |
| `com.example.lab/createVRAPoolObj` | triage | 5 | 1 | 0 | 0 |
| `com.example.lab/listControllers` | triage | 1 | 0 | 0 | 1 |
