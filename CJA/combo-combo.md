---
title: "Combo combo"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/combo-charts"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:05.377166+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Combo combo

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
*This article documents the Combo visualization in* *Customer Journey Analytics .*

*See Combo for the* *Adobe Analytics version of this article.*

style
shade-box
The **Combo** visualization makes it easy to build quickly a comparison visualization without having to build a table first. You can easily view trends in your data in a line/bar combination.

Use a Combo to:

- Compare this week’s orders to orders at the same time last month (and last year).
- Quickly analyze and compare multiple metrics (like Persons and Revenue) against one another on the same chart.
- Analyze a metric against a function (such as Cumulative Average) over a time horizon.

Keep in mind that:

- You can add multiple comparisons in a single Combo chart.
- If you add one or more comparisons, they have to be of the same type, such as Time comparison.
- You can add up to 5 comparisons.
- You can apply up to 3 segments to a metric.
- Calculated metrics are not supported in Combo charts.

## Use

- Add a Combo visualization. See Add a visualization to a panel
- From the drop-down menus, select a dimension for the X-axis and a metric for the Y-axis.
- Select the type of Line comparison that you want to use. table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto Line comparison type Definition Time comparison The most common type of comparison - comparing this time period to 4 weeks ago, for example. If you selected Time comparison, make a secondary selection as to which time period you want to compare. Function You could introduce a function like Average into the comparison. See the list of supported functions . Secondary metric You could, for example, compare Revenue to another metric.
- Select Build . The output looks similar to: The current period is shown in the bar chart. The line chart represents the comparison period. The dots on the line chart are known as bar bells .

## Supported functions

If you select **Function** as the Line comparison type, a function of the metric chosen is returned.

Function
Definition
Column Sum
Adds all numeric values for a metric within a column (across the elements of a dimension)
Cumulative Average
Return the average of the last N rows.
Median
Returns the median for a metric in a column. The median is the number in the middle of a set of numbers. Half the numbers have values that are greater than or equal to the median, and half the number have values that are less than or equal to the median.
Cumulative
The cumulative sum of N rows.
Column Maximum
Returns the largest value in a set of dimension elements for a metric column.
Mean
Returns the arithmetic mean, or average, for a metric.
Column Minimum
Returns the smallest value in a set of dimension elements for a metric column.
Here is an example of the cumulative average of the Revenue metric:

Here is an example of a combo chart with both Cumulative average and Mean functions:

Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
