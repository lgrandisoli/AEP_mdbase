---
title: "Graph-based stitching"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/stitching/gbs"
category: "other"
topic: "analytics-platform/using/stitching/gbs"
created_at: "2026-06-23T20:44:41.799550+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Graph-based stitching

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Data management](#)

CREATED FOR:

- Admin

In graph-based stitching, you specify an event dataset, the persistent ID (cookie) for that dataset and the desired person ID namespace from the identity graph. Graph-based stitching attempts to make the person ID info available for Customer Journey Analytics data analysis on any event. The persistent ID is used to query the identity graph from the Experience Platform Identity Service to obtain the person ID from the specified namespace.

If the person ID info cannot be retrieved for an event, the persistent ID is used instead for that *unstitched* event. As a result, in a [data view](/en/docs/analytics-platform/using/cja-dataviews/data-views) that is associated with a [connection](/en/docs/analytics-platform/using/cja-connections/overview) that contains the dataset enabled for stitching, the person ID data view component contains either the person ID value or persistent ID value at the event level.

## IdentityMap

Graph-based stitching supports the use of the [identityMap field group](/en/docs/experience-platform/xdm/schema/composition#identity) in the following scenarios:

- Use of the primary identity in identityMap namespaces to define the persistentID: If multiple primary identities are found in different namespaces, the identities in the namespaces are sorted lexicographically, and the first identity is selected. If multiple primary identities are found in a single namespace, the first lexicographical available primary identity is selected. In the example below, the namespaces and identities result in a sorted primary identities list, and finally the selected identity. table 0-row-2 1-row-2 2-row-2 layout-auto html-authored Namespaces Identities list ECID code language-none [ {"id": "ecid-3"}, {"id": "ecid-2", "primary": true}, {"id": "ecid-1", "primary": true} ] CCID code language-none [ {"id": "ccid-1"}, {"id": "ccid-2", "primary": true} ] table 0-row-2 1-row-2 layout-auto html-authored Sorted identities list Selected identity code language-none PrimaryIdentities [ {"id": "ccid-2", "namespace": "CCID"}, {"id": "ecid-1", "namespace": "ECID"}, {"id": "ecid-2", "namespace": "ECID"} ] NonPrimaryIdentities [ {"id": "ccid-1", "namespace": "CCID"}, {"id": "ecid-3", "namespace": "ECID"} ] code language-none "id": "ccid-2", "namespace": "CCID"
- Use of identityMap namespace to define the persistentID: If multiple values for persistentID are found in an identityMap namespace, the first lexicographical available identity is used. In the example below, you have selected ECID as the namespace to use. That selection results in a sorted identities list, and finally the selected identity. table 0-row-2 1-row-2 2-row-2 layout-auto html-authored Namespaces Identities list ECID code language-none [ {"id": "ecid-3"}, {"id": "ecid-2", "primary": true}, {"id": "ecid-1", "primary": true} ] CCID code language-none [ {"id": "ccid-1"}, {"id": "ccid-2", "primary": true} ] table 0-row-2 1-row-2 layout-auto html-authored Sorted identities list Selected identity code language-none [ "id": "ecid-1", "id": "ecid-2", "id": "ecid-3" ] code language-none "id": "ecid-1", "namespace": "ECID"

## How graph-based stitching works

Stitching makes a minimum of two passes on data in a given dataset.

- Live stitching : attempts to stitch each hit (event) as it comes in, using the persistent ID to look up the person ID for the selected namespace by querying the identity graph. If the person ID is available from the lookup, this person ID is immediately stitched.
- Replay stitching : replays data based on updated identities from the identity graph. This stage is where hits from previously unknown devices (persistent IDs) become stitched as the identity graph has resolved the identity for a namespace. Two parameters determine the replay: frequency and lookback window . Adobe offers the following combinations of these parameters: Daily lookback on a daily frequency : Data replays every day with a 24-hour lookback window. This option holds an advantage that replays are much more frequent, but unauthenticated profiles must authenticate the same day that they visit your site. Weekly lookback on a weekly frequency : Data replays once a week with a weekly lookback window (see options ). This option holds an advantage that allows unauthenticated sessions a much more lenient time to authenticate. However, unstitched data less than a week old is not reprocessed until the next weekly replay. Biweekly lookback on a weekly frequency : Data replays once every week with a biweekly lookback window (see options ). This option holds an advantage that allows unauthenticated sessions a much more lenient time to authenticate. However, unstitched data less than two weeks old is not reprocessed until the next weekly replay. Monthly lookback on a weekly frequency : Data replays every week with a monthly lookback window (see options ). This option holds an advantage that allows unauthenticated sessions a much more lenient time to authenticate. However, unstitched data less than a month old is not reprocessed until the next weekly replay.
- Privacy : When privacy-related requests are received, in addition to removing the requested identity from the source dataset, any stitching of that identity across unauthenticated events must be undone. Also, the identity must be removed from the identity graph to prevent future graph-based stitching for that specific identity. note important IMPORTANT The unstitching process, as part of privacy requests, changes at the start of 2025. The current unstitching process restitches events using the latest version of known identities. This reassignment of events to another identity might have undesirable legal consequences. To remedy these concerns, from 2025 on, the new unstitching process updates events that are subject of the privacy request with the persistent ID.

Data beyond the lookback window is not replayed. A profile must be authenticated within a given lookback window for an unauthenticated visit and an authenticated visit to be identified together. Once a device is recognized, it is live stitched from that point forward.

Consider the following two identity graph updates over time for visitor A (with persistent ID 246) and visitor B (with persistent ID 3579), and how these updates impact the steps in graph-based stitching.

You can view an identity graph over time for a specific profile using the [Identity Graph Viewer](/en/docs/experience-platform/identity/features/identity-graph-viewer). See also [Identity Service linking logic](/en/docs/experience-platform/identity/features/identity-linking-logic) to get a better understanding of the logic used when linking identities.

### Step 1: Live stitching

Live stitching attempts to stitch each event, upon collection, to known information at that time from the identity graph.

Details
| table 0-row-5 1-row-5 2-row-5 3-row-5 4-row-5 5-row-5 6-row-5 7-row-5 1-align-right 7-align-right 13-align-right 19-align-right 25-align-right 31-align-right 37-align-right 43-align-right layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Time | Persistent IDECID | NamespaceEmail | Resulting ID (after live stitch) |
| 1 | 2023-05-12 11:00 | 246 | 246 *undefined* | 246 |
| 2 | 2023-05-12 14:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com |
| 3 | 2023-05-12 15:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com |
| 4 | 2023-05-12 17:00 | 3579 | 3579 *undefined* | 3579 |
| 5 | 2023-05-12 19:00 | 3579 | 3579 ted.w@gmail.com | ted.w@gmail.com |
| 6 | 2023-05-13 15:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com |
| 7 | 2023-05-13 16:30 | 246 | 246 a.b@yahoo.co.uk246 bob.ab@gmail.com | a.b@yahoo.co.uk |

You can see how for each event the resulting ID is resolved. Based on the time, the persistent ID, and the lookup of the identity graph for the specified person ID namespace.When the lookup resolves to more than one resulting ID (like for event 7), the lexicographic first id returned by the identity graph is selected (a.b@yahoo.co.uk in the example).

### Step 2: Replay stitching

At regular intervals (depending on the chosen lookback window), replay stitching recalculates historical data based on the most recent version of the identity graph, at the time of the interval.

Details
With a replay stitching happening at 2023-05-13 16:30, with a 24-hour lookback window configuration, some events from the sample are re-stitched (indicated by ).

| table 0-row-6 1-row-6 2-row-6 3-row-6 4-row-6 5-row-6 6-row-6 layout-auto |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Time | Persistent IDECID | NamespaceEmail | Resulting ID(after live stitch) | Resulting ID(after replay 24 hours) |
| 2 | 2023-05-12 14:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com | bob.a@gmail.com |
| 3 | 2023-05-12 15:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com | bob.a@gmail.com |
| 4 | 2023-05-12 17:00 | 3579 | 3579 ted.w@gmail.com | 3579 | ted.w@gmail.com |
| 5 | 2023-05-12 19:00 | 3579 | 3579 ted.w@gmail.com | ted.w@gmail.com | ted.w@gmail.com |
| 6 | 2023-05-13 15:00 | 246 | 246 a.b@yahoo.co.uk | bob.a@gmail.com | a.b@yahoo.co.uk |
| 7 | 2023-05-13 16:30 | 246 | 246 a.b@yahoo.co.uk246 bob.ab@gmail.com | a.b@yahoo.co.uk | a.b@yahoo.co.uk |

With replay stitching happening at 2023-05-13 16:30, with a 7-day lookback window configuration, all events from the sample are re-stitched.

| table 0-row-6 1-row-6 2-row-6 3-row-6 4-row-6 5-row-6 6-row-6 7-row-6 layout-auto |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Time | Persistent IDECID | NamespaceEmail | Resulting ID(after live stitch) | Resulting ID(after replay 7 days) |
| 1 | 2023-05-12 11:00 | 246 | 246 *undefined* | 246 | a.b@yahoo.co.uk |
| 2 | 2023-05-12 14:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com | a.b@yahoo.co.uk |
| 3 | 2023-05-12 15:00 | 246 | 246 bob.a@gmail.com | bob.a@gmail.com | a.b@yahoo.co.uk |
| 4 | 2023-05-12 17:00 | 3579 | 3579 ted.w@gmail.com | 3579 | ted.w@gmail.com |
| 5 | 2023-05-12 19:00 | 3579 | 3579 ted.w@gmail.com | ted.w@gmail.com | ted.w@gmail.com |
| 6 | 2023-05-13 15:00 | 246 | 246 a.b@yahoo.co.uk | bob.a@gmail.com | a.b@yahoo.co.uk |
| 7 | 2023-05-13 16:30 | 246 | 246 a.b@yahoo.co.uk246 bob.ab@gmail.com | a.b@yahoo.co.uk | a.b@yahoo.co.uk |

### Step 3: Privacy Request

When you receive a privacy request, the resulting ID is deleted in all records for the user subject of the privacy request.

Details
The following table represents the same data as above, but shows the effect that a privacy request (for example at 2023-05-13 18:00) has for the sample events.

| table 0-row-5 1-row-5 2-row-5 3-row-5 4-row-5 5-row-5 6-row-5 7-row-5 1-align-right 7-align-right 13-align-right 19-align-right 25-align-right 31-align-right 37-align-right 43-align-right layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Time | Persistent IDECID | NamespaceEmail | Resulting ID (after privacy request) |
| 1 | 2023-05-12 11:00 | 246 | 246 a.b@yahoo.co.uk | 246 |
| 2 | 2023-05-12 14:00 | 246 | 246 a.b@yahoo.co.uk | 246 |
| 3 | 2023-05-12 15:00 | 246 | 246 a.b@yahoo.co.uk | 246 |
| 4 | 2023-05-12 17:00 | 3579 | 3579 ted.w@gmail.com | 3579 |
| 5 | 2023-05-12 19:00 | 3579 | 3579 ted.w@gmail.com | 3579 |
| 6 | 2023-05-13 15:00 | 246 | 246 a.b@yahoo.co.uk | 246 |
| 7 | 2023-05-13 16:30 | 246 | 246 a.b@yahoo.co.uk246 bob.ab@gmail.com | 246 |

## Prerequisites

The following prerequisites apply specifically to graph-based stitching:

- The event dataset in Adobe Experience Platform, to which you want to apply stitching, must have one column that identifies a profile on every row, the persistent ID . For example, a visitor ID generated by an Adobe Analytics AppMeasurement library or an ECID generated by the Experience Platform Identity Service.
- The identity graph from Experience Platform Identity Service must be set up at sandbox level, prior to enabling Graph-based stitching. The identity graph must have a namespace (for example Email , or Phone ) that you want to use during stitching to resolve the person ID. The identity graph must be populated with identities info from any relevant datasets (of type event or profile and that contain at least two useful namespaces with ID values). All datasets that hold such relevant identities must be enabled for identity graph data ingestion . This enablement assures that incoming identities are added to the graph over time from all needed sources. If already using Real-Time Customer Data Profile or Adobe Journey Optimizer for a while, the graph should be already set up to a certain extent. If historical stitching backfill is also required for the dataset enabled with graph-based stitching, the graph should already contain historical identities for the entire period, to obtain desired stitching results.
- If you want to use graph-based stitching and you anticipate the event dataset to contribute to the identity graph, you should enable the dataset for the Identity service .
- The persistent ID and person ID can be used with identityMap . Or the persistent ID and person ID can be fields from the XDM schema, in which case the fields must be defined as an identity in the schema.

NOTE
You do
not
require a Real-time Customer Data Platform license for graph-based stitching. The
Prime
package or higher of Customer Journey Analytics includes the required Experience Platform Identity Service entitlements.
## Limitations

The following limitations apply specifically to graph-based stitching:

- Timestamps are not taken into account when querying for the person ID using the specified namespace. So, it is possible that a persistent ID is stitched with a person ID from a record that has an earlier timestamp.
- In shared device scenarios, where the namespace in the graph contains multiple identities, the first lexicographic identity is used. If namespace limits and priorities are configured as part of the release of graph-linking rules, the last authenticated user’s identity is used. See Shared devices for more information.
- There is a hard limit of three months of backfilling identities into the identity graph. You would use backfilling identities in case you are not using an Experience Platform application, like Real-time Customer Data Platform, to populate the identity graph.
- The Identity Service guardrails apply. See, for example, the following static limits : Maximum number of identities in a graph: 50. Maximum number of links to an identity for a single batch ingestion: 50. Maximum number of identities in an XDM record for graph ingestion: 20. Minimum number of identities in an XDM record for graph ingestion: 2.

recommendation-more-help
