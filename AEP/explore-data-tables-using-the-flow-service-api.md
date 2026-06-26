---
title: "Explore data tables using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/explore/tabular"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:00:14.065917+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Explore data tables using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps on how to explore and preview the structure and contents of your data tables using the [Flow Service](https://www.adobe.io/experience-platform-apis/references/flow-service/) API.

NOTE
In order to explore your data tables, you must already have a valid base connection ID for a tabular source. If you do not have this ID, then see the following tutorials for steps on how to create a base connection ID for a tabular source:
- [Advertising](/en/docs/experience-platform/sources/home#advertising)
- [CRM](/en/docs/experience-platform/sources/home#customer-relationship-management)
- [Customer success](/en/docs/experience-platform/sources/home#customer-success)
- [Database](/en/docs/experience-platform/sources/home#database)
- [E-commerce](/en/docs/experience-platform/sources/home#ecommerce)
- [Marketing automation](/en/docs/experience-platform/sources/home#marketing-automation)
- [Payments](/en/docs/experience-platform/sources/home#payments)
- [Protocols](/en/docs/experience-platform/sources/home#protocols)

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Explore your data tables

You can retrieve information on the structure of your data tables by making a GET request to the Flow Service API while providing the base connection ID of your source.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=root
```

Parameter
Description
{BASE_CONNECTION_ID}
The base connection ID of your source.
**Request**

```
curl -X GET \
  'https://platform.adobe.io/data/foundation/flowservice/connections/5e73e5a2-dc36-45a8-9f16-93c7a43af318/explore?objectType=root' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns an array of tables from your source. Find the table you wish to bring into Experience Platform and take note of its path property, as you are required to provide it in the next step to inspect its structure.

```
[
    {
        "type": "table",
        "name": "ACME Spring Campaign",
        "path": "acmeSpringCampaign",
        "canPreview": true,
        "canFetchSchema": true
    },
    {
        "type": "table",
        "name": "ACME Summer Campaign",
        "path": "acmeSummerCampaign",
        "canPreview": true,
        "canFetchSchema": true
    }
]
```

## Inspect the structure of a table

To inspect the contents of your data tables, perform a GET request to the Flow Service API while specifying the path of a table as a query parameter.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=table&object={TABLE_PATH}
```

Parameter
Description
{BASE_CONNECTION_ID}
The base connection ID of your source.
{TABLE_PATH}
The path property of the table you want to inspect.
**Request**

```
curl -X GET \
  'https://platform.adobe.io/data/foundation/flowservice/connections/5e73e5a2-dc36-45a8-9f16-93c7a43af318/explore?objectType=table&object=acmeSpringCampaign' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {IMS_ORG}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns information on the contents and structure of the specified table. Details regarding each of the table’s columns are located within elements of the columns array.

```
{
  "format": "flat",
  "schema": {
    "columns": [
      {
        "name": "TestID",
        "type": "string",
        "xdm": {
          "type": "string"
        }
      },
      {
        "name": "Name",
        "type": "string",
        "xdm": {
          "type": "string"
        }
      },
      {
        "name": "Datefield",
        "type": "string",
        "meta:xdmType": "date-time",
        "xdm": {
          "type": "string",
          "format": "date-time"
        }
      },
      {
        "name": "complaint_type",
        "type": "string",
        "xdm": {
          "type": "string"
        }
      },
      {
        "name": "complaint_description",
        "type": "string",
        "xdm": {
          "type": "string"
        }
      },
      {
        "name": "status",
        "type": "string",
        "xdm": {
          "type": "string"
        }
      },
      {
        "name": "status_change_date",
        "type": "string",
        "meta:xdmType": "date-time",
        "xdm": {
          "type": "string",
          "format": "date-time"
        }
      },
      {
        "name": "city",
        "type": "string",
        "xdm": {
          "type": "string"
        }
      },
      {
        "name": "Datefield2",
        "type": "string",
        "meta:xdmType": "date-time",
        "xdm": {
          "type": "string",
          "format": "date-time"
        }
      }
    ]
  }
}
```

## Next steps

By following this tutorial, you have gathered information on the structure and contents of your data tables. Furthermore, you have retrieved the path to the table that you wish to ingest into Experience Platform. You can use this information to create a source connection and a dataflow to bring your data to Experience Platform. See the following tutorials for specific steps on how to create a source connection and a dataflow using the Flow Service API:

- [Advertising sources](/en/docs/experience-platform/sources/api-tutorials/collect/advertising)
- [CRM sources](/en/docs/experience-platform/sources/api-tutorials/collect/crm)
- [Customer success sources](/en/docs/experience-platform/sources/api-tutorials/collect/customer-success)
- [Database sources](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)
- [E-commerce sources](/en/docs/experience-platform/sources/api-tutorials/collect/ecommerce)
- [Marketing automation sources](/en/docs/experience-platform/sources/api-tutorials/collect/marketing-automation)
- [Payments sources](/en/docs/experience-platform/sources/api-tutorials/collect/payments)
- [Protocols sources](/en/docs/experience-platform/sources/api-tutorials/collect/protocols)

recommendation-more-help
