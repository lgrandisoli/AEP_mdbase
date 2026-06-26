---
title: "Create a Google Cloud Storage source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/google-cloud-storage"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:41.313631+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Google Cloud Storage source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a Google Cloud Storage source connection using the Adobe Experience Platform UI.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Google Cloud Storage connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

### Supported file formats

Experience Platform supports the following file formats to be ingested from external storages:

- Delimiter-separated values (DSV): Any single-character value can be used as a delimiter for DSV-formatted data files.
- JavaScript Object Notation (JSON): JSON formatted data files must be XDM compliant.
- Apache Parquet: Parquet formatted data files must be XDM compliant.

### Gather required credentials

In order to access your Google Cloud Storage data on Experience Platform, you must provide the following values:

Credential
Description
Access key ID
A 61-character, alphanumeric string used to authenticate your Google Cloud Storage account to Experience Platform.
Secret access key
A 40-character, base-64-encoded string used to authenticate your Google Cloud Storage account to Experience Platform.
Bucket name
The name of your Google Cloud Storage bucket. You must specify a bucket name if you want to provide access to a specific subfolder in your cloud storage.
Folder path
The path to the folder that you want to provide access to.
For more information about these values, see the [Google Cloud Storage HMAC keys](https://cloud.google.com/storage/docs/authentication/hmackeys#overview) guide. For steps on how to generate your own access key ID and secret access key, refer to the [Google Cloud Storage overview](/en/docs/experience-platform/sources/connectors/cloud-storage/google-cloud-storage).

Once you have gathered your required credentials, you can follow the steps below to link your Google Cloud Storage account to Experience Platform.

## Connect your Google Cloud Storage account

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Cloud storage category, select **Google Cloud Storage** and then select **Add data**.

The **Connect to Google Cloud Storage** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To connect an existing account, select the Google Cloud Storage account you want to connect with, then select **Next** to proceed.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your Google Cloud Storage credentials. During this step, you can also designate the subfolders that your account will have access to by defining the name of the path to the subfolder.

When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have established a connection to your Google Cloud Storage account. You can now continue on to the next tutorial and [configure a dataflow to bring data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

recommendation-more-help
