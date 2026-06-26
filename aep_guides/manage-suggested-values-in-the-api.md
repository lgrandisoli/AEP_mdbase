---
title: "Manage suggested values in the API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/suggested-values"
category: "tutorials"
topic: "experience-platform/experience-data-model-xdm-guide"
created_at: "2026-06-26T17:38:48.639419+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Data Model (XDM) Guide

# Manage suggested values in the API

Last update: May 23, 2026
- Topics:
- [Schemas](#)

CREATED FOR:

- Developer

For any string field in Experience Data Model (XDM), you can define an **enum** that constrains the values that the field can ingest to a predefined set. If you attempt to ingest data to an enum field and the value does not match any of those defined in its configuration, ingestion will be denied.

In contrast to enums, adding **suggested values** to a string field does not constrain the values that it can ingest. Instead, suggested values affect what predefined values are available in the [Segmentation UI](/en/docs/experience-platform/segmentation/ui/overview) when including the string field as an attribute.

NOTE
There is an approximate five-minute delay for a field’s updated suggested values to be reflected in the Segmentation UI.
This guide covers how to manage suggested values using the [Schema Registry API](https://developer.adobe.com/experience-platform-apis/references/schema-registry/). For steps on how to do this in the Adobe Experience Platform user interface, see the [UI guide on enums and suggested values](/en/docs/experience-platform/xdm/ui/fields/enum).

## Prerequisites

This guide assumes you are familiar with the elements of schema composition in XDM and how to use the Schema Registry API to create and edit XDM resources. Please refer to the following documentation if you require an introduction:

- [Basics of schema composition](/en/docs/experience-platform/xdm/schema/composition)
- [Schema Registry API guide](/en/docs/experience-platform/xdm/api/overview)

It is also strongly recommended that you review the [evolution rules for enums and suggested values](/en/docs/experience-platform/xdm/ui/fields/enum#evolution) if you are updating existing fields. If you are managing suggested values for schemas that participate in a union, see the [rules for merging enums and suggested values](/en/docs/experience-platform/xdm/ui/fields/enum#merging).

## Composition

In the API, the constrained values for an **enum** field are represented by an enum array, while a meta:enum object provides friendly display names for those values.

NOTE
The optional JSON Schema
default
property documents an intended value in the schema definition. Experience Platform does not automatically apply
default
during ingestion or Data Prep flows. See
type-specific field properties in the UI
.
```
"exampleStringField": {
  "type": "string",
  "enum": [
    "value1",
    "value2",
    "value3"
  ],
  "meta:enum": {
    "value1": "Value 1",
    "value2": "Value 2",
    "value3": "Value 3"
  },
  "default": "value1"
}
```

For enum fields, the Schema Registry does not allow meta:enum to be extended beyond the values provided under enum, since attempting to ingest string values outside of those constraints would not pass validation.

Alternatively, you can define a string field that does not contain an enum array and only uses the meta:enum object to denote **suggested values**:

```
"exampleStringField": {
  "type": "string",
  "meta:enum": {
    "value1": "Value 1",
    "value2": "Value 2",
    "value3": "Value 3"
  },
  "default": "value1"
}
```

Since the string does not have an enum array to define constraints, its meta:enum property can be extended to include new values.

## Add suggested values to a standard field add-suggested-standard

To extend the meta:enum of a standard string field, you can create a [friendly name descriptor](/en/docs/experience-platform/xdm/api/descriptors#friendly-name) for the field in question in a particular schema.

NOTE
Suggested values for string fields can only be added at the schema level. In other words, extending the
meta:enum
of a standard field in one schema does not affect other schemas that employ the same standard field.
The following request adds suggested values to the standard eventType field (provided by the [XDM ExperienceEvent class](/en/docs/experience-platform/xdm/classes/experienceevent)) for the schema identified under sourceSchema:

```
curl -X POST \
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/descriptors \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
        "@type": "xdm:alternateDisplayInfo",
        "sourceSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/fbc52b243d04b5d4f41eaa72a8ba58be",
        "sourceProperty": "/eventType",
        "title": {
            "en_us": "Enum Event Type"
        },
        "description": {
            "en_us": "Event type field with soft enum values"
        },
        "meta:enum": {
          "eventA": {
            "en_us": "Event Type A"
          },
          "eventB": {
            "en_us": "Event Type B"
          }
        }
      }'
```

After applying the descriptor, the Schema Registry responds with the following when retrieving the schema (response truncated for space):

```
{
  "$id": "https://ns.adobe.com/{TENANT_ID}/schemas/fbc52b243d04b5d4f41eaa72a8ba58be",
  "title": "Example Schema",
  "properties": {
    "eventType": {
      "type":"string",
      "title": "Enum Event Type",
      "description": "Event type field with soft enum values.",
      "meta:enum": {
        "customEventA": "Custom Event Type A",
        "customEventB": "Custom Event Type B"
      }
    }
  }
}
```

NOTE
If the standard field already contains values under
meta:enum
, the new values from the descriptor do not overwrite the existing fields and are added on instead:
| code language-json |
| --- |
| "standardField": { "type":"string", "title": "Example standard enum field", "description": "Standard field with existing enum values.", "meta:enum": { "standardEventA": "Standard Event Type A", "standardEventB": "Standard Event Type B", "customEventA": "Custom Event Type A", "customEventB": "Custom Event Type B" } } |

## Manage suggested values for a custom field suggested-custom

To manage the meta:enum of a custom field, you can update the field’s parent class, field group, or data type through a PATCH request.

[!WARNING]

In contrast with standard fields, updating the meta:enum of a custom field affects all other schemas that employ that field. If you do not want changes to propagate across schemas, consider creating a new custom resource instead:

- [Create a custom class](/en/docs/experience-platform/xdm/api/classes#create)
- [Create a custom field group](/en/docs/experience-platform/xdm/api/field-groups#create)
- [Create a custom data type](/en/docs/experience-platform/xdm/api/data-types#create)

The following request updates the meta:enum of a “loyalty level” field provided by a custom data type:

```
curl -X PATCH \
  https://platform.adobe.io/data/foundation/schemaregistry/tenant/datatypes/_{TENANT_ID}.datatypes.8779fd45d6e4eb074300023a439862bbba359b60d451627a \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '[
        {
          "op": "replace",
          "path": "/loyaltyLevel/meta:enum",
          "value": {
            "ultra-platinum": "Ultra Platinum",
            "platinum": "Platinum",
            "gold": "Gold",
            "silver": "Silver",
            "bronze": "Bronze"
          }
        }
      ]'
```

After applying the change, the Schema Registry responds with the following when retrieving the schema (response truncated for space):

```
{
  "$id": "https://ns.adobe.com/{TENANT_ID}/schemas/fbc52b243d04b5d4f41eaa72a8ba58be",
  "title": "Example Schema",
  "properties": {
    "loyaltyLevel": {
      "type":"string",
      "title": "Loyalty Level",
      "description": "The loyalty program tier that this customer qualifies for.",
      "meta:enum": {
        "ultra-platinum": "Ultra Platinum",
        "platinum": "Platinum",
        "gold": "Gold",
        "silver": "Silver",
        "bronze": "Bronze"
      }
    }
  }
}
```

## Next steps

This guide covered how to manage suggested values for string fields in the Schema Registry API. See the guide on [defining custom fields in the API](/en/docs/experience-platform/xdm/tutorials/custom-fields-api) for more information on how to create different field types.

recommendation-more-help
