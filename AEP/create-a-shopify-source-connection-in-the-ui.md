---
title: "Create a Shopify source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/ecommerce/shopify"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:00:15.238322+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Shopify source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Use this guide to connect your Shopify account to Adobe Experience Platform through the Sources workspace in the UI.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a Shopify connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow for an eCommerce connector](/en/docs/experience-platform/sources/ui-tutorials/dataflow/ecommerce).

### Gather required credentials

You must have valid Shopify authentication credentials to create a base connection. For details on the required credentials and how to obtain them, refer to the [Shopify source connector overview](/en/docs/experience-platform/sources/connectors/ecommerce/shopify#prerequisites).

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Select the appropriate category in the *Categories* panel. Alternatively, use the search bar to navigate to the specific source that you want to use.

To ingest data from Shopify, select the **Shopify** source card under *eCommerce* and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
### Existing account

If you already have a Shopify account set up, select it from the list and then select **Next** to continue.

### New account

If you are adding a new account, select **New account**. In the input form, enter a name, an optional description, and your Shopify credentials. Shopify supports two authentication methods:

**Basic authentication**: Enter your store’s host and access token in the basic authentication section.

**Access token based authentication**: Enter your store’s host and access token in the access token section.

After entering your credentials for the appropriate authentication method, select **Connect** and allow a few moments for the new connection to be established.

## Next steps

By following this tutorial, you have established a connection to your Shopify account. You can now continue on to the next tutorial and [configure a dataflow to bring eCommerce data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/ecommerce).

recommendation-more-help
