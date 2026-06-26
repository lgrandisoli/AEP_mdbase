---
title: "Create an Azure Data Explorer source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/data-explorer"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:20.923824+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Azure Data Explorer source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced data on a scheduled basis. This tutorial provides steps for creating an Azure Data Explorer (hereinafter referred to as “Data Explorer”) source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Data Explorer connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

In order to access your Data Explorer account on Experience Platform, you must provide the following values:

Credential
Description
endpoint
The endpoint of the Data Explorer server.
database
The name of the Data Explorer database.
tenant
The unique tenant ID used to connect to the Data Explorer database.
servicePrincipalId
The unique service principal ID used to connect to the Data Explorer database.
servicePrincipalKey
The unique service principal key used to connect to the Data Explorer database.
For more information about getting started, refer to [this Data Explorer document](https://docs.microsoft.com/en-us/azure/data-explorer/kusto/management/access-control/how-to-authenticate-with-aad).

## Connect your Azure Data Explorer account

Once you have gathered your required credentials, you can follow the steps below to link your Data Explorer account to Experience Platform.

Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Sources** from the left navigation bar to access the **Sources** workspace. The **Catalog** screen displays a variety of sources for which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the **Databases** category, select **Azure Data Explorer**. If this is your first time using this connector, select **Configure**. Otherwise, select **Add data** to create a new Data Explorer connector.

The **Connect to Azure Data Explorer** page appears. On this page, you can either use new credentials or existing credentials.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your Data Explorer credentials. When finished, select **Connect** and then allow some time for the new connection to establish.

### Existing account

To connect an existing account, select the Data Explorer account you want to connect with, then select **Next** to proceed.

## Next steps

By following this tutorial, you have established a connection to your Data Explorer account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
