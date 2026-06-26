---
title: "Step 2: Choose your upgrade path"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-path"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:07:49.355162+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Step 2: Choose your upgrade path

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

Expand this section to see where the information on this page fits into the larger upgrade process. Make sure that all previous upgrade steps are complete.
Before you continue with this section, first make sure you have completed all previous upgrade tasks.

The information on this page covers Step 2 of the upgrade process, as highlighted in the table below:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 layout-auto |  |
| --- | --- |
| Upgrade task | Details |
| **Step 1: Get started with upgrade** | Learn the benefits of upgrading to Customer Journey Analytics and the basic upgrade process. |
| *Step 2: Choose the upgrade path* | *Various methods are available for upgrading to Customer Journey Analytics. Choose the method that is best for your organization, depending on your organization’s current Adobe Analytics environment and long-term goals.* |
| **Step 3: Send data to Adobe Experience Platform** | The process for sending data to Adobe Experience Platform differs depending on the upgrade path that you chose in Step 2. |
| **Step 4: Retain historical data** | Most organizations need to retain their historical Adobe Analytics data for a certain amount of time. Various options are available to accomplish this. |
| **Step 5: Perform additional implementation tasks** | At this point in the upgrade process, you need to perform various tasks before your Customer Journey Analytics environment is ready to use. These additional tasks apply to upgrades from Adobe Analytics as well as new Customer Journey Analytics implementations. These tasks include: Bringing other data into Experience Platform Creating connections between Platform datasets and Customer Journey Analytics Creating data views Porting the reporting API usage Accounting for Data Feeds and Data Warehouse Migrating projects and components Planning user onboarding For more information, see Customer Journey Analytics Getting Started . |

AVAILABILITY
The information on this page is being replaced with the following more comprehensive upgrade information:
- Recommended upgrade steps For detailed information, see Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

After you decide to upgrade to Customer Journey Analytics, you need to determine the optimal upgrade path for your organization.

The path that you choose for upgrading from Adobe Analytics to Customer Journey Analytics depends on the following factors:

- Your existing Adobe Analytics implementation
- Your goals for the future

Use the information on this page to determine which Customer Journey Analytics upgrade path best aligns with your organization’s current implementation and future goals.

To determine the optimal upgrade path for your organization, the following sections should be read sequentially:

- First, understand the upgrade paths that are available .
- Then, assess which upgrade paths are available to you .
- And finally, weigh the advantages and disadvantages of each upgrade path .

## Understand upgrade paths

Various upgrade paths exist for upgrading from Adobe Analytics to Customer Journey Analytics.

In general, each upgrade path differs in the level of effort required to execute the upgrade, as well as in the long-term viability achieved after the upgrade completes.

The following table lists each upgrade path, its level of effort, and its long-term viability:

Upgrade path
Level of effort
Long-term viability
**New implementation of the Experience Platform Web SDK with the Analytics source connector**You can begin using Customer Journey Analytics by doing a new implementation of the Experience Platform Web SDK. This allows you to begin sending data to Adobe Experience Platform Edge Network and Customer Journey Analytics. In addition, you use the Analytics source connector to bring historical data into Customer Journey Analytics.

For organizations not yet on the Web SDK, this upgrade path is perhaps the most straightforward in getting data to Edge Network because it requires the fewest number of steps; however, because all of the work is done up front (such as creating the XDM schema), it requires a larger initial effort.

The basic steps are:

- Create an XDM schema for your organization.
- Implement the Web SDK.
- Send data to Platform.
- Set up the Analytics source connector.The Analytics source connector is used to bring historical Adobe Analytics data into Customer Journey Analytics.

**Note:** This is the recommended upgrade path when upgrading to Customer Journey Analytics. For more information about this recommended upgrade path, see [Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics](/help/getting-started/cja-upgrade/cja-upgrade-recommendations.md).
High
High
**New implementation of the Experience Platform Web SDK**You can begin using Customer Journey Analytics by doing a new implementation of the Experience Platform Web SDK. This allows you to begin sending data to Adobe Experience Platform Edge Network and Customer Journey Analytics.

