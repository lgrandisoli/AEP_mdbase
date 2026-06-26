---
title: "Bad IDs"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/technotes/badids"
category: "other"
topic: "analytics-platform/using/technotes/badids"
created_at: "2026-06-23T20:44:38.068346+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Bad IDs

Last update: June 5, 2026
- Topics:
- [Administration](#)

CREATED FOR:

- Admin

This article provides context on Bad IDs and how to detect their presence or risk of occurrence in your data, using Query Service.

INFO
Bad IDs are also referred to as BAVIDs in the Customer Journey Analytics interface (originating from
Analytics BAVID
).
## Definition

In Customer Journey Analytics, as part of all data defined in a connection, a Bad ID is an identifier:

- with a specific ID value that originates from a person ID field (non-stitched datasets), or from a persistent ID or a person ID field (stitching-enabled datasets), and
- is on more than one million (1,000,000) events in the connection data (counted for all datasets within the connection), within a month.

When an ID value is marked as a Bad ID, any future events that contain that ID value are discarded from the connection data and do not show up in the reporting.

### Example

An example of a Bad IDs scenario is that you have custom or placeholder values in the person ID field (for example, undefinedfor anonymous traffic). For a stitching-enabled dataset, this situation can have even greater impact on the reporting data since the stitching quality is most likely affected. To solve this, you might need to clear and re-enable the stitching setup, including deleting historical data of datasets in the connection.

## Metrics

The Customer Journey Analytics Connection interface offers **Bad IDs** metrics information at several places in the interface.

- You can see **Bad IDs** (or **BAVIDs**) as possible reasons for skipping records in the **Check skipped details** dialog. Use **Check detail** (if available) below **Records skipped** in the [detail screen of a connection](/en/docs/analytics-platform/using/cja-connections/create-connection).
- For a stitching enabled dataset, the **Dataset preview** shows **Bad IDs** as part of the **Stitching metrics**. This metric can help you identity possible Bad IDs cases. However, be aware that this metric is calculated based on a limited set of data.

Refer to [Bad IDs exposure](#bad-ids-exposure) to help you identify Bad IDs presence for a dataset that you plan to use within a connection (regardless if stitching-enabled or not).

## Exposure

To investigate Bad IDs exposure for a certain dataset field, consider performing the following query in Experience Platform Query Service. Check the top returned ID values to see if there are any candidates for Bad IDs. Be aware that the [Bad ID definition](#definition) takes into account all datasets within the connection.

### Identify (risk of) Bad IDs within a field

You can use Experience Platform Query to service to identify the potential risk of Bad IDs within a field.

The query below returns the first 20 ID values from a field. In descending order by count of total events. And where each value is detected within a certain interval (for example within the last 30 days).

Run this query for a specific person ID field that you want to analyze. For a dataset that needs stitching, you can also run the query for a persistent ID field.

```
SELECT
    /* INSERT FIELD HERE */,
    COUNT(*) AS occurrences
FROM /* INSERT DATASET TABLE NAME HERE */
WHERE timestamp >= NOW() - INTERVAL '30 days'
GROUP BY /* INSERT FIELD HERE */
ORDER BY occurrences DESC
LIMIT 20;
```

In the query, replace INSERT FIELD HERE depending on the type of the field that you investigate for Bad IDs:

- full.field.path.from.XDM.schema (for string fields defined in XDM schema)
- identityMap['namespace_value'][0].id (for fields defined with namespace_value in identityMap)

Check the results to see if there are problematic ID values. Like custom or placeholder values, or values with high occurrence that gets or could get close to 1 million within a month at the connection data level.Even if your implementation is still in the development phase, you should assess the risk of Bad IDs presence once the setup is stable and ready for production.

recommendation-more-help
