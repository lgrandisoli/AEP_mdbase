---
title: "Connect Snowflake to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/snowflake"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:17.272785+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Connect Snowflake to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Snowflake source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this guide to learn how you can connect your Snowflake source account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

The following section provides additional information that you will need to know in order to successfully connect to Snowflake using the Flow Service API.

### Gather required credentials

Read the [Snowflake overview](/en/docs/experience-platform/sources/connectors/databases/snowflake#prerequisites) for information on authentication.

## Connect Snowflake to Experience Platform on Azure azure

Read the steps below for information on how to connect your Snowflake source to Experience Platform on Azure.

NOTE
You must set the
PREVENT_UNLOAD_TO_INLINE_URL
flag to
FALSE
to allow data unloading from your Snowflake database to Experience Platform.
### Create a base connection for Snowflake on Experience Platform on Azure azure-base

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Snowflake authentication credentials as part of the request body.

**API format**

```
POST /connections
```

Key-pair authentication with encrypted private key
| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with encrypted private key", "description": "Snowflake base connection with encrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "privateKeyPassphrase": "abcd1234", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Property Description auth.params.account The name of your Snowflake account. auth.params.username The username associated with your Snowflake account. auth.params.database The Snowflake database from where the data will be pulled from. auth.params.privateKey The Base64-encoded encrypted private key of your Snowflake account. auth.params.privateKeyPassphrase The passphrase that corresponds with your private key. auth.params.warehouse The Snowflake warehouse that you are using. connectionSpec.id The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with encrypted private key", "description": "Snowflake base connection with encrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "privateKeyPassphrase": "abcd1234", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  | Property | Description | auth.params.account | The name of your Snowflake account. | auth.params.username | The username associated with your Snowflake account. | auth.params.database | The Snowflake database from where the data will be pulled from. | auth.params.privateKey | The Base64-encoded encrypted private key of your Snowflake account. | auth.params.privateKeyPassphrase | The passphrase that corresponds with your private key. | auth.params.warehouse | The Snowflake warehouse that you are using. | connectionSpec.id | The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with encrypted private key", "description": "Snowflake base connection with encrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "privateKeyPassphrase": "abcd1234", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| Property | Description |
| auth.params.account | The name of your Snowflake account. |
| auth.params.username | The username associated with your Snowflake account. |
| auth.params.database | The Snowflake database from where the data will be pulled from. |
| auth.params.privateKey | The Base64-encoded encrypted private key of your Snowflake account. |
| auth.params.privateKeyPassphrase | The passphrase that corresponds with your private key. |
| auth.params.warehouse | The Snowflake warehouse that you are using. |
| connectionSpec.id | The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). code language-json { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } | code language-json | { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } |
| code language-json |
| { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } |

Key-pair authentication with unencrypted private key
| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with unencrypted private key", "description": "Snowflake base connection with unencrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Property Description auth.params.account The name of your Snowflake account. auth.params.username The username associated with your Snowflake account. auth.params.database The Snowflake database from where the data will be pulled from. auth.params.privateKey The Base64-encoded unencrypted private key of your Snowflake account. auth.params.warehouse The Snowflake warehouse that you are using. connectionSpec.id The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with unencrypted private key", "description": "Snowflake base connection with unencrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  | Property | Description | auth.params.account | The name of your Snowflake account. | auth.params.username | The username associated with your Snowflake account. | auth.params.database | The Snowflake database from where the data will be pulled from. | auth.params.privateKey | The Base64-encoded unencrypted private key of your Snowflake account. | auth.params.warehouse | The Snowflake warehouse that you are using. | connectionSpec.id | The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with unencrypted private key", "description": "Snowflake base connection with unencrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| Property | Description |
| auth.params.account | The name of your Snowflake account. |
| auth.params.username | The username associated with your Snowflake account. |
| auth.params.database | The Snowflake database from where the data will be pulled from. |
| auth.params.privateKey | The Base64-encoded unencrypted private key of your Snowflake account. |
| auth.params.warehouse | The Snowflake warehouse that you are using. |
| connectionSpec.id | The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). code language-json { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } | code language-json | { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } |
| code language-json |
| { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } |

## Connect Snowflake to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your Snowflake source to Experience Platform on AWS.

### Create a base connection for Snowflake on Experience Platform in AWS aws-base

**API format**

```
POST /connections
```

