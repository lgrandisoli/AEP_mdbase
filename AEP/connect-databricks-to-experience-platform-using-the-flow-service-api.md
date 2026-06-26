---
title: "Connect Databricks to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/databricks"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:13.749447+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Databricks to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

AVAILABILITY
The Databricks source is available in the sources catalog to users who have purchased Real-Time CDP Ultimate.
Read this guide to learn how to connect your Databricks account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Use Experience Platform APIs

Read the guide on [how to get started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide) for information on how to successfully make calls to Experience Platform APIs.

### Configure prerequisite setup

Read the [Databricks overview](/en/docs/experience-platform/sources/connectors/databases/databricks) to learn about the prerequisite configurations that must be completed before you can connect your account to Experience Platform.

### Gather required credentials

Provide values for the following credentials to connect Databricks to Experience Platform.

Credential
Description
domain
The URL of your Databricks workspace. For example,
https://adb-1234567890123456.7.azuredatabricks.net
.
clusterId
The ID of your cluster in Databricks. This cluster must already be an existing cluster and should be an interactive cluster.
accessToken
The access token that authenticates your Databricks account. You can generate your access token using the Databricks workspace.
database
The name of your database in the delta lake.
catalog
The name of your catalog in the delta lake. You do not need to specify a value for a default catalog.
connectionSpec.Id
The connection spec ID returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection spec ID for Databricks is
e9d7ec6b-0873-4e57-ad21-b3a7c65e310b
.
For more information, read the [Databricks overview](/en/docs/experience-platform/sources/connectors/databases/databricks).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint and provide the appropriate authentication credentials for your Databricks account.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for a Databricks source using access token authentication.

View request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Databricks connection to Experience Platform", "description": "A Databricks base connection to Experience Platform", "auth": { "specName": "Access Token Authentication", "params": { "domain": "https://adb-1234567890123456.7.azuredatabricks.net", "clusterId": "xxxx", "accessToken": "xxxx", "database": "acme-db" } }, "connectionSpec": { "id": "e9d7ec6b-0873-4e57-ad21-b3a7c65e310b", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.domain | The URL of your Databricks workspace. |
| auth.params.clusterId | The ID of your cluster in Databricks. This cluster must already be an existing cluster and should be an interactive cluster |
| auth.params.accessToken | The access token that authenticates your Databricks account. |
| auth.params.database | The name of your database in the delta lake. |
| connectionSpec.id | The Databricks connection spec ID. |

**Response**

A successful response returns your newly created connection, including your base connection ID.

View response example
| code language-json |
| --- |
| { "id": "f847950c-1c12-4568-a550-d5312b16fdb8", "etag": "\"0c0099f4-0000-0200-0000-67da91710000\"" } |

## Next steps

By following this tutorial, you have successfully created a connection between your Databricks account and Experience Platform. You can use your newly generated base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
