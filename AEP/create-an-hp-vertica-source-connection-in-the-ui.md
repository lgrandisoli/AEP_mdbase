---
title: "Create an HP Vertica source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/hp-vertica"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:04.376277+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an HP Vertica source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The HP Vertica connector is in beta. See the
Sources overview
for more information on using beta-labeled connectors.
Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced data on a scheduled basis. This tutorial provides steps for creating an HP Vertica source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid HP Vertica connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

The following sections provide additional information that you will need to know in order to successfully connect to HP Vertica using the Flow Service API.

Credential
Description
connectionString
The connection string used to connect to your HP Vertica instance. The connection string pattern for HP Vertica is
Server={SERVER};Port={PORT};Database={DATABASE};UID={USERNAME};PWD={PASSWORD}
For more information about getting started, refer to [this HP Vertica document](https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/ConnectingToVertica/ClientJDBC/CreatingAndConfiguringAConnection.htm).

## Connect your HP Vertica account

Once you have gathered your required credentials, you can follow the steps below to link your HP Vertica account to Experience Platform.

Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Sources** from the left navigation bar to access the **Sources** workspace. The **Catalog** screen displays a variety of sources for which you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the **Databases** category, select **HP Vertica**. If this is your first time using this connector, select **Configure**. Otherwise, select **Add data** to create a new HP Vertica connector.

The **Connect to HP Vertica** page appears. On this page, you can either use new credentials or existing credentials.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your HP Vertica credentials. When finished, select **Connect** and then allow some time for the new connection to establish.

### Existing account

To connect an existing account, select the HP Vertica account you want to connect with, then select **Next** in the top-right corner to proceed.

## Next steps

By following this tutorial, you have established a connection to your HP Vertica account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
