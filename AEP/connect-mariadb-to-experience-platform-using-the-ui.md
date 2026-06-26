---
title: "Connect MariaDB to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/mariadb"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:07.110170+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect MariaDB to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your MariaDB account to Adobe Experience Platform using the sources workspace in the Experience Platform user interface.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a MariaDB connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

Read the [MariaDB overview](/en/docs/experience-platform/sources/connectors/databases/mariadb#prerequisites) for information on authentication.

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Select the appropriate category in the *Categories* panel Alternatively, use the search bar to navigate to the specific source that you want to use.

To use MariaDB, select the **MariaDB** source card under *Databases* and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Use an existing account existing

To use an existing account, select **Existing account** and then select the MariaDB account that you want to use.

## Create a new account create

If you do not have an existing account, then you must create a new account by providing the necessary authentication credentials that correspond with your source.

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform

You can connect your MariaDB account to Experience Platform using either account key or basic authentication.

Account key authentication
To use account key authentication, select **Account key authentication**, provide your [connection string](/en/docs/experience-platform/sources/connectors/databases/mariadb#azure), and then select **Connect to source**.

Basic authentication
To use basic authentication, select **Basic authentication**, provide values for your [authentication credentials](/en/docs/experience-platform/sources/connectors/databases/mariadb#azure), and then select **Connect to source**.

By following this tutorial, you have established a connection to your MariaDB account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
