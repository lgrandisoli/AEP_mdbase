---
title: "Connect your PathFactory account to Experience Platform through the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/marketing-automation/pathfactory"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:38:21.229592+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect your PathFactory account to Experience Platform through the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps on how to connect your PathFactory Visitors, Sessions and Page Views data to Adobe Experience Platform through the UI.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a PathFactory account, you may skip the remainder of this document and proceed to the tutorial on [bringing marketing automation data to Experience Platform using the UI](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

### Gather Required Credentials gather-credentials

To access your PathFactory account on the Experience Platform, you must provide the following values:

Credential
Description
Username
Your PathFactory account username. This is essential for identifying your account in the system.
Password
The password associated with your PathFactory account. Ensure this is kept secure to prevent unauthorized access.
Domain
The domain associated with your PathFactory account. This typically refers to the unique identifier within your PathFactory URL.
Access Token
A unique token used for API authentication to ensure secure communication between your systems and PathFactory.
API Endpoints
Specific API endpoints for accessing data: Visitors, Sessions, and Page Views. Each endpoint corresponds to different data sets you can retrieve. **Note:** These are pre-defined by PathFactory and are specific to the data you intend to access:

- **Visitors Endpoint**: /api/public/v3/data_lake_apis/visitors.json
- **Sessions Endpoint**: /api/public/v3/data_lake_apis/sessions.json
- **Page Views Endpoint**: /api/public/v3/data_lake_apis/page_views.json

For detailed guidance on how to secure and use your credentials, and for information about obtaining and refreshing your access token, visit the [PathFactory Support Center](https://support.pathfactory.com/categories/adobe/). This resource offers comprehensive guides on managing your credentials and ensuring effective and secure API integration.

## Connect your PathFactory account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog displays a variety of sources supported by Experience Platform.

You can select the appropriate category from the list of categories. You can also use the search bar to filter for a specific source.

Under the Marketing automation category, select **PathFactory** and then select **Set up**.

The **Connect to PathFactory** page appears. On this page, you can either create a new account or use an existing account.

### New account

To create a new account, select **New account** and provide a name for your account, an optional description, and the authentication credentials that correspond with your PathFactory account.

When finished, select **Connect to source** and then allow some time for the new connection to establish.

### Existing account

If you already have an existing account, select **Existing account** and then select the account that you would like to use from the list that appears.

## Next steps

By following this tutorial, you have established a connection between your PathFactory account and Experience Platform. You can now continue on to the next tutorial and [create a dataflow to bring your marketing automation data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

recommendation-more-help
