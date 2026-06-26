---
title: "Connect Azure Blob Storage to Experience Platform using the API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/blob"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:34.872383+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Azure Blob Storage to Experience Platform using the API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your Azure Blobg Storage account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

### Gather required credentials

Read the [Azure Blob Storage overview](/en/docs/experience-platform/sources/connectors/cloud-storage/blob#authentication) for information on authentication.

## Connect your Azure Blob Storage account to Experience Platform connect

Read the steps below for information on how to connect your Azure Blob Storage account to Experience Platform.

### Create a base connection

NOTE
Once created, you cannot change the authentication type of a Azure Blob Storage base connection. To change the authentication type, you must create a new base connection.
A base connection links your source to Experience Platform, storing authentication details, connection status, and a unique ID. Use this ID to browse source files and identify specific items to ingest, including their data types and formats.

You can connect your Azure Blob Storage account to Experience Platform using the following authentication types:

- **Account key authentication**: Uses the storage account’s access key to authenticate and connect to your Azure Blob Storage account.
- **Shared access signature (SAS)**: Uses a SAS URI to provide delegated, time-limited access to resources in your Azure Blob Storage account.
- **Service principal based authentication**: Uses an Azure Active Directory (AAD) service principal (client ID and secret) to securely authenticate to your Azure Blob Storage account.

**API format**

```
POST /connections
```

To create a base connection ID, make a POST request to the /connections endpoint and provide your authentication credentials as part of the request parameters.

Account key authentication
To use account key authentication, provide values for your connectionString, container, and folderPath.

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Blob Storage connection using connectingString", "description": "Azure Blob Storage connection using connectionString", "auth": { "specName": "ConnectionString", "params": { "connectionString": "DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY}", "container": "acme-blob-container", "folderPath": "/acme/customers/salesData" } }, "connectionSpec": { "id": "4c10e202-c428-4796-9208-5f1f5732b1cf", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Parameter | Description |
| connectionString | The connection string for your Azure Blob Storage account. The connection string pattern is: DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY};EndpointSuffix=core.windows.net. |
| container | The name of the Azure Blob Storage container where your data files are stored. |
| folderPath | The path within the specified container where your files are located. |
| connectionSpec.id | The connection spec ID of the Azure Blob Storage source. This ID is fixed as: 4c10e202-c428-4796-9208-5f1f5732b1cf. |

Shared access signature
To use shared access signature, provide values for your sasUri, container, and folderPath.

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Blob Storage source connection using SAS URI", "description": "Azure Blob Storage source connection using SAS URI", "auth": { "specName": "SAS URI Authentication", "params": { "sasUri": "https://{ACCOUNT_NAME}.blob.core.windows.net/?sv={STORAGE_VERSION}&st={START_TIME}&se={EXPIRE_TIME}&sr={RESOURCE}&sp={PERMISSIONS}>&sip=<{IP_RANGE}>&spr={PROTOCOL}&sig={SIGNATURE}>", "container": "acme-blob-container", "folderPath": "/acme/customers/salesData" } }, "connectionSpec": { "id": "4c10e202-c428-4796-9208-5f1f5732b1cf", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Parameter | Description |
| sasUri | The shared access signature URI that you can use as an alternative authentication type to connect your account. The SAS URI pattern is: https://{ACCOUNT_NAME}.blob.core.windows.net/?sv={STORAGE_VERSION}&st={START_TIME}&se={EXPIRE_TIME}&sr={RESOURCE}&sp={PERMISSIONS}>&sip=<{IP_RANGE}>&spr={PROTOCOL}&sig={SIGNATURE}. |
| container | The name of the Azure Blob Storage container where your data files are stored. |
| folderPath | The path within the specified container where your files are located. |
| connectionSpec.id | The connection spec ID of the Azure Blob Storage source. This ID is fixed as: 4c10e202-c428-4796-9208-5f1f5732b1cf. |

Service principal based authentication
To connect via service principal based authentication, provide values for your: serviceEndpoint, servicePrincipalId, servicePrincipalKey, accountKind, tenant, container, and folderPath.

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Blob Storage source connection using service principal based authentication", "description": "Azure Blob Storage source connection using service principal based authentication", "auth": { "specName": "Service Principal Based Authentication", "params": { "serviceEndpoint": "{SERVICE_ENDPOINT}", "servicePrincipalId": "{SERVICE_PRINCIPAL_ID}", "servicePrincipalKey": "{SERVICE_PRINCIPAL_KEY}", "accountKind": "{ACCOUNT_KIND}", "tenant": "{TENANT}", "container": "acme-blob-container", "folderPath": "/acme/customers/salesData" } }, "connectionSpec": { "id": "4c10e202-c428-4796-9208-5f1f5732b1cf", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 |  |
| --- | --- |
| Parameter | Description |
| serviceEndpoint | The endpoint URL of your Azure Blob Storage account. Typically in the format: https://{ACCOUNT_NAME}.blob.core.windows.net. |
| servicePrincipalId | The client/application ID of the Azure Active Directory (AAD) service principal used for authentication. |
| servicePrincipalKey | The client secret or password associated with the Azure service principal. |
| accountKind | The type of your Azure Blob Storage account. Common values include Storage (general purpose V1), StorageV2 (general purpose V2), BlobStorage, and BlockBlobStorage. |
| tenant | The Azure Active Directory (AAD) tenant ID where the service principal is registered. |
| container | The name of the Azure Blob Storage container where your data files are stored. |
| folderPath | The path within the specified container where your files are located. |
| connectionSpec.id | The connection spec ID of the Azure Blob Storage source. This ID is fixed as: 4c10e202-c428-4796-9208-5f1f5732b1cf. |

A successful response returns details of the newly created base connection, including its unique identifier (id). This ID is required in the next step to create a source connection.

```
{
    "id": "4cb0c374-d3bb-4557-b139-5712880adc55",
    "etag": "\"1700c57b-0000-0200-0000-5e3b3f440000\""
}
```

## Next steps

By following this tutorial, you have created a Blob connection using APIs and a unique ID was obtained as part of the response body. You can use this connection ID to [explore cloud storages using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage).

recommendation-more-help
