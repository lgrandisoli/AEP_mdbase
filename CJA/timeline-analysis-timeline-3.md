---
title: "Timeline analysis timeline"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/timeline"
category: "guides"
topic: "analytics-platform/using/guided-analysis/timeline"
created_at: "2026-06-23T20:44:05.132920+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Timeline analysis timeline

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- User

The **Timeline** analysis allows you to observe user-level session events over time to find experience patterns and tell better user stories. The left rail allows you to filter the stream by property values and segments. The right rail allows you to select from a randomized list of users that match the filter criteria. The center area shows the stream for the selected user by session, consisting of timestamp, property values, and duration. Duration is not available for the last event in a given session.

NOTE
The Timeline analysis requires that the
Person ID
standard component be available in the
data view
. The inclusion of Person ID in a data view is managed by your Customer Journey Analytics administrator, giving your organization full privacy control over who can access this data.
If a data view does not have the Person ID component added, the following message is displayed:
- **Admins**: *The PersonID property is required for this analysis. Please add Person ID to the data view.*
- **Non-admins**: *The PersonID property is required for this analysis. Please work with your Customer Journey Analytics administrator to add Person ID to the data view.*

https://video.tv.adobe.com/v/3427810/?quality=12&learn=on
## Use cases

Use cases for this analysis include:

- **Friction exploration**: If you find a steep drop in the [Funnel analysis](/en/docs/analytics-platform/using/guided-analysis/funnel) analysis, you can create a segment of those users and apply the segment in this analysis to investigate potential causes.
- **Error behavior**: If users encounter a product error, you can explore what users were doing before or after seeing that error.
- **Data collection validation**: Data admins can filter this analysis to their own Person ID to validate that their organization’s implementation is working as expected.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- **Dimension**: The dimension that you want to view streamed values for. The stream in the center shows values for the selected dimension. You can also apply filters to narrow down the stream to more relevant data. Valid operators for the filter include Equals, Does not equal, Starts with, Ends with, Contains, Does not contain, Exists, and Does not exist.
- **Segments**: The segment that you want to analyze. The selected segment filters your data to focus only on the individuals who match your segment criteria. If you want to narrow down the analysis to a specific Person ID, you can filter to that Person ID in the right panel. One segment is supported for this analysis.

### Chart settings

The Timeline analysis offers the following chart settings, which can be adjusted in the menu above the chart:

- Show as : Shows the desired property values. Show all: Show all property values in a session. Highlight: Visually highlights property values in a session that match the query filters. View only: Only show property values in a session that match the query filters.

### Date range

The desired date range for your analysis. There are two components to this setting:

- **Interval**: The date granularity that you want to view trend data by. This setting does not impact non-trended analysis such as Timeline.
- **Date**: The starting and ending date. Rolling date range presets and previously saved custom ranges are available for your convenience, or you can use the calendar selector to choose a fixed date range.

recommendation-more-help
