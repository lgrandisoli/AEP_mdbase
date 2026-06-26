---
title: "Dynamic and static dimension items"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/manual-vs-dynamic-rows"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:23.729234+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Dynamic and static dimension items

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

In Freeform tables, the rows and columns can contain various component values. These values can be dynamic (change over time) or static (do not change over time), depending on the analysis that you want to build.

## Dynamic dimension items

Dynamic dimension items change over time and are dependent on the metric being sorted by in the freeform table. Dynamic dimension items are preferred when you want to analyze the top items for a given time period.

When you drop a dimension into a freeform table, dynamic rows are returned. Dynamic rows represent the top items that correspond to the dimension for a given metric and time period. You can also drop a dimension into freeform table columns and the dimension automatically expands into the top 5 dimension items.

For example, when you drag the Browser Type dimension into the table, the top Browser Type dimension items (e.g. Microsoft, Apple, Google, etc.) dynamically return to the table rows. If dropped into a column, the top 5 Browser Type dimension items dynamically return.

Dynamic dimension items have the row filter option and a , and do **not** have a lock present. do they have the lock icon? When you click next to a dynamic dimension item, a filter is automatically applied. For more information about applying filters to tables, see [Filter and sort tables](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/filter-and-sort).

## Static dimension items

Static dimension items do not change with time; they are fixed components that are always returned in a freeform table. Static dimension items are preferred when you want to always analyze the same item, whether it be specific campaigns or specific days in the week.

Any time you manually select and drop specific component values (dimension, metric, segment, date range) into a table, the result is a static list of rows or columns.

For example, when you drag over specific Browser Type items such as Microsoft and Apple, those 2 specific items always get pulled into the table.

Static dimension items can also be created if you choose to select **Display only selected rows** from the context menu for selected rows.

Static dimension items do **not** have the row filter option. Instead, a and are present on each item. Select to remove that dimension item from the table.

## Mixed dimension items

Dimension items from different dimensions can be added to the same table. The row header say **Mixed Dimensions** in these cases. These dimension items are static. For example, adding specific dimension items from the Browser Group dimension and other dimension items from the Browser Name dimension.

## Freeform total rows

Dynamic and static rows behave differently in the freeform total row. By default:

- Dynamic rows are summed server-side and de-duplicate metrics such as sessions or persons.
- Static rows are summed client-side and do **not** de-duplicate metrics. To calculate the total row server-side, change the Row setting to **Show grand total**. [Learn more](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/workspace-totals)

recommendation-more-help
