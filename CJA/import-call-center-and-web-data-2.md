---
title: "Import call center and web data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/cross-channel/call-center"
category: "other"
topic: "analytics-platform/using/cja-usecases/cross-channel"
created_at: "2026-06-23T20:43:43.259799+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Import call center and web data

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- User

Customer Journey Analytics provides the valuable and robust capability to combine datasets from different sources into a single Workspace project. Use this guide to understand how your organization can combine website data with call center data. For example, you can understand what actions a customer takes, what content that they view, and what terms that they search for before they contact customer support. You can then determine the content and self-service tools to improve so customers can better resolve issues themselves without needing to call in.

## Prerequisites

- The most important component to combining these two sets of data is a common identifier between each source of data. Examples include a customer ID, a hashed email, login username, or phone number.
- Access to both Adobe Experience Platform and Customer Journey Analytics
- If your dataset includes logs from an interactive voice response system, Adobe recommends processing the data to only include prompt interactions prior to importing it into Platform.
- If your dataset includes call logs, Adobe recommends including the following columns: The date/time when the call started Call reason Call center ID Call center agent ID Duration of call Outcome of call Cost of call (if available) Any additional call meta data that your organization wants to include

## Import web and call center data into Platform

Import your data into Adobe Experience Platform. See [Create a schema](/en/docs/experience-platform/xdm/tutorials/create-schema-ui) and [Ingest data](/en/docs/experience-platform/ingestion/home) in the Adobe Experience Platform documentation.

When importing data into Platform, following these tips can help increase insight in resulting reports:

- Make sure that the identifier used to link call center and web data together are similarly formatted.
- Include the data source in each dataset. For example, include a data_source column in each schema, and set the value of every event to "Web" or "Call center", respectively.mapper

## Stitch the person ID’s together

Customer Journey Analytics requires a common identifier to generate a [combined dataset](/en/docs/analytics-platform/using/cja-connections/combined-dataset).

- If your datasets already have a common identifier on every event across both datasets, you can skip this step and proceed to create a connection.
- If either of your datasets have a common identifier on only some events, you can stitch data together using [Stitching](/en/docs/analytics-platform/using/stitching/overview) for steps to enable cross-channel analysis for these two datasets.

## Create a connection in Customer Journey Analytics

[Create a connection](/en/docs/analytics-platform/using/cja-connections/create-connection) in Customer Journey Analytics.

- If CCA is used, a new stitched dataset is available for you to use. Use the newly created stitched ID field as the person ID.
- Otherwise, you can select both original web and call center datasets for use in the connection.

## Create a data view

After creating a connection, you can [Create a data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview) for use in Analysis Workspace. Helpful components include:

- A page dimension with last touch and session persistence. You can connect call center metrics with the last page that a customer viewed before calling in.
- A calls metric that uses a ‘Call center reason’ schema field to increase occurrences. Use [Metric deduplication](/en/docs/analytics-platform/using/cja-dataviews/component-settings/metric-deduplication) so it increases only once per session.

## Create visualizations

The following visualizations can be used to gain insights from your stitched dataset.

### Dataset overlap

This visualization helps you understand how well CCA stitches data together.

- Create two segments. The variable used in these two segments is the same variable mentioned above that reflects the source of data of each event. See Create a segment for more information. Person container where Dataset ID equals your web data Person container where Dataset ID equals your call center data
- In Analysis Workspace, drag a Venn visualization onto the workspace canvas.
- Drag the two newly created segments to the Add Segment area, and the People metric to the Add Metric area.

The resulting Venn visualization shows the number of people in your dataset that contain both web and call center data. The larger the overlap, the more people that were successfully stitched. The areas that don’t overlap represent people that reside exclusively in one dataset or the other.

### Attribute call center events to web pages

This freeform table lets you see the top pages that contribute to call center events. First, make sure that the desired dimensions and metrics have the correct attribution model:

- Drag the dimension that holds your web page names onto a Freeform Table visualization.
- Replace the metric with the desired call center metric that you want to measure.
- Click the gear icon near the metric header. Click **Use non-default attribution model**.
- Set the desired [Attribution model](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/column-settings). For example, a Time Decay model with a half-life of 15 minutes, and a Lookback Window of Session. This attribution model gives credit to the pages leading up to the call to your call center.

The resulting report shows the top pages that drive calls to your call center. use case behind what we use these pages for

You can further increase insight with this table by splitting Calls by reason or category.

- Click the right chevron under the ‘Call Reason’ dimension in the list of components. This action reveals individual dimension values.
- Drag the desired dimension value(s) under the ‘Calls’ metric, which segments that metric by each respective call reason.
- Repeat for each call reason that you would like to drill into. Use the ‘All sessions’ segment to view the aggregate total.

### Flow visualization

You can gain insight into the what a customer was trying to do before they used the call center channel. This flow visualization helps you understand the most frequent journeys a customer takes to reach your call center. This insight lets you determine the most effective improvements you can make to your site so customers are less likely to call in.

- Click the **Visualizations** tab on the left and drag a flow visualization onto the workspace canvas.
- Click the **Components** tab on the left and locate the ‘Call Reason’ dimension.
- Click the right chevron next to this dimension. This action reveals individual dimension values.
- Drag the desired call reason dimension item to the center location of the flow visualization.
- The flow visualization automatically populates previous and next call reasons. Replace the previous call reason with the website page dimension.
- Click the gear icon in the upper right of the flow visualization and change the flow container to **Session**.

### Histogram

How many customers have called once, called twice, or called 6+ times? Some of these people never visit the website. Use the histogram visualization to determine how many people fall into each bucket. For people who never visit the website, see how we can encourage them to self serve.

- Click the **Visualizations** tab on the left and drag a histogram visualization onto the workspace canvas.
- Click the **Components** tab on the left and drag the calls metric to the histogram visualization.
- Click **Show advanced settings** in the center of the visualization and customize the desired buckets.
- Click **Build**.

recommendation-more-help
