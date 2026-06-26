---
title: "Connect your Salesforce Marketing Cloud account to Experience Platform through the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/marketing-automation/salesforce-marketing-cloud"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:08:01.591579+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect your Salesforce Marketing Cloud account to Experience Platform through the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

WARNING
The Salesforce Marketing Cloud source will be deprecated in January 2026. A new source will be released later this year as an alternative. Once the new source is released, you must plan to migrate to the new source by creating new account connections and dataflows before the end of January 2026.
Read this guide to learn how to connect your Salesforce Marketing Cloud account to Adobe Experience Platform using the sources workspace in the Experience Platform user interface.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a Salesforce Marketing Cloud account, you may skip the remainder of this document and proceed to the tutorial on [bringing marketing automation data to Experience Platform using the UI](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

### Gather required credentials

Read the [Salesforce Marketing Cloud overview](/en/docs/experience-platform/sources/connectors/marketing-automation/salesforce-marketing-cloud#prerequisites) for information on authentication.

## Navigate the sources catalog

IMPORTANT
Custom object ingestion is currently not supported by the Salesforce Marketing Cloud source integration.
In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. Choose a category or use the search bar to find your source.

To connect to Salesforce Marketing Cloud, go to the *Marketing Automation* category, select the **Salesforce Marketing Cloud** source card, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Use an existing account existing

To use an existing account, select **Existing account** and then select the Salesforce Marketing Cloud account that you want to use.

## Create a new account new

You can use the Salesforce Marketing Cloud source to connect to Experience Platform on Azure or Amazon Web Services (AWS).

### Connect to Experience Platform on Azure azure

To connect to Experience Platform on Azure, provide an account name, an optional description, and your [account authentication credentials](/en/docs/experience-platform/sources/connectors/marketing-automation/salesforce-marketing-cloud#azure). When finished, select **Connect to source** and allow for a few moments for the connection to establish.

### Connect to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
To connect to Experience Platform on AWS, ensure that you are in a VA6 sandbox and provide an account name, an optional description, and your [account authentication credentials](/en/docs/experience-platform/sources/connectors/marketing-automation/salesforce-marketing-cloud#aws). When finished, select **Connect to source** and allow for a few moments for the connection to establish.

## Create a dataflow for Salesforce Marketing Cloud data

Now that you have successfully connected your Salesforce Marketing Cloud , you can now [create a dataflow and ingest data from your marketing automation provider into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

recommendation-more-help
