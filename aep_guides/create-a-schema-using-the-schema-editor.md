---
title: "Create a schema using the Schema Editor"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui"
category: "tutorials"
topic: "experience-platform/experience-data-model-xdm-guide"
created_at: "2026-06-26T17:23:51.296178+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Data Model (XDM) Guide

# Create a schema using the Schema Editor

Last update: June 18, 2026
- Topics:
- [Schemas](#)

CREATED FOR:

- Developer

The Adobe Experience Platform user interface allows you to create and manage Experience Data Model (XDM) schemas in an interactive visual canvas called the Schema Editor. This tutorial covers how to create a schema using the Schema Editor.

For demonstration purposes, the steps in this tutorial involve creating an example schema that describes members of a customer loyalty program. While you can use these steps to create a different schema for your own purposes, it is recommended that you first follow along with creating the example schema to learn the capabilities of the Schema Editor.

NOTE
If you are ingesting CSV data into Experience Platform, you can
map that data to an XDM schema created by AI-generated recommendations
(currently in beta) without having to manually create the schema yourself.
If you prefer to compose a schema using the Schema Registry API, start by reading the
Schema Registry developer guide
before attempting the tutorial on
creating a schema using the API
.
## Getting started

This tutorial requires a working understanding of the various aspects of Adobe Experience Platform involved in schema creation. Before beginning this tutorial, please review the documentation for the following concepts:

- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : An overview of XDM schemas and their building blocks, including classes, schema field groups, data types, and individual fields.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Open the Schemas workspace browse

Use the Schemas workspace in the Experience Platform UI to view and manage the schemas available to your organization. The workspace also includes the Schema Editor, where you create and edit schemas throughout this tutorial.

After logging into Experience Platform, select **Schemas** in the left navigation to open the **Schemas** workspace. The **Browse** tab displays a list of schemas (a representation of the Schema Library) for you to view and customize. The list includes the name, type, class, and behavior (record or time-series) on which the schema is based, as well as the date and time the schema was last modified.

See the guide on [exploring existing XDM resources in the UI](/en/docs/experience-platform/xdm/ui/explore) for more information.

## Create and name a schema create

To begin composing a schema, select **Create schema** in the top-right corner of the **Schemas** workspace.

The Create a schema dialog appears. In this dialog, you can choose to either manually create a schema by adding fields and field groups, or you can upload a CSV file and use ML algorithms to generate a schema. Select a schema creation workflow from the dialog.

### [Beta]{class="badge informative"} Manual or ML-assisted schema creation manual-or-assisted

To learn how you can use a ML algorithm to recommend a schema structure based on an uploaded file, see the [machine learning-assisted schema creation guide](/en/docs/experience-platform/xdm/ui/ml-assisted-schema-creation). This UI guide focusses on the manual creation workflow.

### Choose a base class choose-a-class

The Create schema workflow appears. Next, choose a base class for the schema. You can choose between the core classes of XDM Individual Profile and XDM ExperienceEvent, or Other if these classes do not suit your purposes. The Other classes option allows you to either [create a new class](#create-new-class) or choose from other pre-existing classes.

See the [XDM individual profile](/en/docs/experience-platform/xdm/classes/individual-profile) and [XDM ExperienceEvent](/en/docs/experience-platform/xdm/classes/experienceevent) documentation for more information on these classes. For the purposes of this tutorial, select **XDM Individual Profile** followed by **Next**.

### Name and review name-and-review

After you have selected a class, the Name and review section appears. In this section, you provide a name and description to identify your schema. There are several important considerations to make when deciding on a name for your schema:

- Schema names should be short and descriptive so that the schema can be easily found later.
- Schema names must be unique, meaning it should also be specific enough that it will not be reused in the future. For example, if your organization had separate loyalty programs for different brands, it would be wise to name your schema “Brand A Loyalty Members” to make it easy to distinguish from other loyalty-related schemas you might define later.
- You can also use the schema description to provide any additional contextual information regarding the schema.

This tutorial composes a schema to ingest data related to the members of a loyalty program, and therefore the schema is named “Loyalty Members”.

​The schema’s base structure (provided by the class) is shown in the canvas for you to review and verify your selected class and schema structure.

Enter a human-friendly Schema display name in the text field. Next, enter a suitable description to help identify your schema. When you have reviewed your schema structure and are happy with your settings, select **Finish** to create your schema.

### Compose your schema compose-your-schema

The Schema Editor appears. This is the canvas upon which you will compose your schema. The self-titled schema is automatically created in the **Structure** section of the canvas when you arrive in the editor, along with the standard fields included in the base class that you selected. The assigned class for the schema is also listed under **Class** in **Composition** section.

NOTE
You can update the display name and optional description for the schema from the
Schema properties
sidebar. Once a new name is entered, the canvas automatically updates to reflect the new name of the schema.
NOTE
You can
change the class of a schema
at any point during the initial composition process before the schema has been saved, but this should be done with extreme caution. Field groups are only compatible with certain classes, and therefore changing the class will reset the canvas and any fields you have added.
## Add a field group field-group

You can now begin to add fields to your schema by adding field groups. A field group is a group of one or more fields that are often used together to describe a particular concept. This tutorial uses field groups to describe the members of the loyalty program and capture key information such as name, birthday, phone number, address, and more.

To add a field group, select **Add** in the **Field groups** sub-section.

A new dialog appears, displaying a list of available field groups. Each field group is only intended for use with a specific class, therefore the dialog only lists field groups that are compatible with the class you selected (in this case, the XDM Individual Profile class). If you are using a standard XDM class, the list of field groups will be intelligently sorted based on usage popularity.

You can select one of the filters in the left rail to narrow down the list of standard field groups to specific [industries](/en/docs/experience-platform/xdm/schema/industries/overview) like retail, financial services, and healthcare.

Selecting a field group from the list causes it to appear in the right rail. You can select multiple field groups if desired, adding each one to the list in the right rail before confirming. In addition, an icon appears on the right side of the currently selected field group which allows you to preview the structure of the fields it provides.

When previewing a field group, a detailed description of the field group’s schema is provided in the right rail. You can also navigate through the field group’s fields in the provided canvas. As you select different fields, the right rail updates to show details about the field in question. Select **Back** when you are finished previewing to return to the field group selection dialog.

For this tutorial, select the **Demographic Details** field group, then select **Add field group**.

The schema canvas reappears. The **Field groups** section now lists “Demographic Details” and the **Structure** section includes the fields contributed by the field group. You can select the field group’s name under the **Field groups** section to highlight the specific fields it provides within the canvas.

NOTE
Within the Schema Editor, standard (Adobe-generated) classes and field groups are indicated with the padlock icon (
. The padlock appears in the left rail next to the class or field group name, as well as next to any field in the schema diagram that is a part of a system-generated resource.
This field group contributes several fields under the top-level name person with the data type “Person”. This group of fields describes information about an individual, including name, birth date, and gender.

NOTE
Remember that fields may use scalar types (such as string, integer, array, or date), as well as any data type (a group of fields representing a common concept) defined within the Schema Registry.
Notice that the name field has a data type of “Full name”, meaning it too describes a common concept and contains name-related sub-fields such as first name, last name, courtesy title, and suffix.

Select the different fields within the canvas to reveal any additional fields they contribute to the schema structure.

## Add more field groups field-group-2

You can now repeat the same steps to add another field group. When you view the **Add field group** dialog this time, notice that the “Demographic Details” field group has been greyed out and the checkbox next to it cannot be selected. This prevents you from accidentally duplicating field groups that you have already included in the current schema.

For this tutorial, select the standard field groups **Personal Contact Details** and **Loyalty Details** from the list, then select **Add field groups** to add them to the schema.

The canvas reappears with the added field groups listed under **Field groups** in the **Composition** section, and their composite fields added to the schema structure.

## Define a custom field group define-field-group

The Loyalty Members schema is meant to capture data related to the members of a loyalty program, and the standard Loyalty Details field group that you added to the schema provides most of these, including the program type, points, join date, and more.

However, there may be a scenario where you want to include additional custom fields not covered by standard field groups in order to achieve your use cases. In the case of adding custom loyalty fields, you have two options:

- Create a new custom field group to capture these fields. This is the method that will be covered in this tutorial.
- Extend the standard Loyalty Details field group with custom fields. This causes Loyalty Details to be converted to a custom field group, and the original standard field group will no longer be available. See the Schemas UI guide for more information on [adding custom fields to the structure of standard field groups](/en/docs/experience-platform/xdm/ui/resources/schemas#custom-fields-for-standard-groups).

To create a new field group, select **Add** in the **Field groups** sub-section like before, but this time select **Create New Field group** near the top of the dialog that appears. You are then asked to provide a display name and description for the new field group. For this tutorial, name the new field group “Custom Loyalty Details”, then select **Add field groups**.

NOTE
As with class names, the field group name should be short and simple, describing what the field group will contribute to the schema. These too are unique, so you will not be able to reuse the name and must therefore ensure it is specific enough.
“Custom Loyalty Details” should now appear under **Field groups** on the left side of the canvas, but there are no fields associated with it yet and therefore no new fields appear under **Structure**.

## Add fields to the field group field-group-fields

Now that you have created the “Custom Loyalty Details” field group, it is time to define the fields that the field group will contribute to the schema.

To begin, select the **plus (+)** icon next to the name of the schema in the canvas.

An “Untitled Field” placeholder appears in the canvas, and the right rail updates to reveal configuration options for the field.

In this scenario, the schema needs to have an object-type field that describes the person’s current loyalty tier in detail. Using the controls in the right rail, start creating a loyaltyTier field with type “Object” that will be used to hold your related fields.

Under **Assign to**, you must select a field group to assign the field to. Remember that all schema fields belong to either a class or a field group, and since this schema uses a standard class, your only option is to select a field group. Start typing in the name “Custom Loyalty Details”, then select the field group from the list.

When finished, select **Apply**.

The changes are applied and the newly created loyaltyTier object appears. Since this is a custom field, it is automatically nested within an object namespaced to your organization’s tenant ID, preceded by an underscore (_tenantId in this example).

NOTE
The presence of the tenant ID object indicates that the fields you are adding are contained in your organization’s namespace.
In other words, the fields you are adding are unique to your organization and are going to be saved in the Schema Registry in a specific area accessible only to your organization. Fields you define must always be added to your tenant namespace to prevent collisions with names from other standard classes, field groups, data types, and fields.
Select the **plus (+)** icon next to the loyaltyTier object to start adding sub-fields. A new field placeholder appears and the **Field properties** section is visible on the right side of the canvas.

Each field requires the following information:

- **Field Name:** The name of the field, preferably written in camelCase. No space characters are allowed. This is the name used to reference the field in code and in other downstream applications. Example: loyaltyLevel
- **Display Name:** The name of the field, written in title case. This is the name that will be displayed in the canvas when viewing or editing the schema. Example: Loyalty Level
- **Type:** The data type of the field. This includes basic scalar types and any data types defined in the Schema Registry. Examples: String, Integer, Boolean, Person, Address, Phone number, etc.
- **Description:** An optional description of the field should be included with a maximum of 200 characters.

The first field for the loyaltyTier object will be a string called id, representing the ID of the loyalty member’s current tier. The tier ID will be unique for each loyalty member, since this company sets different loyalty tier point thresholds for each customer based on different factors. Set the new field’s type to “String”, and the **Field properties** section becomes populated with additional options, including **Format**, **Maximum length**, and **Default value**. Use **Format** and length settings when ingestion validation is required. **Default value** records informational schema metadata only and is not automatically applied during ingestion or Data Prep flows. See [type-specific field properties](/en/docs/experience-platform/xdm/ui/fields/overview#type-specific-properties).

Since id will be a randomly generated freeform string, no further constraints are necessary. Select **Apply** to apply your changes.

## Add more fields to the field group field-group-fields-2

Now that you have added the id field, you can add additional fields to capture loyalty tier information such as:

- Current point threshold (integer): The minimum number of loyalty points the member must maintain to remain in the current tier.
- Next tier point threshold (integer): The number of loyalty points the member must accrue to graduate to the next tier.
- Effective date (date-time): The date that the loyalty member joined this tier.

To add each field to the schema, select the **plus (+)** icon next to the loyalty object and fill in the required information.

When complete, the loyaltyTier object will contain fields for id, currentThreshold, nextThreshold, and effectiveDate.

## Add an enum field to the field group enum

When defining fields in the Schema Editor, there are some additional options that you can apply to basic field types in order to provide further constraints on the data the field can contain. The use cases for these constrains are explained in the following table:

Constraint
Description
Required
Indicates that the field is required for data ingestion. Any data uploaded to a dataset based on this schema that does not contain this field will fail upon ingestion.
Array
Indicates that the field contains an array of values, each with the data type specified. For example, using this constraint on a field with a data type of “String” specifies that the field will contain an array of strings.
Enum & Suggested Values
An enum indicates that this field must contain one of the values from an enumerated list of possible values. Alternatively, you can also use this option to just provide a list of suggested values for a string field without constraining the field to those values.
Identity
Indicates that this field is an identity field. More information regarding identity fields is provided
later in this tutorial
.
Relationship
While schema relationships can be inferred through the use of the union schema and Real-Time Customer Profile, this only applies to schemas that share the same class. The Relationship constraint indicates that this field references the primary identity of a schema based on a different class, implying a relationship between the two schemas. See the tutorial on
defining a relationship
for more information.
NOTE
Any required, identity, or relationship fields are listed in their respective sections in the left rail, allowing you to locate these fields easily regardless of the schema’s complexity.
For this tutorial, the loyaltyTier object in the schema requires a new enum field that describes the tier class, where the value can only be one of four possible options. To add this field to the schema, select the **plus (+)** icon beside the loyaltyTier object and fill in the required fields for **Field name** and **Display name**. For **Type**, select “String”.

Additional checkboxes appear for the field after its type has been selected, including checkboxes for **Array**, **Enum & Suggested Values**, **Identity**, and **Relationship**.

Select the **Enum & Suggested Values** checkbox, then select **Enum**. Here you can input the **Value** (in camelCase) and **Display Name** (an optional, reader-friendly name in Title Case) for each acceptable loyalty tier class.

When you have completed all field properties, select **Apply** to add the tierClass field to the loyaltyTier object.

## Convert a multi-field object into a data type datatype

The loyaltyTier object now contains several fields and represents a common data structure that could be useful in other schemas. The Schema Editor allows you to readily apply reusable multi-field objects by converting the structure of those objects into data types.

Data types allow for the consistent use of multi-field structures and provide more flexibility than a field group because they can be used anywhere within a schema. This is done by setting the field’s **Type** value to that of any data type defined in the Schema Registry.

To convert the loyaltyTier object to a data type, select the loyaltyTier field in the canvas, then select **Convert to new data type** on the right side of the editor under **Field properties**.

A notification appears, confirming that the object has been successfully converted. In the canvas you can now see that the loyaltyTier field now has a link icon, and the right rail indicates it has a data type of “Loyalty Tier”.

In a future schema, you could now assign a field as a “Loyalty Tier” type and it would automatically include fields for ID, tier class, point thresholds, and effective date.

NOTE
You can also create and edit custom data types independently from editing schemas. See the guide on
creating and editing data types
for more information.
## Search and filter schema fields

Your schema now contains several field groups in addition to the fields provided by its base class. When working with larger schemas, you can select the checkboxes next to field group names in the left rail to filter the displayed fields to only those provided by the field groups you are interested in.

If you are looking for a specific field in your schema, you can also use the search bar to filter displayed fields by name, regardless of which field group they are provided under.

IMPORTANT
The search function takes any selected field group filters into account when displaying matching fields. If a search query is not displaying the results you expect, you may need to double-check that you are not filtering out any relevant field groups.
## Set a schema field as an identity field identity-field

The standard data structure that schemas provide can be leveraged to identify data belonging to the same individual across multiple sources, allowing for various downstream use cases such as segmentation, reporting, data science analysis, and more. In order to stitch data based on individual identities, key fields must be marked as Identity fields within applicable schemas.

Experience Platform makes it easy to denote an identity field through the use of an **Identity** checkbox in the Schema Editor. However, you must determine which field is the best candidate to use as an identity, based on the nature of your data.

For example, there may be thousands of loyalty program members belonging to the same loyalty level, and several that may share the same physical address. In this scenario, however, on enrollment each member of the loyalty program provides their personal email address. Since personal email addresses are usually managed by one person, the field personalEmail.address (provided by the Personal Contact Details field group) is a good candidate for an identity field.

IMPORTANT
The steps outlined below cover how to add an identity descriptor to an existing schema field. As an alternative to defining identity fields within the structure of the schema itself, you can also use an
identityMap
field to contain identity information instead.
If you plan on using
identityMap
, keep in mind that it will override any primary identity you add to the schema directly. See the section on
identityMap
in the
basics of schema composition guide
for more information.
Select the personalEmail.address field in the canvas, and the **Identity** checkbox appears under **Field properties**. Check the box and the option to set this as the **Primary identity** appears. Select this box as well.

NOTE
Each schema may contain only one primary identity field. Once a schema field has been set as the primary identity, you will receive an error message if you later attempt to set another identity field in the schema as the primary.
Next, you must provide an **Identity namespace** from the list of pre-defined namespaces in the dropdown. Since this field is the customer’s email address, select “Email” from the dropdown. Select **Apply** to confirm the updates to the personalEmail.address field.

NOTE
For a list of standard namespaces and their definitions, see the
Identity Service documentation
.
After applying the change, the icon for personalEmail.address shows a fingerprint symbol, indicating that it is now an identity field. The field is also listed in the left rail under **Identities**.

Now all data ingested into the personalEmail.address field will be used to help identify that individual and stitch together a single view of that customer. To learn more about working with identities in Experience Platform, please review the [Identity Service](/en/docs/experience-platform/identity/home) documentation.

## Enable the schema for use in Real-Time Customer Profile profile

[Real-Time Customer Profile](/en/docs/experience-platform/profile/home) leverages identity data in Experience Platform to provide a holistic view of each individual customer. The service builds robust, 360° profiles of customer attributes as well as timestamped accounts of every interaction customers have had across any system integrated with Experience Platform.

In order for a schema to be enabled for use with Real-Time Customer Profile, it must have a primary identity defined. You will receive an error message if you attempt to enable a schema without first defining a primary identity.

To enable the “Loyalty Members” schema for use in Profile, begin by selecting the schema title in the canvas.

On the right side of the editor, information is shown about the schema including its display name, description, and type. In addition to this information, there is a **Profile** toggle button.

Select **Profile** and a popover appears, asking you to confirm that you wish to enable the schema for Profile.

WARNING
Once a schema has been enabled for Real-Time Customer Profile and saved, it cannot be disabled.
Select **Enable** to confirm your choice. You can select the **Profile** toggle again to disable the schema if you wish, but once the schema has been saved while Profile is enabled, it can no longer be disabled.

## More actions more

NOTE
When working with XDM resources, actions are available from both the inventory table (row menu) and the resource detail view (
More
). To access the full set of actions, including
Delete
,
Copy JSON structure
, and
Add to package
, you must select a custom (tenant-defined) resource. Standard (Adobe-provided) resources have limited actions. For a complete overview of actions, constraints, and permissions, see
Manage schemas, classes, field groups, and data types: actions and deletion
.
Within the Schema Editor you can also conduct quick actions to copy the JSON structure of the schema or delete the schema. Select More at the top of the view to display a drop down with quick actions.

### Delete a schema delete-a-schema

You can delete a schema from the Schema Editor using More actions or from the schema details view in the Browse tab. You cannot delete a schema if:

- The schema is enabled for Profile.
- The schema is enabled for Profile and has associated datasets.
- The schema has associated datasets but is not enabled for Profile.

### Copy JSON structure copy-json-structure

Select **Copy JSON structure** to generate an export payload for any schema in the Schema Library. This action copies the JSON structure to your clipboard. Your exported JSON can then be used to import the schema, and any related resources, into a different sandbox or organization. This makes sharing and reusing schemas between different environments simple and efficient.

## Next steps and additional resources

Now that you have finished composing the schema, you can see the complete schema in the canvas. Select **Save** and the schema will be saved to the Schema Library, making it accessible by the Schema Registry.

Your new schema can now be used to ingest data into Experience Platform. Remember that once the schema has been used to ingest data, only additive changes may be made. See the [basics of schema composition](/en/docs/experience-platform/xdm/schema/composition) for more information on schema versioning.

You can now follow the tutorial on [defining a schema relationship in the UI](/en/docs/experience-platform/xdm/tutorials/relationship-ui) to add a new relationship field to the “Loyalty Members” schema.

The “Loyalty Members” schema is also available to be viewed and managed using the Schema Registry API. To begin working with the API, start by reading the [Schema Registry API developer guide](/en/docs/experience-platform/xdm/api/getting-started).

### Video resources

WARNING
The Experience Platform UI shown in the following videos are out of date. Please refer to the documentation above for the latest UI screenshots and functionality.
The following video shows how to create a simple schema in the Experience Platform UI.

https://video.tv.adobe.com/v/27012?quality=12&learn=on
https://video.tv.adobe.com/vc/27012/eng.json
The following video is intended to reinforce your understanding of working with field groups and classes.

https://video.tv.adobe.com/v/27013?quality=12&learn=on
https://video.tv.adobe.com/vc/27013/eng.json
## Appendix

The following sections provide addition information information regarding the use of the Schema Editor.

### Create a new class create-new-class

Experience Platform provides the flexibility to define a schema based on a class that is unique to your organization. To learn how to create a new class, see the guide on [creating and editing classes in the UI](/en/docs/experience-platform/xdm/ui/resources/classes#create).

### Change the class of a schema change-class

You can change the class of a schema at any point during the initial composition process before the schema has been saved.

WARNING
Reassigning the class for a schema should be done with extreme caution. Field groups are only compatible with certain classes, and therefore changing the class will reset the canvas and any fields you have added.
To learn how to change the class of a schema, see the guide on [managing schemas in the UI](/en/docs/experience-platform/xdm/ui/resources/schemas#change-class).

recommendation-more-help
