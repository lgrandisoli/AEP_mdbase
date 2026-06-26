---
title: "Ingest and use ad hoc data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/adhoc"
category: "guides"
topic: "analytics-platform/using/cja-data-ingestion/ingest-use-guides"
created_at: "2026-06-02T19:05:24.408865+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest and use ad hoc data

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

This quick start guide explains how you can ingest ad hoc data into Experience Platform and then use that data in Customer Journey Analytics.

To accomplish this, you need to:

- Create a dataset with a CSV file in Experience Platform. This workflow defines the model (schema) of the data that you want to collect and where to collect the data (dataset).
- Set up a connection in Customer Journey Analytics. This connection should (at least) include your Experience Platform ad hoc dataset.
- Set up a data view in Customer Journey Analytics to define metrics and dimension from the fields in your ad hoc data that you want to use in Analysis Workspace.
- Set up a project in Customer Journey Analytics to build your reports and visualizations.

NOTE
This quick start guide is a simplified guide on how to ingest ad hoc data using into Experience Platform and use that ad hoc data in Customer Journey Analytics. It is highly recommended to study the additional information when referred to.
## Create a dataset with a CSV file

For this quick start, you want to use a CSV file that represents lookup data and contains information similar to the one shown below.

_id
tracking_code
ad_group
campaign_name
1
abc123
abc-adgroup
123 Campaign
2
def123
def-adgroup
123 Campaign
3
ghi123
ghi-adgroup
123 Campaign
4
abc456
abc-adgroup
456 Campaign
5
def456
def-adgroup
456 Campaign
NOTE
Use ad hoc datasets and schemas for record based (lookup, profile) data. Ad hoc datasets and schemas are less suited and should not be considered for time-series (event, summary) data.
You do not need to create an XDM schema for ad hoc data. Experience Platform supports a workflow that, based on the data in the CSV file:

- Creates an ad hoc schema automatically. That schema conforms to the columns of the CSV file.
- Creates a dataset that contains the data from the CSV file.

To start the workflow:

- In the Experience Platform interface, in the left rail, select Workflows .
- Select Create dataset from CSV file .
- Select Launch from the right pane.
- In the Workflows > Create dataset from CSV file wizard: In the Configure dataset step: Enter a Name for the dataset. For example: Sample Data From CSV . Add an optional Description . For example: Sample data from a CSV file . Add one or more optional Tags , or select one or more existing Tags . Select Next . In the Add data step: Select Choose Files to select your CSV file from your computer or network. Alternatively, drag and drop the file from its location on your computer or network onto Drag and drop files . The file is uploaded and Sample data is displayed. Enable or disable Error diagnostics and Enable partial ingestion in line with your preferences. When you Enable Partial ingestion , you can define an Error threshold % . Select Finish .

After the data is successfully prepared and uploaded, you are redirected to **Datasets** in the Experience Platform interface.You see the **Dataset activity** for your **Sample Data from CSV** dataset with the status **Processing**.

To inspect the ad hoc data:

- In the Experience Platform interface, in the left rail, select Datasets .
- Select the Browse tab in Datasets . You should see your dataset listed.
- Select the name of the schema from the Schema column. For example: Sample Data From CSV…
- In the popup, select the Schema name . For example: Sample Data From CSV - adhoc schema - XXXXXXXXXXX . You are redirected to the Schemas > Sample Data From CSV - adhoc schema - XXXXXXXXXXX interface.

In the **Schemas** > **Sample Data From CSV - adhoc schema - XXXXXXXXXXX** interface:

- Select the topmost tenant name object underneath Schemas > Sample Data From CSV - adhoc schema - XXXXXXXXXXX to reveal the fields within the object. The fields within the object represent the structure of the CSV file. The schema is created automatically based on the upload of the ad hoc data. note NOTE The workflow defines all fields in the schema to be of type String. You can not change this type at a later stage. If you need more flexibility in the definition of an ad hoc schema, consider using the API to create an ad hoc schema and then use the Create dataset from schema workflow.

## Set up a connection

