---
title: "Create a Amazon S3 source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/s3"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T16:56:01.367905+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Amazon S3 source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced data on a scheduled basis. This tutorial provides steps for creating an Amazon S3 (hereinafter referred to as “S3”) source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid S3 connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

### Gather required credentials

In order to access your S3 bucket on Experience Platform, you need to provide valid values for the following credentials:

Credential
Description
s3AccessKey
The access key ID for your S3 bucket.
s3SecretKey
The secret key ID for your S3 bucket.
serviceUrl
(Optional) The custom S3 endpoint to connect to. This field is required when your S3 bucket is region-specific. The format for
serviceUrl
is:
https://s3.{REGION}.amazonaws.com/)
.
bucketName
The S3 bucket contains your data and its corresponding descriptive metadata. Your S3 bucket name must be between three and 63 characters long and must begin and end with either a letter or a number. The bucket name can only have lowercase letters, numbers, or hyphens (
-
), and cannot be formatted as an IP address.
folderPath
The path to the folder in your S3 bucket where your data is stored. This credential is required when the user has restricted access.
For more information on getting started, visit [this AWS document](https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/).

## Connect your S3 account

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources for which you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the **Cloud storage** category, select **Amazon S3** and then select **Add data**.

The **Connect to Amazon S3** page appears. On this page, you can either use new credentials or existing credentials.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your S3 credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

### Existing account

To connect an existing account, select the S3 account you want to connect with, then select **Next** to proceed.

## Next steps and additional resources

By following this tutorial, you have established a connection to your S3 account. You can now continue on to the next tutorial and [configure a dataflow to bring data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

recommendation-more-help
