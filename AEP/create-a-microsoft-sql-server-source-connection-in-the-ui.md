---
title: "Create a Microsoft SQL Server source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/sql-server"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:11.699946+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Microsoft SQL Server source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this tutorial to learn how to connect your Microsoft SQL Server account to Adobe Experience Platform using the user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid SQL Server connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

In order to connect to SQL Server on Experience Platform, you must provide the following connection property:

Credential
Description
Connection string
The connection string associated with your Microsoft SQL Server account. Your connection string pattern depends whether you are using server name or instance name for your data source:

- Connection string using server name: Data Source={SERVER_NAME};Initial Catalog={DATABASE};Integrated Security=False;User ID={USER_ID};Password={PASSWORD};
- Connection string using instance name:Data Source={INSTANCE_NAME};Initial Catalog={DATABASE};Integrated Security=False;User ID={USER_ID};Password={PASSWORD};Data Source=mssqlserver.database.windows.net;Initial Catalog=mssqlserver_e2e_db;Integrated Security=False;User ID=mssqluser;Password=mssqlpassword

For more information about getting started, refer to [this SQL Server document](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/authentication-in-sql-server).

## Connect your SQL Server account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Databases* category, select **Microsoft SQL Server**, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account exists, this option changes to
Add data
.
The **Connect to Microsoft SQL Server** page appears. On this page, you can either use new credentials or existing credentials.

Create a new account
To create a new account, select **New account** and provide a name, an optional description, and your credentials.

When finished, select **Connect to source** and then allow some time for the new connection to establish.

Use an existing account
To use an existing account, select **Existing account** and then select the account that you want to use from the existing account catalog.

Select **Next** to proceed.

## Next steps

By following this tutorial, you have established a connection to your SQL Server account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
