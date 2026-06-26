---
title: "Ingest and use data from Adobe Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/analytics"
category: "guides"
topic: "analytics-platform/using/cja-data-ingestion/ingest-use-guides"
created_at: "2026-06-23T20:41:59.636517+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest and use data from Adobe Analytics

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

This quick start guide explains how you can use the data collected by Adobe Analytics in Customer Journey Analytics.

PREREQUISITES
You do have Adobe Analytics licensed and deployed on one or more of your websites, using any of the documented implementation methods:
- Implement Analytics using Experience Platform Edge
- Implement Analytics using Adobe Analytics extension
- Implement Analytics using JavaScript

To accomplish this, you need to:

- Set up an Adobe Analytics source connector in Adobe Experience Platform. The source connector takes care of ingesting your current Adobe Analytics data into a dataset in Adobe Experience Platform.
- Set up a connection in Customer Journey Analytics. The connection should (at least) include your Adobe Experience Platform dataset.
- Set up a data view in Customer Journey Analytics to define metrics and dimension that you want to use in Analysis Workspace.
- Set up a project in Customer Journey Analytics to build your reports and visualizations.

NOTE
This quick start guide is a simplified guide on how to ingest data, using the Adobe Analytics source connector, and use that data in Customer Journey Analytics. It is highly recommended to study the additional information when referred to.
## Set up an Adobe Analytics source connector

The Adobe Analytics source connector allows you to bring Adobe Analytics report suite data into Adobe Experience Platform.

To create an Adobe Analytics source connector:

- In the Platform UI, select Sources , from the left rail.
- Select Adobe applications from the list of CATEGORIES.
- Select Set up or Add data in the Adobe Analytics tile.
- Select Report suite . From the list of report suites, select the one you want to use. Alternatively, you can use Search to search for a report suite. Select Next .
- Select Default schema as the Target schema. Adobe Experience Platform automatically creates the schema and the corresponding dataset to map all standard fields from the selected Adobe Analytics report suite. Select Next .
- Name the data flow and (optionally) provide a description. Select Next .
- Review the connection and select Finish .

Once the connection is created, the dataflow is automatically created to populate a dataset with the Adobe Analytics data from your report suite. The dataflow ingests up to 13 months of historical data for production sandboxes. The backfill in non-production sandboxes is limited to three months.

When the initial ingestion completes, your Adobe Analytics report suite data is ready to be used by Customer Journey Analytics.

See [Create an Adobe Analytics source connection in the UI](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics) for a much more comprehensive tutorial.

## Set up a connection

To use the Adobe Experience Platform data in Customer Journey Analytics, you create a connection that includes the data resulting from setting up your schema, dataset, and workflow.

A connection lets you integrate datasets from Adobe Experience Platform into Workspace. To report on these datasets, you first have to establish a connection between datasets in Adobe Experience Platform and Workspace.

To create your connection:

- In the Customer Journey Analytics UI, select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In the Untitled connection screen: Name and describe your connection in Connection Settings. Select the correct sandbox from the Sandbox list in Data settings and select the number of daily events from the Average number of daily events list. Select Add datasets . In the Select datasets step in Add datasets: Select the dataset automatically created by the Adobe Analytics source connector and any other dataset that you want to include in your connection. Select Next . In the Datasets settings step in Add datasets: For each dataset: Select a Person ID from the available identities defined in the dataset schemas in Adobe Experience Platform. Select the correct data source from the Data source type list. If you specify Other , then add a description for your data source. Set Import all new data and Dataset backfill existing data according to your preferences. Select Add datasets . Select Save .

See [Connections overview](/en/docs/analytics-platform/using/cja-connections/overview) for more information on how to create and manage a connection and how to select and combine datasets.

## Set up a data view

A data view is a container specific to Customer Journey Analytics that lets you determine how to interpret data from a connection. It specifies all dimensions and metrics available in Analysis Workspace and which columns those dimensions and metrics obtain their data from. Data views are defined in preparation for reporting in Analysis Workspace.

To create your data view:

- In the Customer Journey Analytics UI, select Data views , optionally from Data management , in the top menu.
- Select Create new data view .
- In the Configure step: Select your connection from the Connection list. Name and (optionally) describe your connection. Select Save and continue .
- In the Components step: Add any schema field and/or standard component that you want to include to the METRICS or DIMENSIONS component boxes. Select Save and continue .
- In the Settings step: Leave the settings as they are and select Save and finish .

See [Data views overview](/en/docs/analytics-platform/using/cja-dataviews/data-views) for more information on how to create and edit a data view, what components are available for you to use in your data view and how to use segment and sessions settings.

## Set up a project

Analysis Workspace is a flexible browser tool that allows you to quickly build analyses and share insights based on your data. You use Workspace projects to combine data components, tables, and visualizations to craft your analysis and share with anyone in your organization.

To create your project:

- In the Customer Journey Analytics UI, select Projects in the top menu.
- Select Projects in the left navigation.
- Select Create project . Select Blank project .
- Select your data view from the list. .
- To create your first report, start dragging and dropping dimensions and metrics on the Freeform table in the Panel . As an example, drag Program Points Balance and Page View as metrics and email as dimension to get a quick overview of profiles that have visited your website and are part of the loyalty program collecting loyalty points.

See [Analysis Workspace overview](/en/docs/analytics-platform/using/cja-workspace/home) for more information on how to create projects and build your analysis using components, visualizations, and panels.

SUCCESS
You have completed all the steps. Starting by setting up the Adobe Analytics data source connector and configuring that connector for your report suite, your Adobe Analytics data is automatically uploaded into Adobe Experience Platform. You defined a connection in Customer Journey Analytics to use the ingested Adobe Analytics data and other data. Your data view definition allowed you to specify which dimension and metrics to use and finally you created your first project visualizing and analyzing your data.
recommendation-more-help
