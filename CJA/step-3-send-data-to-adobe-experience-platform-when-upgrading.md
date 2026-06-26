---
title: "Step 3: Send data to Adobe Experience Platform when upgrading"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-send-to-platform"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:07:50.317399+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Step 3: Send data to Adobe Experience Platform when upgrading

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User
- Admin

Expand this section to see where the information on this page fits into the larger upgrade process. Make sure all previous upgrade steps are complete.
Before you continue with this section, first make sure you have completed all previous upgrade tasks.

The information on this page covers Step 3 of the upgrade process, as highlighted in the table below:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 layout-auto |  |
| --- | --- |
| Upgrade task | Details |
| **Step 1: Get started with the upgrade** | Learn the benefits of upgrading to Customer Journey Analytics and the basic upgrade process. |
| **Step 2: Choose the upgrade path** | Various methods are available for upgrading to Customer Journey Analytics. Choose the method that is best for your organization, depending on your organization’s current Adobe Analytics environment and long-term goals. |
| *Step 3: Send data to Adobe Experience Platform* | *The process for sending data to Adobe Experience Platform differs depending on the upgrade path that you chose in Step 2.* |
| **Step 4: Retain historical data** | Most organizations need to retain their historical Adobe Analytics data for a certain amount of time. Various options are available to accomplish this. |
| **Step 5: Perform additional implementation tasks** | At this point in the upgrade process, you need to perform various tasks before your Customer Journey Analytics environment is ready to use. These additional tasks apply to upgrades from Adobe Analytics as well as new Customer Journey Analytics implementations. These tasks include: Bringing other data into Experience Platform Creating connections between Platform datasets and Customer Journey Analytics Creating data views Porting the reporting API usage Accounting for Data Feeds and Data Warehouse Migrating projects and components Planning user onboarding For more information, see Customer Journey Analytics Getting Started . |

AVAILABILITY
The information on this page is being replaced with the following more comprehensive upgrade information:
- Recommended upgrade steps For detailed information, see Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

After you [choose the upgrade path](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-path) that is best for your organization, you can begin sending data to Adobe Experience Platform in order to make it available in Customer Journey Analytics.

The process for sending data to Experience Platform for each upgrade path is shown below. Follow the links in the table for detailed configuration information.

Upgrade path
Process for sending data to Platform
Additional information
New implementation of the Experience Platform Web SDK
- Create an XDM schema for your organization. Work with your data team to identify your organization’s ideal schema design for Customer Journey Analytics.
- Implement the Experience Platform Web SDK.
- Send data to Platform.

For detailed information about each of these steps, see [Ingest data via the Adobe Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk).

Because this is a new implementation of the Experience Platform Web SDK, schema mapping is not required because you must create the schema as one of the first steps during implementation.
Migrate your Adobe Analytics implementation to use the Web SDK
- Move your existing Adobe Analytics implementation to the Experience Platform Web SDK, then validate that everything is working in Adobe Analytics. For information about how to do this, use the following resources, depending on whether your current implementation is the Analytics tag extension or AppMeasurement: If you are using the Analytics tag extension, see Migrate from the Adobe Analytics tag extension to the Web SDK tag extension If you are using AppMeasurement, see Migrate from AppMeasurement to the Web SDK
- Create an XDM schema for your organization . Work with your data team to identify your organization’s ideal schema design for Customer Journey Analytics.
- Use Data Prep to map all of the fields in the data object to your XDM schema .
- Begin sending data to Platform by setting up a datastream .

Configure your existing Adobe Analytics Web SDK implementation to send data to Platform
- Begin sending data to Platform by setting up a datastream . Because your Adobe Analytics implementation is already using the Experience Platform Web SDK, you can ignore the other sections in Ingest data via the Adobe Experience Platform Web SDK . If you are already sending data to Platform with your Adobe Analytics implementation, this step is not required. You simply need to create a connection between Platform datasets and Customer Journey Analytics, as described later in this process.
- (Optional) Create an XDM schema for your organization . Work with your data team to identify your organization’s ideal schema design for Customer Journey Analytics. Note: For information about the advantages of creating an XDM schema, see Choose your schema .
- (Conditional) If you created an XDM schema, use Data Prep to map all of the fields in the data object to your XDM schema .

Use the Analytics source connector
Ingest and use data from traditional Adobe Analytics
Adobe Analytics data is automatically mapped to the XDM schema when you use the Analytics source connector. Additional mapping is not required.
## Next, retain historical data

Next, decide how you will [retain historical Adobe Analytics data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-historical-data).

recommendation-more-help
