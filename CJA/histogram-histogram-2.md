---
title: "Histogram histogram"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/histogram"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:43:19.902466+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Histogram histogram

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)

CREATED FOR:

- User

Russ or Meike - Check Hit Type link above.
*This article documents the Histogram visualization in* *Customer Journey Analytics .**See Histogram for the* *Adobe Analytics version of this article.*

style
shade-box
The **Histogram** visualization is similar to a Bar visualization, but it groups numbers into ranges (buckets). Analytics automates the “bucketing” of numbers into ranges, but you can change the settings in [Advanced Settings](#advanced-settings).

## Use

To create a histogram:

- Add a **Histogram** visualization. See [Add a visualization to a panel](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#add-visualizations-to-a-panel).
- Drag a metric from the **Metrics** component list, or select a metric from the *Add a metric* drop-down menu.
- (optional) Select **Show advanced settings**. See [Advanced settings](#advanced-settings).
- Select **Build**.

NOTE
Histograms support only standard metrics, not calculated metrics.
In the example below, a histogram is used to bucket sessions for the number of persons. The histogram shows that most persons do have between 16-21 sessions for the selected date range.

## Advanced settings

As part of the visualization, specific histogram settings are available.

Histogram settings
Description
Starting bucket
Determines which bucket the histogram starts with. “1” is the default. You can set starting numbers from 0 to infinity (no negative numbers).
Metric buckets
Lets you increase/decrease the number of data ranges (buckets.) The maximum number of buckets is 50.
Metric bucket size
Lets you set the size of each bucket. For example, you can change the bucket size from 1 page view to 2 page views.
Counting method
Select from
Global Account
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
,
Account
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
,
Buying Group
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
,
Opportunity
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
,
Person
,
Session
, or
Event
. For example, page views per account
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
, page views per session, or page views per person, or page views per event.
**Examples**:

Starting bucket
Metric buckets
Metric bucket size
Result
1
5
2
0
3
5
Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
Using histograms to identify unexpected data values
recommendation-more-help
