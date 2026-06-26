---
title: "Step 4: Retain historical data when upgrading"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-historical-data"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:44:44.628629+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Step 4: Retain historical data when upgrading

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- Admin

Expand this section to see where the information on this page fits into the larger upgrade process. Make sure all previous upgrade steps are complete.
Before you continue with this section, first make sure you have completed all previous upgrade tasks.

The information on this page covers Step 4 of the upgrade process, as highlighted in the table below:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 layout-auto |  |
| --- | --- |
| Upgrade task | Details |
| **Step 1: Get started with the upgrade** | Learn the benefits of upgrading to Customer Journey Analytics and the basic upgrade process. |
| **Step 2: Choose the upgrade path** | Various methods are available for upgrading to Customer Journey Analytics. Choose the method that is best for your organization, depending on your organization’s current Adobe Analytics environment and long-term goals. |
| **Step 3: Send data to Adobe Experience Platform** | The process for sending data to Adobe Experience Platform differs depending on the upgrade path that you chose in Step 2. |
| *Step 4: Retain historical data* | *Most organizations need to retain their historical Adobe Analytics data for a certain amount of time. Various options are available to accomplish this.* |
| **Step 5: Perform additional implementation tasks** | At this point in the upgrade process, you need to perform various tasks before your Customer Journey Analytics environment is ready to use. These additional tasks apply to upgrades from Adobe Analytics as well as new Customer Journey Analytics implementations. These tasks include: Bringing other data into Experience Platform Creating connections between Platform datasets and Customer Journey Analytics Creating data views Porting the reporting API usage Accounting for Data Feeds and Data Warehouse Migrating projects and components Planning user onboarding For more information, see Customer Journey Analytics Getting Started . |

AVAILABILITY
The information on this page is being replaced with the following more comprehensive upgrade information:
- Recommended upgrade steps For detailed information, see Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

Choose one of the following options to retain historical data when moving from Adobe Analytics to Customer Journey Analytics:

IMPORTANT
When choosing how to retain historical data, contact your Adobe account representative to determine pricing.
## Use the Analytics source connector

You can use the [Analytics source connector](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/analytics) to retain historical data. Regardless of the upgrade path that you choose (even if you upgrade using the Web SDK), you can use the Analytics source connector to retain historical data from your Adobe Analytics environment.

You can use the Analytics source connector to retain historical data by bringing historical data into its own dedicated location, separate from your current data.

The Analytics source connector must be functioning for as long as you need access to the historical data.

## Maintain your existing Adobe Analytics implementation

You can maintain your existing Adobe Analytics implementation alongside your new Customer Journey Analytics implementation for a specific time frame (for example, 1 year). When choosing this option, consider the following:

- Data would not be available in Experience Platform.
- You should plan to decommission the Adobe Analytics implementation after you have sufficient data in Customer Journey Analytics.

## Next, perform additional implementation tasks

At this point in the upgrade process, you need to perform various implementation tasks before your Customer Journey Analytics environment is ready to use.

These additional tasks apply to upgrades from Adobe Analytics as well as new Customer Journey Analytics implementations.

These tasks include:

- Bringing other data into Experience Platform
- Creating connections between Platform datasets and Customer Journey Analytics
- Creating data views
- Porting the reporting API usage
- Accounting for Data Feeds and Data Warehouse use cases
- Migrating projects and components
- Planning user onboarding

For more information, begin with Step 2 in [Customer Journey Analytics Getting Started](/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/cja-getting-started).

recommendation-more-help
