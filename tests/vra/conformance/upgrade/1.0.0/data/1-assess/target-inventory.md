# Target inventory

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

Every external system the workflows and the actions touch. Evidence: plugin object types, calls on typed variables, the Avi plugin client's REST calls, nested calls to workflows that are not in the export (attributed by the types passed to them), and the actions each workflow calls.

Kestra reach comes from `knowledge/plugin-map.yaml`, checked against the Kestra plugin catalogue. `http` means no Kestra plugin exists and the system's REST API is called with `io.kestra.plugin.core.http.Request`. `replace` means vRO-internal state with nothing to call: the Kestra design changes instead. Read or write is judged from the operation's verb.

| Target | Reach | Confirmed | Workflows | Actions | Operations | Reads | Writes |
|---|---|---|---|---|---|---|---|
| SSH hosts | plugin | yes | 1 | 0 | 4 | 0 | 4 |
| REST hosts (vRO HTTP-REST plugin) | plugin | yes | 3 | 4 | 4 | 1 | 3 |
| vRO platform services | replace | yes | 2 | 0 | 4 | 3 | 1 |

## SSH hosts (`ssh-host`)

- Found by: plugin
- vRO plugin: SSH
- Kestra reach: **plugin**
- Kestra tasks: `io.kestra.plugin.fs.ssh.Command`
- Evidence: https://kestra.io/plugins/plugin-fs/ssh/io.kestra.plugin.fs.ssh.command

Workflows (1): Lab - Run Remote Command

| Operation (from workflows and the actions they call) | Workflows | Mode | Reach |
|---|---|---|---|
| `SSHSession.connectWithPassword` | 1 | write | plugin |
| `SSHSession.connectWithPasswordOrIdentity` | 1 | write | plugin |
| `SSHSession.disconnect` | 1 | write | plugin |
| `SSHSession.executeCommand` | 1 | write | plugin |

## REST hosts (vRO HTTP-REST plugin) (`rest-host`)

- Found by: REST request; REST signature (the REST helper's call site)
- vRO plugin: none used here; reached with the HTTP-REST plugin or a REST helper action
- Kestra reach: **plugin**
- Kestra tasks: `io.kestra.plugin.core.http.Request`
- Evidence: https://kestra.io/plugins/core/http/io.kestra.plugin.core.http.request

Workflows (3): Detect - Apply Segment, Detect - Notify, Detect - Patch Linux

| Operation (from workflows and the actions they call) | Workflows | Mode | Reach |
|---|---|---|---|
| `GET /api/v2/jobs/{id}/` | 1 | read | plugin |
| `POST ` | 1 | write | plugin |
| `POST /api/v2/job_templates/{templateId}/launch/` | 1 | write | plugin |
| `POST /api/v2/runs` | 1 | write | plugin |

Operations found only in actions no dev workflow calls: `HTTP request (method and path from the caller)`

## vRO platform services (`vro-platform`)

- Found by: vRO platform call
- vRO plugin: none used here; reached with the HTTP-REST plugin or a REST helper action
- Kestra reach: **replace**
- Kestra tasks: `io.kestra.plugin.core.flow.Subflow`, `io.kestra.plugin.core.log.Log`
- Evidence: https://kestra.io/plugins/core

Workflows (2): Detect - Notify, Lab - Forget Controller

| Operation (from workflows and the actions they call) | Workflows | Mode | Reach |
|---|---|---|---|
| `get configuration element attribute (getAttributeWithKey)` | 1 | read | replace |
| `read configuration element Example` | 1 | read | replace |
| `read configuration element Example/Lab` | 1 | read | replace |
| `write configuration element (removeAttributeWithKey)` | 1 | write | replace |
