---
title: "User preferences"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/user-preferences"
category: "reference"
topic: "analytics-platform/using/cja-workspace/user-preferences"
created_at: "2026-06-02T19:05:48.501258+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# User preferences

Last update: May 12, 2026
- Topics:
- [Workspace Basics](#)

CREATED FOR:

- User

You can manage user settings or preferences for Analysis Workspace and related components for all new projects or panels that you create. Existing projects and panels are not affected.

## Edit preferences

You can update your preferences in the following ways:

- Select **Edit preferences** from the Workspace main interface.
- Select **Project** > **User preferences** from the menu when working in a Workspace project.
- Select **Components** > **Preferences** from the top menu bar in Customer Journey Analytics (only available for product administrators).

## Configure preferences

You can configure the following preferences:

### General preferences

General preferences apply to your Customer Journey Analytics experience in the browser. For information about how to access these preferences, see [Edit preferences](#edit-preferences).

Preference
Options
Landing page
Choose what page displays as the default page when you access Customer Journey Analytics:

- Project list (default)
- Blank project
- Blank Trends guided analysis
- Specific project, selected from a list

Tips
Displays tips in a blue box in the lower-right area of Analysis Workspace.

This option is enabled by default.

Components displayed in left panel groups
Choose how many of each component group to display in the Components menu in the left panel.

If you choose 0 for a component group, the component group is no longer accessible from the left panel.

By default, 5 components are displayed for each of the following component groups:

- Dimensions
- Metrics
- Segments
- Date ranges

For more information about Components in Analysis Workspace, see [Components overview](/en/docs/analytics-platform/using/cja-components/overview).

### IMS Organization preferences ims-organization-preferences

You can update company preferences that apply to all users and projects within your organization. For information about how to access these preferences, see [Edit preferences](#edit-preferences).

Section
Preference
Options
Templates Tab tab
Hide Templates Tab
Hides the Templates Tab for all users in your organization.
Project sharing
Allow sharing only with Workspace users
When this option is enabled, users in your organization cannot see the **Share with anyone** option in the **Share** menu. This means that users cannot share projects with people who don’t have an Analysis Workspace account in your organization as described in [Share a project with anyone (no login required)](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects#share-public-link) in [Share projects](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects).This option is disabled by default for all organizations (meaning that users can share projects with people outside the organization) except for customers who have licensed Healthcare Shield.

Consider the following when enabling or disabling this option:

- When you enable this option, people who previously received access to a project through the Share with anyone share option can no longer access the project.
- If this option is enabled (to allow sharing only with Workspace users) and then later disabled (to allow sharing with anyone), people who previously received access to a project through the Share with anyone share option do not automatically regain their access to the project. In this case, the user who shared the project must enable the **Link is active** option that is available when sharing a project with anyone **(Share** > **Share with anyone**), as described in [Share a project with anyone (no login required)](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects#share-public-link) in [Share projects](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects).
- **For customers who license Healthcare Shield:** This option is enabled by default and cannot be disabled. Before you can disable this option so that users can use the Share with anyone share option, you first need to add the Share project links with anyone permission (located under Reporting Tools) in the Adobe Admin Console. After the permission is added, you can disable this option, then accept the resulting legal notice. For information about how to add a permission in the Admin Console, see [Manage product permissions in the Admin Console](https://helpx.adobe.com/enterprise/using/manage-permissions-and-roles.html).

Require CX Enterprise authentication
When this option is enabled, people who are given access to a project from the **Share with anyone** option in Analysis Workspace must authenticate using their CX Enterprise credentials.

After this option is enabled, any time a user shares a project using the Share with anyone share option, the Require CX Enterprise authentication option is enabled in the share dialog and it cannot be disabled by the user who is sharing the project. For information about how users can share projects with anyone, see [Share a project with anyone (no login required)](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects#share-public-link) in [Share projects](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects).

Consider the following when enabling this option:

- When you enable this option, all projects that were previously shared with the Share with anyone share option, and do not have the Require CX Enterprise authentication option enabled, are deactivated. If this option is enabled (to require CX Enterprise authentication) and then later disabled (to allow anyone with the link to access the project), people who previously received access to a project through the Share with anyone share option do not automatically regain their access to the project. In this case, the user who shared the project must enable the Link is active option that is available when sharing a project with anyone (Share > Share with anyone > Link is active ), as described in Share a project with anyone (no login required) in Share projects .
- This option is available only if SSO is implemented in your organization. For information about how system administrators can enable SSO for your organization, see Set up identity and Single Sign-On . If SSO is configured for your organization, check to see if any kind of auto-account creation is implemented in the console. Typically, a system administrator would set this up, as described in Enable automatic account creation .
- If your organization licenses Healthcare Shield, this option is enabled by default and cannot be disabled.

Project commenting
Allow commenting on projects
When this option is enabled, a comments area is available in the right rail of each project in Analysis Workspace.

Project owners can disable the comments area for a given project, as described in [Create projects](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects).

For more information about commenting in Analysis Workspace projects, see [Add and manage comments in projects](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/comment-projects).

### Projects & Analyses preferences project-and-analysis-preferences

You can customize these preferences for all new Analysis Workspace projects, new Analysis Workspace panels, and new guided analyses. For information about how to access these preferences, see [Edit preferences](#edit-preferences).

Some of these same preferences can also be customized for individual projects in Analysis Workspace, as described in [Project overview](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/freeform-overview).

Section
Preference
Options
Display
View density
Choose how much content to display on the screen by reducing the vertical padding of the left panel, freeform tables, and cohort tables.

- Compact
- Comfortable
- Expanded (default)

Color palette
Choose the visualization color palettes that are used in Analysis Workspace and guided analysis.

- Categorical palette: Applied to many visualizations in Analysis Workspace and guided analysis. Each color represents a distinct categorical value. Choose from Adobe-provided options or enter a custom palette defined by comma-delimited hex values.
- Divergent palette: Applied to the Cohort table in Analysis Workspace and User growth guided analysis. This palette holds a numeric meaning with two extremes and a baseline in the middle.
- Sequential palette: Applied to the Frequency trends (stacked bar) guided analysis. This palette holds a numeric meaning from light to dark.

Data
Data view
Choose the data where tables and visualizations derive their data.

- Most recent (default)
- Specific data view selected from a list

Calendar
Select from a list of:

- Adobe-provided ranges (default is This Month)
- You can enable Make date range components relative to panel calendar by default.

Panel Type
- Freeform (default)
- Blank
- Quick Insights

Instance counting
Enable Count repeat instances to specifies whether repeat instances are counted in reports. For example, when enabled, multiple consecutive page views to the same page are treated as multiple page views. When disabled, multiple consecutive page views to the same page count as a single page view.

**Note:** This setting affects only certain metrics (such as Sessions) and it does not apply to Flow or Fallout visualizations.

Number format
- 1,000.00 (default)
- 1.000,00
- 1 000,00

CSV separator character
- Comma (default)
- Semicolon
- Colon
- Pipe
- Period
- Space
- Tab

Show annotations
Choose whether annotations are visible in your projects. For more information about annotations, see
Annotations overview
.
### Freeform table preferences freeform-table-preferences

You can customize freeform table preferences for all new projects that you create in Analysis Workspace. For information about how to access these preferences, see [Edit preferences](#edit-preferences).

Some of these same preferences can also be customized for individual tables.

Select the linked section titles for more information and context about the available preferences.

Section
Preference
Options
Table
Table type
- Freeform
- Table builder

Default table metric
- Events
- Sessions
- People

Default table dimension
Choose from Minute, Hour, Day, Week, Month, Quarter, or Year.
Align dates
Select this option to align dates from each column to all start on the same row.
Column
Wrap header text
Lets you wrap the header text in Freeform tables to make headers more readable and tables more shareable. This is useful for .pdf rendering and for metrics with long names. Enabled by default.
Show totals
This totals number is typically equal to or a subset of the Grand Total. It reflects any table segments applied within the freeform table, including the Include None option.
Show grand totals
This totals number represents all events that have been collected, sometimes referred to as
data view total
. When a segment is applied either at the panel level or within the freeform table, this total adjusts to reflect all events that match the segment criteria. Grand total is not supported for tables or breakdowns with
static rows
.
Show sparkline
Show or hide line charts at the bottom of the chart. When hidden, the legend changes to no longer visually reference the lines.
Number
Determines if a cell shows/hides the numeric value for the metric. For example, if the metric is Page Views, the numeric value is the number of page views for the row item.
Percent
Determines if a cell shows/hides the percent value for the metric. For example, if the metric is page views, the percent value is the number of page views for the row item divided by the total page views for the column. Note: You can show percentages greater than 100%, to be more accurate. You can also move the upper bound cap to 1,000% to ensure that columns can grow in widths too large.
Show anomalies
This setting was moved from the "Project" tab. this is already in the tool/docs under "Freeform table, But the doc doesn't give a definition.
Determines if anomaly detection is run on the values in this column.
Show forecast
Determines if forecast values are shown automatically for the first metric column in any time-series freeform table you create.
Interpret zero as no value
For cells with a 0 value, determines whether to show a 0 or a blank cell. This is useful when you look at data for each day of a month, and some days haven’t happened yet. Instead of showing 0’s for future dates, blank cells can be shown instead. Charts respect this setting as well (for example, carts do not show a line or bar with 0 values when this setting is checked).
Background
Determines if a cell shows/hides all cell formatting, including the bar graph and conditional formatting

- Bar graph
- Shows a horizontal bar graph representing the cell’s value relative to the total for the column. Conditional formatting For more information about conditional formatting, see “Conditional formatting” in [Column Settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/column-settings)

Cell preview
Shows a preview of how each cell appears with the currently selected formatting options applied.
Row
Breakdown by position
Select this option if you want the breakdown to remain with the position of the item rather than with the item itself. For more information about breakdowns, see
Break down dimensions
.
Percentage calculation
- Column
- Row

Column totals (Static rows only)
- Display sum of rows: Shows the sum of the individual line items
- Display grand total: Shows the de-duplicated sum of rows.

### Visualizations preferences visalization-preferences

You can update visualization preferences for all new prjects that you create in Analysis Workspace. For information about how to access these preferences, see [Edit preferences](#edit-preferences).

Some of these same preferences can also be customized for individual visualizations.

Select the linked section titles for more information and context about the available preferences.

Section
Preference
Options
General Defaults
Percentages
Displays values in percentages for all visualizations.
Legend visible
Lets you hide the detailed legend text for all visualizations.
Limit max items
Reduces the number of items on the X-axis for all visualizations. This preference can be useful if you have a large dataset.
Display dual axis (when applicable)
Only applies if you have two metrics - you can have a y-axis on the left (for one metric) and on the right (for the other metric). This preference is helpful when plotted metrics are of very different magnitudes.
Normalization (when applicable)
Forces metrics to equal proportions. This preference is helpful when plotted metrics are of very different magnitudes.
Anchor Y-axis at zero
If all the values plotted on the chart are considerably above zero, the chart default updates the bottom of the y-axis to NON-ZERO. If you check this box, the y-axis is forced to zero (and re-draws the chart).
Anchor anomalies to scale Y-axis
The y-axis is scaled using anomaly values.
Line
Percentages
Displays values in percentages for the Line visualizations.
Legend visible
Lets you hide the detailed legend text for the Line visualization.
Limit max items
Reduces the number of items on the X-axis in the Line visualization. This preference can be useful if you have a large dataset.
Display dual axis (when applicable)
Only applies if you have two metrics - you can have a y-axis on the left (for one metric) and on the right (for the other metric). This preference is helpful when plotted metrics are of very different magnitudes.
Normalization (when applicable)
Forces metrics to equal proportions. This preference is helpful when plotted metrics are of very different magnitudes.
Show x-axis
Displays the x-axis on the Line chart.
Show y-axis
Displays the y-axis on the Line chart.
Anchor Y-axis
If all the values plotted on the chart are considerably above zero, the chart default renders the bottom of the y-axis NON-ZERO. If you check this box, the y-axis will be forced to zero (and re-draws the chart).
Allow anomalies to scale Y-axis
If you have multiple metrics in a chart, you have to hover over each anomaly to see the confidence band for that metric. To make the visualization more legible, the Anomaly Detection confidence interval does not automatically scale the y-axis. This setting allows the confidence interval to scale the visualization.

For more information, see [View anomalies in Analysis Workspace](/en/docs/analytics-platform/using/cja-workspace/anomaly-detection/view-anomalies).

Allow forecast to scale Y-axis
If you have forecast values that are outside of upper and lower bounds of the historical values, the y-axis does not automatically scale these forecasted values. When turned on, this option does properly scale the y-axis for the forecasted values.
Show min
Overlay a minimum value label to highlight quickly the valleys in a metric. Note: The min values are derived from the visible data points in the visualization, not the full set of values within a dimension.
Show max
overlay a maximum value label to highlight quickly the peaks in a metric. Note: The max values are derived from the visible data points in the visualization, not the full set of values within a dimension.
Show trendline
Show a regression or moving average trendline to your line series. Trendlines help to depict a clearer pattern in the data.
Cohort
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Container
Select the preferred container for cohort analysis in case of an account-based [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank) connection.

The following options are available:

- Global Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Buying Groups [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Opportunities [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Person

Granularity
For trended visualizations, you can change the time granularity (Day, Week, Month, Quarter, or Year). This change also applies to the data source table.
Only show percent
Removes the number value and only shows the percentage.
Round percent to nearest whole
Rounds the percent value to the nearest whole instead of showing the decimal value.
Show average percent row
Inserts a new row at the top of the table and then adds the average for the values within each column.
Combo charts
Show X-axis
Displays the x-axis on the Combo chart.
Show Y-axis
Displays the y-axis on the Combo chart.
Display barbells on lines
Show barbells on lines in Combo charts.
Key Metric Summary
Summary display type
- Emphasize percent change
- Emphasize number value

Show sparklines
how or hide line charts at the bottom of the chart. When hidden, the legend changes to no longer visually reference the lines.
Show max and min on sparklines
Show minimum and maximum values on primary and comparison line charts.
Show comparison
Show comparison data. When hidden, both the comparison line chart and summary change objects are hidden from view.
Number value options
In the **Key Metric Summary** section

- Show percent change
- Show raw difference Raw difference between the total value of the metric in the primary date range and the secondary date range

Fallout
Container
Select the preferred container to analyze pathing. The preferred container helps you to understand account engagement at various B2B container levels [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), person engagement at the person level (across sessions), or constrain the analysis to a single session.

The following options are available:

- Global Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Buying Groups [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Opportunities [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Session
- Person

Flow
Container
Select the preferred container to analyze. The preferred container helps you to understand account engagement at various B2B container levels [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), person engagement at the person level (across sessions), or constrain the analysis to a single session.

The following options are available:

- Global Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Buying Groups [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Opportunities [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Session
- Person

Wrap labels
Normally, the labels on the Flow elements are truncated to save screen real estate, but you can make the entire label visible by checking this box. Default = unchecked.
Include repeat instances
Flow visualizations are based on instances of a dimension. This setting gives you the option to include or exclude repeated instances, for example, Page reloads. However, repeats cannot be removed from Flow visualizations that include multi-valued dimensions, such as listVars, listProps, s.product, merchandising eVars, etc. Default = unchecked.
Show tooltips
Determines whether tooltips, containing node data, are shown when hovering over individual nodes within a flow visualization.
Number of columns
Determines how many columns you want in your Flow diagram.
Items expanded per column
How many items you want in each column.
Journey canvas
Container
Select the preferred container to analyze pathing. The preferred container helps you to understand account engagement at various B2B container levels [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), person engagement at the person level (across sessions), or constrain the analysis to a single session.

The following options are available:

- Global Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Accounts [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Buying Groups [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Opportunities [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)
- Session
- Person

Stacked Charts
100% stacked
This setting on area stacked, bar stacked or horizontal bar stacked visualizations turns the chart into a “100% stacked” visualization.

For more information, see [Bar and bar stacked](/en/docs/analytics-platform/using/cja-workspace/visualizations/bar).

Histogram
Number of buckets
Choose the number of date ranges (buckets) in the visualization. The maximum number of buckets is 50.

For more information, see [Histogram](/en/docs/analytics-platform/using/cja-workspace/visualizations/histogram).

Counting method
Choose from the following options:

- Hit
- Session
- Person

For example, when used with page views, you could choose page views per person, page views for visit, or page views per event. For Hit, “Occurrences” is used as the y-axis metric in a freeform table.

Summary Change
Value
Seem to be basically the same options as in "Number value options"
- Percent change
- Raw difference

Percentages
Displays values in percentages for the Summary Change visualizations.
Legend visible
Lets you hide the detailed legend text for the Summary Change visualization.
Summary Number
Percentages
Displays values in percentages for the Summary Number visualizations.
Legend visible
Lets you hide the detailed legend text for the Summary Number visualization.
Summary value by
Choose from Max, Min, Mean, Median, and Sum.
Abbreviate value
In the
Summary Number
section
Treemap
Percentages
Displays values in percentages for the Treemap visualizations.
Limit max items
Reduces the number of items on the X-axis in the Treemap visualization. This preference can be useful if you have a large dataset.
Venn
Legend visible
Lets you hide the detailed legend text for the Venn visualization.
Scatter
Percentages
Displays values in percentages for the Scatter visualizations.
Legend visible
Lets you hide the detailed legend text for the Scatter visualization.
Limit max items
Reduces the number of items on the X-axis in the Scatter visualization. This preference can be useful if you have a large dataset.
Anchor y-axis at zero
If all the values plotted on the chart are considerably above zero, the chart default renders the bottom of the y-axis NON-ZERO. If you check this box, the y-axis is forced to zero (and re-draws the chart).
## Restore default preferences

You can restore all your user preferences to the system defaults. This preference does not affect administrator preferences under the Company tab.

This action cannot be undone.

- In Customer Journey Analytics, select Components > Preferences from the top menu. Or select Project > User settings from the Workspace menu.
- In the upper-right, select Restore defaults .
- Select Restore defaults in Restore system default settings .

## Dark theme

If you prefer to have a dark background for your Customer Journey Analytics user interface, you can toggle to Dark theme.

- Select the CX Enterprise user icon at the top right.
- Enable Dark theme .

recommendation-more-help
