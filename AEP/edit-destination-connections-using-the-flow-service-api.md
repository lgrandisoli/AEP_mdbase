---
title: "Edit destination connections using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/destinations/api/edit-destination"
category: "reference"
topic: "experience-platform/destinations-guide"
created_at: "2026-05-29T17:07:21.659841+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Destinations Guide

# Edit destination connections using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Destinations](#)

CREATED FOR:

- Admin
- User

This tutorial covers the steps for editing various components of a destination connection. Learn how to update authentication credentials, export location, and more by using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

NOTE
The edit operations described in this tutorial are also supported in the Experience Platform UI. Read the tutorial on how to
edit destinations in the UI
for more information.
## Getting started get-started

This tutorial requires you to have a valid dataflow ID. If you do not have a valid dataflow ID, select your destination of choice from the [destinations catalog](/en/docs/experience-platform/destinations/catalog/overview) and follow the steps outlined to [connect to the destination](/en/docs/experience-platform/destinations/ui/connect-destination) and [activate data](/en/docs/experience-platform/destinations/ui/activate/activation-overview) before attempting this tutorial.

NOTE
The terms
flow
and
dataflow
are used interchangeably in this tutorial. In the context of this tutorial, they have the same meaning.
This tutorial also requires you to have a working understanding of the following components of Adobe Experience Platform:

- [Destinations](/en/docs/experience-platform/destinations/home): Destinations are pre-built integrations with destination platforms that allow for the seamless activation of data from Adobe Experience Platform. You can use destinations to activate your known and unknown data for cross-channel marketing campaigns, email campaigns, targeted advertising, and many other use cases.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know to successfully update your dataflow using the Flow Service API.

### Reading sample API calls reading-sample-api-calls

This tutorial provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

### Gather values for required headers gather-values-for-required-headers

To make calls to Experience Platform APIs, you must first complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform, including those belonging to Flow Service, are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

NOTE
If the
x-sandbox-name
header is not specified, requests are resolved under the
prod
sandbox.
All requests that contain a payload (POST, PUT, PATCH) require an additional media type header:

- Content-Type: application/json

## Look up dataflow details look-up-dataflow-details

The first step in editing your destination connection is to retrieve dataflow details using your flow ID. You can view the current details of an existing dataflow by making a GET request to the /flows endpoint.

TIP
You can use the Experience Platform UI to get the desired dataflow ID of a destination. Go to
Destinations
>
Browse
, select the desired destination dataflow and find the destination ID in the right rail. The destination ID is the value that you will use as flow ID in the next step.
**API format**

```
GET /flows/{FLOW_ID}
```

Parameter
Description
{FLOW_ID}
The unique
id
value for the destination dataflow you want to retrieve.
**Request**

The following request retrieves information regarding your flow ID.

