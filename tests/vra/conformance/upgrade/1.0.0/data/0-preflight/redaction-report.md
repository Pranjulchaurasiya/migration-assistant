# Redaction report (upgrade)

Generated 2026-10-24T16:02:09Z by `kestra-migrate vra run` (sanitize) from `upgrade/`. The sanitized copy is in `upgrade/kestra-assessment/data/0-preflight/sanitized/`, laid out like the original.

**Review this before anything leaves your network.** Open a few files from the copy and check that nothing identifying is left, especially the items under "Not sure" below, which were deliberately left in place. No value that was redacted appears in this report, and no mapping back to the original values is written anywhere.

## What was changed

| Category | Occurrences replaced | Distinct values | Placeholders |
|---|---|---|---|
| HOST | 0 | 0 |  |
| IP | 0 | 0 |  |
| URL | 3 | 3 | <URL-01>, <URL-02>, <URL-03> |
| EMAIL | 0 | 0 |  |
| USER | 0 | 0 |  |
| SECRET | 0 | 0 |  |
| IDENTITY | 0 | 0 |  |
| NETWORK | 0 | 0 |  |

- Configuration element and SecureString values dropped (set to `__NULL__`): **3**
- Configuration element values kept because they can't identify anything (numbers, booleans, netmasks): **0**
- Package `signatures/` and `certificates/` entries removed: **0**. A sanitized package is for analysis only; it will not import into vRO.
- Files read: 52; files changed: 1.

NETWORK covers what a vRA export names networks by: network and subnet names, constraint and cloud account tags, CIDRs. USER also covers vRA owners, subscribers and principals; IDENTITY the tenant (orgId).

Public namespace and schema hosts were kept, because every vRO file has them and they identify no one: none.

The export's own module and category names were kept as written, though they read like host names, because they are code: the workflows' IDs and calls are built from them. None of them read like a host name in this export.

What stays the same: XML structure, item graphs, bindings, workflow, action, module, element and item names, IDs, types, and the scripts' logic. Markup is never edited. Every stage after this one (Preflight, Assess, Understand, Brief and the pages) reads this copy, never the export, so this copy is all the model is sent.

## Placeholders and what they replaced (masked)

| Placeholder | Category | Original (masked) |
|---|---|---|
| <URL-01> | URL | ht… (67 chars) |
| <URL-02> | URL | ht… (60 chars) |
| <URL-03> | URL | ht… (25 chars) |

## Not sure (left in place)

Single-label names with a digit (for example `vc-prod-01`) may be hostnames, and may equally be object names. They were not redacted. If any is a host, redact it by hand or add it to the export's owner notes before sharing.

Nothing.

## Files touched

| File | Changes |
|---|---|
| detection/ConfigurationElement/Example/Endpoints.xml | DROPPED 3, URL 3 |
