---
title: "Connect MySQL to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/mysql"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:33.845204+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect MySQL to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your MySQL account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to MySQL using the Flow Service API.

### Gather required credentials

Read the [MySQL overview](/en/docs/experience-platform/sources/connectors/databases/mysql#prerequisites) for information on authentication.

### Using Experience Platform APIs

Read the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide) for information on how to successfully make calls to Experience Platform APIs.

## Connect MySQL to Experience Platform on Azure azure

Read the steps below for information on how to connect your MySQL account to Experience Platform on Azure.

### Create a base connection for MySQL on Experience Platform on Azure azure-base

A base connection links your source to Experience Platform, storing authentication details, connection status, and a unique ID. Use this ID to browse source files and identify specific items to ingest, including their data types and formats.

**API format**

```
POST /connections
```

To create a base connection ID, make a POST request to the /connections endpoint and provide your MySQL authentication credentials as part of the request parameters.

Connection string based authentication
**Request**

The following request creates a base connection for MySQL using connection string based authentication.

| accordion |
| --- |
| View request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL Base Connection to Experience Platform", "description": "Via Connection String, "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 Property Description auth.params.connectionString The MySQL connection string associated with your account. The MySQL connection string pattern is: Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD} . connectionSpec.id The MySQL connection specification ID: 26d738e0-8963-47ea-aadf-c60de735468a . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL Base Connection to Experience Platform", "description": "Via Connection String, "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 |  | Property | Description | auth.params.connectionString | The MySQL connection string associated with your account. The MySQL connection string pattern is: Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}. | connectionSpec.id | The MySQL connection specification ID: 26d738e0-8963-47ea-aadf-c60de735468a. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL Base Connection to Experience Platform", "description": "Via Connection String, "auth": { "specName": "Connection String Based Authentication", "params": { "connectionString": "Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 |  |
| Property | Description |
| auth.params.connectionString | The MySQL connection string associated with your account. The MySQL connection string pattern is: Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}. |
| connectionSpec.id | The MySQL connection specification ID: 26d738e0-8963-47ea-aadf-c60de735468a. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| View response example |
| code language-json { "id": "1a444165-3439-4c16-8441-653439dc166a", "etag": "\"5b04c219-0000-0200-0000-5e179c8f0000\"" } | code language-json | { "id": "1a444165-3439-4c16-8441-653439dc166a", "etag": "\"5b04c219-0000-0200-0000-5e179c8f0000\"" } |
| code language-json |
| { "id": "1a444165-3439-4c16-8441-653439dc166a", "etag": "\"5b04c219-0000-0200-0000-5e179c8f0000\"" } |

Basic authentication
**Request**

The following request creates a base connection for a MySQL source using basic authentication.

| accordion |
| --- |
| View request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL Base Connection to Experience Platform", "description": "Via Basic Authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "443", "database": "mysql-acme", "username": "acme", "password": "xxxx", "sslMode": "DISABLED" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Property Description auth.params.server The name or IP of your MySQL database. auth.params.database The name of your database. auth.params.username The username that corresponds with your database. auth.params.password The password that corresponds with your database. auth.params.sslMode The method by which data is encrypted during data transfer. connectionSpec.id The MySQL connection specification ID is: 26d738e0-8963-47ea-aadf-c60de735468a . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL Base Connection to Experience Platform", "description": "Via Basic Authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "443", "database": "mysql-acme", "username": "acme", "password": "xxxx", "sslMode": "DISABLED" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  | Property | Description | auth.params.server | The name or IP of your MySQL database. | auth.params.database | The name of your database. | auth.params.username | The username that corresponds with your database. | auth.params.password | The password that corresponds with your database. | auth.params.sslMode | The method by which data is encrypted during data transfer. | connectionSpec.id | The MySQL connection specification ID is: 26d738e0-8963-47ea-aadf-c60de735468a. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL Base Connection to Experience Platform", "description": "Via Basic Authentication", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "443", "database": "mysql-acme", "username": "acme", "password": "xxxx", "sslMode": "DISABLED" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| Property | Description |
| auth.params.server | The name or IP of your MySQL database. |
| auth.params.database | The name of your database. |
| auth.params.username | The username that corresponds with your database. |
| auth.params.password | The password that corresponds with your database. |
| auth.params.sslMode | The method by which data is encrypted during data transfer. |
| connectionSpec.id | The MySQL connection specification ID is: 26d738e0-8963-47ea-aadf-c60de735468a. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| View response example |
| code language-json { "id": "025d4158-4113-403b-b551-e81724d3880c", "etag": "\"ae004437-0000-0200-0000-67ee107e0000\"" } | code language-json | { "id": "025d4158-4113-403b-b551-e81724d3880c", "etag": "\"ae004437-0000-0200-0000-67ee107e0000\"" } |
| code language-json |
| { "id": "025d4158-4113-403b-b551-e81724d3880c", "etag": "\"ae004437-0000-0200-0000-67ee107e0000\"" } |

## Connect MySQL to Experience Platform on Amazon Web Services aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your MySQL account to Experience Platform on AWS.

### Create a base connection for MySQL on Experience Platform on AWS aws-base

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for MySQL to connect to Experience Platform on AWS.

View request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "MySQL on Experience Platform AWS", "description": "MySQL on Experience Platform AWS", "auth": { "specName": "Basic Authentication", "params": { "server": "localhost", "port": "443", "database": "mysql-acme", "username": "acme", "password": "xxxx", "sslMode": "false" } }, "connectionSpec": { "id": "26d738e0-8963-47ea-aadf-c60de735468a", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.server | The name or IP of your MySQL database. |
| auth.params.database | The name of your database. |
| auth.params.username | The username that corresponds with your database. |
| auth.params.password | The password that corresponds with your database. |
| auth.params.sslMode | A boolean value that controls whether SSL is enforced or not, depending on your server support. This configuration defaults to false. |
| connectionSpec.id | The MySQL connection specification ID is: 26d738e0-8963-47ea-aadf-c60de735468a. |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

View response example
| code language-json |
| --- |
| { "id": "f847950c-1c12-4568-a550-d5312b16fdb8", "etag": "\"0c0099f4-0000-0200-0000-67da91710000\"" } |

## Create a dataflow for MySQL data

Now that you have successfully connected your MySQL database, you can now [create a dataflow and ingest data from your database into Experience Platform](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql).

recommendation-more-help
