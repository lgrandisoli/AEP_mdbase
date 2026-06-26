---
title: "Connect PostgreSQL to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/postgres"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:15.270141+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect PostgreSQL to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your PostgreSQL database to Adobe Experience Platform using the sources workspace in the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid PostgreSQL connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

Read the [PostgreSQL overview](/en/docs/experience-platform/sources/connectors/databases/postgres) for more information on authentication.

### Enable SSL encryption for your connection string

You can enable SSL encryption for your PostgreSQL connection string by appending your connection string with the following properties:

Property
Description
Example
EncryptionMethod
Allows you to enable SSL encryption on your PostgreSQL data.
- EncryptionMethod=0(Disabled)
- EncryptionMethod=1(Enabled)
- EncryptionMethod=6(RequestSSL)

ValidateServerCertificate
Validates certificate sent by your PostgreSQL database when
EncryptionMethod
is applied.
- ValidationServerCertificate=0(Disabled)
- ValidationServerCertificate=1(Enabled)

The following is an example of a PostgreSQL connection string appended with SSL encryption: Server={SERVER};Database={DATABASE};Port={PORT};UID={USERNAME};Password={PASSWORD};EncryptionMethod=1;ValidateServerCertificate=1.

## Navigate the sources catalog navigate

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Select the appropriate category in the *Categories* panel Alternatively, use the search bar to navigate to the specific source that you want to use.

To use PostgreSQL, select the **PostgreSQL DB** source card under *Databases* and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Use an existing account existing

To use an existing account, select **Existing account** and then select the PostgreSQL account that you want to use.

## Create a new account create

If you do not have an existing account, then you must create a new account by providing the necessary authentication credentials that correspond with your source.

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform on Azure azure

You can connect your PostgreSQL account to Experience Platform on Azure using either account key or basic authentication.

Account key authentication
To use account key authentication, select **Account key authentication**, provide your [connection string](/en/docs/experience-platform/sources/connectors/databases/postgres#azure), and then select **Connect to source**.

Basic authentication
To use basic authentication, select **Basic authentication**, provide values for your [authentication credentials](/en/docs/experience-platform/sources/connectors/databases/postgres#azure), and then select **Connect to source**.

### Connect to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
To create a new PostgreSQL account and connect to Experience Platform on AWS, ensure that you are in a VA6 sandbox and then provide the necessary [credentials for authentication](/en/docs/experience-platform/sources/connectors/databases/postgres#aws).

## Create a dataflow for your PostgreSQL data

By following this tutorial, you have established a connection to your MariaDB account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
