---
title: "Create a Square base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/payments/square"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:38:26.262411+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Square base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for Square using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Square using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with Square, you must provide values for the following connection properties:

Credential
Description
host
The URL of the Square instance.
clientId
The client ID associated with your Square account.
clientSecret
The client secret associated with your Square account.
accessToken
The access token is used to authenticate your Square account with OAuth 2.0 authentication. The access token can be obtained from Square.
refreshToken
The refresh token is used to generate new access tokens once your current access token expires. The refresh token can be obtained from Square.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Square is:
2acf109f-9b66-4d5e-bc18-ebb2adcff8d5
For more information on these credentials and how to obtain them, see the [Square documentation on OAuth](https://developer.squareup.com/docs/oauth-api/receive-and-manage-tokens).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Square authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Square:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "Square Base Connection",
        "description": "Square Base Connection",
        "auth": {
        "specName": "OAuth2 Refresh Code",
        "params": {
            "host": "{HOST}",
            "clientId": "{CLIENT_ID}",
            "clientSecret": "{CLIENT_SECRET}"
            "accessToken": "{ACCESS_TOKEN}"
            "refreshToken": "{REFRESH_TOKEN}"
            }
        },
        "connectionSpec": {
            "id": "2acf109f-9b66-4d5e-bc18-ebb2adcff8d5",
            "version": "1.0"
        }
    }'
```

Property
Description
auth.params.host
The URL of the Square instance.
auth.params.clientId
The client ID associated with your Square account.
auth.params.clientSecret
The client secret associated with your Square account.
auth.params.accessToken
The access token is used to authenticate your Square account with OAuth 2.0 authentication. The access token can be obtained from Square.
auth.params.refreshToken
The refresh token is used to generate new access tokens once your current access token expires. The refresh token can be obtained from Square.
connectionSpec.id
The Square connection specification ID:
2acf109f-9b66-4d5e-bc18-ebb2adcff8d5
.
**Response**

A successful response returns the newly created connection, including its unique connection identifier (id). This ID is required to explore your data in the next tutorial.

```
{
    "id": "24151d58-ffa7-4960-951d-58ffa7396097",
    "etag": "\"65015e9d-0000-0200-0000-5e89162d0000\""
}
```

## Next steps

By following this tutorial, you have created a Square connection using the Flow Service API and have obtained the connection’s unique ID value. You can use this ID in the next tutorial as you learn how to [explore payments application using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/payments).

recommendation-more-help
