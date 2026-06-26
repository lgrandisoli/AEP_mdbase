---
title: "Create a streaming dataflow for a cloud storage source in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage-streaming"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:35:56.958050+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a streaming dataflow for a cloud storage source in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A dataflow is a scheduled task that retrieves and ingests data from a source to an Adobe Experience Platform dataset. This tutorial provides steps to create a streaming dataflow for a cloud storage source in the UI.

Before attempting this tutorial, you must first establish a valid and authenticated connection between your cloud storage account and Experience Platform. If you do not already have an authenticated connection, see one of the following tutorials for information on authenticating your streaming cloud storage accounts:

- [Amazon Kinesis](/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/kinesis)
- [Azure Event Hubs](/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/eventhub)
- [Google PubSub](/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/google-pubsub)

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Dataflows : Dataflows are a representation of data jobs that move data across Experience Platform. Dataflows are configured across different services, from sources, to Identity Service, to Profile, and to Destinations.
- Data Prep : Data Prep allows data engineers to map, transform, and validate data to and from Experience Data Model (XDM). Data Prep appears as a “Map” step in the Data Ingestion processes, including CSV Ingestion workflow.
- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Add data

NOTE
You can only create one source dataflow per consumer group for a given Event Hub.
After creating your authenticating your streaming cloud storage account, the **Select data** step appears, providing an interface for you to select which data stream you will bring to Experience Platform.

- The left part of the interface is a browser that allows you to view the available data streams within your account;
- The right part of the interface lets you preview up to 100 rows of data from a JSON file.

Select the data stream that you want to use, and then select **Choose file** to upload a sample schema.

TIP
If your data is XDM compliant, you can skip uploading a sample schema, and select
Next
to proceed.
Once your schema uploads, the preview interface updates to display a preview of the schema you uploaded. The preview interface allows you to inspect the contents and structure of a file. You can also use the Search field utility to access specific items from within your schema.

When finished, select **Next**.

## Mapping

The **Mapping** step appears, providing an interface to map the source data to an Experience Platform dataset.

Choose a dataset for inbound data to be ingested into. You can either use an existing dataset or create a new one.

### New dataset

To ingest data into a new dataset, select **New dataset** and enter a name and description for the dataset in the fields provided. To add a schema, you can enter an existing schema name in the **Select schema** dialog box. Alternatively, you can select **Schema advanced search** to search for an appropriate schema.

The Select schema window appears, providing you with a list of available schemas to choose from. Select a schema from the list to update the right-rail to display details specific to the schema you selected, including information on whether the schema is enabled for Profile.

Once you have identified and selected the schema you want to use, select **Done**.

The Target dataset page updates with your selected schema displayed as part of the dataset. During this step, you can enable your dataset for Profile and create a holistic view of an entity’s attributes and behaviors. Data from all enabled datasets will be included in Profile and changes are applied when you save your dataflow.

Toggle the **Profile dataset** button to enable your target dataset for Profile.

### Existing dataset

To ingest data into an existing dataset, select **Existing dataset**, then select the dataset icon.

The **Select dataset** dialog appears, providing you with a list of available datasets to choose from. Select a dataset from the list to update the right-rail to display details specific to the dataset you selected, including information on whether the dataset can be enabled for Profile.

Once you have identified and selected the dataset you want to use, select **Done**.

Once you select your dataset, select the Profile toggle to enable your dataset for Profile.

### Map standard fields

With your dataset and schema established, the **Map standard fields** interface appears, allowing you to manually configure mapping fields for your data.

TIP
Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases.
Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once your source data is mapped, select **Next**.

## Dataflow detail

The **Dataflow detail** step appears, allowing you to name and give a brief description about your new dataflow.

Provide values for the dataflow and select **Next**.

### Review

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Displays your account name, type of source, and other miscellaneous information specific to the streaming cloud storage source you are using.
- **Assign dataset and map fields**: Displays the target dataset and schema you are using for your dataflow.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Monitor and delete your dataflow

Once your streaming cloud storage dataflow has been created, you can monitor the data that is being ingested through it. For more information on monitoring and deleting streaming dataflows, see the tutorial on [monitoring streaming dataflows](/en/docs/experience-platform/sources/ui-tutorials/monitor-streaming).

## Next steps

By following this tutorial, you have successfully created a dataflow to stream data from a cloud storage source. Incoming data can now be used by downstream Experience Platform services such as Real-Time Customer Profile and Data Science Workspace. See the following documents for more details:

- [Real-Time Customer Profile overview](/en/docs/experience-platform/profile/home)
- [Data Science Workspace overview](/en/docs/experience-platform/data-science-workspace/home)

recommendation-more-help
