---
title: "Manage data sources manage-data-sources"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/t-sync-visualization"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:06.841075+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage data sources manage-data-sources

Last update: May 19, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

Synchronizing visualizations lets you control which freeform table or data source corresponds to a visualization.

TIP
You can tell which visualizations are related by the color of
next to the title of visualizations. Matching colors mean that visualizations are based on the same data source.
You can show or hide the data source. You can also lock the selection to selected positions or selected items. These settings determine how the visualization changes (or doesn’t change) when new data comes in.

Option
Description
Data source
Select the data source on which the visualization is based, from the drop-down menu.
Linked visualizations
Lists all linked visualizations. Applies to the data source (freeform table).
Show data source
Lets you show or hide the data source (freeform table) that corresponds to the visualization.
Lock Selection
Select this option to lock the visualization to the data currently selected in the corresponding data table. Once enabled, select between:

- **Selected Positions**: The visualization is locked on the **positions** that are selected in the corresponding data table. These positions continue to be visualized, even if the specific items in these positions change (for example due to sorting or filtering). For example, select this option if you want to show the top five campaign names listed in the data source in this visualization at all times. No matter which campaign names show up.
- **Selected Items**: The visualization is locked on the specific **items** currently selected in the corresponding data table. These items continue to be visualized, even if they change their ranking among items in the table. For example, select this option if you want to show the same five specific campaign names listed in the data source in this visualization at all times. No matter how those campaign names rank.

If the visualization is locked to data that is no longer visible in the connected data table, you can generate a new table. Select **Show table** to generate a new datasource for your current visualization, separate from the original data source.

recommendation-more-help
