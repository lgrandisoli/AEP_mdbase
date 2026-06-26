---
title: "Connect Oracle DB to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/oracle"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:13.846451+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Oracle DB to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your Oracle DB instance to Adobe Experience Platform using the sources workspace in the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have an Oracle DB connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

Read the [Oracle DB overview](/en/docs/experience-platform/sources/connectors/databases/oracle#prerequisites) for information on authentication.

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to Oracle DB, go to the *Databases* category, select the **Oracle DB** source card, and then select **Set up**.

TIP
Sources show
Set up
for new connections and
Add data
if an account already exists.
## Use an existing account existing

To use an existing account, select **Existing account** and then select the Oracle DB account that you want to use.

## Create a new account new

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform on Azure azure

You can connect your Oracle DB database to Experience Platform on Azure using a connection string.

To use connection string authentication, provide your [connection string](/en/docs/experience-platform/sources/connectors/databases/oracle#azure) and select **Connect to source**.

### Connect to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
To create a new Oracle DB account and connect to Experience Platform on AWS, ensure that you are in a VA6 sandbox and then provide the necessary [credentials for authentication](/en/docs/experience-platform/sources/connectors/databases/oracle#aws).

## Create a dataflow for Oracle DB data

Now that you have successfully connected your Oracle DB database, you can now [create a dataflow and ingest data from your database into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
