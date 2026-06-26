---
title: "Schema Registry API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/xdm/api/overview"
category: "reference"
topic: "experience-platform/experience-data-model-xdm-guide"
created_at: "2026-05-29T16:59:06.914399+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Data Model (XDM) Guide

# Schema Registry API guide

Last update: May 23, 2026
- Topics:
- [Schemas](#)

CREATED FOR:

- Developer

The Schema Registry is used to access the Schema Library within Adobe Experience Platform, providing a user interface and RESTful API from which all available library resources are accessible.

The Schema Registry API provides several endpoints that allow you to programmatically manage all schemas and related Experience Data Model (XDM) resources available to you within Experience Platform. This includes those defined by Adobe, Experience Platform partners, and vendors whose applications you use.

These endpoints are outlined below. Please visit the individual endpoint guides for details and refer to the [getting started guide](/en/docs/experience-platform/xdm/api/getting-started) for important information on required headers, reading sample API calls, and more.

IMPORTANT
XDM uses JSON Schema formatting to describe and validate the structure of ingested customer experience data. Before working with the Schema Registry API, it is strongly recommended that you review the
official JSON Schema documentation
for a better understanding of this underlying technology.
To view all available endpoints and CRUD operations, visit the [Schema Registry API reference](https://www.adobe.io/experience-platform-apis/references/schema-registry/).

## Schemas

XDM schemas represent and validate the structure and format of data ingested into Experience Platform. A schema is composed of a class and zero or more schema field groups. You can create, view, edit, and delete schemas using the /schemas endpoint. To learn how to use this endpoint, see the [schemas endpoint guide](/en/docs/experience-platform/xdm/api/schemas).

For a step-by-step guide on how to manually create a complete schema in the Schema Registry API, including creating and adding field groups and data types, see the [API schema creation tutorial](/en/docs/experience-platform/xdm/tutorials/create-schema-api).

If you are ingesting CSV data, see the section on [CSV to schema conversion](#csv-to-schema).

## Behaviors

Behaviors define the nature of data that a schema describes. Each XDM class must reference a specific behavior, which all schemas that employ that class will inherit. See the [behaviors endpoint guide](/en/docs/experience-platform/xdm/api/behaviors) to learn how to view available behaviors in the API.

## Classes

A class defines the base structure of common properties that all schemas based on that class must contain, and determines which field groups are eligible for use in those schemas. Every class must be associated with an existing behavior. See the [classes endpoint guide](/en/docs/experience-platform/xdm/api/classes) for details on working with classes in the API.

## Field groups

Field groups are reuseable components which define one or more fields that represent a particular concept, such as an individual person, a mailing address, or a web browser environment. Field groups are intended to be included as part of a schema that implements a compatible class, depending on the behavior of data they represent (record or time series). See the [field groups endpoint guide](/en/docs/experience-platform/xdm/api/field-groups) to learn how to work with field groups in the API.

## Data types

Data types are used as reference-type fields in classes or field groups in the same way as basic literal fields, with the key difference being that data types can define multiple sub-fields. While similar to field groups in that they allow for the consistent use of a multi-field structure, data types are more flexible because they can be included anywhere in the schema structure whereas field groups can only be added at the root level. See the [data types endpoint guide](/en/docs/experience-platform/xdm/api/data-types) for more information on working with data types in the API.

NOTE
If a field is defined as a specific data type, you cannot create the same field with a different datatype in another schema. This constraint applies across your organization’s tenant.
## Descriptors

Descriptors are sets of metadata that are assigned to specific fields within a schema, providing various contextual details including how those fields (and the schema itself) are related to other schemas. Each schema can have one or more descriptor entities applied to it, and there are several different descriptor types to serve different purposes. See the [descriptors endpoint guide](/en/docs/experience-platform/xdm/api/descriptors) for more information on working with descriptors in the API, and an overview of the different descriptor types and their use cases.

## Unions

While Experience Platform allows you to compose schemas for particular use cases, it also allows you to compose a “union” of schemas belonging to a specific class. A union schema aggregates the fields of all schemas that share the same class into a single representation. By enabling a schema for use with [Real-Time Customer Profile](/en/docs/experience-platform/profile/home), that schema becomes included in the union for its particular class. As such, union schemas cannot be edited directly, and can only be affected by including or excluding schemas for use in Profile.

To learn how to view unions in the Schema Registry API, see the [unions endpoint guide](/en/docs/experience-platform/xdm/api/unions).

## CSV to schema conversion csv-to-schema

You can automatically generate an XDM schema using a CSV file as a template, allowing you to create templates to bulk-import schema fields and cut down on manual API or UI work.

See the [CSV to schema conversion endpoint guide](/en/docs/experience-platform/xdm/api/export) for more information.

NOTE
You can also us the UI to
map a CSV to a schema using AI-generated recommendations
(currently in beta).
## Export export

The Schema Registry API allows you to transfer and share XDM resources between sandboxes and organizations. For any schema, field group, or data type, you can generate an export payload containing the structure of the resource and any dependent resources. This payload can then be used to import the resource into a destination sandbox and organization.

See the [export endpoint guide](/en/docs/experience-platform/xdm/api/export) for more information on how to create an export payload for an existing XDM resource.

## Import

If you use the [export](#export) or [CSV to schema conversion](/en/docs/experience-platform/xdm/api/import) endpoints to create an export payload, you can send that payload to a target organization and sandbox to import the specified resources.

See the [import endpoint guide](/en/docs/experience-platform/xdm/api/export) for more information on how to generate XDM resources from export payloads.

## Sample data

You can generate sample data for any specified schema within the Schema Library. The response object returned can then be used as a source of data ingestion.

See the [sample data endpoint guide](/en/docs/experience-platform/xdm/api/sample-data) for more information on the use of this endpoint.

## Audit log

The Schema Registry maintains a log of all the changes that have occurred to a resource (class, field group, data type, or schema) between different updates. You can retrieve the log for a particular resource by providing its $id or meta:altId in the path of a GET request to this endpoint.

See the [audit log endpoint guide](/en/docs/experience-platform/xdm/api/audit-log) for more information on the use of this endpoint.

## Next steps

To begin making calls using the Schema Registry API, read the [getting started guide](/en/docs/experience-platform/xdm/api/getting-started) then select one of the endpoint guides to learn how to use specific endpoints.

recommendation-more-help
