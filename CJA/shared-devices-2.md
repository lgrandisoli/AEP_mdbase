---
title: "Shared devices"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/stitching/shared-devices"
category: "other"
topic: "analytics-platform/using/cja-usecases/stitching"
created_at: "2026-06-23T20:44:28.754246+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Shared devices

Last update: June 5, 2026
- Topics:
- [Data management](#)
- [Administration](#)

CREATED FOR:

- Admin

This article provides context on shared devices, how to handle and mitigate data from shared devices using [stitching](/en/docs/analytics-platform/using/stitching/overview), and understand shared device exposure in your data using Query Service.

## What is a shared device?

A shared device is a device that is used by more than one person. Common scenarios are devices like tablets, devices used in kiosks or computer equipment shared by agents in a call center.

When two people use the same device and both make an authenticated purchase, sample event data might look like:

Event
Timestamp
Page name
Device ID
Email
1
2023-05-12 12:01
Home page
1234
2
2023-05-12 12:02
Product page
1234
3
2023-05-12 12:03
Order success
1234
ryan@a.com
4
2023-05-12 12:07
Product page
1234
5
2023-05-12 12:08
Order success
1234
cassidy@a.com
As you can see from this table, once authentication happens on events 3 and 5, a link begins to form between a device id and a person id. To understand the impact of any marketing efforts on a person level, these unauthenticated events need to be attributed to the right person.

## Improve person centric analysis

The stitching process addresses this attribution problem by adding the selected person identifier (in the example data, the email) to events where that identifier does not exist. Stitching leverages a mapping between Device IDs and Person IDs to ensure that both authenticated and unauthenticated traffic can be used in analysis, keeping it person centric. See [Stitching](/en/docs/analytics-platform/using/stitching/overview) for more information.

Stitching can attribute shared device data using either last-auth attribution or device-split attribution. All attempts to stitch unauthenticated events to a known user are non-deterministic.

### Last-auth attribution

Last-auth attributes all unknown activity from a shared device to the user who last authenticated. The Experience Platform Identity Service builds the graph-based on the last-auth attribution and, as such, is used in graph-based stitching. See [Identity graph linking rules](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/identity-optimization-algorithm#identity-optimization-algorithm-details) for more information.

When last-auth attribution is used in stitching, Stitched IDs resolve as shown in the table below.

Timestamp
Page name
Device ID
Email
Stitched ID
2023-05-12 12:01
Home page
1234
cassidy@a.com
2023-05-12 12:02
Product page
1234
cassidy@a.com
2023-05-12 12:03
Order success
1234
ryan@a.com
cassidy@a.com
2023-05-12 12:07
Product page
1234
cassidy@a.com
2023-05-12 12:08
Order success
1234
cassidy@a.com
cassidy@a.com
2023-05-13 11:08
Home page
1234
cassidy@a.com
### Device-split

Device-split attributes anonymous activity from a shared device to the most recent known user, looking in the past. Device-split is currently used in field-based stitching.

When device-split attribution is used in stitching, Stitched IDs resolve as shown in the table below.

Timestamp
Page name
Device ID
Email
Stitched ID
2023-05-12 12:01
Home page
1234
ryan@a.com
2023-05-12 12:02
Product page
1234
ryan@a.com
2023-05-12 12:03
Order success
1234
ryan@a.com
ryan@a.com
2023-05-12 12:07
Product page
1234
ryan@a.com
2023-05-12 12:08
Order success
1234
cassidy@a.com
cassidy@a.com
2023-05-13 11:08
Home page
1234
cassidy@a.com
## Shared device exposure

Consider several factors to understand correctly how pervasive shared devices are in your organization. Additionally, understanding the overall contribution of events from shared devices can help you understand the impact on the overall event data used for analysis.

To understand the shared device exposure, you can think about performing the following queries.

- Identify shared devices To understand the number of devices that are shared, perform a query that counts the Device IDs with two or more Person IDs associated. This helps identify devices used by multiple individuals. code language-sql SELECT COUNT(*) FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, COUNT(DISTINCT /* INSERT TRANSIENT FIELD HERE */) AS transient_count FROM /* INSERT DATASET HERE */ GROUP BY 1 ) WHERE transient_count > 1;
- Attribution of events to shared devices For the shared devices identified, determine how many events out of the total can be attributed to these devices. This attribution provides insight into the impact shared devices have on your data and the implications for analysis. code language-sql SELECT COUNT(*) AS total_events, COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL, 1, null)) shared_persistent_ids_events, (COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL, 1, null)) / COUNT(*)) * 100 AS shared_persistent_ids_events_percent FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, /* INSERT TRANSIENT FIELD HERE */ AS transient_id FROM /* INSERT DATASET HERE */ ) events LEFT JOIN ( SELECT persistent_id FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, COUNT(DISTINCT /* INSERT TRANSIENT FIELD HERE */) AS transient_count FROM /* INSERT DATASET HERE */ GROUP BY 1 ) WHERE transient_count > 1 ) shared_persistent_ids ON events.persistent_id = shared_persistent_ids.persistent_id;
- Identify anonymous events on shared devices Among the events attributed to shared devices, identify how many lack a Person ID, indicating anonymous events. The algorithm you choose (for example last-auth, device-split, or ECID-reset) to enhance data quality affects these anonymous events. code language-sql SELECT COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL, 1, null)) shared_persistent_ids_events, COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL AND events.transient_id IS NULL, 1, null)) shared_persistent_ids_anon_events, (COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL AND events.transient_id IS NULL, 1, null)) / COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL, 1, null))) * 100 AS shared_persistent_ids_anon_events_percent FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, /* INSERT TRANSIENT FIELD HERE */ AS transient_id FROM /* INSERT DATASET HERE */ ) events LEFT JOIN ( SELECT persistent_id FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, COUNT(DISTINCT /* INSERT TRANSIENT FIELD HERE */) AS transient_count FROM /* INSERT DATASET HERE */ GROUP BY 1 ) WHERE transient_count > 1 ) shared_persistent_ids ON events.persistent_id = shared_persistent_ids.persistent_id;
- Calculate exposure from event misclassification Finally, assess the exposure each customer might face due to event misclassification. Calculate the percentage of anonymous events over the total events for each shared device. This helps understand the potential impact on customer data accuracy. code language-sql SELECT COUNT(*) AS total_events, COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL, 1, null)) shared_persistent_ids_events, (COUNT(IF(shared_persistent_ids.persistent_id IS NOT NULL AND events.transient_id IS NULL, 1, null)) / COUNT(*)) * 100 AS shared_persistent_ids_events_percent FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, /* INSERT TRANSIENT FIELD HERE */ AS transient_id FROM /* INSERT DATASET HERE */ ) events LEFT JOIN ( SELECT persistent_id FROM ( SELECT /* INSERT PERSISTENT FIELD HERE */ AS persistent_id, COUNT(DISTINCT /* INSERT TRANSIENT FIELD HERE */) AS transient_count FROM /* INSERT DATASET HERE */ GROUP BY 1 ) WHERE transient_count > 1 ) shared_persistent_ids ON events.persistent_id = shared_persistent_ids.persistent_id;

recommendation-more-help
