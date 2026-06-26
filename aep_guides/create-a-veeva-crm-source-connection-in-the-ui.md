---
title: "Create a Veeva CRM source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/crm/veeva"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:05.365061+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Veeva CRM source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced CRM data on a scheduled basis. This tutorial provides steps for creating a Veeva CRM source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Veeva CRM account, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

### Gather required credentials

Credential
Description
environmentUrl
The URL of the Veeva CRM source instance.
username
The username for the Veeva CRM user account.
password
The password for the Veeva CRM user account.
securityToken
The security token for the Veeva CRM user account.
For more information on getting started, refer to this [Veeva CRM document](https://developer.veevacrm.com/doc/Content/rest-api.htm).

## Connect your Veeva CRM account

Once you have gathered your required credentials, you can follow the steps below to link your Veeva CRM account to Experience Platform.

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources for which you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the CRM category, select **Veeva CRM**, and then select **Add data**.

The **Connect Veeva CRM account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the Veeva CRM account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your Veeva CRM credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have established a connection to your Veeva CRM account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

recommendation-more-help
