# Estate report

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

## Headline

| Measure | Value |
|---|---|
| Workflows in the export | 15 |
| Workflows assessed | 15 |
| Actions (script modules) | 9 |
| Configuration elements | 1 |
| Resource elements | 0 |
| Target systems | 2 |
| Clusters (singletons) | 5 (4) |
| Domains | 2 |
| Tests in the estate | 0 (vRO has no unit tests) |
| Lines of script in workflows / actions | 84 / 44 |
| Parse failures | 0 |
| Wrappers flagged | 1 |
| Actions that are clients for a target | 5 |
| Nested calls to something not in the export | 2 |
| Workflows whose first task in the file is not where the run starts | 1 |
| Entry points (vRA export and entry-points.yaml) | 0 |
| Workflows started by an entry point | 0 |
| Entry points naming a workflow not in the package | 0 |

## Readiness colour

A first colour score from the parse alone: green converts as is, amber needs choices, red has a hard blocker.

| Colour | Workflows |
|---|---|
| green | 3 |
| amber | 9 |
| red | 3 |

Why red (a workflow can have several):

| Reason | Workflows |
|---|---|
| plugin type with no known Kestra mapping | 1 |
| OGNL presentation qualifier | 1 |
| file-typed parameter with no Kestra equivalent | 1 |

That first score counts a vendor plugin type as a red blocker when it has no Kestra route on file. The target inventory now gives each target its route (plugin, HTTP, replaced, or none). The brief uses the target inventory, not this colour, to decide reachability.

Recomputed with the target inventory (the colour the explorer shows as readiness):

| Colour | Workflows |
|---|---|
| green | 3 |
| amber | 9 |
| red | 3 |

## Targets

| Target | Kestra reach | Workflows | Actions | Distinct operations (read / write) |
|---|---|---|---|---|
| SSH hosts | plugin | 1 | 0 | 4 (0 / 4) |
| REST hosts (vRO HTTP-REST plugin) | plugin | 3 | 4 | 4 (1 / 3) |
| vRO platform services | plugin | 2 | 0 | 4 (3 / 1) |

Details in [target-inventory.md](target-inventory.md).

## Domains

| Domain | Name | Clusters | Workflows |
|---|---|---|---|
| D1 | Tenant workflows (REST hosts, SSH) | C01, C04 | 12 |
| D2 | Tenant workflows (no external system found) | C02, C03, C05 | 3 |

How each grouping was decided: [domains.md](domains.md).

## Entry points

None on record: no vRA export in the estate folder and nothing in `your-input/entry-points.yaml` (preflight Q2). A workflow nothing calls may be an entry point or unused; the call graph cannot tell.

## Plugin coverage

Snapshot taken 2026-09-30T21:43:15Z (`kestra-plugins-2026-09-30.json`). installed: 255 plugins from http://localhost:8082/api/v1/plugins (Kestra 2.0.2 EE); catalog: 240 plugins from https://api.kestra.io/v1/plugins/subgroups.

| System | Touched through | Coverage | Kestra plugin (installed / catalogue) | Task types | Not covered by a task |
|---|---|---|---|---|---|
| REST hosts (vRO HTTP-REST plugin) | workflow code | Over HTTP (no plugin) | built in / built in | - | - |
| SSH hosts | workflow code | Kestra plugin, some operations over HTTP | plugin-fs 2.11.2 / plugin-fs 2.12.0 | - | SSHSession.connectWithPassword; SSHSession.connectWithPasswordOrIdentity; SSHSession.disconnect; SSHSession.executeCommand |
| vRO platform services | workflow code | Replaced by Kestra features | built in / built in | kv.Delete, kv.Get, kv.Set | - |

Where the instance and the catalogue disagree:

- SSH hosts: plugin-fs: installed 2.11.2, catalogue 2.12.0

## Files

- [parse-inventory.md](parse-inventory.md): every workflow and element as parsed
- [clusters.md](clusters.md): the 30 clusters and their cached summaries
- [target-inventory.md](target-inventory.md), `targets.json`
- [wrappers-and-libraries.md](wrappers-and-libraries.md)
- [unexported-calls.md](unexported-calls.md), `unexported-calls.csv`
- [domains.md](domains.md)
- `assess.json`: everything above, for the next stage
- `your-input/corrections.yaml`: corrections a person may add (optional, see INPUTS.md), read on every run