```
curl -X GET \
    'https://platform.adobe.io/data/foundation/flowservice/flows/226fb2e1-db69-4760-b67e-9e671e05abfc' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the current details of your dataflow including its version, unique identifier (id), and other relevant information. Most relevant for this tutorial are the target connection and base connection IDs highlighted in the response below. You will use these IDs in the next sections to update various components of the destination connection.

```
{
   "items":[
      {
         "id":"226fb2e1-db69-4760-b67e-9e671e05abfc",
         "createdAt":"{CREATED_AT}",
         "updatedAt":"{UPDATED_BY}",
         "createdBy":"{CREATED_BY}",
         "updatedBy":"{UPDATED_BY}",
         "createdClient":"{CREATED_CLIENT}",
         "updatedClient":"{UPDATED_CLIENT}",
         "sandboxId":"{SANDBOX_ID}",
         "sandboxName":"prod",
         "imsOrgId":"{ORG_ID}",
         "name":"2021 winter campaign",
         "description":"ACME company holiday campaign for high fidelity customers",
         "flowSpec":{
            "id":"71471eba-b620-49e4-90fd-23f1fa0174d8",
            "version":"1.0"
         },
         "state":"enabled",
         "version":"\"8b0351ca-0000-0200-0000-61c4d6700000\"",
         "etag":"\"8b0351ca-0000-0200-0000-61c4d6700000\"",
         "sourceConnectionIds":[
            "5e45582a-5336-4ea1-9ec9-d0004a9f344a"
         ],
         "targetConnectionIds":[
            "8ce3dc63-3766-4220-9f61-51d2f8f14618"
         ],
         "inheritedAttributes":{
            "sourceConnections":[
               {
                  "id":"5e45582a-5336-4ea1-9ec9-d0004a9f344a",
                  "connectionSpec":{
                     "id":"8a9c3494-9708-43d7-ae3f-cda01e5030e1",
                     "version":"1.0"
                  },
                  "baseConnection":{
                     "id":"0a82f29f-b457-47f7-bb30-33856e2ae5aa",
                     "connectionSpec":{
                        "id":"8a9c3494-9708-43d7-ae3f-cda01e5030e1",
                        "version":"1.0"
                     }
                  },
                  "typeInfo":{
                     "type":"ProfileFragments",
                     "id":"ups"
                  }
               }
            ],
            "targetConnections":[
               {
                  "id":"8ce3dc63-3766-4220-9f61-51d2f8f14618",
                  "connectionSpec":{
                     "id":"0b23e41a-cb4a-4321-a78f-3b654f5d7d97",
                     "version":"1.0"
                  },
                  "baseConnection":{
                     "id":"7fbf542b-83ed-498f-8838-8fde0c4d4d69",
                     "connectionSpec":{
                        "id":"0b23e41a-cb4a-4321-a78f-3b654f5d7d97",
                        "version":"1.0"
                     }
                  }
               }
            ]
         },
         "transformations":[
            "shortened for brevity"
         ]
      }
   ]
```

style
shade-box
## Edit target connection components (storage location and other components) patch-target-connection

The components of a target connection differ by destination. For example, for Amazon S3 destinations, you can update the bucket and path where files are exported. For Pinterest destinations, you can update your Pinterest Advertiser ID and for Google Customer Match you can update your Pinterest Account ID.

To update components of a target connection, perform a PATCH request to the /targetConnections/{TARGET_CONNECTION_ID} endpoint while providing your target connection ID, version, and the new values you want to use. Remember, you got your target connection ID in the previous step, when you inspected an existing dataflow to your desired destination.

IMPORTANT
The
If-Match
header is required when making a
PATCH
request. The value for this header is the unique version of the target connection you want to update. The etag value updates with every successful update of a flow entity such as dataflow, target connection, and others.
To get the latest version of the etag value, perform a GET request to the
/targetConnections/{TARGET_CONNECTION_ID}
endpoint, where
{TARGET_CONNECTION_ID}
is the target connection ID that you are looking to update.
Make sure to wrap the value of the
If-Match
header in double quotes like in the examples below when making
PATCH
requests.
Below are a few examples of updating parameters in the target connection spec for different types of destinations. But the general rule to update parameters for any destination is as follows:

Get the dataflow ID of the connection > obtain the target connection ID > PATCH the target connection with updated values for the desired parameters.

**API format**

```
PATCH /targetConnections/{TARGET_CONNECTION_ID}
```

Amazon S3
**Request**

The following request updates the bucketName and path parameters of an [Amazon S3](/en/docs/experience-platform/destinations/catalog/cloud-storage/amazon-s3#destination-details) destination connection.

| code language-shell |
| --- |
| curl -X PATCH \ 'https://platform.adobe.io/data/foundation/flowservice/targetConnections/b2cb1407-3114-441c-87ea-2c1a3c84d0b0' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' -H 'If-Match: "1a0037e4-0000-0200-0000-602e06f60000"' \ -d '[ { "op": "replace", "path": "/params", "value": { "bucketName": "newBucketName", "path": "updatedPath" } } ]' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto |  |
| --- | --- |
| Property | Description |
| op | The operation call used to define the action needed to update the dataflow. Operations include: add, replace, and remove. |
| path | Defines the part of the flow that is to be updated. |
| value | The new value you want to update your parameter with. |

**Response**

A successful response returns your target connection ID and an updated Etag. You can verify the update by making a GET request to the Flow Service API, while providing your target connection ID.

| code language-json |
| --- |
| { "id": "b2cb1407-3114-441c-87ea-2c1a3c84d0b0", "etag": "\"50014cc8-0000-0200-0000-6036eb720000\"" } |

Google Ad Manager and Google Ad Manager 360
**Request**

The following request updates the parameters of a [Google Ad Manager](/en/docs/experience-platform/destinations/catalog/advertising/google-ad-manager) or [Google Ad Manager 360 destination](/en/docs/experience-platform/destinations/catalog/advertising/google-ad-manager-360-connection#destination-details) connection to add the new **Append audience ID to audience name** field.

| code language-shell |
| --- |
| curl -X PATCH \ 'https://platform.adobe.io/data/foundation/flowservice/targetConnections/b2cb1407-3114-441c-87ea-2c1a3c84d0b0' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' -H 'If-Match: "1a0037e4-0000-0200-0000-602e06f60000"' \ -d '[ { "op": "add", "path": "/params/appendSegmentId", "value": true } ]' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto |  |
| --- | --- |
| Property | Description |
| op | The operation call used to define the action needed to update the dataflow. Operations include: add, replace, and remove. |
| path | Defines the part of the flow that is to be updated. |
| value | The new value you want to update your parameter with. |

**Response**

A successful response returns your target connection ID and an updated etag. You can verify the update by making a GET request to the Flow Service API, while providing your target connection ID.

| code language-json |
| --- |
| { "id": "b2cb1407-3114-441c-87ea-2c1a3c84d0b0", "etag": "\"50014cc8-0000-0200-0000-6036eb720000\"" } |

Pinterest
**Request**

The following request updates the advertiserId parameter of a [Pinterest destination connection](/en/docs/experience-platform/destinations/catalog/advertising/pinterest#parameters).

| code language-shell |
| --- |
| curl -X PATCH \ 'https://platform.adobe.io/data/foundation/flowservice/targetConnections/b2cb1407-3114-441c-87ea-2c1a3c84d0b0' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' -H 'If-Match: "1a0037e4-0000-0200-0000-602e06f60000"' \ -d '[ { "op": "replace", "path": "/params", "value": { "advertiser_id": "1234567890" } } ]' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto |  |
| --- | --- |
| Property | Description |
| op | The operation call used to define the action needed to update the dataflow. Operations include: add, replace, and remove. |
| path | Defines the part of the flow that is to be updated. |
| value | The new value you want to update your parameter with. |

**Response**

A successful response returns your target connection ID and an updated etag. You can verify the update by making a GET request to the Flow Service API, while providing your target connection ID.

| code language-json |
| --- |
| { "id": "b2cb1407-3114-441c-87ea-2c1a3c84d0b0", "etag": "\"50014cc8-0000-0200-0000-6036eb720000\"" } |

style
shade-box
## Edit base connection components (authentication parameters and other components) patch-base-connection

Edit the base connection when you want to update a destination’s credentials. The components of a base connection differ by destination. For example, for Amazon S3 destinations, you can update the access key and secret key to your Amazon S3 location.

To update components of a base connection, perform a PATCH request to the /connections endpoint while providing your base connection ID, version, and the new values you want to use.

Remember, you got your base connection ID in a [previous step](#look-up-dataflow-details), when you inspected an existing dataflow to your desired destination for the parameter baseConnection.

IMPORTANT
The
If-Match
header is required when making a
PATCH
request. The value for this header is the unique version of the base connection you want to update. The etag value updates with every successful update of a flow entity such as dataflow, base connection, and others.
To get the latest version of the Etag value, perform a GET request to the
/connections/{BASE_CONNECTION_ID}
endpoint, where
{BASE_CONNECTION_ID}
is the base connection ID that you are looking to update.
Make sure to wrap the value of the
If-Match
header in double quotes like in the examples below when making
PATCH
requests.
Below are a few examples of updating parameters in the base connection spec for different types of destinations. But the general rule to update parameters for any destination is as follows:

Get the dataflow ID of the connection > obtain the base connection ID > PATCH the base connection with updated values for the desired parameters.

**API format**

```
PATCH /connections/{BASE_CONNECTION_ID}
```

Amazon S3
**Request**

The following request updates the accessId and secretKey parameters of an [Amazon S3](/en/docs/experience-platform/destinations/catalog/cloud-storage/amazon-s3#destination-details) destination connection.

| code language-shell |
| --- |
| curl -X PATCH \ 'https://platform.adobe.io/data/foundation/flowservice/targetConnections/b2cb1407-3114-441c-87ea-2c1a3c84d0b0' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' -H 'If-Match: "1a0037e4-0000-0200-0000-602e06f60000"' \ -d '[ { "op": "add", "path": "/auth/params", "value": { "accessId": "exampleAccessId", "secretKey": "exampleSecretKey" } } ]' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto |  |
| --- | --- |
| Property | Description |
| op | The operation call used to define the action needed to update the dataflow. Operations include: add, replace, and remove. |
| path | Defines the part of the flow that is to be updated. |
| value | The new value you want to update your parameter with. |

**Response**

A successful response returns your base connection ID and an updated etag. You can verify the update by making a GET request to the Flow Service API, while providing your base connection ID.

| code language-json |
| --- |
| { "id": "b2cb1407-3114-441c-87ea-2c1a3c84d0b0", "etag": "\"50014cc8-0000-0200-0000-6036eb720000\"" } |

Azure Blob
**Request**

The following request updates the parameters of an [Azure Blob destination](/en/docs/experience-platform/destinations/catalog/cloud-storage/azure-blob#authenticate) connection to update the connection string required to connect to an Azure Blob instance.

| code language-shell |
| --- |
| curl -X PATCH \ 'https://platform.adobe.io/data/foundation/flowservice/targetConnections/b2cb1407-3114-441c-87ea-2c1a3c84d0b0' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' -H 'If-Match: "1a0037e4-0000-0200-0000-602e06f60000"' \ -d '[ { "op": "add", "path": "/auth/params", "value": { "connectionString": "updatedString" } } ]' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto |  |
| --- | --- |
| Property | Description |
| op | The operation call used to define the action needed to update the dataflow. Operations include: add, replace, and remove. |
| path | Defines the part of the flow that is to be updated. |
| value | The new value you want to update your parameter with. |

**Response**

A successful response returns your base connection ID and an updated etag. You can verify the update by making a GET request to the Flow Service API, while providing your base connection ID.

| code language-json |
| --- |
| { "id": "b2cb1407-3114-441c-87ea-2c1a3c84d0b0", "etag": "\"50014cc8-0000-0200-0000-6036eb720000\"" } |

style
shade-box
## API error handling api-error-handling

The API endpoints in this tutorial follow the general Experience Platform API error message principles. See [API status codes](/en/docs/experience-platform/landing/troubleshooting#api-status-codes) and [request header errors](/en/docs/experience-platform/landing/troubleshooting#request-header-errors) in the Experience Platform troubleshooting guide for more information on interpreting error responses.

## Next steps next-steps

You have learned how to update various components of a destination connection using the Flow Service API. For more information on destinations, see the [destinations overview](/en/docs/experience-platform/destinations/home).

recommendation-more-help
