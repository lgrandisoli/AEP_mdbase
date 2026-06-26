---
title: "Transition from the Analytics source connector to the Web SDK for Customer Journey Analytics transition-from-source-connector"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/other-upgrade-scenarios/cja-upgrade-from-source-connector"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:53.300249+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Transition from the Analytics source connector to the Web SDK for Customer Journey Analytics transition-from-source-connector

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Use the information on this page when answering questions in the Customer Journey Analytics Upgrade Guide.
To access the guide from Customer Journey Analytics, select the
Workspace
tab, then select
Upgrade to Customer Journey Analytics
in the left panel. Follow the on-screen instructions.
There are inherent disadvantages with using the Analytics source connector as your sole implementation for Customer Journey Analytics.

If your organization has already upgraded to Customer Journey Analytics using only the Analytics source connector implementation, Adobe recommends transitioning to a new implementation of the Web SDK for ongoing data collection, and using the Analytics source connector only for historical data.

## Understand advantages and disadvantages of using the Analytics source connector exclusively

For information about the advantages and disadvantages of using the Analytics source connector, see [Use the Analytics source connector exclusively to upgrade to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-source-connector).

## Transition from the Analytics source connector to the Web SDK

Following is the high-level process for transitioning from exclusively using the Analytics source connector to an implementation comprised of both the Analytics source connector and a Web SDK implementation:

- Create a Web SDK implementation, as described in Detailed recommended upgrade steps in the article, Upgrade from Adobe Analytics to Customer Journey Analytics . After the Web SDK implementation is configured, continue with the following steps.
- Create an XDM schema for the Analytics source connector .
- Map each Adobe Analytics dimension from your Analytics source connector to the dimension in the Web SDK schema. In the Map standard fields section, select the Custom tab. Select Add new mapping . In the Source field , select an Adobe Analytics field from the Adobe Analytics ExperienceEvent Template field group. Then, in the Target field , select the XDM field that you want to map it to. Repeat this process for each field in the Adobe Analytics ExperienceEvent Template field group that you are using to collect data in Adobe Analytics.
- Add the dataset that was automatically created with your original Analytics source connector to your Customer Journey Analytics connection. For more information, see Add the dataset from your current Analytics source connector to the connection .
- (Conditional) If you are using lookup datasets, you must create the lookup dataset and add it to your connection. For more information, see Create lookup datasets to classify data in Customer Journey Analytics .
- Delete your original Analytics source connector.
- Create a new Analytics source connector and map fields .
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
