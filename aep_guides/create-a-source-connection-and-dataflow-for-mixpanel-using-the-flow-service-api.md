---
title: "Create a source connection and dataflow for Mixpanel using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/analytics/mixpanel"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:25.881957+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a source connection and dataflow for Mixpanel using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

The following tutorial walks you through the steps to create a source connection and a dataflow to bring Mixpanel data to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to Mixpanel using the Flow Service API.

### Gather required credentials

In order to connect Mixpanel to Experience Platform, you must provide values for the following connection properties:

Credential
Description
Example
username
The service account username that corresponds with your Mixpanel account. See the
Mixpanel service accounts documentation
for more information.
Test8.6d4ee7.mp-service-account
password
The service account password that corresponds with your Mixpanel account.
dLlidiKHpCZtJhQDyN2RECKudMeTItX1
projectId
Your Mixpanel project ID. This ID is required to create a source connection. See the
Mixpanel project settings documentation
and the
Mixpanel guide on creating and managing projects
for more information.
2384945
timezone
The timezone that corresponds with your Mixpanel project. Timezone is required to create a source connection. See the
Mixpanel project settings documentation
for more information.
Pacific Standard Time
For more information on authenticating your Mixpanel source, see the [Mixpanel source overview](/en/docs/experience-platform/sources/connectors/analytics/mixpanel).

## Create a base connection base-connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your Mixpanel authentication credentials as part of the request body.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Mixpanel:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/connections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "Mixpanel base connection",
      "description": "Mixpanel base connection to authenticate to Experience Platform",
      "connectionSpec": {
          "id": "fd2c8ff3-1de0-4f6b-8fa8-4264784870eb",
          "version": "1.0"
      },
      "auth": {
          "specName": "Basic Authentication",
          "params": {
              "username": "{USERNAME}",
              "password": "{PASSWORD}"
          }
      }
  }'
```

Property
Description
name
The name of your base connection. Ensure that the name of your base connection is descriptive as you can use this to look up information on your base connection.
description
An optional value that you can include to provide more information on your base connection.
connectionSpec.id
The connection specification ID of your source. This ID can be retrieved after your source is registered and approved through the Flow Service API.
auth.specName
The authentication type that you are using to authenticate your source to Experience Platform.
auth.params.
Contains the credentials required to authenticate your source.
auth.params.username
The username that corresponds with your Mixpanel account.
auth.params.password
The password that corresponds with your Mixpanel account.
**Response**

A successful response returns the newly created base connection, including its unique connection identifier (id). This ID is required to explore your source’s file structure and contents in the next step.

```
{
     "id": "70383d02-2777-4be7-a309-9dd6eea1b46d",
     "etag": "\"d64c8298-add4-4667-9a49-28195b2e2a84\""
}
```

## Explore your source explore

Using the base connection ID you generated in the previous step, you can explore files and directories by performing GET requests.Use the following calls to find the path of the file you wish to bring into Experience Platform:

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=rest&object={OBJECT}&fileType={FILE_TYPE}&preview={PREVIEW}&sourceParams={SOURCE_PARAMS}
```

When performing GET requests to explore your source’s file structure and contents, you must include the query parameters that are listed in the table below:

Parameter
Description
{BASE_CONNECTION_ID}
The base connection ID generated in the previous step.
objectType=rest
The type of object that you wish to explore. Currently, this value is always set to
rest
.
{OBJECT}
This parameter is required only when viewing a specific directory. Its value represents the path of the directory you wish to explore. For this source the value would be
json
.
fileType=json
The file type of the file you want to bring to Experience Platform. Currently,
json
is the only supported file type.
{PREVIEW}
A boolean value that defines whether the contents of the connection supports preview.
{SOURCE_PARAMS}
Defines parameters for the source file you want to bring to Experience Platform. To retrieve the accepted format-type for
{SOURCE_PARAMS}
, you must encode the entire
{"projectId":"2671127","timezone":"Pacific Standard Time"}
string in base64.
Note
: In the example below,
"{"projectId":"2671127","timezone":"Pacific Standard Time"}"
encoded in base64 equates to
eyJwcm9qZWN0SWQiOiIyNjcxMTI3IiwidGltZXpvbmUiOiJQYWNpZmljIFN0YW5kYXJkIFRpbWUifQ==
.
**Request**

