---
title: "Create an FTP base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/ftp"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:39.259760+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an FTP base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The FTP connector is in beta. The features and documentation are subject to change. See the
Sources overview
for more information on using beta-labeled connectors.
A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for FTP (File Transfer Protocol) using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to an FTP server using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect to FTP, you must provide values for the following connection properties:

Credential
Description
host
The name or IP address associated with your FTP server.
username
The username with access to your FTP server.
password
The password for your FTP server.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for FTP is:
fb2e94c9-c031-467d-8103-6bd6e0a432f2
.
### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your FTP authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for FTP:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/connections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d  '{
        "name": "FTP connector with password",
        "description": "FTP connector password",
        "auth": {
            "specName": "Basic Authentication for FTP",
            "params": {
                "host": "{HOST}",
                "userName": "{USERNAME}",
                "password": "{PASSWORD}"
            }
        },
        "connectionSpec": {
            "id": "fb2e94c9-c031-467d-8103-6bd6e0a432f2",
            "version": "1.0"
        }
    }'
```

Property
Description
auth.params.host
The host name of your FTP server.
auth.params.username
The username associated with your FTP server.
auth.params.password
The password associated with your FTP server.
connectionSpec.id
The FTP server connection specification ID:
fb2e94c9-c031-467d-8103-6bd6e0a432f2
**Response**

A successful response returns the unique identifier (id) of the newly created connection. This ID is required to explore your FTP server in the next tutorial.

```
{
    "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094",
    "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\""
}
```

## Next steps

By following this tutorial, you have created an FTP connection using the Flow Service API, and have obtained the connection’s unique ID value. You can use this connection ID to [explore cloud storages using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage).

recommendation-more-help
