---
title: "Connect Databricks to Experience Platform in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/databricks"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:04.189465+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Databricks to Experience Platform in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

AVAILABILITY
The Databricks source is available in the sources catalog to users who have purchased Real-Time CDP Ultimate.
Read this guide to learn how to connect your Databricks account to Adobe Experience Platform using the sources workspace in the UI.

## Get started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Gather required credentials

Provide values for the following credentials to connect Databricks to Experience Platform.

Credential
Description
Domain
The URL of your Databricks workspace. For example,
https://adb-1234567890123456.7.azuredatabricks.net
.
Cluster ID
The ID of your cluster in Databricks. This cluster must already be an existing cluster and should be an interactive cluster.
Access token
The access token that authenticates your Databricks account. You can generate your access token using the Databricks workspace.
Database
The name of your database in the delta lake.
For more information, read the [Databricks overview](/en/docs/experience-platform/sources/connectors/databases/databricks).

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to Databricks, go to the *Databases* category, select the **Azure Databricks** source card, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
### Use an existing account

To use an existing account, select **Existing account** and then select the Azure Databricks account that you want to use.

### Create a new account

To create a new account, select **New account** and provide a name and optionally add a description for your account. Next, provide values for the following authentication credentials:

- Domain
- Cluster ID
- Access token
- Database
- Catalog

Additionally, you must copy and paste your Staging SAS URI credentials to your Azure Databricks environment. When finished, select **Connect to source** and allow for a few moments for the connection to establish.

## Create a dataflow for Azure Databricks data

Now that you have successfully connected your Azure Databricks account, you can now [create a dataflow and ingest data from your database into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
