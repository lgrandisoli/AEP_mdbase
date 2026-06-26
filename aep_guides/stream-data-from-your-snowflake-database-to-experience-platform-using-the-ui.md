---
title: "Stream data from your Snowflake database to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/snowflake-streaming"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:16.010933+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Stream data from your Snowflake database to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to stream data from your Snowflake database to Experience Platform using the sources workspace in the UI.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

### Authentication

Read the guide on [prerequisite setup for Snowflake streaming data](/en/docs/experience-platform/sources/connectors/databases/snowflake-streaming) for information on the steps that you need to complete before you can ingest streaming data from Snowflake to Experience Platform.

## Use the Snowflake Streaming source to stream Snowflake data to Experience Platform

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Databases* category, select **Snowflake Streaming**, and then select **Set up**.

TIP
Sources that do not have an authenticated account in the sources catalog display the
Set up
option. Once an authenticated account exists, this option changes to
Add data
.
The **Connect Snowflake Streaming account** page appears. On this page, you can either use new or existing credentials.

### Create a new account

To create a new account, select **New account** and provide a name and an optional description for your account.

Basic authentication
To use Basic authentication, select **Basic Authentication for Snowflake** and provide credentials for your Snowflake account. When finished, select **Connect to source** and allow for a few moments for the connection to establish.

Read the Snowflake Streaming overview for more information on [gathering required credentials](/en/docs/experience-platform/sources/connectors/databases/snowflake-streaming#gather-required-credentials).

KeyPair authentication
To use KeyPair authentication, select **KeyPair Authentication for Snowflake** and provide credentials for your Snowflake account. When finished, select **Connect to source** and allow for a few moments for the connection to establish.

Read the Snowflake Streaming overview for more information on [gathering required credentials](/en/docs/experience-platform/sources/connectors/databases/snowflake-streaming#gather-required-credentials).

To use an existing account, choose **Existing account**, select your account from the list, and select **Next**.

## Select data select-data

IMPORTANT
- A timestamp column must exist in your source table in order for a streaming dataflow to be created. The timestamp is required for Experience Platform to know when data will be ingested and when incremental data will be streamed. You can retroactively add a timestamp column for an existing connection and create a new dataflow.
- Ensure that the case of the data fields in your sample source data file is in accordance with Snowflake’s guidance on case resolution for identifiers. Read the Snowflake document on identifier casing for more information.

The Select data step appears. In this step, you must select the data you want to import into Experience Platform, configure timestamps and timezones, and provide a sample source data file for the ingestion of raw data.

Use the database directory on the left of your screen and select the table that you want to import to Experience Platform.

Next, select the timestamp column type of your table. You can select between two types of timestamp columns: TIMESTAMP_NTZ or TIMESTAMP_LTZ. If you select a column type of TIMESTAMP_NTZ, then you must also provide a timezone. Your columns should have a not null constraint. For more information, read the section on [limitations and frequently asked questions](/en/docs/experience-platform/sources/connectors/databases/snowflake-streaming#limitations-and-frequently-asked-questions).

You can also configure backfill settings during this step. Backfill determines what data is initially ingested. If backfill is enabled, all current files in the specified path will be ingested during the first scheduled ingestion. If not, then only the files that are loaded in between the first run of ingestion and the start time will be ingested. Files loaded prior to the start time will not be ingested.

Select the **Backfill** toggle to enable backfill.

Finally, select **Choose file** to upload a sample source data to help create the mapping set, which will be used in a later step to map your original data to Experience Data Model (XDM).

When finished, select **Next** to proceed.

## Provide dataset and dataflow details provide-dataset-and-dataflow-details

Next, you must provide information on your dataset and your dataflow.

### Dataset details dataset-details

A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows). Data that is successfully ingested into Experience Platform is persisted within the data lake as datasets. During this step, you can create a new dataset or use an existing dataset.

If you have an existing dataset, select **Existing dataset** and then use the **Advanced search** option to view a window of all datasets in your organization, including their respective details, such as whether they are enabled for ingestion into Real-Time Customer Profile.

To use a new dataset, select **New dataset**, then provide a name, and an optional description for your dataset. You must also select an Experience Data Model (XDM) schema that your dataset adheres to.

New dataset details
Description
Output dataset name
The name of your new dataset.
Description
(Optional) A brief overview of the new dataset.
Schema
A dropdown list of schemas that exist in your organization. You can also create your own schema prior to the source configuration process. For more information, read the guide on
creating an XDM schema in the UI
.
### Dataflow details dataflow-details

Once your dataset is configured, you must then provide details on your dataflow, including a name, an optional description, and alert configurations.

Dataflow configurations
Description
Dataflow name
The name of the dataflow. By default, this will use the name of the file that is being imported.
Description
(Optional) A brief description of your dataflow.
Alerts
Experience Platform can produce event-based alerts that users can subscribe to. These options require a running dataflow to trigger them. For more information, read the [alerts overview](/en/docs/experience-platform/sources/ui-tutorials/alerts)

- **Sources Dataflow Run Start**: Select this alert to receive a notification when your dataflow run begins.
- **Sources Dataflow Run Success**: Select this alert to receive a notification if your dataflow ends without any errors.
- **Sources Dataflow Run Failure**: Select this alert to receive a notification if your dataflow run ends with any errors.

When finished, select **Next** to proceed.

## Map fields to an XDM schema mapping

The Mapping step appears. Use the mapping interface to map your source data to the appropriate schema fields before ingesting that data into Experience Platform, then select **Next**. For an extensive guide on how to use the mapping interface, read the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping) for more information.

## Review your dataflow review

The final step in the dataflow creation process is to review your dataflow before executing it. Use the **Review** step to review the details of your new dataflow before it runs. Details are grouped in the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the number of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Next steps

By following this tutorial, you have successfully created a streaming dataflow for Snowflake data. For additional resources, read the documentation below.

### Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to view information on ingestion rates, success, and errors. For more information on how to monitor streaming dataflows, visit the tutorial on [monitoring streaming dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/monitor-streaming).

### Update your dataflow

To update configurations for your dataflows scheduling, mapping, and general information, visit the tutorial on [updating sources dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/update-dataflows).

### Delete your dataflow

You can delete dataflows that are no longer necessary or were incorrectly created using the **Delete** function available in the **Dataflows** workspace. For more information on how to delete dataflows, visit the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/delete).

recommendation-more-help
