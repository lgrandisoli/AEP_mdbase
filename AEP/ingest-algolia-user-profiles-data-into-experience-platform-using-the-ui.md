---
title: "Ingest Algolia User Profiles data into Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/data-partner/algolia-user-profiles"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:18.547083+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Ingest Algolia User Profiles data into Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial guides you through ingesting data from your Algolia User Profiles account into Adobe Experience Platform using the user interface.

## Get started

IMPORTANT
Before you begin, make sure you’ve completed the prerequisites outlined in the
Algolia User Profiles overview
.
This tutorial assumes familiarity with the following Experience Platform components:

- Experience Data Model (XDM) System : The standardized framework Experience Platform uses to organize customer experience data. Basics of schema composition : Learn about schema composition, including key principles and best practices. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : A unified, real-time customer profile based on aggregated data from multiple sources.
- Sources : Ingest data from various sources and use Experience Platform services to structure, label, and enhance the data.

### Gather required credentials

To connect Algolia to Adobe Experience Platform, provide the following credentials:

Credential
Description
Application ID
The unique identifier assigned to your Algolia account.
API Key
The credential for authenticating and authorizing API requests to Algolia’s services.
For more information, refer to the Algolia [authentication documentation](https://www.algolia.com/doc/tools/cli/get-started/authentication/).

## Connect your Algolia account

In the Experience Platform UI, select **Sources** from the left navigation to open the *Sources* workspace. Use the *Categories* panel or search bar to find your desired source.

To connect Algolia, choose the **Algolia** source card under *Data & Identity Partners* and select **Set up**.

TIP
If a source does not yet have an authenticated account, it shows the
Set up
option. Once authenticated, this changes to
Add data
.
## Authentication

### Use an existing account

To use an existing account, choose **Existing account** and select the Algolia User Profiles account you want to use. Then select **Next**.

### Create a new account

To create a new account, select **New account**, then enter a name, an optional description, and your Algolia credentials. Select **Connect to source** and wait for the connection to establish.

## Add data

After your Algolia User Profiles account is created, the **Add data** step appears. Use it to select and preview user profile data for ingestion.

- On the left, enter optional **Indices** and **Affinity(s)**.
- On the right, preview up to 100 rows of user profiles.

Once done, select **Next**.

## Provide dataflow details

If using an existing dataset, choose one associated with a schema that includes the Algolia Profile field group. Make sure the Algolia User Token field is using the Algolia User Token identity namespace. If the Algolia User Token is not currently created or assigned, instructions are provided below.

If creating a new dataset, select a schema using the Algolia Profile field group.

### Create Algolia User Token identity namespace

You will need to create the Algolia User Token identity namespace if it doesn’t already exist in your organization.

Use the left navigation and select **Identities** to access the [Identity Service](/en/docs/experience-platform/identity/home) UI workspace and then select **Create identity namespace**.

Next, provide a **Display Name** and an **Identity Symbol** for your custom namespace. During this step, you must also configure the type of your namespace. When finished, select **Create**.

Custom namespace config
Value
Display Name
Algolia User Token
Identity Symbol
AlgoliaUserToken
Select a type
Cookie ID
Once added, the namespace appears in the list. You can now apply it in your schema.

### Apply your namespace to your schema

Use the left navigation and select **Schemas** to access the [Schemas](/en/docs/experience-platform/xdm/ui/overview) UI workspace. Use the schemas workspace to create or update a schema with the Algolia Profile Details field group. Next, navigate to the **User Token** field and use the right-rail to select the **Identity** box. Additionally, use the input box to define the Algolia User Token identity namespace. When finished, select **Save**.

After the **User Token** field is assigned the Algolia User Token identity namespace, the identity appears in the user profile for any profile.

## Map data fields to an XDM schema

Use the mapping interface to map your source data to schema fields. For more information, refer to the [mapping guide](/en/docs/experience-platform/data-prep/ui/mapping).

## Schedule ingestion runs

Next, use the scheduling interface to define the ingestion schedule of your dataflow.

Scheduling configuration
Description
Frequency
Configure frequency to indicate how often the dataflow should run. You can set your frequency to:

- **Once**: Set your frequency to once to create a one-time ingestion. Configurations for interval and backfill are unavailable when creating a one-time ingestion dataflow. By default, the scheduling frequency is set to once.
- **Minute**: Set your frequency to minute to schedule your dataflow to ingest data on a per-minute basis.
- **Hour**: Set your frequency to hour to schedule your dataflow to ingest data on a per-hour basis.
- **Day**: Set your frequency to day to schedule your dataflow to ingest data on a per-day basis.
- **Week**: Set your frequency to week to schedule your dataflow to ingest data on a per-week basis.

Interval
Once you select a frequency, you can then configure the interval setting to establish the time frame between every ingestion. For example, if you set your frequency to day and configure the interval to 15, then your dataflow will run every 15 days. You cannot set the interval to zero. The minimum accepted interval value for each frequency is as follows:

- **Once**: n/a
- **Minute**: 15
- **Hour**: 1
- **Day**: 1
- **Week**: 1

Start Time
The timestamp for the projected run, presented in UTC time zone.
Backfill
Backfill determines what data is initially ingested. If backfill is enabled, all current files in the specified path will be ingested during the first scheduled ingestion. If backfill is disabled, only the files that are loaded in between the first run of ingestion and the start time will be ingested. Files loaded prior to the start time will not be ingested.
## Review your dataflow

Use the review page for a summary of your dataflow prior to ingestion. Details are grouped in the following categories:

- **Connection** - Shows the source type, the relevant path of the chosen source file, and the number of columns within that source file.
- **Assign dataset & map fields** - Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.
- **Scheduling** - Shows that active period, frequency, and interval of the ingestion schedule.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Next steps

By following this tutorial, you have successfully created a dataflow to bring intent data from your Algolia source to Experience Platform. For additional resources, visit the documentation outlined below.

### Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to view information on ingestion rates, success, and errors. For more information on how to monitor dataflow, visit the tutorial on [monitoring accounts and dataflows in the UI](/en/docs/experience-platform/dataflows/ui/monitor-sources).

### Update your dataflow

To update configurations for your dataflows scheduling, mapping, and general information, visit the tutorial on [updating sources dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/update-dataflows).

### Delete your dataflow

You can delete dataflows that are no longer necessary or were incorrectly created using the **Delete** function available in the **Dataflows** workspace. For more information on how to delete dataflows, visit the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/delete).

recommendation-more-help
