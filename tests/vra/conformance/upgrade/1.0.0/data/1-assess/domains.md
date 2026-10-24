# Domains

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

## Rule

source package family x lifecycle stage (majority of member names by verb: provisioning: ^(create|instantiate|find or create|delete|remove|vs creation|install|deploy)\b; configuration: ^(assign|attach|detach|edit|change|reconfigure|setup|set up|enable|disable|remote|nsx-t cloud|scale ?out|scale ?in|add|update|certificate)\b; operations: ^(get|find|process|avi ssh|send|list|check|run)\b). A cluster whose members and their exported callees make no call to an external system goes to fixtures. The cluster's primary target (most operations, vRO platform excluded) is recorded alongside.

Code makes the grouping. The model was only asked for a name and a sentence per domain, given the cached cluster summaries, and cannot move a cluster. A person can rename or move one by adding `your-input/corrections.yaml`, an optional file (INPUTS.md shows it).

| Domain | Key | Name | Name from | Clusters | Workflows | Targets |
|---|---|---|---|---|---|---|
| D1 | `triage:operations` | Tenant workflows (REST hosts, SSH) | code fallback | C01, C04 | 12 | rest-host, ssh-host |
| D2 | `none:fixtures` | Tenant workflows (no external system found) | code fallback | C02, C03, C05 | 3 |  |


## How each cluster was placed

| Cluster | Domain key | Decided by |
|---|---|---|
| C01 | `triage:operations` | source triage; talks to rest-host (5 of 5 target operations, own or through exported callees); stage from member names {'operations': 5, 'configuration': 2, 'provisioning': 4} |
| C02 | `none:fixtures` | no operation against any external system in any member or its exported callees |
| C03 | `none:fixtures` | no operation against any external system in any member or its exported callees |
| C04 | `triage:operations` | source triage; talks to ssh-host (6 of 6 target operations, own or through exported callees); stage from member names {'operations': 1} |
| C05 | `none:fixtures` | no operation against any external system in any member or its exported callees |
