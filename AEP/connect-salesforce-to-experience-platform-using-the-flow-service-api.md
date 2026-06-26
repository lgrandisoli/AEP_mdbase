---
title: "Connect Salesforce to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/crm/salesforce"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:49.613605+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Salesforce to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how you can connect your Salesforce source account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Connect Salesforce to Experience Platform on Azure azure

Read the steps below for information on how to connect your Salesforce source to Experience PLatform on Azure.

### Gather required credentials

The Salesforce source supports authentication via OAuth2 Client Credential.

To connect your Salesforce account to Flow Service using OAuth 2 Client Credential, provide values for the following credentials:

Credential
Description
environmentUrl
The URL of the Salesforce source instance. The format for
environmentUrl
is
https://[domain].my.salesforce.com
clientId
The client ID is used in tandem with the client secret as part of OAuth2 authentication. Together, the client ID and client secret enable your application to operate on behalf of your account by identifying your application to Salesforce.
clientSecret
The client secret is used in tandem with the client ID as part of OAuth2 authentication. Together, the client ID and client secret enable your application to operate on behalf of your account by identifying your application to Salesforce.
apiVersion
The REST API version of the Salesforce instance that you are using. The value for the API version must be formatted with a decimal. For example, if you are using API version
52
, then you must input the value as
52.0
. If this field is left blank, then Experience Platform will automatically use the latest available version. This value is mandatory for OAuth2 Client Credential authentication.
includeDeletedObjects
A boolean value used to determine whether to include soft deleted records. If set to true, soft-deleted records can be included in your Salesforce query and ingested from your account into Experience Platform. If you do not specify your configuration, this value defaults to
false
.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Salesforce is:
cfc0fee1-7dc0-40ef-b73e-d8b134c436f5
.
For more information on using OAuth for Salesforce, read the [Salesforce guide on OAuth Authorization Flows](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5).

### Create a base connection for Salesforce in Experience Platform on Azure

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection and connect your Salesforce account to Experience Platform on Azure, make a POST request to the /connections endpoint and provide your Salesforce authentication credentials in the request body.

**API format**

```
POST /connections
```

Select to view request
The following request creates a base connection for Salesforce using OAuth 2 Client Credential:

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "ACME Salesforce account", "description": "Salesforce account using OAuth 2", "auth": { "specName": "OAuth2 Client Credential", "params": "environmentUrl": "https://acme-enterprise-3126.my.salesforce.com", "clientId": "xxxx", "clientSecret": "xxxx", "apiVersion": "60.0", "includeDeletedObjects": true } }, "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.environmentUrl | The URL of your Salesforce instance. |
| auth.params.clientId | The client ID associated with your Salesforce account. |
| auth.params.clientSecret | The client secret associated with your Salesforce account. |
| auth.params.apiVersion | The REST API version of the Salesforce instance that you are using. |
| auth.params.includeDeletedObjects | A boolean value used to determine whether or not to include soft deleted records. |
| connectionSpec.id | The Salesforce connection specification ID: cfc0fee1-7dc0-40ef-b73e-d8b134c436f5. |

Select to view response
A successful response returns your newly created base connection along with its unique ID.

| code language-json |
| --- |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700df7b-0000-0200-0000-5e3b424f0000\"" } |

## Connect Salesforce to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your Salesforce source to Experience Platform on AWS.

### Prerequisites

