---
title: "Connect Azure Blob Storage to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/blob"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:35.324993+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Azure Blob Storage to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect yourAzure Blob Storage instance to Adobe Experience Platform using the sources workspace in the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework for organizing customer experience data in Experience Platform. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Azure Blob Storage connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

### Supported file formats

Experience Platform supports the following file formats to be ingested from external storages:

- Delimiter-separated values (DSV): You can use any single column delimiter such as a tab, comma, pipe, semicolon, or hash to collect flat files in any format.
- JavaScript Object Notation (JSON): JSON formatted data files must be XDM compliant.
- Apache Parquet: Parquet formatted data files must be XDM compliant.

### Gather required credentials

Read the [Azure Blob Storage overview](/en/docs/experience-platform/sources/connectors/cloud-storage/blob#authentication) for information on authentication.

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to Azure Blob Storage, go to the *Cloud storage* category, select the **Azure Blob Storage** source card, and then select **Set up**.

TIP
Sources show
Set up
for new connections and
Add data
if an account already exists.
## Use an existing account

To use an existing account, select **Existing account** and then select the Azure Blob Storage account that you want to use.

## Create a new account

To create a new account, select **New account** and then provide a name and optionally add a description for your account. You can connect your Azure Blob Storage account to Experience Platform using the following authentication types:

- **Account key authentication**: Uses the storage account’s access key to authenticate and connect to your Azure Blob Storage account.
- **Shared access signature (SAS)**: Uses a SAS URI to provide delegated, time-limited access to resources in your Azure Blob Storage account.
- **Service principal based authentication**: Uses an Azure Active Directory (AAD) service principal (client ID and secret) to securely authenticate to your Azure Blob Storage account.

Account key authentication
Select **Account key authentication** and provide your connectionString, container, and folderPath. Next, select **Connect to source** and allow for a few moments for the connection to establish.

Shared access signature
Select **Shared access signature** and provide your sasUri, container, and folderPath. Next, select **Connect to source** and allow for a few moments for the connection to establish.

Service principal based authentication
Select **Service principal based authentication** and provide your serviceEndpoint, servicePrincipalId, servicePrincipalKey, accountKind, tenant, container, and folderPath. Next, select **Connect to source** and allow for a few moments for the connection to establish.

## Next steps

By following this tutorial, you have established a connection to your Azure Blob Storage account. You can now continue on to the next tutorial and [configure a dataflow to bring data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

recommendation-more-help
