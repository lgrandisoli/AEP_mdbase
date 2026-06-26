---
title: "Connect Amazon S3 to Experience Platform using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/s3"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T16:56:00.581046+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Amazon S3 to Experience Platform using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how you can connect your Amazon S3 source account to Adobe Experience Platform using the [Flow Service API](https://developer.adobe.com/experience-platform-apis/references/flow-service/).

## Get started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Connect Amazon S3 to Experience Platform on Azure azure

Read the steps below for information on how to connect your Amazon S3 source to Experience Platform on Azure.

### Gather required credentials

In order for Flow Service to connect with your Amazon S3 storage, you must provide values for the following connection properties:

Credential
Description
s3AccessKey
The access key ID for your Amazon S3 bucket.
s3SecretKey
The secret key ID for your Amazon S3 bucket.
serviceUrl
(Optional) The custom Amazon S3 endpoint to connect to. This field is required when your Amazon S3 bucket is region-specific. The format for
serviceUrl
is:
https://s3.{REGION}.amazonaws.com/)
.
bucketName
The Amazon S3 bucket contains your data and its corresponding descriptive metadata. Your Amazon S3 bucket name must be between three and 63 characters long and must begin and end with either a letter or a number. The bucket name can only have lowercase letters, numbers, or hyphens (
-
), and cannot be formatted as an IP address.
folderPath
The path to the folder in your Amazon S3 bucket where your data is stored. This credential is required when the user has restricted access.
s3SessionToken
(Optional) A short-term, temporary token that allows you to provide temporary access to your Amazon S3 resources to users in untrusted environments. See the
Amazon S3 overview
for more information.
connectionSpec.id
The connection specification returns a source’s connector properties, including authentication specifications related to creating the base and source connections. The connection specification ID for Amazon S3 is:
ecadc60c-7455-4d87-84dc-2a0e293d997b
.
For more information on getting started, visit [this Amazon Web Services document](https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/).

### Create a base connection for Amazon S3 on Experience Platform on Azure

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your S3 authentication credentials as part of the request parameters.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Amazon S3:

Select to view request example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Amazon S3 base connection", "description": "Amazon S3 base connection with temporary session token", "auth": { "specName": "Access Key", "params": { "s3AccessKey": "{S3_ACCESS_KEY}", "s3SecretKey": "{S3_SECRET_KEY}", "s3SessionToken": "{S3_SESSION_TOKEN} } }, "connectionSpec": { "id": "ecadc60c-7455-4d87-84dc-2a0e293d997b", "version": "1.0" } }' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.s3AccessKey | The access key associated with your S3 bucket. |
| auth.params.s3SecretKey | Your secret key associated with your S3 bucket. |
| auth.params.s3SessionToken | (Optional) The short-term, temporary S3 token used to access your bucket. |
| connectionSpec.id | The S3 connection specification ID: ecadc60c-7455-4d87-84dc-2a0e293d997b |

**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your storage in the next tutorial.

Select to view response example
| code language-json |
| --- |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |

### Update your S3 session token

The s3SessionToken is temporary and must be updated when it expires. You can update the session token associated with your base connection by making a PATCH request to Flow Service API. See the [S3 overview](/en/docs/experience-platform/sources/connectors/cloud-storage/s3#azure) for more information on temporary security credentials for S3.

IMPORTANT
The
If-Match
header is required when making a PATCH request. The value for this header is the unique etag of the connection you want to update.
**API format**

```
PATCH /connections
```

**Request**

The following request creates a base connection for Amazon S3:

Select to view request example
| code language-shell |
| --- |
| curl -X PATCH \ 'https://platform.adobe.io/data/foundation/flowservice/connections/4cb0c374-d3bb-4557-b139-5712880adc55' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'Content-Type: application/json' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'If-Match: "1700d77b-0000-0200-0000-5e3b41a10000"' -d '[ { "op": "replace", "path": "/auth/params/s3SessionToken", "value": "{SESSION_TOKEN}" } ]' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Parameter | Description |
| op | The operation call used to define the action needed to update the connection. Operations include: add, replace, and remove. |
| path | The path of the parameter to be updated. |
| value | The new value you want to update your parameter with. |

**Response**

A successful response returns your base connection ID and an updated etag. You can verify the update by making a GET request to the Flow Service API, while providing your connection ID.

Select to view response example
| code language-json |
| --- |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"3600e378-0000-0200-0000-5f40212f0000\"" } |

