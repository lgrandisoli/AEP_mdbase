---
title: "Create a ServiceNow source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/customer-success/servicenow"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:11.835356+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a ServiceNow source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced data on a scheduled basis. This tutorial provides steps for creating a ServiceNow source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid ServiceNow connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/customer-success)

### Gather required credentials

In order to access your ServiceNow account on Experience Platform, you must provide the following values:

Credential
Description
endpoint
The endpoint of the ServiceNow server.
username
The username used to connect to the ServiceNow server for authentication.
password
The password to connect to the ServiceNow server for authentication.
For more information about getting started, refer to [this ServiceNow document](https://developer.servicenow.com/app.do#!/rest_api_doc?v=newyork&id=r_TableAPI-GET).

## Connect your ServiceNow account

Once you have gathered your required credentials, you can follow the steps below to link your ServiceNow account to Experience Platform.

Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Sources** from the left navigation bar to access the **Sources** workspace. The **Catalog** screen displays a variety of sources for which you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the **Customer Success** category, select **ServiceNow**. If this is your first time using this connector, select **Configure**. Otherwise, select **Connect source** to create a new ServiceNow connector.

The **Connect to ServiceNow** page appears. On this page, you can either use new credentials or existing credentials.

### New account

If you are using new credentials, select **New account**. On the input form that appears, provide a name, an optional description, and your ServiceNow credentials. When finished, select **Connect** and then allow some time for the new connection to establish.

### Existing account

To connect an existing account, select the ServiceNow account you want to connect with, then select **Next** to proceed.

## Next steps

By following this tutorial, you have established a connection to your ServiceNow account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/customer-success).

recommendation-more-help
