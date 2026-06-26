---
title: "Totals workspace-totals"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/workspace-totals"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:45:01.801654+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Totals workspace-totals

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

In Freeform tables, a total row appears at each breakdown level and can show two totals:

- **Table total** ➊ - This total is typically equal to or a subset of the Grand total. The total reflects any table segments applied within the freeform table, including the Include None option.
- **Grand total** (**out of** *number*) ➋ - This total represents all events that have been collected. When a segment is applied either at the panel level or within the freeform table, this total adjusts to reflect all events that match the segment criteria.

## Display totals

Under **Column settings**, there are options to **Show totals** and **Show grand total**. If these settings are unchecked, totals are removed from the table, which may be desired in cases where totals don’t make sense.

In a freeform table that contains [static rows](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/manual-vs-dynamic-rows), totals behave differently. And are controlled using **Row Settings**.

Option
Description
Show sum of current rows as the total
Show a client-side sum of the rows in the table. This total does
not
de-duplicate metrics like sessions or persons.
Show grand total
Show a server-side sum. This total de-duplicate metrics like sessions or persons.
See [Dynamic vs static dimension items in freeform tables](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/manual-vs-dynamic-rows).

## Frequently asked questions

Questions
Answer
Which
total
are the gray column percentages based on?
This *total* depends on the **Percentages** setting selection under **Row Settings**:

- Calculate percentages by column - This setting is the default. Percentages are based on the Table total.
- Calculate percentages by row - Percentages are based on the Grand total.

How does the
Include “No value”
setting impact totals?
If the
Include “No value”
setting is unchecked, the
No value
row is removed from the table, the Table total, and carries through to any calculated metrics that use
Total
metric types
.
When custom table segments are applied to a freeform table, do all of my calculated metrics and conditional formatting account for the segment?
Not currently. **Include “No value”** is account for, but custom table segments do not impact the following:

- The column max / min range that conditional formatting uses looks across all data.
- Calculated metrics that leverage **Grand total** metric types.
- Calculated metrics with functions that calculate across rows in a freeform table: Column Sum, Column max, Column min, Count, Mean, Median, Percentile, Quartile, Row Count, Standard Deviation, Variance, Cumulative, Cumulative Average, Regression variants, T-Score, T-Test, Z-Score, and Z-Test.

In Calculated Metrics, what does the
Grand total
metric type reflect?
Grand total
continues to refer to the
Grand total
, and does not reflect segments applied to a table or the
Table total
.
What total is shown when data is either copied and pasted from a freeform table or downloaded via CSV?
The total row reflects the
Table total
only and respects the column
Show totals
setting.
recommendation-more-help
