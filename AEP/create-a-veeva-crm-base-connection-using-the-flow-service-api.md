---
title: "Create a Veeva CRM base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/crm/veeva"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:52.072413+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Veeva CRM base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Veeva CRM using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting Started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you need to know in order to successfully connect to Veeva CRM using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with Veeva CRM, you must provide values for the following connection properties:

Credential
Description
environmentUrl
The URL of your Veeva CRM instance.
username
The username value of your Veeva CRM account.
password
The password value of your Veeva CRM account.
securityToken
The security token for your Veeva CRM instance.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Veeva CRM is:
fcad62f3-09b0-41d3-be11-449d5a621b69
.
For more information about these values, refer to this [Veeva CRM document](https://developer.veevacrm.com/doc/Content/rest-api.htm).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Veeva CRM authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Veeva CRM:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json'
    -d '{
        "name": "Veeva CRM base connection",
        "description": "Base Connection for Veeva CRM",
        "auth": {
            "specName": "Basic Authentication",
            "params": {
                "environmentUrl": "{ENVIRONMENT_URL}",
                "username": "{USERNAME}",
                "password": "{PASSWORD}",
                "securityToken": "{SECURITY_TOKEN}"
            }
        },
        "connectionSpec": {
            "id": "fcad62f3-09b0-41d3-be11-449d5a621b69",
            "version": "1.0"
        }
    }'
```

Parameter
Description
name
The name of your Veeva CRM base connection. You can use this name to lookup your Veeva CRM base connection.
description
An optional description for your Veeva CRM base connection.
auth.specName
The authentication type used for the connection.
auth.params.environmentUrl
The URL of your Veeva CRM instance.
auth.params.username
The username value of your Veeva CRM account.
auth.params.password
The password value of your Veeva CRM account.
auth.params.securityToken
The security token for your Veeva CRM instance.
connectionSpec.id
The connection specification ID for Veeva CRM:
fcad62f3-09b0-41d3-be11-449d5a621b69
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

## Next steps

By following this tutorial, you have created a Veeva CRM base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring CRM data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/crm)

recommendation-more-help
