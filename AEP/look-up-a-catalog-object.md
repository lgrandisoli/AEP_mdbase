---
title: "Look up a Catalog object"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/catalog/api/look-up-object"
category: "reference"
topic: "experience-platform/catalog-and-datasets-guide"
created_at: "2026-05-29T17:08:12.579124+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Catalog and Datasets Guide

# Look up a Catalog object

Last update: May 13, 2026
- Topics:
- [Catalog](#)

CREATED FOR:

- Developer

If you know the unique identifier for a specific Catalog object, you can perform a GET request to view that object’s details.

NOTE
When viewing specific objects, it is still best practice to
filter by properties
and return only the properties you are interested in.
**API format**

```
GET /{OBJECT_TYPE}/{OBJECT_ID}
GET /{OBJECT_TYPE}/{OBJECT_ID}?properties={PROPERTY_1},{PROPERTY_2},{PROPERTY_3}
```

Parameter
Description
{OBJECT_TYPE}
The type of Catalog object to be retrieved. Valid objects are:

- batches
- dataSets
- dataSetFiles

{OBJECT_ID}
The identifier of the specific object you want to retrieve.
**Request**

The following request retrieves a dataset by its ID, returning its name, description, tags, and files properties.

```
curl -X GET \
  'https://platform.adobe.io/data/foundation/catalog/dataSets/5ba9452f7de80400007fc52a?properties=name,description,tags,files' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the specified dataset with only the requested properties in the body.

```
{
    "5ba9452f7de80400007fc52a": {
        "name": "Sample Dataset",
        "description": "Sample dataset containing important data.",
        "tags": {
            "adobe/pqs/table": [
                "sample_dataset"
            ]
        },
        "files": "@/dataSetFiles?dataSetId=5ba9452f7de80400007fc52a"
    }
}
```

NOTE
Properties whose values are prefixed with
@
represent interrelated objects. See the appendix section on
viewing interrelated objects
for steps on how to view the details of these objects.
recommendation-more-help
