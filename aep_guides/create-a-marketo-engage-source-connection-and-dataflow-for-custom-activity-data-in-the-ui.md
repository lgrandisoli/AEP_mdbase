---
title: "Create a Marketo Engage source connection and dataflow for custom activity data in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/marketo-custom-activities"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:24:51.801969+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Marketo Engage source connection and dataflow for custom activity data in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
This tutorial provides specific steps on how to set up and bring
custom activity
data from Marketo to Experience Platform. For steps on how to bring
standard activity
data, read the
Marketo UI guide
.
In addition to [standard activities](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#activities), you can also use the Marketo source to bring custom activities data to Adobe Experience Platform. This document provides steps on how to create a source connection and dataflow for custom activity data using the Marketo source in the UI.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- [B2B namespaces and schema auto-generation utility](/en/docs/experience-platform/sources/connectors/adobe-applications/marketo/marketo-namespaces): The B2B namespaces and schema auto-generation utility allows you to use Postman to auto-generate values for your B2B namespaces and schemas. You must complete your B2B namespaces and schemas first, before creating a Marketo source connection and dataflow.
- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. Create and edit schemas in the UI : Learn how to create and edit schemas in the UI.
- [Identity namespaces](/en/docs/experience-platform/identity/features/namespaces): Identity namespaces are a component of Identity Service that serve as indicators of the context to which an identity relates. A fully qualified identity includes an ID value and a namespace.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Retrieve your custom activity details

The first step to bringing custom activity data from Marketo to Experience Platform is to retrieve the API name and the display name of your custom activity.

Login to your account using the [Marketo](https://app-sjint.marketo.com/#MM0A1) interface. In the left navigation, under Database Management, select **Marketo Custom Activities**.

The interface updates to a display of your custom activities, including information on their respective display names and API names. You can also use the right-rail to select and view other custom activities from your account.

Select **Fields** from the top header to view the fields associated with your custom activity. In this page, you can view the names, API names, descriptions, and data types of the fields in your custom activity. Details regarding individual fields will be used in a later step, when creating a schema.

## Set up field groups for custom activities in the B2B activities schema

In the *Schemas* dashboard of the Experience Platform UI, select **Browse** and then select **B2B Activity** from the list of schemas.

TIP
Use the search bar to expedite your navigation through the list of schemas.
### Create a new field group for custom activity

Next, add a new field group to the B2B Activity schema. This field group should correspond with the custom activity that you want to ingest and should use the custom activity’s display name that you retrieved earlier.

To add a new field group, select **+ Add** beside the *Field groups* panel under *Composition*.

The *Add field groups* window appears. Select **Create new field group** and then provide the same display name for the custom activity that you retrieved in an earlier step and provide an optional description for your new field group. When finished, select **Add field groups**.

Once created, your new field group for custom activity appears in the Field groups catalog.

### Add a new field to your schema structure

Next, add a new field to your schema. This new field must be set to type: object and will contain the individual fields of the custom activity.

To add a new field, select the plus sign (+) beside the schema name. An entry for *Untitled Field | Type* appears. Next, configure properties of your field using the *Field properties* panel. Set the field name to be your custom activity’s API name and set the display name to be your custom activity’s display name. Then, set the type as object and assign the field group to the custom activity field group that you created in the previous step. When finished, select **Apply**.

The new field appears in your schema.

### Add sub-fields to the object field add-sub-fields-to-the-object-field

The last step in preparing your schema is to add individual fields inside the field that you created in the previous step.

## Create a dataflow

With your schema setup complete, you can now proceed to create a dataflow for your custom activity data.

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search bar.

Under the Adobe applications category, select **Marketo Engage**. Then, select **Add data** to create a new Marketo dataflow.

### Select data

Select **Activities** from the list of Marketo datasets and then select **Next**.

### Dataflow detail

Next, [provide information for your dataflow](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/marketo#provide-dataflow-details), including names and descriptions for your dataset and dataflow, the schema that you will be using, and configurations for Profile ingestion, error diagnostics, and partial ingestion.

### Mapping

Mappings for standard activity fields are auto-populated, but custom activity fields must be mapped to their corresponding target fields manually.

To start mapping your custom activity fields, select **New field type** and then select **Add new field**.

Navigate through the source data structure and find the custom activity field that you want to ingest. When finished, select **Select**.

TIP
To avoid confusion and handle duplicate field names, custom activity fields are prefixed with the API name.
To add a target field, select the schema icon and then select the custom activity fields from the target schema.

Repeat the steps to add the rest of your custom activity mapping fields. When finished, select **Next**.

### Review

The *Review* step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source entity, and the amount of columns within that source entity.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Save & ingest** and allow some time for the dataflow to be created.

### Add custom activities to an existing activities dataflow add-to-existing-dataflows

To add custom activity data to an existing dataflow, modify the mappings of an existing activities dataflow with the custom activity data that you want to ingest. This allows you to ingest custom activity into the same existing activities dataset. For more information on how to update the mappings of an existing dataflow, read the guide on [updating dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/update-dataflows).

### Use Query Service to filter activities for custom activities query-service-filter

Once your dataflow is complete, you can use [Query Service](/en/docs/experience-platform/query/home) to filter activities for your custom activity data.

When custom activities are ingested into Experience Platform, the API name of the custom activity automatically becomes its eventType. Use eventType={API_NAME} to filter for custom activity data.

```
SELECT * FROM with_custom_activities_ds_today WHERE eventType='aepCustomActivityDemo1'
```

Use the IN clause to filter multiple custom activities:

```
SELECT * FROM $datasetName WHERE eventType='{API_NAME}'
SELECT * FROM $datasetName WHERE eventType IN ('aepCustomActivityDemo1', 'aepCustomActivityDemo2')
```

The image below shows an example SQL statement in the [Query Editor](/en/docs/experience-platform/query/ui/user-guide) that filters for custom activity data.

## Next steps

By following this tutorial, you have set up an Experience Platform schema for Marketo custom activity data and created a dataflow to bring that data to Experience Platform. For general information on the Marketo source, read the [Marketo source overview](/en/docs/experience-platform/sources/connectors/adobe-applications/marketo/marketo).

recommendation-more-help
