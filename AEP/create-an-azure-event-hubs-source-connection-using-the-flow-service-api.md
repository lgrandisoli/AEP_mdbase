---
title: "Create an Azure Event Hubs source connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/eventhub"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:15.548834+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Create an Azure Event Hubs source connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Azure Event Hubs source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this tutorial to learn how to connect Azure Event Hubs (hereinafter referred to as “Event Hubs”) to Experience Platform, using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect Event Hubs to Experience Platform using the Flow Service API.

### Gather required credentials

In order for Flow Service to connect with your Event Hubs account, you must provide values for the following connection properties:

Standard authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Credential | Description |
| sasKeyName | The name of the authorization rule, which is also known as the SAS key name. |
| sasKey | The primary key of the Event Hubs namespace. The sasPolicy that the sasKey corresponds to must have manage rights configured in order for the Event Hubs list to be populated. |
| namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |
| connectionSpec.id | The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e. |

SAS authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| Credential | Description |
| sasKeyName | The name of the authorization rule, which is also known as the SAS key name. |
| sasKey | The primary key of the Event Hubs namespace. The sasPolicy that the sasKey corresponds to must have manage rights configured in order for the Event Hubs list to be populated. |
| namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |
| eventHubName | Fill in your Azure Event Hub name. Read the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create#create-an-event-hub) for more information on Event Hub names. |
| connectionSpec.id | The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e. |

