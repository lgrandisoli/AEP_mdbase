---
title: "Define a one-to-one relationship between two schemas using the Schema Editor relationship-ui"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/relationship-ui"
category: "tutorials"
topic: "experience-platform/experience-data-model-xdm-guide"
created_at: "2026-05-29T16:57:15.202198+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Data Model (XDM) Guide

# Define a one-to-one relationship between two schemas using the Schema Editor relationship-ui

Last update: May 23, 2026
- Topics:
- [Schemas](#)

CREATED FOR:

- Developer

The ability to understand the relationships between your customers and their interactions with your brand across various channels is an important part of Adobe Experience Platform. Defining these relationships within the structure of your Experience Data Model (XDM) schemas allows you to gain complex insights into your customer data.

While schema relationships can be inferred through the use of the union schema and Real-Time Customer Profile, this only applies to schemas that share the same class. To establish a relationship between two schemas belonging to different classes, a dedicated relationship field must be added to a source schema, which references the identity of the other related schema.

NOTE
If both the source and destination schemas belong to the same class, a dedicated relationship field should
not
be used. In this case, use the union schema UI to see the relationship. Instructions on how to do this can be found in the
view relationships
section of the union schema UI guide.
This document provides a tutorial for defining a relationship between two schemas using the Schema Editor in the Experience Platform user interface. For steps on defining schema relationships using the API, see the tutorial on [defining a relationship using the Schema Registry API](/en/docs/experience-platform/xdm/tutorials/relationship-api).

NOTE
For steps on how to create a many-to-one relationship in Adobe Real-Time Customer Data Platform B2B Edition, see the guide on
creating B2B relationships
.
## Getting started

This tutorial requires a working understanding of XDM System and the Schema Editor in the Experience Platform UI. Before beginning this tutorial, please review the following documentation:

- [XDM System in Experience Platform](/en/docs/experience-platform/xdm/home): An overview of XDM and its implementation in Experience Platform.
- [Basics of schema composition](/en/docs/experience-platform/xdm/schema/composition): An introduction of the building blocks of XDM schemas.
- [Create a schema using the Schema Editor](/en/docs/experience-platform/xdm/tutorials/create-schema-ui): A tutorial covering the basics of working with the Schema Editor.

## Define a source and reference schema

It is expected that you have already created the two schemas that will be defined in the relationship. For demonstration purposes, this tutorial creates a relationship between members of an organization’s loyalty program (defined in a “Loyalty Members” schema) and their favorite hotel (defined in a “Hotels” schema).

IMPORTANT
In order to establish a relationship, both schemas must have defined primary identities and be enabled for Real-Time Customer Profile. See the section on
enabling a schema for use in Profile
in the schema creation tutorial if you require guidance on how to configure your schemas accordingly.
Schema relationships are represented by a dedicated field within a **source schema** that points to another field within a **reference schema**. In the steps that follow, “Loyalty Members” will be the source schema, while “Hotels” will act as the reference schema.

The following sections describe the structure of each schema used in this tutorial before a relationship has been defined.

### Loyalty Members schema

The source schema “Loyalty Members” is based on the XDM Individual Profile class, containing field that describe members of a loyalty program. One of these fields, personalEmail.addess, serves as the primary identity for the schema under the Email namespace. As seen under **Schema Properties**, this schema has been enabled for use in Real-Time Customer Profile.

### Hotels schema

The reference schema “Hotels” is based on a custom “Hotels” class, and contains fields that describe a hotel. In order to participate in a relationship, the reference schema must also have a primary identity defined and be enabled for Profile. In this case, _tenantId.hotelIdacts as the primary identity for the schema, using a custom “Hotel ID” identity namespace.

NOTE
To learn how to create custom identity namespaces, refer to the
Identity Service documentation
.
## Create a relationship field group

NOTE
This step is only required if your source schema does not have a dedicated string-type field to be used as a pointer to the reference schema’s primary identity. If this field is already defined in your source schema, skip to the next step of
defining a relationship field
.
In order to define a relationship between two schemas, the source schema must have a dedicated field that will indicate the reference schema’s primary identity. You can add this field to the source schema by creating a new schema field group or extending an existing one.

In the case of the Loyalty Members schema, a new preferredHotel field will be added to indicate the loyalty member’s preferred hotel for company visits. Start by selecting the plus icon (**+**) next to the source schema’s name.

A new field placeholder appears in the canvas. Under **Field properties**, provide a field name and display name for the field, and set its type to “String”. Under **Assign to**, select an existing field group to extend, or type in a unique name to create a new field group. In this case, a new “Preferred Hotel” field group is created.

When finished, select **Apply**.

The updated preferredHotel field appears in the canvas, located under a _tenantId object since it is a custom field. Select **Save** to finalize your changes to the schema.

## Define a relationship field for the source schema relationship-field

Once your source schema has a dedicated reference field defined, you can designate it as a relationship field.

NOTE
Relationships can only be supported on string or string array fields.
Select the preferredHotel field in the canvas, then select **Add relationship** in the **Field properties** sidebar.

The Add relationship dialog appears. From this dialog you can set required parameters for configuring a relationship field. For Real-Time CDP B2C users, you can **only** set a one-to-one relationship between the source and reference schema.

NOTE
If you have access to Real-Time CDP B2B Edition, you can use the canvas’s right-rail controls to define a relationship field, as well as build a many-to-one relationship using the
same dialog
.
Use the dropdown for **Reference schema** and select the reference schema for the relationship (“Hotels” in this example).

NOTE
Only schemas that contain a primary identity are included in the reference schema dropdown menu. This safeguard prevents you from accidentally creating a relationship with a schema that isn’t properly configured yet.
The reference schema’s identity namespace (in this case, “Hotel ID”) is automatically populated under **Reference identity namespace**. Select **Apply** when finished.

The preferredHotel field is now highlighted as a relationship in the canvas, displaying the name of the reference schema. Select **Save** to save your changes and complete the workflow.

### Edit an existing relationship field edit-relationship

To change the reference schema, select a field with an existing relationship, then select **Edit relationship** in the **Field properties** sidebar.

The Edit relationship dialog appears. From here, you can follow the process outlined in [defining a relationship field](#relationship-field) or delete the relationship. Select **Delete relationship** to remove the relationship to the reference schema.

## Filter and search for relationships filter-and-search

You can filter and search for specific relationships within your schemas from the Relationships tab of the Schemas workspace. You can use this view to quickly locate and manage your relationships. Read the document on [exploring schema resources](/en/docs/experience-platform/xdm/ui/explore#lookup) for detailed instructions on the filtering options.

## Next steps

By following this tutorial, you have successfully created a one-to-one relationship between two schemas using the Schema Editor. For steps on how to define relationships using the API, see the tutorial on [defining a relationship using the Schema Registry API](/en/docs/experience-platform/xdm/tutorials/relationship-api).

recommendation-more-help