For organizations not yet on the Web SDK, this upgrade path is perhaps the most straightforward in getting data to Edge Network because it requires the fewest number of steps; however, because all of the work is done up front (such as creating the XDM schema), it requires a larger initial effort.

The basic steps are:

- Create an XDM schema for your organization.
- Implement the Web SDK.
- Send data to Platform.

High
High
**Migrate your Adobe Analytics implementation to use the Web SDK**If your Adobe Analytics implementation is AppMeasurement or the Analytics extension, you can migrate it to use the Adobe Experience Platform Web SDK to begin sending data to Edge Network and Adobe Analytics, prior to sending it to Customer Journey Analytics.

For organizations not yet on the Web SDK, this is the easiest and smoothest way to get data to Edge Network; it requires more steps, but offers a more methodical transition from Adobe Analytics to Customer Journey Analytics, with more tangible milestones.

The basic steps are:

- Move your existing Adobe Analytics implementation to the Web SDK and validate that everything is working in Adobe Analytics.
- Create an XDM schema for your organization as you have time.
- Use Datastream mapping to map all of the fields in the data object to your XDM schema.
- Send data to Platform.

Moderate
High
**Configure your existing Adobe Analytics Web SDK implementation**If your Adobe Analytics implementation is already using the Adobe Experience Platform Web SDK, you can begin sending data to Platform by setting up a datastream. Or, if you are already sending data to Platform, you simply need to create a connection between Platform datasets and Customer Journey Analytics.

Before you send data to Platform for use in Customer Journey Analytics, consider updating your Adobe Analytics schema for the specific needs of your organization and any other Platform applications you use.

The basic steps are:

- Begin sending data to Platform. If you are already sending data to Platform with your Adobe Analytics implementation, this step is not required. You simply need to create a connection between Platform datasets and Customer Journey Analytics, as described later in this process.
- (Optional) Create an XDM schema for your organization as you have time.
- (Conditional) If you created an XDM schema, use datastream mapping to map all of the fields in the data object to your XDM schema.

Low
High
**Use the Analytics Source Connector**If your Adobe Analytics implementation is AppMeasurement or the Analytics extension, you can begin sending data to a data view in Customer Journey Analytics.

This is the easiest way to get data to Customer Journey Analytics, but is the least viable method in the long term.

**Note:** This upgrade path can be used independently. However, for best results, we recommended using this upgrade path in conjunction with a new implementation of the Experience Platform WebSDK. For more information about this recommended upgrade path, see [Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics](/help/getting-started/cja-upgrade/cja-upgrade-recommendations.md).

Low
Low
Use the following diagram to help visualize where each upgrade path falls on the spectrum in terms of level of effort and long-term viability:

## Assess the upgrade paths available to you based on your current Adobe Analytics implementation

Not all upgrade paths are available for each type of Adobe Analytics implementation.

Use the information below to help you understand which upgrade path is most appropriate for your organization.

Contact your Adobe representative if you need more specific advice, guidance, or support.

Existing Adobe Analytics implementation
Available upgrade paths
AppMeasurement
- New implementation of the Experience Platform Web SDK
- Migrate Adobe Analytics to the Web SDK
- Analytics Source Connector
- (Recommended) New implementation of the Experience Platform Web SDK with the Analytics Source Connector

Adobe Analytics extension
- New implementation of the Experience Platform Web SDK
- Migrate Adobe Analytics to the Web SDK
- Analytics Source Connector
- (Recommended) New implementation of the Experience Platform Web SDK with the Analytics Source Connector

Web SDK
- Configure the Adobe Analytics Web SDK implementation to send data to Platform
- (Recommended) New implementation of the Experience Platform Web SDK with the Analytics Source Connector

## Weigh the advantages and disadvantages of the upgrade paths available to you

The advantages and disadvantages of a given upgrade path differ depending on your existing Adobe Analytics implementation.