```
curl -X GET \
    'https://platform.adobe.io/data/foundation/flowservice/connections/70383d02-2777-4be7-a309-9dd6eea1b46d/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJsaXN0SWQiOiIxMGMwOTdjYTcxIn0=' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns the structure of the queried file.

```
{
    "format": "hierarchical",
    "schema": {
        "type": "object",
        "properties": {
            "event": {
                "type": "string"
            },
            "properties": {
                "type": "object",
                "properties": {
                    "$mp_api_endpoint": {
                        "type": "string"
                    },
                    "$insert_id": {
                        "type": "string"
                    },
                    "item_id": {
                        "type": "string"
                    },
                    "distinct_id": {
                        "type": "string"
                    },
                    "$mp_api_timestamp_ms": {
                        "type": "integer",
                        "minimum": -9007199254740992,
                        "maximum": 9007199254740991
                    },
                    "item_price": {
                        "type": "string"
                    },
                    "$import": {
                        "type": "boolean"
                    },
                    "item_name": {
                        "type": "string"
                    },
                    "time": {
                        "type": "integer",
                        "minimum": -9007199254740992,
                        "maximum": 9007199254740991
                    },
                    "mp_processing_time_ms": {
                        "type": "integer",
                        "minimum": -9007199254740992,
                        "maximum": 9007199254740991
                    }
                }
            }
        }
    },
    "data": [
        {
            "event": "Items purchased",
            "properties": {
                "time": 1652825148,
                "distinct_id": "test@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b70",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1652850348643,
                "item_id": "29066",
                "item_name": "charger",
                "item_price": "800.00",
                "mp_processing_time_ms": 1652850348702
            }
        },
        {
            "event": "Items sold",
            "properties": {
                "time": 1652423938,
                "distinct_id": "test@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b70",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1652449138115,
                "item_id": "29036",
                "item_name": "chair",
                "item_price": "5000.00",
                "mp_processing_time_ms": 1652449138173
            }
        },
        {
            "event": "Items sold",
            "properties": {
                "time": 1652854256,
                "distinct_id": "test@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b70",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1652879456538,
                "item_id": "29066",
                "item_name": "mobile",
                "item_price": "7000.00",
                "mp_processing_time_ms": 1652879456604
            }
        },
        {
            "event": "Sign off",
            "properties": {
                "time": 1648140611,
                "distinct_id": "test@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b75",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648555709515,
                "item_id": "29073",
                "item_name": "Watch",
                "item_price": "50000.00",
                "mp_processing_time_ms": 1648555710375
            }
        },
        {
            "event": "Items sold",
            "properties": {
                "time": 1648140612,
                "distinct_id": "test@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b75",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648556481708,
                "item_id": "29073",
                "item_name": "Pen",
                "item_price": "1000.00",
                "mp_processing_time_ms": 1648556481880
            }
        },
        {
            "event": "Sign in",
            "properties": {
                "time": 1648140614,
                "distinct_id": "test1@test.com",
                "$import": true,
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b75",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648556032401,
                "item_id": "29073",
                "item_name": "Watch",
                "item_price": "50000.00",
                "mp_processing_time_ms": 1648556032462
            }
        },
        {
            "event": "Item Purchased",
            "properties": {
                "time": 1648165814,
                "distinct_id": "test1@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b74",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648480684785,
                "item_id": "29073",
                "item_name": "Watch",
                "item_price": "50000.00",
                "mp_processing_time_ms": 1648480685058
            }
        },
        {
            "event": "Item Purchased",
            "properties": {
                "time": 1648165814,
                "distinct_id": "test1@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b75",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648551687866,
                "item_id": "29073",
                "item_name": "Watch",
                "item_price": "50000.00",
                "mp_processing_time_ms": 1648551687922
            }
        },
        {
            "event": "Sign off",
            "properties": {
                "time": 1648530419,
                "distinct_id": "test1@test.com",
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b75",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648555619274,
                "item_id": "29073",
                "item_name": "Watch",
                "item_price": "50000.00",
                "mp_processing_time_ms": 1648555619326
            }
        },
        {
            "event": "Items sold",
            "properties": {
                "time": 1648566534,
                "distinct_id": "test1@test.com",
                "$import": true,
                "$insert_id": "935d87b1-00cd-41b7-be34-b9d98dd08b75",
                "$mp_api_endpoint": "api.mixpanel.com",
                "$mp_api_timestamp_ms": 1648635830114,
                "item_id": "29073",
                "item_name": "Pen",
                "item_price": "1000.00",
                "mp_processing_time_ms": 1648635831010
            }
        }
    ]
}
```

## Create a source connection source-connection

You can create a source connection by making a POST request to the Flow Service API. A source connection consists of a connection ID, a path to the source data file, and a connection spec ID.

**API format**

```
POST /sourceConnections
```

**Request**

The following request creates a source connection for Mixpanel:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "Mixpanel source connection",
      "description": "Mixpanel source connection",
      "baseConnectionId": "70383d02-2777-4be7-a309-9dd6eea1b46d",
      "connectionSpec": {
          "id": "fd2c8ff3-1de0-4f6b-8fa8-4264784870eb",
          "version": "1.0"
      },
      "data": {
          "format": "json"
      },
      "params": {
          "projectId": "{PROJECT_ID}",
          "timezone": "{TIMEZONE}"
      }
  }'
```

