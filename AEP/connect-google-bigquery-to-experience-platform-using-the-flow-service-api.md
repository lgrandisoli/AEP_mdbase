---
title: "Connect Google BigQuery to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/bigquery"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:19.412640+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Connect Google BigQuery to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Google BigQuery source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this guide to learn how to connect your Google BigQuery database to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

### Gather required credentials

Read the [Google BigQuery authentication guide](/en/docs/experience-platform/sources/connectors/databases/bigquery#prerequisites) for detailed steps on retrieving your Google BigQuery credentials.

## Connect Google BigQuery to Experience Platform on Azure azure

Read the steps below for information on how to connect your Google BigQuery source to Experience Platform on Azure.

### Create a base connection for Google BigQuery on Experience Platform on Azure azure-base

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Google BigQuery authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

Use basic authentication
| accordion |
| --- |
| Request |
| The following request creates a base connection for Google BigQuery using basic authentication. code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery connection with basic authentication", "description": "Google BigQuery connection with basic authentication", "auth": { "specName": "Basic Authentication", "type": "OAuth2.0", "params": { "project": "{PROJECT}", "clientId": "{CLIENT_ID}, "clientSecret": "{CLIENT_SECRET}", "refreshToken": "{REFRESH_TOKEN}" } }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 Property Description auth.params.project The project ID of the default Google BigQuery project to query. against. auth.params.clientId The ID value used to generate the refresh token. auth.params.clientSecret The client value used to generate the refresh token. auth.params.refreshToken The refresh token obtained from Google used to authorize access to Google BigQuery. connectionSpec.id The Google BigQuery connection specification ID: 3c9b37f8-13a6-43d8-bad3-b863b941fedd . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery connection with basic authentication", "description": "Google BigQuery connection with basic authentication", "auth": { "specName": "Basic Authentication", "type": "OAuth2.0", "params": { "project": "{PROJECT}", "clientId": "{CLIENT_ID}, "clientSecret": "{CLIENT_SECRET}", "refreshToken": "{REFRESH_TOKEN}" } }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  | Property | Description | auth.params.project | The project ID of the default Google BigQuery project to query. against. | auth.params.clientId | The ID value used to generate the refresh token. | auth.params.clientSecret | The client value used to generate the refresh token. | auth.params.refreshToken | The refresh token obtained from Google used to authorize access to Google BigQuery. | connectionSpec.id | The Google BigQuery connection specification ID: 3c9b37f8-13a6-43d8-bad3-b863b941fedd. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery connection with basic authentication", "description": "Google BigQuery connection with basic authentication", "auth": { "specName": "Basic Authentication", "type": "OAuth2.0", "params": { "project": "{PROJECT}", "clientId": "{CLIENT_ID}, "clientSecret": "{CLIENT_SECRET}", "refreshToken": "{REFRESH_TOKEN}" } }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| Property | Description |
| auth.params.project | The project ID of the default Google BigQuery project to query. against. |
| auth.params.clientId | The ID value used to generate the refresh token. |
| auth.params.clientSecret | The client value used to generate the refresh token. |
| auth.params.refreshToken | The refresh token obtained from Google used to authorize access to Google BigQuery. |
| connectionSpec.id | The Google BigQuery connection specification ID: 3c9b37f8-13a6-43d8-bad3-b863b941fedd. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). This ID is required to explore your data in the next tutorial. code language-json { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } | code language-json | { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } |
| code language-json |
| { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } |

Use service authentication
| accordion |
| --- |
| Request |
| The following request creates a base connection for Google BigQuery using service authentication: code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery base connection with service account", "description": "Google BigQuery connection with service account", "auth": { "specName": "Service Authentication", "params": { "projectId": "{PROJECT_ID}", "keyFileContent": "{KEY_FILE_CONTENT}, "largeResultsDataSetId": "{LARGE_RESULTS_DATASET_ID}" } }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 Property Description auth.params.projectId The project ID of the default Google BigQuery project to query. against. auth.params.keyFileContent The key file that is used to authenticate the service account. You must encode the key file content in Base64. auth.params.largeResultsDataSetId (Optional) The pre-created Google BigQuery dataset ID that is required in order to enable support for large result sets. | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery base connection with service account", "description": "Google BigQuery connection with service account", "auth": { "specName": "Service Authentication", "params": { "projectId": "{PROJECT_ID}", "keyFileContent": "{KEY_FILE_CONTENT}, "largeResultsDataSetId": "{LARGE_RESULTS_DATASET_ID}" } }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 |  | Property | Description | auth.params.projectId | The project ID of the default Google BigQuery project to query. against. | auth.params.keyFileContent | The key file that is used to authenticate the service account. You must encode the key file content in Base64. | auth.params.largeResultsDataSetId | (Optional) The pre-created Google BigQuery dataset ID that is required in order to enable support for large result sets. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery base connection with service account", "description": "Google BigQuery connection with service account", "auth": { "specName": "Service Authentication", "params": { "projectId": "{PROJECT_ID}", "keyFileContent": "{KEY_FILE_CONTENT}, "largeResultsDataSetId": "{LARGE_RESULTS_DATASET_ID}" } }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| Property | Description |
| auth.params.projectId | The project ID of the default Google BigQuery project to query. against. |
| auth.params.keyFileContent | The key file that is used to authenticate the service account. You must encode the key file content in Base64. |
| auth.params.largeResultsDataSetId | (Optional) The pre-created Google BigQuery dataset ID that is required in order to enable support for large result sets. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). This ID is required to explore your data in the next tutorial. code language-json { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } | code language-json | { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } |
| code language-json |
| { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } |

## Connect Google BigQuery to Experience Platform on Amazon Web Services (AWS) aws

Read the steps below for information on how to connect your Google BigQuery database to Experience Platform on AWS.

### Create a base connection for Google BigQuery on Experience Platform on AWS

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
**API format**

```
POST /connections
```

**Request**

The following request creates a base connection to connect Google BigQuery to Experience Platform on AWS.

Select to view example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google BigQuery base connection on AWS", "description": "Google BigQuery base connection on AWS", "auth": { "specName": "Service Authentication", "params": { "projectId": "{PROJECT_ID}", "keyFileContent": "{KEY_FILE_CONTENT}, "datasetId": "{DATASET_ID}" }, "connectionSpec": { "id": "3c9b37f8-13a6-43d8-bad3-b863b941fedd", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.projectId | The project ID of the default Google BigQuery project to query. against. |
| auth.params.keyFileContent | The key file that is used to authenticate the service account. You must encode the key file content in Base64. |
| auth.params.datasetId | The dataset ID that corresponds with your Google BigQuery source. This ID represents where the data tables are located. |

**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your storage in the next tutorial.

Select to view example
| code language-json |
| --- |
| { "id": "6990abad-977d-41b9-a85d-17ea8cf1c0e4", "etag": "\"ca00acbf-0000-0200-0000-60149e1e0000\"" } |

## Next steps

By following this tutorial, you have created a Google BigQuery base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
