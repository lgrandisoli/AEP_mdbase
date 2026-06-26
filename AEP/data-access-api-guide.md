---
title: "Data Access API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-access/api"
category: "reference"
topic: "experience-platform/data-access-guide"
created_at: "2026-05-29T16:59:20.712619+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Access Guide

# Data Access API guide

Last update: May 13, 2026
- Topics:
- [Data Access](#)

CREATED FOR:

- Developer

IMPORTANT
The Data Access API is now
deprecated
. You are advised to use Destinations for exporting data from Adobe Experience Platform. For more information, please refer to the
dataset export destinations documentation
.
The Data Access API supports Adobe Experience Platform by providing users with a RESTful interface focused on the discoverability and accessibility of ingested datasets within Experience Platform.

## API specification reference

Refer to the [Data Access OpenAPI reference documentation](https://developer.adobe.com/experience-platform-apis/references/data-access/) to view a standardized, machine-readable format for easier integration, testing, and exploration.

## Terminology terminology

The table provides a description of some terms commonly used throughout this document.

Term
Description
Dataset
A collection of data that includes a schema and fields.
Batch
A set of data collected over a period of time and processed together as a single unit.
## Retrieve list of files within a batch retrieve-list-of-files-in-a-batch

To retrieve a list of files belonging to a particular batch, use the batch identifier (batchID) with the Data Access API.

**API format**

```
GET /batches/{BATCH_ID}/files
```

Property
Description
{BATCH_ID}
The ID of the specified batch.
**Request**

```
curl -X GET https://platform.adobe.io/data/foundation/export/batches/{BATCH_ID}/files \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

```
{
  "data": [
    {
      "dataSetFileId": "{FILE_ID_1}",
      "dataSetViewId": "string",
      "version": "1.0.0",
      "created": "string",
      "updated": "string",
      "isValid": true,
      "_links": {
        "self": {
          "href": "https://platform.adobe.io/data/foundation/export/files/{FILE_ID_1}"
        }
      }
    },
    {
      "dataSetFileId": "{FILE_ID_2}",
      "dataSetViewId": "string",
      "version": "1.0.0",
      "created": "string",
      "updated": "string",
      "isValid": true,
      "_links": {
        "self": {
          "href": "https://platform.adobe.io/data/foundation/export/files/{FILE_ID_2}"
        }
      }
    },
  ],
  "_page": {
    "limit": 100,
    "count": 1
  }
}
```

The "data" array contains a list of all files within the specified batch. Each file returned has its own unique ID ({FILE_ID}) contained within the "dataSetFileId" field. You can use this unique ID to access or download the file.

Property
Description
data.dataSetFileId
The file ID for each file in the specified batch.
data._links.self.href
The url to access the file.
## Access and download files within a batch

To access specific details of a file, use a file identifier ({FILE_ID}) with the Data Access API, including its name, size in bytes, and a link to download.

The response contains a data array. Depending on whether the file pointed to by the ID is an individual file or a directory, the data array returned may contain a single entry or a list of files belonging to that directory. Each file element includes the details of the file.

**API format**

```
GET /files/{FILE_ID}
```

Property
Description
{FILE_ID}
Equal to the
"dataSetFileId"
, the ID of the file to be accessed.
**Request**

```
curl -X GET https://platform.adobe.io/data/foundation/export/files/{FILE_ID} \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Single file response**

```
{
  "data": [
    {
      "name": "{FILE_NAME}",
      "length": "{LENGTH}",
      "_links": {
        "self": {
          "href": "https://platform.adobe.io/data/foundation/export/files/{FILE_ID}?path={FILE_NAME}"
        }
      }
    }
  ],
  "_page": {
    "limit": 100,
    "count": 1
  }
}
```

Property
Description
data.name
The name of the file (for example,
profiles.parquet
).
data.length
The size of the file (in bytes).
data._links.self.href
The URL to download the file.
**Directory response**

```
{
  "data": [
    {
      "dataSetFileId": "{FILE_ID_1}",
      "dataSetViewId": "string",
      "version": "1.0.0",
      "created": "string",
      "updated": "string",
      "isValid": true,
      "_links": {
        "self": {
          "href": "https://platform.adobe.io/data/foundation/export/files/{FILE_ID_1}"
        }
      }
    },
    {
      "dataSetFileId": "{FILE_ID_2}",
      "dataSetViewId": "string",
      "version": "1.0.0",
      "created": "string",
      "updated": "string",
      "isValid": true,
      "_links": {
        "self": {
          "href": "https://platform.adobe.io/data/foundation/export/files/{FILE_ID_2}"
        }
      }
    }
  ],
  "_page": {
    "limit": 100,
    "count": 2
  }
}
```

When a directory is returned, it contains an array of all files within the directory.

Property
Description
data.name
The name of the file (for example,
profiles.parquet
).
data._links.self.href
The URL to download the file.
## Access the contents of a file access-file-contents

You can also use the Data Access API to access the contents of a file. You can then download the contents to an external source.

**API format**

```
GET /files/{dataSetFileId}?path={FILE_NAME}
```

Property
Description
{FILE_NAME}
The name of the file you are trying to access.
**Request**

```
curl -X GET https://platform.adobe.io/data/foundation/export/files/{FILE_ID}?path={FILE_NAME} \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

Property
Description
{FILE_ID}
The ID of the file within a dataset.
{FILE_NAME}
The full name of the file (for example,
profiles.parquet
).
**Response**

Contents of the file

## Additional code samples

For additional samples, refer to the [data access tutorial](/en/docs/experience-platform/data-access/tutorials/dataset-data).

## Subscribe to data ingestion events subscribe-to-data-ingestion-events

You can subscribe to specific high-value events through the [Adobe Developer Console](https://developer.adobe.com/console/). For instance, you can subscribe to data ingestion events to be notified of potential delays and failures. See the tutorial on [subscribing to Adobe event notifications](/en/docs/experience-platform/observability/alerts/subscribe) for more information.

recommendation-more-help
