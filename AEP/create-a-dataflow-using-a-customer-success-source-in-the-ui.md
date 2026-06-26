---
title: "Create a Dataflow using a customer success source in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/dataflow/customer-success"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:54.696777+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Dataflow using a customer success source in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A dataflow is a scheduled task that retrieves and ingests data from a source to a dataset in Adobe Experience Platform. This tutorial provides steps on how to create a dataflow for a customer success source using the Experience Platform UI.

NOTE
- In order to create a dataflow, you must already have an authenticated account with a customer success source. A list of tutorials for creating different customer success source accounts in the UI can be found in the [sources overview](/en/docs/experience-platform/sources/home#customer-success).
- For Experience Platform to ingest data, timezones for all table-based batch sources must be configured to UTC.

## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Sources : Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- Data Prep : Allows data engineers to map, transform, and validate data to and from Experience Data Model (XDM).

## Add data

After creating your customer success source account, the **Add data** step appears, providing an interface for you to explore your customer success source account’s table hierarchy.

- The left half of the interface is a browser, displaying a list of data tables contained in your account. The interface also includes a search option that allows you to quickly identify the source data you intend to use.
- The right half of the interface is a preview panel, allowing you to preview up to 100 rows of data.

NOTE
The search source data option is available to all table-based sources excluding the Adobe Analytics, Amazon Kinesis, and Azure Event Hubs.
Once you find the source data, select the table, then select **Next**.

## Provide dataflow details

The Dataflow detail page allows you to select whether you want to use an existing dataset or a new dataset. During this process, you can also configure settings for Profile dataset, Error diagnostics, Partial ingestion, and Alerts.

### Use an existing dataset

To ingest data into an existing dataset, select **Existing dataset**. You can either retrieve an existing dataset using the Advanced search option or by scrolling through the list of existing datasets in the dropdown menu. Once you have selected a dataset, provide a name and a description for your dataflow.

### Use a new dataset

To ingest into a new dataset, select **New dataset** and then provide an output dataset name and an optional description. Next, select a schema to map to using the Advanced search option or by scrolling through the list of existing schemas in the dropdown menu. Once you have selected a schema, provide a name and a description for your dataflow.

### Enable Profile and error diagnostics

Next, select the **Profile dataset** toggle to enable your dataset for Profile. This allows you to create a holistic view of an entity’s attributes and behaviors. Data from all Profile-enabled datasets will be included in Profile and changes are applied when you save your dataflow.

Error diagnostics enables detailed error message generation for any erroneous records that occur in your dataflow, while Partial ingestion allows you to ingest data containing errors, up to a certain threshold that you manually define. See the [partial batch ingestion overview](/en/docs/experience-platform/ingestion/batch/partial) for more information.

### Enable alerts

You can enable alerts to receive notifications on the status of your dataflow. Select an alert from the list to subscribe to receive notifications on the status of your dataflow. For more information on alerts, see the guide on [subscribing to sources alerts using the UI](/en/docs/experience-platform/sources/ui-tutorials/alerts).

When you are finished providing details to your dataflow, select **Next**.

## Map data fields to an XDM schema

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once your source data is successfully mapped, select **Next**.

## Schedule ingestion runs

The Scheduling step appears, allowing you to configure an ingestion schedule to automatically ingest the selected source data using the configured mappings. By default, scheduling is set to Once. To adjust your ingestion frequency, select **Frequency** and then select an option from the dropdown menu.

TIP
Interval and backfill are not visible during a one-time ingestion.
If you set your ingestion frequency to Minute, Hour, Day, or Week, then you must set an interval to establish a set time frame between every ingestion. For example, an ingestion frequency set to Day and an interval set to 15 means that your dataflow is scheduled to ingest data every 15 days.

During this step, you can also enable **backfill** and define a column for the incremental ingestion of data. Backfill is used to ingest historical data, while the column you define for incremental ingestion allows new data to be differentiated from existing data.

See the table below for more information on scheduling configurations.

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
Load incremental data by
An option with a filtered set of source schema fields of type, date, or time. The field that you select for
Load incremental data by
must have its date-time values in UTC timezone in order to correctly load incremental data. All table-based batch sources pick incremental data by comparing a delta column time stamp value to the corresponding flow run window UTC time, and then copying the data from the source, if any new data is found within the UTC time window.
## Review your dataflow

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the amount of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.
- **Scheduling**: Shows the active period, frequency, and interval of the ingestion schedule.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to see information on ingestion rates, success, and errors. For more information on how to monitor dataflow, see the tutorial on [monitoring accounts and dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/monitor).

## Delete your dataflow

You can delete dataflows that are no longer necessary or were incorrectly created using the **Delete** function available in the **Dataflows** workspace. For more information on how to delete dataflows, see the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/delete).

## Next steps

By following this tutorial, you have successfully created a dataflow to bring data from your customer success source to Experience Platform. Incoming data can now be used by downstream Experience Platform services such as Real-Time Customer Profile and Data Science Workspace. See the following documents for more details:

- [Real-Time Customer Profile overview](/en/docs/experience-platform/profile/home)
- [Data Science Workspace overview](/en/docs/experience-platform/data-science-workspace/home)

WARNING
The Experience Platform UI shown in the following video is out-of-date. Please refer to the documentation above for the latest UI screenshots and functionality.
https://video.tv.adobe.com/v/29711?quality=12&learn=on
https://video.tv.adobe.com/vc/29711/eng.json
recommendation-more-help
