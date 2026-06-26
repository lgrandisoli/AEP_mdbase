---
title: "Key metric summary key-metric-summary"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/key-metric"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:43:26.290933+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Key metric summary key-metric-summary

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)

CREATED FOR:

- User

## How the Key Metric Summary visualization handles the comparison date range
                
                (This will probably release in January. Per Jaden Howell)
                
                * If the primary date range is set to the panel date range, there are 2-6 options that are considered 'relative' to the primary date range. These usually include the previous period (same amount of time immediately proceeding the primary date range), and 52 weeks prior to that date range.
                
                * If the comparison date range is set to one of the 'relative' options, upon updating the primary date range, the comparison date range updates to the period immediate preceding the panel date range.
                
                * If your comparison date range is *not* set to a 'relative' option, then updating the panel date range changes your primary date range, but has no effect on the comparison date range.
                
                **Example 1**
                
                Primary date range is set to the panel's date range: 'Yesterday'
                Comparison date range is set to a relative date range, one of: 'Previous day', 'Same day last week', 'Same day 4 weeks prior', 'Same day last month', 'Same day last year', or 'Same day 52 weeks prior'.
                When I change the panel's date range to 'This month', the comparison date range will update to 'Previous month'.
                
                **Example 2**
                 
                Primary date range is set to the panel's date range: 'Yesterday'
                Comparison date range is set to a non-relative date range, such as 'Feb 2nd, 2022', 'Highest sales day', 'Last week', etc. 
                
                <div class="extension note">
                  <div>NOTE</div>
                  <div>
                    <p>Last week is relative to the day the project is opened on, but it is not based on the panel’s date range of ‘Yesterday’. In other cases, such as if the panel’s date range was ‘This week’, it may be relative.</p>
                  </div>
                </div>
                
                
                When you change the panel's date range to '4 days ago', the comparison date range remains at the previous selection.
*This article documents the Key metric summary visualization in* *Customer Journey Analytics .**See Key metric summary for the* *Adobe Analytics version of this article.*

style
shade-box
The **Key metric summary** visualization lets you see how an important metric is trending within a single timeframe. It also lets you compare metric performance across two timeframes. It provides the benefits of multiple visualizations combined into one visualization:

- Line visualization shows how the metric is trending for the primary and comparison date ranges
- Summary percent change shows the metric increase or decrease between the primary and comparison date ranges
- Current total value ( summary number ) for the metric

## Use cases

This visualization addresses various common use cases, including:

- An analyst trying to understand how opportunity creation looked this month compared to the same timeframe last year.
- A marketer exploring how lead generation for a specific lead type has changed from this month to last month.
- An executive wanting to understand how new bookings changed from this quarter to last quarter.

## Use

- Add a Key metric summary visualization. See Add a visualization to a panel .
- Configure the visualization by selecting a Metric , a Primary date range , a Comparison date range (optional) and a Segment (optional): table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Option Description Metric Select the metric you want to examine. All metrics are supported. Primary date range The current date range for the freeform table. Choose from any available date ranges in your data view. Choose Panel date range if you want to use the same date range that is being used on the panel where the visualization is located. Comparison date range The date range that you want to compare with the primary date range. Segment (optional) Any segment that you are interested in for this summary. note NOTE When the Primary date range field is set to Panel date range , the Comparison date range can automatically update, depending on whether the Comparison date range option you choose is relative to the primary date range or fixed. Relative: If the Comparison date range field is set to an option that is relative to the primary date range (such Previous day , Same day last week , Same day 4 weeks prior , and so forth), then any updates to the Primary date range field cause the Comparison date range to automatically update to the period that immediately follows the date range of the panel. Fixed: If the Comparison date range field is set to a fixed date range (such as February 3, 2023 ), then changes made to the Primary date range field or the panel date range have no effect on the Comparison date range . However, any updates to the panel date range cause the Primary date range to automatically update.
- Select Build .

The output of the key metric summary looks like:

Consider the following when viewing the output:

- The Previous period line graph (always displayed in gray) corresponds to the Comparison date range in the configuration step.
- If a comparison date range is not specified during configuration or is hidden in the visualization settings, only the line graph for the primary date range is displayed. The summary change is hidden.
- From here, you can hover over the line graphs to see the statistics for individual days:

## Configure

After building the visualization, you can edit the original configuration.

- Select Configure visualization at the top of the visualization. You are taken back to the original configuration dialog.
- Change the settings as preferred. Select Reset to reset the current settings. Select Build to rebuild the visualization.

## Settings

As part of the visualization settings, specific key metric summary settings are available.

Setting
Description
Emphasize percent change
Display summary change in prominent bold type in the center of the visualization
Emphasize number value
Display summary number in prominent bold type in the center of the visualization
Legend visible
Show or hide the legend at the bottom of the visualization
Show annotations
Show or hide annotations added by an admin
Hide title
Hide the visualization’s title.
Percentages
Displays the visualization in a percentage instead of a number.
Show trendlines
Show trendlines in the visualization.
Show max and min on trendlines
Show or hide minimum and maximum values on primary and comparison line charts
Show comparison percentage and trendline
Show or hide comparison data. When hidden, both the comparison line chart and summary change objects are hidden from view.
Show total number
Show or hide summary number
Show raw difference
Show or hide raw difference between the total value of the metric in the primary date range and the secondary date range
Abbreviate value
Select **Abbreviate value** to abbreviate intelligently the number value. When selected, enter a number to define the amount of abbreviation. For example:

| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 html-authored no-header |  |  |
| --- | --- | --- |
| **Original value** | **Abbreviation** | **Result** |
| $12,011,141.25 | Not selected | $12,011,141.25 |
| $12,011,141.25 | Selected, set to 1 | $12M |
| $12,011,141.25 | Selected, set to 2 | $12.0M |
| $12,011,141.25 | Selected, set to 2 | $12.011M |
| $12,011,141.25 | Select, set to 3 | $12.011M |

## Edit visualization

After you build the visualization, you can edit the original configuration.

- Select in the top-right corner of the visualization. You are now taken back to the original configuration view .
- Change the metric, primary date range, comparison date range, or segment as preferred.

Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