Before you use the information below to determine which upgrade path is right for you, review the information in [Understand upgrade paths](#understand-migration-methods) if you haven’t already.

NOTE
While each of the upgrade paths described in the following sections can be used independently, Adobe recommends a two-pronged upgrade approach when upgrading from Adobe Analytics to Customer Journey Analytics, regardless of your current Adobe Analytics implementation:
the Adobe Analytics source connector
and a
new implementation of the Experience Platform WebSDK
.
### For Adobe Analytics implementations using: AppMeasurement and Adobe Analytics extension

Following are the upgrade paths available for organizations who have implemented Adobe Analytics with AppMeasurement or the Adobe Analytics extension. Expand each section to view the advantages and disadvantages of each upgrade path.

#### Upgrade paths

New implementation of the Experience Platform Web SDK
| table 0-row-2 1-row-2 layout-auto |  |
| --- | --- |
| Advantages | Disadvantages |
| Provides all the advantages of hosting data in Experience Edge Network : These advantages include: Highly performant reporting and data availability because Adobe Experience Platform is built to power real-time personalization use cases Consolidate implementation for Adobe CX Enterprise data collection between other CX Enterprise products (AJO, RTCDP, and so forth) Not reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth) Future-proof : Future implementation updates are easier. | Requires a new implementation from scratch : The requirement to do a new implementation from scratch means the following disadvantages: Time consuming : This is the most time-consuming and demanding upgrade path because it requires that you start over with a new implementation. Must re-create the full schema in XDM : Before you can start implementing the Web SDK, you have to re-create the full schema in XDM. Must re-create rules and data elements : Before you can start implementing the Web SDK, you have to re-create any rule conditions and data elements from your Adobe Analytics implementation. Does not account for retaining historical data: Adobe recommends using the Analytics source connector in conjunction with a new implementation of the Experience Platform Web SDK in order to retain historical data after upgrading to Customer Journey Analytics. Does not account for comparing data from your original implementation with that of your new implementation: Adobe recommends using the Analytics source connector in conjunction with a new implementation of the Experience Platform Web SDK in order to compare data after upgrading to Customer Journey Analytics. |

Migrate Adobe Analytics to the Experience Platform Web SDK
| table 0-row-2 1-row-2 layout-auto |  |
| --- | --- |
| Advantages | Disadvantages |
| Provides all the advantages of hosting data in Experience Edge Network : These advantages include: Highly performant reporting and data availability because Adobe Experience Platform is built to power real-time personalization use cases Consolidate implementation for Adobe CX Enterprise data collection between other CX Enterprise products (AJO, RTCDP, and so forth) Not reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth) Uses your existing implementation : While this approach requires some implementation changes, it does not require a completely new implementation from scratch. You can use your existing data layer and code with minimal changes to implementation logic without impacting your existing Adobe Analytics reporting. Provides flexibility to create an XDM schema for your organization at a later time : You can migrate your existing Adobe Analytics implementation to use the Web SDK and validate that everything is working in Adobe Analytics, then create the XDM schema. This flexibility allows for a more methodical and thoughtful upgrade to Customer Journey Analytics. | Requires mapping to send data to Platform : When your organization is ready to use Customer Journey Analytics, you must send data to a data set in Adobe Experience Platform. This action requires that every field in the data object be an entry in the datastream mapping tool that assigns it to an XDM schema field. Mapping only needs to be done once for this workflow, and it doesn’t involve making implementation changes. However, it is an extra step that is not required when sending data in an XDM object. Technical debt : Because this approach uses a modified form of your existing implementation, it can be harder to track implementation logic and perform changes in the future when needed. |

