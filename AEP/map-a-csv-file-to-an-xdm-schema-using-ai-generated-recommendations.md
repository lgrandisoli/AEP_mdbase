---
title: "Map a CSV file to an XDM schema using AI-generated recommendations"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/tutorials/map-csv/recommendations"
category: "tutorials"
topic: "experience-platform/data-ingestion-guide"
created_at: "2026-05-29T17:00:49.452317+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Ingestion Guide

# Map a CSV file to an XDM schema using AI-generated recommendations

Last update: May 23, 2026
- Topics:
- [Data Ingestion](#)

CREATED FOR:

- Developer

NOTE
For information on generally available CSV mapping capabilities in Experience Platform, see the document on
mapping a CSV file to an existing schema
.
In order to ingest CSV data into Adobe Experience Platform, the data must be mapped to an Experience Data Model (XDM) schema. You can choose to map to [an existing schema](/en/docs/experience-platform/ingestion/tutorials/map-csv/existing-schema), but if you do not know exactly which schema to use or how it should be structured, you can instead use dynamic recommendations based on machine-learning (ML) models within the Experience Platform UI.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- [Experience Data Model (XDM System)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. At a minimum, you must understand the concept of behaviors in XDM , so you can decide whether to map your data to a Profile class (record behavior) or ExperienceEvent class (time-series behavior).
- [Batch ingestion](/en/docs/experience-platform/ingestion/batch/overview): The method by which Experience Platform ingests data from user-supplied datafiles.
- [Adobe Experience Platform Data Prep](/en/docs/experience-platform/ingestion/batch/overview): A suite of capabilities that allow you to map and transform ingested data to conform to XDM schemas. The documentation on [Data Prep functions](/en/docs/experience-platform/data-prep/functions) is specifically relevant for schema mapping.

## Provide dataflow details

In the Experience Platform UI, select **Sources** in the left navigation. On the **Catalog** view, navigate to the **Local system** category. Under **Local file upload**, select **Add data**.

The **Map CSV XDM schema** workflow appears, starting on the **Dataflow detail** step.

Select **Create a new schema using ML recommendations**, causing new controls to appear. Choose the appropriate class for the CSV data you want to map (Profile or ExperienceEvent). You can optionally use the dropdown menu to select the relevant industry for your business, or leave it blank if the provided categories do not apply to you. If your organization operates under a [business-to-business (B2B)](/en/docs/experience-platform/xdm/tutorials/relationship-b2b) model, select the **B2B data** checkbox.

From here, provide a name for the schema that will be created from the CSV data, and a name for the output dataset that will contain the data ingested under that schema.

You can optionally configure the following additional features for the dataflow before proceeding:

Input name
Description
Description
A description for the dataflow.
Error diagnostics
When enabled, error messages are generated for newly ingested batches, which can be viewed when fetching the corresponding batch in the
API
.
Partial ingestion
When enabled, valid records for new batch data will be ingested within a specified error threshold. This threshold allows you to configure the percentage of acceptable errors before the entire batch fails.
Dataflow details
Provide a name and optional description for the dataflow that will bring the CSV data into Experience Platform. The dataflow is automatically assigned a default name when starting this workflow. Changing the name is optional.
Alerts
Select from a list of
in-product alerts
that you want to receive regarding the status of the dataflow once it has been initiated.
When you are finished configuring the dataflow, select **Next**.

## Select data

On the **Select data** step, use the left column to upload your CSV file. You can select **Choose files** to open a file explorer dialog to select the file from, or you can drag and drop the file onto the column directly.

After uploading the file, a sample data section appears that shows the first ten rows of the received data so you can verify it has uploaded correctly. Select **Next** to continue.

## Configure schema mappings

The ML models are run to generate a new schema based on your dataflow configuration and your uploaded CSV file. When the process is complete, the Mapping step populates to show the mappings for each individual field alongside fully navigable view of the generated schema structure.

NOTE
You can filter all fields in your schema based on a variety of criteria during the source-to-target field mapping workflow. The default behavior is to display all mapped fields. To change the displayed fields, select the filter icon next to the search input field and choose from the dropdown options.
{width="100" modal="regular"}
From here, you can optionally [edit the field mappings](#edit-mappings) or [alter the field groups they are associated with](#edit-schema) according to your needs. When satisfied, select **Finish** to complete the mapping and initiate the dataflow you configured earlier. The CSV data is ingested into the system and populates a dataset based on the generated schema structure, ready to be consumed by downstream Experience Platform services.

### Edit field mappings edit-mappings

Use the field mapping preview to edit existing mappings or remove them entirely. For more information on how to manage a mapping set in the UI, refer to the [UI guide for Data Prep mapping](/en/docs/experience-platform/data-prep/ui/mapping#mapping-interface).

### Edit field groups edit-field-groups

The CSV fields are automatically mapped to existing XDM field groups using ML models. If you want to change the field group for any particular CSV field, select **Edit** next to the schema tree.

A dialog appears, allowing you to edit the display name, data type, and field group for any field in the mapping. Select the edit icon ( ) next to a source field to edit its details in the right column before selecting **Apply**.

When you are finished adjusting the schema recommendations for your source fields, select **Save** to apply the changes.

## Next steps

This guide covered how to map a CSV file to an XDM schema using AI-generated recommendations, allowing you to bring that data into Experience Platform through batch ingestion.

For steps on mapping a CSV file to an existing schema, refer to the [existing schema mapping workflow](/en/docs/experience-platform/ingestion/tutorials/map-csv/existing-schema). For information on streaming data to Experience Platform in real time through prebuilt source connections, refer to the [sources overview](/en/docs/experience-platform/sources/home).

You can also use Machine Learning (ML) algorithms to **generate a schema from sample CSV data**. This workflow automatically creates a new schema based on the structure and content of your CSV file. This newly created schema matches your data’s format to save you time and increase accuracy when defining the structure, fields, and data types for large complex datasets. See the [ML-Assisted schema creation guide](/en/docs/experience-platform/xdm/ui/ml-assisted-schema-creation) for more information on this workflow.

recommendation-more-help
