---
title: "Connect your Salesforce Service Cloud account to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/customer-success/salesforce-service-cloud"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:08.832920+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect your Salesforce Service Cloud account to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Follow this step-by-step guide to seamlessly connect your Salesforce Service Cloud account and import your customer success data into Adobe Experience Platform.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Salesforce Service Cloud connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow for a customer success](/en/docs/experience-platform/sources/ui-tutorials/dataflow/customer-success)

### Gather required credentials

Read the [authentication guide](/en/docs/experience-platform/sources/connectors/customer-success/salesforce-service-cloud#credentials) for more information on retrieving your credentials.

## Connect your Salesforce Service Cloud account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Select **Salesforce Service Cloud** under the *Customer success* category, and then select **Add data**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account exists, this option changes to
Add data
.
The **Connect to Salesforce Service Cloud** page appears. On this page, you can either use new credentials or existing credentials.

### Use an existing account

To use an existing account, select **Existing account**, and then select the desired account from the list that appears. When finished, select **Next** to proceed.

### Create a new account

To create a new account, select **New account** and provide a name and a description for your new Salesforce Service Cloud account. Next, select **OAuth2 Client Credential** and then provide values for the following credentials:

- Environment URL
- Client ID
- Client secret
- API version

When finished, select **Connect to source**.

## Next steps

By following this tutorial, you have established a connection to your Salesforce Service Cloud account. You can now continue on to the next tutorial and [configure a dataflow to bring Customer Success data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/customer-success).

recommendation-more-help
