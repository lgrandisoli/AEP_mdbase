---
title: "Datasets UI guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/user-guide"
category: "guides"
topic: "experience-platform/catalog-and-datasets-guide"
created_at: "2026-05-29T16:55:55.477114+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Catalog and Datasets Guide

# Datasets UI guide

Last update: May 13, 2026
- Topics:
- [Catalog](#)

CREATED FOR:

- Developer

This user guide provides instructions on performing common actions when working with datasets within Adobe Experience Platform user interface.

## Getting started

This user guide requires a working understanding of the following components of Adobe Experience Platform:

- Datasets : The storage and management construct for data persistence in Experience Platform.
- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor : Learn how to build your own custom XDM schemas using the Schema Editor within the Experience Platform user interface.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- Adobe Experience Platform Data Governance : Ensure compliancy with regulations, restrictions, and policies regarding the usage of customer data.

## View datasets view-datasets

In the Experience Platform UI, select **Datasets** in the left-navigation to open the **Datasets** dashboard. The dashboard lists all available datasets for your organization. Details are displayed for each listed dataset, including its name, the schema the dataset adheres to, and the status of the most recent ingestion run.

Select the name of a dataset from the Browse tab to access its **Dataset activity** screen and see details of the dataset you selected. The activity tab includes a graph visualizing the rate of messages being consumed as well as a list of successful and failed batches.

## More actions more-actions

You can Delete or Enable a dataset for Profile from the Dataset details view. To see the available actions, select **… More** in the top right of the UI. The drop-down menu appears.

If you select **Enable a dataset for Profile**, a confirmation dialog appears. Select **Enable** to confirm your choice.

NOTE
To enable a dataset for Profile, the schema that the dataset adheres to must be compatible for use in Real-Time Customer Profile. See the
Enable a dataset for profile
section for more information.
If you select **Delete**, the Delete dataset confirmation dialog appears. Select **Delete** to confirm your choice.

NOTE
You cannot delete system datasets.
You can also delete a dataset or add a dataset for use with Real-Time Customer Profile from the inline actions found on the Browse tab. See the [inline actions section](#inline-actions) for more information.

## Inline dataset actions inline-actions

The datasets UI now offers a collections of inline actions for each available dataset. Select the ellipsis (…) of a dataset that you want to manage to see the available options in a pop-up menu. The available actions include;

- [Preview dataset](#preview)
- [Manage data and access labels](#manage-and-enforce-data-governance)
- [Enable unified profile](#enable-profile)
- [Manage tags](#manage-tags)
- [Set data retention policy](#data-retention-policy)
- [Move to folders](#move-to-folders)
- [Delete](#delete).

More information on these available actions can be found in their respective sections. To learn how to manage large numbers of datasets simultaneously, refer to the [bulk actions](#bulk-actions) section.

### Preview a dataset preview

You can preview up to 100 rows of sample data for any dataset, either from the inline options in the Browse tab or from the Dataset activity view.

From the Browse tab, select the ellipsis (…) next to the dataset name and choose Preview dataset. If the dataset is empty, the preview option is deactivated. Alternatively, from the **Dataset activity** screen, select **Preview dataset** near the top-right corner of your screen.

This opens the preview window, where the hierarchical schema view for the dataset appears on the left.

NOTE
The schema diagram on the left only displays fields that contain data. Fields without data are automatically hidden to streamline the UI and focus on relevant information.
Alternatively, from the **Dataset activity** screen, select **Preview dataset** to open the preview window and review a sample of your dataset’s structure and values.

The dataset preview window provides a quick way to explore and validate your dataset’s structure and data.

#### Dataset preview window dataset-preview-window

The following animation shows the dataset preview window with its navigation and data exploration features:

The dataset preview window includes:

- An object browser sidebar on the left for navigating and filtering dataset fields.
- Data type indicators next to each column name for insight into the structure of the dataset.
- A SQL query display at the top of the window, showing the query used to generate the dataset.
- A formatted table view of up to 100 rows for efficient data review.

These features help you navigate, understand schema details, and validate sample data efficiently.

#### Advanced Query Editor shortcut query-editor-shortcut

If your organization has a Data Distiller license, you can access the Advanced Query Editor directly from the dataset preview window. Use this shortcut to move seamlessly from previewing sample data to running and refining queries in Query Service.

AVAILABILITY
Access to the Advanced Query Editor is limited to organizations with a Data Distiller SKU license. If your organization does not have the required license, this option does not appear in the dataset preview window.
Select Advanced Query Editor in the upper right of the preview window to open Query Service with your current SQL query pre-loaded and executed. You can continue analyzing or modify the SQL without re-entering the query.

For additional analysis, use downstream services such as Query Service and JupyterLab. See the following documents for more information:

- [Query Service overview](/en/docs/experience-platform/query/home)
- [JupyterLab user guide](/en/docs/experience-platform/data-science-workspace/jupyterlab/overview)

### Manage and enforce data governance on a dataset manage-and-enforce-data-governance

You can manage the data governance labels for a dataset by selecting the inline options of the Browse tab. Select the ellipses (…) next to the dataset name that you wish to manage, followed by **Manage data and access labels** from the dropdown menu.

Data usage labels, applied at the schema level, allow you to categorize datasets and fields according to usage policies that apply to that data. See the [Data Governance overview](/en/docs/experience-platform/data-governance/home) to learn more about labels, or refer to the [data usage labels user guide](/en/docs/experience-platform/data-governance/labels/overview) for instructions on how to apply labels to schemas for propagation to datasets.

## Enable a dataset for Real-Time Customer Profile enable-profile

Every dataset has the ability to enrich customer profiles with its ingested data. To do so, the schema that the dataset adheres to must be compatible for use in Real-Time Customer Profile. A compatible schema satisfies the following requirements:

- The schema has at least one attribute specified as an identity property.
- The schema has an identity property defined as the primary identity.

For more information on enabling a schema for Profile, see the [Schema Editor user guide](/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

You can enable a dataset for Profile from both the inline options of the Browse tab and also the Dataset activity view. From the Browse tab of the Datasets workspace, select the ellipsis of a dataset that you want to enable for Profile. A menu list of options appears. Next, select **Enable unified profile** from the list of available options.

Alternatively, from the dataset’s **Dataset activity** screen, select the **Profile** toggle within the **Properties** column. Once enabled, data that is ingested into the dataset will also be used to populate customer profiles.

NOTE
If a dataset already contains data and is then enabled for Profile, the existing data is not automatically consumed by Profile. After a dataset is enabled for Profile, it is recommended that you re-ingest any existing data to have it contribute to customer profiles.
Datasets that have been enabled for Profile can also be filtered on this criteria. See the section on how to [filter Profile enabled datasets](#filter-profile-enabled-datasets) for more information.

### Manage dataset tags manage-tags

Add custom created tags to organize datasets and improve search, filtering, and sorting capabilities. From the Browse tab of the Datasets workspace, select the ellipsis of a dataset that you want to manage followed by **Manage tags** from the dropdown menu.

The Manage tags dialog appears. Enter a short description to create a custom tag, or choose from a pre-existing tag to label your dataset. Select **Save** to confirm your settings.

The Manage tags dialog can also remove existing tags from a dataset. Simply select the ‘x’ next to the tag that you wish to remove and select **Save**.

Once a tag has been added to a dataset, the datasets can be filtered based on the corresponding tag. See the section on how to [filter datasets by tags](#enable-profile) for more information.

For more information on how to classify business objects for easier discovery and categorization, see the guide on [managing metadata taxonomies](/en/docs/experience-platform/administrative-tags/ui/managing-tags). This guide explains how users with the right permissions can create pre-defined tags, assign them to categories, and manage all related CRUD operations in the Experience Platform UI.

### Set data retention policy data-retention-policy

Manage dataset expiration and retention settings using the inline action menu from the Browse tab of the Datasets workspace. You can use this feature to configure how long data is retained in the data lake and Profile store. The expiration date is based on when data was ingested into Experience Platform and your configured retention period.

IMPORTANT
To apply or update retention rules for an ExperienceEvent dataset, your user role must include the
Manage datasets
permission. This role-based access control ensures that only authorized users can modify dataset retention settings.
See the
Access control overview
for more information on assigning permissions in Adobe Experience Platform.
TIP
The data lake stores raw, unprocessed data, such as event logs, clickstream data, and bulk-ingested records, for analytics and processing. The Profile store contains customer-identifiable data, including identity-stitched events and attribute information, to support real-time personalization and activation.
To configure your retention period, select the ellipsis next to the dataset followed by **Set data retention policy** from the dropdown menu.

The Set dataset retention dialog appears. The dialog displays sandbox-level license usage metrics, dataset-level details, and current data retention settings. These metrics show your usage compared to your entitlements and help you assess dataset-specific storage and retention configurations. The metrics include dataset name, type, Profile enablement status, and data lake and Profile store usage.

NOTE
Sandbox-level licensed data lake storage metrics are still in development and may not appear. A full breakdown of your license usage metrics can be found on the License Usage dashboard. See the documentation for descriptions of these metrics.
Configure your preferred retention period in the data retention settings dialog. Enter a number and select a time unit (days, months, or years) from the dropdown menu. You can configure separate retention settings for the data lake and Profile Service.

NOTE
The minimum retention period for the data lake is 30 days. The minimum retention period for Profile Service is one day.
Additionally, you can only update the retention period for Profile Service once every 30 days.
To support transparency and monitoring, timestamps are provided for the **last** and **next** data retention job executions. The timestamps help you understand when the last data cleanup occurred and when the next one is scheduled.

#### Storage impact insights storage-impact-insights

To open a visual forecast of the storage impact of different retention policies, select **View Experience Event Data distribution**.

The chart displays the distribution of experience events across various retention periods for the currently selected dataset. Hover over each bar to see the precise number of records that will be removed if the selected retention period is applied.

You can use the visual forecast to evaluate the impact of different retention periods and make informed business decisions. For example, if you select a 30-day retention period and the chart shows that 60% of your data will be deleted, you may choose to extend retention to preserve more data for analysis.

NOTE
The Experience Event distribution chart is specific to the selected dataset and reflects only its data. It applies exclusively to data stored in the data lake.
When you are satisfied with your configuration, select **Save** to confirm your settings.

IMPORTANT
Once data retention rules are applied, any data older than the number of days defined by the expiration value is permanently deleted and cannot be recovered.
After configuring your retention settings, use the Monitoring UI to confirm that your changes were executed by the system. The Monitoring UI provides a centralized view of data retention activity across all datasets. From there, you can track job execution, review how much data was deleted, and ensure that your retention policies are functioning as expected.

To explore how retention policies apply across different services, see the dedicated guides on [Experience Event Dataset Retention in Profile](/en/docs/experience-platform/profile/event-expirations) and [Experience Event Dataset Retention in the Data Lake](/en/docs/experience-platform/catalog/datasets/experience-event-dataset-retention-ttl-guide). This visibility supports governance, compliance, and efficient data lifecycle management.

To learn how to use the monitoring dashboard to track source dataflows in the Experience Platform UI, see the [Monitor dataflows for sources in the UI](/en/docs/experience-platform/dataflows/ui/monitor-sources) documentation.

For more information on the rules that define dataset expirations date ranges and best practices for configuring your data retention policy, see the [frequently asked questions page](/en/docs/experience-platform/catalog/catalog-faq).

#### Enhanced visibility of retention periods and storage metrics retention-and-storage-metrics

Four new columns provide greater visibility into your data management: **Data Lake Storage**, **Data Lake Retention**, **Profile Storage**, and **Profile Retention**. These metrics show how much storage your data consumes and its retention period in both data lake and Profile Service.

This increased visibility empowers you to make informed decisions and manage storage costs more effectively. Sort datasets by storage size to identify the largest ones in your current sandbox. These insights support data management best practices and help ensure compliance with your licensed entitlements.

The following table provides an overview of the new retention and storage metrics. It details each column’s purpose and how it supports managing data retention and storage.

Column title
Description
Data Lake Retention
The current retention period for each dataset in the data lake. This value is configurable and determines how long data is retained before deletion.
Data Lake Storage
The current storage usage for each dataset in the data lake. Use this metric to manage storage limits and optimize usage.
Profile Storage
The current storage usage for each dataset within the Profile Service. Helps monitor storage consumption and support data management decisions.
Profile Retention
The current retention period for Profile datasets. You can update this value to control how long Profile data is retained.
To act on the insights from storage and retention metrics, refer to the [data management license entitlement best practices guide](/en/docs/experience-platform/landing/license/data-management-best-practices). Use it to manage what data you ingest and retain, apply filters and expiration rules, and control data growth to stay within your licensed usage limits.

### Move to folders move-to-folders

You can place datasets within folders for better dataset management. To move a dataset into a folder, select the ellipses (…) next to the dataset name you wish to manage, followed by **Move to folder** from the dropdown menu.

The Move dataset to folder dialog appears. Select the folder you want to move the audience to, then select **Move**. A popup notification informs you that the dataset move has been successful.

TIP
You can also create folders directly from the Move dataset dialog. To create a folder, select the create folder icon (
) in the top right of the dialog.
Once the dataset is in a folder, you can choose to only display datasets that belong to a specific folder. To open your folder structure, select the show folders icon ( ). Next, select your chosen folder to see all associated datasets.

### Delete a dataset delete

You can delete a dataset from either the dataset inline actions in the Browse tab or the top right of the Dataset activity view. From the Browse view, select the ellipses (…) next to the dataset name you wish to delete. A menu list of options appears. Next, select **Delete** from the dropdown menu.

A confirmation dialog appears. Select **Delete** to confirm.

Alternatively, select **Delete dataset** from the **Dataset activity** screen.

NOTE
Datasets created and utilized by Adobe applications and services (such as Adobe Analytics, Adobe Audience Manager, or Offer Decisioning) cannot be deleted.
A confirmation box appears. Select **Delete** to confirm the deletion of the dataset.

### Delete a Profile-enabled dataset

If a dataset is enabled for Profile, deleting that dataset through the UI will delete it from the data lake, Identity Service, and also any profile data associated with that dataset in the Profile store.

You can delete profile data associated with a dataset from the Profile store (leaving the data in the data lake) using the Real-Time Customer Profile API. For more information, see the [profile system jobs API endpoint guide](/en/docs/experience-platform/profile/api/profile-system-jobs).

## Search and filter datasets search-and-filter

To search or filter the list of available datasets, select the filter icon ( ) at the top left of the workspace. A set of filter options in the left rail appears. There are several methods to filter your available datasets. These include: [Show System Datasets](#show-system-datasets), [Included in profile](#filter-profile-enabled-datasets), [Tags](#filter-by-tag), [Creation date](#filter-by-creation-date), [Modified date, Created by](#filter-by-creation-date), and [Schema](#filter-by-schema).

The list of applied filters is displayed above the filtered results.

### Show system datasets show-system-datasets

By default, only datasets that you have ingested data into are shown. If you want to see the system-generated datasets, select the **Yes** checkbox in the Show system datasets section. System-generated datasets are only used to process other components. For example, the system-generated profile export dataset is used to process the profile dashboard.

### Filter Profile enabled datasets filter-profile-enabled-datasets

The datasets that have been enabled for Profile data are used to populate customer profiles after data has been ingested. See the section on [enabling datasets for Profile](#enable-profile) to learn more.

To filter your dataset based on whether they have been enabled for Profile, select the Yes checkbox from the filter options.

### Filter datasets by tag filter-by-tag

Enter your custom tag name in the Tags input, then select your tag from the list of available options to search and filter datasets that correspond to that tag.

### Filter datasets by creation date filter-by-creation-date

Datasets can be filtered by creation date over a custom time period. This can be used to exclude historic data or to generate specific chronological data insights and reporting. Choose a Start date and an End date by selecting the calendar icon for each field. After which, only datasets that conform to that criteria will appear in the Browse tab.

### Filter datasets by modified date filter-by-modified-date

Similar to the filter for creation date, you can filter your datasets based on the date they were last modified. In the Modified date section, Choose a Start date and an End date by selecting the calendar icon for each field. After which, only datasets that were modified during that period will appear in the Browse tab.

### Filter by schema filter-by-schema

You can filter datasets based on the schema that defines their structure. Either select the dropdown icon or input the schema name into the text field. A list of potential matches appears. Select the appropriate schema from the list.

## Bulk actions bulk-actions

Use bulk actions to enhance your operational efficiency and perform multiple actions on numerous datasets simultaneously. You can save time and maintain an organized data structure with bulk actions such as [Move to folder](#move-to-folders), [Edit tags](#manage-tags), and [Delete](#delete) datasets.

To act on more than one dataset at a time, select individual datasets with the checkbox on each row, or select an entire page with the column header checkbox. Once selected, the bulk action bar appears.

When you apply bulk actions to datasets, the following conditions apply:

- You can select datasets from different pages of the UI.
- If you select a filter, the selected datasets will reset.

## Sort datasets by created date sort

Datasets in the Browse tab can be sorted by either ascending or descending dates. Select the Created or Last updated column headings to alternate between ascending and descending. Once selected, the column indicates this with either an up or down arrow to the side of the column header.

## Create a dataset create

To create a new dataset, start by selecting **Create dataset** in the **Datasets** dashboard.

In the next screen, you are presented with the following two options for creating a new dataset:

- [Create dataset from schema](#schema)
- [Create dataset from CSV file](#csv)

### Create a dataset with an existing schema schema

In the **Create dataset** screen, select **Create dataset from schema** to create a new empty dataset.

The **Select schema** step appears. Browse the schema listing and select the schema that the dataset will adhere to before selecting **Next**.

The **Configure dataset** step appears. Provide the dataset with a name and optional description, then select **Finish** to create the dataset.

Datasets can be filtered from the list of available datasets in the UI with the schema filter. See the section on how to [filter datasets by schema](#filter-by-schema) for more information.

### Create a dataset with a CSV file csv

When a dataset is created using a CSV file, an ad hoc schema is created to provide the dataset with a structure that matches the provided CSV file. In the **Create dataset** screen, select **Create dataset from CSV file**.

The **Configure** step appears. Provide the dataset with a name and optional description, then select **Next**.

The **Add data** step appears. Upload the CSV file by either dragging and dropping it onto the center of your screen, or select **Browse** to explore your file directory. The file can be up to ten gigabytes in size. Once the CSV file is uploaded, select **Save** to create the dataset.

NOTE
CSV column names must start with alphanumeric characters, and can contain only letters, numbers, and underscores.
## Monitor data ingestion

In the Experience Platform UI, select **Monitoring** in the left-navigation. The **Monitoring** dashboard lets you view the statuses of inbound data from either batch or streaming ingestion. To view the statuses of individual batches, select either **Batch end-to-end** or **Streaming end-to-end**. The dashboards list all batch or streaming ingestion runs, including those that are successful, failed, or still in progress. Each listing provides details of the batch, including the batch ID, the name of the target dataset, and the number of records ingested. If the target dataset is enabled for Profile, the number of ingested identity and profile records is also displayed.

You can select on an individual **Batch ID** to access the **Batch overview** dashboard and see details for the batch, including error logs should the batch fail to ingest.

If you wish to delete the batch, select **Delete batch** near the top right of the dashboard. Deleting a batch also removes its records from the dataset that the batch was originally ingested to.

NOTE
If the ingested data has been enabled for Profile and processed, then deleting a batch does not delete that data from the Profile store.
## Next steps

This user guide provided instructions for performing common actions when working with datasets in the Experience Platform user interface. For steps on performing common Experience Platform workflows involving datasets, please refer to the following tutorials:

- [Create a dataset using APIs](/en/docs/experience-platform/catalog/datasets/create)
- [Query dataset data using the Data Access API](/en/docs/experience-platform/data-access/home)
- [Configure a dataset for Real-Time Customer Profile and Identity Service using APIs](/en/docs/experience-platform/profile/tutorials/dataset-configuration)

recommendation-more-help
