---
title: "Create an Oracle Eloqua base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/marketing-automation/oracle-eloqua"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:07:58.576763+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Oracle Eloqua base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

WARNING
The Oracle Eloqua source will be deprecated in January 2026. A new source will be released later this year as an alternative. Once the new source is released, you must plan to migrate to the new source by creating new account connections and dataflows before the end of January 2026.
A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Oracle Eloqua using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting Started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you need to know in order to successfully connect to Oracle Eloqua using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with Oracle Eloqua, you must provide values for the following connection properties:

Credential
Description
endpoint
The endpoint of your Oracle Eloqua.
username
The username of your Oracle Eloqua account. The username must be formatted as
siteName + \\ + username
, where
siteName
is the company name you used to log in to Oracle Eloqua and
username
is your username. For example, your log in username can be:
adobe\\emily
.
password
The password corresponding to your Oracle Eloqua username.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The value for the connection specification ID of the Oracle Eloqua source is fixed as:
35d6c4d8-c9a9-11eb-b8bc-0242ac130003
.
For more information on authentication credentials for Oracle Eloqua, see the [Oracle Eloqua guide on authentication](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Authentication_Basic.html).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Oracle Eloqua authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Oracle Eloqua:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/connections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json'
  -d '{
      "name": "Oracle Eloqua Base Connection",
      "description": "Base Connection for Oracle Eloqua",
      "auth": {
          "specName": "Basic Authentication",
          "params": {
              "endpoint": "{ENDPOINT}",
              "username": "{USERNAME}",
              "password": "{PASSWORD}"
          }
      },
      "connectionSpec": {
          "id": "35d6c4d8-c9a9-11eb-b8bc-0242ac130003",
          "version": "1.0"
      }
  }'
```

Parameter
Description
name
The name of your Oracle Eloqua base connection. It is recommended to provide a descriptive name as you can use this value to look up your base connection.
description
(Optional) A property that you can include to provide supplementary information on your base connection.
auth.specName
The authentication type used for the connection.
auth.params.endpoint
The endpoint of your Oracle Eloqua server.
auth.params.username
The concatenated credential that includes the site name and username that corresponds with your Oracle Eloqua account.
auth.params.password
The password that corresponds with your Oracle Eloqua account.
connectionSpec.id
The value for the connection specification ID of the Oracle Eloqua source is fixed as:
35d6c4d8-c9a9-11eb-b8bc-0242ac130003
.
**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id). This ID is required in the next step to create a source connection.

```
{
    "id": "2484f2df-c057-4ab5-84f2-dfc0577ab592",
    "etag": "\"10033e77-0000-0200-0000-5e96785b0000\""
}
```

## Next steps

By following this tutorial, you have created an Oracle Eloqua base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring marketing automation data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/marketing-automation)

recommendation-more-help
