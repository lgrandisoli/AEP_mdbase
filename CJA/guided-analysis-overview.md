---
title: "Guided analysis overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/overview"
category: "overview"
topic: "analytics-platform/using/guided-analysis/overview"
created_at: "2026-06-02T19:04:57.354584+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Guided analysis overview

Last update: May 13, 2026
- Topics:
- [Guided Analysis](#)

CREATED FOR:

- User

Guided analysis enables users, from marketing to product to analysts, to self-serve high quality data and insights about the customer journey through guided workflows, built on the cross-channel data of Customer Journey Analytics. Similar to Analysis Workspace and Mobile scorecards, Guided analysis uses data from a [Data view](/en/docs/analytics-platform/using/cja-dataviews/data-views), which references data in Adobe Experience Platform through a [Connection](/en/docs/analytics-platform/using/cja-connections/overview). Many reports created in Guided analysis can seamlessly transfer to Analysis Workspace for additional research.

The following guided analyses are available:

Icon
Analysis
Description
Active growth
Identify who is new, retained, returning, or dormant.
Conversion trends
Track changes in conversion rates over time.
Engagement
Understand the breadth and depth of feature engagement.
First use impact
Measure the impact of first-time feature use on key indicators.
Frequency
Measure engagement by frequency of use.
Funnel
Compare conversion rates between steps.
Net growth
Are you gaining or losing users?
Release impact
Compare performance across equal periods pre- and post-release.
Retention
Measure your users’ ongoing return habits.
Timeline
Explore patterns in session activity.
Trends
Measure user engagement over time.
## Access

You can access Guided analysis from the Customer Journey Analytics homepage.

- Select Guided analysis from the homepage, which takes you directly to the Trends analysis .
- Select Create new to see the different view options and choose a different starting point for your analysis.

You can also access Guided analysis from within an Analysis Workspace project.

- Select Blank project from the homepage to create an empty Workspace project.
- Select Guided Analysis in the left rail.
- Drag any new analysis onto the Workspace canvas, then select Create to generate the desired analysis (for example: Create Trends ). You can also drag an existing analysis onto the Workspace canvas from under the Saved section.

## Interface

The interface for Guided analysis follows a question and answer format. Form your question in the query rail, then get an answer with a written insight, chart, and table. You can then ask the next question with analyses and visualization settings.

Guided analysis uses the following UI elements:

Interface preview
UI Element
Description
Query rail
Configure your *question* by selecting the desired components (events, properties, and segments) that make up an analysis. The following options are available across all analysis, with additional settings available on a per view basis.

- **View**: Select from the options to switch to a new analysis. Your query selections are maintained within the allowed limits for the new analysis.
- **Events**: The events that you want to measure. Each analysis enforces different limits to the number of events that you can configure. Events are sometimes labeled as **Start and return events**, **Steps**, or **Key indicators**. Events are identified in the analysis using 1, 2, …Select **Add an event** to add new events.
- **Factors**: If available, allows you to specify factors such as date since and first time event.
- **Counted as**: The counting method that you want to apply to the selected events. Select from the drop-down menu.
- **Segments**: The segments that you want to measure. Each analysis enforces different limits to the number of segments that you can configure. Segments are identified in the analysis using A, B, …Select **Add a segment** to add new segments.
- **Breakdown**: If available, the breakdown you want to apply to the analysis.

On some of the settings, additional configuration is available.

- Filters : Use to narrow down events or segments by specific dimensions. When a dimension is selected, both standard filter criteria (such as Equals , Contains , or Ends with ) and the top 1000 dimension values are available. Select to add additional filters. Select to remove a filter.
- More actions : Use to select actions, like Rename : to rename an event or segment. Duplicate : to duplicate an event or segment. Remove : to remove an event, segment or breakdown. Edit segment : to edit a segment in the Segment builder . Add to favorites : to add the segment to the list of favorite segments in the Segment manager . Save as : to save the segment as a new component. In the Save segments to components dialog, you can specify a segment name and a description. You can select to mark the new segment as a favorite. Select Save to save the segment as a new segment. Link start and return events .: to link start and return events in a Retention analysis. Unlink start and return events : to unlink start and return events in a Retention analysis.

Chart
A visualization of the data returned based on your input from the query rail and settings. Which visualization you see depends on the view and settings above the chart. The chart also includes:

- **Tooltips**: Hover over any chart data point to expose a tooltip with more information.
- **Legend**: Hover over the chart legend series to view definitions where available, focus on that series, and temporarily hide other series. Select a series in the legend to hide the series.
- **Annotations**: Applicable [annotations](/en/docs/analytics-platform/using/cja-components/annotations/overview) are visible between the visualization and the legend. It is shown as a icon in the annotation’s configured color. Analyses that show data over time place the icon under the configured date or date range. Analyses that do not show data over time show the icon in the lower right corner of the chart.
- **Select actions**: Expose the next available actions by selecting any data point. Options include **Save segment**.

Table
A table representation of the data returned based on your input from the query rail and settings. Rows in the table using event (1, 2, …) and segment identifiers (A, B, …) for reference. Columns in the table depend on the analysis above the chart. The table also includes for each row:

- **Select actions**: Toggle to hide or expose a chart series for a row. Select for additional actions. Options include **Save segment**.

Visualization settings
Options above the chart that allow you to ask the next question and customize how the chart and table return data. The following options are available across all analysis, with additional settings available on a per analysis basis.

- **Chart settings**: Fine-tune what your chart and table display. Available options depend on the analysis selected.
- **Overlay settings**: Add an overlay. Available options depend on the analysis selected.
- **Bucket settings**: Auto bucket or apply custom bucket settings to the data. Available options depend on the analysis selected.
- **Compare settings**: Compare data to a specific date range. Available options depend on the analysis selected.
- **Display settings**: Select how to show the data. Available options depend on the analysis selected.
- **Date range**: A calendar picker that allows you to determine the date range of the analysis. You can also select an interval for trended analyses, such as daily, weekly, or monthly.
- **Insights**: Contextual insights depending on the analysis that you view. These insights provide observations for the current analysis. If multiple insights are available, you can view them using the arrows on the right. You can toggle the visibility of this box by using the light bulb icon in the top right.

Menu
Available in a Guided analysis project
Commands in the top-right of a Guided analysis project that provide overarching actions for your analysis.

- *Name of data view*: Change the data view that the analysis uses. When you change the data view, available components in the query rail also change.
- **Copy link**: Copies a link to the analysis to your clipboard. You are prompted to save before sharing.
- **Share**: Opens the sharing modal, with further options for sharing to individual users or groups. You can share an analysis with other users, or generate a link to share with anyone.
- **Save**: Saves the analysis. If you’re saving a new analysis, the **Save analysis** dialog appears that requests a name and description. Once saved, an **Analysis saved** dialog allows you to share your analysis.
- **Add to Workspace**: Shows available Workspace projects that you can add this analysis to. Selecting a Workspace project opens that Workspace project in a new tab, adding the analysis at the bottom of the project.

Select for more actions, like:

- **Save as**: Saves the analysis separately from the current analysis, creating a copy. A dialog appears that requests a new name and description.
- **Export to Workspace**: Recreates the current Guided analysis query in Analysis Workspace. The Workspace project is created in a new tab, preventing interruption while working within Guided analysis. It is a copy of the analysis, and does not remain in sync with the original analysis once opened. Use this command when you want to handoff to your analyst team, or dive deeper into the data than what the analysis allows for.
- **Copy chart to clipboard**: Copies the chart graphic to your clipboard, to be pasted in other applications. The query rail and table are not included in the graphic.
- **Download PNG**: Downloads the chart graphic as a .png. The query rail and table are not included in the graphic.
- **Download CSV**: Downloads the table data as a .csv. The query rail and chart are not included in the file.

Menu
Available in a Guided analysis visualization in Analysis workspace.
Commands in a Guided analysis visualization in Analysis workspace.

- **Chart**: to show only the chart of the analysis.
- **Table**: to show only the table of the analysis.
- **All**: to show chart and table of the analysis.
- **Edit**: to edit the configuration of the analysis
- *Date range*: to configure the date range for the analysis.

## Provisioning

Guided analyses are included in Customer Journey Analytics packages in the following way:

Package
Available analyses
Customer Journey Analytics add-ons
Active growth, Conversion trends, Frequency, Funnel, Net growth, Retention, Trends
Customer Journey Analytics Foundation
Trends
Customer Journey Analytics Select
Foundation views + Active growth, Conversion trends, Frequency, Funnel, Net growth, Retention
Customer Journey Analytics Prime
Select views + Engagement, First use impact, Release impact, Timeline
Customer Journey Analytics Ultimate
Prime views
Product profile administrators can add or remove access to Guided analysis in the Adobe Admin Console.

- Log in to the [Adobe Admin Console](https://adminconsole.adobe.com).
- Select **Customer Journey Analytics** in the list of products.
- Select the desired product profile for the permissions that you want to edit.
- Select the **Permissions** tab, then click **Edit** under Reporting Tools.
- Select next to **Guided Analysis Access** in the list of Available Permission Items, which adds it to the list of Included Permission Items.
- Select **Save**.

See [User level access](/en/docs/analytics-platform/using/technotes/access-control#user-level-access) for more information.

TIP
Some admins prefer to enable Guided analysis and disable Analysis Workspace for new users to Customer Journey Analytics. Once those users mature with the product and your organizational data, you can then enable access to Analysis Workspace.
recommendation-more-help
