---
title: "Visualizations overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations"
category: "overview"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:42:13.832098+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Visualizations overview

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

Workspace offers a number of visualizations that let you generate visual representations of your data. Such as bar charts, donut charts, histograms, line charts, maps, scatterplots, and others.

## Types

The following visualization types are available in Analysis Workspace:

Icon
Name
Description
Area
An area graph visualization. Like a line graph, but with a colored area below the line. Use an area graph when you have multiple metrics and want to visualize the area expressed by the intersection of two or more metrics.
Bar
A bar graph visualization with vertical bars representing various values across one or more metrics.
Bar stacked
A stacked bar graph visualization with vertical bars representing various values across one or more metrics.
Bullet
A bullet graph visualization, which shows how a value you are interested in compares to or measures against other performance ranges (goals).
Cohort table
A cohort visualization is a group of people sharing common characteristics over a specified period. A cohort table is useful for retention, churn or latency analysis.
Combo
A combo chart enables you to build quickly a comparison visualization without having to build a table first.
Donut
Similar to a pie chart, a donut visualization shows data as parts or segments of a whole.
Fallout
A fallout visualization shows where persons left (fell out) and continued through (fell through) a predefined sequence of pages.
Flow
A flow visualization shows exact customer paths through your websites and apps.
Freeform table
A freeform table visualization is an interactive visualization. The freeform table visualization is the foundation for data analysis in Workspace.
Histogram
A histogram visualization buckets persons, visits or events into buckets based on a metric volume.
Horizontal bar
A horizontal bar visualization shows horizontal bars representing various values across one or more metrics.
Horizontal bar stacked
A stacked horizontal bar visualization shows horizontal bars representing various values across one or more metrics.
Journey canvas
A journey canvas visualization helps you to analyze and gain insights on the journeys that you provide to your users and customers.
Key metric summary
A Key metrics summary visualization combines the line, summary change, and summary number visualizations.
Line
A line visualization represents metrics using a line to show how values change over a period of time. A line chart uses time along the x-axis.
Scatter
A scatterplot visualization shows the relationship between dimension items and up to three metrics.
Section header
To identify and articulate sections within a panel.
Summary change
A summary change visualization shows the change between the selected cells as one large number or percentage.
Summary number
A summary number visualization shows the selected cell as one large number.
Text
A text visualization lets you add user-defined text to your Workspace. Helpful for adding additional context to your analysis and insights, in addition to leveraging panel/visualization descriptions
Treemap
A treemap visualization displays hierarchical (tree-structured) data as a set of nested rectangles.
Venn
A venn visualization uses circles to depict the metric overlap of up to 3 segments.
## Add visualizations to a panel

