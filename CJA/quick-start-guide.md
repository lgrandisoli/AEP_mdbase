---
title: "Quick start guide"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/cja-getting-started"
category: "other"
topic: "customer-journey-analytics/customer-journey-analytics-guide"
created_at: "2026-06-02T18:51:23.316802+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Quick start guide

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User

To implement Customer Journey Analytics, you need to follow this workflow. Some initial tasks are performed in Adobe Experience Platform, and some in Customer Journey Analytics.

## Prerequisites

Customer Journey Analytics is available for customers who

- Are provisioned for the [Adobe Experience Platform](https://www.adobe.com/experience-platform.html), and
- Have purchased the Customer Journey Analytics SKU

## Workflow

Task
Details
Step 1: If you are upgrading from Adobe Analytics to Customer Journey Analytics: Choose an upgrade path and send data to Adobe Experience Platform
There are various paths available when upgrading from Adobe Analytics to Customer Journey Analytics. Each possible upgrade path has its own advantages and disadvantages, and a path that is right for one organization might not make sense for another.

To begin upgrading from Adobe Analytics to Customer Journey Analytics, do either of the following:

- Follow the upgrade path recommended by Adobe. For more information, see [Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations).
- Learn about all available upgrade paths and choose the path that best suits your organization. For more information, see [Get started with the upgrade to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-getstarted).

Step 2: Get other data into Adobe Experience Platform
This step, performed in Adobe Experience Platform, involves several sub steps:

- **Step 2a: Prepare your data schema**: Use [Adobe Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home) to standardize customer experience data and [define schemas](/en/docs/experience-platform/xdm/tutorials/create-schema-ui) for customer experience management.
- **Step 2b: Create a dataset based on the schema**: Data in Platform consists of datasets, such as email datasets, CRM datasets, POS datasets, the Adobe Analytics dataset, etc… Each dataset consists of a schema and batches of data. You can [create a dataset in Experience Platform](/en/docs/platform-learn/getting-started-for-data-architects-and-data-engineers/create-datasets).
- **Step 2c: Ingest data into Experience Platform**: Here, you have several options.

Step 3: Create connections between platform datasets and Customer Journey Analytics
A connection lets you integrate datasets from Adobe Experience Platform into Workspace. In order to report on Experience Platform datasets, you first have to establish a connection between datasets in Experience Platform and Workspace.
See
Create or edit a connection
.
Step 4: Create data views
A data view is a “filtered” view of the data. You can create different data views for the same connection, with different settings for visit timeout, attribution, etc… You can create multiple data views for a single dataset.
See
Create a data view
.
Step 5: Port the reporting API usage
Applies only when migrating from Adobe Analytics
The Customer Journey Analytics reporting API is in the same format, but uses a different endpoint. Port the reporting API usage from the Adobe Analytics reporting API to the Customer Journey Analytics reporting API.
Step 6: Account for Data Feeds and Data Warehouse use cases
Applies only when migrating from Adobe Analytics
Decide how you will use the export options that are available in Customer Journey Analytics in order to best replicate the Data Feeds and Data Warehouse features you were using in Adobe Analytics.
link to docs Rob is creating
Step 7: Migrate projects and components
Applies only when migrating from Adobe Analytics
The Component migration area in Adobe Analytics allows you to migrate projects and their associated components from Adobe Analytics to Customer Journey Analytics.

The migration process includes:

- Re-creating Adobe Analytics projects in Customer Journey Analytics.
- Mapping dimensions and metrics from Adobe Analytics report suites to dimensions and metrics in Customer Journey Analytics data views.

Before you begin the migration, first [Prepare to migrate components and projects from Adobe Analytics to Customer Journey Analytics](/en/docs/analytics/admin/admin-tools/component-migration/prepare-component-migration).

After you make all of the needed preparations, you can [Migrate components and projects from Adobe Analytics to Customer Journey Analytics](/en/docs/analytics/admin/admin-tools/component-migration/component-migration).

Step 8: Plan user onboarding
Like in Adobe Analytics, Analysis Workspace is the main user-facing tool in Customer Journey Analytics. However, there are some key differences when using Analysis Workspace in Customer Journey Analytics that users need to be aware of.

You should give your users ample time (3 - 6 months) to become familiar with the key differences of Analysis Workspace in Customer Journey Analytics.

For information about some of the key differences between Adobe Analytics and Customer Journey Analytics, see [User Guide for Adobe Analytics users](/en/docs/analytics-platform/using/compare-aa-cja/aa-to-cja-user).

Step 9: Report on your cross-channel data in Workspace
After you have created connections and data views, analyze the data you have brought in using the power and flexibility of Analysis Workspace.
See
Perform basic analysis
and
Perform advanced analysis
.
## Quick start guides

The [Data ingestion](/en/docs/analytics-platform/using/cja-data-ingestion/data-ingestion) section provides quick start guides on the workflow above. These quick start guides illustrate how to ingest data from a variety of sources (including Adobe Analytics) in Adobe Experience Platform and then use that data in Customer Journey Analytics.

recommendation-more-help
