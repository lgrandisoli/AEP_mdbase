---
title: "Create a Square source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/payments/square"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:38:28.647965+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Square source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a Square source connector using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

### Gather required credentials

In order to access your Square account Experience Platform, you must provide the following values:

Credential
Description
Host
The URL of the Square instance.
Client ID
The client ID associated with your Square account.
Client secret
The client secret associated with your Square account.
Access token
The access token is used to authenticate your Square account with OAuth 2.0 authentication. The access token can be obtained from Square.
Refresh token
The refresh token is used to generate new access tokens once your current access token expires. The refresh token can be obtained from Square.
For more information on these credentials and how to obtain them, see the [Square documentation on OAuth](https://developer.squareup.com/docs/oauth-api/receive-and-manage-tokens).

Once you have gathered your required credentials, you can follow the steps below to link your Square account to Experience Platform.

## Connect your Square account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Payments category, select **Square**, and then select **Add data**.

The **Connect to Square** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the Square account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and the appropriate values for your Square credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have authenticated and created a source connection between your Square account and Experience Platform. You can now continue on to the next tutorial and [create a dataflow to bring payments data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/payments).

recommendation-more-help
