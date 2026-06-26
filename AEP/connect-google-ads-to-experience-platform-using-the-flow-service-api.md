---
title: "Connect Google Ads to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/advertising/ads"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:27.552434+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Google Ads to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

Read this tutorial to learn how to connect your Google Ads account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get Started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Google Ads using the Flow Service API.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

### Gather required credentials

For information on authentication, read the [Google Ads source overview](/en/docs/experience-platform/sources/connectors/advertising/ads).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Google Ads authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Google Ads:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/connections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json'
  -d '{
      "name": "Google Ads base connection",
      "description": "Google Ads base connection",
      "auth": {
          "specName": "Basic Authentication",
          "params": {
              "clientCustomerID": "{CLIENT_CUSTOMER_ID}",
              "loginCustomerID": "{LOGIN_CUSTOMER_ID}",
              "developerToken": "{DEVELOPER_TOKEN}",
              "refreshToken": "{REFRESH_TOKEN}",
              "clientId": "{CLIENT_ID}",
              "clientSecret": "{CLIENT_SECRET}",
              "googleAdsApiVersion": "v19"

          }
      },
      "connectionSpec": {
          "id": "d771e9c1-4f26-40dc-8617-ce58c4b53702",
          "version": "1.0"
      }
  }'
```

Property
Description
auth.params.clientCustomerID
The client customer ID of your Google Ads account.
auth.params.loginCustomerID
The login customer ID that corresponds with your Google Ads manager account.
auth.params.developerToken
The developer token of your Google Ads account.
auth.params.refreshToken
The refresh token of your Google Ads account.
auth.params.clientID
The client ID of your Google Ads account.
auth.params.clientSecret
The client secret of your Google Ads account.
auth.params.googleAdsApiVersion
The Google Ads API version that you are using. Experience Platform currently supports version
v19
and newer. Make sure you’re using one of these supported versions to ensure compatibility.
connectionSpec.id
The Google Ads connection specification ID:
d771e9c1-4f26-40dc-8617-ce58c4b53702
.
**Response**

A successful response returns details of the newly created base connection, including its unique identifier (id). This ID is required in the next step to create a source connection.

```
{
    "id": "2484f2df-c057-4ab5-84f2-dfc0577ab592",
    "etag": "\"10033e77-0000-0200-0000-5e96785b0000\""
}
```

## Create a dataflow to ingest advertising data

By following this tutorial, you have created a Google Ads base connection using the Flow Service API and connected your Google Ads account to Experience Platform. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring advertising data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/advertising)

recommendation-more-help
