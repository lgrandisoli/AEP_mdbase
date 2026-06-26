---
title: "Enable stitching"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/stitching/use-stitching-ui"
category: "other"
topic: "analytics-platform/using/stitching/use-stitching-ui"
created_at: "2026-06-23T20:42:21.982147+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Enable stitching

Last update: May 13, 2026
- Topics:
- [Stitching](#)
- [Cross-Channel Analysis](#)

CREATED FOR:

- Admin

You can enable stitching on one or more event datasets you have configured as part of your connection. The Customer Journey Analytics package that you have licensed determines the number of event datasets you can enable for stitching.

You enable stitching as part of the [dataset settings](/en/docs/analytics-platform/using/cja-connections/create-connection#dataset-settings) for an event dataset when you [create a connection](/en/docs/analytics-platform/using/cja-connections/create-connection) or when you [edit a connection](/en/docs/analytics-platform/using/cja-connections/manage-connections#edit-a-connection).

## Prerequisites

You need to check and meet the prerequisites for the stitching method you specify: [field-based stitching](/en/docs/analytics-platform/using/stitching/fbs#prerequisites) or [graph-based stitching](/en/docs/analytics-platform/using/stitching/gbs#prerequisites).

## Preflight checks

If you meet the prerequisites, you might want to perform some preflight checks on the data in the event dataset before you enable identity stitching:

- If you are going to use Experience Data Model (XDM) schema fields for persistent ID or person ID, ensure that identities are marked properly in the schema for the event dataset. See Identity namespace overview .
- Verify identity coverage for both persistent ID and person ID: Persistent ID Query 7 days of data where your persistent ID field is not null and divide by a query of 7 days of data for all events in your dataset. This percentage should be above 95%. Example of a query you could use for verification: code language-sql SELECT COUNT(*) AS total_events, COUNT({PERSISTENT_ID_FIELD}) AS events_with_persistentid, ROUND(COUNT({PERSISTENT_ID_FIELD}) / COUNT(*), 2) AS percent_with_persistentid_not_null FROM {DATASET_TABLE_NAME} WHERE TO_TIMESTAMP(timestamp, '{FORMAT_STRING}') >= TIMESTAMP '{START_DATE}' AND TO_TIMESTAMP(timestamp, 'FORMAT_STRING') < TIMESTAMP '{END_DATE}'; Where: {PERSISTENT_ID_FIELD} is the field for the persistent ID. For example: identityMap.ecid[0] . {DATASET_TABLE_NAME} is the table name for the event dataset. {FORMAT_STRING} is the format string for the timestamp field. For example: MM/DD/YY HH12:MI AM . {START_DATE} is the start date. For example: 2024-01-01 00:00:00 . {END_DATE} is the end date in standard format. For example: 2024-01-08 00:00:00 . Person ID For graph-based stitching, ensure that the identity graph contains fragments that link ID values from your chosen persistent ID namespace and person ID namespace. You could run a test by going to the Experience Platform Identity graph viewer and query the graph by some sample persistent ID values. Verify to see if these persistent ID values are linked to person ID values in the graph. For field-based stitching, query 7 days of data where your person ID field is not null and divide by a query of 7 days of data for all events in your dataset. This percentage should ideally above 5%. Example of a query you could use for verification: code language-sql SELECT COUNT(*) AS total_events, COUNT({PERSON_ID_FIELD}) AS events_with_personid, ROUND(COUNT({PERSON_ID_FIELD}) / COUNT(*), 2) AS percent_with_personid_not_null FROM {DATASET_TABLE_NAME} WHERE TO_TIMESTAMP(timestamp, '{FORMAT_STRING}') >= TIMESTAMP '{START_DATE}' AND TO_TIMESTAMP(timestamp, 'FORMAT_STRING') < TIMESTAMP '{END_DATE}'; Where: {PERSON_ID_FIELD} is the field for the person ID. For example: identityMap.crmId[0] . {DATASET_TABLE_NAME} is the table name for the event dataset. {FORMAT_STRING} is the format string for the timestamp field. For example: MM/DD/YY HH12:MI AM . {START_DATE} is the start date. For example: 2024-01-01 00:00:00 . {END_DATE} is the end date in standard format. For example: 2024-01-08 00:00:00 .

## Enable identity stitching enable-identity-stitching

You can enable identity stitching when you [add](/en/docs/analytics-platform/using/cja-connections/create-connection#add-datasets) or [edit](/en/docs/analytics-platform/using/cja-connections/create-connection#edit-a-dataset) an event dataset in a person-based connection. Identity stitching is not available for account-based connections.

### Dataset settings

To enable stitching, in the event dataset **Datasets settings** section of the **Add datasets** or **Edit dataset** dialog.

- Select Enable identity stitching . If you enable or disable stitching for a saved event dataset in the connection, the Change Person ID dialog displays the implications of a change of the person ID. Select Continue to continue. The Enable identity stitching dialog summarizes the consequences of stitching identities. Select Continue to continue.
- Select a persistent ID from the Persistent ID drop-down menu. If you select Identity Map for the persistent ID, select a namespace. You have two options: Select Use primary identity namespace to use the primary identity namespace. Select a namespace from the Namespace drop-down menu.
- Select a person ID from the Person ID drop-down menu. If you select Identity Map for the person ID, select a namespace. You have two options: Select Use primary identity namespace to use the primary identity namespace. Select a namespace from the Namespace drop-down menu. If you select Identity Graph for the person ID (to use graph-based stitching ), you have to select a namespace. note NOTE Ensure that you are entitled to use the identity graph. Before that, a Change to identity graph dialog is displayed to ensure you have finished the setup of the identity graph for the dataset. This setup is part of the graph-based prerequisites before you can use the identity graph for stitching. Select Continue to continue. Select a namespace from the Namespace drop-down menu.
- Select a replay window from the Replay window drop-down menu. The available options are dependent on the Customer Journey Analytics package that you are entitled to.
- Select Next to see a preview of the event dataset subject to stitching.

### Datasets preview

On top of the standard **Datasets preview** interface, when [adding](/en/docs/analytics-platform/using/cja-connections/create-connection#add-datasets) or [editing](/en/docs/analytics-platform/using/cja-connections/create-connection#edit-a-dataset) datasets in a person-based connection, two additional information panels are available.

#### Stitching metrics

AVAILABILITY
Stitching metrics are not available for graph-based stitching.
**Stitching metrics** are calculated using a sample set of data with event timestamps from the last 7 days. This sample set of data usually differs from the sample data used in the **Preview** table. Stitching metrics provide details for:

- Person ID coverage : The coverage of the selected person ID used for identification during the stitching process (live and replay). For the best field-based stitching results, a person ID (user info) should be sent on at least one event for each persistent ID (device info). For the best graph-based stitching results, a (persistent ID, person ID) relation should be present in the identity graph for each persistent ID. Person ID coverage is shown as a percentage and compared to what is recommended on a stable development or on a production setup. The higher this coverage value is, the better stitching results are obtained with the selected person ID.
- Persistent ID coverage : This value is used for identification during the stitching process (live and replay), in case a person ID value cannot be detected. Events with no persistent ID and no person ID are dropped from the data. For best stitching results, a persistent ID should be present on all events. Persistent ID coverage is shown as a percentage and compared to what is the minimum recommended on a stable development or on a production setup.

#### Bad IDs

AVAILABILITY
Bad IDs are not available for graph-based stitching.
INFO
Bad IDs are also referred to as BAVIDs in the Customer Journey Analytics interface.
In Customer Journey Analytics, a Bad ID is an identifier:

- with a specific ID value that originates from either a persistent ID or a person ID field in stitching-enabled datasets, **and**
- is on more than one million (1,000,000) events in the connection data, within a month.

When an ID value is marked as a Bad ID, any future events that contain that ID value are discarded from the connection data and do not show up in the reporting.

Examples of Bad IDs use cases:

- You have custom or placeholder values in the person ID field (for example, undefined). Such values can also affect [stitching and reporting data quality](/en/docs/analytics-platform/using/stitching/faq#undefined-person-id-values).
- In a field-based stitching configuration, if multiple people share a device and the total number of transitions between users exceeds 50,000. In this scenario, the stitching process stops to use the person ID info for that device, and only uses persistent ID info instead. Consequently, all dataset events from that device are sent into connection data with the persistent ID identity, with a high chance of causing a Bad IDs situation.

NOTE
The
Stitching metrics
, including
Bad IDs
, are calculated based on a limited set of data. To identify Bad IDs presence for a dataset you plan to use for stitching, refer to the
Bad IDs technote
.
### Save

Once you save a connection, the stitching process for stitching enabled datasets is started as soon as the ingestion of data for these datasets starts.

CAUTION
For datasets that are enabled for stitching in the Connections interface, the backfill status is immediately and incorrectly reported as
x
backfills completed
for the number of backfills completed. Use other ways to verify whether data from the stitched dataset is backfilled.
## Limitations

On top of the [field-based stitching limitations](/en/docs/analytics-platform/using/stitching/fbs#limitations) and [graph-based stitching limitations](/en/docs/analytics-platform/using/stitching/gbs#limitations), the following limitations apply when you enable stitching in the Connections interface:

- You can only stitch an event dataset once as part of a single connection. You cannot define the same event dataset more than once and use a separate stitching configuration for each instance. If you want to apply different stitching configurations on the same dataset, use a separate connection for each configuration.

## Migration

Stitching enabled in the Connections interface can coexist without any issues with request-based stitching.

For example, you have web-based stitched datasets in the data lake as a result of earlier or current stitching requests. You can add stitched data from a call-center dataset using the Connections interface to combine that data with the web-based data.

Eventually, Adobe will migrate your request-based stitched datasets to the new stitching in connections experience.

recommendation-more-help
