---
title: "Connect Salesforce Marketing Cloud to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/marketing-automation/salesforce-marketing-cloud"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:08:01.169353+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Salesforce Marketing Cloud to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

WARNING
The Salesforce Marketing Cloud source will be deprecated in January 2026. A new source will be released later this year as an alternative. Once the new source is released, you must plan to migrate to the new source by creating new account connections and dataflows before the end of January 2026.
Read this guide to learn how to connect your Salesforce Marketing Cloud account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Azure Synapse Analytics using the Flow Service API.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

The following section provides additional information that you will need to know in order to successfully connect to Salesforce Marketing Cloud using the Flow Service API.

### Gather required credentials

Read the [Salesforce Marketing Cloud authentication overview](/en/docs/experience-platform/sources/connectors/marketing-automation/salesforce-marketing-cloud) for information on authentication.

### Using Experience Platform APIs

Read the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide) for information on how to successfully make calls to Experience Platform APIs.

## Connect Salesforce Marketing Cloud to Experience Platform on Azure

Read the following to learn how to create a base connection and connection your Salesforce Marketing Cloud account to Experience Platform on Azure.

### Create a base connection azure-base

IMPORTANT
Custom object ingestion is currently not supported by the Salesforce Marketing Cloud source integration.
A **base connection** stores key information that links your source system to Adobe Experience Platform. This includes:

- Your source’s authentication credentials
- The current status of the connection
- A unique **base connection ID**

The **base connection ID** allows you to browse and explore files from your source, helping you identify which items to ingest, along with their data types and formats.

To create a base connection ID, send a POST request to the /connections endpoint, including your Salesforce Marketing Cloud authentication credentials in the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Salesforce Marketing Cloud.

View example request
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Salesforce Marketing Cloud base connection for Azure", "description": "Salesforce Marketing Cloud base connection for Azure", "auth": { "specName": "Client-Id-Secret Based Authentication", "params": { "host": "acme-ab12c3d4e5fg6hijk7lmnop8qrst", "clientId": "acme-salesforce-marketing-cloud", "clientSecret": "xxxx" } }, "connectionSpec": { "id": "ea1c2a08-b722-11eb-8529-0242ac130003", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.host |  |
| auth.params.clientId | The client ID associated with your Salesforce Marketing Cloud application. |
| auth.params.clientSecret | The client secret associated with your Salesforce Marketing Cloud application. |
| connectionSpec.id | The Salesforce Marketing Cloud connection specification ID: ea1c2a08-b722-11eb-8529-0242ac130003. |

View example response
**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

| code language-json |
| --- |
| { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } |

## Connect Salesforce Marketing Cloud to Experience Platform on Amazon Web Services aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your Salesforce Marketing Cloud account to Experience Platform on AWS.

### Create a base connection aws-base

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Salesforce Service Cloud to connect to Experience Platform on AWS.

View request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Salesforce Marketing Cloud base connection for AWS", "description": "Salesforce Marketing Cloud base connection for AWS", "auth": { "specName": "OAuth2 Client Credential", "params": { "subdomain": "mc563885gzs27c5t9-63k636ttgm", "clientId": "3a1b2c3d4e5f67890123456789abcdef", "clientSecret": "xxxx" } }, "connectionSpec": { "id": "ea1c2a08-b722-11eb-8529-0242ac130003", "version": "1.0" } }' |

**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id).

View response example
| code language-json |
| --- |
| { "id": "2fce94c1-9a93-4971-8e94-c19a93097129", "etag": "\"d403848a-0000-0200-0000-5e978f7b0000\"" } |

## Create a dataflow for Salesforce Marketing Cloud data

Now that you have successfully connected your Salesforce Marketing Cloud account, you can now [create a dataflow and ingest data from your marketing automation provider into Experience Platform](/en/docs/experience-platform/sources/api-tutorials/collect/marketing-automation).

recommendation-more-help
