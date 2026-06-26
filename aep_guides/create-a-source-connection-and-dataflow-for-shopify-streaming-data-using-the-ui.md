---
title: "Create a source connection and dataflow for Shopify Streaming data using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/ecommerce/shopify-streaming"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:33:54.009551+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a source connection and dataflow for Shopify Streaming data using the UI

Last update: June 18, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to stream data from a Shopify Streaming source to Adobe Experience Platform through the user interface.

## Getting started getting-started

Before you begin, make sure you’re familiar with the following parts of Experience Platform:

- Experience Data Model (XDM) System : A standardized framework designed to help you organize and manage your customer experience data in a consistent way across Adobe Experience Platform. Basics of schema composition : An introduction to building your own data schemas, including simple best practices and how to structure your data effectively for your specific needs. Schema Editor tutorial : Step-by-step instructions to guide you through creating custom data schemas directly in the Platform UI, so you can tailor your data model to your business requirements.
- Real-Time Customer Profile : Empowers you to create comprehensive, real-time customer profiles that aggregate data from multiple sources, enabling a unified view of each individual customer.

IMPORTANT
This tutorial requires you to have completed the prerequisite setup for your Shopify Streaming account. For steps on setting up your account, read the
Shopify Streaming overview
.
## Connect your Shopify Streaming account

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Select the appropriate category in the *Categories* panel. Alternatively, use the search bar to navigate to the specific source that you want to use.

To stream data from Shopify, select the **Shopify Streaming** source card under *ecommerce* and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
### Create a new account

To create a new account for your Shopify Streaming source, select **New account** and provide a name and an optional description for your account. Next, provide values for your **primarySecretKey** and **secondarySecretKey** and then select **Connect to source**. Allow for a few moments for the connection to establish, and then select **Next** to proceed.

For more information on HMAC key-based authentication, read the [Shopify Streaming authentication overview](/en/docs/experience-platform/sources/connectors/ecommerce/shopify-streaming).

## Select data

The **Select data** step appears, providing an interface for you to select the data that you bring to Experience Platform.

- The left part of the interface is a browser that allows you to view the available data streams within your account;
- The right part of the interface lets you preview up to 100 rows of data from a JSON file.

Select **Upload files** to upload a JSON file from your local system. Alternatively, you can drag and drop the JSON file you want to upload into the Drag and drop files panel.

Once your file uploads, the preview interface updates to display a preview of the schema you uploaded. The preview interface allows you to inspect the contents and structure of a file. You can also use the Search field utility to access specific items from within your schema.

When finished, select **Next**.

## Dataflow detail

The **Dataflow detail** step appears, providing you with options to use an existing dataset or establish a new dataset for your dataflow, as well as an opportunity to provide a name and description for your dataflow. During this step, you can also configure settings for Profile ingestion, error diagnostics, partial ingestion, and alerts.

When finished, select **Next**.

## Mapping

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you select. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once your source data is successfully mapped, select **Next**.

## Review

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the number of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Get your streaming endpoint URL

With your streaming dataflow created, you can now retrieve your streaming endpoint URL. This endpoint will be used to subscribe to your webhook, allowing your streaming source to communicate with Experience Platform.

To retrieve your streaming endpoint, go to the Dataflow activity page of the dataflow that you just created and copy the endpoint from the bottom of the Properties panel.

## Next steps

By following this tutorial, you have established a source connection and dataflow to your Shopify Streaming account. For instructions on how to connect your Shopify Streaming account using the API, please read the tutorial on [creating a source connection and dataflow to stream Shopify data using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/create/ecommerce/shopify-streaming).

recommendation-more-help
