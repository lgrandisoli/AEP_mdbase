---
title: "Create a Google PubSub Source Connection Using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/google-pubsub"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:21.254756+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Create a Google PubSub Source Connection Using the Flow Service API

Last update: May 25, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Google PubSub source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
This tutorial walks you through the steps to connect Google PubSub (hereinafter referred to as “PubSub”) to Experience Platform, using the [Flow Service API](%5Bhttps://www.adobe.io/experience-platform-apis/references/flow-service/%5D(https://www.adobe.io/experience-platform-apis/references/flow-service/)).

## Get started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect PubSub to Experience Platform using the Flow Service API.

### Gather required credentials

You must provide values for the connection properties outlined below in order to connect your PubSub account to Flow Service. For more information on authentication and prerequisite setup, read the [PubSub source overview](/en/docs/experience-platform/sources/connectors/cloud-storage/google-pubsub#prerequisites).

Project-based authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Credential | Description |
| projectId | The project ID required to authenticate PubSub. |
| credentials | The credential required to authenticate PubSub. You must ensure that you put the complete JSON file after removing the white spaces from your credentials. |
| connectionSpec.id | The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source target connections. The PubSub connection specification ID is: 70116022-a743-464a-bbfe-e226a7f8210c. |

Topic and subscription-based authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Credential | Description |
| credentials | The credential required to authenticate PubSub. You must ensure that you put the complete JSON file after removing the white spaces from your credentials. |
| topicName | The name of the resource that represents a feed of messages. You must specify a topic name if you want to provide access to a specific stream of data in your PubSub source. The topic name format is: projects/{PROJECT_ID}/topics/{TOPIC_ID}. |
| subscriptionName | The name of your PubSub subscription. In PubSub, subscriptions allow you to receive messages, by subscribing to the topic in which messages have been published to. **Note**: A single PubSub subscription can only be used for one dataflow. In order to make multiple dataflows, you must have multiple subscriptions. The subscription name format is: projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}. |
| connectionSpec.id | The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source target connections. The PubSub connection specification ID is: 70116022-a743-464a-bbfe-e226a7f8210c. |

For more information about these values, read this [PubSub authentication](https://cloud.google.com/pubsub/docs/authentication) document. To use service account-based authentication, read this [PubSub guide on creating service accounts](https://cloud.google.com/docs/authentication/production#create_service_account) for steps on how to generate your credentials.

TIP
If you are using service account-based authentication, ensure that you have granted sufficient user access to your service account and that there are no extra white spaces in the JSON, when copying and pasting your credentials.
### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

TIP
Once created, you cannot change the authentication type of a Google PubSub base connection. To change the authentication type, you must create a new base connection.
The first step in creating a source connection is to authenticate your PubSub source and generate a base connection ID. A base connection ID allows you to explore and navigate files from within your source and identify specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your PubSub authentication credentials as part of the request parameters.

The PubSub source allows you to specify the type of access that you want to allow during authentication. You can set up your account to have root access or restrict access to a particular PubSub topic and subscription.

NOTE
Principal (roles) assigned to a PubSub project are inherited in all of the topics and subscriptions created inside a PubSub project. If you want a principal (role) to have access to a specific topic, then that principal (role) must also be added to the topic’s corresponding subscription as well. For more information, read the
PubSub documentation on access control
.
**API format**

```
POST /connections
```

Project-based authentication
To create base connection with project-based authentication, make a POST request to the /connections endpoint and provide your projectId and credentials in the request body.

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google PubSub connection", "description": "Google PubSub connection", "auth": { "specName": "Project Based Authentication", "params": { "projectId": "{PROJECT_ID}", "credentials": "{CREDENTIALS}" } }, "connectionSpec": { "id": "70116022-a743-464a-bbfe-e226a7f8210c", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 Property Description auth.params.projectId The project ID required to authenticate PubSub. auth.params.credentials The credential or key required to authenticate PubSub. connectionSpec.id The PubSub connection spec ID: 70116022-a743-464a-bbfe-e226a7f8210c . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google PubSub connection", "description": "Google PubSub connection", "auth": { "specName": "Project Based Authentication", "params": { "projectId": "{PROJECT_ID}", "credentials": "{CREDENTIALS}" } }, "connectionSpec": { "id": "70116022-a743-464a-bbfe-e226a7f8210c", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 |  | Property | Description | auth.params.projectId | The project ID required to authenticate PubSub. | auth.params.credentials | The credential or key required to authenticate PubSub. | connectionSpec.id | The PubSub connection spec ID: 70116022-a743-464a-bbfe-e226a7f8210c. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google PubSub connection", "description": "Google PubSub connection", "auth": { "specName": "Project Based Authentication", "params": { "projectId": "{PROJECT_ID}", "credentials": "{CREDENTIALS}" } }, "connectionSpec": { "id": "70116022-a743-464a-bbfe-e226a7f8210c", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| Property | Description |
| auth.params.projectId | The project ID required to authenticate PubSub. |
| auth.params.credentials | The credential or key required to authenticate PubSub. |
| connectionSpec.id | The PubSub connection spec ID: 70116022-a743-464a-bbfe-e226a7f8210c. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). This base connection ID is required in the next step to create a source connection. code language-json { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } | code language-json | { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |
| code language-json |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |

Topic and subscription-based authentication
To create base connection with topic and subscription-based authentication, make a POST request to the /connections endpoint and provide your credentials, topicName, and subscriptionName in the request body.

| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google PubSub connection", "description": "Google PubSub connection", "auth": { "specName": "Topic & Subscription Based Authentication", "params": { "credentials": "{CREDENTIALS}", "topicName": "projects/{PROJECT_ID}/topics/{TOPIC_ID}", "subscriptionName": "projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}" } }, "connectionSpec": { "id": "70116022-a743-464a-bbfe-e226a7f8210c", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Property Description auth.params.credentials The credential or key required to authenticate PubSub. auth.params.topicName The project ID and topic ID pair for the PubSub source that you want to provide access to. auth.params.subscriptionName The project ID and subscription ID pair for the PubSub source that you want to provide access to. connectionSpec.id The PubSub connection spec ID: 70116022-a743-464a-bbfe-e226a7f8210c . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google PubSub connection", "description": "Google PubSub connection", "auth": { "specName": "Topic & Subscription Based Authentication", "params": { "credentials": "{CREDENTIALS}", "topicName": "projects/{PROJECT_ID}/topics/{TOPIC_ID}", "subscriptionName": "projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}" } }, "connectionSpec": { "id": "70116022-a743-464a-bbfe-e226a7f8210c", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  | Property | Description | auth.params.credentials | The credential or key required to authenticate PubSub. | auth.params.topicName | The project ID and topic ID pair for the PubSub source that you want to provide access to. | auth.params.subscriptionName | The project ID and subscription ID pair for the PubSub source that you want to provide access to. | connectionSpec.id | The PubSub connection spec ID: 70116022-a743-464a-bbfe-e226a7f8210c. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Google PubSub connection", "description": "Google PubSub connection", "auth": { "specName": "Topic & Subscription Based Authentication", "params": { "credentials": "{CREDENTIALS}", "topicName": "projects/{PROJECT_ID}/topics/{TOPIC_ID}", "subscriptionName": "projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}" } }, "connectionSpec": { "id": "70116022-a743-464a-bbfe-e226a7f8210c", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| Property | Description |
| auth.params.credentials | The credential or key required to authenticate PubSub. |
| auth.params.topicName | The project ID and topic ID pair for the PubSub source that you want to provide access to. |
| auth.params.subscriptionName | The project ID and subscription ID pair for the PubSub source that you want to provide access to. |
| connectionSpec.id | The PubSub connection spec ID: 70116022-a743-464a-bbfe-e226a7f8210c. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created connection, including its unique identifier ( id ). This base connection ID is required in the next step to create a source connection. code language-json { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } | code language-json | { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |
| code language-json |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"6507cfd8-0000-0200-0000-5e18fc600000\"" } |

## Create a source connection source

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
      "name": "Google PubSub source connection",
      "description": "A source connection for Google PubSub",
      "baseConnectionId": "4cb0c374-d3bb-4557-b139-5712880adc55",
      "connectionSpec": {
          "id": "70116022-a743-464a-bbfe-e226a7f8210c",
          "version": "1.0"
      },
      "data": {
          "format": "json"
      },
      "params": {
          "topicName": "projects/{PROJECT_ID}/topics/{TOPIC_ID}",
          "subscriptionName": "projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_ID}",
          "dataType": "raw"
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
The base connection ID of your PubSub source that was generated in the previous step.
connectionSpec.id
The fixed connection specification ID for PubSub. This ID is:
70116022-a743-464a-bbfe-e226a7f8210c
data.format
The format of the PubSub data that you want to ingest. Currently, the only supported data format is
json
.
params.topicName
The name of your PubSub topic. In PubSub, a topic is a named resource that represents a feed of messages.
params.subscriptionName
The subscription name that corresponds with a given topic. In PubSub, subscriptions allow you to read messages from a topic. One or many subscriptions can be assigned to a single topic.
params.dataType
This parameter defines the type of the data that is being ingested. Supported data types include:
raw
and
xdm
.
**Response**

A successful response returns the unique identifier (id) of the newly created source connection. This ID is required in the next tutorial to create a dataflow.

```
{
    "id": "e96d6135-4b50-446e-922c-6dd66672b6b2",
    "etag": "\"66013508-0000-0200-0000-5f6e2ae70000\""
}
```

NOTE
After you create or update a streaming dataflow, a brief 5-minute pause in data ingestion is required to prevent any potential instances of data loss or data drops.
## Next steps

By following this tutorial, you have created a PubSub source connection using the Flow Service API. You can use this source connection ID in the next tutorial to [create a streaming dataflow using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/collect/streaming).

recommendation-more-help
