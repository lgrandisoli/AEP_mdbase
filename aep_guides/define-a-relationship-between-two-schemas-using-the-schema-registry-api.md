---
title: "Define a relationship between two schemas using the Schema Registry API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/relationship-api"
category: "tutorials"
topic: "experience-platform/experience-data-model-xdm-guide"
created_at: "2026-06-26T17:38:40.782733+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Data Model (XDM) Guide

# Define a relationship between two schemas using the Schema Registry API

Last update: May 23, 2026
- Topics:
- [Schemas](#)

CREATED FOR:

- Developer

The ability to understand the relationships between your customers and their interactions with your brand across various channels is an important part of Adobe Experience Platform. Defining these relationships within the structure of your Experience Data Model (XDM) schemas allows you to gain complex insights into your customer data.

While schema relationships can be inferred through the use of the union schema and Real-Time Customer Profile, this only applies to schemas that share the same class. To establish a relationship between two schemas belonging to different classes, a dedicated relationship field must be added to a **source schema**, which indicates the identity of a separate **reference schema**.

NOTE
The Schema Registry API refers to reference schemas as “destination schemas”. These are not to be confused with destination schemas in
Data Prep mapping sets
or schemas for
destination connections
.
This document provides a tutorial for defining a one-to-one relationship between two schemas defined by your organization using the [Schema Registry API](https://www.adobe.io/experience-platform-apis/references/schema-registry/).

## Getting started

This tutorial requires a working understanding of Experience Data Model (XDM) and XDM System. Before beginning this tutorial, please review the following documentation:

- [XDM System in Experience Platform](/en/docs/experience-platform/xdm/home): An overview of XDM and its implementation in Experience Platform. Basics of schema composition : An introduction of the building blocks of XDM schemas.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

Before starting this tutorial, please review the [developer guide](/en/docs/experience-platform/xdm/api/getting-started) for important information that you need to know in order to successfully make calls to the Schema Registry API. This includes your {TENANT_ID}, the concept of “containers”, and the required headers for making requests (with special attention to the Accept header and its possible values).

## Define a source and reference schema define-schemas

It is expected that you have already created the two schemas that will be defined in the relationship. This tutorial creates a relationship between members of an organization’s current loyalty program (defined in a “Loyalty Members” schema) and their favorite hotels (defined in a “Hotels” schema).

Schema relationships are represented by a **source schema** having a field that refers to another field within a **reference schema**. In the steps that follow, “Loyalty Members” will be the source schema, while “Hotels” will act as the reference schema.

IMPORTANT
In order to establish a relationship, both schemas must have defined primary identities and be enabled for Real-Time Customer Profile. See the section on
enabling a schema for use in Profile
in the schema creation tutorial if you require guidance on how to configure your schemas accordingly.
In order to define a relationship between two schemas, you must first acquire the $id values for both schemas. If you know the display names (title) of the schemas, you can find their $id values by making a GET request to the /tenant/schemas endpoint in the Schema Registry API.

**API format**

```
GET /tenant/schemas
```

**Request**

```
curl -X GET \
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/schemas \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Accept: application/vnd.adobe.xed-id+json'
```

NOTE
The Accept header
application/vnd.adobe.xed-id+json
returns only the titles, IDs, and versions of the resulting schemas.
**Response**

A successful response returns a list of schemas defined by your organization, including their name, $id, meta:altId, and version.

```
{
    "results": [
        {
            "title": "Newsletter Subscriptions",
            "$id": "https://ns.adobe.com/{TENANT_ID}/schemas/192a66930afad02408429174c311ae73",
            "meta:altId": "_{TENANT_ID}.schemas.192a66930afad02408429174c311ae73",
            "version": "1.2"
        },
        {
            "title": "Loyalty Members",
            "$id": "https://ns.adobe.com/{TENANT_ID}/schemas/2c66c3a4323128d3701289df4468e8a6",
            "meta:altId": "_{TENANT_ID}.schemas.2c66c3a4323128d3701289df4468e8a6",
            "version": "1.5"
        },
        {
            "title": "Hotels",
            "$id": "https://ns.adobe.com/{TENANT_ID}/schemas/d4ad4b8463a67f6755f2aabbeb9e02c7",
            "meta:altId": "_{TENANT_ID}.schemas.d4ad4b8463a67f6755f2aabbeb9e02c7",
            "version": "1.0"
        }
    ],
    "_page": {
        "orderby": "updated",
        "next": null,
        "count": 3
    },
    "_links": {
        "next": null,
        "global_schemas": {
            "href": "https://platform-stage.adobe.io/data/foundation/schemaregistry/global/schemas"
        }
    }
}
```

Record the $id values of the two schemas you want to define a relationship between. These values will be used in later steps.

## Define a reference field for the source schema

Within the Schema Registry, relationship descriptors work similarly to foreign keys in relational database tables: a field in the source schema acts as a reference to the primary identity field of a reference schema. If your source schema does not have a field for this purpose, you may need to create a schema field group with the new field and add it to the schema. This new field must have a type value of string.

IMPORTANT
The source schema cannot use its primary identity as a reference field.
In this tutorial, the reference schema “Hotels” contains an hotelId field that serves as the schema’s primary identity. However, the source schema “Loyalty Members” does not have a dedicated field to be used as a reference to hotelId, and therefore a custom field group needs to be created in order to add a new field to the schema: favoriteHotel.

NOTE
If your source schema already has a dedicated field that you plan to use as a reference field, you can skip ahead to the step on
creating a reference descriptor
.
### Create a new field group

In order to add a new field to a schema, it must first be defined in a field group. You can create a new field group by making a POST request to the /tenant/fieldgroups endpoint.

**API format**

```
POST /tenant/fieldgroups
```

**Request**

The following request creates a new field group that adds a favoriteHotel field under the _{TENANT_ID} namespace of any schema it is added to.

```
curl -X POST\
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/fieldgroups \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'content-type: application/json' \
  -d '{
        "type": "object",
        "title": "Favorite Hotel",
        "meta:intendedToExtend": ["https://ns.adobe.com/xdm/context/profile"],
        "description": "Favorite hotel field group for the Loyalty Members schema.",
        "definitions": {
            "favoriteHotel": {
              "properties": {
                "_{TENANT_ID}": {
                  "type":"object",
                  "properties": {
                    "favoriteHotel": {
                      "title": "Favorite Hotel",
                      "type": "string",
                      "description": "Favorite hotel for a Loyalty Member."
                    }
                  }
                }
              }
            }
        },
        "allOf": [
            {
              "$ref": "#/definitions/favoriteHotel"
            }
        ]
      }'
```

**Response**

A successful response returns the details of the newly created field group.

```
{
    "$id": "https://ns.adobe.com/{TENANT_ID}/mixins/3387945212ad76ee59b6d2b964afb220",
    "meta:altId": "_{TENANT_ID}.mixins.3387945212ad76ee59b6d2b964afb220",
    "meta:resourceType": "mixins",
    "version": "1.0",
    "type": "object",
    "title": "Favorite Hotel",
    "meta:intendedToExtend": [
        "https://ns.adobe.com/xdm/context/profile"
    ],
    "description": "Favorite hotel field group for the Loyalty Members schema.",
    "definitions": {
        "favoriteHotel": {
            "properties": {
                "_{TENANT_ID}": {
                    "type": "object",
                    "properties": {
                        "favoriteHotel": {
                            "title": "Favorite Hotel",
                            "type": "string",
                            "description": "Favorite hotel for a Loyalty Member.",
                            "meta:xdmType": "string"
                        }
                    },
                    "meta:xdmType": "object"
                }
            },
            "type": "object",
            "meta:xdmType": "object"
        }
    },
    "allOf": [
        {
            "$ref": "#/definitions/favoriteHotel"
        }
    ],
    "meta:xdmType": "object",
    "meta:abstract": true,
    "meta:extensible": true,
    "meta:containerId": "tenant",
    "meta:tenantNamespace": "_{TENANT_ID}",
    "meta:registryMetadata": {
        "eTag": "quM2aMPyb2NkkEiZHNCs/MG34E4=",
        "palm:sandboxName": "prod"
    }
}
```

Property
Description
$id
The read-only, system generated unique identifier of the new field group. Takes the form of a URI.
Record the $id URI of the field group, to be used in the next step of adding the field group to the source schema.

### Add the field group to the source schema

Once you have created a field group, you can add it to the source schema by making a PATCH request to the /tenant/schemas/{SCHEMA_ID} endpoint.

**API format**

```
PATCH /tenant/schemas/{SCHEMA_ID}
```

Parameter
Description
{SCHEMA_ID}
The URL-encoded
$id
URI or
meta:altId
of the source schema.
**Request**

The following request adds the “Favorite Hotel” field group to the “Loyalty Members” schema.

```
curl -X PATCH \
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/schemas/_{TENANT_ID}.schemas.533ca5da28087c44344810891b0f03d9 \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -d '[
    {
      "op": "add",
      "path": "/allOf/-",
      "value":  {
        "$ref": "https://ns.adobe.com/{TENANT_ID}/mixins/3387945212ad76ee59b6d2b964afb220"
      }
    }
  ]'
```

Property
Description
op
The PATCH operation to be performed. This request uses the
add
operation.
path
The path to the schema field where the new resource will be added. When adding field groups to schemas, the value must be “/allOf/-”.
value.$ref
The
$id
of the field group to be added.
**Response**

A successful response returns the details of the updated schema, which now includes the $ref value of the added field group under its allOf array.

```
{
    "$id": "https://ns.adobe.com/{TENANT_ID}/schemas/2c66c3a4323128d3701289df4468e8a6",
    "meta:altId": "_{TENANT_ID}.schemas.2c66c3a4323128d3701289df4468e8a6",
    "meta:resourceType": "schemas",
    "version": "1.1",
    "type": "object",
    "title": "Loyalty Members",
    "description": "",
    "allOf": [
        {
            "$ref": "https://ns.adobe.com/xdm/context/profile"
        },
        {
            "$ref": "https://ns.adobe.com/xdm/context/profile-person-details"
        },
        {
            "$ref": "https://ns.adobe.com/xdm/context/profile-personal-details"
        },
        {
            "$ref": "https://ns.adobe.com/{TENANT_ID}/mixins/ec16dfa484358f80478b75cde8c430d3"
        },
        {
            "$ref": "https://ns.adobe.com/xdm/context/identitymap"
        },
        {
            "$ref": "https://ns.adobe.com/{TENANT_ID}/mixins/3387945212ad76ee59b6d2b964afb220"
        }
    ],
    "meta:containerId": "tenant",
    "meta:class": "https://ns.adobe.com/xdm/context/profile",
    "meta:abstract": false,
    "meta:extensible": false,
    "meta:tenantNamespace": "_{TENANT_ID}",
    "imsOrg": "{ORG_ID}",
    "meta:extends": [
        "https://ns.adobe.com/xdm/context/profile",
        "https://ns.adobe.com/xdm/data/record",
        "https://ns.adobe.com/xdm/context/identitymap",
        "https://ns.adobe.com/xdm/common/extensible",
        "https://ns.adobe.com/xdm/common/auditable",
        "https://ns.adobe.com/xdm/context/profile-person-details",
        "https://ns.adobe.com/xdm/context/profile-personal-details",
        "https://ns.adobe.com/{TENANT_ID}/mixins/ec16dfa484358f80478b75cde8c430d3",
        "https://ns.adobe.com/{TENANT_ID}/mixins/61969bc646b66a6230a7e8840f4a4d33"
    ],
    "meta:xdmType": "object",
    "meta:registryMetadata": {
        "repo:createdDate": 1557525483804,
        "repo:lastModifiedDate": 1566419670915,
        "xdm:createdClientId": "{API_KEY}",
        "xdm:lastModifiedClientId": "{CLIENT_ID}",
        "eTag": "ITNzu8BVTO5pw9wfCtTTpk6U4WY="
    }
}
```

## Create a reference identity descriptor reference-identity

Schema fields must have a reference identity descriptor applied to them if they are being used as a reference to another schema in a relationship. Since the favoriteHotel field in “Loyalty Members” will refer to the hotelId field in “Hotels”, favoriteHotel must be given a reference identity descriptor.

Create a reference descriptor for the source schema by making a POST request to the /tenant/descriptors endpoint.

**API format**

```
POST /tenant/descriptors
```

**Request**

The following request creates a reference descriptor for the favoriteHotel field in the source schema “Loyalty Members”.

```
curl -X POST \
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/descriptors \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
    "@type": "xdm:descriptorReferenceIdentity",
    "xdm:sourceSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/533ca5da28087c44344810891b0f03d9",
    "xdm:sourceVersion": 1,
    "xdm:sourceProperty": "/_{TENANT_ID}/favoriteHotel",
    "xdm:identityNamespace": "Hotel ID"
  }'
```

Parameter
Description
@type
The type of descriptor being defined. For reference descriptors the value must be
xdm:descriptorReferenceIdentity
.
xdm:sourceSchema
The
$id
URL of the source schema.
xdm:sourceVersion
The version number of the source schema.
sourceProperty
The path to the field in the source schema that will be used to refer to the reference schema’s primary identity.
xdm:identityNamespace
The identity namespace of the reference field. This must be the same namespace as the reference schema’s primary identity. See the
identity namespace overview
for more information.
**Response**

A successful response returns the details of the newly created reference descriptor for the source field.

```
{
    "@type": "xdm:descriptorReferenceIdentity",
    "xdm:sourceSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/533ca5da28087c44344810891b0f03d9",
    "xdm:sourceVersion": 1,
    "xdm:sourceProperty": "/_{TENANT_ID}/favoriteHotel",
    "xdm:identityNamespace": "Hotel ID",
    "meta:containerId": "tenant",
    "@id": "53180e9f86eed731f6bf8bf42af4f59d81949ba6"
}
```

## Create a relationship descriptor create-descriptor

Relationship descriptors establish a one-to-one relationship between a source schema and a reference schema. Once you have defined a reference identity descriptor for the appropriate field in the source schema, you can create a new relationship descriptor by making a POST request to the /tenant/descriptors endpoint.

**API format**

```
POST /tenant/descriptors
```

**Request**

The following request creates a new relationship descriptor, with “Loyalty Members” as the source schema and “Hotels” as the reference schema.

```
curl -X POST \
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/descriptors \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
    "@type": "xdm:descriptorOneToOne",
    "xdm:sourceSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/2c66c3a4323128d3701289df4468e8a6",
    "xdm:sourceVersion": 1,
    "xdm:sourceProperty": "/_{TENANT_ID}/favoriteHotel",
    "xdm:destinationSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/d4ad4b8463a67f6755f2aabbeb9e02c7",
    "xdm:destinationVersion": 1,
    "xdm:destinationProperty": "/_{TENANT_ID}/hotelId"
  }'
```

Parameter
Description
@type
The type of descriptor to be created. The
@type
value for relationship descriptors is
xdm:descriptorOneToOne
.
xdm:sourceSchema
The
$id
URL of the source schema.
xdm:sourceVersion
The version number of the source schema.
xdm:sourceProperty
The path to the reference field in the source schema.
xdm:destinationSchema
The
$id
URL of the reference schema.
xdm:destinationVersion
The version number of the reference schema.
xdm:destinationProperty
The path to the primary identity field in the reference schema.
### Response

A successful response returns the details of the newly created relationship descriptor.

```
{
    "@type": "xdm:descriptorOneToOne",
    "xdm:sourceSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/2c66c3a4323128d3701289df4468e8a6",
    "xdm:sourceVersion": 1,
    "xdm:sourceProperty": "/_{TENANT_ID}/favoriteHotel",
    "xdm:destinationSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/d4ad4b8463a67f6755f2aabbeb9e02c7",
    "xdm:destinationVersion": 1,
    "xdm:destinationProperty": "/_{TENANT_ID}/hotelId",
    "meta:containerId": "tenant",
    "@id": "76f6cc7105f4eaab7eb4a5e1cb4804cadc741669"
}
```

## Next steps

By following this tutorial, you have successfully created a one-to-one relationship between two schemas. For more information on working with descriptors using the Schema Registry API, see the [Schema Registry developer guide](/en/docs/experience-platform/xdm/api/descriptors). For steps on how to define schema relationships in the UI, see the tutorial on [defining schema relationships using the Schema Editor](/en/docs/experience-platform/xdm/tutorials/relationship-ui).

recommendation-more-help
