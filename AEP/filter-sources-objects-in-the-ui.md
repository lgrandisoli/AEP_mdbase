---
title: "Filter sources objects in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/filter"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:07:56.910866+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Filter sources objects in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Use the filtering, search, and inline action tools in the Adobe Experience Platform user interface to streamline your workflow in the Sources workspace

- Use filtering and search capabilities to navigate your way through sources accounts and dataflows in your organization.
- Use inline actions to modify configuration settings applied to your dataflows and improve organizational workflows. You can use inline actions to apply tags, set up alerts, or create ingestion jobs on demand.

## Get started

It is helpful to have an understanding of the following Experience Platform features and concepts before working with the object navigation tools in the sources workspace:

- [Sources](/en/docs/experience-platform/sources/home): Use sources in Experience Platform to ingest data from an Adobe Application or a third-party data source.
- [Administrative Tags](/en/docs/experience-platform/administrative-tags/overview): Use administrative tags to apply metadata keywords to your objects and enable search to find that object within the Experience Platform ecosystem.
- [Alerts](/en/docs/experience-platform/observability/home): Use alerts to receive notifications that provide an update on the status of objects such as your sources dataflows.
- [Dataflows](/en/docs/experience-platform/dataflows/home): Dataflows are representations of data jobs that move data across Experience Platform. You can use the sources workspace to create dataflows that ingest data from a given source to Experience Platform.
- [Datasets](/en/docs/experience-platform/catalog/datasets/user-guide): A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows).
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Use sandboxes in Experience Platform to create virtual partitions between your Experience Platform instances and create environments dedicated to development or production.

## Filter sources dataflows filter-sources-dataflows

In the Experience Platform UI, select **Sources** in the left navigation and then select **Dataflows** from the top header.

By default, the filter menu is displayed on the left of the interface. To hide the menu, select **Hide filters**.

You can filter your sources dataflows by the following parameters:

Filter
Description
Source platform
Filter your dataflows based on the source that they were created with.
Tags
Filter your dataflows based on the tags applied to them.
Status
Filter your dataflows based on their current status.
Target dataset
Filter your dataflows based on the target dataset they were created with.
Account name
Filter your dataflows based on the name of the account that they correspond with.
Created by
Filter your dataflows based on who created them.
Creation date
Filter your dataflows based on the date they were created.
Modified date
Filter your dataflows based on the date they were last updated.
### Filter dataflows by source platform filter-dataflows-by-source-platform

Use the Source platform panel to filter your dataflows by type of source. You can either type in a particular source or use the dropdown menu to see a list of sources in the catalog. You can also filter for several different sources for a given query. For example, you can select Amazon S3, Azure Data Lake Storage Gen2, and Google Cloud Storage to update the catalog and display only the dataflows that were created with the selected sources.

### Filter dataflows by tags filter-dataflows-by-tags

Use the tags panel to filter your dataflows by their respective tags.

Select **Has any tag** and then select the tags that you want to filter by using the dropdown menu. Use this setting to filter for dataflows that have any of the tags that you selected.

Select **Has all tags** and then select the tags that you want to filter by using the dropdown menu. Usee this setting to filter for dataflows that have all of the tags that you selected.

### Filter dataflows by status filter-dataflows-by-status

You can filter by status using the Status panel.

Status
Description
Enabled
Select
Enabled
to filter your view and display only active dataflows.
Disabled
Select
Disabled
to filter your view and display only deactivated dataflows.
Draft
Select
Draft
to filter your view and display only dataflows that are in draft mode.
### Filter dataflows by target dataset filter-dataflows-by-target-dataset

Select **Target dataset** to access a dropdown menu of all target datasets. Then, select a target dataset to filter your view and display only the dataflows that were created using your specified target datasets.

### Filter dataflows by account name filter-dataflows-by-account-name

Select **Account name** to access a dropdown menu of all accounts. Then, select an account to filter your view and display dataflows created by your selected account.

