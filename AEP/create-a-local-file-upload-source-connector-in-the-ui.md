---
title: "Create a local file upload source connector in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/local-system/local-file-upload"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:22.844380+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a local file upload source connector in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a local file upload source connector to ingest local files to Experience Platform using the user interface.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Upload local files to Experience Platform

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources for which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Local system category, select **Local file upload**, and then select **Add data**.

### Use an existing dataset

The Dataflow detail page allows you to select whether you want to ingest your CSV data into an existing dataset or a new dataset.

To ingest your CSV data into an existing dataset, select **Existing dataset**. You can either retrieve an existing dataset using the Advanced search option or by scrolling through the list of existing datasets in the dropdown menu.

With a dataset selected, provide a name for your dataflow and an optional description.

During this process, you can also enable Error diagnostics and Partial ingestion. Error diagnostics enables detailed error message generation for any erroneous records that occur in your dataflow, while Partial ingestion allows you to ingest data containing errors, up to a certain threshold that you manually define. See the [partial batch ingestion overview](/en/docs/experience-platform/ingestion/batch/partial) for more information.

### Use a new dataset

To ingest your CSV data into a new dataset, select **New dataset** and then provide an output dataset name and an optional description. Next, select a schema to map to using the Advanced search option or by scrolling through the list of existing schemas in the dropdown menu.

With a schema selected, provide a name for your dataflow and an optional description, and then apply the Error diagnostics and Partial ingestion settings you want for your dataflow. When finished, select **Next**.

### Select data

The Select data step appears, providing you an interface to upload your local files and preview their structure and contents. Select **Choose files** to upload a CSV file from your local system. Alternatively, you can drag and drop the CSV file you want to upload into the Drag and drop files panel.

TIP
Only CSV files are currently supported by local file upload. The maximum file size for each file is 1 GB.
Once your file is uploaded, the preview interface updates to display the contents and structure of the file.

Depending on your file, you can select a column delimiter such as tabs, commas, pipes, or a custom column delimiter for your source data. Select the **Delimiter** dropdown arrow and then select the appropriate delimiter from the menu.

When finished, select **Next**.

## Mapping

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapping interface, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once your mapping sets are ready, select **Finish** and allow for a few moments for the new dataflow to be created.

## Monitor data ingestion

Once your CSV file is mapped and created, you can monitor the data that is being ingested through it using the monitoring dashboard. For more information, see the tutorial on [monitoring sources dataflows in the UI](/en/docs/experience-platform/dataflows/ui/monitor-sources).

## Next steps

By following this tutorial, you have successfully mapped a flat CSV file to an XDM schema and ingested it into Experience Platform. This data can now be used by downstream Experience Platform services such as Real-Time Customer Profile. See the overview for [Real-Time Customer Profile](/en/docs/experience-platform/profile/home) for more information.

recommendation-more-help
