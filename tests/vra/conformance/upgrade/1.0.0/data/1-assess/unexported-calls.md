# Unexported calls

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

2 calls from workflows go to something that is not in the export. A migration that converts only the export breaks at each one.

| Kind | Calls | What it means |
|---|---|---|
| plugin library workflow | 0 | Shipped with a vRO plugin (the parameters are plugin objects). Replace with a call to the target's API. |
| vRO library workflow | 0 | Shipped with vRO itself. Replace by design (the Kestra side has its own mechanism). |
| unknown workflow | 0 | Nothing says what it is. Ask the owner (preflight Q1). |
| action not in export | 2 | An action from a module that was not exported. |

## Lab - Enable Override

| Item | Mode | Called | ID | Kind | Reaches |
|---|---|---|---|---|---|
|  | action | waitTaskEnd | `com.example.vendor/waitTaskEnd` | action not in export |  |

## Lab - Purge Volumes

| Item | Mode | Called | ID | Kind | Reaches |
|---|---|---|---|---|---|
|  | action | purgeOrphanedVolumes | `com.example.vendor/purgeOrphanedVolumes` | action not in export |  |