### Filter dataflows by user filter-dataflows-by-user

Use the Created by panel to filter dataflows by the user who created or last updated the dataflows. Select the dropdown and then select the username to filter your dataflows by.

### Filter dataflows by creation date filter-dataflows-by-creation-date

You can filter your dataflows by their creation dates. In the Created date panel, configure a start date and end date to create a time frame window and filter your view to display only dataflows created within that window.

You can configure your time frame by inputting your start and end date. Alternatively, select the calendar icon and use the calendar to configure your dates.

You can also follow the same steps, but filter dataflows by their last modification date, as opposed to their creation date.

### Filter dataflows by modification date filter-dataflows-by-modification-date

Similarly, you can apply the same principles and filter your dataflow by their dates of modification. Use the **Modified date** to configure a particular time frame and filter your view to display only dataflows that have been modified during that period.

### Combine filters combine-filters

You can combine different filters to widen or narrow down your search. In the example below, a filter is applied to search for:

- Dataflows that were created using the Amazon S3 source.
- Dataflows that contain the **ACME** tag.
- Datalfows that are currently enabled.
- Dataflows that were created using the Loyalty Dataset B2C dataset.
- Dataflows that were created between 4/1/2024 and 4/19/2024.

To remove all filters, select **Clear all**.

## Filter sources accounts filter-sources-accounts

In the Experience Platform UI, select Sources in the left navigation and then select **Accounts** from the top header. You can filter your sources accounts based on the source that they were created with or the user that created them.

## Search for accounts and dataflows search-for-accounts-and-dataflows

You can accelerate efficiency by using the search bar to immediately navigate to a particular account or dataflow.

Search for dataflows
Use the search bar in the Dataflows page to find a specific dataflow. You can search for a dataflow using its name or description.

Search for accounts
Use the search bar in the Accounts page to find a specific account. You can search for an account using its name or description.

## Inline actions for sources dataflows inline-actions-for-sources-dataflows

Select the ellipses (...) beside a dataflow name for a list of inline actions that you can use to make modifications to your dataflow.

Inline actions
Description
Edit schedule
Select
Edit schedule
to update the ingestion schedule of your dataflow. A dataflow that has been set to one-time ingestion cannot be edited.
Disable dataflow
Select
Disable dataflow
to deactivate a dataflow run. This option does not delete your dataflow.
View in monitoring
Select
View in monitoring
to view the metrics and status of your dataflow in the monitoring dashboard. For more information, read the guide on
monitoring sources dataflows
.
Delete
Select
Delete
to delete your dataflow.
Run on-demand
Select
Run on-demand
to trigger a single iteration of a dataflow run. For more information, read the guide on
creating an on-demand dataflow run
.
Subscribe to alerts
Select **Subscribe to alerts** to view a pop-up window of alerts that you can subscribe to:

- Sources Dataflow Run Start: Select this alert to receive a notification when your on-demand dataflow run begins.
- Sources Dataflow Run Success: Select this alert to receive a notification when your on-demand dataflow run finishes successfully.
- Sources Dataflow Run Failure: Select this alert when your on-demand dataflow run fails due to errors.

For more information, read the guide on [subscribing to alerts for sources dataflows](/en/docs/experience-platform/sources/ui-tutorials/alerts).

Add to package
Select
Add to package
to add your dataflow to a package and export it for use in a different sandbox. During this step, you can either create a new package or add your dataflow to an existing package. For information, read the guide on
sandbox tooling
.
Manage tags
Select
Manage tags
to add or remove tags from your dataflow. Use tags to manage metadata taxonomies and classify business objects for easier discovery and categorization. For more information, read the guide on
managing tags
.
## Next steps

By reading this document, you have learned how to navigate your way through the sources accounts and dataflows pages. For more information on sources, read the [sources overview](/en/docs/experience-platform/sources/home).

recommendation-more-help