Use the Analytics Source Connector
| table 0-row-2 1-row-2 layout-auto |  |
| --- | --- |
| Advantages | Disadvantages |
| Least time-consuming and demanding upgrade path. Data is migrated to Customer Journey Analytics quickly with minimal investment | Data is not sent to Edge Network : This results in the following disadvantages: Highest level of latency in reporting across all upgrade paths; not optimized for real-time personalization use cases. Data cannot be shared with other Adobe Experience Platform applications; it is constrained to Customer Journey Analytics only Reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth) Difficult to move to the Web SDK in the future : Eventually, you will likely want access to the advantages provided by the Experience Platform Web SDK. In order to start using the Experience Platform Web SDK, you must do a new implementation. Uses the Analytics Experience Event field group in your schema : This field group adds many Adobe Analytics events that are not needed in your Customer Journey Analytics schema. This can lead to a more cluttered, complex schema than what is otherwise needed for Customer Journey Analytics. Because of these disadvantages, Adobe recommends using the Analytics source connector in conjunction with a new implementation of the Experience Platform Web SDK. |

### For Adobe Analytics implementations using: Web SDK

The following upgrade path is available for organizations who have implemented Adobe Analytics with the Experience Platform Web SDK.

When choosing this upgrade path, you also need to choose your schema.

#### Upgrade path

Configure the Adobe Analytics Web SDK implementation to send data to Platform
| table 0-row-2 1-row-2 layout-auto |  |
| --- | --- |
| Advantages | Disadvantages |
| This is the preferred upgrade path if your Adobe Analytics implementation is already using the Web SDK. Provides all the advantages of hosting data in Experience Edge Network : These advantages include: Highly performant reporting and data availability because Adobe Experience Platform is built to power real-time personalization use cases Consolidate implementation for Adobe CX Enterprise data collection between other CX Enterprise products (AJO, RTCDP, and so forth) Not reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth) Uses your existing implementation : While this approach requires some implementation changes, it does not require a completely new implementation from scratch. You can use your existing data layer and code with minimal changes to implementation logic without impacting your existing Adobe Analytics reporting. Provides an option to use an XDM schema : You can choose to use your existing Adobe Analytics schema or create an XDM schema and map fields in the data object to your XDM schema. XDM schemas are a flexible schema to define any fields you need, and only those fields that are relevant. See “Using your own XDM schema” below for more information about the advantages of using your own XDM schema. Retains rules and data elements : While it does require new rule actions, you can reuse your existing data elements and rule conditions with minimal changes. Future-proof : If you choose to use your own XDM schema, then future implementation updates are easier. | None |

#### Choose your schema

If you chose the upgrade path that allows you to configure the Adobe Analytics Web SDK implementation to send data to Platform, you can choose the schema that you want to use.

You can choose whether to use your existing Adobe Analytics schema, or you can update to your own XDM schema to better align with the needs of your organization as you begin to use other Platform services.

Use the Adobe Analytics schema with the Adobe Analytics Web SDK implementation
| table 0-row-2 1-row-2 |  |
| --- | --- |
| Advantages | Disadvantages |
| Advantages of using the Adobe Analytics schema include: Ease of upgrade If you are already sending data to Adobe Analytics with the Adobe Experience Platform Web SDK, you can add an additional service to your datastream to send data to Adobe Experience Platform (which then can be used in your Customer Journey Analytics configuration). | Disadvantages of using the Adobe Analytics schema include: While using the Adobe Analytics schema doesn’t limit you in terms of how it can be used with other Platform applications, it does result in a schema that is more complex than it otherwise could be. This is because the Adobe Analytics schema contains many objects that are specific to Adobe Analytics that are unlikely to be used by your organization. When changes to the schema are required, you have to sift through thousands of unused fields to find the field that requires updating. |

Use your own XDM schema with the Adobe Analytics Web SDK implementation
| table 0-row-2 1-row-2 |  |
| --- | --- |
| Advantages | Disadvantages |
| Advantages of updating to your own XDM schema include: A streamlined schema that is tailored to the needs of your organization and the specific Platform applications that you use. When changes to the schema are required, you don’t have to sift through thousands of unused fields to find the field that requires updating. | Disadvantages of updating to your own XDM schema include: Updating your schema is a time-consuming process that is required before you begin sending data to Platform. |

## Next, send data to Adobe Experience Platform

After you use the information above to choose a upgrade path, learn how to [send data to Adobe Experience Platform](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-send-to-platform) depending on the upgrade path that you chose.

recommendation-more-help
