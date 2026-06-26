---
title: "Use Destination SDK to configure a file-based destination"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/destinations/destination-sdk/guides/configure-file-based-destination-instructions"
category: "guides"
topic: "experience-platform/destinations-guide"
created_at: "2026-06-26T17:28:27.067048+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Destinations Guide

# Use Destination SDK to configure a file-based destination

Last update: May 23, 2026
- Topics:
- [Destinations](#)

CREATED FOR:

- Admin
- User

## Overview overview

This page describes how to use the information in [Configuration options in Destinations SDK](/en/docs/experience-platform/destinations/destination-sdk/functionality/configuration-options) and in other Destination SDK functionality and API reference documents to configure a [file-based destination](/en/docs/experience-platform/destinations/destination-types#file-based). The steps are laid out in sequential order below.

## Prerequisites prerequisites

Before advancing to the steps illustrated below, read the [Destination SDK getting started](/en/docs/experience-platform/destinations/destination-sdk/getting-started) page for information on obtaining the necessary Adobe I/O authentication credentials and other prerequisites to work with Destination SDK APIs.

## Steps to use the configuration options in Destination SDK to set up your destination steps

## Step 1: Create a server and file configuration create-server-file-configuration

Start by [creating a server and file configuration](/en/docs/experience-platform/destinations/destination-sdk/authoring-api/server-operations/create-destination-server) using the /destinations-server endpoint.

Shown below is an example configuration for an Amazon S3 destination. For more details about the fields used in the configuration and to configure other types of file-based destinations, see their corresponding [server configurations](/en/docs/experience-platform/destinations/destination-sdk/functionality/destination-server/server-specs).

**API format**

```
POST platform.adobe.io/data/core/activation/authoring/destination-servers
```

```
{
    "name": "S3 destination",
    "destinationServerType": "FILE_BASED_S3",
    "fileBasedS3Destination": {
        "bucket": {
            "templatingStrategy": "PEBBLE_V1",
            "value": "{{customerData.bucketName}}"
        },
        "path": {
            "templatingStrategy": "PEBBLE_V1",
            "value": "{{customerData.path}}"
        }
    },
    "fileConfigurations": {
        "compression": {
            "templatingStrategy": "PEBBLE_V1",
            "value": "{{customerData.compression}}"
        },
        "fileType": {
            "templatingStrategy": "PEBBLE_V1",
            "value": "{{customerData.fileType}}"
        },
        "csvOptions": {
            "quote": {
                "templatingStrategy": "NONE",
                "value": "\""
            },
            "quoteAll": {
                "templatingStrategy": "NONE",
                "value": "false"
            },
            "escape": {
                "templatingStrategy": "NONE",
                "value": "\\"
            },
            "escapeQuotes": {
                "templatingStrategy": "NONE",
                "value": "true"
            },
            "header": {
                "templatingStrategy": "NONE",
                "value": "true"
            },
            "ignoreLeadingWhiteSpace": {
                "templatingStrategy": "NONE",
                "value": "true"
            },
            "ignoreTrailingWhiteSpace": {
                "templatingStrategy": "NONE",
                "value": "true"
            },
            "nullValue": {
                "templatingStrategy": "NONE",
                "value": ""
            },
            "dateFormat": {
                "templatingStrategy": "NONE",
                "value": "yyyy-MM-dd"
            },
            "timestampFormat": {
                "templatingStrategy": "NONE",
                "value": "yyyy-MM-dd'T':mm:ss[.SSS][XXX]"
            },
            "charToEscapeQuoteEscaping": {
                "templatingStrategy": "NONE",
                "value": "\\"
            },
            "emptyValue": {
                "templatingStrategy": "NONE",
                "value": ""
            }
        }
    }
}
```

## Step 2: Create destination configuration create-destination-configuration

Shown below is an example of a destination configuration, created by using the /destinations API endpoint.

To connect the server and file configuration from step 1 to this destination configuration, add the instance ID of the server and file configuration as destinationServerId here.

**API format**

```
POST platform.adobe.io/data/core/activation/authoring/destinations
```

```
{
    "name": "Amazon S3 destination",
    "description": "Amazon S3 destination is a fictional destination, used for this example.",
    "status": "Test",
    "customerAuthenticationConfigurations": [
        {
            "authType": "S3"
        }
    ],
    "customerEncryptionConfigurations": [],
    "customerDataFields": [
        {
            "name": "bucketName",
            "title": "Amazon S3 bucket name",
            "description": "Enter the Amazon S3 Bucket name that will host the exported files.",
            "type": "string",
            "isRequired": true,
            "pattern": "(?=^.{3,63}$)(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)",
            "readOnly": false,
            "hidden": false
        },
        {
            "name": "path",
            "title": "Amazon S3 path",
            "description": "Enter Amazon S3 folder path",
            "type": "string",
            "isRequired": true,
            "pattern": "^[0-9a-zA-Z\\/\\!\\-_\\.\\*\\''\\(\\)]*((\\%SEGMENT_(NAME|ID)\\%)?\\/?)+$",
            "readOnly": false,
            "hidden": false
        },
        {
            "name": "compression",
            "title": "Select compression type",
            "description": "Select the file compression type used by the exported files.",
            "type": "string",
            "isRequired": true,
            "readOnly": false,
            "enum": [
                "GZIP",
                "NONE",
                "bzip2",
                "lz4",
                "snappy",
                "deflate"
            ]
        },
        {
            "name": "fileType",
            "title": "Select a file format",
            "description": "Select the file format to be used by the exported files.",
            "type": "string",
            "isRequired": true,
            "readOnly": false,
            "hidden": false,
            "enum": [
                "csv",
                "json",
                "parquet"
            ],
            "default": "csv"
        }
    ],
    "uiAttributes": {
        "documentationLink": "https://www.adobe.com/go/destinations-YOURDESTINATION-en",
        "category": "S3",
        "connectionType": "S3",
        "flowRunsSupported": true,
        "monitoringSupported": true,
        "frequency": "Batch"
    },
    "destinationDelivery": [
        {
            "deliveryMatchers": [
                {
                    "type": "SOURCE",
                    "value": [
                        "batch"
                    ]
                }
            ],
            "authenticationRule": "CUSTOMER_AUTHENTICATION",
            "destinationServerId": "eec25bde-4f56-4c02-a830-9aa9ec73ee9d"
        }
    ],
    "schemaConfig": {
        "profileRequired": true,
        "segmentRequired": true,
        "identityRequired": true
    },
    "batchConfig": {
        "allowMandatoryFieldSelection": true,
        "allowDedupeKeyFieldSelection": true,
        "defaultExportMode": "DAILY_FULL_EXPORT",
        "allowedExportMode": [
            "DAILY_FULL_EXPORT",
            "FIRST_FULL_THEN_INCREMENTAL"
        ],
        "allowedScheduleFrequency": [
            "DAILY",
            "EVERY_3_HOURS",
            "EVERY_6_HOURS",
            "EVERY_8_HOURS",
            "EVERY_12_HOURS",
            "ONCE"
        ],
        "defaultFrequency": "DAILY",
        "defaultStartTime": "00:00",
       "filenameConfig":{
         "allowedFilenameAppendOptions":[
            "SEGMENT_NAME",
            "DESTINATION_INSTANCE_ID",
            "DESTINATION_INSTANCE_NAME",
            "ORGANIZATION_NAME",
            "SANDBOX_NAME",
            "DATETIME",
            "CUSTOM_TEXT"
         ],
         "defaultFilenameAppendOptions":[
            "DATETIME"
         ],
         "defaultFilename":"%DESTINATION%_%SEGMENT_ID%"
      }
    },
    "backfillHistoricalProfileData": true
}
```

## Step 3: Create audience metadata configuration create-audience-metadata-configuration

For some destinations, Destination SDK requires that you configure an audience metadata configuration to programmatically create, update, or delete audiences in your destination. See [Audience metadata management](/en/docs/experience-platform/destinations/destination-sdk/functionality/audience-metadata-management) for information on when you need to set up this configuration and how to do it.

If you use an audience metadata configuration, you must connect it to the destination configuration you created in step 2. Add the instance ID of your audience metadata configuration to your destination configuration as audienceTemplateId.

```
{
    "name": "Amazon S3 destination",
    "description": "Amazon S3 destination is a fictional destination, used for this example.",
    "status": "Test",
    "customerAuthenticationConfigurations": [
        {
            "authType": "S3"
        }
    ],
    "customerEncryptionConfigurations": [],
    "customerDataFields": [
        {
            "name": "bucketName",
            "title": "Amazon S3 bucket name",
            "description": "Enter the Amazon S3 Bucket name that will host the exported files.",
            "type": "string",
            "isRequired": true,
            "pattern": "(?=^.{3,63}$)(?!^(\\d+\\.)+\\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])\\.)*([a-z0-9]|[a-z0-9][a-z0-9\\-]*[a-z0-9])$)",
            "readOnly": false,
            "hidden": false
        },
        {
            "name": "path",
            "title": "Amazon S3 path",
            "description": "Enter Amazon S3 folder path",
            "type": "string",
            "isRequired": true,
            "pattern": "^[0-9a-zA-Z\\/\\!\\-_\\.\\*\\''\\(\\)]*((\\%SEGMENT_(NAME|ID)\\%)?\\/?)+$",
            "readOnly": false,
            "hidden": false
        },
        {
            "name": "compression",
            "title": "Select compression type",
            "description": "Select the file compression type used by the exported files.",
            "type": "string",
            "isRequired": true,
            "readOnly": false,
            "enum": [
                "GZIP",
                "NONE",
                "bzip2",
                "lz4",
                "snappy",
                "deflate"
            ]
        },
        {
            "name": "fileType",
            "title": "Select a file format",
            "description": "Select the file format to be used by the exported files.",
            "type": "string",
            "isRequired": true,
            "readOnly": false,
            "hidden": false,
            "enum": [
                "csv",
                "json",
                "parquet"
            ],
            "default": "csv"
        }
    ],
    "uiAttributes": {
        "documentationLink": "http://www.adobe.com/go/destinations-YOURDESTINATION-en",
        "category": "S3",
        "connectionType": "S3",
        "flowRunsSupported": true,
        "monitoringSupported": true,
        "frequency": "Batch"
    },
    "destinationDelivery": [
        {
            "deliveryMatchers": [
                {
                    "type": "SOURCE",
                    "value": [
                        "batch"
                    ]
                }
            ],
            "authenticationRule": "CUSTOMER_AUTHENTICATION",
            "destinationServerId": "eec25bde-4f56-4c02-a830-9aa9ec73ee9d"
        }
    ],
    "segmentMappingConfig":{
        "mapExperiencePlatformSegmentName":false,
        "mapExperiencePlatformSegmentId":false,
        "mapUserInput":false
    },
    "audienceMetadataConfig":{
        "audienceTemplateId":"cbf90a70-96b4-437b-86be-522fbdaabe9c"
    },
    "schemaConfig": {
        "profileRequired": true,
        "segmentRequired": true,
        "identityRequired": true
    },
    "batchConfig": {
        "allowMandatoryFieldSelection": true,
        "allowDedupeKeyFieldSelection": true,
        "defaultExportMode": "DAILY_FULL_EXPORT",
        "allowedExportMode": [
            "DAILY_FULL_EXPORT",
            "FIRST_FULL_THEN_INCREMENTAL"
        ],
        "allowedScheduleFrequency": [
            "DAILY",
            "EVERY_3_HOURS",
            "EVERY_6_HOURS",
            "EVERY_8_HOURS",
            "EVERY_12_HOURS",
            "ONCE"
        ],
        "defaultFrequency": "DAILY",
        "defaultStartTime": "00:00",
       "filenameConfig":{
         "allowedFilenameAppendOptions":[
            "SEGMENT_NAME",
            "DESTINATION_INSTANCE_ID",
            "DESTINATION_INSTANCE_NAME",
            "ORGANIZATION_NAME",
            "SANDBOX_NAME",
            "DATETIME",
            "CUSTOM_TEXT"
         ],
         "defaultFilenameAppendOptions":[
            "DATETIME"
         ],
         "defaultFilename":"%DESTINATION%_%SEGMENT_ID%"
      }
    },
    "backfillHistoricalProfileData": true
}
```

## Step 4: Set up authentication set-up-authentication

Depending on whether you specify "authenticationRule": "CUSTOMER_AUTHENTICATION" or "authenticationRule": "PLATFORM_AUTHENTICATION" in the destination configuration above, you can set up authentication for your destination by using the /destination or the /credentials endpoint.

NOTE
CUSTOMER_AUTHENTICATION
is the more common of the two authentication rules and is the one to use if you require users to provide some form of authentication to your destination before they can set up a connection and export data.
- If you selected "authenticationRule": "CUSTOMER_AUTHENTICATION" in the destination configuration, see the following sections for the authentication types supported by Destination SDK for file-based destinations: Amazon S3 authentication Azure Blob Azure Data Lake Storage Google Cloud Storage SFTP authentication with SSH key SFTP authentication with password
- If you selected "authenticationRule": "PLATFORM_AUTHENTICATION" , you must create a credentials configuration and pass the credential object’s ID in the authenticationId parameter in the destination delivery configuration.

## Step 5: Test your destination test-destination

After setting up your destination using the configuration endpoints in the previous steps, you can use the [destination testing tool](/en/docs/experience-platform/destinations/destination-sdk/testing-api/batch-destinations/file-based-destination-testing-overview) to test the integration between Adobe Experience Platform and your destination.

As part of the process to test your destination, you must use the Experience Platform UI to create audiences, which you will activate to your destination. Refer to the two resources below for instructions how to create audiences in Experience Platform:

- [Create an audience - documentation page](/en/docs/experience-platform/segmentation/ui/audience-portal#create-audience)
- [Create an audience - video walkthrough](/en/docs/platform-learn/tutorials/audiences/create-audiences)

## Step 6: Publish your destination publish-destination

NOTE
This step is not required if you are creating a private destination for your own use, and are not looking to publish it in the destinations catalog for other customers to use.
After configuring and testing your destination, use the [destination publishing API](/en/docs/experience-platform/destinations/destination-sdk/publishing-api/create-publishing-request) to submit your configuration to Adobe for review.

## Step 7: Document your destination document-destination

NOTE
This step is not required if you are creating a private destination for your own use, and are not looking to publish it in the destinations catalog for other customers to use.
If you are an Independent Software Vendor (ISV) or System Integrator (SI) creating a [productized integration](/en/docs/experience-platform/destinations/destination-sdk/overview#productized-custom-integrations), use the [self-service documentation process](/en/docs/experience-platform/destinations/destination-sdk/document-destination/documentation-instructions) to create a product documentation page for your destination in the [Experience Platform destinations catalog](/en/docs/experience-platform/destinations/catalog/overview).

## Step 8: Submit destination for Adobe’s review submit-for-review

NOTE
This step is not required if you are creating a private destination for your own use, and are not looking to publish it in the destinations catalog for other customers to use.
Finally, before the destination can be published in the Experience Platform catalog and visible to all Experience Platform customers, you need to officially submit the destination for Adobe’s review. Find complete information about how to [submit for review a productized destination authored in Destination SDK](/en/docs/experience-platform/destinations/destination-sdk/guides/submit-destination).

recommendation-more-help
