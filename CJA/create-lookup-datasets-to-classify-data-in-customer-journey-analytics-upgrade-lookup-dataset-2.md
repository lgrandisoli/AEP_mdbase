---
title: "Create lookup datasets to classify data in Customer Journey Analytics upgrade-lookup-dataset"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-datasets/cja-upgrade-dataset-lookup"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:51.191290+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create lookup datasets to classify data in Customer Journey Analytics upgrade-lookup-dataset

Last update: June 5, 2026
- Topics:
- [Data management](#)
- [Analysis Workspace](#)
- [Administration](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

Similar to classifications data in Adobe Analytics, lookup datasets are the method for classifying data in Customer Journey Analytics.

When using the Analytics source connector, some standard lookup datasets are automatically applied at report time. For more information, see [Add standard lookups to your datasets](/en/docs/analytics-platform/using/cja-connections/standard-lookups).

In order to classify data in Customer Journey Analytics when using the Experience Platform Web SDK, you need to create a custom schema and a lookup dataset for each dimension that contains data that you want to classify.

## Create a custom schema to use with the lookup dataset

Create a new custom schema for each dimension that contains data that you want to classify in Customer Journey Analytics. When you create the lookup dataset in a later step, it will reference this schema.

Repeat this process for each dimension that contains data that you want to classify.

To create a schema for use with a lookup dataset in Customer Journey Analytics:

- In Adobe Experience Platform, select Schemas in the Data Management section in the left rail.
- Select Create schema .
- Select Manual . This allows you to manually add fields and field groups to your schema. Choose Select to proceed to the next page of the creation wizard.
- On the Schema details page, select Other , then select Custom .
- Select Create class . add screenshot
- In the Create class dialog box, specify a name and description for the schema, select Record , then select Create .
- Continue with Create a lookup dataset .

## Create a lookup dataset

After you [create a custom schema](#create-a-custom-schema-to-use-with-the-lookup-dataset) to use for a lookup dataset, you need to create the lookup dataset and map it to your schema.

Repeat this process for each dimension that contains data that you want to classify.

To create a lookup dataset for use with a schema in Customer Journey Analytics:

NOTE
The following process uses a CSV file to create the dataset. You could also use any other method available for importing data into Experience Platform, such as setting up a datastream.
- In Adobe Experience Platform, select Workflows in the left rail.
- Select Map CSV to XDM schema , then select Launch .
- In the Dataset details section, select New dataset .
- Specify a name and description for your dataset.
- In the Schema field, select the schema that you created for lookup datasets, as described in Create a schema for lookup datasets .
- Select Next .
- On the Map CSV to XDM schema page , in the Upload files section, select Choose files , then browse your file system for the file that contains the classification information for the dimension for which you want to apply classification data. For example, this might be a spreadsheet that lists the field IDs and corresponding field names.
- Select Next
- After the file uploads, review the mappings to make sure they are accurate. The columns of the CSV file are listed under Source Data and their corresponding XDM schema fields are listed under Target Field . Platform automatically provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. For more information about the mapping process, see Map a CSV file to an existing XDM schema in the Experience Platform documentation.
- Select Finish .
- Continue with Add the lookup dataset to your connection in Customer Journey Analytics .

## Add the lookup dataset to your connection in Customer Journey Analytics

After you [create a custom schema](#create-a-custom-schema-to-use-with-the-lookup-dataset) and you [create a lookup dataset](#create-a-lookup-dataset), you need to add the lookup dataset to your connection in Customer Journey Analytics.

Repeat this process for each dimension that contains data that you want to classify.

To add the lookup dataset to your connection in Customer Journey Analytics:

- In Customer Journey Analytics, select Connections , optionally from Data management , in the top menu.
- Select next to the connection where you want to add the lookup dataset, then select Edit . add screenshot
- Select Add datasets .
- In the Add datasets dialog box, select the lookup dataset that you created, then select Next .
- In the Person ID field, select a person ID from the available identities defined in the your dataset schema that you configured in Experience Platform.
- Select Add datasets , then select Save . is there a step right in between here where you select the dataset
- Using the Key field and the Matching key field, create a correlation between the field in your lookup dataset with that in your event or summary dataset.
- Repeat this process until all lookup datasets are added to your connection in Customer Journey Analytics.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