For information on how to set up your Salesforce account to be able to connect to Experience Platform on AWS, read the [Salesforce overview](/en/docs/experience-platform/sources/connectors/crm/salesforce#aws).

### Create a base connection for Salesforce on Experience Platform on AWS

To create a base connection and connect your Salesforce account to Experience Platform on AWS, make a POST request to the /connections endpoint and provide the appropriate values for your credentials.

**API format**

```
POST /connections
```

**Request**

Select to view request
The following request creates a base connection for the Salesforce source in Experience Platform on AWS.

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'Content-Type: application/json' \ -d '{ "name": "ACME Salesforce account on AWS", "description": "ACME Salesforce account on AWS", "auth": { "specName": "OAuth2 JWT Token Credential", "params": "jwtToken": "{JWT_TOKEN}, "clientId": "xxxx", "clientSecret": "xxxx", "instanceUrl": "https://acme-enterprise-3126.my.salesforce.com" } }, "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" } }' |

For information on how to retrieve your Salesforce jwtToken, read the guide on [how to set up a Salesforce source to connect to Experience Platform on AWS](/en/docs/experience-platform/sources/connectors/crm/salesforce#aws).

**Response**

Select to view response
A successful response returns your newly created base connection along with its unique ID.

| code language-json |
| --- |
| { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "etag": "\"1700df7b-0000-0200-0000-5e3b424f0000\"" } |

### Verify your connection status

To verify your connection status, make a GET request to the /connections endpoint and provide the base connection ID that was generated in the creation step.

**API format**

```
GET /connections
```

**Request**

Select to view request
The following request retrieves information for base connection ID: 3e908d3f-c390-482b-9f44-43d3d4f2eb82.

| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/3e908d3f-c390-482b-9f44-43d3d4f2eb82' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'Content-Type: application/json' \ |

**Response**

Initializing
| accordion |
| --- |
| Select to view response example |
| The following response displays information for base connection ID: 3e908d3f-c390-482b-9f44-43d3d4f2eb82 while in the initializing state. code language-json { "items": [ { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "createdAt": 1736506325115, "updatedAt": 1736506325717, "createdBy": "acme@techacct.adobe.com", "updatedBy": "acme@techacct.adobe.com", "createdClient": "{CREATED_CLIENT}", "updatedClient": "{UPDATED_CLIENT}", "sandboxId": "{SANDBOX_ID}", "sandboxName": "{SANDBOX_NAME}", "imsOrgId": "{ORG_ID}", "name": "JWT Token Auth Authentication E2E-1736506322", "description": "Base Connection for salesforce E2E", "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" }, "state": "initializing", "auth": { "specName": "OAuth2 JWT Token Credential", "params": { "jwtToken": "{JWT_TOKEN}", "clientId": "{CLIENT_ID}", "clientSecret": "{CLIENT_SECRET}", "instanceUrl": "https://acme-enterprise-3126.my.salesforce.com" } } } } ] | code language-json | { "items": [ { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "createdAt": 1736506325115, "updatedAt": 1736506325717, "createdBy": "acme@techacct.adobe.com", "updatedBy": "acme@techacct.adobe.com", "createdClient": "{CREATED_CLIENT}", "updatedClient": "{UPDATED_CLIENT}", "sandboxId": "{SANDBOX_ID}", "sandboxName": "{SANDBOX_NAME}", "imsOrgId": "{ORG_ID}", "name": "JWT Token Auth Authentication E2E-1736506322", "description": "Base Connection for salesforce E2E", "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" }, "state": "initializing", "auth": { "specName": "OAuth2 JWT Token Credential", "params": { "jwtToken": "{JWT_TOKEN}", "clientId": "{CLIENT_ID}", "clientSecret": "{CLIENT_SECRET}", "instanceUrl": "https://acme-enterprise-3126.my.salesforce.com" } } } } ] |
| code language-json |
| { "items": [ { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "createdAt": 1736506325115, "updatedAt": 1736506325717, "createdBy": "acme@techacct.adobe.com", "updatedBy": "acme@techacct.adobe.com", "createdClient": "{CREATED_CLIENT}", "updatedClient": "{UPDATED_CLIENT}", "sandboxId": "{SANDBOX_ID}", "sandboxName": "{SANDBOX_NAME}", "imsOrgId": "{ORG_ID}", "name": "JWT Token Auth Authentication E2E-1736506322", "description": "Base Connection for salesforce E2E", "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" }, "state": "initializing", "auth": { "specName": "OAuth2 JWT Token Credential", "params": { "jwtToken": "{JWT_TOKEN}", "clientId": "{CLIENT_ID}", "clientSecret": "{CLIENT_SECRET}", "instanceUrl": "https://acme-enterprise-3126.my.salesforce.com" } } } } ] |

