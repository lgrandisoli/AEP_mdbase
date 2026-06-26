---
title: "Connect your Salesforce account to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/crm/salesforce"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:59.577382+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect your Salesforce account to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read this guide to learn how to connect your Salesforce account and bring your CRM data into Adobe Experience Platform using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have an authenticated Salesforce account, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow for CRM data](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

### Gather required credentials gather-required-credentials

The Salesforce source supports authentication via OAuth2 Client Credential.

Credential
Description
Environment URL
The URL of the Salesforce source instance. The format for environment URL is
https://[domain].my.salesforce.com
.
Client ID
The client ID is used in tandem with the client secret as part of OAuth2 authentication. Together, the client ID and client secret enable your application to operate on behalf of your account by identifying your application to Salesforce.
Client secret
The client secret is used in tandem with the client ID as part of OAuth2 authentication. Together, the client ID and client secret enable your application to operate on behalf of your account by identifying your application to Salesforce.
API version
The REST API version of the Salesforce instance that you are using. The value for the API version must be formatted with a decimal. For example, if you are using API version
52
, then you must input the value as
52.0
. If this field is left blank, then Experience Platform will automatically use the latest available version.
Include deleted objects
A boolean value used to determine whether to include soft deleted records. If set to true, soft-deleted records can be included in your Salesforce query and ingested from your account into Experience Platform If you do not specify your configuration, this value defaults to
false
.
For more information on using OAuth for Salesforce, read the [Salesforce guide on OAuth Authorization Flows](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_flows.htm&type=5).

## Connect your Salesforce account

In the Experience Platform UI, navigate to **Sources** from the left menu to open the Sources workspace. Use the catalog on the left to browse categories, or use the search bar to quickly find the source you want to connect.

Select **Salesforce** under the *CRM* category, and then select **Add data**.

TIP
In the sources catalog, you’ll see
Set up
if no account is connected, or
Add data
if an account is already authenticated.
The **Connect to Salesforce** page appears. On this page, you can either use new credentials or existing credentials.

### Use an existing account

To use an existing account, select **Existing account** and then select the account that you want to use from the list that appears. When finished, select **Next** to proceed.

### Create a new account

To create a new account, select **New account** and provide a name and a description for your new Salesforce account.

For OAuth 2 Client Credential, select **OAuth2 Client Credential** and then provide values for the following credentials:

- Environment URL
- Client ID
- Client secret
- API version
- Include delete objects

When finished, select **Connect to source**.

### Skip preview of sample data skip-preview-of-sample-data

During the data selection step, you may encounter a timeout when ingesting large tables or files of data. You can skip data preview to circumvent the timeout and still view your schema, albeit without sample data. To skip data preview, enable the **Skip previewing sample data** toggle.

The rest of the workflow will remain the same. The only caveat is that skipping data preview may prevent calculated and required fields from being auto-validated during the mapping step, and you will then have to manually validate those fields during mapping.

## Next steps

By following this tutorial, you have established a connection to your Salesforce account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

recommendation-more-help
