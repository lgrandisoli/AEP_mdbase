---
title: "Compare Analytics Source Connector data to Adobe Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/troubleshooting/compare"
category: "other"
topic: "analytics-platform/using/troubleshooting/compare"
created_at: "2026-06-23T20:43:31.385356+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Compare Analytics Source Connector data to Adobe Analytics

Last update: May 13, 2026
- Topics:
- [Troubleshooting](#)

CREATED FOR:

- Developer
- Admin

As your organization adopts Customer Journey Analytics, it is possible to notice some differences in data between Adobe Analytics and Customer Journey Analytics. These differences are normal and can happen for several reasons. Customer Journey Analytics is designed to allow you to improve upon some of the limitations on your data in Adobe Analytics. This flexibility can cause some differences in how Customer Journey Analytics interprets data. Use this article to understand potential differences in how Customer Journey Analytics and Adobe Analytics treats your data.

This page assumes that you ingest Adobe Analytics data into Adobe Experience Platform using the [Analytics source connector](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics), then created a [connection](/en/docs/analytics-platform/using/cja-connections/overview) and [data view](/en/docs/analytics-platform/using/cja-dataviews/data-views) in Customer Journey Analytics.

Consider the following possible reasons why data might differ between reporting platforms:

- Different datasets or report suites : Make sure that the report suite in Adobe Analytics and the report suite that the Source Connector derives data from are the same.
- Calendar settings : Report suites in Adobe Analytics contain a time zone and other calendar settings that you can configure. Similarly, data views in Customer Journey Analytics have a separate setting that you can control. Make sure that these settings match between products if parity is desired.
- Additional datasets : Customer Journey Analytics provides the capability to include multiple datasets within a single connection. These differences include additional event datasets, profile datasets, or lookup datasets. This capability is a key differentiator between Adobe Analytics and Customer Journey Analytics, allowing insight into cross-channel data.
- Stitched datasets : Adobe provides the ability to analyze person IDs between two datasets, resulting in a new dataset containing stitched IDs. These stitched datasets contain additional data beyond what an Adobe Analytics report suite offers.
- Data Sources : Customer Journey Analytics does not include any type of Data Sources uploaded to an Adobe Analytics report suite, including summary data sources or transaction ID data sources.
- Dimension and metric settings : Within a data view, every dimension and metric contains its own settings that your organization can alter. These changes apply at the time the report is run, and is therefore applied retroactively. Dimension and metric settings in Adobe Analytics change how data is collected, making those changes apply from that point forward. If you changed component settings in either product, they can create reporting differences. If focusing on a specific dimension, make sure that the attribution and persistence settings match between Adobe Analytics and Customer Journey Analytics. note tip TIP Adobe highly recommends that dimensions in Adobe Analytics use an allocation of ‘Most recent (last)’. This allocation setting allows much more attribution flexibility in Customer Journey Analytics.
- Visit definition : In addition to individual dimension and metric settings, the data view itself contains settings that fundamentally change how vistor data is interpreted. For example, you can apply a segment to an entire data view (similar to a Virtual report suite in Adobe Analytics). You can also change the definition of a visit duration, or automatically start a new visit on any desired event. Any of these settings can have a notable impact on reporting differences between Customer Journey Analytics and Adobe Analytics.

## Checking record count between products

If all of the above settings appear similar and you want to at least validate the number of records between products, you can use the following steps:

- In Adobe Experience Platform Query Services , run the following Total Records by timestamps query: code language-sql SELECT Substring(from_utc_timestamp(timestamp,'{timeZone}'), 1, 10) AS Day, Count(_id) AS Records FROM {dataset} WHERE timestamp >= from_utc_timestamp('{fromDate}','UTC') AND timestamp < from_utc_timestamp('{toDate}','UTC') AND timestamp IS NOT NULL AND enduserids._experience.aaid.id IS NOT NULL GROUP BY Day ORDER BY Day;
- In Adobe Analytics Data feeds , generate feed files for the desired date range. Count the number of rows within each file, identifying and excluding the following rows: exclude_hit is not 0 (Data excluded from Analysis Workspace in both products) hit_source is 0 , 3 , 5 , 7 , 8 , 9 , or 10 (Data Sources and other non-hit data) page_event is 53 or 63 (Streaming Media keep-alive hits) Rows matching any of the above criteria are excluded from the Analytics Source Connector ingestion workflow, and therefore should also be excluded when counting data feed rows.
- The total records in Query Services should match the number of rows in a data feed for the same time period.

recommendation-more-help