Enabled
| accordion |
| --- |
| Select to view response example |
| The following response displays information for base connection ID: 3e908d3f-c390-482b-9f44-43d3d4f2eb82 while in the enabled state. code language-json { "items": [ { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "createdAt": 1736506325115, "updatedAt": 1736506413299, "createdBy": "acme@techacct.adobe.com", "updatedBy": "acme@AdobeID", "createdClient": "{CREATED_CLIENT}", "updatedClient": "acme", "sandboxId": "{SANDBOX_ID}", "sandboxName": "{SANDBOX_NAME}", "imsOrgId": "{ORG_ID}", "name": "JWT Token Auth Authentication E2E-1736506322", "description": "Base Connection for salesforce E2E", "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" }, "state": "enabled", "auth": { "specName": "OAuth2 JWT Token Credential", "params": { "jwtToken": "{JWT_TOKEN}", "clientId": "{CLIENT_ID}", "clientSecret": "{CLIENT_SECRET}", "instanceUrl": "https://adb8-dev-ed.develop.my.salesforce.com", "orgId": "00DdL000001iPRxUAM" } }, "version": "\"6d27f305-40be-41c3-97d4-a701827c34df\"", "etag": "\"6d27f305-40be-41c3-97d4-a701827c34df\"" } ] } | code language-json | { "items": [ { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "createdAt": 1736506325115, "updatedAt": 1736506413299, "createdBy": "acme@techacct.adobe.com", "updatedBy": "acme@AdobeID", "createdClient": "{CREATED_CLIENT}", "updatedClient": "acme", "sandboxId": "{SANDBOX_ID}", "sandboxName": "{SANDBOX_NAME}", "imsOrgId": "{ORG_ID}", "name": "JWT Token Auth Authentication E2E-1736506322", "description": "Base Connection for salesforce E2E", "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" }, "state": "enabled", "auth": { "specName": "OAuth2 JWT Token Credential", "params": { "jwtToken": "{JWT_TOKEN}", "clientId": "{CLIENT_ID}", "clientSecret": "{CLIENT_SECRET}", "instanceUrl": "https://adb8-dev-ed.develop.my.salesforce.com", "orgId": "00DdL000001iPRxUAM" } }, "version": "\"6d27f305-40be-41c3-97d4-a701827c34df\"", "etag": "\"6d27f305-40be-41c3-97d4-a701827c34df\"" } ] } |
| code language-json |
| { "items": [ { "id": "3e908d3f-c390-482b-9f44-43d3d4f2eb82", "createdAt": 1736506325115, "updatedAt": 1736506413299, "createdBy": "acme@techacct.adobe.com", "updatedBy": "acme@AdobeID", "createdClient": "{CREATED_CLIENT}", "updatedClient": "acme", "sandboxId": "{SANDBOX_ID}", "sandboxName": "{SANDBOX_NAME}", "imsOrgId": "{ORG_ID}", "name": "JWT Token Auth Authentication E2E-1736506322", "description": "Base Connection for salesforce E2E", "connectionSpec": { "id": "cfc0fee1-7dc0-40ef-b73e-d8b134c436f5", "version": "1.0" }, "state": "enabled", "auth": { "specName": "OAuth2 JWT Token Credential", "params": { "jwtToken": "{JWT_TOKEN}", "clientId": "{CLIENT_ID}", "clientSecret": "{CLIENT_SECRET}", "instanceUrl": "https://adb8-dev-ed.develop.my.salesforce.com", "orgId": "00DdL000001iPRxUAM" } }, "version": "\"6d27f305-40be-41c3-97d4-a701827c34df\"", "etag": "\"6d27f305-40be-41c3-97d4-a701827c34df\"" } ] } |

## Next steps

By following this tutorial, you have created a Salesforce base connection using the Flow Service API. You can use this base connection ID in the following tutorials:

- [Explore the structure and contents of your data tables using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/tabular)
- [Create a dataflow to bring CRM data to Experience Platform using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/crm)

recommendation-more-help
