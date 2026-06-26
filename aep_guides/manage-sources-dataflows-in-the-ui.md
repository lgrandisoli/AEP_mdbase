---
title: "Manage sources dataflows in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/manage"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:23:15.938618+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Manage sources dataflows in the UI

Last update: June 22, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

You can use the *Sources workspace* in the Adobe Experience Platform user interface to manage your existing source dataflows.

- Use the Dataflows page to access a centralized view of your organization’s existing dataflows and search, filter, organize, and take actions on individual flows.
- Use filtering and search capabilities to navigate through source accounts and dataflows in your organization
- Use inline actions to modify configuration settings applied to your dataflows, improve organizational workflows, and apply tags, subscribe to alerts, or create ingestion jobs on demand.

## Get started

Before you begin, ensure that you have the following:

- Access to Adobe Experience Platform.
- Both **View Sources** and **Manage Sources** permissions are required.

It is helpful to have an understanding of the following Experience Platform features and concepts before working with the object navigation tools in the Sources workspace:

- [Sources](/en/docs/experience-platform/sources/home): Learn how to connect, manage, and monitor external data sources in Experience Platform.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Discover how sandboxes let you develop and test different projects in isolated environments.
- [Administrative tags](/en/docs/experience-platform/administrative-tags/overview): Use administrative tags to apply metadata keywords to your objects and enable search to find that object within the Experience Platform ecosystem.
- [Datasets](/en/docs/experience-platform/catalog/datasets/user-guide): A dataset is a management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows).

## Access your source dataflows

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace, and then select **Dataflows** from the top header. The *Dataflows* page displays a list of existing dataflows in your organization. From this page, you can search for specific dataflows, apply filters to narrow results, organize dataflows with tags, inspect metadata in the table, and continue to related actions such as updating or deleting a dataflow.

## Search and filter dataflows

Use the Dataflows page to quickly locate a specific dataflow or narrow the results.

### Search for a dataflow

Use the search field on the **Dataflows** page to find a dataflow from the current inventory view. After you enter a search term, the table updates to show matching results.

### Filter your dataflows

Select the filter icon ( ) to refine the list of available dataflows. You can apply one or more filters to narrow the results based on the metadata associated with each dataflow.

Available filter categories include:

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
To filter your dataflows:

- Select the filter control to open the filter panel.
- Select one or more filter criteria.
- Review the updated results in the dataflows table.
- Clear individual filters or select Clear all to remove all filters and return to the full list.

Use filters to find dataflows by source platform, identify dataflows with a particular status, or narrow the table to dataflows associated with a specific dataset or account.

## Organize dataflows with tags

You can use tags to organize your dataflows and improve discoverability on the **Dataflows** page. Tags are especially useful when you want to group related dataflows and then use filters to find them again later

To organize a dataflow with tags:

- Locate the dataflow that you want to update.
- Select the ellipses (...) beside the dataflow name to open the action menu.
- Select the tag-related action.
- Add or remove tags as needed.
- Select **Done** to save your changes.
- Use the **Tags** filter to find similarly tagged dataflows.

Use tags to create an organizational layer for browsing and filtering workflows, and to manage a larger number of dataflows more efficiently.

## Resize table columns

You can resize table columns on the **Dataflows** page to display more metadata when values are truncated in the default table view. This is useful when you want to inspect longer values such as dataflow names, account details, or target dataset information.

To resize a column, hover over the edge of a column header and drag the boundary to adjust its width.

Resize columns as needed to make it easier to review dataflow details before you take action.

## Take action on a dataflow

After you locate the dataflow that you want to work with, select the ellipses (...) beside the dataflow name to view the available inline actions. Depending on the dataflow type and your permissions, available actions can include editing a schedule, disabling or deleting a dataflow, running a dataflow on demand, managing tags, and more.

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
- Sources Dataflow Run Failure: Select this alert to receive a notification when your on-demand dataflow run fails due to errors.

For more information, read the guide on [subscribing to alerts for sources dataflows](/en/docs/experience-platform/sources/ui-tutorials/alerts).

Add to package
Select
Add to package
to add your dataflow to a package and export it for use in a different sandbox. During this step, you can either create a new package or add your dataflow to an existing package. For more information, read the guide on
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
