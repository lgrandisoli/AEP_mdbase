---
title: "Create a GreenPlum base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/greenplum"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:02.560347+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a GreenPlum base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for GreenPlum using the [Flow Service API](https://docs.greenplum.org/6-7/security-guide/topics/Authenticate.html).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to GreenPlum using the Flow Service API.

Credential
Description
connectionString
The connection string used to connect to your GreenPlum instance. The connection string pattern for GreenPlum is
HOST={SERVER};PORT={PORT};DB={DATABASE};UID={USERNAME};PWD={PASSWORD}
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for GreenPlum is
37b6bf40-d318-4655-90be-5cd6f65d334b
.
For more information on acquiring a connection string, refer to [this GreenPlum document](https://docs.greenplum.org/6-7/security-guide/topics/Authenticate.html).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your GreenPlum authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for GreenPlum:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "GreenPlum test connection",
        "description": "A test connection for a GreenPlum source",
        "auth": {
            "specName": "Basic Authentication",
            "params": {
                    "connectionString": "HOST={SERVER};PORT={PORT};DB={DATABASE};UID={USERNAME};PWD={PASSWORD}"
                }
        },
        "connectionSpec": {
            "id": "37b6bf40-d318-4655-90be-5cd6f65d334b",
            "version": "1.0"
        }
    }'
```

Parameter
Description
auth.params.connectionString
The connection string used to connect to a GreenPlum account. The connection string pattern is:
HOST={SERVER};PORT={PORT};DB={DATABASE};UID={USERNAME};PWD={PASSWORD}
.
connectionSpec.id
The GreenPlum connection specification ID:
37b6bf40-d318-4655-90be-5cd6f65d334b
.
**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your data in the next tutorial.

```
{
    "id": "575abae5-c99a-452c-9aba-e5c99ac52c4d",
    "etag": "\"e5012c89-0000-0200-0000-5eaa036b0000\""
}
```

## Next steps

By following this tutorial, you have created a GreenPlum base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
