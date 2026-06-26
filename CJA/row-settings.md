---
title: "Row settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/table-settings"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:08:08.713417+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Row settings

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

Row settings vary depending on which component you have dragged into the table. To access table row settings, select **Settings** next to a dimension, segment, metric, time period, or a breakdown within each of these objects.

Setting
Description
Breakdown by position
By default, this setting is disabled and breakdowns are fixed to static row items. For example, imagine you breakdown the top 3 Page dimension items (Homepage, Search Results, Checkout) by Marketing Channel. Then, you leave the project and return two weeks later. Upon opening the project again, the top 3 pages have changed, and now Homepage, Search Results and Checkout are the top 4-6 pages instead. By default, your Marketing Channel breakdowns still appear under Homepage, Search Results and Checkout, even though they are now in rows 4-6.
In contrast,
Breakdown by position
always breaks down the top 3 items, regardless of what they are. Referring back to the example, when you re-open your project, the Marketing Channel breakdowns are tied to the top 3 pages in the table. And not to Homepage, Search Results and Checkout, which are now in rows 4-6.
Percentages
Calculate percentages by column
(default): the percentages visible in a cells are calculated based on the column total.
Calculate percentages by row
: the percentages in cells are calculated across the row, as opposed to down the column, with Grand total as the denominator. This calculation is useful for trending percentages.
Column totals
These settings are available only for
static rows
.
Show as sum of current rows
shows a client-side sum of the rows in the table, which means the total does
not
de-duplicate metrics like visits or persons.
Show grand total
shows a server-side sum, which means the total of de-duplicated metrics.
See [Row and column settings in a Freeform table](/en/docs/analytics-learn/tutorials/analysis-workspace/building-freeform-tables/row-and-column-settings-in-freeform-tables#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
## Change row count

To change the number of rows that are displayed:

- Click the number next to Rows at the top of the first column of the table.
- From the drop-down menu, select the number of rows you would like the table to display.

## Context-menu

The following context menu options are available when selecting the dimension header.

Option
Description
Copy selection to clipboard
Copy the selection from the visualization onto the clipboard.
Download items as CSV (
dimension name
)
Immediately download the dimension items (to a maximum of 50,000) of the visualization to your local device. A maximum of 50,000 dimension items for the selected dimension.
Download selection as CSV
Immediately download the dimension items of the visualization to your local device.
Create hyperlink for all dimension items
Create hyperlinks for all the dimension items. See
Hyperlinks for dimensions in a freeform table
Edit hyperlink for all dimension items
Edit hyperlinks for all the dimension items. See
Hyperlinks for dimensions in a freeform table
Remove hyperlink for all dimension items
Remove hyperlinks for all the dimension items. See
Hyperlinks for dimensions in a freeform table
Delete
Deletes the dimension from the table.
Visualize
Visualize the dimension using any of the available visualizations.
Display only selected rows
Display only the selected items in the visualization.
Create annotation from selection
Open up the
Annotation details
to add an annotation.
The following additional context menu options are available when selecting one or more dimension items (first column) or one or more individual cells in the freeform table.

Option
Description
Create hyperlink
Create a hyperlink for the item. See
Hyperlinks for dimensions in a freeform table
Edit hyperlink
Edit a hyperlink for the item. See
Hyperlinks for dimensions in a freeform table
Remove hyperlink
Remove a hyperlink for the item. See
Hyperlinks for dimensions in a freeform table
Breakdown
Break down the dimension item. Select from the list of
Dimensions
,
Metrics
,
Segments
or
Date ranges
. Alternative search for a component, using
Search
.
Delete selected
Delete the selected rows (items).
Trend selection
Create a trended line chart visualization for the selection.
Display only selected rows
Display only the selected rows in the visualization.
Display all rows
Display all rows in the visualization.
Create segment from selection
Open up the
Segment builder
to build a segment from the selection.
Create audience from selection
Open up the
Create audience
dialog to build an audience from the selection.
The following additional context menu options are available when selecting a metric column header.

Option
Description
Create metric from selection
Create a new metric from the selected metric. Metric can be Mean, Media, Column max, Column min, Column sum. You can also select Open in calculated metric builder to create a calculated metric.
Add time period column
Add a time period column. You are offered several options, where the calendar range of the panel determines the *date range*:

- Prior date range to this date range
- These date range to this date range .
- Custom date range to this date range . Opens up the Date range builder to specify the date range.

See [Date comparison](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/time-comparison) for more information.

Compare time periods
Adds compare time period columns. Only available when the dimension is not based on time. You are offered several options determines the *date range*:

- Prior date range to this date range
- Custom date range to this date range . Opens up the Date range builder to specify the date range.

See [Date comparison](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/time-comparison) for more information.

Modify attribution models
Modify the attribution model for the column.
Compare attribution model
Specify a new attibution model and compare it to the attribution model for the selected column. A new column is added with the new attribution model metrics. Also, a Percent change column is added for comparison.
Reset column widths
Reset the column widths to the default width.
Create annotation from selection
Open up the
Annotation details
to add an annotation.
Create segment from selection
Open up the
Segment builder
to build a segment from the selection.
Create audience from selection
Open up the
Create audience
dialog to build an audience from the selection.
## Change row height

You can set the [view density](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/view-density) of a project to **Compact**, **Comfortable**, and **Expanded**.

recommendation-more-help
