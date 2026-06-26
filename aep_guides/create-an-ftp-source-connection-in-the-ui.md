---
title: "Create an FTP source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/ftp"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:40.958759+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an FTP source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The FTP connector is in beta. See the
Sources overview
for more information on using beta-labeled connectors.
This tutorial provides steps for creating an FTP source connection using the Adobe Experience Platform UI.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid FTP connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

### Gather required credentials

In order to connect to FTP, you must provide values for the following connection properties:

Credential
Description
host
The name or IP address associated with your FTP server.
username
The username with access to your FTP server.
password
The password for your FTP server.
## Connect to your FTP server

Once you have gathered your required credentials, you can follow the steps below to create a new FTP account to connect to Experience Platform.

Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources for which you can create an inbound account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Cloud storage category, select **FTP**. If this is your first time using this connector, select **Configure**. Otherwise, select **Add data** to create a new FTP connection.

The **Connect to FTP** page appears. On this page, you can either use new credentials or existing credentials.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your credentials. When finished, select **Connect** and then allow some time for the new connection to establish.

### Existing account

To connect an existing account, select the FTP account you want to connect with, then select **Next** to proceed.

## Next steps

By following this tutorial, you have established a connection to your FTP account. You can now continue on to the next tutorial and [configure a dataflow to bring data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

recommendation-more-help
