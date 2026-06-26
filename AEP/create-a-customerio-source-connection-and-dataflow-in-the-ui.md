---
title: "Create a Customer.io source connection and dataflow in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/marketing-automation/customerio-webhook"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:27.477967+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Create a Customer.io source connection and dataflow in the UI

Last update: May 26, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The Customer.io source is in beta. Please read the
sources overview
for more information on using beta-labeled sources.
This tutorial provides steps for creating a Customer.io source connection and dataflow using the Adobe Experience Platform user interface.

## Getting started getting-started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Prerequisites prerequisites

The following section provides information on prerequisites to complete before you can create a Customer.io source connection.

### Sample JSON to define the source schema for Customer.io prerequisites-json-schema

Before creating a Customer.io source connection, you will require a source schema to be provided. You can use the below JSON.

```
{
  "event_id": "01E4C4CT6YDC7Y5M7FE1GWWPQJ",
  "object_type": "customer",
  "metric": "subscribed",
  "timestamp": 1613063089,
  "data": {
    "customer_id": "42",
    "email_address": "test@example.com",
    "identifiers": {
      "id": "42",
      "email": "test@example.com",
      "cio_id": "d9c106000001"
    }
  }
}
```

### Create an Experience Platform schema for Customer.io create-platform-schema

You must also ensure that you create an Experience Platform schema to use for your source. See the tutorial on [creating an Experience Platform schema](/en/docs/experience-platform/xdm/schema/composition) for comprehensive steps on how to create a schema.

## Connect your Customer.io account connect-account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace and see a catalog of sources available in Experience Platform.

Use the *Categories* menu to filter sources by category. Alternatively, enter a source name in the search bar to find a specific source from the catalog.

Go to the Marketing automation category to see the Customer.io source card. To begin, select **Add data**.

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

All the mappings listed below are mandatory and should be setup before proceeding to the Review stage.

Target Field
Description
object_type
The object type, refer to the Customer.io
events
documentation for the supported types.
id
The object’s identifier.
email
The email address associated with the object.
event_id
The unique identifier of the event.
cio_id
The Customer.io identifier for the event.
metric
The event type. For more information, refer to the Customer.io
events
documentation for supported types.
timestamp
The timestamp when the event occurred.
IMPORTANT
Do not map
cio_id
when executing Customer.io webhook in the
test mode
as there will be no associated fields sent from Customer.io.
Once your source data is successfully mapped, select **Next**.

## Review review

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the amount of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Get your streaming endpoint URL get-streaming-endpoint

With your streaming dataflow created, you can now retrieve your streaming endpoint URL. This endpoint will be used to subscribe to your webhook, allowing your streaming source to communicate with Experience Platform.

In order to construct the URL used to configure the webhook on Customer.io you must retrieve the following:

- **Dataflow ID**
- **Streaming endpoint**

To retrieve your **Dataflow ID** and **Streaming endpoint**, go to the Dataflow activity page of the dataflow that you just created and copy the details from the bottom of the Properties panel.

Once you have retrieved your streaming endpoint and dataflow ID, build a URL based on the following pattern: {STREAMING_ENDPOINT}?x-adobe-flow-id={DATAFLOW_ID}. For example, a constructed webhook URL may look like: https://dcs.adobedc.net/collection/febc116d22ba0ea2868e9c93b199375302afb8a589617700991bb8f3f0341ad7?x-adobe-flow-id=439b3fc4-3042-4a3a-b5e0-a494898d3fb0

## Set up reporting webhook in Customer.io set-up-webhook

With your webhook URL created, you can now set up your reporting webhook using the Customer.io user interface. For steps on setting up reporting webhooks, please read the [Customer.io guide](https://customer.io/docs/webhooks/#setup) on setting up webhooks.

In the Customer.io user interface, input your [webhook URL](#get-streaming-endpoint-url) in the WEBHOOK ENDPOINT field.

TIP
You can subscribe to a variety of different events for your reporting webhook. Each events’ message will be ingested to Experience Platform when a Customer.io action event trigger criteria is met. For more information on the different events, please refer to the
Customer.io events documentation
.
## Next steps next-steps

By following this tutorial you have successfully configured a streaming dataflow to bring your Customer.io data to Experience Platform. To monitor the data that is being ingested, refer to the guide on [monitoring streaming dataflows using Experience Platform UI](/en/docs/experience-platform/sources/ui-tutorials/monitor-streaming).

## Additional resources additional-resources

The sections below provide additional resources that you can refer to when using the Customer.io source.

### Guardrails guardrails

For information on guardrails, please refer to the [Customer.io timeouts and failures page](https://customer.io/docs/webhooks/#timeouts-and-failures).

### Validation validation

To validate that you have correctly set up the source and Customer.io messages are being ingested, follow the steps below:

- You can check the Customer.io **Activity Logs** page to identify the events being captured by Customer.io.

- In the Experience Platform UI, select **View Dataflows** beside the Customer.io card menu on the sources catalog. Next, select **Preview dataset** to verify the data that was ingested for the events that you have selected within Customer.io.

recommendation-more-help
