---
title: "Create an Adobe Campaign Managed Cloud Services source connection using Experience Platform UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/campaign"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:24:45.567357+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Adobe Campaign Managed Cloud Services source connection using Experience Platform UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps to create a source connection to bring your Adobe Campaign Managed Cloud Services data to Adobe Experience Platform.

## Getting started

This guide requires a working understanding of the following components of Experience Platform:

- Sources : Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Sandboxes : Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Connect Adobe Campaign Managed Cloud Services to Experience Platform

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources that you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. You can also use the search bar to narrow down the displayed sources.

Under the **Adobe applications** category, select **Adobe Campaign Managed Cloud Services** and then select **Add data**.

### Select data select-data

The Select data step appears, providing you with an interface to configure your Adobe Campaign instance, Target mapping, and Schema name.

Property
Description
Adobe Campaign instance
The name of the Adobe Campaign environment instance that you are using.
Target mapping
The technical objects used by Campaign in order to deliver messages, and contain all the technical settings required to send deliveries.
Schema name
The name of the schema entity that you are bringing to Experience Platform. Options include Delivery Log and Tracking Log.
Once you have provided values for your Campaign instance, target mapping, and schema name, the screen updates to display a preview of your schema as well as a sample dataset. When finished, select **Next**.

### Use an existing dataset

The Dataflow detail page allows you to select whether you want to use an existing dataset or configure a new dataset for your dataflow.

To use an existing dataset, select **Existing dataset**. You can either retrieve an existing dataset using the Advanced search option or by scrolling through the list of existing datasets in the dropdown menu.

With a dataset selected, provide a name for your dataflow and an optional description.

### Use a new dataset

To use a new dataset, select **New dataset** and then provide an output dataset name and an optional description. Next, select a schema to map to using the Advanced search option or by scrolling through the list of existing schemas in the dropdown menu. When finished, select **Next**.

### Enable alerts

You can enable alerts to receive notifications on the status of your dataflow. Select an alert from the list to subscribe and receive notifications on the status of your dataflow. For more information on alerts, see the guide on [subscribing to sources alerts using the UI](/en/docs/experience-platform/sources/ui-tutorials/alerts).

When you are finished providing details to your dataflow, select **Next**.

### Map data fields to an XDM schema

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

IMPORTANT
When mapping your source fields to target XDM fields, you must ensure that you map your designated primary identity field to its appropriate target XDM field.
For each audience, you can add up to 20 fields to map to Adobe Campaign. You can change this limit by updating the value of the
NmsCdp_Aep_Sources_Max_Columns
option in the Administration > Platform > Options folder of Campaign explorer.
Once your source data is successfully mapped, select **Next**.

### Review your dataflow

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the amount of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

### Monitor your dataset activity

Once your dataflow has been created, you can monitor the data that is being ingested through it to see information on ingested rates and successful and failed batches.

To start viewing your dataset activity, select **Dataflows** in the sources catalog.

Next, select the target dataset from the list of dataflows that appear.

The dataset activity page appears. From here, you can see information on the performance of your dataflow, including rate of ingestion, successful batches, and failed batches.

This page also provides you with an interface to update the metadata description of your dataflow, enable partial ingestion and error diagnostics, as well as add new data to your dataset.

IMPORTANT
You cannot backfill old event logs with the Adobe Campaign Managed Cloud Services source. If backfill is required, use a custom workflow or a custom implementation to export data to Amazon S3 or Azure Blob, or from Amazon S3 or Azure Blob to an Adobe Experience Platform dataset.
## Next steps

By following this tutorial, you have successfully created a dataflow to bring your Campaign v8 delivery logs and tracking logs data to Experience Platform. Incoming data can now be used by downstream Experience Platform services such as Real-Time Customer Profile and Data Science Workspace. See the following documents for more details:

- [Real-Time Customer Profile overview](/en/docs/experience-platform/profile/home)
- [Data Science Workspace overview](/en/docs/experience-platform/data-science-workspace/home)

recommendation-more-help
