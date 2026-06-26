---
title: "Create a Google PubSub source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/google-pubsub"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:12.458486+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Create a Google PubSub source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Google PubSub source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
This tutorial provides steps for creating a Google PubSub (hereinafter referred to as “PubSub”) using the Experience Platform user interface.

## Get started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

If you already have a valid PubSub connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

### Gather required credentials

You must provide values for the connection properties outlined below in order to connect your PubSub account to Experience Platform. For more information on authentication and prerequisite setup, read the [PubSub source overview](/en/docs/experience-platform/sources/connectors/cloud-storage/google-pubsub#prerequisites).

Project-based authentication
| table 0-row-2 1-row-2 2-row-2 |  |
| --- | --- |
| Credential | Description |
| Project ID | The project ID required to authenticate PubSub. |
| Credentials | The credential required to authenticate PubSub. You must ensure that you put the complete JSON file after removing the white spaces from your credentials. |

Topic and subscription-based authentication
| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Credential | Description |
| Credentials | The credential required to authenticate PubSub. You must ensure that you put the complete JSON file after removing the white spaces from your credentials. |
| Topic name | The name of your PubSub subscription. In PubSub, subscriptions allow you to receive messages, by subscribing to the topic in which messages have been published to. **Note**: A single PubSub subscription can only be used for one dataflow. In order to make multiple dataflows, you must have multiple subscriptions. |
| Subscription name | The name of your PubSub subscription. In PubSub, subscriptions allow you to receive messages, by subscribing to the topic in which messages have been published to. |

For more information about these values, see the following [PubSub authentication](https://cloud.google.com/pubsub/docs/authentication) document. If you are using service account-based authentication, see the following [PubSub guide](https://cloud.google.com/docs/authentication/production#create_service_account) for steps on how to generate your credentials.

TIP
If you are using service account-based authentication, ensure that you have granted sufficient user access to your service account and that there are no extra white spaces in the JSON, when copying and pasting your credentials.
Once you have gathered your required credentials, you can follow the steps below to link your PubSub account to Experience Platform.

## Connect your PubSub account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Cloud storage category, select **Google PubSub**, and then select **Add data**.

The **Connect to Google PubSub** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the PubSub account you want to create a new dataflow with, then select **Next** to proceed.

### New account

TIP
- When creating an account with restricted access, you must provide at least one of your topic name or subscription name. Authentication will fail if both values are missing.
- Once created, you cannot change the authentication type of a Google PubSub base connection. To change the authentication type, you must create a new base connection.

If you are creating a new account, select **New account**, and then provide a name and an optional description for your new PubSub account.

The PubSub source allows you to specify the type of access that you want to allow during authentication. You can set up your account to have either project-based authentication or topic and subscription-based authentication. Project-based authentication allows you to grant access to the root-level project in your account, while topic and subscription-based authentication allows you to restrict access to a particular PubSub topic and subscription.

Project-based authentication
To create an account with access to your root PubSub project folder. Select **Google PubSub authentication credentials** as your authentication type and provide your project ID and credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

Topic and subscription-based authentication
To create an account with restricted access only to a particular PubSub topic and subscription, select **Google PubSub Scoped authentication credentials** and then provide your credentials, topic name, and/or subscription name. When finished, select **Connect to source** and then allow some time for the new connection to establish.

NOTE
Principal (roles) assigned to a PubSub project are inherited in all of the topics and subscriptions created inside a PubSub project. If you want a principal (role) to have access to a specific topic, then that principal (role) must also be added to the topic’s corresponding subscription as well. For more information, read the
PubSub documentation on access control
.
## Select data

A successful authentication brings you to the Select data step, where you can navigate through your PubSub data hierarchy and select the data that you want to bring to Experience Platform.

Project-based authentication
If you have authenticated with project-based access, the Select data interface will display all subscriptions within your project that has a topic attached to them.

Topic and subscription-based authentication
If you have authenticated with a topic and subscription-based access, the Select data interface display can vary depending on the information that you provided.

- If you provide only the topic name, then the interface displays all topic-subscription pairs that correspond to the topic provided.
- If you only provide the subscription name, then the interface displays all topic-subscription pairs that correspond to the subscription name provided.
- If both topic and subscription names are provided, then the interface displays the topic-subscription pair that corresponds with both provided values.

## Next steps

By following this tutorial, you have created a connection between your PubSub account and Experience Platform. You can now continue on to the next tutorial and [configure a dataflow to bring streaming data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage-streaming).

recommendation-more-help
