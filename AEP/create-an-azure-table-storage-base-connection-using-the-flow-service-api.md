---
title: "Create an Azure Table Storage base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/ats"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:01.386748+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Azure Table Storage base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The Azure Table Storage connector is in beta. See the
Sources overview
for more information on using beta-labeled connectors.
A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Azure Table Storage using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Azure Table Storage using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with Azure Table Storage, you must provide values for the following connection properties:

Credential
Description
connectionString
The connection string used to connect to an Azure Table Storage instance. The connection string pattern for Azure Table Storage is:
DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY}
.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Azure Table Storage is
ecde33f2-c56f-46cc-bdea-ad151c16cd69
.
For more information about obtaining a connection string, refer to [this Azure Table Storage document](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Azure Table Storage authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Azure Table Storage:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Azure Table Storage connection",
        "description": "Azure Table Storage connection",
        "auth": {
            "specName": "Connection String Based Authentication",
            "params": {
                "connectionString": "DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY}"
            }
        },
        "connectionSpec": {
            "id": "ecde33f2-c56f-46cc-bdea-ad151c16cd69",
            "version": "1.0"
        }
    }'
```

Parameter
Description
auth.params.connectionString
The connection string used to connect to an Azure Table Storage instance. The connection string pattern for Azure Table Storage is:
DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY}
.
connectionSpec.id
The Azure Table Storage connection specification ID:
ecde33f2-c56f-46cc-bdea-ad151c16cd69
.
**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your data in the next tutorial.

```
{
    "id": "82abddb3-d59a-436c-abdd-b3d59a436c21",
    "etag": "\"7d00fde3-0000-0200-0000-5e84d9430000\""
}
```

## Next steps

By following this tutorial, you have created an Azure Table Storage base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
