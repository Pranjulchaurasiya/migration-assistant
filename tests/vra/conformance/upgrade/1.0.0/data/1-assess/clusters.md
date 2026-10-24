# Clusters

Generated 2026-10-24T16:02:10Z by `/vro-assess`. Code only: no model calls apart from the domain names, which come from one cached call over the cached cluster summaries.

Method: single-linkage agglomerative over weighted feature similarity, implemented as union-find, cut at the threshold, threshold 0.62. Weights: shape 0.3, graph 0.1, plugins 0.15, sdk 0.1, io 0.15, scripts 0.2.

Clustered by a fingerprint of each workflow's item types, graph shape, plugin types, SDK calls, signature and normalised scripts.

Names and summaries come from `2-understand/cluster-summaries.json` (model-written by Understand), matched to clusters by member set; a cluster without one has no name here.

| Cluster | Size | Domain | Name (cached summary) | First of a kind | Colour mix |
|---|---|---|---|---|---|
| C01 | 11 | D1 |  | Lab - Find or Create Tenant | amber 7, green 3, red 1 |
| C02 | 1 | D2 |  | Detect - Create Group | red 1 |
| C03 | 1 | D2 |  | Lab - Create Tenant | amber 1 |
| C04 | 1 | D1 |  | Lab - Run Remote Command | red 1 |
| C05 | 1 | D2 |  | Process Tenant Notification | amber 1 |

## C01: 

Members: Detect - Apply Segment, Detect - Notify, Detect - Patch Linux, Lab - Change Password, Lab - Create Admin, Lab - Create Pool, Lab - Delete Tenant, Lab - Enable Override, Lab - Find or Create Tenant, Lab - Forget Controller, Lab - Purge Volumes

Strongest pair: Lab - Create Admin and Lab - Find or Create Tenant at 0.816.

## C02: 

Members: Detect - Create Group

## C03: 

Members: Lab - Create Tenant

## C04: 

Members: Lab - Run Remote Command

## C05: 

Members: Process Tenant Notification
