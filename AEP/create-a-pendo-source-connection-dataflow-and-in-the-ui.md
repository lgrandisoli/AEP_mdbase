---
title: "Create a Pendo source connection dataflow and in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/analytics/pendo-webhook"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:32.647800+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Create a Pendo source connection dataflow and in the UI

Last update: May 26, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The Pendo source is in beta. Please read the
sources overview
for more information on using beta-labeled sources.
This tutorial provides steps for creating a Pendo source connection and dataflow using the Adobe Experience Platform user interface.

## Getting started getting-started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Prerequisites prerequisites

The following section provides information on prerequisites to complete before you can create a Pendo source connection.

### Sample JSON to define the source schema for Pendo prerequisites-json-schema

Before creating a Pendo source connection, you will require a source schema to be provided. You can use the JSON below.

```
{
  "accountId": "58f79ee324d3f",
  "timestamp": 1673372516,
  "visitorId": "test@test.com",
  "uniqueId": "166e50cdf40930fe1367e4d44795c9c74d88b83a",
  "properties": {
    "guideProperties": {
  "name": "Guide Conversion Test"
  }
}
}
```

For more information, read the [Pendo guide on webhooks](https://support.pendo.io/hc/en-us/articles/360032285012-Webhooks).

### Create an Experience Platform schema for Pendo create-platform-schema

You must also ensure that you first create an Experience Platform schema to use for your source. See the tutorial on [creating an Experience Platform schema](/en/docs/experience-platform/xdm/schema/composition) for comprehensive steps on how to create a schema.

## Connect your Pendo account connect-account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace and see a catalog of sources available in Experience Platform.

Use the *Categories* menu to filter sources by category. Alternatively, enter a source name in the search bar to find a specific source from the catalog.

Go to the Analytics category to see the Pendo source card. To begin, select **Add data**.

## Select data select-data

The **Select data** step appears, providing an interface for you to select the data that you want to bring to Experience Platform.

- The left part of the interface is a browser that allows you to view the available data streams within your account;
- The right part of the interface lets you preview up to 100 rows of data from a JSON file.

Select **Upload files** to upload a JSON file from your local system. Alternatively, you can drag and drop the JSON file you want to upload into the Drag and drop files panel.

Once your file uploads, the preview interface updates to display a preview of the schema you uploaded. The preview interface allows you to inspect the contents and structure of a file. You can also use the Search field utility to access specific items from within your schema.

When finished, select **Next**.

## Dataflow detail dataflow-detail

The **Dataflow detail** step appears, providing you with options to use an existing dataset or establish a new dataset for your dataflow, as well as an opportunity to provide a name and description for your dataflow. During this step, you can also configure settings for Profile ingestion, error diagnostics, partial ingestion, and alerts.

When finished, select **Next**.

## Mapping mapping

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

The mappings listed below are mandatory and should be setup before proceeding to the Review stage.

Target Field
Description
uniqueId
The Pendo identifier for the event.
Once your source data is successfully mapped, select **Next**.

## Review review

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the amount of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Get your streaming endpoint URL get-streaming-endpoint-url

With your streaming dataflow created, you can now retrieve your streaming endpoint URL. This endpoint will be used to subscribe to your webhook, allowing your streaming source to communicate with Experience Platform.

In order to construct the URL used to configure the webhook on Pendo you must retrieve the following:

- **Dataflow ID**
- **Streaming endpoint**

To retrieve your **Dataflow ID** and **Streaming endpoint**, go to the Dataflow activity page of the dataflow that you just created and copy the details from the bottom of the Properties panel.

Once you have retrieved your streaming endpoint and dataflow ID, build a URL based on the following pattern: {STREAMING_ENDPOINT}?x-adobe-flow-id={DATAFLOW_ID}. For example, a constructed webhook URL may look like: https://dcs.adobedc.net/collection/0c61859cc71939a0caf01123f91b2fc52589018800ad46b6c76c2dff3595ee95

## Set up Webhook in Pendo set-up-webhook

Next, login to your account on [Pendo](https://pendo.io/) and create a webhook. For steps on how to create a webhook using the Pendo user interface, please refer to the [Pendo guide on creating webhook](https://support.pendo.io/hc/en-us/articles/360032285012-Webhooks#create-a-webhook-0-4).

Once your webhook is created, navigate to the settings page of your Pendo webhook and input your webhook URL in the URL field.

TIP
You can subscribe to a variety of different events categories to determine the kind of events you want to send from your Pendo instance to Experience Platform. For more information on the different events, please refer to the
Pendo documentation
.
## Next steps next-steps

By following this tutorial you have successfully configured a streaming dataflow to bring your Pendo data to Experience Platform. To monitor the data that is being ingested, refer to the guide on [monitoring streaming dataflows using Experience Platform UI](/en/docs/experience-platform/sources/ui-tutorials/monitor-streaming).

## Additional resources additional-resources

The sections below provide additional resources that you can refer to when using the Pendo source.

### Validation validation

To validate that you have correctly set up the source and Pendo messages are being ingested, follow the steps below:

- You can check the Pendo **Reports** > **Chat History** page to identify the events being captured by Pendo.

- In the Experience Platform UI, select **View Dataflows** beside the Pendo card menu on the sources catalog. Next, select **Preview dataset** to verify the data that was ingested for the webhooks that you have configured within Pendo.

### Errors and troubleshooting errors-and-troubleshooting

When checking a dataflow run, you might encounter the following error message: The message can't be validated ... uniqueID:expected minLength:1, actual 0].

To fix this error, you must verify that the *uniqueID* mapping has been set up. For additional guidance, refer to the [Mmpping](#mapping) section.

For more information visit the [Pendo Help Center](https://www.pendo.io/help-center/).

recommendation-more-help
