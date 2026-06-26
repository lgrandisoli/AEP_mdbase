---
title: "Freeform table overview freeform-table-overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table"
category: "overview"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:05.823290+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Freeform table overview freeform-table-overview

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
*This article documents the Freeform table visualization in* *Customer Journey Analytics .**See Freeform table for the* *Adobe Analytics version of this article.*

style
shade-box
In Analysis Workspace, a **Freeform table** visualization is the foundation for interactive data analysis. You can drag and drop a combination of [components](/en/docs/analytics-platform/using/cja-components/overview) into rows and columns to create a custom table for your analysis. As each component is dropped, the table updates immediately so you can quickly analyze and dig deeper.

To create and configure a Freeform table:

- Add a **Freeform table** visualization. See [Add a visualization to a panel](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#add-visualizations-to-a-panel).

## Automated tables

The quickest way to build a table is to drop components directly into a blank project, panel or freeform table. A freeform table is built for you in a recommended format. [Watch the tutorial](/en/docs/analytics-learn/tutorials/analysis-workspace/building-freeform-tables/auto-build-freeform-tables-in-analysis-workspace).

## Freeform table builder

If you prefer to add several components to your table first, then render the data, you can select **Enable table builder**. With the builder enabled, you can drag and drop dimensions, breakdowns, metrics and segments to build tables that answer more complex questions. Data updates once you select **Build**.

## Interactions

You can interact with and customize a freeform table in a variety of ways:

### Filter and sort

- You can [filter and sort](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/filter-and-sort) the data in a table.

### Rows

- You can quickly [create a new visualization](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#visualize) from one or more rows using .
- You can fit more rows into a single screen by adjusting the project’s [view density](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/view-density).
- Each dimension row can show up to 400 rows, before pagination occurs. Select the number next to **Rows** in the first column header, to show more rows on a page. Navigate to a different page using in the first column header.
- You can break down rows by additional components. To break down many rows at once, select multiple rows and then drag the next component on top of the selected rows. Learn more about [breakdowns](/en/docs/analytics-platform/using/cja-components/dimensions/t-breakdown-fa).
- Rows can be [segmented](/en/docs/analytics-platform/using/cja-components/segments/seg-overview) to show a reduced set of items. Additional settings are available under [Row settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/table-settings).

### Columns

- Components can be stacked within columns to create segmented metrics, cross-tab analysis and more.
- Each column’s view can be adjusted under the [column settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/column-settings).
- Several actions are available through the [context menu](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#context-menu). The menu provides different actions depending on if you select the table header, rows, or columns.

## Settings

Select to display **Table settings**. The following specific visualization [settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#settings) are available:

### Data source

Option
Description
Linked visualizations
.
Lists all linked visualizations.
Show data source
When unchecked, the freeform table that functions as the data source for the visualization is hidden in Workspace.
### Settings

Option
Description
Align dates from each columns to all start on the same row
To align or not align dates from each columns to all start on the same row.
## Context menu

The following [context menu](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#context-menu) options are available from the header of the visualization:

Option
Description
Insert copied visualization
Paste (insert) a copied visualization to another place within the project, or into a completely different project.
Copy data to clipboard
Copy data from the visualization onto the clipboard.
Copy selection to clipboard
Copy the selection from the visualization onto the clipboard.
Download items as CSV (
dimension name
)
Immediately download the dimension items (to a maximum of 50,000) of the visualization to your local device. A maximum of 50,000 dimension items for the selected dimension.
Copy visualization
Copy the visualization, so that you can insert the visualization to another place within the project, or into a completely different project.
Download data CSV
Immediately download the displayed data of the visualization to your local device.
Export full table…
Export the full table to a designated cloud locations. See
Exports Customer Journey Analytics reports to the cloud
Duplicate visualization
Make an exact duplicate of the visualization.
Edit description
Add (or edit) a text description for the visualization. See
Text
.
Get visualization link
Copy and share a link directly to the visualization. A Share link dialog displays the link. Select Copy to copy the link to your clipboard.
Start over
Delete the configuration for the current visualization so you can re-configure it from scratch.
Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
