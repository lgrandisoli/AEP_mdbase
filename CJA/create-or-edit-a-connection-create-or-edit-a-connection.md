---
title: "Create or edit a connection create-or-edit-a-connection"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/create-connection"
category: "other"
topic: "analytics-platform/using/cja-connections/create-connection"
created_at: "2026-06-02T19:04:28.930059+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create or edit a connection create-or-edit-a-connection

Last update: May 13, 2026
- Topics:
- [Connections](#)

CREATED FOR:

- Admin

The connection creation and edit workflow experience brings all the dataset and connection configuration settings to the center of the screen with an assistive workflow. It provides detailed dataset selection, configuration, and review experience. And allows you to specify critical information like [dataset type](#dataset-types), size, schema, dataset id, batch status, backfill status, identities, and much more, to reduce the risk of wrong connection configuration. Here is an overview of the capabilities:

- You can enable a rolling data retention window when you create the connection.
- You can add to and remove datasets from a connection. (Removing a dataset removes it from the connection and impacts any associated data views and underlying Analysis Workspace projects.)
- You can enable and request backfill data per dataset.
- You can edit datasets, for example to request another backfill.
- You can import existing data per dataset.

See [Connect to data sources](/en/docs/customer-journey-analytics-learn/tutorials/connections/connecting-customer-journey-analytics-to-data-sources-in-platform#_blank) for a demo video.

style
shade-box
## Prerequisites

The maximum number of datasets you can add to a connection is capped at 100. The mix depends on which Customer Journey Analytics package your company has purchased.

Contact your administrator if you’re unsure which Customer Journey Analytics package you have.

Select
package
Foundation
package
Any combination of event, profile, lookup, or summary datasets, adding up to 100
One event dataset per connection
Up to 99 profile, lookup, or summary datasets per connection
## Create a connection create-connection

To create a connection:

- In Customer Journey Analytics, select **Connections**, optionally from **Data management**, in the top menu.
- Select **Create new connection**.

You can now [edit the details for your connection](#edit-a-connection).

## Edit a connection edit-connection

How you edit the connection depends on the Customer Journey Analytics package you have licensed:

- [Customer Journey Analytics](#customer-journey-analytics)
- [Customer Journey Analytics B2B Edition](#customer-journey-analytics-b2b-edition)

### Customer Journey Analytics

In the **Connections** > *Name of the connection* screen:

- Configure the connection settings. table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Setting Description Connection name Enter a unique name for the connection. Connection description Describe the purpose of this connection. Tags Specify tags to add tags to your connection so you can use these tags to search for the connection at a later stage. Enable rolling data window This checkbox, if checked, lets you define Customer Journey Analytics data retention as a rolling window in months (1 month, 3 months, 6 months, and so on), at the connection level. Data retention is based on event dataset timestamps and applies to event datasets only. No rolling data window setting exists for profile or lookup datasets, since there are no applicable timestamps. However, if your connection includes any profile or lookup datasets (besides one or more event datasets), that data is retained for the same time period. The main benefit is that you store or report only on data that is applicable and useful and delete older data that is no longer useful. It helps you stay under your contract limits and reduces the risk of overage cost. If you leave the default (unchecked), the Adobe Experience Platform data retention setting supersedes the retention period. If you have 25 months’ worth of data in Experience Platform, Customer Journey Analytics gets 25 months of data through backfill. If you deleted 10 of those months in Experience Platform, Customer Journey Analytics would retain the remaining 15 months. If you enable a rolling data window, specify in Select number of months the number of months for which you enable the rolling data window. Sandbox Choose a sandbox in Experience Platform that contains the datasets for which you want to create a connection. Adobe Experience Platform provides sandboxes which partition a single Platform instance into separate virtual environments to help develop and evolve digital experience applications. You can think of sandboxes as “data silos” that contain datasets. Sandboxes are used to control access to datasets. Once you have selected the sandbox, the left rail shows all the datasets in that sandbox that you can pull from. Add datasets Select Add datasets to add datasets. If the connection has no datasets yet, you can also select Add datasets in the datasets table. For the datasets you have configured, the table of datasets shows the following columns: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 Column Description Dataset name Select one or more datasets that you want to pull into Customer Journey Analytics and select Add . (If you have many datasets to choose from, you can search for the right one(s) using the Search datasets search bar above the list of datasets.) Select to open a context menu for the selected dataset. Based on the (type of) dataset, you can select: Delete dataset to delete a dataset . Edit dataset to edit a dataset . Past backfills to display past backfills for the dataset . Last updated For event datasets only, this setting is automatically set to the default timestamp field from event-based schemas in Experience Platform. “N/A” means that this dataset contains no data. Number of records The total records in the previous month for the dataset in Experience Platform. Schema The schema based on which the dataset was created in Adobe Experience Platform. Dataset type For each dataset that you added to this connection, Customer Journey Analytics automatically sets the dataset type based on the data coming in. There are 3 different dataset types: Event data, Profile data, and Lookup data. See the table below for an explanation of dataset types. Stitched If a dataset is enabled for stitching in the Connection UI , the value is true . Otherwise, the value is false . Stitched datasets that are the result of the request to stitch procedure are not identified as stitched in this table, and by default have a value of false . Granularity The granularity of the data in the dataset; only applicable for summary datasets. Data source type The data source type of the dataset. Not applicable for summary datasets. Person ID The Person ID that is used to support person-based reporting for the dataset. Key The key that is used for a lookup dataset. Matching Key The matching key that is used for a lookup dataset. Import new data The status of importing new data for the dataset: x On if the dataset is configured to import new data, and x Off if the dataset is configured not to import new data. Backfill data The status of backfill data for the dataset. x backfills failed for number of failed backfills, x backfills processing for number of processing backfills, x backfills completed for number of backfills completed, and Off in case no backfills are configured. You can search for a specific dataset using the field.

### Customer Journey Analytics B2B Edition

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)

In the **Connections** > *Name of the connection* screen:

- Configure the connection settings. table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 Setting Description Connection name Enter a unique name for the connection. Connection description Describe the purpose of this connection. Tags Specify tags to add tags to your connection so you can use these tags to search for the connection at a later stage. Primary ID Select the proper primary ID for your connection: Person for a person-based connection you typically use in a B2C scenario. Account for an account-based connection you typically use in a B2B scenario. As soon as you add one or more datasets to your connection, you are no longer able to change the primary ID. The selection of the primary ID defines whether the connection is person-based or account-based. The connection base determines the available settings for certain types of datasets. Optional containers If you have selected Account as the Primary ID , select additional containers. Global account : enables configuration of global accounts in a connection. Opportunity : enables configuration of opportunities in a connection. Buying group : enables configuration of buying groups in a connection. Sandbox Choose a sandbox in Experience Platform that contains the datasets to which you want to create a connection. Adobe Experience Platform provides sandboxes which partition a single Platform instance into separate virtual environments to help develop and evolve digital experience applications. You can think of sandboxes as “data silos” that contain datasets. Sandboxes are used to control access to datasets. Once you have selected the sandbox, the left rail shows all the datasets in that sandbox that you can pull from. Enable rolling data window This checkbox, if checked, lets you define Customer Journey Analytics data retention as a rolling window in months (1 month, 3 months, 6 months, and so on), at the connection level. Data retention is based on event dataset timestamps and applies to event datasets only. No rolling data window setting exists for profile or lookup datasets, since there are no applicable timestamps. However, if your connection includes any profile or lookup datasets (besides one or more event datasets), that data is retained for the same time period. The main benefit is that you store or report only on data that is applicable and useful and delete older data that is no longer useful. It helps you stay under your contract limits and reduces the risk of overage cost. If you leave the default (unchecked), the Adobe Experience Platform data retention setting supersedes the retention period. If you have 25 months’ worth of data in Experience Platform, Customer Journey Analytics gets 25 months of data through backfill. If you deleted 10 of those months in Platform, Customer Journey Analytics would retain the remaining 15 months. If you enable a rolling data window, specify in Select number of months the number of months for which you enable the rolling data window. Add datasets Select Add datasets to add datasets . If the connection has no datasets yet, you can also select Add datasets in the datasets table. For the datasets you have configured, the table of datasets shows the following columns: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 16-row-2 17-row-2 Column Description Dataset name Select one or more datasets that you want to pull into Customer Journey Analytics and select Add . (If you have many datasets to choose from, you can search for the right one(s) using the Search datasets search bar above the list of datasets.) Select to open a context menu for the selected dataset. Based on the (type of) dataset, you can select: Delete dataset to delete a dataset . Edit dataset to edit a dataset . Past backfills to display past backfills for the dataset . Last updated For event datasets only, this setting is automatically set to the default timestamp field from event-based schemas in Experience Platform. “N/A” means that this dataset contains no data. Number of records The total records in the previous month for the dataset in Experience Platform. Schema The schema based on which the dataset was created in Adobe Experience Platform. Dataset type For each dataset that you added to this connection, Customer Journey Analytics automatically sets the dataset type based on the data coming in. Granularity The granularity of the data in the dataset; only applicable for summary datasets. Data source type The data source type of the dataset. Not applicable for summary datasets. Account ID (only displayed for account-based connections) The Account ID that is used to support account-based reporting for the dataset. Global Account ID (only displayed for account-based connections) The Global Account ID that is used to support account-based reporting for the dataset. Buying Group ID (only displayed for account-based connections) The Buying Group ID that is used to lookup buying group data. Opportunity ID (only displayed for account-based connections) The Opportunity ID that is used to lookup opportunity data. Person ID The Person ID that is used to support person-based reporting for the dataset. Key The key that is used for a lookup dataset. Matching Key The matching key that is used for a lookup dataset. Import new data The status of importing new data for the dataset: x On if the dataset is configured to import new data, and x Off if the dataset is configured not to import new data. Backfill data The status of backfill data for the dataset. x backfills failed for number of failed backfills, x backfills processing for number of processing backfills, x backfills completed for number of backfills completed, and Off in case no backfills are configured. You can search for a specific dataset using the field.

## Datasets datasets

You [add one or more datasets](#add-datasets) or [edit existing datasets](#edit-a-dataset) as part of connection workflow.

NOTE
Values earlier than the year 1900 for Date and Date-time fields in a row in any type of dataset are replaced with the value
null
before the row is ingested.
Rows in an event or summary dataset with a timestamp value before the year 1900 are dropped from ingestion.
INFO
In the Customer Journey Analytics interface,
Relational
datasets might be labeled as
Model-based
.
### Dataset types dataset-types

For each dataset that you add to this connection, Customer Journey Analytics automatically sets the dataset type based on the data coming in.

IMPORTANT
Add at least one event or summary dataset (standard or of type ad hoc or relational) to your connection.
There are different dataset types: Event data, Profile data, Lookup data and Summary data, each based on their corresponding XDM-based schema.

Dataset type
Description
Timestamp
Schema
Person ID
Account ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Event
Data that represents events in time. For example, web visits, interactions, transactions, POS data, survey data, ad impression data, and so on. This data could be typical clickstream data, with a customer ID or a Cookie ID, and a timestamp. With event data, you have flexibility which ID is used as the Person ID.
Set to the default timestamp field from event-based schemas in Experience Platform.
Any built-in or custom schema that is based on an XDM class with the
Time Series
behavior. Examples include
XDM Experience Event
or
XDM Decision Event
.
You can pick which Person ID or Account ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
you want to include. Each dataset schema defined in the Experience Platform can have its own set of one or more identities defined and associated with an identity namespace. Any of these identities can be used as the Person ID or Account ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
. Examples include Cookie ID, Stitched ID, User ID, Tracking Code, Account ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
, and so on.
Lookup
You can add datasets as lookups of fields within all dataset types: Profile, Lookup, and Event datasets (the latter was always supported). This additional capability expands the capability of Customer Journey Analytics to support complex data models, including B2B. This data is used to look up values or keys found in your Event, Profile, or Lookup data. You can add up to three levels of lookups. (Note that
Derived Fields
cannot be used as matching keys for lookups within Connections.) For example, you might upload lookup data that maps numeric IDs in your event data to product names. See the
B2B example
for an example.
N/A
Any built-in or custom schema that is based on an XDM class with the
Record
behavior, except for the
XDM Individual Profile
class.
N/A
Profile
Data that is applied to your account, persons, users, or customers in the Event data. For example, allows you to upload CRM data about your customers.
N/A
Any built-in or custom schema that is based on the
XDM Individual Profile
class.
You can pick which Person ID / Account ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
you want to include. Each dataset (except summary datasets), defined in Experience Platform, has its own set of one or more Person IDs or Account IDs
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
defined. For example, Cookie ID, Stitched ID, User ID, Tracking Code, Account ID, and so on.
Note
: If you create a connection that includes datasets with different IDs, the reporting reflects that. To merge datasets, you need to use the same Person ID or Account ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
.
Summary
Time-series data that is not associated with an individual Person ID. Summary data represents aggregated data at a different level of aggregation, for example campaigns. You can use this data in Customer Journey Analytics to support various use cases. See
Summary data
for more information.
Automatically set to the default timestamp field from event-based Summary Metrics schemas in Experience Platform. Only hourly or daily granularity is supported.
Any built-in or custom schema that is based on the
XDM Summary Metrics
class.
N/A
Alternatively, the dataset types listed above, can be based on an ad hoc or relational schema instead of a generic XDM-based schema.

Dataset type
Description
Timestamp
Schema
Person ID
Adhoc
Ad hoc data based on an
ad hoc schema
with fields that are namespaced for usage only by a single dataset.
Dependent on the dataset type you select for the ad hoc dataset.
Any ad hoc schema that is based on a class based on the
ad hoc
behavior
Dependent on the dataset type you select for the ad hoc dataset.
Model
Relational data based on a relational schema.
Dependent on the dataset type you select for the relational dataset.
Any relational schema.
Dependent on the dataset type you select for the relational dataset.
### Add datasets

You can add one or more Experience Platform datasets when you create or edit a connection.

#### For person-based connections

- In Connection > Name of the connection interface, select Add datasets .
- In the ➊ Select datasets step, you see a list of the Experience Platform datasets. For each dataset, the list shows: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Column Description Dataset Name of the dataset. Select the name to direct you to the dataset in Experience Platform. Select to display a popup with more details for the dataset. You can select Edit in Platform to edit the dataset directly in Experience Platform. Dataset type The type of dataset: Event , Profile , Lookup , Summary , Adhoc , or Relational . Number of records The total records in the previous month for the dataset in Experience Platform. Schema The schema for the dataset. Select the name to direct you to the schema in Experience Platform. Last batch The state of the last batch ingested in Experience Platform. See Batch states more information. Dataset ID The id of the dataset. Last updated The last updated timestamp of the dataset. To change the columns displayed for the list of datasets, select and select the columns to be displayed in the Customize table dialog. To search for a specific dataset, use the search field. To toggle between showing or hiding the selected datasets, select Hide selected or Show selected . To remove a dataset from the list of selected datasets, use . To remove all selected datasets, select Clear all . To display details of a dataset, select .
- Select one or more datasets and select Next . At least one event or summary dataset must be part of the connection.
- Configure the settings for each of the selected datasets , one by one, in the ➋ Datasets settings step of the Add datasets dialog. To remove a dataset from the connection, select Remove . To take a step back, select Back . To cancel adding datasets to a connection, select Cancel .
- You need to specify all the required settings for the selected datasets before you can continue. If required input is missing, you see a red number that indicates how many datasets of a specific type are missing that required input. A and an explanation in red identify required fields that do not have input or a selected value. Once you have configured all required settings for all datasets, select Next .
- In ❸ Datasets preview you see a preview for each dataset that is based on a simple set of data from recently ingested data. To show namespaces for each of the columns in the table, enable Show column namespace . To search in the sample data, use . To configure what columns to show, select . In the Customize table dialog: Select the columns that you want to show in the table. Select Apply to apply the selection, or Cancel to cancel the selection. To display the data for columns that contain array or object data, select Values . The Dataset info pane shows details about the dataset. Select the value for Schema or Dataset to open the relevant interface in Experience Platform in a new browser tab. To remove a dataset from the connection, select Remove . To take a step back, select Back . To cancel adding datasets to a connection, select Cancel .
- Select Add datasets to add the configured datasets to the connection.

#### For account-based connections

You can add one or more Experience Platform datasets when you create or edit a connection.

- In Connection > Name of the connection interface, select Add datasets .
- In the ➊ Select datasets step, you see a list of the Experience Platform datasets. For each dataset, the list shows: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Column Description Dataset Name of the dataset. Select the name to direct you to the dataset in Experience Platform. Select to display a popup with more details for the dataset. You can select Edit in Platform to edit the dataset directly in Experience Platform. Dataset type The type of dataset: Event , Profile , Lookup , Summary , Adhoc , or Relational . Number of records The total records in the previous month for the dataset in Experience Platform. Schema The schema for the dataset. Select the name to direct you to the schema in Experience Platform. Last batch The state of the last batch ingested in Experience Platform. See Batch states more information. Dataset ID The id of the dataset. Last updated The last updated timestamp of the dataset. To change the columns displayed for the list of datasets, select and select the columns to be displayed in the Customize table dialog. To search for a specific dataset, use the search field. To toggle between showing or hiding the selected datasets, select Hide selected or Show selected . To remove a dataset from the list of selected datasets, use . To remove all selected datasets, select Clear all . To display details of a dataset, select .
- Select one or more datasets and select Next . At least one event or summary dataset must be part of the connection.
- Configure the settings for each of the selected datasets , one by one, in the ➋ Datasets settings step of the Add datasets dialog.
- Select Add datasets to add the configured datasets to the connection. You are notified when you have not provided all required settings for each of the datasets you want to add. Alternatively, you can select Cancel to cancel the addition of datasets to the connection. Or select Back to step back to the ➊ Select datasets step.

### Edit a dataset

To edit a dataset that is already configured for a connection, in the **Connections** > *Name of the connection* interface:

#### For person-based connections

- Select Edit connection .
- Select for the dataset listed in the dataset table that you want to edit.
- Select Edit dataset .
- In ❶ Dataset settings , configure the dataset settings in the Edit dataset: Dataset name dialog. If you make changes, ensure you specify all required settings for the dataset before you continue. If the required input is missing, you cannot continue. A and an explanation in red identify required fields that do not have input or a selected value. note NOTE You cannot edit the Dataset type , Person ID , Identity namespace and Timestamp for an ad hoc or a relational dataset that is part of a saved connection. To change any of these settings: Delete the existing ad hoc or relational dataset from the connection. Add the same dataset with updated settings to the connection. To remove the dataset from the connection, select Remove . Once you have configured all the required settings for the dataset, select Next .
- In ❷ Datasets preview you see a preview for each dataset that is based on a simple set of data from recently ingested data. To show namespaces for each of the columns in the table, enable Show column namespace . To search in the sample data, use . To configure what columns to show, select . In the Customize table dialog: Select the columns that you want to show in the table. Select Apply to apply the selection, or Cancel to cancel the selection. To display the data for columns that contain array or object data, select Values . The Dataset info pane shows details about the dataset. Select the value for Schema or Dataset to open the relevant interface in Experience Platform in a new browser tab. To remove a dataset from the connection, select Remove . To take a step back, select Back . To cancel adding datasets to a connection, select Cancel .
- Select Apply to apply the dataset settings. Select Cancel to cancel.

#### For account-based connections

- Select Edit connection .
- Select for the dataset listed in the dataset table that you want to edit.
- Select Edit dataset .
- Configure the dataset settings in the Edit dataset: Dataset name dialog. note NOTE You cannot edit the Dataset type , Person ID , Identity namespace and Timestamp for an ad hoc or a relational dataset that is part of a saved connection. To change any of these settings: Delete the existing ad hoc or relational dataset from the connection. Add the same dataset with updated settings to the connection.
- Select Apply to apply the dataset settings. Select Cancel to cancel.

### Dataset settings

When you add datasets or edit an existing dataset, you configure the dataset settings for each dataset. The settings available depend on the [type of dataset](#dataset-types) and, for some dataset types, on the type of connection (person-based or [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank) account-based.).

All datasets and dataset types have [general settings and details](#general-dataset-settings-and-details), such as whether or not to import new data and request backfills.

#### Event dataset

The specific settings for an event dataset are dependent on the type of connection.

##### Person-based connection

For an event dataset in a person-based connection, you can specify:

Setting
Description
Person ID
Select a Person ID from the drop-down menu of available identities. These identities were defined in the dataset schema in Experience Platform. See [Use Identity Map as a Person ID](#use-identity-map-as-a-person-id) for information on how to use Identity Map as a Person ID.

If there are no Person IDs to choose from, that means no Person IDs are defined in the schema. See [Define identity fields in the UI](/en/docs/experience-platform/xdm/ui/fields/identity) for more information.

The value for the selected Person ID is considered to be case sensitive. For example, abc123 and ABC123 are two different values.

If a record doesn’t contain a value for the identity you have selected as the Person ID for the event dataset, the record is skipped.

Enable identity stitching
Select to
enable identity stitching
for this event dataset.
Timestamp
This setting is automatically set to the default timestamp field from event-based schemas in Experience Platform.
Data source type
Select a type of data source. Types of data sources include:

- Web data
- Mobile App data
- POS data
- CRM data
- Survey data
- Call Center data
- Product data
- Accounts data
- Transaction data
- Customer Feedback data
- Other

This field is used to survey the types of data sources in use.

Data source description
A description of the data source when you have selected Other as the data source type.
##### Account-based connection

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)

For an event dataset in an account-based connection, you can specify:

Setting
Description
Global Account ID
Select a Global Account ID (the unique identifier for an account) from the available identities defined in the dataset schema in the Experience Platform. Applicable when you have added Global Account as a container to your connection.

If a record doesn’t contain a value for the identity you have selected as the Account ID for the event dataset, the record is skipped.

Account ID
Select an Account ID (the unique identifier for an account) from the available identities defined in the dataset schema in the Experience Platform. Applicable when you have not added Global Account as a container to your connection.
Opportunity ID
Select an Opportunity ID (the unique identifier for an opportunity) from the available identities defined in the dataset schema in the Experience Platform.
Buying Group ID
Select a Buying Group ID (the unique identifier for a buying group) from the available identities defined in the dataset schema in the Experience Platform.
Person ID
Select a Person ID from the drop-down menu of available identities. These identities were defined in the dataset schema in the Experience Platform. See [Use Identity Map as a Person ID](#id-map) for information on how to use Identity Map as a Person ID.

If there are no Person IDs to choose from, that means one or more Person IDs have not been defined in the schema. See [Define identity fields in the UI](/en/docs/experience-platform/xdm/ui/fields/identity) for more information.

The value for the selected Person ID is considered to be case sensitive. For example, abc123 and ABC123 are two different values.

Timestamp
This setting is automatically set to the default timestamp field from event-based schemas in Experience Platform.
Data source type
Select a type of data source. Types of data sources include:

- Web data
- Mobile App data
- POS data
- CRM data
- Survey data
- Call Center data
- Product data
- Accounts data
- Transaction data
- Customer Feedback data
- Other

This field is used to survey the types of data sources in use.

Data source description
A description of the data source when you have selected Other as the data source type.
#### Profile dataset

The specific settings for a profile dataset are dependent on the type of connection.

##### Person-based connection

For a profile dataset in a person-based connection, you specify:

Setting
Description
Person ID
Select a Person ID from the drop-down menu of available identities. These identities were defined in the dataset schema in Experience Platform. See [Use Identity Map as a Person ID](#id-map) for information on how to use Identity Map as a Person ID.

If there are no Person IDs to choose from, no Person IDs are defined in the schema. See [Define identity fields in the UI](/en/docs/experience-platform/xdm/ui/fields/identity) for more information.

The value for the selected Person ID is considered to be case sensitive. For example, abc123 and ABC123 are two different values.

If a record doesn’t contain a value for the identity you have selected as the Person ID for the profile dataset, the record is skipped.

Data source type
Select a type of data source. Types of data sources include:

- Web data
- Mobile App data
- POS data
- CRM data
- Survey data
- Call Center data
- Product data
- Accounts data
- Transaction data
- Customer Feedback data
- Other

This field is used to survey the types of data sources in use.

Data source description
A description of the data source when you have selected Other as the data source type.
#### Account-based connection

For a profile dataset in an account-based connection, you specify:

Setting
Description
Person ID
Select a Person ID from the drop-down menu of available identities. These identities were defined in the dataset schema in Experience Platform. See [Use Identity Map as a Person ID](#id-map) for information on how to use Identity Map as a Person ID.

If there are no Person IDs to choose from, no Person IDs are defined in the schema. See [Define identity fields in the UI](/en/docs/experience-platform/xdm/ui/fields/identity) for more information.

The value for the selected Person ID is considered to be case sensitive. For example, abc123 and ABC123 are two different values.

If a record doesn’t contain a value for the identity you have selected as the Person ID for the profile dataset, the record is skipped.

Global Account field
Select a global account field to support account-based reporting for the dataset from the drop-down menu of available identities. Applicable when you have added Global Account as a container to your connection.
Account field
Select an account field to support account-based reporting for the dataset from the drop-down menu of available identities. Applicable when you have not added Global Account as a container to your connection.
Data source type
Select a type of data source. Types of data sources include:

- Web data
- Mobile App data
- POS data
- CRM data
- Survey data
- Call Center data
- Product data
- Accounts data
- Transaction data
- Customer Feedback data
- Other

This field is used to survey the types of data sources in use.

Data source description
A description of the data source when you have selected Other as the data source type.
#### Lookup dataset

The specific settings for a lookup dataset are dependent on the type of connection.

##### Person-based connection

For a lookup dataset in a person-based connection, you specify:

Settings
Description
Key
The key to use for a Lookup dataset.

If a record doesn’t contain a value for the key you have selected for the lookup dataset, the record is skipped.

Matching key
The matching key to join on in one of the event datasets. If this list is empty, you probably haven’t added or configured an event dataset.
Data source type
Select a type of data source. Types of data sources include:

- Web data
- Mobile App data
- POS data
- CRM data
- Survey data
- Call Center data
- Product data
- Accounts data
- Transaction data
- Customer Feedback data
- Other

This field is used to survey the types of data sources in use.

Data source description
A description of the data source when you have selected Other as the data source type.
Transform dataset
For specific B2B lookup datasets, you can enable the transformation of a dataset for proper B2B person-based reporting scenarios. See
Transform datasets for B2B lookups
for more information.
##### Account-based connection

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)

For a lookup dataset in an account-based connection, you can specify:

Settings
Description
Key
The key to use for a Lookup dataset.

If a record doesn’t contain a value for the key you have selected for the lookup dataset, the record is skipped.

Matching key type
Select how to join the datasets: based on a
Match by field
or
Match by container
. See
Match by container of field
for more information.
Matching key
The matching key to join on in one of the event datasets. If this list is empty, you probably haven’t added or configured an event dataset.Based on your selected **Matching key type**, select the appropriate value:

- **Match by field**: Select a field from the **Matching key** drop-down menu to join with one of the event datasets. If this list is empty, you probably haven’t added or configured an event dataset.
- **Match by container**: Select a container from the **Matching key** drop-down menu to use to join with one of the event datasets. The containers you included as part of setting up the connection determine the available containers to select.

Global Account field
The Global Account ID to use for account-based reporting.
#### Summary dataset

The specific settings for a summary dataset are:

Setting
Description
Timestamp
This setting is automatically set to the default timestamp field from event-based schemas in Experience Platform.
Timezone
Select the appropriate timezone for the time-series summary data.
Granularity
Represents the time frame used to aggregate summary data by, currently either hour or day. Derived from the data in the dataset.
#### Ad hoc dataset

NOTE
Although possible to configure and select, for performance reasons you should avoid to using an ad hoc dataset for time-series (event, summary) data. Relational or generic XDM based datasets are much better suited for time-series data than ad hoc datasets.
The specific settings for an ad hoc dataset are:

Setting
Selected dataset type
Description
Dataset type
N/A
The type of data in the ad hoc dataset. Possible values are:
Event
,
Profile
,
Lookup
, and
Summary
.
Person ID
Event, Profile
Select a field from the ad hoc or relational schema that represent the Person ID. This field can be any field in the dataset. Select from
Identity namespace fields
or from
Non-identity fields
.
You can only select an identifier from
Identity namespace
if one or more of the fields in the ad hoc schema are labeled as an identity and have an identity namespace.
Identity namespace
Event
Select an identity namespace in case you have selected a Person ID from
Non-identity
fields.
Timestamp
Event, Summary
Select a field from the ad hoc schema that represents the timestamp field. This field can be any of the available fields of type
DateTime
.
Key
Lookup
The key to use for a Lookup dataset.
If a record doesn’t contain a value for the key you have selected for the lookup dataset, the record is skipped.
Matching key
Lookup
The matching key to join on in one of the event or lookup datasets. If this list is empty, you probably haven’t added or configured an event or lookup dataset.
#### Relational dataset

NOTE
Relational datasets are predominantly used to support the upcoming Experience Platform Data Mirror for Customer Journey Analytics capability.
The specific settings for a relational dataset are:

Setting
Selected dataset type
Description
Dataset type
N/A
The type of data in the relational dataset.
If the dataset contains time-series data, the possible values are:
Event
and
Summary
.
If the dataset contains record data, the possible values are:
Profile
and
Lookup
.
Person ID
Event, Profile
Select a field from the relational schema that represents the Person ID. The selection is limited to the list of fields in the relational schema that are marked as Identity and do have an identity namespace.
Timestamp
Event, Summary
The field that is defined as the timestamp descriptor in the schema. This field is populated automatically.
Key
Lookup
The key to use for a Lookup dataset.
If a record doesn’t contain a value for the key you have selected for the lookup dataset, the record is skipped.
Matching key
Lookup
The matching key to join on in one of the event datasets. If this list is empty, you probably haven’t added or configured an event or lookup dataset.
#### General dataset settings and details

Each (type of dataset) has the following common settings:

Setting
Description
Import new data
Enable this option if you want to establish an ongoing connection. With an ongoing connection new data batches that are added to the datasets are available automatically in Workspace.
Dataset backfill
Enable **Backfill all existing data** to ensure that all existing data is backfilled.Select **Request backfill** to backfill historical data for a specific period. You can define up to 10 dataset backfill periods.

- Define the period by entering start and end data or selecting dates using .
- Select **Queue backfill** to add the backfill to the list, or **Cancel** to cancel.

For each entry, select to edit the period, or select to delete the entry.On backfills:

- You can backfill each dataset individually.
- You prioritize new data added to a dataset in the connection, so this new data has the lowest latency.
- Any backfill (historical) data is imported at a slower rate. The amount of historical data influences the latency.
- The Analytics source connector imports up to 13 months of data (irrespective of size) for production sandboxes. The backfill in non-production sandboxes is limited to 3 months.
- For production sandboxes, if you have licensed the additional SKU that entitles you to import more than 13 months of historical backfill data, contact Adobe to request the extended backfill.

Batch status
Possible status indicators are:

- Success
- X backfill(s) processing
- Off

Dataset ID
This ID is automatically generated.
Description
The description given to this dataset when the dataset was created.
Number of records
The dataset’s size.
Schema
The schema based on which the dataset was created in Adobe Experience Platform.
Dataset
The name of the dataset.
Preview:
dataset name
Previews the dataset for first 10 rows and first 10 columns.
Remove
You can
delete a dataset
without deleting the whole connection. The deletion of a dataset from a connection reduces the costs involved in data ingestion and the cumbersome process of recreating the whole connection and associated data views.
### Re-ingest data

You sometimes require to re-ingest data from one or more datasets into a connection. For ad hoc or relational dataset you need to [delete and then add the dataset once again](#edit-a-dataset). For other datasets, you can update settings. To do so:

- For the dataset you want to re-ingest data for: Change any of the following: An identifier (Person ID, Account ID, or other ID) for an already ingested event dataset. A key, matching key, or matching key type (field or container) for an already ingested profile or lookup dataset. Alternatively, you can toggle Backfill all existing data backfill on the dataset. Apply the changes for the dataset.
- Save the connection. Data is re-ingested for the specific datasets.

### Delete a dataset

When you delete a dataset, you are notified about the implications of the deletion. Deletion of a dataset can impact all associated connections, data views and projects. Also, if you do delete the one and only event or summary dataset in your connection, you are prompted to add another event or summary dataset. You can only save a connection that contains at least one event or summary dataset.

### Past backfills

When you select **Past backfills** in the interface, a **Past backfills: Name of dataset** dialog shows the most recent backfills from the dataset.

## Connection preview preview

To preview the connection that you have created, select **Connection preview** in the Connection settings dialog.

This preview contains some columns listing the connection configuration. What column types are shown depends on your individual datasets.

## Connection map

To see a map of the relationships between the datasets that are part of your connection, select **Connection map** in the Connection settings dialog.

This map helps you to get a better understanding of how you have defined your connection. And how you have set up the relationship between your event, profile, lookup, and summary datasets, using containers and identifiers.

## Use numeric fields as lookup keys and lookup values numeric

This lookup functionality is useful if you want to add a numeric field such as a cost or margin to a string-based key field. It allows numeric values to be part of lookups, either as keys or as values. In your lookup schema, you might have numeric values tied to, for example, your product names, COGS, campaign marketing cost, or margins. Here is an example lookup schema in Adobe Experience Platform:

You now support bringing in these values as metrics or dimensions into Customer Journey Analytics reporting. When you set up your connection and pull in lookup datasets, you can edit the datasets to select the Key and Matching Key:

When you set up a data view based on this connection, you add the numeric values as components to the data view. Any project based on this data view can then report on these numeric values.

## Use Identity Map as a Person ID id-map

Customer Journey Analytics supports the ability to use the Identity Map for its Person ID. Identity Map is a map data structure that allows you to upload key value pairs. The keys are identity namespaces and the value is a structure that holds the identity value. The Identity Map exists on each row/event uploaded and is populated for each row accordingly.

The Identity Map is available for any dataset that uses a schema based on the [ExperienceEvent XDM](/en/docs/experience-platform/xdm/home) class. When you select such a dataset to be included in a Customer Journey Analytics Connection, you have the option of selecting either a field as the primary ID or the Identity Map:

If you select Identity Map, you get two additional configuration options:

Option
Description
Use primary identity namespace
This option instructs Customer Journey Analytics to find the identity in the Identity Map that is marked with a
primary=true
attribute and use that identity as the Person ID for that row. This identity is the primary key that is used in Experience Platform for partitioning. And this identity is also the prime candidate for usage as Customer Journey Analytics Person ID (depending on how the dataset is configured in a Customer Journey Analytics connection).
Namespace
(This option is only available if you do not use the Primary ID Namespace.) Identity namespaces are a component of the
Experience Platform Identity Service
. Namespaces serve as indicators of the context to which an identity relates. If you specify a namespace, Customer Journey Analytics searches each row’s Identity Map for this namespace key and use the identity under that namespace as the Person ID for that row. Since Customer Journey Analytics cannot do a full dataset scan of all rows to determine which namespaces are present, all possible namespaces are displayed in the drop-down menu. Know which namespaces are specified in the data; these namespaces are not auto-detected.
### Identity Map edge cases id-map-edge

This table shows the two configuration options when edge cases are present and how they are handled:

Option
No IDs are present in the Identity Map
Multiple IDs, none marked as primary
Multiple IDs are marked as primary
Single ID, marked as primary or not
Invalid namespace with an ID marked as primary
Use primary identity namespace checked
Customer Journey Analytics drops the row.
Customer Journey Analytics drops the row, as no primary ID is specified.
All IDs marked as primary, under all namespaces, are extracted into a list. They are then alphabetically sorted; with the new sorting, the first namespace with its first ID is used as the Person ID.
The single ID is used as the Person ID.
Even though the namespace may be invalid (not present in Adobe Experience Platform), Customer Journey Analytics uses the primary ID under that namespace as the Person ID.
Specific Identity Map namespace selected
Customer Journey Analytics drops the row.
All IDs under the selected namespace are extracted into a list and the first is used as the Person ID.
All IDs under the selected namespace are extracted into a list and the first is used as the Person ID.
All IDs under the selected namespace are extracted into a list and the first is used as the Person ID.
All IDs under the selected namespace are extracted into a list and the first is used as the Person ID. (Only a valid namespace can be selected at Connection creation time, so it is not possible for an invalid namespace/ID to be used as Person ID)
## Calculate the average number of daily events average-number

This calculation is done for every dataset in the connection.

- Go to Adobe Experience Platform Query Services and create a query. The query would look like this: code language-none Select AVG(A.total_events) from (Select DISTINCT COUNT (*) as total_events, date(TIMESTAMP) from analytics_demo_data GROUP BY 2 Having total_events>0) A; In this example, “analytics_demo_data” is the name of the dataset.
- To show all the datasets that exist in Adobe Experience Platform, perform the Show Tables query.

Related Articles
- [Data ingestion overview](/en/docs/analytics-platform/using/cja-data-ingestion/data-ingestion)
- [How to Leverage Event, Lookup, and Profile Datasets in Adobe Customer Journey Analytics](https://experienceleaguecommunities.adobe.com/adobe-analytics-3/how-to-leverage-event-lookup-and-profile-datasets-in-adobe-customer-journey-analytics-12699)

recommendation-more-help
