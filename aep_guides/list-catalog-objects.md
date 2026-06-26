---
title: "List Catalog objects"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/catalog/api/list-objects"
category: "reference"
topic: "experience-platform/catalog-and-datasets-guide"
created_at: "2026-06-26T17:38:55.429749+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Catalog and Datasets Guide

# List Catalog objects

Last update: June 18, 2026
- Topics:
- [Catalog](#)

CREATED FOR:

- Developer

You can retrieve a list of all available objects of a specific type through a single API call, with best practice being to include filters that limit the size of the response.

**API format**

```
GET /{OBJECT_TYPE}
GET /{OBJECT_TYPE}?{FILTER}={VALUE}&{FILTER_2}={VALUE}
```

Parameter
Description
{OBJECT_TYPE}
The type of Catalog object to be listed. Valid objects are:

- batches
- dataSets
- dataSetFiles

{FILTER}
A query parameter used to filter the results returned in the response. Multiple parameters are separated by ampersands (
&
). See the guide on
filtering Catalog data
for more information.
**Request**

The sample request below retrieves a list of datasets, with a limit filter reducing the response to five results, and a properties filter that limits the properties displayed for each dataset.

```
curl -X GET \
  'https://platform.adobe.io/data/foundation/catalog/dataSets?limit=5&properties=name,description,files' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns a list of Catalog objects in the form of key-value pairs, filtered by the query parameters provided in the request. For each key-value pair, the key represents a unique identifier for the Catalog object in question, which can then be used in another call to [view that specific object](/en/docs/experience-platform/catalog/api/look-up-object) for more details.

NOTE
If a returned object does not contain one or more of the requested properties indicated by the
properties
query, the response returns only the requested properties that it does include, as shown in
Sample Dataset 3
and
Sample Dataset 4
below.
```
{
    "5ba9452f7de80400007fc52a": {
        "name": "Sample Dataset 1",
        "description": "Description of dataset.",
        "files": "@/dataSetFiles?dataSetId=5ba9452f7de80400007fc52a"
    },
    "5bb276b03a14440000971552": {
        "name": "Sample Dataset 2",
        "description": "Description of dataset.",
        "files": "@/dataSetFiles?dataSetId=5bb276b03a14440000971552"
    },
    "5bceaa4c26c115000039b24b": {
        "name": "Sample Dataset 3"
    },
    "5bda3a4228babc0000126377": {
        "name": "Sample Dataset 4",
        "files": "@/dataSetFiles?dataSetId=5bda3a4228babc0000126377"
    },
    "5bde21511dd27b0000d24e95": {
        "name": "Sample Dataset 5",
        "description": "Description of dataset.",
        "files": "@/dataSetFiles?dataSetId=5bde21511dd27b0000d24e95"
    }
}
```

recommendation-more-help
