---
title: "Stream Talon.One data to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/loyalty/talon-one-streaming"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:24.082500+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Stream Talon.One data to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

AVAILABILITY
The Talon.One source is in beta. Read the
terms and conditions
in the sources overview for more information on using beta-labeled sources.
Read this guide to learn how to connect and stream your data from Talon.One to Adobe Experience Platform using the sources workspace in the UI.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

IMPORTANT
Read the
Talon.One overview
to learn about prerequisite steps that you need to complete before connecting your account to Experience Platform.
## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Select the appropriate category in the *Categories* panel. Alternatively, use the search bar to navigate to the specific source that you want to use.

To stream data from Talon.One, select the **Talon.One Streaming Events** source card under *Loyalty* and then select **Add data**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Select data

Next, use the *Select data* interface to upload a sample JSON file to define your source schema. During this step, you can use the preview interface to view the file structure of the payload. When finished, select **Next**.

## Dataflow details

Next, you must provide information regarding your dataset and your dataflow.

### Dataset details

A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns/fields) and records (rows). Data that is successfully ingested into Experience Platform is persisted within the data lake as datasets.

During this step, you can either use an existing dataset or create a new dataset.

NOTE
Regardless of whether you use an existing dataset or create a new dataset, you must ensure that your dataset is
enabled for Profile
ingestion.
Select for steps to enable Profile ingestion, error diagnostics, and partial ingestion.
If your dataset is enabled for Real-Time Customer Profile, then during this step, you can toggle **Profile dataset** to enable your data for Profile ingestion. You can also use this step to enable **Error diagnostics** and **Partial ingestion**.

- **Error diagnostics**: Select **Error diagnostics** to instruct the source to produce error diagnostics that you can later reference when monitoring your dataset activity and dataflow status.
- **Partial ingestion**: Partial batch ingestion is the ability to ingest data containing errors, up to a certain configurable threshold. This feature allows you to successfully ingest all of your accurate data into Experience Platform, while all of your incorrect data is batched separately with information on why it is invalid.

### Dataflow details

Once your dataset is configured, you must then provide details on your dataflow, including a name, an optional description, and alert configurations.

Dataflow configurations
Description
Dataflow name
The name of the dataflow. By default, this will use the name of the file that is being imported.
Description
(Optional) A brief description of your dataflow.
Alerts
Experience Platform can produce event-based alerts which users can subscribe to, these options allow a running dataflow to trigger these. For more information, read the [alerts overview](/en/docs/experience-platform/sources/ui-tutorials/alerts)

- **Sources Dataflow Run Start**: Select this alert to receive a notification when your dataflow run begins.
- **Sources Dataflow Run Success**: Select this alert to receive a notification if your dataflow ends without any errors.
- **Sources Dataflow Run Failure**: Select this alert to receive a notification if your dataflow run ends with any errors.

## Mapping

Use the mapping interface to map your source data to the appropriate schema fields before ingesting data to Experience Platform. For more information, read the [mapping guide in the UI](/en/docs/experience-platform/data-prep/ui/mapping).

## Review

The *Review* step appears, allowing you to review the details of your dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the account name, source platform, and the source name.
- **Assign dataset and map fields**: Shows the target dataset and the schema that the dataset adheres to.

After confirming the details are correct, select **Finish**.

## Retrieve the streaming endpoint URL

With the connection created, the sources detail page appears. This page shows details of your newly created connection, including previously run dataflows, ID, and streaming endpoint URL.

## Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to see information on ingestion rates, success, and errors. For more information on how to monitor dataflow, see the tutorial on [monitoring accounts and dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/monitor-streaming).

## Known limitations

To ensure accurate data ingestion, you should send data from Talon.One’s loyalty points changed, tier upgrade, and tier downgrade notifications to the connector. Because the loyalty points changed notification does not include tier information, you must send these notifications to a separate profile dataset. If you combine points changed data with tier upgrade or downgrade notifications in the same dataset, tier information will be lost or overwritten with null values. Tier upgrade and downgrade notifications can use the same dataset, as both include tier details. After ingestion, Profile merge rules will automatically update the merged profile to reflect the most recent points and tier information.

recommendation-more-help