Basic authentication
The following request creates a base connection for Snowflake to ingest data to Experience Platform on AWS:

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection for Experience Platform on AWS", "description": "Snowflake base connection for Experience Platform on AWS", "auth": { "specName": "Basic Authentication", "params": { "host": "acme.snowflakecomputing.com", "port": "443", "username": "acme-cj123", "password": "{PASSWORD}", "database": "ACME_DB", "warehouse": "COMPUTE_WH", "schema": "{SCHEMA}" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Property Description auth.params.host The host URL that your Snowflake account connects to. auth.params.port The port number that is used by Snowflake when connecting to a server over the internet. auth.params.username The username associated with your Snowflake account. auth.params.database The Snowflake database from where the data will be pulled from. auth.params.password The password associated with your Snowflake account. auth.params.warehouse The Snowflake warehouse that you are using. auth.params.schema The name of the schema associated with your Snowflake database. You must ensure that the user you want to give database access to, also has access to this schema. | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection for Experience Platform on AWS", "description": "Snowflake base connection for Experience Platform on AWS", "auth": { "specName": "Basic Authentication", "params": { "host": "acme.snowflakecomputing.com", "port": "443", "username": "acme-cj123", "password": "{PASSWORD}", "database": "ACME_DB", "warehouse": "COMPUTE_WH", "schema": "{SCHEMA}" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  | Property | Description | auth.params.host | The host URL that your Snowflake account connects to. | auth.params.port | The port number that is used by Snowflake when connecting to a server over the internet. | auth.params.username | The username associated with your Snowflake account. | auth.params.database | The Snowflake database from where the data will be pulled from. | auth.params.password | The password associated with your Snowflake account. | auth.params.warehouse | The Snowflake warehouse that you are using. | auth.params.schema | The name of the schema associated with your Snowflake database. You must ensure that the user you want to give database access to, also has access to this schema. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection for Experience Platform on AWS", "description": "Snowflake base connection for Experience Platform on AWS", "auth": { "specName": "Basic Authentication", "params": { "host": "acme.snowflakecomputing.com", "port": "443", "username": "acme-cj123", "password": "{PASSWORD}", "database": "ACME_DB", "warehouse": "COMPUTE_WH", "schema": "{SCHEMA}" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| Property | Description |
| auth.params.host | The host URL that your Snowflake account connects to. |
| auth.params.port | The port number that is used by Snowflake when connecting to a server over the internet. |
| auth.params.username | The username associated with your Snowflake account. |
| auth.params.database | The Snowflake database from where the data will be pulled from. |
| auth.params.password | The password associated with your Snowflake account. |
| auth.params.warehouse | The Snowflake warehouse that you are using. |
| auth.params.schema | The name of the schema associated with your Snowflake database. You must ensure that the user you want to give database access to, also has access to this schema. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). code language-json { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } | code language-json | { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |
| code language-json |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |

Key-pair authentication with unencrypted private key
| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with unencrypted private key", "description": "Snowflake base connection with unencrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Property Description auth.params.account The name of your Snowflake account. auth.params.username The username associated with your Snowflake account. auth.params.database The Snowflake database from where the data will be pulled from. auth.params.privateKey The Base64-encoded unencrypted private key of your Snowflake account. auth.params.warehouse The Snowflake warehouse that you are using. connectionSpec.id The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3 . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with unencrypted private key", "description": "Snowflake base connection with unencrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  | Property | Description | auth.params.account | The name of your Snowflake account. | auth.params.username | The username associated with your Snowflake account. | auth.params.database | The Snowflake database from where the data will be pulled from. | auth.params.privateKey | The Base64-encoded unencrypted private key of your Snowflake account. | auth.params.warehouse | The Snowflake warehouse that you are using. | connectionSpec.id | The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Snowflake base connection with unencrypted private key", "description": "Snowflake base connection with unencrypted private key", "auth": { "specName": "KeyPair Authentication", "params": { "account": "acme-snowflake123", "username": "acme-cj123", "database": "ACME_DB", "privateKey": "{BASE_64_ENCODED_PRIVATE_KEY}", "warehouse": "COMPUTE_WH" } }, "connectionSpec": { "id": "b2e08744-4f1a-40ce-af30-7abac3e23cf3", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| Property | Description |
| auth.params.account | The name of your Snowflake account. |
| auth.params.username | The username associated with your Snowflake account. |
| auth.params.database | The Snowflake database from where the data will be pulled from. |
| auth.params.privateKey | The Base64-encoded unencrypted private key of your Snowflake account. |
| auth.params.warehouse | The Snowflake warehouse that you are using. |
| connectionSpec.id | The Snowflake connection specification ID: b2e08744-4f1a-40ce-af30-7abac3e23cf3. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). code language-json { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } | code language-json | { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |
| code language-json |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |

By following this tutorial, you have created a Snowflake base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
