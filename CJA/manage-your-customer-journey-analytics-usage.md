---
title: "Manage your Customer Journey Analytics usage"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/technotes/estimate-usage"
category: "other"
topic: "analytics-platform/using/technotes/estimate-usage"
created_at: "2026-06-02T19:05:19.374310+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage your Customer Journey Analytics usage

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

TIP
Use the
Usage
interface
to
view
the usage of ingested and reportable rows across all connections in Customer Journey Analytics.
You can manage your Customer Journey Analytics usage in the [Connections interface](/en/docs/analytics-platform/using/cja-connections/create-connection). In this interface, you can can define the Customer Journey Analytics data retention as a rolling window in months (1 month, 3 months, 6 months, etc.), at the connection level.

The main benefit is that you store or report only on data that is applicable and useful and delete older data that is no longer useful. It helps you stay under your contract limits and reduces the risk of overage cost.

If you leave the default (unchecked), the retention period will be superseded by the Adobe Experience Platform data retention setting. If you have 25 months’ worth of data in Experience Platform, Customer Journey Analytics will get 25 months of data through backfill. If you deleted 10 of those months in Platform, Customer Journey Analytics would retain the remaining 15 months.

Data retention is based on timestamps and applies to event datasets and summary data datasets only. No rolling data window setting exists for profile or lookup datasets, since there are no applicable timestamps. If your connection includes any profile or lookup datasets, since they are joined with event datasets, the data is retained in Customer Journey Analytics based on your data retention settings on the event dataset timestamps.

Related Articles
View your Customer Journey Analytics usage
recommendation-more-help
