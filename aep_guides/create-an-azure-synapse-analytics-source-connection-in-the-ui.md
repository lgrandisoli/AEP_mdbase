---
title: "Create an Azure Synapse Analytics source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/synapse-analytics"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:08.293545+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Create an Azure Synapse Analytics source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Azure Synapse Analytics source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this guide to learn how to connect your Azure Synapse Analytics account to Adobe Experience Platform using the sources workspace in the UI.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Azure Synapse Analytics connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

Read the [Azure Synapse Analytics overview](/en/docs/experience-platform/sources/connectors/databases/synapse-analytics#prerequisites) for information on authentication.

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to Azure Synapse Analytics, go to the *Databases* category, select the **Azure Synapse analytics** source card, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Use an existing account existing

To use an existing account, select **Existing account** and then select the Azure Synapse Analytics account that you want to use.

## Create a new account new

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform

You can connect your Azure Synapse Analytics account to Experience Platform using either account key authentication or service principal and key authentication.

Account key authentication
To use account key authentication, select **Account key authentication**, provide your [connection string](/en/docs/experience-platform/sources/connectors/databases/synapse-analytics#prerequisites), and then select **Connect to source**.

Service principal and key authentication
Alternatively, select **Service principal and key authentication**, provide values for your [authentication credentials](/en/docs/experience-platform/sources/connectors/databases/synapse-analytics#prerequisites), and then select **Connect to source**.

## Create a dataflow for Azure Synapse Analytics data

Now that you have successfully connected your Azure Synapse Analytics database, you can now [create a dataflow and ingest data from your database into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
