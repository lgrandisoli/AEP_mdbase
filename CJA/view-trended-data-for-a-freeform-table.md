---
title: "View trended data for a freeform table"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table-trended-data"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:08:37.854016+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# View trended data for a freeform table

Last update: May 13, 2026
- Topics:
- [Freeform Tables](#)

CREATED FOR:

- User
- Admin

You can view the trend of the data that is included in a freeform table. This trended data shows in the following areas within Analysis Workspace:

- Sparklines
- Line visualizations

## Use sparklines to view trended data

Sparklines are shown in the metric column header of freeform tables.

Sparklines always include:

- Trended data for all data in the column
- Any search filter criteria applied to the table dimension For more information, see Filter and sort .

## Use line visualizations to view trended data

[Line](/en/docs/analytics-platform/using/cja-workspace/visualizations/line) visualizations display the data of the freeform table they are connected to.

### Connect a line visualization to a freeform table

Depending on how and when the line visualization was added to the project, it might already be connected to the desired freeform table. Use the following steps to check or to manually connect it:

- Add a line visualization to an Analysis Workspace project.
- Select the dot next to the visualization name, select the Data source tab, then select the name of the freeform table that you want to connect to the line visualization.

### Choose the data that is included in the line visualization

The data that is included in the connected line visualization differs, depending on which cell is selected in the freeform table.

To view a trend of all data in the freeform table, select the sparkline cell in the freeform table.

When the sparkline cell is selected, the cell displays as dark gray.

When the sparkline cell of the connected table is selected, line visualizations include:

- Trended data for all data in the column
- Any search filter criteria applied to the table dimension For more information, see Filter and sort .

When the sparkline of the connected table is not selected, line visualizations include:

- Data for the row that is selected in the connected table. If no row is selected, data for the first dimension only of the connected table is shown.
- Any search filter criteria applied to the table dimension is ignored For more information, see Filter and sort .

## Include filter criteria in connected line visualizations

For information about when filter criteria is included in connected line visualizations, see [Include filter criteria in trended data in sparklines and line visualizations](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/filter-and-sort#include-filter-criteria-in-trended-data-in-sparklines-and-line-visualizations)

recommendation-more-help
