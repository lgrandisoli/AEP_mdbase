---
title: "Connect Azure Synapse Analytics to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/synapse-analytics"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:17.790189+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Connect Azure Synapse Analytics to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Azure Synapse Analytics source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this guide to learn how to connect your Azure Synapse Analytics account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Azure Synapse Analytics using the Flow Service API.

### Gather required credentials

Read the [Azure Synapse Analytics overview](/en/docs/experience-platform/sources/connectors/databases/synapse-analytics#prerequisites) for information on authentication.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Connect Azure Synapse Analytics to Experience Platform

Read the following to learn how to create a base connection and connection your Azure Synapse Analytics account to Experience Platform.

### Create a base connection

A **base connection** stores key information that links your source system to Adobe Experience Platform. This includes:

- Your source’s authentication credentials
- The current status of the connection
- A unique **base connection ID**

The **base connection ID** allows you to browse and explore files from your source, helping you identify which items to ingest, along with their data types and formats.

To create a base connection ID, send a POST request to the /connections endpoint, including your Azure Synapse Analytics authentication credentials in the request parameters.

**API format**

```
POST /connections
```

Connection String Based Authentication
**Request**

The following request creates a base connection for Azure Synapse Analytics using connection string based authentication.

| accordion |
| --- |
| View example request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Connection for Azure Synapse Analytics", "description": "Connection for Azure Synapse Analytics", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server=tcp:{SERVER_NAME}.database.windows.net,1433;Database={DATABASE};User ID={USERNAME}@{SERVER_NAME};Password={PASSWORD};Trusted_Connection=False;Encrypt=True;Connection Timeout=30" } }, "connectionSpec": { "id": "a49bcc7d-8038-43af-b1e4-5a7a089a7d79", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 Parameter Description auth.params.connectionString The connection string used to connect to Azure Synapse Analytics. The Azure Synapse Analytics connection string pattern is Server=tcp:{SERVER_NAME}.database.windows.net,1433;Database={DATABASE};User ID={USERNAME}@{SERVER_NAME};Password={PASSWORD};Trusted_Connection=False;Encrypt=True;Connection Timeout=30 . connectionSpec.id The Azure Synapse Analytics connection specification ID is: a49bcc7d-8038-43af-b1e4-5a7a089a7d79 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Connection for Azure Synapse Analytics", "description": "Connection for Azure Synapse Analytics", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server=tcp:{SERVER_NAME}.database.windows.net,1433;Database={DATABASE};User ID={USERNAME}@{SERVER_NAME};Password={PASSWORD};Trusted_Connection=False;Encrypt=True;Connection Timeout=30" } }, "connectionSpec": { "id": "a49bcc7d-8038-43af-b1e4-5a7a089a7d79", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 |  | Parameter | Description | auth.params.connectionString | The connection string used to connect to Azure Synapse Analytics. The Azure Synapse Analytics connection string pattern is Server=tcp:{SERVER_NAME}.database.windows.net,1433;Database={DATABASE};User ID={USERNAME}@{SERVER_NAME};Password={PASSWORD};Trusted_Connection=False;Encrypt=True;Connection Timeout=30. | connectionSpec.id | The Azure Synapse Analytics connection specification ID is: a49bcc7d-8038-43af-b1e4-5a7a089a7d79. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Connection for Azure Synapse Analytics", "description": "Connection for Azure Synapse Analytics", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server=tcp:{SERVER_NAME}.database.windows.net,1433;Database={DATABASE};User ID={USERNAME}@{SERVER_NAME};Password={PASSWORD};Trusted_Connection=False;Encrypt=True;Connection Timeout=30" } }, "connectionSpec": { "id": "a49bcc7d-8038-43af-b1e4-5a7a089a7d79", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 |  |
| Parameter | Description |
| auth.params.connectionString | The connection string used to connect to Azure Synapse Analytics. The Azure Synapse Analytics connection string pattern is Server=tcp:{SERVER_NAME}.database.windows.net,1433;Database={DATABASE};User ID={USERNAME}@{SERVER_NAME};Password={PASSWORD};Trusted_Connection=False;Encrypt=True;Connection Timeout=30. |
| connectionSpec.id | The Azure Synapse Analytics connection specification ID is: a49bcc7d-8038-43af-b1e4-5a7a089a7d79. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| View example response |
| code language-json { "id": "6bc13a3b-3546-455f-813a-3b3546a55fb1", "etag": "\"3500866c-0000-0200-0000-5e83afa30000\"" } | code language-json | { "id": "6bc13a3b-3546-455f-813a-3b3546a55fb1", "etag": "\"3500866c-0000-0200-0000-5e83afa30000\"" } |
| code language-json |
| { "id": "6bc13a3b-3546-455f-813a-3b3546a55fb1", "etag": "\"3500866c-0000-0200-0000-5e83afa30000\"" } |

Service Principal Key Based Authentication
The following request creates a base connection for Azure Synapse Analytics using service principal key based authentication.

**Request**

| accordion |
| --- |
| View example request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Connection for Azure Synapse Analytics", "description": "Connection for Azure Synapse Analytics", "auth": { "specName": "Service Principal Key Based Authentication", "params": { "server": "yourworkspace.sql.azuresynapse.net", "database": "SalesDW", "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db47", "servicePrincipalId": "e7b8c1f2-1234-4c9a-9f3e-abcdef123456", "servicePrincipalKey": "~XyZ1234abcDEF5678..." } }, "connectionSpec": { "id": "a49bcc7d-8038-43af-b1e4-5a7a089a7d79", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Credential Description auth.params.server The fully qualified domain name of your Azure Synapse Analytics SQL endpoint. auth.params.database The name of the specific database within your Azure Synapse Analytics workspace. auth.params.tenant The Azure Active Directory tenant ID associated with your Azure subscription. auth.params.servicePrincipalId The client ID of an Azure Active Directory application. auth.params.servicePrincipalKey The client secret or password associated with the service principal. connectSpec.id The connection spec ID of Azure Synapse Analytics. | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Connection for Azure Synapse Analytics", "description": "Connection for Azure Synapse Analytics", "auth": { "specName": "Service Principal Key Based Authentication", "params": { "server": "yourworkspace.sql.azuresynapse.net", "database": "SalesDW", "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db47", "servicePrincipalId": "e7b8c1f2-1234-4c9a-9f3e-abcdef123456", "servicePrincipalKey": "~XyZ1234abcDEF5678..." } }, "connectionSpec": { "id": "a49bcc7d-8038-43af-b1e4-5a7a089a7d79", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  | Credential | Description | auth.params.server | The fully qualified domain name of your Azure Synapse Analytics SQL endpoint. | auth.params.database | The name of the specific database within your Azure Synapse Analytics workspace. | auth.params.tenant | The Azure Active Directory tenant ID associated with your Azure subscription. | auth.params.servicePrincipalId | The client ID of an Azure Active Directory application. | auth.params.servicePrincipalKey | The client secret or password associated with the service principal. | connectSpec.id | The connection spec ID of Azure Synapse Analytics. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Connection for Azure Synapse Analytics", "description": "Connection for Azure Synapse Analytics", "auth": { "specName": "Service Principal Key Based Authentication", "params": { "server": "yourworkspace.sql.azuresynapse.net", "database": "SalesDW", "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db47", "servicePrincipalId": "e7b8c1f2-1234-4c9a-9f3e-abcdef123456", "servicePrincipalKey": "~XyZ1234abcDEF5678..." } }, "connectionSpec": { "id": "a49bcc7d-8038-43af-b1e4-5a7a089a7d79", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| Credential | Description |
| auth.params.server | The fully qualified domain name of your Azure Synapse Analytics SQL endpoint. |
| auth.params.database | The name of the specific database within your Azure Synapse Analytics workspace. |
| auth.params.tenant | The Azure Active Directory tenant ID associated with your Azure subscription. |
| auth.params.servicePrincipalId | The client ID of an Azure Active Directory application. |
| auth.params.servicePrincipalKey | The client secret or password associated with the service principal. |
| connectSpec.id | The connection spec ID of Azure Synapse Analytics. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| View example response |
| code language-json { "id": "6bc13a3b-3546-455f-813a-3b3546a55fb1", "etag": "\"3500866c-0000-0200-0000-5e83afa30000\"" } | code language-json | { "id": "6bc13a3b-3546-455f-813a-3b3546a55fb1", "etag": "\"3500866c-0000-0200-0000-5e83afa30000\"" } |
| code language-json |
| { "id": "6bc13a3b-3546-455f-813a-3b3546a55fb1", "etag": "\"3500866c-0000-0200-0000-5e83afa30000\"" } |

## Next steps

By following this tutorial, you have created a Azure Synapse Analytics base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
