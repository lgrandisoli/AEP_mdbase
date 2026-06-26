---
title: "Manage connections manage-connections"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/manage-connections?lang=en"
category: "other"
topic: "analytics-platform/using/cja-connections/manage-connections"
created_at: "2026-06-23T20:44:18.080718+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage connections manage-connections

Last update: June 11, 2026
- Topics:
- [Data management](#)
- [Analysis Workspace](#)
- [Components](#)
- [Integrations](#)

CREATED FOR:

- Admin

Once you have [created or edited one or more connections](/en/docs/analytics-platform/using/cja-connections/create-connection), you can manage them in **Connections**. The Connections interface let you:

- View all your connections at a glance, including the owner, the sandbox, and when the connections were created and modified.
- Edit a connection.
- Delete a connection.
- Create a data view from a connection.
- View all datasets in a connection.
- Check the status of your connection’s datasets and the status of the ingestion process. For example, when is your data available so that you can start with reporting and analysis in Analysis Workspace.
- Identify any data discrepancies due to misconfiguration. Are you missing any rows? If so, what rows are missing and why? Did you misconfigure connections and cause missing data in Customer Journey Analytics?
- Get insights on the usage of ingested and reportable rows across all your connections.

Connections has two interfaces: [List](#list) and [Usage](#usage).

## List

The **List** interface is the default interface for Connections. If not selected, select the **List** tab to access the interface.

The **List** interface shows a table of all connections available.△

The following columns or icons are available in the table.

Column or Icon
Description
Name
The connection’s friendly name. Select the hyperlinked name to see the
details of the connection
.
To view information about Datasets included, Sandbox, Owner, and more, select next to the connection name.

A popup window displays details about the dataset.

To
create a data view
for the connection, select
. This icon only shows when no data view is already associated with the connection.
Select to open a context menu. You can select:

**Edit** to [edit](#edit-a-connection) a connection.

**Delete** to [delete](#delete-a-connection) a connection.

**Create new data view** to [create a new data view](#create-a-data-view) for the connection.

**Connection map** to view a [connection map](#map-a-connection) for the connection.

[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Connection type
The type of connection:
Person
-based or
Account
-based connection.
Datasets
One or more links to the datasets that are part of the connection. You can select the dataset hyperlink to view the dataset in the connection. If more datasets are part of the selected connection, select **+ x more** to show a **Datasets included** panel. This panel shows links to all datasets and an option to search for specific datasets that is part of the connection.

Select a dataset name to open the dataset in the Experience Platform interface in a new tab.

Sandbox
The
Experience Platform sandbox
from which this connection draws its datasets. You select this sandbox when you created the connection. You cannot change the sandbox once a connection is saved.
Owner
The person who created the connection.
Import new data
The status of importing new data for datasets:

**x On** for datasets configured to import new data, and

*x Off* for datasets not configured to import new data.

Date created
The timestamp when the connection was created.
Last modified
The timestamp when the connection is last updated.
Backfill data
The status for backfill data across datasets.

**x backfills failed** for number of failed backfills across datasets,

**x backfills processing** for number of processing backfills across datasets,

**x backfills completed** for number of completed backfills for datasets, and

*Off* in case no backfills are defined for the datasets in the connection.

Integrations
Shows any Experience Platform applications that are enabled with the connection.
Use in CJA
Shows whether the connection has been enabled for use with Customer Journey Analytics.
To configure which columns to display in the table, select . In the **Customize table** dialog, select the columns to show. Then select **Apply**.

### Search connections

You can quickly search connections using the box.

### Filter connections

To apply a filter to the list of connections, select . Then select from the following filter options:

Filter option
Description
Datasets
Only connections that are associated with the datasets you select are displayed.
Owner
Only connections owned by the people you select are displayed.
Sandbox
Only connections available in the sandboxes you select are displayed.
Connection Type
Filter on
person
-based or
account
-based
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
connections.
Use in CJA
Select
On
to show only connections that are enabled for use with Customer Journey Analytics. Select
Off
to show only connections that are not yet enabled for use with Customer Journey Analytics.
Integrations
Only connections with selected integrations are displayed.
Select **Hide filters** to hide the filter pane.

### Edit a connection

To edit a connection:

- Select next to the connection name
- Select **Edit** from the context menu.

Alternatively, you can:

- Select the connection row.
- Select Edit from the blue action bar.

See [Create or edit a connection](/en/docs/analytics-platform/using/cja-connections/create-connection) for more information.

### Delete a connection connections-delete

To delete a connection:

- Select next to the connection name.
- Select **Delete**.

Alternatively, you can:

- Select the connection row.
- Select Delete from the blue action bar.

When you delete a connection, a **Delete connection** panel indicates which data views are deleted and which workspace projects are affected.

- In ➊ Info , the implications of the deletion of the connection are shown. Select Continue to confirm the deletion.
- In ➋ Confirmation , enter the name of the connection in Type connection name , and select Delete to delete the connection. Select Cancel to cancel.

See [Deletion implications](/en/docs/analytics-platform/using/technotes/deletion) for more information about deleting a connection.

### Create a data view for a connection

To create a data view for a connection:

- Select next to the connection name.
- Select **Create new data view**.

Alternatively, you can:

- Select the connection row.
- Select Create data view from the blue action bar.

See [Create or edit a data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview) for more information.

### Journey Optimizer connections

You can use a Journey Optimizer connection in Customer Journey Analytics to bring the following additional value to your connection:

- Perform in-depth analysis of Journey Optimizer data within Customer Journey Analytics (by using the Analyze in CJA button within Journey Optimizer). For more information, see Analyze in Customer Journey Analytics in the Journey Optimizer documentation.
- Edit the Journey Optimizer connection and associated data views. For more information about editing options, see Edit a connection .

IMPORTANT
When you enable a Journey Optimizer connection for use with Customer Journey Analytics as described in this section, each Row of Data within the connection counts toward your licensed Rows of Data each month for Customer Journey Analytics and appears within the Connections Usage UI. Select the
Use in CJA
option on the connection only if you are comfortable with the additional usage of Rows of Data in Customer Journey Analytics.
If you were entitled to both Customer Journey Analytics and Journey Optimizer between October 2024 and October 2025, see the following document about
AJO-Enabled Connections
.
To enable this functionality, your organization needs access to Customer Journey Analytics. If you don’t have access, contact your Adobe sales representative.

#### Use a Journey Optimizer connection use-connection-in-cja

To use a Journey Optimizer connection in Customer Journey Analytics:

- Locate the Journey Optimizer connection that you want to use with Customer Journey Analytics. Select Filter in the Connections tab. In the Use in CJA section, select Off . This displays all Journey Optimizer connections that are not currently configured for use in Customer Journey Analytics.
- Select the name of the Journey Optimizer connection.
- Select Use in CJA . The Use this connection in Customer Journey Analytics dialog displays.
- Enable the toggle, Use connection in CJA .
- Select Use connection .

#### Remove a Journey Optimizer connection remove-connection-in-cja

You can remove a Journey Optimizer connection from Customer Journey Analytics at any time. However, removing the connection from Customer Journey Analytics after it is being used results in the following:

- The Journey Optimizer connection and any associated data views are reset to their default state and can no longer be edited
- Any custom derived fields associated with the connection are deleted.
- You can no longer perform in-depth analysis of Journey Optimizer data within Customer Journey Analytics. This means that the Analyze in CJA button in Journey Optimizer is disabled.

IMPORTANT
Billing for the connection in Customer Journey Analytics includes the full month during which the connection is removed.
To remove the connection from Customer Journey Analytics:

- Locate the Journey Optimizer connection that you want to remove from Customer Journey Analytics. Select Filter in the Connections tab. In the Use in CJA section, select On . This displays all Journey Optimizer connections that are currently configured for use in Customer Journey Analytics.
- To view the connection, select the name of the Journey Optimizer connection that you want to remove from Customer Journey Analytics.
- When viewing the Journey Optimizer connection, select Remove from CJA . The Remove this connection from Customer Journey Analytics dialog displays:
- Disable the option, Remove connection from CJA .
- Select Remove connection .

### Map a connection

To view a [connection map](/en/docs/analytics-platform/using/cja-connections/create-connection#connection-map) that details the relationships between the datasets that are part of a connection:

- Select next to the connection name.
- Select **Connection map**.

### Connection details connection-detail

To go to the details for a connection, select a hyperlinked connection name in the connections table.

The Connections details interface provides a detailed view of the status of a connection. You can:

- Check the status of your connection’s datasets and of the ingestion process.
- Identify configuration problems that can cause skipped or deleted records.
- See when the data is available for reporting.

User Interface
Description
Edit Connection
To edit the details of a connection, select
Edit Connection
. See
Create or edit a connection
for more information.
Dataset selector
Select one or all datasets to show details for in the connection. You cannot multi-select datasets. Defaults to
All datasets
.
Date range selector
Select a data range to show details for in the connection. Edit start date, end date, or select
to open the date range selector. In the date range selector, select a date range by using one of the predefined periods (for example
Last 6 months
) or use the calendar to select start and end date. Select
Apply
to apply the new date range to the connection details.
Records of event data available
The total number of event dataset rows available for reporting,
for the entire connection
. This count is independent of any date range or dataset selection.
Metrics
Summarize the event, lookup, profile and summary dataset records that are added, skipped, and deleted, and the number of batches added. These metrics are based on **the dataset and date range that you have selected**.

Select **Check detail** to show the **Check skipped detail** popup. The popup lists the number of skipped records and the reason for all event datasets or selected dataset.

Select popup with more information. For some skipped reasons, like Empty visitor ID, the popup displays **Sample PSQL for EQS** (Experience Platform for Query Service) you can use in [Query Service](/en/docs/experience-platform/query/home) to query for the skipped records in the dataset. Select **Copy sample PSQL for EQS** to copy the SQL.

Records added
A visualization to indicate how many rows were added in the selected time period,
for the dataset and date range you have selected
. Updates every 10 minutes.
Records skipped
A visualization to indicate how many rows were skipped in the selected time period, **for the dataset and date range you have selected**. Reasons for skipping records include: missing timestamps, missing or invalid Person ID or Account ID [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), and so forth. Updates every 10 minutes.

Invalid IDs (such as undefined, or 00000000, or any combination of numbers and letters in a Person ID that appear in an event more than 1 million times in a given month) are IDs that cannot be attributed to any specific user or person. These rows cannot be ingested into the system and result in error-prone ingestion and reporting. To fix invalid Person IDs or Account IDs [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), you have 3 options:

- Use [Stitching](/en/docs/analytics-platform/using/stitching/overview) to populate the undefined or all-zero user IDs with valid user IDs.
- Blank out user IDs, which are then skipped during ingestion (preferable to invalid or all-zero user IDs).
- Fix any invalid user IDs in your system before ingesting the data.

Records deleted
A visualization to indicate how many rows were deleted in the selected time period, **for the dataset and date range you have selected**. Someone might have deleted a dataset in Experience Platform, for example. Updates every 10 minutes.

In some scenarios, this value can also include records replaced, as with stitching or some lookup dataset updates. Consider this example:

- You upload one record to an XDM Individual Profile dataset, which Customer Journey Analytics is configured to ingest as profile lookup data. In the connection details, this dataset would display 1 record added.
- You upload a duplicate of the original record into the same AEP dataset, which now contains two records. Customer Journey Analytics ingests the additional record from the profile or account [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank) lookup dataset. Seeing that a profile or account record is already ingested in the connection for that Person ID or Account ID [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), Customer Journey Analytics deletes its earlier version and adds the new profile data. In the connection details, this action would represent 1 record added and 1 record deleted, because Customer Journey Analytics only retains the most recent profile lookup data for any ingested Person ID or Account ID [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank).
- In total, the AEP dataset contains two records that happen to be identical. Separately, the Customer Journey Analytics connection details display the status of its ingested data: 2 records added and 1 record deleted for this profile dataset.

Dataset search field. You can search the datasets table by dataset name or dataset ID.
Datasets table
The datasets that are part of the connection. See the table below for further explanation. Select
a single dataset to show only connection details for the selected dataset. This is equivalent to the selection of a dataset from the
Dataset selector
.
The datasets table displays the following columns for each dataset:

Column
Description
Datasets
The name of the dataset. You can select the hyperlink to open the dataset in the Experience Platform UI in a new tab. You can select the row or the checkbox to show details for the selected dataset only.
Dataset ID
The dataset id, generated by Experience Platform.
Records added
The number of dataset records (rows) added to a connection during the selected date range.
Records skipped
The number of dataset records (rows) skipped during data transfer for a connection during the selected date range.
Records deleted
The number of dataset records (rows) removed from a connection during the selected date range.
Batches added
The number of batches that have been added to a connection during the selected date range.
Last added
The timestamp of the latest batch that has been added to a connection.
Data source type
The source type. You define the source type when you add a dataset to a connection.
Dataset type
The
dataset type
. Type can be
Event
,
Profile
,
Lookup
,
Summary
. An adhoc or relational dataset is identifed by
(Adhoc)
or
(Relational)
. For example,
Event (Adhoc)
or
Lookup (Relational)
.
Stitched
If a dataset is
enabled for stitching in the Connection UI
, the value is
true
. Otherwise the value is
false
. Stitched datasets that are the result of the
request to stitch procedure
are not identified as stitched in this table, and by default have a value of
false
.
Schema
The Experience Platform schema that the dataset is based on.
Import new data
The status of importing new data for the dataset:

**x On** if dataset is configured to import new data, and

*x Off* if dataset is configured not to import new data import.

Transform data
The transformation status of applicable B2B lookup datasets. See [Transform datasets for B2B lookups](/en/docs/analytics-platform/using/cja-connections/transform-datasets-b2b-lookups) for more information.

**x On** for applicable datasets enabled for transformation,

*x Off* for applicable datasets not enabled for transformation, and

**N/A** for all other datasets, not applicable for transformation.

Backfill data
The status of backfill data for the dataset.

**x backfills failed** for number of failed backfills,

**x backfills processing** for number of processing backfills,

**x backfills completed** for number of backfills completed, and

*Off* in case backfills are not configured.

IMPORTANT
Any data ingested before August 13, 2021 is not reflected in the Connections interface.
#### Connection panel

When no individual dataset is selected in the datasets table, the right panel shows connection options and details.

Options
Description
Refresh
To refresh the connection and allow recently added records to be reflected, select
Refresh
.
Delete
Delete
this connection.
Create data view
Create a data view
based on this connection. See
Data views
for more information.
Use in CJA
Use a Journey Optimizer connection in Customer Journey Analytics to bring additional value to your Journey Optimizer connection. For more information, see
Use a Journey Optimizer connection in Customer Journey Analytics
.
Connection name
The friendly name of the connection.
Connection description
A more detailed description that describes the purpose of this connection.
Sandbox
The
Experience Platform sandbox
from which this connection draws its datasets. You select this sandbox when you created the connection. You cannot change the sandbox once a connection is saved.
Connection ID
A generated identifier for the connection. You can use
to copy the value.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Primary ID type
The primary ID type for the connection:
Person
for a person-based connection,
Account
for an account-based connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Containers
The configured containers for the connection.
Data views using connection
The data views that use this connection.
Import new data
The status of importing new data for datasets:

**x On** for how many datasets are configured to import new data, and

*x Off* for how many datasets new data import is turned off.

Backfill data
The status of backfill data for datasets.

**x backfills failed** for number of failed backfills across datasets,

**x backfills processing** for number of processing backfills across datasets,

**x backfills completed** for number of completed backfills for datasets, and

*Off* in case no backfills are defined for the datasets in the connection.

Transform data
The transformation status of applicable B2B lookup datasets. See [Transform datasets for B2B lookups](/en/docs/analytics-platform/using/cja-connections/transform-datasets-b2b-lookups) for more information.

**x On** for number of datasets enabled for transformation.

Created by
The name of the person who created the connection.
Last modified
The timestamp of the last change to the connection.
Last modified by
The name of the person who last modified the connection.
#### Dataset panel

When a dataset row is selected in the datasets table, a panel on the right side of the Connections interface show details for the selected dataset.

Details
Description
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Global Account ID
The identity you have specified as the Global Account ID for the connection. Only applicable for an account-based connection for which a Global Account container is configured.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Account ID
The identity you have specified as the Account ID for the connection. Only applicable for an account-based connection for which no Global Account container is configured.
Person ID
The identity you have specified as the Person ID for the connection.
Key
The key that you have specified for a lookup dataset.
Matching Key
The matching key that you have specified for a lookup dataset.
Timestamp
The timestamp defined for an event dataset.
Records available
The total number of rows ingested for this dataset, for the particular time period selected through the calendar. There is no latency in terms of getting the data to appear in reporting, once it is added. However, when you create a brand new connection, there is
latency
.
Records added
The number of dataset records (rows) added to a connection during the selected date range.
Records skipped
The number of dataset records (rows) skipped during data transfer for a connection during the selected date range.
Batches added
The number of batches that have been added to a connection.
Records deleted
The number of dataset records (rows) removed from a connection during the selected date range.
Last added
The timestamp of the latest batch that has been added to a connection.
Import new data
The status of importing new data for the dataset:

**x On** if the dataset is configured to import new data, and

*x Off* if the dataset is configured not to import new data.

Backfill data
The status of backfill data for the dataset.

**x backfills failed** for number of failed backfills,

**x backfills processing** for number of processing backfills,

**x backfills completed** for number of backfills completed, and

*Off* in case no backfills are configured.

To show a dialog with an overview of the past backfills for the dataset, select {width="15"} **Past backfills**.

Data source type
Data source type as defined when the dataset was added to the connection.
Dataset type
The
dataset type
. Type can be
Event
,
Profile
,
Lookup
,
Summary
. An adhoc or relational dataset is identifed by
(Adhoc)
or
(Relational)
. For example,
Event (Adhoc)
or
Lookup (Relational)
.
Schema
The Experience Platform schema that this dataset is based on.
Dataset ID
The dataset ID, as generated in Experience Platform.
## Usage connections-usage

The Usage interface shows the usage of ingested and reportable rows across all connections. If not selected, select the **Usage** tab to access the interface.

This interface supports you to determine whether your Customer Journey Analytics usage complies with what is contractually agreed upon. In addition to monitoring purposes, you can use the Usage interface to plan your Customer Journey Analytics license renewal.

The Usage interface uses the following metrics:

Metric name
Description
Historical reportable rows
Count of rows for the period older than 13 months.
Core reportable rows
Count of rows over the last 13 months.
Core data volume
Total amount of data stored on disk.
Average row size
Average amount of storage consumed for each row of data ingested and stored.
Ingested rows
How many rows are ingested for the specific period.
Reportable rows
How many rows of data do you have as part of the connection for the specific period.
Cumulative rows
How many rows are ingested up until the specific month.
NOTE
Data is collected, starting from July 2024 for the core, historical, and total records. Reach out to your account manager for earlier historical data.
The Usage interface consists of two panels:

- The Key usage metrics panel that displays: Four summary visualizations that display total and percentual changes from the previous month for: Core data reportable rows . The total number of rows available over the past 13 months for the current month, with a percentage change compared to the previous month. For example, on February 1, 2024, the number shows the total rows available with an event timestamp from January 2023 to January 2024. Historical data reportable rows . The total number of rows available over a period older than 13 months for the current month, with a percentage change compared to the previous month. For example, on February 1, 2024, the number shows the total rows available with an event timestamp older than January 2023. Core data volume . The total amount of data stored on disk that is timestamped for the current month (in TB), with a percentage change compared to the previous month. Average row size . The average amount of storage consumed by each row of data ingested and stored for the current month (in kB), with a percentage change compared to the previous month. A stacked vertical bar visualization that displays the Core and Historical data reportable rows for the last 13 months. When you hover over any stacked bar in the visualization, a popup shows the number of rows for that specific part of the bar. In the example below, the core data reportable rows are shown for the current month (August 2025: 936M (936,347,325)).
- A combined panel, showing three subpanels for: accordion Ingested rows The Ingested rows subpanel measures the total number of records added to the system each month, providing insight into data growth and ingestion rates. The subpanel provides a summary of this month’s total ingested rows and the change from the previous month. You can hover over data points in the visualization to display a popup with more details. accordion Reportable rows The Reportable rows visualization tracks the number of rows available for reporting by subtracting skipped and deleted rows from ingested rows, serving as a key metric for billing and data usage. The subpanel provides two summaries: Last month total : A summary of total reportable rows up until this month. This month : A summary of this month’s total reportable rows and the change from the previous month. You can hover over data points in the visualizations to display a popup with more details. accordion Detail breakdown You can use the Detail breakdown table to view detailed metrics by connection, dataset, sandbox, and tags. Datasets are reported using ids instead of names, as dataset names can be modified during a reporting period. Unknown datasets or connections are reported using ids. For the months before September 2024, data was collected at the dataset level and is displayed as Other datasets for clarity. Starting from September 2024, data is gathered at a granular dataset level, and Other datasets do no longer appear. To change the breakdown, select a combination for View by and Breakdown by . table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 View by options Breakdown by options Connection - and Dataset Dataset - Sandbox Connection Tag Connection You can define a Time range in months to report on. Use to select the time range.

Related Articles
View, troubleshoot, and modify connection settings
tutorial.
Manage your Customer Journey Analytics usage
recommendation-more-help
