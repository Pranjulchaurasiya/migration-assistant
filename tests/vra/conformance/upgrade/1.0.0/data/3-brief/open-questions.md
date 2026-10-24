# Open questions for owners

Every question below is an item in `your-input/answers.yaml`: a preflight one under the key shown, one from reading the workflows in the `questions` group. Answer it there and re-run. This page only lists them.

## Preflight (the export cannot answer these)

- [x] **Q1** Is this export the whole vRO estate? If not, what is missing, and how many vRO nodes or clusters does the estate run on? (`q1-scope`)
- [x] **Q2** What starts these workflows from outside vRO? Two ways to answer, and they can be combined: put the vRA content export (a .vra-ng from Build Tools) in the export folder, and the tool reads its catalog items, cloud templates and event broker subscriptions; and list in your-input/entry-points.yaml whatever that export does not hold, or everything if there is no export: vRO scheduled tasks and policies, the ITSM (for example ServiceNow), and scripts calling the vRO REST API. Set complete: true there once the list is whole. (`q2-external-callers`)
- [x] **Q3** For each system the tool found (SSH hosts), is there a non-production instance a converted flow can run against? Name any other system the workflows reach. (`q3-non-production-targets`)
- [x] **Q4** Is anything in this export off limits for this migration (owned by another team, frozen, vendor supplied, or due to be replaced)? (`q4-off-limits`)
- [x] **Q5** Has anyone tried to migrate or rewrite any of this before? What happened? (`q5-prior-attempts`)
- [x] **Q6** Who owns each functional area (for example load balancing, network provisioning, tenant onboarding)? Name a person or team per area. (`q6-owners`)
- [x] **Q7** Can you export twelve months of workflow run history (vRO workflow tokens, or the vRA deployment history), with workflow ID, start time and result? (`q7-execution-history`)
- [x] **Q8** The code uses these vRO plugins: HTTP-REST plugin (built in), SSH, the plugin of type AD. Is that the list? Correct it if not, and add the installed version per node and any custom or in-house plugin. (`q8-plugin-inventory`)
- [x] **Q9** If vRA starts any of these workflows: will it stay as the front end, with its catalog items and subscriptions calling Kestra, or be replaced, with Kestra Apps and flows taking over its catalog items, cloud templates and subscriptions? Answer keep, replace, or replace with a bridge until then (vRA's subscriptions call Kestra through webhooks while the Apps and flows are built, then vRA is switched off). (`q9-vra-front-end`)

## Per workflow, by domain

Questions whose theme is correctness, external contract or concurrency put a workflow in Needs owner input. A question a decision already asks is not asked again: it is listed under *Asked once* below.

### Tenant workflows (REST hosts, SSH) (8 questions, asked 10 times across the specs; owner: preflight Q6)

- [ ] *error semantics*: What should Detect   Apply Segment do when the target is unreachable? Applies to: Detect - Apply Segment (Convert), Detect - Notify (Convert).
  - also asked for Detect - Notify: What should Detect   Notify do when the target is unreachable?
- [ ] *error semantics*: What should Detect   Patch Linux do when the target is unreachable? Applies to: Detect - Patch Linux (Convert).
- [ ] *error semantics*: What should Lab   Change Password do when the target is unreachable? Applies to: Lab - Change Password (Manual).
- [ ] *error semantics*: What should Lab   Create Admin do when the target is unreachable? Applies to: Lab - Create Admin (Manual), Lab - Create Pool (Rebuild).
  - also asked for Lab - Create Pool: What should Lab   Create Pool do when the target is unreachable?
- [ ] *error semantics*: What should Lab   Enable Override do when the target is unreachable? Applies to: Lab - Enable Override (Needs owner input).
- [ ] *error semantics*: What should Lab   Forget Controller do when the target is unreachable? Applies to: Lab - Forget Controller (Rebuild).
- [ ] *error semantics*: What should Lab   Purge Volumes do when the target is unreachable? Applies to: Lab - Purge Volumes (Manual).
- [ ] *error semantics*: What should Lab   Run Remote Command do when the target is unreachable? Applies to: Lab - Run Remote Command (Manual).

### Tenant workflows (no external system found) (3 questions; owner: preflight Q6)

- [ ] *error semantics*: What should Detect   Create Group do when the target is unreachable? Applies to: Detect - Create Group (Convert).
- [ ] *error semantics*: What should Lab   Create Tenant do when the target is unreachable? Applies to: Lab - Create Tenant (Wrapper).
- [ ] *error semantics*: What should Process Tenant Notification do when the target is unreachable? Applies to: Process Tenant Notification (Rebuild).

## Suspected defects

Behavior the specs found in the code that looks unintended. Each one, with its evidence, is on its workflow's page, and is a keep-or-fix item in `your-input/answers.yaml`.

- Detect - Apply Segment: 1 possible defect, on [its page](../../report/workflows/detect-apply-segment.html)
- Detect - Create Group: 1 possible defect, on [its page](../../report/workflows/detect-create-group.html)
- Detect - Notify: 1 possible defect, on [its page](../../report/workflows/detect-notify.html)
- Detect - Patch Linux: 1 possible defect, on [its page](../../report/workflows/detect-patch-linux.html)
- Lab - Change Password: 1 possible defect, on [its page](../../report/workflows/lab-change-password.html)
- Lab - Create Admin: 1 possible defect, on [its page](../../report/workflows/lab-create-admin.html)
- Lab - Create Pool: 1 possible defect, on [its page](../../report/workflows/lab-create-pool.html)
- Lab - Create Tenant: 1 possible defect, on [its page](../../report/workflows/lab-create-tenant.html)
- Lab - Enable Override: 1 possible defect, on [its page](../../report/workflows/lab-enable-override.html)
- Lab - Forget Controller: 1 possible defect, on [its page](../../report/workflows/lab-forget-controller.html)
- Lab - Purge Volumes: 1 possible defect, on [its page](../../report/workflows/lab-purge-volumes.html)
- Lab - Run Remote Command: 1 possible defect, on [its page](../../report/workflows/lab-run-remote-command.html)
- Process Tenant Notification: 1 possible defect, on [its page](../../report/workflows/process-tenant-notification.html)
