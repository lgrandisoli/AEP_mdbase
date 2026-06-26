---
title: "Manage data usage labels for a schema"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/labels"
category: "tutorials"
topic: "experience-platform/experience-data-model-xdm-guide"
created_at: "2026-06-26T17:27:10.171103+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Data Model (XDM) Guide

# Manage data usage labels for a schema

Last update: May 23, 2026
- Topics:
- [Schemas](#)

CREATED FOR:

- Developer

All data that is brought into Adobe Experience Platform is constrained by Experience Data Model (XDM) schemas. This data may be subject to usage restrictions defined by your organization or by legal regulations. To account for this, the Experience Platform allows you to restrict the usage of certain datasets and fields through the use of [data usage labels](/en/docs/experience-platform/data-governance/labels/overview).

A label applied to a schema field indicates the usage policies that apply to the data contained in that specific field.

Labels can be applied to individual schemas, and fields within those schemas. When labels are applied directly to a schema, those labels are propagated to all existing and future datasets that are based on that schema.

In addition, any field label that you add in one schema propagates to all other schemas that employ the same field from a shared class or field group. This helps to ensure that usage rules for similar fields are consistent across your entire data model.

This tutorial covers the steps for adding labels to a schema using the Schema Editor in the Experience Platform UI.

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Experience Data Model (XDM) System](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. Schema Editor : Learn how to create and manage schemas and other resources in the Experience Platform UI.
- [Adobe Experience Platform Data Governance](/en/docs/experience-platform/data-governance/home): Provides the infrastructure for enforcing data usage restrictions on Experience Platform operations, using policies that define which marketing actions can (or cannot) be performed on labeled data.

## Select a schema or field to add labels to select-schema-field

To start adding labels, you must first [select an existing schema to edit](/en/docs/experience-platform/xdm/ui/resources/schemas#edit) or [create a new schema](/en/docs/experience-platform/xdm/ui/resources/schemas#create) to view its structure in the Schema Editor.

To edit the labels for an individual field, you can select the field in the canvas and then select **Manage access** in the right rail.

IMPORTANT
A maximum of 300 labels can be applied to any schema.
You can also select the **Labels** tab, choose the desired field from the list, and select **Apply Access and Data Governance Labels** in the right rail.

To edit the labels for the entire schema, in the **Labels** tab, select the checkbox under the filter icon. This selects every available field in the schema. Next, select **Apply Access and Data Governance Labels** in the right rail.

NOTE
A disclaimer message appears when you first attempt to edit the labels for a schema or field, explaining how label usage affects downstream operations depending on your organization’s policies. Select
Proceed
to continue editing.
## Edit the labels for the schema or field edit-labels

A dialog appears that allows you to edit the labels for the selected field. If you selected an individual object-type field, the right rail lists the sub-fields that the applied labels will propagate to.

NOTE
If you are editing fields for the whole schema, the right rail does not list the applicable fields and displays the schema name instead.
Use the displayed list to select the labels you want to add to the schema or field. As labels are chosen, the **Applied labels** section updates to show the labels that have been selected so far.

To filter the displayed labels by type, select the desired category in the left rail. To create a new custom label, select **Create label**.

Once you are satisfied with your chosen labels, select **Save** to apply them to the field or schema.

The **Labels** tab reappears, showing the applied labels for the schema.

## Next steps

This guide covered how to manage data usage labels for schemas and fields. For information on managing data usage labels, including how to add them to specific datasets rather than at the schema level, see the [data usage labels UI guide](/en/docs/experience-platform/data-governance/labels/user-guide).

recommendation-more-help