## Connect Amazon S3 to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
Read the steps below for information on how to connect your Amazon S3 source to Experience Platform on AWS.

### Prerequisites

To connect your Amazon S3 account to Experience Platform on AWS, you must have the following:

- An AWS account with access to the Amazon S3 bucket or folder that you want to connect.
- The necessary IAM permissions that allow s3:GetObject and s3:ListBucket actions.

#### Retrieve the IAM role for your bucket permissions

**API format**

```
GET /connectionSpecs/{CONNECTION_SPEC_ID}/configs?authType={AUTH_TYPE}
```

**Request**

Select to view request example
| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connectionSpecs/ecadc60c-7455-4d87-84dc-2a0e293d997b/configs?authType=IamBasedAuthentication' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'Content-Type: application/json' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ |

**Response**

A successful response returns your IAM Role. This value is required in the next step to set up permissions in your Amazon S3 bucket.

Select to view response example
| code language-json |
| --- |
| { "configParams": { "IAMRole": "{IAM_ROLE}" } } |

### Set up permissions in your Amazon S3 bucket

- Log in to your account in the [AWS Management Console](https://aws.amazon.com/).
- Navigate to your Amazon S3 bucket and then select **Permissions**.
- Edit the bucket policy and add the following permissions:

TIP
IAM_ROLE_TO_ALLOW_LIST
is the IAM role fetched through the API in the previous step. You must replace {YOUR_BUCKET_NAME} with the actual name of your Amazon S3 bucket. If you want to give access to a specific folder, then you must also replace {YOUR_FOLDER_NAME} with the actual name of the folder that you want to give access to.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AEP Get Object Related Policy Prod",
            "Effect": "Allow",
            "Principal": {
                "AWS": "{IAM_ROLE_TO_ALLOW_LIST}"
            },
            "Action": "s3:Get*",
            "Resource": "arn:aws:s3:::{YOUR_BUCKET_NAME}/{YOUR_FOLDER_NAME}"
        },
        {
            "Sid": "AEP List Bucket Prod",
            "Effect": "Allow",
            "Principal": {
                "AWS": "{IAM_ROLE_TO_ALLOW_LIST}"
            },
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::{YOUR_BUCKET_NAME}"
        }
    ]
}
```

### Create a base connection for Amazon S3 on Experience Platform in AWS

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for Amazon S3:

Select to view example
| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "Amazon S3 base connection for Experience Platform on AWS", "description": "Amazon S3 base connection for Experience Platform on AWS", "auth": { "specName": "IAMRole Based", "params": { "bucketName": "{YOUR_BUCKET_NAME}" } }, "connectionSpec": { "id": "ecadc60c-7455-4d87-84dc-2a0e293d997b", "version": "1.0" } }' |

| table 0-row-2 1-row-2 |  |
| --- | --- |
| Property | Description |
| auth.params.bucketName | The name of your Amazon S3 bucket. This is the same value that was added to permissions in the prior step. |

**Response**

A successful response returns details of the newly created connection, including its unique identifier (id). This ID is required to explore your storage in the next tutorial.

Select to view example
| code language-json |
| --- |
| { "id": "4cb0c374-d3bb-4557-b139-5712880adc55", "etag": "\"1700d77b-0000-0200-0000-5e3b41a10000\"" } |

## Next steps

By following this tutorial, you have created an S3 connection using APIs and a unique ID was obtained as part of the response body. You can use this connection ID to [explore cloud storages using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage).

recommendation-more-help
