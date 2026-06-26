---
title: "Export datasets"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-export/export-datasets"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-export"
created_at: "2026-06-23T20:45:41.606361+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Export datasets

Last update: June 5, 2026
- Topics:
- [Administration](#)
- [Data management](#)
- [Components](#)

CREATED FOR:

- Admin

This article outlines how the Customer Journey Analytics Export datasets can be used to implement the following [data export use case](/en/docs/analytics-platform/using/cja-usecases/data-export/overview):

- Data backup

## Introduction

Exporting data using Experience Platform Export datasets allows you to export data from your Customer Journey Analytics data views to any cloud storage destination.

## More information

You can export raw datasets, from the data lake in Experience Platform, to cloud storage destinations. This export is in Experience Platform Destinations terminology referred to as Dataset export destinations. See [Export datasets to cloud storage destinations](/en/docs/experience-platform/destinations/ui/activate/export-datasets) for an overview.

The following cloud storage destinations are supported:

- [Azure Data Lake Storage Gen2](/en/docs/experience-platform/destinations/catalog/cloud-storage/adls-gen2)
- [Data Landing Zone](/en/docs/experience-platform/destinations/catalog/cloud-storage/data-landing-zone)
- [Google Cloud Storage](/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)
- [Amazon S3](/en/docs/experience-platform/destinations/catalog/cloud-storage/amazon-s3#changelog)
- [Azure Blob](/en/docs/experience-platform/destinations/catalog/cloud-storage/azure-blob#changelog)
- [SFTP](/en/docs/experience-platform/destinations/catalog/cloud-storage/sftp#changelog)

### Experience Platform UI

You can export and schedule the export of your datasets through the Experience Platform UI. This section describes the steps involved.

#### Select destination

When you have determined the cloud storage destination to where you want to export the dataset to, [select the destination](/en/docs/experience-platform/destinations/ui/activate/export-datasets#select-destination). When you have not yet configured a destination for your preferred cloud storage, you must [create a new destination connection](/en/docs/experience-platform/destinations/ui/connect-destination).

As part of configuring a destination, you can define:

- the file type (JSON or Parquet),
- whether the resulting file should be compressed or not, and
- whether a manifest file should be included or not.

#### Select dataset

When you have selected the destination, in the next **Select datasets** step you have to select your dataset from the list of datasets. If you have create multiple scheduled queries, and you want the datasets to send to the same cloud storage destination, you can select the corresponding datasets. See [Select your datasets](/en/docs/experience-platform/destinations/ui/activate/export-datasets#select-datasets) for more information.

#### Schedule dataset export

Finally, you want to schedule your dataset export as part of the **Scheduling** step. In that step you can define the schedule and whether the dataset export should be incremental or not. See [Schedule dataset export](/en/docs/experience-platform/destinations/ui/activate/export-datasets#scheduling) for more information.

#### Final steps

[Review](/en/docs/experience-platform/destinations/ui/activate/export-datasets#review) your selection, and when correct, start exporting your dataset to the cloud storage destination.

First, you must [verify](/en/docs/experience-platform/destinations/ui/activate/export-datasets#verify) a successful data export. When exporting datasets, Experience Platform creates one or multiple .json or .parquet files in the storage location defined in your destination. Expect new files to be deposited in your storage location according to the export schedule you set up. Experience Platform creates a folder structure in the storage location that you specified as part of the selected destination, where it deposits the exported files. A new folder is created for each export time, following the pattern: folder-name-you-provided/datasetID/exportTime=YYYYMMDDHHMM. The default file name is randomly generated and ensures that exported file names are unique.

### Flow Service API

Alternatively, you can export and schedule the export of datasets using APIs. The steps involved are documented in [Export datasets by using the Flow Service API](/en/docs/experience-platform/destinations/api/export-datasets).

#### Get started

To export datasets, ensure you have the [required permissions](/en/docs/experience-platform/destinations/api/export-datasets#permissions). Also verify that the destination to where you want to send your dataset supports exporting datasets. You then must [gather the values for required and optional headers](/en/docs/experience-platform/destinations/api/export-datasets#gather-values-headers) that you use in the API calls. You also need to [identify the connection spec and flow spec IDs of the destination](/en/docs/experience-platform/destinations/api/export-datasets#gather-connection-spec-flow-spec) you are intending to export datasets to.

#### Retrieve eligible datasets

You can [retrieve a list of eligible datasets](/en/docs/experience-platform/destinations/api/export-datasets#retrieve-list-of-available-datasets) for export and verify whether your dataset is part of that list using the [GET /connectionSpecs/{id}/configs](https://developer.adobe.com/experience-platform-apis/references/destinations/#tag/Configurations/operation/getDatasets) API.

#### Create source connection

Next, you must [create a source connection](/en/docs/experience-platform/destinations/api/export-datasets#create-source-connection) for the dataset, using its unique ID, that you want to export to the cloud storage destination. You use the [POST /sourceConnections](https://developer.adobe.com/experience-platform-apis/references/destinations/#tag/Source-connections/operation/postSourceConnection) API.

#### Authenticate to destination (create base connection)

You now must [create a base connection](/en/docs/experience-platform/destinations/api/export-datasets#create-base-connection) to authenticate and securely store the credentials to your cloud storage destination using the [POST /targetConection](https://developer.adobe.com/experience-platform-apis/references/destinations/#tag/Target-connections/operation/postTargetConnection) API.

#### Provide export parameters

Next, you must [create an additional target connection that stores the export parameters](/en/docs/experience-platform/destinations/api/export-datasets#create-target-connection) for your dataset using, once more, the [POST /targetConection](https://developer.adobe.com/experience-platform-apis/references/destinations/#tag/Target-connections/operation/postTargetConnection) API. These export parameters include location, file format, compression, and more.

#### Set up dataflow

Finally, you [set up the dataflow](/en/docs/experience-platform/destinations/api/export-datasets#create-dataflow) to ensure that your dataset is exported to your cloud storage destination using the [POST /flows](https://developer.adobe.com/experience-platform-apis/references/destinations/#tag/Dataflows/operation/postFlow) API. In this step, you can define the schedule for the export, using the scheduleParams parameter.

#### Validate dataflow

To [check successful executions of your dataflow](/en/docs/experience-platform/destinations/api/export-datasets#get-dataflow-runs), use the [GET /runs](https://developer.adobe.com/experience-platform-apis/references/destinations/#tag/Dataflow-runs/operation/getFlowRuns) API, specifying the dataflow ID as query parameter. This dataflow ID is an identifier returned when you set up the dataflow.

[Verify](/en/docs/experience-platform/destinations/ui/activate/export-datasets#verify) a successful data export. When exporting datasets, Experience Platform creates one or multiple .json or .parquet files in the storage location defined in your destination. Expect new files to be deposited in your storage location according to the export schedule you set up. Experience Platform creates a folder structure in the storage location that you specified as part of the selected destination, where it deposits the exported files. A new folder is created for each export time, following the pattern: folder-name-you-provided/datasetID/exportTime=YYYYMMDDHHMM. The default file name is randomly generated and ensures that exported file names are unique.

recommendation-more-help