For more information on shared access signatures (SAS) authentication for Event Hubs, read the [Azure guide on using SAS](https://docs.microsoft.com/en-us/azure/event-hubs/authenticate-shared-access-signature).

Event Hub Azure Active Directory Auth
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Credential | Description |
| tenantId | The tenant ID that you want to request permission from. Your tenant ID can be formatted as a GUID or as a friendly name. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. |
| clientId | The application ID assigned to your app. You can retrieve this ID from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| clientSecretValue | The client secret that is used alongside the client ID to authenticate your app. You can retrieve your client secret from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |

For more information on Azure Active Directory, read the [Azure guide on using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application).

Event Hub Scoped Azure Active Directory Auth
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| Credential | Description |
| tenantId | The tenant ID that you want to request permission from. Your tenant ID can be formatted as a GUID or as a friendly name. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. |
| clientId | The application ID assigned to your app. You can retrieve this ID from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| clientSecretValue | The client secret that is used alongside the client ID to authenticate your app. You can retrieve your client secret from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |
| eventHubName | Fill in your Azure Event Hub name. Read the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create#create-an-event-hub) for more information on Event Hub names. |

For more information about these values, refer to [this Event Hubs document](https://docs.microsoft.com/en-us/azure/event-hubs/authenticate-shared-access-signature).

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

TIP
Once created, you cannot change the authentication type of an Event Hubs base connection. To change the authentication type, you must create a new base connection.
The first step in creating a source connection is to authenticate your Event Hubs source and generate a base connection ID. A base connection ID allows you to explore and navigate files from within your source and identify specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Event Hubs authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

Standard authentication
To create an account using standard authentication, make a POST request to the /connections endpoint while providing values for your sasKeyName, sasKey, and namespace.

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Azure EventHub authentication credentials", "params": { "sasKeyName": "{SAS_KEY_NAME}", "sasKey": "{SAS_KEY}", "namespace": "{NAMESPACE}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Property Description auth.params.sasKeyName The name of the authorization rule, which is also known as the SAS key name. auth.params.sasKey The generated shared access signature. auth.params.namespace The namespace of the Event Hubs you are accessing. connectionSpec.id The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Azure EventHub authentication credentials", "params": { "sasKeyName": "{SAS_KEY_NAME}", "sasKey": "{SAS_KEY}", "namespace": "{NAMESPACE}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  | Property | Description | auth.params.sasKeyName | The name of the authorization rule, which is also known as the SAS key name. | auth.params.sasKey | The generated shared access signature. | auth.params.namespace | The namespace of the Event Hubs you are accessing. | connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Azure EventHub authentication credentials", "params": { "sasKeyName": "{SAS_KEY_NAME}", "sasKey": "{SAS_KEY}", "namespace": "{NAMESPACE}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| Property | Description |
| auth.params.sasKeyName | The name of the authorization rule, which is also known as the SAS key name. |
| auth.params.sasKey | The generated shared access signature. |
| auth.params.namespace | The namespace of the Event Hubs you are accessing. |
| connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created base connection, including its unique identifier ( id ). This connection ID is required in the next step to create a source connection. code language-json { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } | code language-json | { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |
| code language-json |
| { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |

SAS authentication
To create an account using SAS authentication, make a POST request to the /connections endpoint while providing values for your sasKeyName, sasKey,namespace, and eventHubName.

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Azure EventHub authentication credentials", "params": { "sasKeyName": "{SAS_KEY_NAME}", "sasKey": "{SAS_KEY}", "namespace": "{NAMESPACE}", "eventHubName": "{EVENT_HUB_NAME} } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 Property Description auth.params.sasKeyName The name of the authorization rule, which is also known as the SAS key name. auth.params.sasKey The generated shared access signature. auth.params.namespace The namespace of the Event Hubs you are accessing. params.eventHubName The name for your Event Hubs source. connectionSpec.id The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Azure EventHub authentication credentials", "params": { "sasKeyName": "{SAS_KEY_NAME}", "sasKey": "{SAS_KEY}", "namespace": "{NAMESPACE}", "eventHubName": "{EVENT_HUB_NAME} } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  | Property | Description | auth.params.sasKeyName | The name of the authorization rule, which is also known as the SAS key name. | auth.params.sasKey | The generated shared access signature. | auth.params.namespace | The namespace of the Event Hubs you are accessing. | params.eventHubName | The name for your Event Hubs source. | connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Azure EventHub authentication credentials", "params": { "sasKeyName": "{SAS_KEY_NAME}", "sasKey": "{SAS_KEY}", "namespace": "{NAMESPACE}", "eventHubName": "{EVENT_HUB_NAME} } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| Property | Description |
| auth.params.sasKeyName | The name of the authorization rule, which is also known as the SAS key name. |
| auth.params.sasKey | The generated shared access signature. |
| auth.params.namespace | The namespace of the Event Hubs you are accessing. |
| params.eventHubName | The name for your Event Hubs source. |
| connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created base connection, including its unique identifier ( id ). This connection ID is required in the next step to create a source connection. code language-json { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } | code language-json | { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |
| code language-json |
| { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |

Event Hub Azure Active Directory Auth
To create an account using Azure Active Directory Auth, make a POST request to the /connections endpoint while providing values for your tenantId, clientId,clientSecretValue, and namespace.

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Event Hub Azure Active Directory Auth", "params": { "tenantId": "{TENANT_ID}", "clientId": "{CLIENT_ID}", "clientSecretValue": "{CLIENT_SECRET_VALUE}", "namespace": "{NAMESPACE}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 Property Description auth.params.tenantId The tenant ID of your application. Note : The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. auth.params.clientId The client ID of your organization. auth.params.clientSecretValue The client secret value of your organization. auth.params.namespace The namespace of the Event Hubs you are accessing. connectionSpec.id The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Event Hub Azure Active Directory Auth", "params": { "tenantId": "{TENANT_ID}", "clientId": "{CLIENT_ID}", "clientSecretValue": "{CLIENT_SECRET_VALUE}", "namespace": "{NAMESPACE}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  | Property | Description | auth.params.tenantId | The tenant ID of your application. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. | auth.params.clientId | The client ID of your organization. | auth.params.clientSecretValue | The client secret value of your organization. | auth.params.namespace | The namespace of the Event Hubs you are accessing. | connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Event Hub Azure Active Directory Auth", "params": { "tenantId": "{TENANT_ID}", "clientId": "{CLIENT_ID}", "clientSecretValue": "{CLIENT_SECRET_VALUE}", "namespace": "{NAMESPACE}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| Property | Description |
| auth.params.tenantId | The tenant ID of your application. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. |
| auth.params.clientId | The client ID of your organization. |
| auth.params.clientSecretValue | The client secret value of your organization. |
| auth.params.namespace | The namespace of the Event Hubs you are accessing. |
| connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created base connection, including its unique identifier ( id ). This connection ID is required in the next step to create a source connection. code language-json { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } | code language-json | { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |
| code language-json |
| { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |

Event Hub Scoped Azure Active Directory Auth
To create an account using Azure Active Directory Auth, make a POST request to the /connections endpoint while providing values for your tenantId, clientId,clientSecretValue, namespace, and eventHubName.

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Event Hub Scoped Azure Active Directory Auth", "params": { "tenantId": "{TENANT_ID}", "clientId": "{CLIENT_ID}", "clientSecretValue": "{CLIENT_SECRET_VALUE}", "namespace": "{NAMESPACE}", "eventHubName": "{EVENT_HUB_NAME}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Property Description auth.params.tenantId The tenant ID of your application. Note : The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. auth.params.clientId The client ID of your organization. auth.params.clientSecretValue The client secret value of your organization. auth.params.namespace The namespace of the Event Hubs you are accessing. auth.params.eventHubName The name for your Event Hubs source. connectionSpec.id The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Event Hub Scoped Azure Active Directory Auth", "params": { "tenantId": "{TENANT_ID}", "clientId": "{CLIENT_ID}", "clientSecretValue": "{CLIENT_SECRET_VALUE}", "namespace": "{NAMESPACE}", "eventHubName": "{EVENT_HUB_NAME}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  | Property | Description | auth.params.tenantId | The tenant ID of your application. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. | auth.params.clientId | The client ID of your organization. | auth.params.clientSecretValue | The client secret value of your organization. | auth.params.namespace | The namespace of the Event Hubs you are accessing. | auth.params.eventHubName | The name for your Event Hubs source. | connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Azure Event Hubs connection", "description": "Connector for Azure Event Hubs", "auth": { "specName": "Event Hub Scoped Azure Active Directory Auth", "params": { "tenantId": "{TENANT_ID}", "clientId": "{CLIENT_ID}", "clientSecretValue": "{CLIENT_SECRET_VALUE}", "namespace": "{NAMESPACE}", "eventHubName": "{EVENT_HUB_NAME}" } }, "connectionSpec": { "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| Property | Description |
| auth.params.tenantId | The tenant ID of your application. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. |
| auth.params.clientId | The client ID of your organization. |
| auth.params.clientSecretValue | The client secret value of your organization. |
| auth.params.namespace | The namespace of the Event Hubs you are accessing. |
| auth.params.eventHubName | The name for your Event Hubs source. |
| connectionSpec.id | The Event Hubs connection specification ID is: bf9f5905-92b7-48bf-bf20-455bc6b60a4e |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created base connection, including its unique identifier ( id ). This connection ID is required in the next step to create a source connection. code language-json { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } | code language-json | { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |
| code language-json |
| { "id": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |

## Create a source connection

TIP
An Event Hubs consumer group can only be used for a single flow at a given time.
A source connection creates and manages the connection to the external source from where data is ingested. A source connection consists of information like data source, data format, and a source connection ID needed to create a dataflow. A source connection instance is specific to a tenant and organization.

To create a source connection, make a POST request to the /sourceConnections endpoint of the Flow Service API.

**API format**

```
POST /sourceConnections
```

**Request**

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \
  -H 'authorization: Bearer {ACCESS_TOKEN}' \
  -H 'content-type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -d '{
      "name": "Azure Event Hubs source connection",
      "description": "A source connection for Azure Event Hubs",
      "baseConnectionId": "4cdbb15c-fb1e-46ee-8049-0f55b53378fe",
      "connectionSpec": {
          "id": "bf9f5905-92b7-48bf-bf20-455bc6b60a4e",
          "version": "1.0"
      },
      "data": {
          "format": "json"
      },
      "params": {
          "eventHubName": "{EVENT_HUB_NAME}",
          "dataType": "raw",
          "reset": "latest",
          "consumerGroup": "{CONSUMER_GROUP}"
      }
  }'
```

Property
Description
name
The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection.
description
An optional value that you can provide to include more information on your source connection.
baseConnectionId
The connection ID of your Event Hubs source that was generated in the previous step.
connectionSpec.id
The fixed connection specification ID for Event Hubs. This ID is:
bf9f5905-92b7-48bf-bf20-455bc6b60a4e
.
data.format
The format of the Event Hubs data that you want to ingest. Currently, the only supported data format is
json
.
params.eventHubName
The name for your Event Hubs source.
params.dataType
This parameter defines the type of the data that is being ingested. Supported data types include:
raw
and
xdm
.
params.reset
This parameter defines how the data will be read. Use
latest
to start reading from the most recent data, and use
earliest
to start reading from the first available data in the stream. This parameter is optional and defaults to
earliest
if unprovided.
params.consumerGroup
The publish or subscription mechanism to be used for Event Hubs. This parameter is optional and defaults to
$Default
if unprovided. Refer to this
Event Hubs guide on event consumers
for more information.
Note
: An Event Hubs consumer group can only be used for a single flow at a given time.
NOTE
After you create or update a streaming dataflow, a brief 5-minute pause in data ingestion is required to prevent any potential instances of data loss or data drops.
## Next steps

By following this tutorial, you have created an Event Hubs source connection using the Flow Service API. You can use this source connection ID in the next tutorial to [create a streaming dataflow using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/streaming).

recommendation-more-help
