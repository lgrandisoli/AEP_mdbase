---
title: "Create an Azure Event Hubs source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/eventhub"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:16.710168+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Create an Azure Event Hubs source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Azure Event Hubs source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this tutorial to learn how to create an Azure Event Hubs account using the Adobe Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Event Hubs connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage-streaming).

### Gather required credentials

In order to authenticate your Event Hubs source connector, you must provide values for the following connection properties:

Standard authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Credential | Description |
| SAS key name | The name of the authorization rule, which is also known as the SAS key name. |
| SAS key | The primary key of the Event Hubs namespace. The sasPolicy that the sasKey corresponds to must have manage rights configured in order for the Event Hubs list to be populated. |
| Namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |

SAS authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Credential | Description |
| SAS key name | The name of the authorization rule, which is also known as the SAS key name. |
| SAS key | The primary key of the Event Hub namespace. The sasPolicy that the sasKey corresponds to must have manage rights configured in order for the Event Hubs list to be populated. |
| Namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |
| Event Hub name | Fill in your Azure Event Hub name. Read the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create#create-an-event-hub) for more information on Event Hub names. |

Event Hub Azure Active Directory Auth
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| Credential | Description |
| Tenant ID | The tenant ID that you want to request permission from. Your tenant ID can be formatted as a GUID or as a friendly name. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. |
| Client ID | The application ID assigned to your app. You can retrieve this ID from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| Client Secret Value | The client secret that is used alongside the client ID to authenticate your app. You can retrieve your client secret from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| Namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |

For more information on Azure Active Directory, read the [Azure guide on using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application).

Event Hub Scoped Azure Active Directory Auth
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| Credential | Description |
| Tenant ID | The tenant ID that you want to request permission from. Your tenant ID can be formatted as a GUID or as a friendly name. **Note**: The tenant ID is referred to as the “Directory ID” in the Microsoft Azure interface. |
| Client ID | The application ID assigned to your app. You can retrieve this ID from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| Client Secret Value | The client secret that is used alongside the client ID to authenticate your app. You can retrieve your client secret from the Microsoft Entra ID portal where you registered your Azure Active Directory. |
| Namespace | The namespace of the Event Hub you are accessing. An Event Hub namespace provides a unique scoping container, in which you can create one or more Event Hubs. |
| Event Hub name | Fill in your Azure Event Hub name. Read the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create#create-an-event-hub) for more information on Event Hub names. |

For more information on Azure Active Directory, read the [Azure guide on using Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application).

Once you have gathered your required credentials, you can follow the steps below to link your Event Hubs account to Experience Platform.

## Connect your Event Hubs account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Cloud storage category, select **Azure Event Hubs**, and then select **Add data**.

The **Connect to Azure Event Hubs** dialog appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the Event Hubs account you want to use, then select **Next** to proceed.

### New account

TIP
Once created, you cannot change the authentication type of an Event Hubs base connection. To change the authentication type, you must create a new base connection.
To create a new account, select **New account**, and then provide a name and an optional description for your new Event Hubs account.

Standard authentication
To create an Event Hubs account with standard authentication, use the Account authentication dropdown menu and then select **Standard authentication**. Next, provide values for your SAS key name, SAS key, and Namespace.

Once you have inputted your authentication credentials, select **Connect to source**.

SAS authentication
To create an Event Hubs account with SAS authentication, use the Account authentication dropdown menu and then select **SAS authentication**. Next, provide values for your SAS key name, SAS key, Namespace, and Event Hubs name.

Once you have inputted your authentication credentials, select **Connect to source**.

Event Hub Azure Active Directory Auth
To create an Event Hubs account with Event Hub Azure Active Directory authentication, use the Account authentication dropdown menu and then select **Event Hub Azure Active Directory**. Next, provide values for your Tenant ID, Client ID, Client Secret Value, and Namespace.

Event Hub Scoped Azure Active Directory Auth
To create an Event Hubs account with Event Hub Scoped Azure Active Directory authentication, use the Account authentication dropdown menu and then select **Event Hub Scoped Azure Active Directory**. Next, provide values for your Tenant ID, Client ID, Client Secret Value, Namespace, and Event Hub Name.

## Next steps

By following this tutorial, you have connected your Event Hubs account to Experience Platform. You can now continue on to the next tutorial and [configure a dataflow to bring data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage-streaming).

recommendation-more-help
