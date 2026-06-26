---
title: "Configure a fallout visualization configure-fallout-visualization"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/configuring-fallout"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:07:58.285033+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure a fallout visualization configure-fallout-visualization

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

You can specify **touchpoints** to create a multi-dimensional fallout sequence. In many cases, a touchpoint is a page on your site. However, touchpoints are not limited to pages. For example, you can add events, such as units, as well as unique persons and return visits. You can also add dimensions, such as a category, browser type, or internal search term.

You can even add segments within a touchpoint. For example, you might want to compare segments, such as iOS and Android users. Drag the desired segments to the top of the fallout and information about those segments is added to the fallout report. If you want to show only those segments, you can remove the All People baseline.

Fallout visualizations have no limitation on the number of touchpoints you can add or the number of components you can use.

You can do pathing on dimensions, metrics, and segments. For example, suppose that someone is looking at shoes, shirt on one page, and on the next page they’re looking at shirt, socks. The next product flow report from shoes will be shirt and socks, NOT shirt.

## Use

- Add a Fallout visualization. See Add a visualization to a panel .
- Drag a component to the Add touchpoint drop-down menu. note tip TIP You can add a single page to the fallout report, rather than the entire dimension. Click the right arrow on the page dimension to pick a specific page, such as home , to add to the Fallout report.
- Continue adding touchpoints until your sequence is complete. The circled numbers in the gray portion of the bar show the fallout between touchpoints (not the overall fallout to that point). The circled numbers in the green portion of the bar show the successful fall through from the previous touchpoint to the current touchpoint. When adding touchpoints, you can do any of the following: Combine multiple components by dragging one or more additional components onto a single touchpoint. note NOTE Multiple segments are joined with AND, but multiple items such as dimension items and metrics are joined with OR. Reorder touchpoints by dragging them to a different level within the fallout hierarchy. Combine two touchpoints by dragging one touchpoint onto another. Drop the touchpoint when you see the word Combine . Constrain individual touchpoints to the next event (as opposed to eventually ) within the path. Beneath each touchpoint, there is a selector with the options Eventual path and Next event , as shown here: table 0-row-2 1-row-2 2-row-2 Option Description Eventual path (default) Persons are counted that will eventually land on the next page in the path, but not necessarily on the next event. Next event Persons are counted that will land on the next page in the path on the very next event. Hover over a touchpoint to see the fallout and other information about that level. Information includes the touchpoint’s name, the person count, and success rate. You can also compare the success rate to other touchpoints.

## Settings settings

As part of the visualization, specific settings are available.

Fallout container
Description
Session
or
Person
Switch between Session and Person to analyze person pathing. The default is Person. These settings help you understand person engagement at the person level (across sessions), or constrain the analysis to a single session.
## Context menu

As part of the visualization, specific context menu options are available.

### Access the context menu

You can access the context menu in either of the following ways:

- Hover over a touchpoint in the visualization, then select Click to analyze .
- Right-click a touchpoint in the visualization.

### Context menu options

The following context menu options are available:

Option
Description
Trend touchpoint
See trend data for a touchpoint in a line graph, with some pre-built anomaly detection data.
Trend touchpoint (%)
Trends the total fallout percentage.
Trend all touchpoints (%)
Trends all the touchpoint percentages in the fallout (except
All People
, if it’s included), on the same chart.
Break down fallthrough at this touchpoint
View what persons did between two touchpoints (this touchpoint and the next touchpoint) if they continued to the next touchpoint. This creates a freeform table showing your dimensions. You can replace dimensions and other elements of the table. For example, a table that is labeled
Fallthrough: All People > Page equals any of home
and contains
Page
as the dimension and
People
segmented by the
project-only quick segment
Fallthrough: All People > Page equals any of home
as the metric. Inspect the segment to understand how the fallthrough segment is determined.
Break down fallout at this touchpoint
View what people who did not make it through the funnel did immediately after the selected step. This creates a freeform table showing your dimensions. You can replace dimensions and other elements of the table. For example, a table that is labeled
Fallout: People > Page equals any of home
and contains
Page
as the dimension and
People
segmented by the
project-only quick segment
Fallthrough: All Visitors > Page equals any of home
segment as the metric. Inspect the segment to understand how the fallout segment is determined.
Create segment from touchpoint
Create a new segment from the selected touchpoint.
Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
