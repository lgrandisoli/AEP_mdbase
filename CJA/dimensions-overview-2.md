---
title: "Dimensions overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/dimensions/overview"
category: "overview"
topic: "analytics-platform/using/cja-components/dimensions"
created_at: "2026-06-23T20:42:49.637685+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Dimensions overview

Last update: May 13, 2026
- Topics:
- [Dimensions](#)

CREATED FOR:

- User
- Admin

Dimensions are a component type in Customer Journey Analytics that are used to analyze data. For example, you use dimensions when building reports in [Analysis Workspace](/en/docs/analytics-platform/using/cja-workspace/home) or in [Report Builder](/en/docs/analytics-platform/using/cja-reportbuilder/rb-overview).

Customer Journey Analytics dimensions are of unlimited type; values can be numeric, text, objects, lists, or mixtures of all.

A basic report in Customer Journey Analytics shows rows of dimensions (commonly string values), against a column of metrics (commonly numeric values).

For example, if you combined the Page dimension with the People metric, you would get a ranked report showing your top-visited pages by people:

Page
People
Home page
800
Product page
500
Purchase page
100
Each dimension represents a different part or facet of your site. You can combine one of more of these dimensions with one or more metrics to create a desired report.

## Create dimensions

Customer Journey Analytics administrators can [create dimensions within a data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#components).

## Standard dimensions

When you create a data view, the following components are added by default as dimensions to your data view:

Component Name
Notes
15 Minute
Each 15 minutes that a given event happened (rounded down). The first dimension item is the first 15 minutes in the date range, and the last dimension item is the last 15 minutes in the date range.
30 Minute
Each 30 minutes that a given event happened (rounded down). The first dimension item is the first 30 minutes in the date range, and the last dimension item is the last 30 minutes in the date range.
5 Minute
Each 5 minutes that a given event happened (rounded down). The first dimension item is the first 15 minutes in the date range, and the last dimension item is the last 5 minutes in the date range.
Day
The day that a given event happened. The first dimension item is the first day in the date range, and the last dimension item is the last day in the date range.
Day of Week
The day of the week that a given event happened. The first dimension item is the first day of the week in the date range, and the last dimension item is the last day of the week in the date range.
Day of Month
The day of the month that a given event happened. The first dimension item is the first day of the month in the date range, and the last dimension item is the last day of the month in the date range.
Event Depth
Assigns sequential numerical values (1, 2, 3, etc.) to each event interaction within a session. With this dimension you can enable detailed tracking and analysis of where specific events occur in the sequential flow of user interactions within the
bounded experience session you have defined for your data view
. You can track the progression of events from start to finish within a bounded session. As an example: A visitor lands on your homepage (event 1, session start), uses the search function (event 2), views a product details page (event 3), adds to cart (event 4), proceeds to checkout (event 5), and completes a purchase (event 6, session end). You can use Event depth now in a segment definition to segment data based on interaction depth.
Hour
The hour that a given event happened (rounded down). The first dimension item is the first hour in the date range, and the last dimension item is the last hour in the date range.
Hour of Day
The hour of the day that a given event happened (rounded down). The first dimension item is the first hour of the day in the date range, and the last dimension item is the last hour of the day in the date range.
Minute
The minute that a given event happened (rounded down). The first dimension item is the first minute in the date range, and the last dimension item is the last minute in the date range.
Minute of Hour
The minute of the hour that a given event happened (rounded down). The first dimension item is the first minute of the hour in the date range, and the last dimension item is the last minute of the hour in the date range.
Month
The month that a given event happened. The first dimension item is the first month in the date range, and the last dimension item is the last month in the date range.
Month of Year
The month of the year that a given event happened. The first dimension item is the first month of the year in the date range, and the last dimension item is the last month of the year in the date range.
Quarter
The quarter that a given event happened. The first dimension item is the first quarter in the date range, and the last dimension item is the last quarter in the date range.
Quarter of Year
The quarter of the year that a given event happened. The first dimension item is the first quarterof the year in the date range, and the last dimension item is the last quarter of the year in the date range.
Second
The second that a given event happened (rounded down). The first dimension item is the first second in the date range, and the last dimension item is the last second in the date range.
Week
The week that a given event happened. The first dimension item is the first week in the date range, and the last dimension item is the last week in the date range.
Week of year
The week of year that a given event happened. The first dimension item is the first week of year in the date range, and the last dimension item is the last week of year in the date range.
Year
The year that a given event happened. The first dimension item is the first year in the date range, and the last dimension item is the most recent year in the date range.
## Add dimension descriptions

Customer Journey Analytics administrators can add descriptions for dimensions and other components either within the data view or directly within Analysis Workspace. For information about how to add descriptions to dimensions, see [Add component descriptions](/en/docs/analytics-platform/using/cja-components/add-component-descriptions).

Related Articles
Discover Deeper Customer Insights with the Event Depth Feature
recommendation-more-help
