---
title: "Get started with data sources about-data-sources"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:56.618104+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with data sources about-data-sources

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Data Sources](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

TIP
New to data management in Journey Optimizer? Start with the
Get started with data management
overview to understand schemas, datasets, identities, and how data flows before configuring data sources.
The data source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys, for:

- [condition definition](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions)
- parameter and personalization data in [actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action)
- [custom wait definition](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity#custom)
- [time zone definition](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management)

➡️ [Discover this feature in video](#video)

This configuration is not required if your journeys only leverage local data coming from an event payload. For example, if your journey is composed of an event followed by a channel action activity that only uses data from the event, there is no need to configure a data source.

There are two types of data sources:

- The **pre-configured** Adobe Experience Platform data source that defines the connection to the Real-time Customer Profile Service. This is a built-in data source. See [this page](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/adobe-experience-platform-data-source).
- The **external** data sources that allow you to define a connection to external systems. These are the ones you can create. See [this page](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/external-data-sources).

NOTE
As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases. For more information on responses, see this
section
For each data source, you define the information to retrieve using field groups. Field groups are sets of fields that can be retrieved from a data source. See [this page](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/configure-data-sources#define-field-groups).

NOTE
Schema relationships are not supported for data sources.
## Choose your data access strategy data-access-strategy

Before configuring a data source, consider which approach best fits your use case. Three options are available, each with different trade-offs in terms of persistence, profile enrichment, and reusability. For a detailed discussion of these options, see [Best practices for advanced journeys in Journey Optimizer](/en/perspectives/best-practices-for-advanced-journeys-in-journey-optimizer#_blank).

**Option 1 — Access external data via Custom Actions (no Data Lake)**

Connect directly to an external API at journey runtime without persisting data in the Experience Platform Data Lake. Best suited when:

- The data is only useful within the journey context and not needed elsewhere.
- The external system is accessible through an API endpoint that returns the attributes needed.

Learn more about [custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action) and [custom action responses](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response).

TIP
This option is a good fit if you answer
yes
to both questions:
- Is the data only useful inside the journey context and not needed elsewhere? If the data is also needed for audiences or other channels, consider Options 2 or 3.
- Is the external system accessible through an API endpoint that returns the required attributes? If not, you will need to ingest the data into the Data Lake first.

**Option 2 — Dataset in Data Lake, not enabled for Profile**

Ingest data into a dataset to trigger and personalize journeys based on contextual event data, without contributing to the Real-Time Customer Profile. Best suited when:

- Records contain an identity field usable to access profiles already stored in Experience Platform.
- The data is not needed for audience creation or identity stitching outside of Journey Optimizer.

TIP
This option is a good fit if you answer
yes
to both questions:
- Do records contain an identity field that can be used to access profiles already stored in Experience Platform? If not, journeys will not be able to access and deliver to profiles.
- Is the data NOT needed for [audience](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences) creation or identity stitching outside of Journey Optimizer? If it is, use Option 3 instead.

**Option 3 — Profile-enabled dataset in Data Lake**

Ingest data into a [profile-enabled dataset](/en/docs/experience-platform/catalog/datasets/user-guide#enable-profile#_blank) to create audiences, enrich identity graphs, and leverage data across multiple journeys and RT-CDP destinations. Best suited when:

- The data is useful for audience definitions used in channels beyond Journey Optimizer.
- The data contains multiple identities that contribute to richer, stitched profile fragments.

CAUTION
Before you enable a dataset for Profile
, assess the following areas:
- **Data synchronization** — External databases must be synchronized, with alerts in place to identify ingestion failures.
- **Profile guardrails** — Profile-specific guardrails apply in addition to the [general data ingestion guardrails](/en/docs/experience-platform/ingestion/guardrails#_blank) for Experience Platform.
- **Identity integrity** — Identity data in your source systems must be carefully planned to maintain healthy identity graphs.
- **Data Lake utilization** — Overall storage consumption, table relationships, and addressable profiles must be assessed before ingestion.

Data persisted in Data Lake
Dataset enabled for Profile
Option 1
— External data via Custom Actions
No
No
Option 2
— Dataset not enabled for Profile
Yes
No
Option 3
— Profile-enabled dataset
Yes
Yes
For more information on how to configure an Adobe Experience Platform Data Source and an external data source and how to find and use data in a journey, watch this [tutorial video](/en/docs/journey-optimizer-learn/tutorials/configuration/journey-configuration/configure-data-sources#_blank).

## How-to video video

Understand what a data source is and learn how to configure Experience Platform and external data sources.

https://video.tv.adobe.com/v/334256?quality=12&learn=on
recommendation-more-help
