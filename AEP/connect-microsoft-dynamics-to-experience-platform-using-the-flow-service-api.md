---
title: "Connect Microsoft Dynamics to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/crm/ms-dynamics"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:46.730460+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Microsoft Dynamics to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how you can connect your Microsoft Dynamics source to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

The following sections provide additional information that you will need to know in order to successfully connect Experience Platform to a Dynamics account using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect to Dynamics, you must provide values for the following connection properties:

Basic authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Credential | Description |
| serviceUri | The service URL of your Dynamics instance. |
| username | The user name for your Dynamics user account. |
| password | The password for your Dynamics account. |

Service-principal and key authentication
| table 0-row-2 1-row-2 2-row-2 |  |
| --- | --- |
| Credential | Description |
| servicePrincipalId | The client ID of your Dynamics account. This ID is required when using service principal and key-based authentication. |
| servicePrincipalKey | The service principal secret key. This credential is required when using service principal and key-based authentication. |

For more information on getting started, refer to [this Dynamics document](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/authenticate-oauth).

## Create a base connection

TIP
Once created, you cannot change the authentication type of a Dynamics base connection. To change the authentication type, you must create a new base connection.
A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Dynamics authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

Basic authentication
To create a Dynamics base connection using basic authentication, make a POST request to the Flow Service API while providing values for your connection’s serviceUri, username, and password.

**Request**

The following request creates a base connection for a Dynamics source using basic authentication.

| accordion |
| --- |
| Select to view request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics connection", "description": "Dynamics connection using basic auth", "auth": { "specName": "Basic Authentication for Dynamics-Online", "params": { "serviceUri": "{SERVICE_URI}", "username": "{USERNAME}", "password": "{PASSWORD}" } }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Property Description auth.params.serviceUri The service URI associated with your Dynamics instance. auth.params.username The username associated with your Dynamics account. auth.params.password The password associated with your Dynamics account. connectionSpec.id The Dynamics connection specification ID: 38ad80fe-8b06-4938-94f4-d4ee80266b07 | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics connection", "description": "Dynamics connection using basic auth", "auth": { "specName": "Basic Authentication for Dynamics-Online", "params": { "serviceUri": "{SERVICE_URI}", "username": "{USERNAME}", "password": "{PASSWORD}" } }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  | Property | Description | auth.params.serviceUri | The service URI associated with your Dynamics instance. | auth.params.username | The username associated with your Dynamics account. | auth.params.password | The password associated with your Dynamics account. | connectionSpec.id | The Dynamics connection specification ID: 38ad80fe-8b06-4938-94f4-d4ee80266b07 |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics connection", "description": "Dynamics connection using basic auth", "auth": { "specName": "Basic Authentication for Dynamics-Online", "params": { "serviceUri": "{SERVICE_URI}", "username": "{USERNAME}", "password": "{PASSWORD}" } }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| Property | Description |
| auth.params.serviceUri | The service URI associated with your Dynamics instance. |
| auth.params.username | The username associated with your Dynamics account. |
| auth.params.password | The password associated with your Dynamics account. |
| connectionSpec.id | The Dynamics connection specification ID: 38ad80fe-8b06-4938-94f4-d4ee80266b07 |

**Response**

A successful response returns the newly created base connection, including its unique identifier (id).

| accordion |
| --- |
| Select to view response example |
| code language-json { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"9e0052a2-0000-0200-0000-5e35tb330000\"" } | code language-json | { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"9e0052a2-0000-0200-0000-5e35tb330000\"" } |
| code language-json |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"9e0052a2-0000-0200-0000-5e35tb330000\"" } |

Service principal key-based authentication
To create a Dynamics base connection using service principal key-based authentication, make a POST request to the Flow Service API while providing values for your connection’s serviceUri, servicePrincipalId, and servicePrincipalKey.

**Request**

The following request creates a base connection for a Dynamics source using basic service principal key-based authentication.