To use the Experience Platform dataset in Customer Journey Analytics, you create a connection that includes the ad hoc dataset resulting from the [workflow](#create-a-dataset-with-a-csv-file)

A connection lets you integrate datasets from Experience Platform into Workspace. To report on these datasets, you first have to establish a connection between datasets in Experience Platform and Workspace.

To create your connection:

- In the Customer Journey Analytics UI, select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In the Untitled connection screen: Name and describe your connection in Connection Settings . Select the correct sandbox from the Sandbox list in Data settings and select the number of daily events from the Average number of daily events list. Select Add datasets .
- In the Select datasets step in Add datasets : Select the dataset that you created earlier, for example Sample Data From CSV , and any other dataset you want to include in your connection. The ad hoc datasets do have the Adhoc Dataset type. Select Next .
- In the Datasets settings step in Add datasets : For your ad hoc dataset: Select the type of ad hoc dataset. For example: Lookup . Select a Key from the available keys defined in the ad hoc schema. Select a Matching key from an event dataset that you have added as part of your connection. Select the correct data source from the Data source type list. If you specify Other , then add a description for your data source. Set Import all new data and Dataset backfill existing data according to your preferences. Select Add datasets . Select Save .

See [Ad hoc dataset settings](/en/docs/analytics-platform/using/cja-connections/create-connection#adhoc-dataset) for more details on the settings available for ad hoc datasets.

IMPORTANT
On top of the general recommendation not to use ad hoc datasets and schemas for time-series data, you cannot use the
Create dataset from CSV
workflow for time-series data. This workflow defines all fields to be of type String which you cannot modify afterwards. When you add a time-series based dataset (event or summary) to a connection, this type of dataset requires the definition of at least one field of type DateTime.
If you do require to use ad hoc time-series data, consider
using the API to create an ad hoc schema
and then use the
Create dataset from schema
workflow.
After you create a [connection](/en/docs/analytics-platform/using/cja-connections/overview), you can perform various management tasks, such as [selecting and combining datasets](/en/docs/analytics-platform/using/cja-connections/combined-dataset), [checking the status of a connection’s datasets and the status of data ingestion](/en/docs/analytics-platform/using/cja-connections/manage-connections), and more.

## Set up a data view

A data view is a container specific to Customer Journey Analytics that lets you determine how to interpret data from a connection. It specifies all dimensions and metrics available in Analysis Workspace and which columns those dimensions and metrics obtain their data from. Data views are defined in preparation for reporting in Analysis Workspace.

To create your data view:

- In the Customer Journey Analytics UI, select Data views , optionally from Data management , in the top menu.
- Select Create new data view .
- In the Configure step: Select your connection from the Connection list. Name and (optionally) describe your connection. Select Save and continue .
- In the Components step: Add any schema field and/or standard component that you want to include to the METRICS or DIMENSIONS component boxes. Ensure you add relevant fields from the dataset that contains the ad hoc data. To access those fields: Select Event datasets . Select Adhoc & Relational fields . Drag and drop fields from the ad hoc schemas onto METRICS or DIMENSIONS . Optionally, use derived fields to modify any of the ad hoc fields from their default String type and format to another type or format. Select Save and continue .
- In the Settings step: Leave the settings as they are and select Save and finish .

See [Data views overview](/en/docs/analytics-platform/using/cja-dataviews/data-views) for more information on how to create and edit a data view. And what components are available for you to use in your data view and how to use segment and sessions settings.

## Set up a project

Analysis Workspace is a flexible browser tool that allows you to build analyses quickly and share insights based on your data. You use Workspace projects to combine data components, tables, and visualizations to craft your analysis and share with anyone in your organization.

To create your project:

- In the Customer Journey Analytics UI, select Projects in the top menu.
- Select Projects in the left navigation.
- Select Create project .
- Select Blank project .
- Select your data view from the list.
- To create your first report, start dragging and dropping dimensions and metrics on the Freeform table in the Panel. Including those metrics or dimension that are based on your ad hoc data.

See [Analysis Workspace overview](/en/docs/analytics-platform/using/cja-workspace/home) for more information on how to create projects and build your analysis using components, visualizations, and panels.

SUCCESS
You have completed all the steps. You started by defining what ad hoc data that you wanted to collect (CSV file). You used the workflow to create an ad hoc dataset and schema from that CSV file. You defined a connection in Customer Journey Analytics to use the ingested ad hoc data and other data. Your data view definition allowed you to specify which dimension and metrics to use and finally you created your first project visualizing and analyzing your data.
recommendation-more-help
