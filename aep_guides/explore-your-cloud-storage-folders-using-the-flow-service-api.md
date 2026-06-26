---
title: "Explore your cloud storage folders using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:34:35.030008+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Explore your cloud storage folders using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps on how to explore and preview the structure and contents of your cloud storage using the [Flow Service](https://www.adobe.io/experience-platform-apis/references/flow-service/) API.

NOTE
In order to explore your cloud storage, you must already have a valid base connection ID for a cloud storage source. If you do not have this ID, then see the
sources overview
for a list of cloud storage sources that you can create a base connection with.
## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Explore your cloud storage folders

You can retrieve information on the structure of your cloud storage folders by making a GET request to the Flow Service API while providing the base connection ID of your source.

When performing GET requests to explore your cloud storage, you must include the query parameters that are listed in the table below:

Parameter
Description
objectType
The type of object that you wish to explore. Set this value as either:

- folder: Explore a specific directory
- root: Explore the root directory.

object
This parameter is required only when viewing a specific directory. Its value represents the path of the directory you wish to explore.
**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=root
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=folder&object={PATH}
```

Parameter
Description
{BASE_CONNECTION_ID}
The base connection ID of your cloud storage source.
{PATH}
The path of a directory.
**Request**

```
curl -X GET \
  'http://platform.adobe.io/data/foundation/flowservice/connections/dc3c0646-5e30-47be-a1ce-d162cb8f1f07/explore?objectType=folder&object=root' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns an array of files and folders found within the queried directory. Take note of the path property of the file you wish you upload, as you are required to provide it in the next step to inspect its structure.

```
[
    {
        "type": "file",
        "name": "account.csv",
        "path": "/test-connectors/testFolder-fileIngestion/account.csv",
        "canPreview": true,
        "canFetchSchema": true
    },
    {
        "type": "file",
        "name": "profileData.json",
        "path": "/test-connectors/testFolder-fileIngestion/profileData.json",
        "canPreview": true,
        "canFetchSchema": true
    },
    {
        "type": "file",
        "name": "sampleprofile--3.parquet",
        "path": "/test-connectors/testFolder-fileIngestion/sampleprofile--3.parquet",
        "canPreview": true,
        "canFetchSchema": true
    }
]
```

## Inspect the structure of a file

To inspect the structure of data file from your cloud storage, perform a GET request while providing the file’s path and type as a query parameter.

You can inspect the structure of a data file from your cloud storage source by performing a GET request while providing the file’s path and type. You can also inspect different file types such as CSV, TSV, or compressed JSON and delimited files by specifying their file types as part of the query parameters.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=file&object={FILE_PATH}&fileType={FILE_TYPE}&{QUERY_PARAMS}&preview=true
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=file&object={FILE_PATH}&preview=true&fileType=delimited&columnDelimiter=\t
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=file&object={FILE_PATH}&preview=true&fileType=delimited&compressionType=gzip;
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=FILE&object={FILE_PATH}&preview=true&fileType=delimited&encoding=ISO-8859-1;
```

Parameter
Description
{BASE_CONNECTION_ID}
The connection ID of your cloud storage source connector.
{FILE_PATH}
The path to the file you want to inspect.
{FILE_TYPE}
The type of the file. Supported file types include:

- DELIMITED: Delimiter-separated value. DSV files must be comma-separated.
- JSON: JavaScript Object Notation. JSON files must be XDM compliant
- PARQUET: Apache Parquet. Parquet files must be XDM compliant.

{QUERY_PARAMS}
Optional query parameters that can be used to filter results. See the section on
query parameters
for more information.
**Request**

```
curl -X GET \
    'http://platform.adobe.io/data/foundation/flowservice/connections/{BASE_CONNECTION_ID}/explore?objectType=file&object=/aep-bootcamp/Adobe%20Pets%20Customer%2020190801%20EXP.json&fileType=json&preview=true' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the structure of the queried file including table names and data types.

```
[
    {
        "name": "Id",
        "type": "String"
    },
    {
        "name": "FirstName",
        "type": "String"
    },
    {
        "name": "LastName",
        "type": "String"
    },
    {
        "name": "Email",
        "type": "String"
    },
    {
        "name": "Phone",
        "type": "String"
    }
]
```

## Using query parameters query

The [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/) supports the use of query parameters to preview and inspect different file types.

Parameter
Description
columnDelimiter
The single character value you specified as a column delimiter to inspect CSV or TSV files. If the parameter is unprovided, the value defaults to a comma
(,)
.
compressionType
A required query parameter for previewing a compressed delimited or JSON file. The supported compressed files are:

- bzip2
- gzip
- deflate
- zipDeflate
- tarGzip
- tar

encoding
Defines which encoding type to use when rendering preview. The supported encoding types are:
UTF-8
and
ISO-8859-1
.
Note
: The
encoding
parameter is only available when ingesting delimited CSV files. Other file types will be ingested with the default encoding,
UTF-8
.
## Next steps

By following this tutorial, you have explored your cloud storage system, found the path of the file you wish to bring in to Experience Platform, and viewed its structure. You can use this information in the next tutorial to [collect data from your cloud storage and bring it into Experience Platform](/en/docs/experience-platform/sources/api-tutorials/collect/cloud-storage).

recommendation-more-help
