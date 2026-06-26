---
title: "Create a Teradata Vantage base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/teradata-vantage"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:15.867398+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Teradata Vantage base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Teradata Vantage using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

The following section provides additional information that you will need to know in order to successfully connect to Teradata Vantage using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with Teradata Vantage, you must provide the following connection properties:

Credential
Description
connectionString
A connection string is a string that provides information about a data source and how you can connect to it. The connection string pattern for Teradata Vantage is
DBCName={SERVER};Uid={USERNAME};Pwd={PASSWORD}
.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Teradata Vantage is:
2fa8af9c-2d1a-43ea-a253-f00a00c74412
For more information about getting started, refer to this [Teradata Vantage document](https://docs.teradata.com/r/Teradata-VantageTM-Advanced-SQL-Engine-Security-Administration/July-2021/Setting-Up-the-Administrative-Infrastructure/Controlling-Access-to-the-Operating-System/Working-with-OS-Level-Security-Options).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Teradata Vantage authentication credentials as part of the request body.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Teradata Vantage:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/connections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "Teradata Vantage base connection",
      "description": "Teradata Vantage base connection",
      "auth": {
          "specName": "ConnectionString,
          "params": {
              "connectionString": "DBCName={SERVER};Uid={USERNAME};Pwd={PASSWORD}"
          }
      },
      "connectionSpec": {
          "id": "2fa8af9c-2d1a-43ea-a253-f00a00c74412",
          "version": "1.0"
      }
  }'
```

Property
Description
auth.params.connectionString
The connection string used to connect to your Teradata Vantage instance. The connection string pattern for Teradata Vantage is
DBCName={SERVER};Uid={USERNAME};Pwd={PASSWORD}
.
connectionSpec.id
The Teradata Vantage connection specification ID:
2fa8af9c-2d1a-43ea-a253-f00a00c74412
.
**Response**

A successful response returns the newly created connection, including its unique connection identifier (id). This ID is required to explore your data in the next tutorial.

```
{
    "id": "2fce94c1-9a93-4971-8e94-c19a93097129",
    "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\""
}
```

By following this tutorial, you have created a Teradata Vantage base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
