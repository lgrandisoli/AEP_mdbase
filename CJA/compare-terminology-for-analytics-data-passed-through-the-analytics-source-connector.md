---
title: "Compare terminology for Analytics data passed through the Analytics source connector"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/terminology"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/cja-aa-comparison"
created_at: "2026-06-02T19:04:54.790561+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Compare terminology for Analytics data passed through the Analytics source connector

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User

Some terminology differences exist between Adobe Analytics, Data Feeds, Analytics source connector/Data Lake, and Customer Journey Analytics. This topic aims to highlight and clarify those differences.

Related Terms
Adobe Analytics
Adobe Analytics Data Feeds
Analytics source connector/Data Lake
Customer Journey Analytics
Notes
- Hits
- Occurrences
- Records
- Events

**Occurrences** metricSee:

- [Terms used in Adobe Analytics](/en/docs/analytics/technotes/terms)
- [Occurrences](/en/docs/analytics/components/metrics/occurrences)

Count of rows (records) in the data feed file
Count of rows (records) in the datasetSee:

- [Compare your Adobe Analytics data to Customer Journey Analytics data](/en/docs/analytics-platform/using/troubleshooting/compare)

Events
metric
- “Hit” and “occurrence” are synonymous in Adobe Analytics.
- See *Custom Events* below.
- Certain data is filtered as it passes through the Analytics source connector to Adobe Experience Platform. See [Compare your Adobe Analytics data to Customer Journey Analytics data](/en/docs/analytics-platform/using/troubleshooting/compare)

- Unique Visitors
- Unique Devices
- Unique Cookies

**Unique Visitors** metricSee:

- [Terms used in Adobe Analytics](/en/docs/analytics/technotes/terms)
- [Unique Visitors](/en/docs/analytics/components/metrics/unique-visitors)

Distinct values of **post_visid_high & post_visid_low** concatenated together.See:

- [Use data feeds to calculate common metrics](/en/docs/analytics/export/analytics-data-feed/data-feed-contents/datafeeds-calculate)

Count distinct of
endUserIDs._experience.aaid.id
People
metric, if
endUserIDs._experience.aaid.id
is chosen as the Person ID.
- A “person” in Adobe Analytics is usually associated with a “device identifier” such as a cookie. AAID is the primary device identifier in Adobe Analytics, not ECID. See also [AAID, ECID, AACUSTOMID and the Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/aaid-ecid-adc).
- “Visitor” is not an out-of-the-box metric in Customer Journey Analytics. But if you choose **endUserIDs._experience.aaid.id** as the Person ID, the People metric in Customer Journey Analytics is roughly equivalent to Unique Visitors in Adobe Analytics.

- People

**People** metricSee:

- [People](/en/docs/analytics/components/metrics/people)

Not available
Count distinct of
<path>
.stitchedId
(available in stitched datasets only)
People
metric
- The People metric in Customer Journey Analytics is the count distinct of Person IDs. Depending on what you choose as the Person ID in the Customer Journey Analytics connection, the People metric can mean different things.

- Visits
- Sessions

**Visits** metricSee:

- [Terms used in Adobe Analytics](/en/docs/analytics/technotes/terms)
- [Visits](/en/docs/analytics/components/metrics/visits)
- [Report time processing](/en/docs/analytics/components/virtual-report-suites/vrs-report-time-processing)

Distinct values of **post_visid_high, post_visid_low, visit_num & visit_start_time_gmt** concatenated together.See:

- [Use data feeds to calculate common metrics](/en/docs/analytics/export/analytics-data-feed/data-feed-contents/datafeeds-calculate)

Not available
Sessions
metric
- With report-time processing in Adobe Analytics virtual report suites and Customer Journey Analytics data views, the concept of a visit (session) is configurable. As a result, visit (session) counts may differ between environments depending on the definition applied. See also [Compare data processing across Adobe Analytics and Customer Journey Analytics reporting features](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/data-processing-comparisons) and [Virtual report suites, Data views, Adobe Experience Platform sandboxes and the Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/vrs-dataview-sandbox-adc).

- Custom events
- Success events

Custom events 1-1000
**post_events_list**See:

- [Use data feeds to calculate common metrics](/en/docs/analytics/export/analytics-data-feed/data-feed-contents/datafeeds-calculate)

**_experience.analytics.**

- event1to100.event1 through event901to1000.event1000

**_experience.analytics.**

- event1to100.event1 through event901to1000.event1000

- An “event” in Adobe Analytics is a [Success Event](/en/docs/analytics/components/metrics/custom-events) (custom event) that has been set in an Adobe Analytics image request (data collection server call.)

- Event deduplication
- Metric deduplication

See:

- [Event ID serialization](/en/docs/analytics/implementation/vars/page-vars/events/event-serialization)

The **post_events_list** column contains deduplicated event metrics.See

- [Data column reference](/en/docs/analytics/export/analytics-data-feed/data-feed-contents/datafeeds-reference).

Not available
See:

- [Metric deduplication component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/metric-deduplication)

- Event/metric de-duplication in Adobe Analytics differs slightly from Customer Journey Analytics. In Adobe Analytics, deduplication occurs at data processing time. In Customer Journey Analytics, deduplication occurs at report runtime, providing more flexibility. Deduplicated metrics may differ slightly in Adobe Analytics vs Customer Journey Analytics.

- Instances metrics

See:

- [Instances](/en/docs/analytics/components/metrics/instances)

Count of times a “pre” variable is not null (e.g. eVar1).
Count of times a “mid” variable is not null (e.g.
_experience.analytics.
customDimensions.eVars.eVar1
).
You can create
Instances
metrics by
creating metrics from eVar fields.
- Instances is normally associated with prop and eVar columns as a means to determine how many times the variable has been set.

recommendation-more-help
