---
title: "Map a CSV file to an existing XDM schema"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/tutorials/map-csv/existing-schema"
category: "tutorials"
topic: "experience-platform/data-ingestion-guide"
created_at: "2026-05-29T17:07:32.209735+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Ingestion Guide

# Map a CSV file to an existing XDM schema

Last update: May 23, 2026
- Topics:
- [Data Ingestion](#)

CREATED FOR:

- Developer

NOTE
This document covers how to map a CSV file to an existing XDM schema. For information on how to use the AI-generated schema recommendation tool (currently in beta), see the document on
mapping a CSV file using machine-learning recommendations
.
In order to ingest CSV data into Adobe Experience Platform, the data must be mapped to an Experience Data Model (XDM) schema. This tutorial covers how to map a CSV file to an XDM schema using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- [Experience Data Model (XDM System)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Batch ingestion](/en/docs/experience-platform/ingestion/batch/overview): The method by which Experience Platform ingests data from user-supplied datafiles.
- [Adobe Experience Platform Data Prep](/en/docs/experience-platform/ingestion/batch/overview): A suite of capabilities that allow you to map and transform ingested data to conform to XDM schemas. The documentation on [Data Prep functions](/en/docs/experience-platform/data-prep/functions) is particularly relevant for schema mapping.

This tutorial also requires that you have already created a dataset to ingest your CSV data into. For steps on creating a dataset in the UI, see the [data ingest tutorial](/en/docs/experience-platform/ingestion/tutorials/ingest-batch-data).

## Choose a destination

Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Workflows** from the left navigation bar to access the **Workflows** workspace.

From the **Workflows** screen, select **Map CSV to XDM schema** under the **Data ingestion** section and then select **Launch**.

The **Map CSV to XDM schema** workflow appears, starting on the **Destination** step. Choose a dataset for inbound data to be ingested into. You can either use an existing dataset or create a new one.

**Use an existing dataset**

To ingest your CSV data into an existing dataset, select **Use existing dataset**. You can either retrieve an existing dataset using the search function or by scrolling through the list of existing datasets in the panel.

To ingest your CSV data into a new dataset, select **Create new dataset** and enter a name and description for the dataset in the fields provided. Select a schema by using either the search function or by scrolling through the list of schemas provided. Select **Next** to proceed.

## Add data

The **Add data** step appears. Drag-and-drop your CSV file into the space provided, or select **Choose files** to manually input your CSV file.

The **Sample data** section appears once the file is uploaded, showing the first ten rows of data. Once you have confirmed that the data has uploaded as expected, select **Next**.

## Map CSV fields to XDM schema fields

The **Mapping** step appears. The columns of the CSV file are listed under **Source Field**, with their corresponding XDM schema fields listed under **Target Field**.

Experience Platform automatically provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases.

To accept all the auto-generating mapping values, select the checkbox labelled “Accept all target fields”.

Sometimes, more than one recommendation is available for the source schema. When this happens, the mapping card displays the most prominent recommendation, followed by a blue circle that contains the number of additional recommendations available. Selecting the light bulb icon will show a list of the additional recommendations. You can choose one of the alternate recommendations by selecting the checkbox next to the recommendation you want to map to instead.

Alternatively, you can choose to manually map your source schema to your target schema. Hover over the source schema you want to map, then select the plus icon.

The **Map source to target field** popover appears. From here, you can select which field you want to be mapped, followed by **Save** to add your new mapping.

If you want to remove one of the mappings, hover over that mapping, then select the minus icon.

### Add calculated field add-calculated-field

Calculated fields allow for values to be created based on the attributes in the input schema. These values can then be assigned to attributes in the target schema and be provided a name and description to allow for easier reference.

Select the **Add calculated field** button to proceed.

The **Create calculated field** panel appears. The left dialog box contains the fields, functions, and operators supported in calculated fields. Select one of the tabs to start adding functions, fields, or operators to the expression editor.

Tab
Description
Fields
The fields tab lists fields and attributes available in the source schema.
Functions
The functions tab lists the functions available to transform the data. To learn more about the functions you can use within calculated fields, please read the guide on
using Data Prep (Mapper) functions
.
Operators
The operators tab lists the operators that are available to transform the data.
You can manually add fields, functions, and operators using the expression editor at the center. Select the editor to start creating an expression.

Select **Save** to proceed.

The mapping screen reappears with your newly created source field. Apply the appropriate corresponding target field and select **Finish** to complete the mapping.

## Monitor data ingestion

Once your CSV file is mapped and created, you can monitor the data that is being ingested through it. For more information on monitoring data ingestion, see the tutorial on [monitoring data ingestion](/en/docs/experience-platform/ingestion/quality/monitor-data-ingestion).

## Next steps

By following this tutorial, you have successfully mapped a flat CSV file to an XDM schema and ingested it into Experience Platform. This data can now be used by downstream Experience Platform services such as Real-Time Customer Profile. See the overview for [Real-Time Customer Profile](/en/docs/experience-platform/profile/home) for more information.

TIP
You can also use machine learning (ML) algorithms to
generate a schema from sample data
from the Schema workspace. This workflow automatically creates a new schema based on the structure and content of your file, ensuring that the schema matches your data’s format. This saves you time and increases accuracy when defining the structure, fields, and data types for large complex datasets. See the
ML-Assisted schema creation guide
for more information on this workflow.
recommendation-more-help
