---
title: "Compare data processing across Adobe Analytics and Customer Journey Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/data-processing-comparisons"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/cja-aa-comparison"
created_at: "2026-06-02T19:04:53.698762+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Compare data processing across Adobe Analytics and Customer Journey Analytics

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User

You often need the ability to process data before it is useful for reporting. You can process that data at several stages in the journey that spans from collecting data to generating your report or visualization.

In Adobe Analytics most of that processing of data occurs immediately after collecting the data. Functionalties like VISTA Rules, Processing Rules, Marketing Channels Processing Rules are available to support this **collection-time processing**.The data is then stored and at report time you can apply additional processing. For example, break down dimensions, apply segmentation, or select a different attribution model. This **report-time processing** happens on the fly.

In Adobe Analytics, report-time processing commonly represents a smaller amount of processing than what happens at collection-time.

In contrast, Customer Journey Analytics is designed to require minimal upfront collection-time processing before data is organized and stored. The underlying architecture of Customer Journey Analytics is designed to work with the stored data at report-time. Customer Journey Analytics offers its powerful report-time processing functionality not only in Analysis Workspace. Additional report-time processing functionality is available through the definition of [components](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview) and [derived fields](/en/docs/analytics-platform/using/cja-dataviews/derived-fields) in your data views.

Understanding the differences in data processing for the various reporting features can be helpful in understanding which metrics are available where and why they may differ.

For example, *visits* is defined as a metric in Adobe Analytics at data processing time. And *sessions* is calculated as a metric in Customer Journey Analytics at report time. As a result, the two metrics may differ based on the rules for the session definition in a Customer Journey Analytics data view.

Also, visits and sessions as a metric are not available in datasets created by the Analytics source connector. And therefore would require you to define the session in your query logic to do comparisons.

## Terminology terms

The table below defines terminology for the different types of processing logic that are applied to Adobe Analytics and Customer Journey Analytics:

Term
Definition
Notes
Collection-time processing
Logic that is performed when data is being collected and processed, before being stored for reporting and analytics purposes.
This logic is ‘baked into’ historical data and generally cannot easily be changed.
Report-time processing
Logic that is performed at the time a report is run.
This logic can be applied to future and historical data at report runtime in a non-destructive manner.
Hit-level logic
Logic applied at a row-by-row level.
Examples: Processing rules, VISTA, certain marketing channel rules.
Visit-level logic
Logic that is applied at the visit level.
Examples: Visit and session definition.
Visitor-level logic
Logic that is applied at the person level.
Example: Cross-device/cross-channel person stitching.
Segment logic
Evaluation of event/visit/person (event/session/person) segment rules.
Example: People who bought red shoes.
Calculated metrics
Evaluation of customer-created custom metrics. Calculated metrics can be based on complex formulas, including segments.
For example, the number of people who bought red shoes.
Attribution logic
Logic to calculate attribution.
Example: eVar persistence.
Component Settings
Applying customizations to metrics or dimensions, like attribution, behavior, format, and others
Example: value bucketing to combine numeric values based on a range
Derived fields
Logic that applies to schema or standard fields as part of defining components in a Data view.
Example: creating a new marketing channel dimension
Over time, Adobe Analytics and now Customer Journey Analytics have improved their flexibility by allowing visit and person-level data logic to be performed at report runtime.

## Types of data processing types

The data processing steps performed by Adobe Analytics and Customer Journey Analytics and the timing of those steps varies from feature to feature. The table below provides a summary of the types of data processing for each feature, and when data processing is applied.

Feature
Applied at processing time
Applied at report time
Not available
Notes
Adobe Analytics
reporting
(not including advanced attribution features or virtual report suites with report-time processing)
- [Processing rules](/en/docs/analytics/admin/admin-tools/manage-report-suites/edit-report-suite/report-suite-general/c-processing-rules/processing-rules)
- [VISTA rules](/en/docs/analytics/technotes/terms)
- Hit-level [marketing channel rules](/en/docs/analytics/admin/admin-tools/manage-report-suites/edit-report-suite/marketing-channels/c-rules)
- Visit-level marketing channel rules (see note)
- Visit definition
- Attribution logic

- Segment logic
- Calculated metrics

- Cross-Device Analytics (see note)

- Cross-Device Analytics requires the use of virtual report suites with report time processing.
- “Visit-level marketing channel rules” include the following: **Is First Page of Visit**, **Override Last-Touch Channel**, and **Marketing Channel Expiration**. (See [documentation](/en/docs/analytics-platform/using/cja-usecases/aa-data/marketing-channels).)

Adobe Analytics
Data Warehouse
- Processing rules
- VISTA rules
- Hit-level marketing channel rules
- Visit-level marketing channel rules
- Visit definition
- Attribution logic

- Segment logic

- Calculated metrics
- Cross-Device Analytics

Adobe Analytics
Data Feeds
- Processing rules
- VISTA rules
- Hit-level marketing channel rules
- Visit-level marketing channel rules
- Visit definition (visitnum field)
- Attribution logic (in post columns)

- Segment logic
- Calculated metrics
- Cross-Device Analytics

- ID mappings for certain marketing channel-related columns in data feeds are not included with data feeds. (See the [data feed documentation](/en/docs/analytics/export/analytics-data-feed/data-feed-contents/datafeeds-reference).)

Adobe Analytics
Livestream
- Processing rules
- VISTA rules

- Hit-level marketing channel rules
- Visit-level marketing channel rules
- Visit logic
- Attribution logic
- Segment logic
- Calculated metrics
- Cross-Device Analytics

Adobe Analytics
Advanced attribution features
- Processing rules
- VISTA rules
- Visit definition (see note)
- Cross-Device Analytics (see note)

- Hit-level marketing channel rules (see note)
- Visit-level marketing channel rules (see note) Attribution logic
- Segment logic
- Calculated metrics

- Cross-Device Analytics requires the use of virtual report suites with report time processing.
- Advanced attribution features in Core Analytics use marketing channels that are derived completely at report time (that is, derived mid-values.)
- Advanced attribution features use a processing-time visit definition except when used in a report-time processing virtual report suite.

Adobe Analytics virtual report suites with
report-time processing
- Processing rules
- VISTA rules
- [Cross-Device Analytics](/en/docs/analytics/components/cda/overview)

- Visit definition
- Attribution logic
- Segment logic
- Calculated metrics
- Other virtual report suite report-time processing settings

- Hit-level marketing channel rules
- Visit-level marketing channel rules

- See Virtual report suite report-time processing [documentation](/en/docs/analytics/components/virtual-report-suites/vrs-report-time-processing).

Analytics source connector
-based dataset in Adobe Experience Platform data lake
- Processing rules
- VISTA rules
- Hit-level marketing channel rules
- Field-based stitching (see note)

- [Visit-level marketing channel rules](/en/docs/analytics-platform/using/cja-usecases/aa-data/marketing-channels)
- Visit logic
- Attribution logic
- Segment logic

- Apply your own segment logic and calculated metrics
- Field-based stitching creates a separate stitched dataset in addition to the one created by the Analytics source connector.

Customer Journey Analytics
reporting
- Implemented as part of Adobe Experience Platform Data Collection

- Session definition
- [Data view](/en/docs/analytics-platform/using/cja-dataviews/data-views) settings
- Attribution logic
- Calculated metrics
- Segment logic

- Visit-level marketing channel rules

- Use stitched datasets to take advantage of cross-channel analytics.

recommendation-more-help
