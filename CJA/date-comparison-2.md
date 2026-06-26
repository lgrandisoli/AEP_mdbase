---
title: "Date comparison"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-date-ranges/time-comparison"
category: "other"
topic: "analytics-platform/using/cja-components/cja-date-ranges"
created_at: "2026-06-23T20:45:59.013457+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Date comparison

Last update: May 13, 2026
- Topics:
- [Calendar](#)

CREATED FOR:

- User

Date comparison in Analysis Workspace lets you take any column containing a date range and create a common date comparison, such as: year-over-year, quarter-over-quarter, month-over-month, and so forth.

## Compare time periods

Analysis requires context, and often that context is provided by a previous time period. For example, the question *How much better or worse are you doing now compared to this time last year?* is fundamental to understanding your business. Date comparison includes a *difference* column automatically, which shows the percentage change compared to a specified time period.

- Create a Freeform table , with any dimensions and metrics you want to compare over a time period.
- Set the time period on the panel or column to determine the comparison time frame, and whether it is a rolling or fixed time comparison. To create a rolling time comparison, set the panel or column date range to a rolling date range (such as Last 7 days , Last 30 days , and so forth). To create a fixed time comparison, set the panel or column date range to a custom date range.
- Open the context menu for a table row and select Compare time periods . note NOTE This context menu option is disabled for metric rows, date range rows, and time dimension rows.
- Depending on how you have set the table’s date range, you have these options for comparison: table 0-row-2 1-row-2 2-row-2 3-row-2 Option Description Prior x weeks / months / quarters / years to this date range Compare to the selected date range immediately before this date range. These x weeks / months / quarters / years last year to this date range Compare to the same date range a year ago. Custom date range to this date range Let you define a custom date range. note NOTE When you select a custom number of days, for example October 7 - October 20 (a 14-day range), you will get only 2 options: Prior 14 days before this date range , and Custom date range to this date range .
- The resulting comparison looks like this: Rows in the Percent change column appear red for negative values and green for positive values.

## Add a time period column for comparison

You can now add a time period to each column in a table, enabling you to add a time period that is different from the one your calendar is set to.

- Right-click a column in the table and select Add time period column .
- Depending on how you have set the table’s date range, you have these options for comparison: table 0-row-2 1-row-2 2-row-2 3-row-2 Option Description Prior x weeks / months / quarters / years to this date range Add a column with the week/month/etc. immediately before this date range. These x weeks / months / quarters / years last year to this date range Add the same date range a year ago. Custom date range to this date range Let you create a custom date range. note NOTE When you select a custom number of days, for example October 7 - October 20 (a 14-day range), you will get only 2 options: Prior 14 days before this date range , and Custom date range to this date range .
- The time period is inserted on top of the column that you selected:
- You can add as many time columns as you want, as well as mix and match different date ranges:
- In addition, you can sort on each column, which changes the order of days depending on the column you are sorting on.

## Align column dates to start on the same row

You can align the dates from each column to all start on the same row.

For example, you do a day-over-day comparison for the last week (ending October 5, 2024) and the previous week. By default the left column will start with September 22 and the right column will start with September 29.

You can enable **Align dates from each column to all start on the same row** in [Settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table#settings-1) for the Freeform table visualization to align column dates to start on the same row.

Consider the following when using this option:

- This setting is enabled by default for all new projects.
- This setting applies to the entire table. For example, if you change this setting for a breakdown within the table, the setting is applied to the entire table.

recommendation-more-help
