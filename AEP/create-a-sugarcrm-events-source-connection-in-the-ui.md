---
title: "Create a SugarCRM Events source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/crm/sugarcrm-events"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:51.665764+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a SugarCRM Events source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a SugarCRM Events source connection using the Adobe Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid SugarCRM account, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

### Gather required credentials

In order to connect SugarCRM Events to Experience Platform, you must provide values for the following connection properties:

Credential
Description
Example
Host
The SugarCRM API endpoint the source connects to.
developer.salesfusion.com
Username
Your SugarCRM developer account username.
abc.def@example.com@sugarmarketdemo000.com
Password
Your SugarCRM developer account password.
123456789
### Create an Experience Platform schema for SugarCRM

Before creating a SugarCRM source connection, you must also ensure that you first create an Experience Platform schema to use for your source. See the tutorial on [creating an Experience Platform schema](/en/docs/experience-platform/xdm/schema/composition) for comprehensive steps on how to create a schema.

WARNING
When mapping the schema ensure you also map the mandatory
event_id
and
timestamp
fields required by Experience Platform.
## Connect your SugarCRM Events account

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *CRM* category, select **SugarCRM Events**, and then select **Add data**.

The **Connect SugarCRM Events account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the SugarCRM Events account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have established a connection to your SugarCRM Events account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

## Additional resources

The sections below provide additional resources that you can refer to when using the SugarCRM source.

### Guardrails guardrails

The SugarCRM API throttle rates are 90 calls per minute or 2000 calls per day, whichever happens first. However, this restriction has been circumvented by adding a parameter into the connection spec that will delay request time so that the rate limit is never reached.

### Validation validation

To validate that you have correctly set up the source and SugarCRM Events data is being ingested, follow the steps below:

- In the Experience Platform UI, select View Dataflows beside the SugarCRM Events card menu on the sources catalog. Next, select Preview dataset to verify the data that was ingested.
- Depending on the object type you are working with, you can verify the aggregated data against the counts visible on the SugarMarket Events page below:

NOTE
The SugarMarket pages do not include the deleted object counts. However, data retrieved through this source will also include the deleted count, these would be marked with a deleted flag.
recommendation-more-help
