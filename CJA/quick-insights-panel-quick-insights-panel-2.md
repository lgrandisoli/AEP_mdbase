---
title: "Quick insights panel quick-insights-panel"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/panels/quickinsight"
category: "other"
topic: "analytics-platform/using/cja-workspace/panels"
created_at: "2026-06-23T20:43:10.636286+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Quick insights panel quick-insights-panel

Last update: May 13, 2026
- Topics:
- [Panels](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
*This article documents the Quick insights panel in* *Customer Journey Analytics*.*See Quick insights panel for the* *Adobe Analytics version of this article.*

style
shade-box
Quick Insights provides guidance for non-analysts and new users of Analysis Workspace to learn how to answer business questions quickly and easily. It is also a great tool for advanced users who want to answer a simple question quickly without having to build a table themselves.

When you first start using this Analysis Workspace, you might wonder:

- what visualizations would be most useful,
- which dimensions and metrics might facilitate insights,
- where to drag and drop items,
- where to create a segment,
- and more.

To help with these questions, Quick insights leverages an algorithm that presents you with the most popular dimensions, metrics, segments, and date ranges your company uses. This algorithm is based on your own company’s usage of data components in Analysis Workspace. In fact, you see dimensions, metrics, and segment tagged with POPULAR in the drop-down menu, as shown here:

Quick Insights helps you

- Properly build a data table and an accompanying visualization in Analysis Workspace.
- Learn the terminology and vocabulary for basic components and pieces of Analysis Workspace.
- Do simple breakdowns of dimensions, add multiple metrics, or compare segments easily within a Freeform table.
- Change or try out various visualization types to find the find tool for your analysis quickly and intuitively.

## Basic key terminology

The following are some of the basic terms that you need to be familiar with. Each data table consists of 2 or more building blocks (components) that you use to tell your data story.

Building block (Component)
Definition
Dimension
Dimensions are descriptions or characteristics of metric data that can be viewed, broken down, and compared in a project. They are non-numeric values and dates that break down into dimension items. For example,
browser
or
page
is a dimension.
Dimension item
Dimension items are individual values for a dimension. For example, dimension items for the browser dimension would be
Chrome
,
Firefox
,
Edge
, or others.
Metric
Metrics are quantitative information about person activity, such as views, click-throughs, reloads, average time spent, units, orders, revenue, and so on.
Visualization
Workspace offers
a number of visualizations
to build visual representations of your data. Such as bar charts, donut charts, histograms, line charts, maps, scatterplots, and others.
Dimension Breakdown
A dimension breakdown is a way to break down a dimension by other dimensions. For example, you could break down the US States by Mobile Devices to get the mobile device visits per state. Or you could break Mobile Devices down by Mobile Device types, by Regions, by Internal Campaigns, and more.
Segment
Segments let you identify subsets of persons based on characteristics or website interactions. For example, you can build People segments based on

- attributes: browser type, device, number of visits, country, gender, or
- interactions: campaigns, keyword search, search engine, or
- exits and entries: persons from Facebook, a defined landing page, referring domain, or
- custom variables: form field, defined categories, customer ID.

## Use

To use a **Quick insights** panel:

- Create a Quick insights panel. For information about how to create a panel, see Create a panel .
- When you first use a Quick insights panel, you might want to go through the short Intro tutorial that teaches you some of the basics. Select next to the Quick insights panel title and select Intro tutorial from the popup.
- Specify the input for the panel.
- Observe the output for the panel.

### Panel input

Select your building blocks:

- **Analyze** - specify a dimension (orange)
- **by** - specify a metric (green)
- **segment by** - specify a segment (blue)
- **on** - specify a date range (purple).

You have to select at least one dimension and one metric for the visualization to function properly.

You can specify the building blocks in three ways:

- Drag and drop components from the left panel.
- Start typing in one of the building block fields. When input is found, the building block field auto populates with possible values.
- Specify a building block drop-down menu (for example Country in **Analyze**) and **search** the list of possible value (using ) for the value you want to use (for example, **Country code**).

Select **Clear** to clear all input fields.

### Panel output

- When you have added at least one dimension and one metric, you can see the results. A Freeform table with the dimension (Country code) and metric (Sessions), segmented by Web sessions for the Last 12 months. An accompanying visualization, in this case a bar chart . The visualization that is generated is based on the type of data you added to the table. Any time-based data (such as Sessions per Day/Month) defaults to a Line chart. Any non-time-based data (such as Sessions per Device) defaults to a Bar chart. You can change the type of visualization by clicking on the drop-down arrow next to the visualization type.
- Try adding some more refinements as described below under More tips
- You might want to save your project, using Project > Save .

## More tips

Other useful hints pop up in the Quick Insights Builder, some of them depending on your last action.

- First, you might want to complete the More tips tutorial. This tutorial shows up 24 hours after you have created a project with at least one dimension and one metric. Select next to the Quick insights panel title and select More tips from the popup.
- You can analyze multiple dimensions and metrics, combine or compare segments, and specify a date range: Analyze dimension Broken-Down by : You can use up to 3 levels of breakdowns on dimensions to drill down to the data you really need. See ➊, ➋, and ➌. Add more metrics by : You can add up to 2 more metrics. See ➍ and ➎. segment by : You can add up to 2 more segments. For example, add Bookings as a segment and combine that segment with Frequent Bookers and First Time Fliers segments you compare. See ➏, ➐, and ➑. on: You can specify the date range. See ➒.

## Known limitations

If you try to edit directly within the table, the Quick Insights panel can become out of sync. Select **Resync Builder** at the top right of the panel to restore it to the previous Quick Insights settings.

You get a warning before adding anything directly to the table:

Otherwise, building directly causes the table to behave as a traditional Freeform table, without the helpful features for new users.

Related Articles
Create a panel
recommendation-more-help
