---
title: "Connect AWS Redshift to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/redshift"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:35:58.071712+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Connect AWS Redshift to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The AWS Redshift source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this guide to learn how you can connect your AWS Redshift source account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Connect AWS Redshift to Experience Platform on Azure azure

Read the steps below for information on how to connect your AWS Redshift source to Experience Platform on Azure.

### Gather required credentials

In order for Flow Service to connect with AWS Redshift, you must provide the following connection properties:

| Credential | Description || server | The server name of your AWS Redshift instance. || port | The TCP port that a AWS Redshift server uses to listen for client connections. || username | The username associated with your AWS Redshift account. || password | The password that corresponds with the user account. || database | The AWS Redshift database where data is to be fetched from. || connectionSpec.id | The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for AWS Redshift is 3416976c-a9ca-4bba-901a-1f08f66978ff. |

For more information about getting started, refer to this [AWS Redshift document](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html).

### Create a base connection for AWS Redshift on Experience Platform on Azure [#azure-base]

NOTE
The default encoding standard for Redshift is Unicode. This cannot be changed.
A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your AWS Redshift authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

Select to view example
The following request creates a base connection for AWS Redshift:

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "AWS-redshift base connection", "description": "base connection for AWS-redshift, "auth": { "specName": "Basic Authentication", "params": { "server": "{SERVER}", "port": "{PORT}, "username": "{USERNAME}", "password": "{PASSWORD}", "database": "{DATABASE}" } }, "connectionSpec": { "id": "3416976c-a9ca-4bba-901a-1f08f66978ff", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.server | The server name of your AWS Redshift instance. |
| auth.params.port | The TCP port that a AWS Redshift server uses to listen for client connections. |
| auth.params.username | The username associated with your AWS Redshift account. |
| auth.params.password | The password that corresponds with the user account. |
| auth.params.database | The AWS Redshift database where data is to be fetched from. |
| connectionSpec.id | The AWS Redshift connection specification ID: 3416976c-a9ca-4bba-901a-1f08f66978ff |

**Response**

Select to view example
A successful response returns the newly created connection, including its unique identifier (id). This ID is required to explore your data in the next tutorial.

| code language-json |
| --- |
| { "id": "373e88fc-43da-4e3c-be88-fc43da3e3c0f", "etag": "\"1700ce7b-0000-0200-0000-5e3b405e0000\"" } |

## Connect AWS Redshift to Experience Platform on AWS Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on AWS Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your AWS Redshift source to Experience Platform on AWS.

### Create a base connection for AWS Redshift on Experience Platform on AWS aws-base

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for AWS Redshift:

Select to view example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "AWS Redshift base connection for Experience Platform on AWS", "description": "AWS Redshift base connection for Experience Platform on AWS", "auth": { "specName": "Basic Authentication", "params": { "server": "{SERVER}", "port": "5439", "username": "{USERNAME}", "password": "{PASSWORD}", "database": "{DATABASE}", "schema": "{SCHEMA}" } }, "connectionSpec": { "id": "3416976c-a9ca-4bba-901a-1f08f66978ff", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.server | The server name of your AWS Redshift instance. |
| auth.params.port | The TCP port that a AWS Redshift server uses to listen for client connections. |
| auth.params.username | The username associated with your AWS Redshift account. |
| auth.params.password | The password that corresponds with the user account. |
| auth.params.database | The AWS Redshift database where data is to be fetched from. |
| auth.params.schema | The name of the schema associated with your AWS Redshift database. You must ensure that the user you want to give database access to, also has access to this schema. |
| connectionSpec.id | The AWS Redshift connection specification ID: 3416976c-a9ca-4bba-901a-1f08f66978ff |

**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your storage in the next tutorial.

Select to view example
| code language-json |
| --- |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |

## Next steps

By following this tutorial, you have created an AWS Redshift base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
