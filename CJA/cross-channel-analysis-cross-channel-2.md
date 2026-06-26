---
title: "Cross-channel analysis cross-channel"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/cross-channel/cross-channel"
category: "other"
topic: "analytics-platform/using/cja-usecases/cross-channel"
created_at: "2026-06-23T20:42:31.601337+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Cross-channel analysis cross-channel

Last update: June 5, 2026
- Topics:
- [Administration](#)
- [Data management](#)

CREATED FOR:

- User

Cross-channel analysis enables a single consolidated view of customer behavior across various channels by unifying data from various web, mobile, and offline properties. For example, you can use this consolidated view to analyze customer interactions across desktop and mobile to understand customer behavior and extract insights to optimize digital customer experiences. You can also analyze customer interactions across channels, including digital and offline channels such as support interactions and in-store purchases to better understand and optimize the customer journey.

## Implementation Steps

- Create schemas for data to be ingested.
- Create datasets for data to be ingested.
- Ingest data into Experience Platform : Event-based data from website or mobile app through the Edge Network or Analytics source connector. Profile data (for example from a CRM system, call center application, loyalty application). Lookup data (for example product name, category from a product information system).
- Use a common namespace ID across datasets. Use Stitching to elevate any event-based dataset in respect to providing the common ID on each row. Note that Customer Journey Analytics does not currently use the Experience Platform Profile or Identity services for stitching.
- Perform any custom data preparation to ensure a common key across time series datasets to be ingested into Customer Journey Analytics.
- Give lookup data a primary ID that can join to a field in the event data. Counts as rows in licensing.
- Set the same primary ID for profile data as the primary ID of the event data.
- Create a connection to ingest the relevant datasets from Experience Platform to Customer Journey Analytics.
- Create a data view on the connection to select the specific dimensions and metrics to be included in the view. Attribution and allocation settings are also configured in the data view. These settings are computed at report time.
- Create a project to configure dashboards and reports within Analysis Workspace.

## Considerations

When establishing this workflow, make sure that you take the following points into consideration.

- Analyzing data across channels requires the same ID namespace on every record.
- The union process of unifying disparate datasets requires a common primary person/entity key across the datasets.
- Secondary key-based unions are currently not supported.
- The stitching process allows for rekeying identities in rows based on transient ID (such as an authentication ID) info from records sharing same persistent ID.This allows for resolving disparate records to a single stitched ID for analysis at the person level, rather than at the device or cookie level.
- Objects and attributes of the same XDM field merge into one dimension in Customer Journey Analytics. To merge multiple attributes from various datasets into the same Customer Journey Analytics dimension, the datasets should reference the same XDM field or schema.

recommendation-more-help
