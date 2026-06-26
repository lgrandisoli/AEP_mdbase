---
title: "Update accounts using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/update"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:06:25.905219+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Update accounts using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

In some circumstances, it may be required to update the details of an existing base connection. Flow Service provides you with the ability to add, edit, and delete details of an existing batch or streaming connection, including its name, description, and credentials.

This tutorial covers the steps for updating the details and credentials of a connection using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

TIP
You do not need to create a new base connection when an update is required. Any changes you make to your base connection are reflected in the associated dataflow.
## Getting started

This tutorial requires you to have an existing connection and a valid connection ID. If you do not have an existing connection, select your source of choice from the [sources overview](/en/docs/experience-platform/sources/home) and follow the steps outlined before attempting this tutorial.

This tutorial also requires you to have a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Look up connection details

The first step in updating your connection is to retrieve its details using your connection ID. To retrieve your connection’s current details make a GET request to the Flow Service API while providing the connection ID, of the connection you want to update.

**API format**

```
GET /connections/{CONNECTION_ID}
```

Parameter
Description
{CONNECTION_ID}
The unique
id
value for the connection you want to retrieve.
**Request**

The following request retrieves information regarding your connection.

```
curl -X GET \
    'https://platform.adobe.io/data/foundation/flowservice/connections/139f6a5f-a78b-4744-9f6a-5fa78bd74431' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the current details of your connection including its credentials, unique identifier (id), and version. The version value is required to update your connection.

```
{
    "items": [
        {
            "createdAt": 1597973312000,
            "updatedAt": 1597973312000,
            "createdBy": "{CREATED_BY}",
            "updatedBy": "{UPDATED_BY}",
            "createdClient": "{CREATED_CLIENT}",
            "updatedClient": "{UPDATED_CLIENT}",
            "sandboxName": "{SANDBOX_NAME}",
            "id": "139f6a5f-a78b-4744-9f6a-5fa78bd74431",
            "name": "E2E_SF Base_Connection",
            "connectionSpec": {
                "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5",
                "version": "1.0"
            },
            "state": "enabled",
            "auth": {
                "specName": "Basic Authentication",
                "params": {
                    "securityToken": "{SECURITY_TOKEN}",
                    "password": "{PASSWORD}",
                    "username": "my-salesforce-account",
                    "environmentUrl": "login.salesforce.com"
                }
            },
            "version": "\"1400dd53-0000-0200-0000-5f3f23450000\"",
            "etag": "\"1400dd53-0000-0200-0000-5f3f23450000\""
        }
    ]
}
```

## Update connection

To update your connection’s name, description, and credentials, perform a PATCH request to the Flow Service API while providing your connection ID, version, and the new information you want to use.

IMPORTANT
The
If-Match
header is required when making a PATCH request. The value for this header is the unique version of the connection you want to update.
**API format**

```
PATCH /connections/{CONNECTION_ID}
```

Parameter
Description
{CONNECTION_ID}
The unique
id
value for the connection you want to update.
**Request**

The following request provides a new name and description, as well as a new set of credentials, to update your connection with.

```
curl -X PATCH \
    'https://platform.adobe.io/data/foundation/flowservice/connections/139f6a5f-a78b-4744-9f6a-5fa78bd74431' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
    -H 'If-Match: 1400dd53-0000-0200-0000-5f3f23450000' \
    -d '[
        {
            "op": "replace",
            "path": "/auth/params",
            "value": {
                "username": "salesforce-connector-username",
                "password": "{NEW_PASSWORD}",
                "securityToken": "{NEW_SECURITY_TOKEN}"
            }
        },
        {
            "op": "replace",
            "path": "/name",
            "value": "Test salesforce connection"
        },
        {
            "op": "add",
            "path": "/description",
            "value": "A test salesforce connection"
        }
    ]'
```

Parameter
Description
op
The operation call used to define the action needed to update the connection. Operations include:
add
,
replace
, and
remove
.
path
The path of the parameter to be updated.
value
The new value you want to update your parameter with.
**Response**

A successful response returns your connection ID and an updated etag. You can verify the update by making a GET request to the Flow Service API, while providing your connection ID.

```
{
    "id": "139f6a5f-a78b-4744-9f6a-5fa78bd74431",
    "etag": "\"3600e378-0000-0200-0000-5f40212f0000\""
}
```

## Next steps

By following this tutorial, you have updated the credentials and information associated with your connection using the Flow Service API. For more information on using source connectors, see the [sources overview](/en/docs/experience-platform/sources/home).

recommendation-more-help
