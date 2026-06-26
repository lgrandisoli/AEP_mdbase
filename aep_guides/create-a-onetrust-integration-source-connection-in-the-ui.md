---
title: "Create a OneTrust Integration source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/consent/onetrust"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:48.975814+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a OneTrust Integration source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The OneTrust Integration source only supports ingestion of consent and preferences data and not cookies.
This tutorial provides steps for creating a [OneTrust Integration](https://my.onetrust.com/s/contactsupport?language=en_US) source connection to ingest both historic and scheduled consent data into Adobe Experience Platform using the Experience Platform user interface.

## Prerequisites

IMPORTANT
The OneTrust Integration source connector and documentation were created by the OneTrust Integration team. For any inquiries or update requests, please contact the
OneTrust team
directly.
Before you can connect OneTrust Integration to Experience Platform, you must first retrieve your access token. For detailed instructions on finding your access token, see the [OneTrust Integration OAuth 2 guide](https://developer.onetrust.com/docs/api-docs-v3/b3A6MjI4OTUyOTc-generate-access-token).

The access token does not refresh automatically after it expires because system-to-system refresh tokens are not supported by OneTrust. Therefore, it is necessary to make sure that your access token is updated in the connection before it expires. The maximum configurable lifespan for an access token is one year. To learn more about updating your access token, see the [OneTrust document on managing your OAuth 2.0 client credentials](https://developer.onetrust.com/docs/documentation/ZG9jOjIyODk1MTUw-managing-o-auth-2-0-client-credentials).

### Gather required credentials

In order to connect OneTrust Integration to Experience Platform, you must provide values for the following authentication credentials:

Credential
Description
Example
Host name
The environment from which the OneTrust Integration data needs to be pulled from.
app.onetrust.com
Authorization Test URL
(Optional) The authorization test URL is used to validate credentials when creating a base connection. If unprovided, credentials are automatically checked during the source connection creation step instead.
Access Token
The access token that corresponds with your OneTrust Integration account.
ZGFkZDMyMjFhMmEyNDQ2ZGFhNTdkZjNkZjFmM2IyOWE6QjlUSERVUTNjOFVsRmpEZTJ6Vk9oRnF3Sk8xNlNtcm4=
For more information on these credentials, see the [OneTrust Integration authentication documentation](https://developer.onetrust.com/docs/api-docs-v3/b3A6MjI4OTUyOTc-generate-access-token).

## Connect your OneTrust Integration account

NOTE
The OneTrust Integration API specifications are being shared with Adobe for data ingestion.
In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace for a catalog of sources available in Experience Platform.

Use the *Categories* menu to filter sources by category. Alternatively, enter a source name in the search bar to find a specific source from the catalog.

Go to the Consent & Preferences category for the OneTrust Integration source card. To begin, select **Add data**.

The **Connect OneTrust Integration account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the OneTrust Integration account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have established a connection to your OneTrust Integration account. You can now continue on to the next tutorial and [configure a dataflow to bring consent data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/consent-and-preferences).

recommendation-more-help
