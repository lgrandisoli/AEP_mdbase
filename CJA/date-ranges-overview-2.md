---
title: "Date ranges overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-date-ranges/overview"
category: "overview"
topic: "analytics-platform/using/cja-components/cja-date-ranges"
created_at: "2026-06-23T20:43:04.225075+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Date ranges overview

Last update: May 13, 2026
- Topics:
- [Calendar](#)

CREATED FOR:

- User

In a Workspace project, you typically use the [calendar in a panel](/en/docs/analytics-platform/using/cja-workspace/panels/panels#calendar) to specify the date range for the visualizations in that panel.

Date range components enable you to define and override the calendar settings for the panel.

## Use date ranges

You can use a date range component to redefine the calendar for the panel.

Or, you can use a date range in a Freeform table as a metric or dimension.

- **Metric**. For example, to compare a dimension for two different months for a specific metric.
- **Dimension**. To compare a metric on different dimension items for the date range dimension.

NOTE
When you use date ranges in a Freeform table, the date ranges override the calendar specified for the panel to which the Freeform table belongs.
You use a date range as you would [use any component](/en/docs/analytics-platform/using/cja-components/overview#analysis-workspace-components). You drag the date range from the **Date ranges** component panel and drop the component on:

- **Calendar**: You **Replace** the current calendar configuration with the date range.
- **Metric column header**: You **Replace** the metric, **Add** the date range as a metric, or **Filter** the metric using the date range component.
- **Dimension column header**: You **Replace** the current dimensions. The new dimension is now **Date ranges**. Once the dimension is Date ranges, you can **Add** additional date ranges as dimension items.
- **Dimension item**: You **Breakdown** the specific dimension item by the date range.

You can also add a date range column directly in a Freeform table visualization:

- In a metric column, select from the context menu: Add time period column . You can select between suggested options that are based on the current calendar or create a custom date range . Compare time periods . You can select between a suggested option that is based on the current calendar or create a custom date range .
- Based upon your selection, additional date range columns are added to the Freeform table.

## Default date ranges

Analysis Workspace provides a number of default date ranges.

Day
Week
Month
Quarter
Year
Today
This week
This month
This quarter
This year
Yesterday
This week (excluding today)
This month (excluding today)
This quarter (excluding today)
This year (excluding today)
2 days ago
2 weeks ago
2 months ago
3 days ago
3 weeks ago
3 months ago
Last 7 days
Last week
Last month
Last quarter
Last year
Last 14 days
Last 2 full weeks
Last 2 full months
Last 4 full quarters
Last 30 days
Last 3 full weeks
Last 3 full months
Last 60 days
Last 4 full weeks
Last 6 full months
Last 90 days
Last 12 full weeks
Last 12 full months
Last 7 full days
Last 52 full weeks
Last 13 full months
Last 14 full days
Last 30 full days
Last 90 full days
## Custom date ranges

You can create your own custom date ranges. See [Create date range](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/create) for the various options available to create date ranges. You then build, modify, and save date ranges in the [Date range builder](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/create#date-range-builder).

You use the [Date range manager](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/manage) to manage date ranges.

recommendation-more-help
