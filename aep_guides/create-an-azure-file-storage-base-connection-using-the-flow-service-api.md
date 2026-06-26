---
title: "Create an Azure File Storage base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/azure-file-storage"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:36.100656+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Azure File Storage base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Azure File Storage using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Azure File Storage using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with Azure File Storage, you must provide values for the following connection properties:

Credential
Description
host
The endpoint of the Azure File Storage instance you are accessing.
userId
The user with sufficient access to the Azure File Storage endpoint.
password
The password for your Azure File Storage instance
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Azure File Storage is:
be5ec48c-5b78-49d5-b8fa-7c89ec4569b8
.
For more information about getting started refer to [this Azure File Storage document](https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-windows).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Azure File Storage authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Azure File Storage:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
        -d '{
        "name": "Azure File Storage connection",
        "description": "An Azure File Storage test connection",
        "auth": {
            "specName": "Basic Authentication",
            "params": {
                    "host": "{HOST}",
                    "userId": "{USER_ID}",
                    "password": "{PASSWORD}"
                }
        },
        "connectionSpec": {
            "id": "be5ec48c-5b78-49d5-b8fa-7c89ec4569b8",
            "version": "1.0"
        }
    }'
```

Property
Description
auth.params.host
The endpoint of the Azure File Storage instance you are accessing…
auth.params.userId
The user with sufficient access to the Azure File Storage endpoint.
auth.params.password
The Azure File Storage access key.
connectionSpec.id
The Azure File Storage connection specification ID:
be5ec48c-5b78-49d5-b8fa-7c89ec4569b8
.
**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id). This ID is required in the next step to create a source connection.

```
{
    "id": "f9377f50-607a-4818-b77f-50607a181860",
    "etag": "\"2f0276fa-0000-0200-0000-5eab3abb0000\""
}
```

## Next steps

By following this tutorial, you have created an Azure File Storage connection using the Flow Service API and have obtained the connection’s unique ID value. You can use this ID in the next tutorial as you learn how to [explore a third-party cloud storage using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage).

recommendation-more-help
