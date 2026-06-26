---
title: "Manage data usage labels in the UI user-guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-governance/labels/user-guide"
category: "guides"
topic: "experience-platform/data-governance-guide"
created_at: "2026-05-29T16:57:23.466556+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Governance Guide

# Manage data usage labels in the UI user-guide

Last update: May 13, 2026
- Topics:
- [Data Governance](#)

CREATED FOR:

- User
- Developer
- Admin

This user guide covers steps for working with data usage labels within the Experience Platform user interface.

## Manage labels manage-labels

To apply labels to your data, you need the **Manage Usage Labels** permission for use on the default production sandbox called “prod”. To create a custom label, you must also have administrative rights on the product profile. Each organization only has one list of applicable labels. You **cannot** delete labels. Instead you can remove them from the datasets or fields to which they are applied.

See the guide on how to [configure permissions](/en/docs/platform-learn/getting-started-for-data-architects-and-data-engineers/configure-permissions) or the [access control overview](/en/docs/experience-platform/access-control/home) for more information on how to assign a permission. If you do not have access to the Admin Console for your organization, please contact your organization admin.

## Manage labels at the schema level

You can add labels directly to a schema or fields within that schema. Any fields applied at the schema level will propagate to all datasets based on that schema.

NOTE
If your data usage policies were created before you labeled your field, you may encounter a governance policy violation dialog when you apply labels to your new schema. This dialog indicates that applying this label will violate an existing usage policy. Use the data lineage diagram to understand what other configuration changes need to be made before you can add the label to your schema field.
See the
data usage policy violation documentation
for more information on policy violations.
In order to manage data usage labels at the schema level, you must select an existing schema or create a new one. After logging into Adobe Experience Platform, select **Schemas** on the left-navigation to open the **Schemas** workspace. This page lists all created schemas belonging to your organization, along with useful details related to each schema.

The next section provides steps for creating a new schema to apply labels to. If you wish to edit labels for an existing schema, select the schema from the list and skip ahead to [adding data usage labels to the schema](#add-labels).

### Create a new schema

To create a new schema, select **Create schema** in the top-right corner of the **Schemas** workspace. See the guide on [how to create a schema using the Schema Editor](/en/docs/experience-platform/xdm/tutorials/create-schema-ui#create) for complete instructions. Alternatively, you can [create a schema using the Schema Registry API](/en/docs/experience-platform/xdm/tutorials/create-schema-api) if required.

### Add data usage labels to a schema add-labels-to-schema

After creating a new schema, or selecting an existing schema from the list in the Browse tab of the Schemas workspace, select a field from your schema in the Schema Editor. In the Field properties sidebar, select **Apply Access and Data Governance Labels**.

A dialog appears that allows you to apply and manage data usage labels at the schema level and field level. See the XDM tutorial for complete instructions on [how to add or edit data usage labels for XDM schemas](/en/docs/experience-platform/xdm/tutorials/labels#select-schema-field).

### Add data usage labels to a specific dataset add-labels-to-dataset

IMPORTANT
Labels can no longer be applied to fields at the dataset level. This workflow has been deprecated in favour of applying labels at the schema level. Any labels previously applied at the dataset object level will still be supported through the Experience Platform UI until 31st May 2024. To ensure that your labels are consistent across all schemas, any labels previously attached to fields at the dataset level must be migrated to the schema level by you over the coming year. See the documentation for instructions on
how to migrate previously applied labels from the dataset to the schema level
.
Labels can be applied to the entire dataset from the **Data Governance** tab of the **Datasets** workspace. The workspace allows you to manage data usage labels at the dataset level.

To edit data usage labels at the dataset level, start by selecting the pencil icon ( ) in the row of the dataset name.

The **Edit Governance Labels** dialog opens. Within the dialog, check the boxes next to the labels you wish to apply to the dataset. Remember that these labels will be inherited by all fields within the dataset. The **Applied Labels** header updates as you check each box, showing the labels you have chosen. Once you have selected the desired labels, select **Save Changes**.

The **Data Governance** workspace reappears, showing the labels that you have applied at the dataset level in the initial row of the table. You can also see the labels, indicated by individual cards, that are inherited down to each of the fields within the dataset.

### Remove labels from a dataset remove-labels-from-a-dataset

Labels added at the dataset level have an “x” next to their card. This allows you to remove the labels from the entire dataset. Inherited labels beside each field do not have an “x” next to them and appear “greyed out”. These **inherited labels are read-only**, meaning they cannot be removed or edited at the field level.

The **Show Inherited Labels** toggle is on by default, which allows you to see any labels inherited down from the schema to its fields. Switching the toggle off hides any inherited labels within the dataset.

NOTE
Labels that were applied before the dataset labelling feature was deprecated can be removed from the dataset by finding the relevant dataset and selecting the cancel icon on the label.
See the documentation for instructions on
how to migrate previously applied labels from the dataset to the schema level
.
## Manage custom labels manage-custom-labels

You can create your own custom usage labels within the **Policies** workspace in the Experience Platform UI. Select **Policies** in the left-navigation, then select **Labels** to view a list of existing labels. From here, select **Create label**.

The **Create label** dialog appears. From here, provide the following information for the new label:

- **Name**: A unique identifier for the label. This value is used for lookup purposes and should therefore be short and concise.
- **Friendly name**: A friendly display name for the label.
- **Description**: (Optional) A description for the label to provide further context.

When finished, select **Create**.

The dialog closes, and the newly created custom label appears in the list under the **Labels** tab.

The label can now be selected under **Custom Labels** when editing usage labels for datasets and fields, or when creating data usage policies.

## Next steps

Now that you have added data usage labels at the dataset and field level, you can begin to ingest data into Experience Platform. To learn more, start by reading the [data ingestion documentation](/en/docs/experience-platform/ingestion/home).

You can also now define data usage policies based on the labels you have applied. For more information, see the [data usage policies overview](/en/docs/experience-platform/data-governance/policies/overview).

recommendation-more-help
