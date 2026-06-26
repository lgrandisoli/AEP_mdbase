---
title: "Metrics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/apply-create-metrics"
category: "other"
topic: "analytics-platform/using/cja-components/apply-create-metrics"
created_at: "2026-06-23T20:43:02.886841+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Metrics

Last update: May 13, 2026
- Topics:
- [Metrics](#)

CREATED FOR:

- User

Metrics allow you to quantify data points in Analysis Workspace. They are most commonly used as columns in a visualization and tied to dimensions.

## Use metrics in Analysis Workspace

Metrics are flexible in their use within Analysis Workspace. Drag a metric to an empty Freeform table to see that metric trended over the project’s date period. You can also drag a metric when a dimension is present to see that metric compared to each dimension item. Dragging a metric on top of an existing metric header replaces it, and dragging a metric next to a header lets you see both metrics side-by-side.

For information about how to add metrics and other types of components to Analysis Workspace, see [Use components in Analysis Workspace](/en/docs/analytics-platform/using/cja-components/use-components-in-workspace).

## Types of metrics

Adobe offers several types of metrics for use in Analysis Workspace:

- Standard metrics : Example of standard metrics are People, Sessions, Events. Contrary to Adobe Analytics, Customer Journey Analytics allows you to define standard metrics in a flexible way within the scope of a connection and a data view. People : The People metric in Customer Journey Analytics is the count distinct of Person IDs. Depending on what you choose as the Person ID when you configure datasets in your connection, the People metric can mean different things. Sessions : The Sessions metric in Customer Journey Analytics is what you define as part of the configuration of the Sessions settings in your data view. See Session settings . Events : The Events metric in Customer Journey Analytics are comprised of the events that are part of any event dataset you have configured as part of your connection. See Standard metrics for the full list of standard metrics.
- Calculated metrics : User-defined metrics that are based on standard metrics, static numbers, or algorithmic functions.
- Calculated metric templates : Adobe-defined metrics that behave similarly to calculated metrics. You can use them as-is in Workspace projects, or save a copy to customize the logic. See Default calculated metrics .

You can see whether a metric is approved or not. If you want more details on a metric, hover over the metric, and select . See [Component info](/en/docs/analytics-platform/using/cja-components/use-components-in-workspace#component-info) for more information.

## Standard metrics

The full list of standard metrics in Customer Journey Analytics:

Component Name
Notes
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Accounts
Based on the Account ID specified in a Connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Buying Group
The buying groups, based on the Buying group ID specified in the Connection.
Events
The number of rows from all event datasets in a Connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Global Accounts
Based on the Global Accounts ID specified in the Connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Opportunities
The opportunities, based on the Opportunity ID specified in the Connection.
People
Based on the person ID specified in a Connection.
Session Ends
The number of events that were the last event of a session. Similar to Session Starts, it can also be used in a segment definition to segment things down to the last event of every session.

This component must be included in your data view for the following [calculated metric](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) to be available in Workspace:

- Session End Rate

Session Starts
The number of events that were the first event of a session. When used in a segment definition (for example, ‘Session Starts exists’), it segments down to just the first event of every session.

This component must be included in your data view for the following [calculated metric](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) to be available in Workspace:

- Session Start Rate

Sessions
Based on the data view’s session settings.
Time Spent (seconds)
Sums the time between two different values for a dimension.

This component must be included in your data view for the following [calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) to be available in Workspace:

- Time Spent Per Person
- Time Spent Per Session

## Create calculated metrics

Calculated metrics allow you to easily configure how metrics relate to each other, using simple operators or statistical functions. See [Calculated metrics overview](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/calc-metr-overview) for more information.

There are several ways to create calculated metrics. The method you choose determines whether the calculated metric is available from the component list across all projects, or only in the project where it was created.

### Create calculated metrics for all projects

You can use the [calculated metric builder](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics) to [create calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-workflow). When created in this way, calculated metrics are available in the component list and can then be used in projects throughout your organization.

### Create calculated metrics for a single project

You can quickly create a calculate metric that is available only for the project where it was created.

To create a calculated metric for a single project:

- In Analysis Workspace, open the project where you want to create the calculated metric.
- In a freeform table, right-click the column header of a single column. Or Select two columns while holding the Shift key, then right-click one of the selected columns.
- Select Create metric from selection
- To create a calculated metric for this project only, choose from the available options. When a single column is selected, the following options are available: Mean : Creates a new column that shows the mean value in the set of dimension elements for the column. This uses the Mean function. Median : Creates a new column that shows the median value in the set of dimension elements for the column. This uses the Median function. Column max : Creates a new column that shows the largest value in the set of dimension elements for the column. This uses the Column Maximum function. Column min : Creates a new column that shows the smallest value in the set of dimension elements for the column. This uses the Column Minimum function. Column sum :Creates a new column that adds all numeric values for a metric within a column (across the elements of a dimension). This uses the Column Sum function. When two columns are selected, the following options are available: Divide : Creates a new column that divides the values of the two selected columns. Subtract : Creates a new column that subtracts the values of the two selected columns. Add : Creates a new column that adds the values of the two selected columns. Multiply : Creates a new column that multiplies the values of the two selected columns. Percent change : Creates a new column that shows the percent change between the two selected columns.

## Compare metrics with different attribution models

To quickly compare one attribution model to another for a metric, select **Compare attribution models** from the context menu for a metric.

This shortcut lets you compare one attribution model to another without dragging in a metric and configuring it twice.

recommendation-more-help
