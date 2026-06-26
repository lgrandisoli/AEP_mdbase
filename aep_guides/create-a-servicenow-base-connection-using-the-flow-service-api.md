---
title: "Create a ServiceNow base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/customer-success/servicenow"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:10.939292+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a ServiceNow base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Google ServiceNow using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to a ServiceNow server using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect to ServiceNow, you must provide values for the following connection properties:

Credential
Description
endpoint
The endpoint of the ServiceNow server.
username
The username used to connect to the ServiceNow server for authentication.
password
The password to connect to the ServiceNow server for authentication.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for ServiceNow is:
eb13cb25-47ab-407f-ba89-c0125281c563
.
For more information about getting started, refer to [this ServiceNow document](https://developer.servicenow.com/app.do#!/rest_api_doc?v=newyork&id=r_TableAPI-GET).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your ServiceNow authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for ServiceNow:

```
curl -X POST \
    'http://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Connection for service-now",
        "description": "Connection for service-now,
        "auth": {
            "specName": "Basic Authentication",
            "params": {
                "endpoint": "{ENDPOINT}",
                "username": "{USERNAME}",
                "password": "{PASSWORD}"
            }
        },
        "connectionSpec": {
            "id": "eb13cb25-47ab-407f-ba89-c0125281c563",
            "version": "1.0"
        }
    }'
```

Parameter
Description
auth.params.server
The endpoint of your ServiceNow server.
auth.params.username
The username used to connect to the ServiceNow server for authentication.
auth.params.password
The password to connect to the ServiceNow server for authentication.
connectionSpec.id
The ServiceNow connection specification ID:
eb13cb25-47ab-407f-ba89-c0125281c563
**Response**

A successful response returns the newly created connection, including its unique identifier (id). This ID is required to explore your CRM system in the next step.

```
{
    "id": "8a3ca3dd-6d00-4c95-bca3-dd6d00dc954b",
    "etag": "\"8e0052a2-0000-0200-0000-5e25fb330000\""
}
```

## Next steps

By following this tutorial, you have created a ServiceNow base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring customer success data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/customer-success)

recommendation-more-help