| accordion |
| --- |
| Select to view request example |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics connection", "description": "Dynamics connection using key-based authentication", "auth": { "specName": "Service Principal Key Based Authentication", "params": { "serviceUri": "{SERVICE_URI}", "servicePrincipalId": "{SERVICE_PRINCIPAL_ID}", "servicePrincipalKey": "{SERVICE_PRINCIPAL_KEY}" } }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Property Description auth.params.serviceUri The service URI associated with your Dynamics instance. auth.params.servicePrincipalId The client ID of your Dynamics account. This ID is required when using service principal and key-based authentication. auth.params.servicePrincipalKey The service principal secret key. This credential is required when using service principal and key-based authentication. connectionSpec.id The Dynamics connection specification ID: 38ad80fe-8b06-4938-94f4-d4ee80266b07 | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics connection", "description": "Dynamics connection using key-based authentication", "auth": { "specName": "Service Principal Key Based Authentication", "params": { "serviceUri": "{SERVICE_URI}", "servicePrincipalId": "{SERVICE_PRINCIPAL_ID}", "servicePrincipalKey": "{SERVICE_PRINCIPAL_KEY}" } }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  | Property | Description | auth.params.serviceUri | The service URI associated with your Dynamics instance. | auth.params.servicePrincipalId | The client ID of your Dynamics account. This ID is required when using service principal and key-based authentication. | auth.params.servicePrincipalKey | The service principal secret key. This credential is required when using service principal and key-based authentication. | connectionSpec.id | The Dynamics connection specification ID: 38ad80fe-8b06-4938-94f4-d4ee80266b07 |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics connection", "description": "Dynamics connection using key-based authentication", "auth": { "specName": "Service Principal Key Based Authentication", "params": { "serviceUri": "{SERVICE_URI}", "servicePrincipalId": "{SERVICE_PRINCIPAL_ID}", "servicePrincipalKey": "{SERVICE_PRINCIPAL_KEY}" } }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| Property | Description |
| auth.params.serviceUri | The service URI associated with your Dynamics instance. |
| auth.params.servicePrincipalId | The client ID of your Dynamics account. This ID is required when using service principal and key-based authentication. |
| auth.params.servicePrincipalKey | The service principal secret key. This credential is required when using service principal and key-based authentication. |
| connectionSpec.id | The Dynamics connection specification ID: 38ad80fe-8b06-4938-94f4-d4ee80266b07 |

**Response**

A successful response returns the newly created connection, including its unique identifier (id).

| accordion |
| --- |
| Select to view response example |
| code language-json { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"9e0052a2-0000-0200-0000-5e35tb330000\"" } | code language-json | { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"9e0052a2-0000-0200-0000-5e35tb330000\"" } |
| code language-json |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"9e0052a2-0000-0200-0000-5e35tb330000\"" } |

## Explore your data tables

To explore your Dynamics data tables, make a GET request to the /connections/{BASE_CONNECTION_ID}/explore endpoint and provide your base connection ID as part of the query parameters.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=root
```

Query parameters
Description
{BASE_CONNECTION_ID}
The ID of the base connection. Use this ID to explore the contents and structure of your source.
**Request**

The following request retrieves the list of available tables and views for a Dynamics source with the base connection ID: dd668808-25da-493f-8782-f3433b976d1e.

Select to view request example
| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/dd668808-25da-493f-8782-f3433b976d1e/explore?objectType=root' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ |

**Response**

A successful response returns the Dynamics tables and views directory at the root level.

Select to view response example
| code language-json |
| --- |
| [ { "type": "table", "name": "systemuserlicenses", "path": "systemuserlicenses", "canPreview": true, "canFetchSchema": true }, { "type": "table", "name": "Process Dependency", "path": "workflowdependency", "canPreview": true, "canFetchSchema": true }, { "type": "view", "name": "accountView1", "path": "accountView1", "canPreview": true, "canFetchSchema": true }, { "type": "view", "name": "Inactive_ACC_custom", "path": "Inactive_ACC_custom", "canPreview": true, "canFetchSchema": true } ] |

### Use primary key to optimize data exploration

NOTE
You can only use non-lookup attributes when using the primary key approach to optimization.
You can optimize your explore queries by providing primaryKey as part of your query parameters. You must specify the primary key of the Dynamics table when including primaryKey as a query parameter.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?preview=true&object={OBJECT}&objectType={OBJECT_TYPE}&previewCount=10&primaryKey={PRIMARY_KEY}
```

Query parameters
Description
{BASE_CONNECTION_ID}
The ID of the base connection. Use this ID to explore the contents and structure of your source.
preview
A boolean value that enables data preview.
{OBJECT}
The Dynamics object that you want to explore.
{OBJECT_TYPE}
The type of the object.
previewCount
A restriction that limits the returned preview to only a certain number of records.
{PRIMARY_KEY}
The primary key of the table that you are retrieving for preview.
**Request**

Select to view request example
| code language-shell |
| --- |
| curl -X GET \ 'https://platform-stage.adobe.io/data/foundation/flowservice/connections/dd668808-25da-493f-8782-f3433b976d1e/explore?preview=true&object=lead&objectType=table&previewCount=10&primaryKey=leadid' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ |

## Inspect the structure of a table

To inspect the structure of a specific table, make a GET request to /connections/{BASE_CONNECTION_ID}/explore and provide the path to the specific table as a query parameter.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?object={TABLE_PATH}&objectType=table
```

Query parameter
Description
{BASE_CONNECTION_ID}
The ID of the base connection. Use this ID to explore the contents and structure of your source.
{TABLE_PATH}
The path to the particular table that you want to explore.
**Request**

The following request retrieves the structure and contents of a Dynamics table with path workflowdependency.

Select to view request example
| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/dd668808-25da-493f-8782-f3433b976d1e/explore?object=workflowdependency&objectType=table' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ |

**Response**

A successful response returns the contents of path workflowdependency.

Select to view response example
| code language-json |
| --- |
| { "format": "flat", "schema": { "columns": [ { "name": "first_name", "type": "string", "meta": { "originalType": "String" } }, { "name": "last_name", "type": "string", "meta": { "originalType": "String" } }, { "name": "email", "type": "string", "meta": { "originalType": "String" } } ] } } |

## Inspect the structure of a view

In Dynamics, a view refers to the columns to display, the width of each column, the default system in which a list of records are sorted, and the default filters applied to restrict which records will appear in the list.

To inspect the structure of a view, make a GET request to /connections/{BASE_CONNECTION_ID}/explore and specify the view path in your query parameters. Additionally, you must specify objectType as view.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?object={VIEW_PATH}&objectType=view
```

