---
title: "Step 1: Get started with the upgrade to Customer Journey Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-getstarted"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:42:25.710261+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Step 1: Get started with the upgrade to Customer Journey Analytics

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- Admin

AVAILABILITY
The information on this page is being replaced with the following more comprehensive upgrade information:
- Recommended upgrade steps For detailed information, see Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

Customer Journey Analytics is the next generation of analytics. It allows multi-channel data collection (both online and offline data), combined with powerful report-time processing functionality (through the definition of components and derived fields in data views).

Before you begin the process of upgrading from Adobe Analytics to Customer Journey Analytics, you should understand the benefits of Customer Journey Analytics, as well as the steps required to successfully upgrade.

## Understand the benefits of Customer Journey Analytics

Following are some of the key benefits: (For a comprehensive list, as well as more information about each of these key features, see [Features available only in Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/cja-aa#adobe-customer-journey-analytics-features-not-available-in-adobe-analytics).)

- Multi-channel reporting Customer Journey Analytics is combined with Experience Platform’s ability to hold all kinds of data schemas and types. Collect and report on data from multiple channels, such as digital (Web), Point-of-Sale systems, mobile, CRM systems, and more.
- Report-time transformations in data views Data views in Customer Journey Analytics allow you to further interpret data from a connection. You can alter or remove data without changing your implementation, use substrings to manipulate dimensions, create metrics from any value, segment subevents, or use derived fields. All of these transformations are non-destructive.
- Transformations apply to historical and new data Data View manipulation can be applied to both historical and new data in a non-destructive manner.
- Derived fields Derived fields allow for report-time transformations to your data. Data can be combined, corrected, or created on the fly and applies retroactively to all reporting.
- Data views replace virtual report suites Data views take the concept of virtual report suites as they exist today and expand it to enable additional controls on the data made available by connections. These changes make general settings like timezone and session time-out intervals configurable and retroactive.
- Unlimited customer dimensions and metrics Values can be numeric, text, objects, lists, or mixtures of all. Dimensions can be nested or hierarchical.

## Understand the upgrade process

The information on this page covers Step 1 of the upgrade process, as highlighted in the table below. Complete all steps in this table to upgrade from Adobe Analytics to Customer Journey Analytics.

Upgrade task
Details
Step 1: Get started with the upgrade
Learn the benefits of upgrading to Customer Journey Analytics and the basic upgrade process.
Step 2:
Choose the upgrade path
Various methods are available for upgrading to Customer Journey Analytics. Choose the method that is best for your organization, depending on your organization’s current Adobe Analytics environment and long-term goals.
Step 3:
Send data to Adobe Experience Platform
The process for sending data to Adobe Experience Platform differs depending on the upgrade path that you chose in Step 2.
Step 4:
Retain historical data
Most organizations need to retain their historical Adobe Analytics data for a certain amount of time. Various options are available to accomplish this.
Step 5:
Perform additional implementation tasks
At this point in the upgrade process, you need to perform various tasks before your Customer Journey Analytics environment is ready to use.

These additional tasks apply to upgrades from Adobe Analytics as well as new Customer Journey Analytics implementations.

These tasks include:

- Bringing other data into Experience Platform
- Creating connections between Platform datasets and Customer Journey Analytics
- Creating data views
- Porting the reporting API usage
- Accounting for Data Feeds and Data Warehouse
- Migrating projects and components
- Planning user onboarding

For more information, see [Customer Journey Analytics Getting Started](/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/cja-getting-started).

## First, choose the upgrade path

Various methods are available for upgrading to Customer Journey Analytics. [Choose the method that is best for your organization](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-path).

The upgrade path that you choose depends on your organization’s current Adobe Analytics environment and long-term goals.

recommendation-more-help
