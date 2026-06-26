---
title: "Connect Didomi to Experience Platform"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/consent/didomi"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:46.196348+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Connect Didomi to Experience Platform

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

AVAILABILITY
The Didomi source is in beta. Read the
terms and conditions
in the sources overview for more information on using beta-labeled sources.
Read this guide to learn how to connect your Didomi account to Adobe Experience Platform using the sources workspace in the UI.

IMPORTANT
- This documentation page was created by the *Didomi* team. For any inquiries or update requests, please contact them directly at *support@didomi.io*.
- For step-by-step instructions on generating the connection, refer to the [Didomi Adobe source connector documentation](https://developers.didomi.io/integrations/third-party-apps/preference-management-platform-integrations/Adobe-source-connector).

## Get started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

### Set up your Didomi account

Before you can proceed, ensure that you read and complete the prerequisite steps outlined in the [Didomi overview](/en/docs/experience-platform/sources/connectors/consent/didomi#prerequisites) to successfully connect your account to Experience Platform.

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to Didomi, go to the *Databases* category, select the **Didomi** source card, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Add your source data schema

Next, use the *Select data* interface to upload the JSON file that was [downloaded in the prerequisite steps](/en/docs/experience-platform/sources/connectors/consent/didomi#download-the-sample-payload-file).

You can use the preview interface to view the file structure of the payload. When finished, select **Next**.

## Provide dataflow details

Next, you must provide information regarding your dataset and your dataflow.

### Dataset details

A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows). Data that is successfully ingested into Experience Platform is persisted within the data lake as datasets.

During this step, you can either use an existing dataset or create a new dataset.

NOTE
Regardless of whether you use an existing dataset or create a new dataset, you must ensure that your dataset is
enabled for Profile
ingestion.
Select for steps to enable Profile ingestion, error diagnostics, and partial ingestion.
If your dataset is enabled for Real-Time Customer Profile, then during this step, you can toggle **Profile dataset** to enable your data for Profile-ingestion. You can also use this step to enable **Error diagnostics** and **Partial ingestion**.

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
Experience Platform can produce event-based alerts which users can subscribe to, these options all a running dataflow to trigger these. For more information, read the [alerts overview](/en/docs/experience-platform/sources/ui-tutorials/alerts)

- **Sources Dataflow Run Start**: Select this alert to receive a notification when your dataflow run begins.
- **Sources Dataflow Run Success**: Select this alert to receive a notification if your dataflow ends without any errors.
- **Sources Dataflow Run Failure**: Select this alert to receive a notification if your dataflow run ends with any errors.

## Mapping

Use the mapping interface to map your source data to the appropriate schema fields before ingesting data to Experience Platform. For more information, read the [mapping guide in the UI](/en/docs/experience-platform/data-prep/ui/mapping)

Mapping is used specifically to transfer **purpose data** from Didomi into the Experience Platform dataset. These purposes represent the user’s consent choices (such as, for analytics, personalization, advertising, etc.) and are the only accepted mapping fields in this integration.

Use the [sample webhook payload downloaded](/en/docs/experience-platform/sources/connectors/consent/didomi#download-the-sample-payload-file) from the Didomi webhook settings to map each Didomi purpose to the appropriate fields in your Adobe dataset.

When finished, select **Next**.

## Review

The *Review* step appears, allowing you to review the details of your dataflow before it is created. Details are group within the following categories:

- **Connection**: Shows the account name, source platform, and the source name.
- **Assign dataset and map fields**: Shows the target dataset and the schema that the dataset adheres to.

After confirming the details are correct, select **Finish**.

## Retrieve the streaming endpoint URL

With the connection created, the sources detail page appears. This page shows details of your newly created connection, including previously run dataflows, ID, and streaming endpoint URL.

## Finish the Configuration on Adobe

Once your dataflow is created, navigate to the *Sources* catalog and then select **Dataflows**. Use the dataflows directory to locate your Didomi dataflow and access the *Dataflow activity* interface. Next, use the *Properties* panel in the right-rail and retrieve values for the following:

- Streaming endpoint
- Dataflow ID

In the Experience Platform UI:

- After completing the configuration, review the configuration parameters that were missing from the initial webhook setup.
- Once these values are available, return to Didomi and update the webhook configuration.

## Update the Webhook Configuration

Once your configuration is complete, navigate back to the Didomi console and update your webhook configuration with your **streaming endpoint URL** and **dataflow ID**.

Once this is complete, Didomi will begin sending consent management and preference management events through the integration, and the data will be stored in your Adobe dataset.

## Next steps

By following this tutorial, you have successfully created a dataflow to bring batch data from your Didomi source to Experience Platform. For additional resources, visit the documentation outlined below.

### Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to view information on ingestion rates, success, and errors. For more information on how to monitor dataflow, visit the tutorial on [monitoring accounts and dataflows in the UI](/en/docs/experience-platform/dataflows/ui/monitor-sources).

### Update your dataflow

To update configurations for your dataflows scheduling, mapping, and general information, visit the tutorial on [updating sources dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/update-dataflows).

### Delete your dataflow

You can delete dataflows that are no longer necessary or were incorrectly created using the **Delete** function available in the **Dataflows** workspace. For more information on how to delete dataflows, visit the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/delete).

recommendation-more-help
