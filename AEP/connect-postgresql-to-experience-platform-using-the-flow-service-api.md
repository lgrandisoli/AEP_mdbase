---
title: "Connect PostgreSQL to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/postgres"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:14.742870+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect PostgreSQL to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your PostgreSQL database to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to PostgreSQL using the Flow Service API.

### Using Experience Platform APIs

Read the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide) for information on how to successfully make calls to Experience Platform APIs.

### Gather required credentials

Read the [PostgreSQL overview](/en/docs/experience-platform/sources/connectors/databases/postgres) for more information on authentication.

### Enable SSL encryption for your connection string

You can enable SSL encryption for your PostgreSQL connection string by appending your connection string with the following properties:

Property
Description
Example
EncryptionMethod
Allows you to enable SSL encryption on your PostgreSQL data.
- EncryptionMethod=0(Disabled)
- EncryptionMethod=1(Enabled)
- EncryptionMethod=6(RequestSSL)

ValidateServerCertificate
Validates certificate sent by your PostgreSQL database when
EncryptionMethod
is applied.
- ValidationServerCertificate=0(Disabled)
- ValidationServerCertificate=1(Enabled)

The following is an example of a PostgreSQL connection string appended with SSL encryption: Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD};EncryptionMethod=1;ValidateServerCertificate=1.

## Connect PostgreSQL to Experience Platform on Azure azure

Read the steps below to learn how to connect your PostgreSQL account to Experience Platform on Azure.

### Create a base connection azure-base

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your PostgreSQL authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

Account key based authentication
**Request**

The following request creates a base connection for PostgreSQL using account key based authentication:

| accordion |
| --- |
| View request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via connection string", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD}" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 Property Description auth.params.connectionString The connection string associated with your PostgreSQL account. The PostgreSQL connection string pattern is: Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD} . connectionSpec.id The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via connection string", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD}" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 |  | Property | Description | auth.params.connectionString | The connection string associated with your PostgreSQL account. The PostgreSQL connection string pattern is: Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD}. | connectionSpec.id | The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via connection string", "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD}" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 |  |
| Property | Description |
| auth.params.connectionString | The connection string associated with your PostgreSQL account. The PostgreSQL connection string pattern is: Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD}. |
| connectionSpec.id | The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137. |

**Response**

A successful response returns the unique identifier (id) of the newly created base connection.

| accordion |
| --- |
| View response example |
| code language-json { "id": "056dd1b4-da33-42f9-add1-b4da3392f94e", "etag": "\"1700e582-0000-0200-0000-5e3c85180000\"" } | code language-json | { "id": "056dd1b4-da33-42f9-add1-b4da3392f94e", "etag": "\"1700e582-0000-0200-0000-5e3c85180000\"" } |
| code language-json |
| { "id": "056dd1b4-da33-42f9-add1-b4da3392f94e", "etag": "\"1700e582-0000-0200-0000-5e3c85180000\"" } |

Basic authentication
**Request**

The following request creates a base connection for PostgreSQL using basic authentication:

| accordion |
| --- |
| View request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via basic authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "3306", "database": "postgresql-acme", "username": "acme", "password": "xxxx", "sslMode": "Allow" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Property Description auth.params.server The name or IP address of your PostgreSQL database. auth.params.port The port number of the database server. auth.params.database The name of your PostgreSQL database. auth.params.username The username associated with your PostgreSQL database authentication. auth.params.password The password associated with your PostgreSQL database authentication. auth.params.sslMode The method by which data is encrypted during data transfer. The available values include: Disable , Allow , Prefer , Verify Ca , and Verify Full . connectionSpec.id The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via basic authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "3306", "database": "postgresql-acme", "username": "acme", "password": "xxxx", "sslMode": "Allow" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  | Property | Description | auth.params.server | The name or IP address of your PostgreSQL database. | auth.params.port | The port number of the database server. | auth.params.database | The name of your PostgreSQL database. | auth.params.username | The username associated with your PostgreSQL database authentication. | auth.params.password | The password associated with your PostgreSQL database authentication. | auth.params.sslMode | The method by which data is encrypted during data transfer. The available values include: Disable, Allow, Prefer, Verify Ca, and Verify Full. | connectionSpec.id | The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via basic authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "3306", "database": "postgresql-acme", "username": "acme", "password": "xxxx", "sslMode": "Allow" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| Property | Description |
| auth.params.server | The name or IP address of your PostgreSQL database. |
| auth.params.port | The port number of the database server. |
| auth.params.database | The name of your PostgreSQL database. |
| auth.params.username | The username associated with your PostgreSQL database authentication. |
| auth.params.password | The password associated with your PostgreSQL database authentication. |
| auth.params.sslMode | The method by which data is encrypted during data transfer. The available values include: Disable, Allow, Prefer, Verify Ca, and Verify Full. |
| connectionSpec.id | The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137. |

**Response**

A successful response returns the unique identifier (id) of the newly created base connection.

| accordion |
| --- |
| View response example |
| code language-json { "id": "2c15b1c5-73bf-47ab-9098-0467fcd854d9", "etag": "\"2600fc39-0000-0200-0000-67dd48f80000\"" } | code language-json | { "id": "2c15b1c5-73bf-47ab-9098-0467fcd854d9", "etag": "\"2600fc39-0000-0200-0000-67dd48f80000\"" } |
| code language-json |
| { "id": "2c15b1c5-73bf-47ab-9098-0467fcd854d9", "etag": "\"2600fc39-0000-0200-0000-67dd48f80000\"" } |

## Connect PostgreSQL to Experience Platform on Amazon Web Services aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your PostgreSQL database to Experience Platform on AWS.

### Create a base connection aws-base

To create a base connection ID, make a POST request to the /connections endpoint while providing your PostgreSQL authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for PostgreSQL to connect to Experience Platform on AWS.

View request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "PostgreSQL base connection", "description": "PostgreSQL base connection via basic authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "3306", "database": "postgresql-acme", "username": "acme", "password": "xxxx", "sslMode": "false" } }, "connectionSpec": { "id": "74a1c565-4e59-48d7-9d67-7c03b8a13137", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.server | The name or IP address of your PostgreSQL database. |
| auth.params.port | The port number of the database server. |
| auth.params.database | The name of your PostgreSQL database. |
| auth.params.username | The username associated with your PostgreSQL database authentication. |
| auth.params.password | The password associated with your PostgreSQL database authentication. |
| sslMode | A boolean value that controls whether SSL is enforced or not, depending on your server support. This configuration defaults to false. |
| connectionSpec.id | The PostgreSQL connection specification IDs: 74a1c565-4e59-48d7-9d67-7c03b8a13137. |

**Response**

A successful response returns the unique identifier (id) of the newly created base connection.

View response example
| code language-json |
| --- |
| { "id": "2c15b1c5-73bf-47ab-9098-0467fcd854d9", "etag": "\"2600fc39-0000-0200-0000-67dd48f80000\"" } |

## Next steps

Now that you have created a connection between your PostgreSQL database and Experience Platform, you can now proceed to next steps and bring your PostgreSQL data to Experience Platform. For more information, read the following documentation:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
