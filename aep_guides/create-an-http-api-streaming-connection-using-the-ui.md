---
title: "Create an HTTP API streaming connection using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/streaming/http"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:38:33.063927+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an HTTP API streaming connection using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a streaming source connection using the Sources workspace.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Create a streaming connection

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources that you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the **Streaming** category, select **HTTP API** and then select **Add data**.

The **Connect HTTP API account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the HTTP API account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**. On the input form that appears, provide an account name and an optional description. You will also get the option of providing the following configuration properties:

- **Authentication:** This property determines whether or not the streaming connection requires authentication. Authentication ensures that data is collected from trusted sources. If you’re dealing with Personally Identifiable Information (PII), this property should be turned on. By default, this property is turned off.
- **XDM compatible:** This property denotes if this streaming connection will be sending events which are compatible with XDM schemas. By default, this property is turned off.

When finished, select **Connect to source** and then select **Next** to proceed.

## Select data

After creating the HTTP API connection, the **Select data** step appears, providing you with an interface to upload and preview your data.

Select **Upload files** to upload your data. Alternatively, you can drag and drop your data into the Drag and drop files section of the interface.

With your data uploaded, you can use the right-side of the interface to preview your file hierarchy. Select **Next** to proceed.

## Map data fields to an XDM schema

The Mapping step appears, providing an interface to map the source data to an Experience Platform dataset.

The HTTP API source supports ingestion of JSON files. JSON files do not require manual configuration if they are marked as XDM-complaint. If not, then you must explicitly configure the mapping.

Choose a dataset for inbound data to be ingested into. You can either use an existing dataset or create a new one.

### Create a new dataset

To create a new dataset, select **New dataset**. On the form that appears, provide the name, an optional description, as well as the target schema for the dataset. If you select a Profile-enabled schema, you can choose if the dataset should also be Profile-enabled.

### Use an existing dataset

To use an existing dataset, select **Existing dataset**. On the form that appears, select the dataset that you want to use. Once you select a dataset, you can choose if the dataset should be Profile-enabled.

### Map standard fields

Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

To add a new source field, select **Add new mapping**.

A new source field and target field pairing appears. To add a new source field, select the arrow icon beside the Select source field input bar.

The Select attributes panel allows you to explore your file hierarchy and select a specific source field to map to a target XDM field. Once you have selected the source field you want to map, select **Select** to proceed.

With a source field selected, you can now identify the appropriate target XDM field to map to. Select the schema icon under the target field section.

The Map source field to target field window appears, providing you with an interface to explore the schema of your target dataset. Select the target field that matches your source field, and then select **Select** to proceed.

Once your source fields are all mapped to their appropriate target XDM fields, select **Next**

## Dataflow detail

The **Dataflow detail** step appears. On this page, you can provide details for the created dataflow by giving a name and an optional description.

After providing details for the dataflow, select **Next**.

## Review

The **Review** step appears, allowing you to review the details of your dataflow before it is created. Details are group within the following categories:

- **Connection**: Shows the account name, source platform, and the source name.
- **Assign dataset and map fields**: Shows the target dataset and the schema that the dataset adheres to.

After confirming the details are correct, select **Finish**.

## Get streaming endpoint URL

With the connection created, the sources detail page appears. This page shows details of your newly created connection, including previously run dataflows, ID, and streaming endpoint URL.

## Next steps

By following this tutorial, you have created a streaming HTTP connection, enabling you to use the streaming endpoint to access a variety of Data Ingestion APIs. For instructions to create a streaming connection in the API, please read the [creating a streaming connection tutorial](/en/docs/experience-platform/sources/api-tutorials/create/streaming/http).

To learn how to stream data to Experience Platform, please read either the tutorial on [streaming time series data](/en/docs/experience-platform/ingestion/tutorials/streaming-time-series-data) or the tutorial on [streaming record data](/en/docs/experience-platform/ingestion/tutorials/streaming-record-data).

recommendation-more-help
