---
title: "Create a Zendesk source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/customer-success/zendesk"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:57.512072+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Zendesk source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a Zendesk source connection using the Adobe Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

### Gather required credentials

In order to access your Zendesk account on Experience Platform, you must provide values for the following credentials:

Credential
Description
Example
Subdomain
The unique domain specific to your account created during the registration process.
yoursubdomain
Access token
Zendesk API token.
0lZnClEvkJSTQ7olGLl7PMhVq99gu26GTbJtf
For more information on authenticating your Zendesk source, see the [Zendesk source overview](/en/docs/experience-platform/sources/connectors/customer-success/zendesk).

### Create an Experience Platform schema for Zendesk

Before creating a Zendesk source connection, you must also ensure that you first create an Experience Platform schema to use for your source. See the tutorial on [creating an Experience Platform schema](/en/docs/experience-platform/xdm/schema/composition) for comprehensive steps on how to create a schema.

For additional guidance on your Zendesk schema required for the Zendesk Search API, refer to the [limits](#limits) section below.

## Connect your Zendesk account

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Customer Success* category, select **Zendesk**, and then select **Add data**.

The **Connect Zendesk account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the *Zendesk* account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

### Select data

Once your source is authenticated, the page updates into an interactive schema tree that allows you to explore and inspect the hierarchy of your data. Select **Next** to proceed.

## Next steps

By following this tutorial, you have authenticated and created a source connection between your Zendesk account and Experience Platform. You can now continue on to the next tutorial and [create a dataflow to bring customer success data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/customer-success).

## Additional resources

The sections below provides additional resources that you can refer to when using the Zendesk source.

### Validation validation

The following outlines steps you can take to validate that you have successfully connected your Zendesk source and that Zendesk profiles are being ingested to Experience Platform.

In the Experience Platform UI, select **Datasets** from the left navigation to access the Datasets workspace. The Dataset Activity screen displays the details of executions.

Next, select the dataflow run ID of the dataflow that you want to view to see specific details about that dataflow run.

Finally, select **Preview dataset** to display the data that was ingested.

You can also verify your Experience Platform data against the data on your Zendesk > Customers page.

### Zendesk schema

The table below lists the supported mappings that must be set up for Zendesk.

TIP
See
Zendesk Search API > Export Search Results
for more information on the API.
Source
Type
results.active
Boolean
results.alias
String
results.created_at
String
results.custom_role_id
Integer
results.default_group_id
Integer
results.details
String
results.email
String
results.external_id
Integer
results.iana_time_zone
String
results.id
Integer
results.last_login_at
String
results.locale
String
results.locale_id
Integer
results.moderator
Boolean
results.name
String
results.notes
String
results.only_private_comments
Boolean
results.organization_id
Integer
results.phone
String
results.photo
String
results.report_csv
Boolean
results.restricted_agent
Boolean
results.result_type
String
results.role
String
results.role_type
Integer
results.shared
Boolean
results.shared_agent
Boolean
results.shared_phone_number
Boolean
results.signature
String
results.suspended
Boolean
results.ticket_restriction
String
results.time_zone
String
results.two_factor_auth_enabled
Boolean
results.updated_at
String
results.url
String
results.verified
Boolean
### Limits limits

- The Zendesk Search API > Export Search Results returns a maximum of 1000 records per page. The value for the filter[type] parameter is set to user and hence the Zendesk connection only returns users. The number of results per page is managed by the page[size] parameter. The value is set to 100 . This is done to reduce the impact of speed reduction constraints set by Zendesk. See Limits and Pagination . You can also refer to Paginating through lists using cursor pagination .

recommendation-more-help
