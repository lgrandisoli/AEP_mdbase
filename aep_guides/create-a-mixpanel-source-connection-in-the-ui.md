---
title: "Create a Mixpanel source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/analytics/mixpanel"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:24.277974+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Mixpanel source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps for creating a Mixpanel source connection using the Adobe Experience Platform Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

### Gather required credentials

In order to connect Mixpanel to Experience Platform, you must provide values for the following connection properties:

Credential
Description
Example
Username
The service account username that corresponds with your Mixpanel account. See the
Mixpanel service accounts documentation
for more information.
Test8.6d4ee7.mp-service-account
Password
The service account password that corresponds with your Mixpanel account.
dLlidiKHpCZtJhQDyN2RECKudMeTItX1
Project ID
Your Mixpanel project ID. This ID is required to create a source connection. See the
Mixpanel project settings documentation
and the
Mixpanel guide on creating and managing projects
for more information.
2384945
Timezone
The timezone that corresponds with your Mixpanel project. Timezone is required to create a source connection. See the
Mixpanel project settings documentation
for more information.
Pacific Standard Time
For more information on authenticating your Mixpanel source, see the [Mixpanel source overview](/en/docs/experience-platform/sources/connectors/analytics/mixpanel).

## Connect your Mixpanel account

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Analytics* category, select Mixpanel, and then select **Add data**.

The **Connect Mixpanel account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the Mixpanel account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Select your project ID and timezone project-id-and-timezone

Once your source is authenticated, provide your project ID and timezone and then select **Select**.

The timezone that you designate prior to ingesting your Mixpanel data to Experience Platform must be the same as your Mixpanel profile timezone setting. Any changes to your data’s timezone will only be applied to new events and old events will remain in the timezone that you previously designated. Mixpanel accommodates Daylight Savings Time and will adjust your ingestion timestamp appropriately. For more information on how timezones affect your data, see the Mixpanel guide on [managing timezones for projects](https://help.mixpanel.com/hc/en-us/articles/115004547203-Manage-Timezones-for-Projects-in-Mixpanel).

After a few moments, the right interface updates to a preview panel, allowing you to inspect your schema before creating a dataflow. When finished, select **Next**.

## Next steps

By following this tutorial, you have established a connection to your Mixpanel account. You can now continue on to the next tutorial and [configure a dataflow to bring analytics data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/analytics).

## Additional resources additional-resources

The sections below provides additional resources that you can refer to when using the Mixpanel source.

### Validation validation

The following outlines steps you can take to validate that you have successfully connected your Mixpanel source and that Mixpanel events are being ingested to Experience Platform.

In the Experience Platform UI, select **Datasets** from the left navigation bar to access the Datasets workspace. The Dataset Activity screen displays the details of executions.

Next, select the dataflow run ID of the dataflow that you want to view to see specific details about that dataflow run.

Finally, select **Preview dataset** to display the data that was ingested.

You can verify this data against the data on the Mixpanel > Events page. See the [Mixpanel document on Events](https://help.mixpanel.com/hc/en-us/articles/4402837164948-Events-formerly-Live-View-) for more information.

### Mixpanel schema

The table below lists the supported mappings that must be set up for Mixpanel.

TIP
See
Event Export API > Download
for more information on the API.
Source
Type
distinct_id
string
event_name
string
import
boolean
insert_id
string
item_id
string
item_name
string
item_price
string
mp_api_endpoint
string
mp_api_timestamp_ms
integer
mp_processing_time_ms
integer
time
integer
### Limits limits

- You have a maximum of 100 concurrent queries and 60 queries per hour as indicated on [Export API Rate Limits](https://help.mixpanel.com/hc/en-us/articles/115004602563-Rate-Limits-for-API-Endpoints).

recommendation-more-help
