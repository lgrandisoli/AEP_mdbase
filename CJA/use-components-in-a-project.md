---
title: "Use components in a project"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/use-components-in-workspace"
category: "other"
topic: "analytics-platform/using/cja-components/use-components-in-workspace"
created_at: "2026-06-02T19:06:08.158942+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use components in a project

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

Components make up the actual data of any project in Analysis Workspace. Components consist of dimensions, metrics, segments, and date ranges. You can add components to a project by dragging them into visualizations or panels.

See the [Components overview](/en/docs/analytics-platform/using/cja-components/overview) for more information on the types of components that you can add.

TIP
For information about each component, use
. See
Component info
for more information
## Add components to a project

- Create a project in Analysis Workspace .
- Add a panel or add a visualization to the project in Analysis Workspace. If you add a component to a blank project, a freeform table visualization is already created for you.
- Select Components from the button panel. You see all available components in the left panel. See Interface for more details.
- Scroll to or search for the component that you want to add, then drag it to a panel or visualization within your project.
- You can optionally drag a component to the segment drop zone in a panel header. This drag and drop defines the component as a segment and applies the segment to all the content within the panel. For information about how you can use the segment drop zone on a panel to segment your panel, see Drop zone in Panels overview .
- For more detailed information, see the following sections: Add dimensions to a project Add metrics to a project Add segments to a project Add date ranges to a project

### Add dimensions to a project

[Dimensions](/en/docs/analytics-platform/using/cja-components/dimensions/overview) are variables in Customer Journey Analytics that typically contain string values. In contrast, [metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/calc-metr-overview) contain numeric values that tie to a dimension. A basic report shows rows of string values (dimension), against a column of numeric values (metric).

- Start adding a dimension to your project in Analysis Workspace, as described in Add components to a project .
- Choose one of the following methods to add dimensions and determine the type of data you want to analyze: Drag a dimension to a visualization (such as a freeform table) in Analysis Workspace. Drag one or more dimensions from the left panel onto the segment drop zone to create a quick segment, as described in Add segments to a project .
- You can optionally break down dimensions and dimension items in Analysis Workspace with other components. For more information, see Break down dimensions in Workspace .

For more information about how to use dimensions in Analysis Workspace, see [Preview dimensions](/en/docs/analytics-platform/using/cja-components/dimensions/view-dimensions), [Break down dimensions](/en/docs/analytics-platform/using/cja-components/dimensions/t-breakdown-fa), and [Time-parting dimensions](/en/docs/analytics-platform/using/cja-components/dimensions/time-parting-dimensions).

### Add metrics to a project

Metrics allow you to quantify data points in Analysis Workspace. They are most commonly used as columns in a visualization and tied to dimensions.

To add a metric to a project in Analysis Workspace:

- Start adding a metric to your project in Analysis Workspace,as described in Add components to a project .
- Choose one of the following methods to add a metric in Analysis Workspace: Drag a metric to the metric drop zone in an empty Freeform table to see that metric trended over the project’s date period. Drag a metric when a dimension is present to see that metric for each dimension item. Drag a metric on top of an existing metric header to replace it. Drag a metric next to the left of right side of an existing metric header to add the new metric. Drag a metric above or below an existing metric header to create a metric overlap.

For more information about metrics, see [Metrics](/en/docs/analytics-platform/using/cja-components/apply-create-metrics).

### Add segments to a project

[Segments](/en/docs/analytics-platform/using/cja-components/segments/seg-overview) allow you to identify subsets of persons, sessions or events based on characteristics or specific interactions.

You can use segments in Analysis Workspace in any of the following ways:

- Add segments to a panel When you add segments to a panel, the segments apply to all content within the panel. For information about how you can use the segment drop zone on a panel to segment your panel, see Drop zone in Panels overview .
- Add segments to a visualization When you add segments to a column in a freeform table, the segments apply to all content within the table column. You can also add segments as part of a fallout visualization.
- Use segments in components Whe you define components like calculated metrics , annotations , or even segments you can use segments as part of the definition.

### Add date ranges to a project

[Date ranges](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/overview) determine the reporting time frame in Analysis Workspace, and can be applied to one or more panels within a project and also to some visualizations (like the Freeform table).

Each panel includes a date range by default. There are multiple ways to update a date range for a panel. One way to update a date range for a panel in Analysis Workspace is to drag a date range component from the left panel:

- Optionally, add a date range to your project in Analysis Workspace, as described in Add components to a project .
- Drag and drop a date range from the left panel onto: The current date range, to modify the date range for the panel. A metric or dimension in a Freeform table visualization. See Use date ranges for more information.

For more information about how to use and manage date ranges in Analysis Workspace, see [Date ranges overview](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/overview).

## Component info

You can hover over any component to display . When selected, a popup is displayed with additional information on the component.

Based on your access control, you can:

- Access the Data dictionary definition for the component.
- Access the component builder or data view where the component is defined.

recommendation-more-help
