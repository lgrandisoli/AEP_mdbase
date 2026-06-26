---
title: "Create a Microsoft Dynamics source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/crm/dynamics"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:48.245125+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Microsoft Dynamics source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps to create a Microsoft Dynamics (hereinafter referred to as “Dynamics”) source connection using the Adobe Experience Platform UI.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Dynamics account, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow for a CRM source](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

### Gather required credentials

In order to authenticate your Dynamics source, you must provide values for the following connection properties:

Basic authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Credential | Description |
| serviceUri | The service URL of your Dynamics instance. |
| username | The user name for your Dynamics user account. |
| password | The password for your Dynamics account. |

Service-principal and key authentication
| table 0-row-2 1-row-2 2-row-2 |  |
| --- | --- |
| Credential | Description |
| servicePrincipalId | The client ID of your Dynamics account. This ID is required when using service principal and key-based authentication. |
| servicePrincipalKey | The service principal secret key. This credential is required when using service principal and key-based authentication. |

For more information on getting started, refer to [this Dynamics document](https://docs.microsoft.com/en-us/powerapps/developer/common-data-service/authenticate-oauth).

## Connect your Dynamics account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the CRM category, select **Microsoft Dynamics**, and then select **Add data**.

The **Connect Microsoft Dynamics account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the Dynamics account you want to use, then select **Next** in the top-right corner to proceed.

### New account

TIP
Once created, you cannot change the authentication type of an Dynamics base connection. To change the authentication type, you must create a new base connection.
To create a new account, select **New account**, and then provide a name and an optional description for your new Dynamics account.

You can use either basic authentication or service-principal and key authentication when creating a Dynamics account.

Basic authentication
To create a Dynamics account with basic authentication, select Basic authentication and then provide values for your Service URI, Username, and Password. **Note**: Basic authentication in Dynamics may be blocked by two-factor authentication, which is currently not supported by Experience Platform. In this case, it is recommended to use key-based authentication to create a source connector using Dynamics.

When finished, select **Connect to source** and then allow some time for the new account to establish.

Service-principal and key authentication
To create a Dynamics account with service-principal and key authentication, select **Service-principal and key authentication** and then provide values for your Service principal ID and Service principal key.

When finished, select **Connect to source** and then allow some time for the new account to establish.

## Next steps

By following this tutorial, you have established a connection to your Dynamics account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm).

recommendation-more-help