See [Add visualizations to the freeform panel](/en/docs/customer-journey-analytics-learn/tutorials/analysis-workspace/panels/add-components-to-the-freeform-panel#_blank) for a demo video.

style
shade-box
- Open the Workspace project where you want to add a visualization.
- Use any of the following methods to add the visualization: In the left panel, select Visualizations , then drag a visualization to the panel where you want to add the visualization to. On the panel where you want to add the visualization, select , then choose the icon that represents the visualization that you want to add. Hover over the icon for each visualization to see the name. Add a blank panel , then select the visualization that you want to add. From the context menu of an existing visualization in your Analysis Workspace project, select Duplicate visualization or Copy visualization . Use the Workspace Insert menu to insert a visualization. From the context menu in a Freeform table, select Visualize . Then select the visualization from the submenu. Based on the current selection in the table, Workspace determines which visualization to offer and interprets the data to build the requested visualization.

When you add a simple visualization, for example a [Line](/en/docs/analytics-platform/using/cja-workspace/visualizations/line) of [Bar](/en/docs/analytics-platform/using/cja-workspace/visualizations/bar) visualization, the visualization uses the closest freeform table as the data source. You can always modify the [data source](#data-source) of a your visualizations.

## Manage visualizations

You can manage a visualization when you hover over the visualization or select the visualization.

- To collapse a visualization, select .
- To reveal a collapsed visualization, select .
- To delete a visualization, select . To undo, select **Edit** > **Undo** (*cmd+z* | *ctrl+z*).
- To return a visualization to the default height, select .
- To move a visualization within a panel, drag and drop the visualization whenever a is visible (ususally when you hover over the header).

## Legend

A visualization legend helps you to relate date in a source table to plotted series in the visualization. The legend is interactive - you can select a legend item to show/hide a series in the visualization, which is helpful if you want to simplify the data being visualized.

Additionally, you can rename legend labels to help you make visuals more consumable. Note: legend editing does **not** apply to: Treemap, Bullet, Summary Change/Number, Text, Freeform, Histogram, Cohort or Flow visualizations.

To edit a legend label:

- Right-click one of the legend labels.
- Click Edit Label .
- Enter the new label text.
- Press Enter to save.

## Settings

Each visualization has its own settings. To access visualization settings, select **Settings** in the visualization header to show a popup.

Depending on the visualization, you can configure

- details for the source of data of the visualization through the **Data source** tab, and
- settings for the visualization through the **Settings** tab.

### Data source

You can control which data source and items or positions within that data source correspond to a visualization. See [Manage data sources](/en/docs/analytics-platform/using/cja-workspace/visualizations/t-sync-visualization) for more information.

### Settings

Which visualization settings are available depends on the visualization. The table below summarizes the most common settings. Some visualizations do have specific settings. See the individual visualization documentation for more details.

Option
Description
Visualization type
Change the type of visualization used to visualize the data.
Granularity
Change the time granularity for trended visualizations. This change also applies to the data source table.
Percentages
Display values in percentages.
100% stacked
Turn the chart into a 100% stacked visualization. Only applicable for an area, bar and horizontal bar stacked visualization.
Legend visible
Show the legend text.
Limit max items
Limit the number of items that a visualization displays. When selected, define the number of max items.
Show annotations
Show the annotations made for this visualization.
Hide title
Hide the title of the visualization.
Anchor y-axis at zero
Force the bottom of the y-axis to zero. If all the values plotted on the chart are considerably above zero, the chart default makes the bottom of the y-axis non-zero. If you enable this option, the y-axis is forced to zero (and the chart is redrawn).
Display dual axis
Display left and right y-axes for two different metrics. This option only applies if you have two metrics. Dual axes are helpful when plotted metrics are of different magnitudes.
Show x-axis
Show the x-axis in the visualization.
Show y-axis
Show the y-axis in the visualization.
Show barbells on lines
Show barbells on the line visualization in a combo chart visualization.
Normalization
Force metrics to equal proportions. Equal proportions are helpful when plotted metrics are of different magnitudes.
Show anomalies
Enhance line graphs and freeform tables by displaying anomaly detection. Anomaly detection in line visualizations includes an expected value (dashed line) and an expected range (shaded band).
Show forecast
Enhance line graphs and freeform tables by displaying forecast values.
Show min
Show the minimal value in the visualization.
Show max
Show the maximal value in the visualization.
Show trendline
Show a trendline in the visualization. When selected, you can select the type of trendline from the drop-down menu.
You can customize the settings for all visualizations that you create. For more information, see [User preferences](/en/docs/analytics-platform/using/cja-workspace/user-preferences).

## Context menu right-click

Use the context menu (available through alternate select, for example, right-click when using a mouse) on a visualization header to access additional functionality for a visualization. Not all options are available for all visualizations.

Option
Description
Insert copied visualization
Paste (insert) a copied visualization to another place within the project, or into a completely different project.
Copy data to clipboard
Copy data
from the visualization onto the clipboard.
Copy selection to clipboard
Copy the selection
from the visualizaion onto the clipboard.
Download items as CSV (
dimension name
)
Download the dimension items
(to a maximum of 50,000) of the visualization to your local device. A maximum of 50,000 dimension items for the selected dimension.
Copy visualization
Copy the visualization, so that you can insert the visualization to another place within the project, or into a completely different project.
Download data CSV
Download the displayed data
of the visualization to your local device.
Export full table
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
## Configuration

Some visualizations (like Cohort table, Fallout, Flow, and others) have a configuration dialog to assist you in building the visualization. Use at the top of the visualization to access and change the configuration.

## Visualize

If you are not sure which visualization to pick, select **Visualize** in any freeform table row (available on hover). This selection is the fastest way to add a visualization. Analysis Workspace takes an educated guess at which visualization would best fit your data. For example, if you have one row selected, it creates a trended [line graph](/en/docs/analytics-platform/using/cja-workspace/visualizations/line). If you have three segment rows selected, it creates a [venn](/en/docs/analytics-platform/using/cja-workspace/visualizations/venn) diagram.

recommendation-more-help
