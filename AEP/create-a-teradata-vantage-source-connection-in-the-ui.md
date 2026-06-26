---
title: "Create a Teradata Vantage source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/teradata-vantage"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:16.594046+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Teradata Vantage source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a Teradata Vantage source connector using the Adobe Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Gather required credentials

In order to access your Teradata Vantage account on Experience Platform, you must provide the following authentication value:

Credential
Description
Connection string
A connection string is a string that provides information about a data source and how you can connect to it. The connection string pattern for Teradata Vantage is
DBCName={SERVER};Uid={USERNAME};Pwd={PASSWORD}
.
For more information about getting started, refer to this [Teradata Vantage document](https://docs.teradata.com/r/Teradata-VantageTM-Advanced-SQL-Engine-Security-Administration/July-2021/Setting-Up-the-Administrative-Infrastructure/Controlling-Access-to-the-Operating-System/Working-with-OS-Level-Security-Options).

## Connect your Teradata Vantage account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Databases category, select **Teradata Vantage** and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account exists, this option changes to
Add data
.
The **Connect to Teradata Vantage** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To connect an existing account, select the Teradata Vantage account you want to connect with, then select **Next** to proceed.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your Teradata Vantage credentials. When finished, select **Connect** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have established a connection to your Teradata Vantage account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
