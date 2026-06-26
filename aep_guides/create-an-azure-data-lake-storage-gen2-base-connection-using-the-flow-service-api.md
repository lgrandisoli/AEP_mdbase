---
title: "Create an Azure Data Lake Storage Gen2 base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/adls-gen2"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:30.017706+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Azure Data Lake Storage Gen2 base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Azure Data Lake Storage Gen2 (hereinafter referred to as “ADLS Gen2”) using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully create an ADLS Gen2 source connection using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect to ADLS Gen2, you must provide values for the following connection properties:

Credential
Description
url
The endpoint for ADLS Gen2. The endpoint pattern is:
https://<accountname>.dfs.core.windows.net
.
servicePrincipalId
The application’s client ID.
servicePrincipalKey
The application’s key.
tenant
The tenant information that contains your application.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for ADLS Gen2 is:
b3ba5556-48be-44b7-8b85-ff2b69b46dc4
.
For more information about these values, refer to [this ADLS Gen2 document](https://docs.microsoft.com/en-us/azure/data-factory/connector-azure-data-lake-storage).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your ADLS Gen2 authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for ADLS Gen2:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "adls-gen2",
        "description": "Connection for adls-gen2",
        "auth": {
            "specName": "Basic Authentication for adls-gen2",
            "params": {
                "url": "{URL}",
                "servicePrincipalId": "{SERVICE_PRINCIPAL_ID}",
                "servicePrincipalKey": "{SERVICE_PRINCIPAL_KEY}",
                "tenant": "{TENANT}"
            }
        },
        "connectionSpec": {
            "id": "b3ba5556-48be-44b7-8b85-ff2b69b46dc4",
            "version": "1.0"
        }
    }'
```

Property
Description
auth.params.url
The URL endpoint for your ADLS Gen2 account.
auth.params.servicePrincipalId
The service principal ID of your ADLS Gen2 account.
auth.params.servicePrincipalKey
The service principal key of your ADLS Gen2 account.
auth.params.tenant
The tenant information of your ADLS Gen2 account.
connectionSpec.id
The ADLS Gen2 connection specification ID:
b3ba5556-48be-44b7-8b85-ff2b69b46dc41
.
**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id). This ID is required in the next step to create a source connection.

```
{
    "id": "7497ad71-6d32-4973-97ad-716d32797304",
    "etag": "\"23005f80-0000-0200-0000-5e1d00a20000\""
}
```

## Next steps

By following this tutorial, you have created an ADLS Gen2 connection using APIs and a unique ID was obtained as part of the response body. You can use this connection ID to [explore cloud storages using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage).

recommendation-more-help
