---
title: "Connect MySQL to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/mysql"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:35.036363+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect MySQL to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your MySQL database to Adobe Experience Platform using the sources workspace in the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a MySQL connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

Read the [MySQL overview](/en/docs/experience-platform/sources/connectors/databases/mysql#prerequisites) for information on authentication.

## Navigate the sources catalog

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to MySQL, go to the *Databases* category, select the **MySQL** source card, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Use an existing account existing

To use an existing account, select **Existing account** and then select the MySQL account that you want to use.

## Create a new account new

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform on Azure azure

You can connect your MySQL database to Experience Platform on Azure using either account key or basic authentication.

Account key authentication
To use account key authentication, select **Account key authentication**, provide your [connection string](/en/docs/experience-platform/sources/connectors/databases/mysql#azure), and then select **Connect to source**.

Basic authentication
To use basic authentication, select **Basic authentication**, provide values for your [authentication credentials](/en/docs/experience-platform/sources/connectors/databases/mysql#azure), and then select **Connect to source**.

### Connect to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
To create a new MySQL account and connect to Experience Platform on AWS, ensure that you are in a VA6 sandbox and then provide the necessary [credentials for authentication](/en/docs/experience-platform/sources/connectors/databases/mysql#aws).

## Create a dataflow for MySQL data

Now that you have successfully connected your MySQL database, you can now [create a dataflow and ingest data from your database into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
