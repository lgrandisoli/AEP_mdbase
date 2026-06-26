---
title: "Create a Microsoft SQL Server base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/databases/sql-server"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:31.778957+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Microsoft SQL Server base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

Read this tutorial to learn how to create a base connection for Microsoft SQL Server using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Microsoft SQL Server using the Flow Service API.

### Gather required credentials gather-required-credentials

In order to connect to Microsoft SQL Server, you must provide the following connection property:

Credential
Description
Example
connectionString
The connection string associated with your Microsoft SQL Server account. Your connection string pattern depends whether you are using server name or instance name for your data source:

- Connection string using server name: Data Source={SERVER_NAME};Initial Catalog={DATABASE};Integrated Security=False;User ID={USER_ID};Password={PASSWORD};
- Connection string using instance name:Data Source={INSTANCE_NAME};Initial Catalog={DATABASE};Integrated Security=False;User ID={USER_ID};Password={PASSWORD};

Data Source=mssqlserver.database.windows.net;Initial Catalog=mssqlserver_e2e_db;Integrated Security=False;User ID=mssqluser;Password=mssqlpassword
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Microsoft SQL Server is
1f372ff9-38a4-4492-96f5-b9a4e4bd00ec
.
For more information about obtaining a connection string, refer to this [Microsoft SQL Server document](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/authentication-in-sql-server).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Microsoft SQL Server authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Microsoft SQL Server:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/connections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "Base connection for sql-server",
      "description": "Base connection for sql-server",
      "auth": {
          "specName": "Connection String Based Authentication",
          "params": {
              "connectionString": "Data Source=mssqlserver.database.windows.net;Initial Catalog=mssqlserver_e2e_db;Integrated Security=False;User ID=mssqluser;Password=mssqlpassword"
          }
      },
      "connectionSpec": {
          "id": "1f372ff9-38a4-4492-96f5-b9a4e4bd00ec",
          "version": "1.0"
  }'
```

Property
Description
auth.params.connectionString
The connection string associated with your Microsoft SQL Server account. Read the section on
gathering required credentials
for more information.
connectionSpec.id
The Microsoft SQL Server connection specification ID is:
1f372ff9-38a4-4492-96f5-b9a4e4bd00ec
.
**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your database in the next tutorial.

```
{
    "id": "0b8224e4-0de8-4293-8224-e40de80293c6",
    "etag": "\"5802c519-0000-0200-0000-5e4d89520000\""
}
```

## Next steps

By following this tutorial, you have created an Microsoft SQL Server base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring database data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql)

recommendation-more-help
