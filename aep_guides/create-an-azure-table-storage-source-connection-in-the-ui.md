---
title: "Create an Azure Table Storage source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/ats"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:22.830412+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Azure Table Storage source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced data on a scheduled basis. This tutorial provides steps for creating a Azure Table Storage (hereinafter referred to as “ATS”) source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid ATS connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

In order to access your ATS account on Experience Platform, you must provide the following values:

Credential
Description
connectionString
A connection string to connect to your Azure Table Storage instance. The connection string to connect to ATS instance. The connection string pattern for ATS is
DefaultEndpointsProtocol=https;AccountName={ACCOUNT_NAME};AccountKey={ACCOUNT_KEY}
.
For more information about getting started, refer to [this Azure Table Storage document](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction).

## Connect your Azure Table Storage account

Once you have gathered your required credentials, you can follow the steps below to link your ATS account to Experience Platform.

Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Sources** from the left navigation bar to access the **Sources** workspace. The **Catalog** screen displays a variety of sources for which you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the **Databases** category, select **Azure Table Storage**. If this is your first time using this connector, select **Configure**. Otherwise, select **Add data** to create a new ATS connector.

The **Connect to Azure Table Storage** page appears. On this page, you can either use new credentials or existing credentials.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your ATS credentials. When finished, select **Connect** and then allow some time for the new connection to establish.

### Existing account

To connect an existing account, select the ATS account you want to connect with, then select **Next** to proceed.

## Next steps

By following this tutorial, you have established a connection to your ATS account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
