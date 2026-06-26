---
title: "Connect Google Ads to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/advertising/ads"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:21.732381+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Connect Google Ads to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The Google Ads source is currently in beta and only supports one-time ingestion. You can use
the API method
to perform incremental data ingestion of your Google Ads data into Experience Platform.
See the
Sources overview
for more information on using beta-labeled sources.
Read this guide to learn how to connect your Google Ads account to Adobe Experience Platform using the sources workspace in the Experience Platform UI.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Google Ads connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/advertising)

### Gather required credentials

For information on authentication, read the [Google Ads source overview](/en/docs/experience-platform/sources/connectors/advertising/ads).

## Connect your Google Ads account

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. You can select the appropriate category in the *Categories* panel. Alternatively, you can use the search bar to navigate to the specific source that you want to use.

To use Google Ads, select the **Google Ads** source card under *Advertising* and then select **Add data**.

.

### Existing account

To use an existing account, select **Existing account** and then select the account that you want to use from the list of accounts on the interface.

Once you have selected your account, select **Next** to proceed to the next step.

.

### New account

If you do not have an existing account, then you must create a new account by providing the necessary authentication credentials that correspond with your source.

To create a new account, select **New account** and then provide an account name and optionally, a description for your account details. Next, provide the appropriate authentication values to authenticate your source against Experience Platform:

- **Client customer ID**: The client customer ID is the account number that corresponds with the Google Ads client account that you want to manage with the Google Ads API. This ID follows the template of 123-456-7890.
- **Login customer ID**: The login customer ID is the account number that corresponds with your Google Ads manager account and is used to fetch report data from a specific operating customer. For more information on the login customer ID, read the [Google Ads API documentation](https://developers.google.com/search-ads/reporting/concepts/login-customer-id).
- **Developer token**: The developer token allows you to access the Google Ads API. You can use the same developer token to make requests against all of your Google Ads accounts. Retrieve your developer token by [logging in to your manager account](https://ads.google.com/home/tools/manager-accounts/) and then navigating to the API Center page.
- **Refresh token**: The refresh token is a part of OAuth2 authentication. This token allows you to regenerate your access tokens after they expire.
- **Client ID**: The client ID is used in tandem with the client secret as part of OAuth2 authentication. Together, the client ID and client secret enables your application to operate on behalf of your account by identifying your application to Google.
- **Client secret**: The client secret is used in tandem with the client ID as part of OAuth2 authentication. Together, the client ID and client secret enables your application to operate on behalf of your account by identifying your application to Google.
- **Google Ads API version**: The current API version supported by Google Ads. While the latest Google Ads API version is v21, Experience Platform currently supports version v19 and newer. Make sure you’re using one of these supported versions to ensure compatibility.

Once you have inputted your credentials, select **Connect to source** and allow for a few moments for the connection to process. When finished, select **Next**.

.

## Select data select-data

With Google Ads, you must provide the list of attributes for ingestion during the data selection phase of the workflow. In order to retrieve these attributes, you must use the [Google Ads Query Builder](https://developers.google.com/google-ads/api/fields/v19/overview_query_builder).

In the Google Ads Query Builder, navigate to the resource type that you want to use and then use the attributes selector to select your attributes, segments, and metrics.

The attributes that you select populates the Google Ads Query Language panel. Ensure that you use the Standard mode and then select, **Enter or edit a query**.

Next, select **Validate Query** to validate your Google Ads query.

If successful, the Google Ads Query Builder returns a message indicating that your query is valid. Next, copy **only the attributes** from within the query.

Navigate back to the data selection phase of the sources workflow in the Experience Platform UI and then paste the attributes in the *List attributes* panel.

Select **Preview** to preview the data, and then select **Next** to proceed.

## Create a dataflow to ingest advertising data

By following this tutorial, you have established a connection to your Google Ads account. You can now continue on to the next tutorial and [configure a dataflow to bring advertising data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/advertising).

recommendation-more-help
