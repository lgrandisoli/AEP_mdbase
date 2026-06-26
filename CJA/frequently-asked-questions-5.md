---
title: "Frequently asked questions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-faq"
category: "overview"
topic: "analytics-platform/using/cja-overview/cja-faq"
created_at: "2026-06-02T19:07:20.618681+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Frequently asked questions

Last update: May 12, 2026
- Topics:
- [FAQ](#)

CREATED FOR:

- User

Adobe Customer Journey Analytics is the next-generation analytics product. This article provides answers to frequently asked questions about Customer Journey Analytics. For more information, review [Customer Journey Analytics feature support](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/cja-aa).

## 1. Prerequisites prerequisites

Do I need Private Device Graph or Device Coop for Customer Journey Analytics?
No, Private Device Graph or Device Coop are not required for Customer Journey Analytics. In fact, they are not yet supported.
Do I need Experience Cloud ID (ECID) for Customer Journey Analytics?
No, Customer Journey Analytics supports any ID in a dataset, whether that’s ECID or any other ID you choose.
What if I need to ETL (Extract, Transform, Load) my data prior to Customer Journey Analytics?
Customer Journey Analytics includes
Data Prep
capabilities to help transform your data before putting it into the Adobe Experience Platform data lake. If you need ETL after the data has already been ingested,
Adobe Experience Platform Query Service
provides some limited options, although there may be extra fees involved.
## 2. Stitching data stitching

Can Customer Journey Analytics "stitch" across devices or across datasets?
Yes. Customer Journey Analytics has
Stitching
functionality that works across authenticated and unauthenticated events within a dataset. This stitching allows for resolving disparate records to a single stitched ID, for cross-device analysis at the person level.
Furthermore, when a common namespace ID (Person ID) is used across datasets within a
Connection
, you are able to run analysis on a seamless combination of multiple datasets, “stitched” at the person level.
Is stitching from anonymous behavior to authenticated behavior supported?
Yes.
Stitching
looks at user data from both authenticated and unauthenticated sessions to generate a stitched ID.
How does 'replay' work in stitching?
Stitching “replays” data based on unique identifiers it has learned. Replay is aiming to stitch initially unauthenticated events from devices that have been identified in the meantime.
Learn more
How does stitching historical data (backfill) work?
When first turned on, Adobe provides a backfill of stitched data that goes back as far as selected by you (up to a maximum of 25 months, depending on the Customer Journey Analytics package you are entitled to). In order to do this backfill, the transient ID must exist in the unstitched data that far back in time.
Learn more
What is the expected behavior for non-stitched profile data set records?
**Example scenario**: You join two datasets in a Customer Journey Analytics connection by using CRMid as the Person ID. One is a Web Event dataset with CRMid in all records. The other dataset is a CRM profile data set. 40% of the CRM data set has CRMid present in the Web event data set. The other 60% are not present in the Web event dataset - do these records appear in reporting in Analysis Workspace?

**Answer**: Profile rows that have no events tied to them are stored in Customer Journey Analytics. However, you cannot view them in Analysis Workspace until an event tied to that ID appears.

## 3. Getting data into Customer Journey Analytics ingest

Can I combine data from different Adobe Experience Platform sandboxes in one Customer Journey Analytics connection?
No, you cannot access data across sandboxes. You can combine only datasets that are located within the same sandbox.
Learn more
How do I connect online data to offline data in Customer Journey Analytics?
As long as the person ID matches between datasets, Customer Journey Analytics can connect segments, attribution, flow, fallout, and so on across datasets.
How do I bring my offline data into Customer Journey Analytics?
Your entitlement to Customer Journey Analytics allows you to ingest data into Experience Platform. You can then create connections to that data and data views in Customer Journey Analytics, for reporting in Analysis Workspace. The Experience Platform’s data on-boarding team can help provide recommendations or consulting for you, if needed.
How do I get Adobe Analytics data into Customer Journey Analytics?
Adobe Analytics data can be connected to Experience Platform through the
Analytics source connector
. Most Adobe Analytics fields are brought over in XDM format, but other fields are not yet available.
How long does it take to assemble dataset elements into a data view?
A few hours to get started, and a few days to backfill the last 13 months of data.
Is it necessary to bring PII data to establish connections between the data?
No, you can use any ID, including a hash of a customer ID, which is not PII.
What are the limits for ingesting past or future dates/timestamps into Customer Journey Analytics event datasets?
- Regarding past dates/timestamps: Event data up to ten years old.
- Regarding future dates/timestamps: Event data (predictive) up to one month in the future.

## 4. Latency considerations latency

NOTE
There is no fixed data size in Customer Journey Analytics and thus Adobe cannot commit to a standard ingestion time. Adobe is actively working to reduce these latencies through new updates and ingestion optimization.
- Live data or events: Processed and ingested within 90 minutes, once data is available in Adobe Experience Platform. (Batch size > 50 million rows: longer than 90 mins.) If stitching is enabled, ingestion may take up to 4 hours. See [guardrails](/en/docs/analytics-platform/using/technotes/guardrails) for more details.
- Small backfills: within seven days
- Large backfills: within 30 days

Adobe recently changed how it processes data in Customer Journey Analytics:

- Event data for the ‘current’ day is streamed in as live data. Any data with an event time prior to 11:59:59 pm(23:59:59) on the previous day is treated as a backfill.
- Any event data with a timestamp more than 24 hours old (even if it’s in the same batch as newer data) is considered backfill and is ingested at a lower priority.

## 5. Set rolling window for Connection data retention data-retention

The [Enable rolling data window setting](/en/docs/analytics-platform/using/cja-connections/create-connection#create-connection) lets you define Customer Journey Analytics data retention as a rolling window in months (three months, six months, and so on). It is set at a connection level, not at a dataset level. Data retention is based on event dataset timestamps and applies to event datasets only. No data retention setting exists for profile or lookup datasets since there are no applicable timestamps.

The main benefit is that you store or report only on data that is applicable and useful and delete older data that is no longer useful. It helps you stay under your contract limits and reduces the risk of overage cost.

## 6. Implications of deleting objects or components deletion

See [Deletion and reset implications](/en/docs/analytics-platform/using/technotes/deletion) for an overview of the implications when you delete or reset Customer Journey Analytics or Experience Platform objects or components.

## 7. Considerations when merging report suites in Customer Journey Analytics merge-reportsuite

If you plan to ingest Adobe Analytics data through the [Adobe Analytics source connector](/en/docs/experience-platform/sources/connectors/adobe-applications/analytics), consider these ramifications when merging two or more Adobe Analytics report suites.

Issue
Consideration
Variables
Variables such as eVars may not line up across report suites. For example, eVar1 in report suite 1 may point to
Page
. In report suite 2, eVar1 may point to
Internal Campaign
, leading to mixed and inaccurate reporting.
Sessions and People counts
They get deduplicated across report suites. As a result, counts may not match.
Metric deduplication
Deduplicates instances of a metric (for example, Orders) if multiple rows have the same transaction ID (for example, Purchase ID). This prevents over-counting of key metrics. As a result, metrics like Orders may not add up across report suites.
Currency
Currency conversion is not yet supported in Customer Journey Analytics. If the report suites you are trying to merge use different base currencies, problems may arise.
Persistence
Persistence
extends across report suites, which impacts segments, attribution, and so on. Numbers may not add up properly.
Classifications
Classifications do not automatically get deduplicated when merging report suites. When combining multiple classifications files into a single lookup dataset, you could encounter problems.
## 8. Adobe Analytics components

Can I share/publish audiences from Customer Journey Analytics to Experience Platform Real-Time CDP, or other CX Enterprise applications?
You can
create and publish audiences
identified in Customer Journey Analytics to Real-time Customer Profile in Adobe Experience Platform for customer targeting and personalization.
What happened to my old eVar setting?
eVars, props, and events in the Adobe Analytics sense no longer exist in Customer Journey Analytics. You have unlimited schema elements (dimensions, metrics, list fields). So all attribution settings you used to apply during the data collection process are now applied at query time.
Where are all my session and variable persistence settings now?
Customer Journey Analytics applies all of these settings at report time, and these settings now live in data views. Changes to these settings are now retroactive, and you can have multiple versions by using multiple data views!
What happens to your existing segments/calculated metrics?
Customer Journey Analytics no longer uses eVars, props, or events and instead uses any Adobe Experience Platform schema. This means none of the existing segments or calculated metrics are compatible with Customer Journey Analytics.
How does Customer Journey Analytics handle
Uniques Exceeded
limitations?
Customer Journey Analytics has no unique value limitations, so no need to worry about them!
If I am an existing Data Workbench customer, can I move to Customer Journey Analytics right now?
It depends on your use case, so work with your Adobe Account team. Your current use case may already be a good fit for Customer Journey Analytics!
## 9. Estimate connection size estimate-size

See [Connections usage](/en/docs/analytics-platform/using/cja-connections/manage-connections#usage).

## 10. Regarding usage overages overage

Usage limits are regularly monitored and enforced by Adobe. “Rows of data” means the daily average rows of data available for analysis within Customer Journey Analytics.

For example, your contract entitles you to one million rows of data. Suppose that on day 1 of using Customer Journey Analytics, you upload two million rows of data. On day 2, you delete 1 million rows and keep your usage at that committed maximum (that is, one million rows of data) for the remainder of your License Term. Depending on your contractual terms, you may still incur prorated over-usage fees for day 1, since you exceeded your “rows of data” license entitlement.

## 11. Diagnose data discrepancies discrepancies

Sometimes, you may notice that the total number of events ingested by your connection is different from the number of rows in the dataset in Adobe Experience Platform. In this example, the dataset “B2B Impression” has 7650 rows, but the dataset contains 3830 rows in Adobe Experience Platform. There are several reasons why discrepancies can happen, and the following steps can be taken to diagnose:

- Break down this dimension by Platform Dataset ID and you notice two datasets with the same size but different Platform Dataset IDs . Each dataset has 3825 records. That means Customer Journey Analytics ignored five records due to missing person IDs or missing timestamps:
- In addition, if you check in Adobe Experience Platform, there is no dataset with Id “5f21c12b732044194bffc1d0”, hence someone deleted this particular dataset from Adobe Experience Platform when the initial connection was created. Later, it got added to Customer Journey Analytics again, but a different Platform Dataset ID was generated by Adobe Experience Platform.

Read more about the [implications of dataset and connection deletion](/en/docs/analytics-platform/using/cja-overview/cja-faq#implications-of-deleting-data-components) in Customer Journey Analytics and Adobe Experience Platform.

## 12. Regional data collection

Adobe CX Enterprise uses Regional Data Collection (RDC) so that interactions between your visitors and Adobe and non-Adbobe solutions occur as close to your visitors as possible. Once data is collected regionally at a Data Collection Center (DCC, also known as Edge site, part of the Platform Edge Network), it is forwarded over a secure connection to the relevant solutions based on the configuration of your datastream and/or event forwarding.

The regional data collection process uses the following steps:

- DNS automatically resolves the collection hostname to the IP address of the Data Collection Center nearest to the visitor.
- The visitor sends the data to that location.
- The data is immediately forwarded over a secure connection to the solutions defined by the datastream or event forwarding configuration.

Using regional data collection provides several benefits:

- **Performance**: With RDC, your visitors connect to the closest DCC. This optimization provides the fastest response time, resulting in more accurate tracking and faster loading times.
- **Redundancy**: If there is a disruption in communication between the DCC and your DPC, Adobe’s RDC infrastructure saves data locally, then forwards it to the DPC when communications are restored.

RDC currently includes the following locations (subject to change):

RDC Type
Data Collection Centers
Global (Default)
Oregon, Virginia, Ireland, Paris, Mumbai, Singapore, Tokyo, Sydney
Americas Only
Oregon, Virginia
Europe Only
Ireland, Paris
Asia Pacific Only
Mumbai, Singapore, Tokyo, Sydney
When the data hits the regional data center, the datastream configuration determines how data is routed further.

Customer Journey Analytics requires datasets from Adobe Experience Platform, so your datastream / event forwarding configuration requires the Adobe Experience Platform service to route the data from the regional data center to the data center where your Adobe Experience Platform instance is located. Customer Journey Analytics and its supporting services and infrastructure are deployed at that same Adobe Experience Platform instance.

See [Data collection overview](/en/docs/experience-platform/collection/home) for more information about the process of data collection beyond the Adobe Experience Platform Edge Network and its regional data centers.

recommendation-more-help
