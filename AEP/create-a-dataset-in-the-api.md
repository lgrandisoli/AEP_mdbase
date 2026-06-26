---
title: "Create a dataset in the API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/catalog/api/create-dataset"
category: "reference"
topic: "experience-platform/catalog-and-datasets-guide"
created_at: "2026-05-29T17:06:24.669761+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Catalog and Datasets Guide

# Create a dataset in the API

Last update: May 13, 2026
- Topics:
- [Catalog](#)

CREATED FOR:

- Developer

In order to create a dataset using the Catalog API, you must know the $id value of the Experience Data Model (XDM) schema on which the dataset will be based. Once you have the schema ID, you can create a dataset by making a POST request to the /datasets endpoint in the Catalog API.

NOTE
This document only covers how to create a dataset object in Catalog. For full steps on how to create, populate, and monitor a dataset, please refer to the following
tutorial
.
**API format**

```
POST /dataSets
```

**Request**

The following request creates a dataset that references a previously defined schema.

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/catalog/dataSets?requestDataSource=true' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -d '{
    "name":"LoyaltyMembersDataset",
    "schemaRef": {
        "id": "https://ns.adobe.com/{TENANT_ID}/schemas/719c4e19184402c27595e65b931a142b",
        "contentType": "application/vnd.adobe.xed+json;version=1"
    }
}'
```

Property
Description
name
The name of the dataset to be created.
schemaRef.id
The URI
$id
value for the XDM schema the dataset will be based on.
schemaRef.contentType
Indicates the format and version of the schema. See the section on
schema versioning
in the XDM API guide for more information.
NOTE
This example uses the
Apache Parquet
file format for its
containerFormat
property. An example that uses the JSON file format can be found in the
batch ingestion developer guide
.
**Response**

A successful response returns HTTP Status 201 (Created) and a response object that consists of an array containing the ID of the newly created dataset in the format "@/datasets/{DATASET_ID}". The dataset ID is a read-only, system-generated string that is used to reference the dataset in API calls.

```
[
    "@/dataSets/5c8c3c555033b814b69f947f"
]
```

recommendation-more-help