Property
Description
name
The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection.
description
An optional value that you can include to provide more information on your source connection.
baseConnectionId
The base connection ID of Mixpanel. This ID was generated in an earlier step.
connectionSpec.id
The connection specification ID that corresponds to your source.
data.format
The format of the Mixpanel data that you want to ingest. Currently, the only supported data format is
json
.
params.projectId
Your Mixpanel project ID.
params.timezone
The timezone of your Mixpanel project.
**Response**

A successful response returns the unique identifier (id) of the newly created source connection. This ID is required in a later step to create a dataflow.

```
{
     "id": "246d052c-da4a-494a-937f-a0d17b1c6cf5",
     "etag": "\"712a8c08-fda7-41c2-984b-187f823293d8\""
}
```

## Create a target XDM schema target-schema

In order for the source data to be used in Experience Platform, a target schema must be created to structure the source data according to your needs. The target schema is then used to create an Experience Platform dataset in which the source data is contained.

A target XDM schema can be created by performing a POST request to the [Schema Registry API](https://www.adobe.io/experience-platform-apis/references/schema-registry/).

For detailed steps on how to create a target XDM schema, see the tutorial on [creating a schema using the API](/en/docs/experience-platform/xdm/api/schemas).

## Create a target dataset target-dataset

A target dataset can be created by performing a POST request to the [Catalog Service API](https://developer.adobe.com/experience-platform-apis/references/catalog/), providing the ID of the target schema within the payload.

For detailed steps on how to create a target dataset, see the tutorial on [creating a dataset using the API](/en/docs/experience-platform/catalog/api/create-dataset).

## Create a target connection target-connection

A target connection represents the connection to the destination where the ingested data is to be stored. To create a target connection, you must provide the fixed connection specification ID that corresponds to the data lake. This ID is: c604ff05-7f1a-43c0-8e18-33bf874cb11c.

You now have the unique identifiers a target schema a target dataset and the connection spec ID to the data lake. Using these identifiers, you can create a target connection using the Flow Service API to specify the dataset that will contain the inbound source data.

**API format**

```
POST /targetConnections
```

**Request**

The following request creates a target connection for Mixpanel:

```
curl -X POST \
    'https://platform.adobe.io/data/foundation/flowservice/targetConnections' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}' \
    -H 'Content-Type: application/json' \
    -d '{
        "name": "{Mixpanel} Target Connection",
        "description": "{Mixpanel} Target Connection",
        "connectionSpec": {
            "id": "fd2c8ff3-1de0-4f6b-8fa8-4264784870eb",
            "version": "1.0"
        },
        "data": {
            "format": "json"
        },
        "params": {
            "dataSetId": "5ef4551c52e054191a61a99f"
        }
    }'
```

Property
Description
name
The name of your target connection. Ensure that the name of your target connection is descriptive as you can use this to look up information on your target connection.
description
An optional value that you can include to provide more information on your target connection.
connectionSpec.id
The connection specification ID that corresponds to data lake. This fixed ID is:
fd2c8ff3-1de0-4f6b-8fa8-4264784870eb
.
data.format
The format of the Mixpanel data that you want to bring to Experience Platform.
params.dataSetId
The target dataset ID retrieved in a previous step.
**Response**

A successful response returns the new target connection’s unique identifier (id). This ID is required in later steps.

```
{
     "id": "7c96c827-3ffd-460c-a573-e9558f72f263",
     "etag": "\"a196f685-f5e8-4c4c-bfbd-136141bb0c6d\""
}
```

## Create a mapping mapping

In order for the source data to be ingested into a target dataset, it must first be mapped to the target schema that the target dataset adheres to. This is achieved by performing a POST request to [Data Prep API](https://www.adobe.io/experience-platform-apis/references/data-prep/) with data mappings defined within the request payload.

**API format**

```
POST /conversion/mappingSets
```

**Request**

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/conversion/mappingSets' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "version": 0,
      "xdmSchema": "https://ns.adobe.com/{TENANT_ID}/schemas/995dabbea86d58e346ff91bd8aa741a9f36f29b1019138d4",
      "xdmVersion": "1.0",
      "id": null,
      "mappings": [
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.distinct_id",
              "destination": "_extconndev.distinct_id",
              "name": "distinct_id",
              "description": "Mixpanel"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.event_name",
              "destination": "_extconndev.event_name"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.import",
              "destination": "_extconndev.import"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.insert_id",
              "destination": "_extconndev.insert_id"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.item_id",
              "destination": "_extconndev.item_id"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.item_name",
              "destination": "_extconndev.item_name"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.item_price",
              "destination": "_extconndev.item_price"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.mp_api_endpoint",
              "destination": "_extconndev.mp_api_endpoint"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.mp_api_timestamp_ms",
              "destination": "_extconndev.mp_api_timestamp_ms"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.mp_processing_time_ms",
              "destination": "_extconndev.mp_processing_time_ms"
          },
          {
              "sourceType": "ATTRIBUTE",
              "source": "data.time",
              "destination": "_extconndev.time"
          }
      ]
  }'
```

Property
Description
xdmSchema
The ID of the
target XDM schema
generated in an earlier step.
mappings.destinationXdmPath
The destination XDM path where the source attribute is being mapped to.
mappings.sourceAttribute
The source attribute that needs to be mapped to a destination XDM path.
mappings.identity
A boolean value that designates whether the mapping set will be marked for Identity Service.
**Response**

A successful response returns details of the newly created mapping including its unique identifier (id). This value is required in a later step to create a dataflow.

```
{
    "id": "bf5286a9c1ad4266baca76ba3adc9366",
    "version": 0,
    "createdDate": 1597784069368,
    "modifiedDate": 1597784069368,
    "createdBy": "{CREATED_BY}",
    "modifiedBy": "{MODIFIED_BY}"
}
```

## Create a flow flow

The last step towards bringing data from Mixpanel to Experience Platform is to create a dataflow. By now, you have the following required values prepared:

- [Source connection ID](#source-connection)
- [Target connection ID](#target-connection)
- [Mapping ID](#mapping)

A dataflow is responsible for scheduling and collecting data from a source. You can create a dataflow by performing a POST request while providing the previously mentioned values within the payload.

To schedule an ingestion, you must first set the start time value to epoch time in seconds. Then, you must set the frequency value to one of the five options: once, minute, hour, day, or week. The interval value designates the period between two consecutive ingestions however, creating a one-time ingestion does not require an interval to be set. For all other frequencies, the interval value must be set to equal or greater than 15.

**API format**

```
POST /flows
```

**Request**

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/flows' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "{Mixpanel} dataflow",
      "description": "{Mixpanel} dataflow",
      "flowSpec": {
          "id": "6499120c-0b15-42dc-936e-847ea3c24d72",
          "version": "1.0"
      },
      "sourceConnectionIds": [
          "246d052c-da4a-494a-937f-a0d17b1c6cf5"
      ],
      "targetConnectionIds": [
          "7c96c827-3ffd-460c-a573-e9558f72f263"
      ],
      "transformations": [
          {
              "name": "Mapping",
              "params": {
                  "mappingId": "bf5286a9c1ad4266baca76ba3adc9366",
                  "mappingVersion": "0"
              }
          }
      ],
      "scheduleParams": {
          "startTime": "1625040887",
          "frequency": "minute",
          "interval": 15
      }
  }'
```

Property
Description
name
The name of your dataflow. Ensure that the name of your dataflow is descriptive as you can use this to look up information on your dataflow.
description
An optional value that you can include to provide more information on your dataflow.
flowSpec.id
The flow specification ID required to create a dataflow. This fixed ID is:
6499120c-0b15-42dc-936e-847ea3c24d72
.
flowSpec.version
The corresponding version of the flow specification ID. This value defaults to
1.0
.
sourceConnectionIds
The
source connection ID
generated in an earlier step.
targetConnectionIds
The
target connection ID
generated in an earlier step.
transformations
This property contains the various transformations that are needed to be applied to your data. This property is required when bringing non-XDM-compliant data to Experience Platform.
transformations.name
The name assigned to the transformation.
transformations.params.mappingId
The
mapping ID
generated in an earlier step.
transformations.params.mappingVersion
The corresponding version of the mapping ID. This value defaults to
0
.
scheduleParams.startTime
This property contains information on the ingestion scheduling of the dataflow.
scheduleParams.frequency
The frequency at which the dataflow will collect data. Acceptable values include:
once
,
minute
,
hour
,
day
, or
week
.
scheduleParams.interval
The interval designates the period between two consecutive flow runs. The interval’s value should be a non-zero integer. Interval is not required when frequency is set as
once
and should be greater than or equal to
15
for other frequency values.
**Response**

A successful response returns the ID (id) of the newly created dataflow. You can use this ID to monitor, update, or delete your dataflow.

```
{
     "id": "993f908f-3342-4d9c-9f3c-5aa9a189ca1a",
     "etag": "\"510bb1d4-8453-4034-b991-ab942e11dd8a\""
}
```

## Appendix

The following section provides information on the steps you can to monitor, update, and delete your dataflow.

### Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to see information on flow runs, completion status, and errors. For complete API examples, read the guide on [monitoring your sources dataflows using the API](/en/docs/experience-platform/sources/api-tutorials/monitor).

### Update your dataflow

Update the details of your dataflow, such as its name and description, as well as its run schedule and associated mapping sets by making a PATCH request to the /flows endpoint of Flow Service API, while providing the ID of your dataflow. When making a PATCH request, you must provide your dataflow’s unique etag in the If-Match header. For complete API examples, read the guide on [updating sources dataflows using the API](/en/docs/experience-platform/sources/api-tutorials/update-dataflows).

### Update your account

Update the name, description, and credentials of your source account by performing a PATCH request to the Flow Service API while providing your base connection ID as a query parameter. When making a PATCH request, you must provide your source account’s unique etag in the If-Match header. For complete API examples, read the guide on [updating your source account using the API](/en/docs/experience-platform/sources/api-tutorials/update).

### Delete your dataflow

Delete your dataflow by performing a DELETE request to the Flow Service API while providing the ID of the dataflow you want to delete as part of the query parameter. For complete API examples, read the guide on [deleting your dataflows using the API](/en/docs/experience-platform/sources/api-tutorials/delete-dataflows).

### Delete your account

Delete your account by performing a DELETE request to the Flow Service API while providing the base connection ID of the account you want to delete. For complete API examples, read the guide on [deleting your source account using the API](/en/docs/experience-platform/sources/api-tutorials/delete).

recommendation-more-help
