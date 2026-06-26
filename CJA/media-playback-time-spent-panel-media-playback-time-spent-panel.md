---
title: "Media playback time spent panel media-playback-time-spent-panel"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/panels/media-playback-time-spent"
category: "other"
topic: "analytics-platform/using/cja-workspace/panels"
created_at: "2026-06-02T19:06:03.415454+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Media playback time spent panel media-playback-time-spent-panel

Last update: May 13, 2026
- Topics:
- [Panels](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
*This article documents the Media playback time spent panel in* *Customer Journey Analytics*.*See Media playback time spent panel for the* *Adobe Analytics version of this article.*

style
shade-box
NOTE
The Media average minute audience panel is available only to customers who have purchased the Streaming Media Collection Add-on for Customer Journey Analytics.
Contact your Adobe sales representative or Adobe account team for more information.
The **Media playback time spent** panel enables analysis of playback over time, with details on peak concurrency and the ability to break down and compare.

In Analysis Workspace, Playback time spent is the amount of time spent viewing your media streams at a specific point in time. It includes pause, buffer, and time to start.

Customers who have purchased the Streaming Media Collection Add-on can analyze playback time spent to gain valuable insight into the quality of content and viewer engagement. And to help when troubleshooting or planning for volume or scale.

Playback time spent can help you understand:

- Where peak concurrency occurred.
- Where drop-offs occurred.

See [Media playback time spent](/en/docs/analytics-learn/tutorials/media-analytics/measuring-media-analytics/media-playback-time-spent-panel#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
## Use

To use an **Media playback time spent** panel:

- Create a Media playback time spent panel. For information about how to create a panel, see Create a panel .
- Ensure you select a data view for the panel that has components configured from the Streaming Media Collection.
- Specify the input for the panel.
- Observe the output for the panel.

### Panel input

You can configure the Media Playback Time Spent panel using these input settings:

Setting
Description
Panel date range
The panel date range default is Today. You may edit it to view a single day or many months at a time.
This visualization is limited to 1440 rows of data (for example, 24-hours at minute-level granularity). If a date range and granularity combination results in more than 1440 rows, the granularity is automatically updated to accommodate the full date range.
Granularity
The granularity default is Minute.
This visualization is limited to 1440 rows of data (for example, 24-hours at minute-level granularity). If a date range and granularity combination results in more than 1440 rows, the granularity is automatically updated to accommodate the full date range.
Panel summary numbers
To see date or time details for playback time spent, a summary number is available. The Maximum shows details for peak concurrency. The Minimum shows details for the trough. Sum adds up the total playback time spent for the selection. The panel default shows Maximum only, but you can change it to show Minimum, Sum, or any combination of the three.
If you are using breakdowns, a summary number is displayed for each.
Series breakdown
Optionally, you can break down your visualization by segments, dimensions, dimension items, or date ranges.

- You may view up to 10 lines at a time. Breakdowns are limited to a single level.

- When dragging a dimension, the top dimension items are automatically selected based on the selected panel date range.

- To compare date ranges, drag 2 or more date ranges into the series breakdown segment.

Time format
You can view the playback time spent in either
Hours:Minutes:Seconds
(default) or in
Minutes
(which is displayed in whole numbers, rounded up at 0.5).
Date sequence display
If you’ve placed at least two date range segments as series breakdowns, you see the option to select either overlay (default) or sequential. Overlay displays the lines with a common x-axis start so that they run in parallel, while sequential displays the lines with their specific x-axis start. If the data lines up (for example, segment 1 ends at 8:44 pm and segment 2 starts at 8:45 pm), then the lines show in sequence.
### Panel output

The Media Playback Time Spent panel returns a line chart and summary numbers to include details for the maximum, minimum, and/or sum of playback time spent. At the top of the panel, a summary line is provided to remind you of the panel settings you selected.

At any time, select to edit and rebuild the panel.

If you select series breakdown, a line on the line chart and a summary number is displayed for each:

### Data source

The only metric that can be used in this panel is Playback Time Spent.

Metric
Description
Playback Time Spent
Total
hours:minutes:seconds
(or
minutes
) of content viewed during the selected granularity including pause, buffer, and time to start.
## FAQs

Question
Answer
Where is the Freeform table? How can I see the data source?
The Freeform table is not available in this view. To download the data source, from the context menu in the line chart select the option to download the CSV file.
Why did my granularity change?
This visualization is limited to 1440 rows of data (for example, 24-hours at minute-level granularity). If a date range and granularity combination results in more than 1440 rows, the granularity is automatically updated to accommodate the full date range.

When changing from a larger date range to a smaller one, the granularity is updated to the lowest detail allowable once the date range is changed. To view a higher granularity, edit the panel and rebuild.

How do I compare video names, segments, content types, and more?
To compare these in a single visualization, drag segments, dimensions, or specific dimension items in the series breakdown segment.

The view is limited to 10 breakdowns. To view more than 10, you must use multiple panels.

How do I compare date ranges?
To compare date ranges in a single visualization, use the series breakdowns by dragging 2 or more date ranges. These date ranges override the panel date range.
How do I change the visualization type?
This panel only allows for the line visualization for the time series.
Can I run anomaly detection?
No. Anomaly detection is not available for this panel.
Related Articles
Create a panel
Media average minute audience panel
Media concurrent viewers panel
recommendation-more-help
