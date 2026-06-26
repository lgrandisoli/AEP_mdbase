---
title: "Connect MariaDB to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/mariadb"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:06.581353+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect MariaDB to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your MariaDB account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to MariaDB using the Flow Service API.

### Gather required credentials

Read the [MariaDB overview](/en/docs/experience-platform/sources/connectors/databases/mariadb#prerequisites) for information on authentication.

### Using Experience Platform APIs

Read the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide) for information on how to successfully make calls to Experience Platform APIs.

## Connect MariaDB to Experience Platform

Read the steps below for information on how to connect your MariaDB account to Experience Platform.

### Create a base connection for MariaDB

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

**API format**

```
POST /connections
```

To create a base connection ID, make a POST request to the /connections endpoint and provide the appropriate authentication credentials for your MariaDB account.

Connection string based authentication
**Request**

The following request creates a base connection for a MariaDB source using connection string based authentication.

| accordion |
| --- |
| View request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MariaDB connection", "description": "MariaDB connection", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={HOST};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}" } }, "connectionSpec": { "id": "3000eb99-cd47-43f3-827c-43caf170f015", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 Property Description auth.params.connectionString The connection string associated with your MariaDB authentication. The MariaDB connection string pattern is: Server={HOST};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD} . connectionSpec.id The MariaDB connection specification ID is: 3000eb99-cd47-43f3-827c-43caf170f015 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MariaDB connection", "description": "MariaDB connection", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={HOST};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}" } }, "connectionSpec": { "id": "3000eb99-cd47-43f3-827c-43caf170f015", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 |  | Property | Description | auth.params.connectionString | The connection string associated with your MariaDB authentication. The MariaDB connection string pattern is: Server={HOST};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}. | connectionSpec.id | The MariaDB connection specification ID is: 3000eb99-cd47-43f3-827c-43caf170f015. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MariaDB connection", "description": "MariaDB connection", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={HOST};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}" } }, "connectionSpec": { "id": "3000eb99-cd47-43f3-827c-43caf170f015", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 |  |
| Property | Description |
| auth.params.connectionString | The connection string associated with your MariaDB authentication. The MariaDB connection string pattern is: Server={HOST};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}. |
| connectionSpec.id | The MariaDB connection specification ID is: 3000eb99-cd47-43f3-827c-43caf170f015. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| View response example |
| code language-json { "id": "be3a2d71-1fb6-4fea-ba2d-711fb61fea50", "etag": "\"02002624-0000-0200-0000-5e41f7040000\"" } | code language-json | { "id": "be3a2d71-1fb6-4fea-ba2d-711fb61fea50", "etag": "\"02002624-0000-0200-0000-5e41f7040000\"" } |
| code language-json |
| { "id": "be3a2d71-1fb6-4fea-ba2d-711fb61fea50", "etag": "\"02002624-0000-0200-0000-5e41f7040000\"" } |

Basic authentication
**Request**

The following request creates a base connection for a MariaDB source using basic authentication.

| accordion |
| --- |
| View request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MariaDB on Experience Platform using basic auth", "description": "MariaDB on Experience Platform using basic auth", "auth": { "specName": "Basic Authentication", "params": { "server": "{SERVER}", "database": "{DATABASE}", "username": "{USERNAME}", "password": "{PASSWORD}", "sslMode": "{SSLMODE}" } }, "connectionSpec": { "id": "3000eb99-cd47-43f3-827c-43caf170f015", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Property Description auth.params.server The name or IP of your MariaDB database. auth.params.database The name of your database. auth.params.username The username that corresponds with your database. auth.params.password The password that corresponds with your database. auth.params.sslMode The method by which data is encrypted during data transfer. connectionSpec.id The MariaDB connection specification ID is: 3000eb99-cd47-43f3-827c-43caf170f015 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MariaDB on Experience Platform using basic auth", "description": "MariaDB on Experience Platform using basic auth", "auth": { "specName": "Basic Authentication", "params": { "server": "{SERVER}", "database": "{DATABASE}", "username": "{USERNAME}", "password": "{PASSWORD}", "sslMode": "{SSLMODE}" } }, "connectionSpec": { "id": "3000eb99-cd47-43f3-827c-43caf170f015", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  | Property | Description | auth.params.server | The name or IP of your MariaDB database. | auth.params.database | The name of your database. | auth.params.username | The username that corresponds with your database. | auth.params.password | The password that corresponds with your database. | auth.params.sslMode | The method by which data is encrypted during data transfer. | connectionSpec.id | The MariaDB connection specification ID is: 3000eb99-cd47-43f3-827c-43caf170f015. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MariaDB on Experience Platform using basic auth", "description": "MariaDB on Experience Platform using basic auth", "auth": { "specName": "Basic Authentication", "params": { "server": "{SERVER}", "database": "{DATABASE}", "username": "{USERNAME}", "password": "{PASSWORD}", "sslMode": "{SSLMODE}" } }, "connectionSpec": { "id": "3000eb99-cd47-43f3-827c-43caf170f015", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| Property | Description |
| auth.params.server | The name or IP of your MariaDB database. |
| auth.params.database | The name of your database. |
| auth.params.username | The username that corresponds with your database. |
| auth.params.password | The password that corresponds with your database. |
| auth.params.sslMode | The method by which data is encrypted during data transfer. |
| connectionSpec.id | The MariaDB connection specification ID is: 3000eb99-cd47-43f3-827c-43caf170f015. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| View response example |
| code language-json { "id": "f847950c-1c12-4568-a550-d5312b16fdb8", "etag": "\"0c0099f4-0000-0200-0000-67da91710000\"" } | code language-json | { "id": "f847950c-1c12-4568-a550-d5312b16fdb8", "etag": "\"0c0099f4-0000-0200-0000-67da91710000\"" } |
| code language-json |
| { "id": "f847950c-1c12-4568-a550-d5312b16fdb8", "etag": "\"0c0099f4-0000-0200-0000-67da91710000\"" } |

## Next steps

By following this tutorial, you have created a MariaDB base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