Query parameter
Description
{BASE_CONNECTION_ID}
The ID of the base connection. Use this ID to explore the contents and structure of your source.
{VIEW_PATH}
The path to the view that you want to inspect.
**Request**

The following request retrieves accountView1.

Select to view request example
| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/dd668808-25da-493f-8782-f3433b976d1e/explore?object=accountView1&objectType=view' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ |

**Response**

A successful response returns the structure of accountView1.

Select to view response example
| code language-json |
| --- |
| { "format": "flat", "schema": { "columns": [ { "name": "name", "type": "string", "meta": { "originalType": "string" }, "xdm": { "type": "string" } }, { "name": "fetchxml", "type": "string", "meta": { "originalType": "string" }, "xdm": { "type": "string" } }, { "name": "querytype", "type": "integer", "meta": { "originalType": "int" }, "xdm": { "type": "integer", "minimum": -2147483648, "maximum": 2147483647 } }, { "name": "userqueryid", "type": "string", "meta": { "originalType": "guid" }, "xdm": { "type": "string" } } ] } } |

## Preview entity type view

To preview the contents of a view, make a GET request to /connections/{BASE_CONNECTION_ID}/explore and include the view path as well as preview=true in your query parameters.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?object={VIEW_PATH}&preview=true&objectType=view
```

Query parameter
Description
{BASE_CONNECTION_ID}
The ID of the base connection. Use this ID to explore the contents and structure of your source.
{VIEW_PATH}
The path to the view that you want to inspect.
**Request**

The following request previews the contents of accountView1.

Select to view request example
| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/dd668808-25da-493f-8782-f3433b976d1e/explore?object=accountView1&preview=true&objectType=view' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ |

**Response**

A successful response returns the contents of accountView1.

Select to view response example
| code language-json |
| --- |
| { "format": "flat", "schema": { "columns": [ { "name": "emailaddress1", "type": "string", "meta": { "originalType": "string" }, "xdm": { "type": "string" } }, { "name": "contactid", "type": "string", "meta": { "originalType": "guid" }, "xdm": { "type": "string" } }, { "name": "fullname", "type": "string", "meta": { "originalType": "string" }, "xdm": { "type": "string" } } ] }, "data": [ { "contactid": "396e19de-0852-ec11-8c62-00224808a1df", "fullname": "Tim Barr", "emailaddress1": "barrtim@googlemedia.com" } ] } |

## Create a source connection to ingest view

To create a source connection and ingest a view, make a POST request to the /sourceConnections endpoint, provide the table name, and specify entityType as view in the request body.

**API format**

```
POST /sourceConnections
```

**Request**

The following request creates a Dynamics source connection and ingests views.

Select to view request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics Source Connection", "description": "Dynamics Source Connection", "baseConnectionId": "dd668808-25da-493f-8782-f3433b976d1e", "data": { "format": "tabular", "schema": null, "properties": null }, "params": { "tableName": "Contacts with name TIM", "entityType": "view" }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' |

**Response**

A successful response returns the newly generated source connection ID and its corresponding etag.

Select to view response example
| code language-json |
| --- |
| { "id": "e566bab3-1b58-428c-b751-86b8cc79a3b4", "etag": "\"82009592-0000-0200-0000-678121030000\"" } |

### Use primary key to optimize your dataflow

You can also optimize your Dynamics dataflow by specifying the primary key as part of your request body parameters.

**API format**

```
POST /sourceConnections
```

**Request**

The following request creates a Dynamics source connection while specifying the primary key as contactid.

Select to view request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Dynamics Source Connection", "description": "Dynamics Source Connection", "baseConnectionId": "dd668808-25da-493f-8782-f3433b976d1e", "data": { "format": "tabular" }, "params": { "tableName": "contact", "primaryKey": "contactid" }, "connectionSpec": { "id": "38ad80fe-8b06-4938-94f4-d4ee80266b07", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| Property | Description |
| baseConnectionId | The ID of the base connection. |
| data.format | The format of the data. |
| params.tableName | The name of the table in Dynamics. |
| params.primaryKey | The primary key of the table that will optimize queries. |
| connectionSpec.id | The connection spec ID that corresponds with the Dynamics source. |

**Response**

A successful response returns the newly generated source connection ID and its corresponding etag.

Select to view response example
| code language-json |
| --- |
| { "id": "e566bab3-1b58-428c-b751-86b8cc79a3b4", "etag": "\"82009592-0000-0200-0000-678121030000\"" } |

## Next steps

By following this tutorial, you have created a Microsoft Dynamics base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring CRM data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/crm)

recommendation-more-help
