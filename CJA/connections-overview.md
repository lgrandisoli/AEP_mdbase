---
title: "Connections overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/overview"
category: "overview"
topic: "analytics-platform/using/cja-connections/overview"
created_at: "2026-06-02T19:04:29.878278+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Connections overview

Last update: May 13, 2026
- Topics:
- [Connections](#)

CREATED FOR:

- Admin

Connections allow Customer Journey Analytics product administrators to define what Experience Platform data sources, such as event, lookup, profile, and summary datasets, are ingested. Connections are the foundation of Customer Journey Analytics and determine the availability of data (fields) that you can define in a [data view](/en/docs/analytics-platform/using/cja-dataviews/data-views) as dimension or metrics.

IMPORTANT
You can combine multiple Experience Platform datasets into a single connection.
## Connections workflow

See [Connect to data sources](/en/docs/customer-journey-analytics-learn/tutorials/connections/connecting-customer-journey-analytics-to-data-sources-in-platform#_blank) for a demo video.

style
shade-box
On a high-level, the Connections workflow allows you to:

Interface
Description
➊
Manage your connections and overall usage
of Customer Journey Analytics from the Connections manager.
➋
Inspect the details of a connection
, like dataset records ingested, skipped, or deleted.
➌
Create or edit the configuration of a connection
, like a rolling data window, the sandbox to use, which datasets are part of the connection, and more.
➍
Add datasets to a connection
. Your connection should at least have one event or summary dataset but can contain a variety of event, profile, lookup, and summary datasets.
➎
Configure the settings
for datasets that you add. You can determine how to link different datasets based on a common person-based or
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
account-based identifier.
➏
Edit the settings for an existing dataset
. You can always revisit the dataset settings at a later stage.
## Access control

Access to connections management should be restricted to a core management group. Connection configurations have contractual implications regarding volume allotments for data brought into Customer Journey Analytics.

Related Articles
Access control
.
recommendation-more-help
