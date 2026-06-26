---
title: "Media concurrent viewers panel media-concurrent-viewers-panel"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/panels/media-concurrent-viewers"
category: "other"
topic: "analytics-platform/using/cja-workspace/panels"
created_at: "2026-06-23T20:43:09.686688+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Media concurrent viewers panel media-concurrent-viewers-panel

Last update: May 13, 2026
- Topics:
- [Panels](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
For more information about Media Concurrent Viewers, visit [MA doc page]( https://url).
*This article documents the Media concurrent viewers panel in* *Customer Journey Analytics*.*See Media concurrent viewers panel for the* *Adobe Analytics version of this article.*

style
shade-box
NOTE
The Media average minute audience panel is available only to customers who have purchased the Streaming Media Collection Add-on for Customer Journey Analytics.
Contact your Adobe Sales representative or Adobe account team for more information.
The **Media concurrent viewers** panel enables analysis of concurrent viewers over time, with details on peak concurrency and the ability to break down and compare.

You can analyze concurrent viewers to understand where peak concurrency occurred or where drop-offs happened to provide valuable insight into the quality of content and viewer engagement. And to help with troubleshooting or planning for volume or scale.

In Analysis Workspace, the Concurrent viewers metric is the number of unique persons viewing your media streams at a specific point in time, regardless of the number of sessions.

See [Media concurrent viewers panel](/en/docs/analytics-learn/tutorials/analysis-workspace/using-panels/media-concurrent-viewers-panel-in-analysis-workspace#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
## Use

To use an **Media concurrent viewers** panel:

- Create a Media concurrent viewers panel. For information about how to create a panel, see Create a panel .
- Ensure you select a data view for the panel that has components configured from the Streaming Media Collection.
- Specify the input for the panel.
- Observe the output for the panel.

### Panel input

You can configure the Media concurrent viewers panel using these input settings:

Setting
Description
Panel date range
The panel date range default is Today. You may edit it to view a single day or many months at a time.
This visualization is limited to 1440 rows of data (for example, 24-hours at minute-level granularity). If a date range and granularity combination results in more than 1440 rows, the granularity is automatically updated to accommodate the full date range.
Granularity
The granularity default is Minute.
This visualization is limited to 1440 rows of data (for example, 24-hours at minute-level granularity). If a date range and granularity combination results in more than 1440 rows, the granularity is automatically updated to accommodate the full date range.
Panel summary numbers
To see date or time details for concurrent viewers, a summary number is available. The Maximum shows details for peak concurrency.
Minimum
shows details for the trough. The panel default shows Maximum only, but you can change it to show Minimum or both Maximum and Minimum.
If you are using breakdowns, a summary number is displayed for each.
Series breakdown
Optionally, you can break down your visualization by segments, dimensions, dimension items, or date ranges.
You may view up to 10 lines at a time. Breakdowns are limited to a single level.
When dragging a dimension, the top dimension items are selected automatically based on the selected panel date range.
To compare date ranges, drag 2 or more date ranges into the series breakdown segment.
Here is an example of the panel configured for **Minute** granularity, with **Maximum only** summary numbers. And broken down by **Other**, **Table**, **Mobile Phone**, **Gaming Console**, **Media Player**, **Set-top Box**, **Television**.

### Panel output

The Media Concurrent Viewers panel returns a line chart and summary numbers to include details for the maximum and/or minimum concurrent viewers. At the top of the panel, a summary line is provided to remind you of the panel settings you selected.

At any time, select to edit and rebuild the panel.

If you select a series breakdown, a line on the line chart and a summary number is displayed for each:

### Data source

The only metric that can be used in this panel is **Concurrent viewers**:

Metric
Description
Concurrent viewers
The number of unique persons viewing your media streams at a specific point in time, regardless of the number of sessions.
A Freeform table is not available in this view. To view the data source, you can download the data source from the line chart visualization context menu and select **Download data as CSV**. Series breakdowns are included.

## FAQs

Question
Answer
Where is the Freeform table? How can I see the data source?
The Freeform table is not available in this view. You can download the data source from the line chart context menu and select
Download data as CSV
.
Why did my granularity change?
This visualization is limited to 1440 rows of data (for example, 24-hours at minute-level granularity). If a date range and granularity combination results in more than 1440 rows, the granularity is automatically updated to accommodate the full date range.
When changing from a larger date range to a smaller one, the granularity is updated to the lowest detail allowable once the date range is changed. To view a higher granularity, edit the panel and rebuild.
How do I compare video names, segments, content types, and others?
To compare these items in a single visualization, drag segments, dimensions, or specific dimension items in the series breakdown segment.
The view is limited to 10 breakdowns. To view more than 10, you must use multiple panels.
How do I compare date ranges?
To compare date ranges in a single visualization, use the series breakdowns by dragging 2 or more date ranges. The date ranges override the panel date range.
How do I change the visualization type?
This panel only allows for the line visualization for the time series.
Can I run anomaly detection?
No. Anomaly detection is not available for this panel.
Why use unique persons instead of active sessions?
Using unique persons enables removal of unwanted spikes at show boundaries (where sessions are ending and starting at the same time).
What does it mean to have concurrent viewers at higher granularity than minute?
With a granularity larger than a minute, concurrent viewers is the sum of unique concurrent viewers for all minutes within that time range. For example, at hour-level granularity concurrent viewers are the sum of unique concurrent viewers for all minutes within the hour.
Does the workspace panel show the same information as the Concurrent Viewers Report?
No. In Analysis Workspace, the Concurrent viewers metric is defined as the number of unique persons viewing your media stream at a specific point in time. Regardless of the number of sessions.
This metric is different than Concurrent viewer reporting in the Reports section, which uses Concurrent Active Sessions. Using unique persons accounts for the removal of unwanted peaks at show boundaries (where sessions are ending and starting at the same time).
Related Articles
Create a panel
Media playback time spent panel
Media average minute audience panel
recommendation-more-help
