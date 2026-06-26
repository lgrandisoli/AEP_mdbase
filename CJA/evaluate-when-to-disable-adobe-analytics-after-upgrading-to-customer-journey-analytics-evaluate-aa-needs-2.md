---
title: "Evaluate when to disable Adobe Analytics after upgrading to Customer Journey Analytics evaluate-aa-needs"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-fully-move"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:49.289257+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Evaluate when to disable Adobe Analytics after upgrading to Customer Journey Analytics evaluate-aa-needs

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Administration](#)

CREATED FOR:

- Admin

NOTE
Use the information on this page when answering questions in the Customer Journey Analytics Upgrade Guide.
To access the guide from Customer Journey Analytics, select the
Workspace
tab, then select
Upgrade to Customer Journey Analytics
in the left panel. Follow the on-screen instructions.
Most organizations will eventually disable Adobe Analytics after upgrading to Customer Journey Analytics. This is due to the cost and complexity of maintaining two analytics environments.

However, Adobe recommends that you keep your Adobe Analytics environment running for a period of time after implementing Customer Journey Analytics. The following sections describe the reasons for doing so as well as the suggested timing of disabling Adobe Analytics.

## Uses of Adobe Analytics during and after an upgrade

When deciding if and when your organization should disable Adobe Analytics, consider the following uses of Adobe Analytics during and after an upgrade to Customer Journey Analytics:

Uses of Adobe Analytics during and after upgrade
Explanation
Perform side-by-side data comparison
Adobe recommends that you keep your Adobe Analytics environment running for a period of time after your new Customer Journey Analytics environment is running and collecting data. This is the best way to compare your Customer Journey Analytics data side-by-side with your Adobe Analytics data.

Don’t disable Adobe Analytics until you are comfortable with the data in your Customer Journey Analytics environment.

**Note:** Adobe recommends a new implementation of the Web SDK for your Customer Journey Analytics environment, in conjunction with the Analytics source connector for historical data. [Learn more](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)

Retain historical data from Adobe Analytics
Adobe recommends that you keep your Adobe Analytics environment in place with the Analytics source connector for a period of time after your new Customer Journey Analytics environment is running and collecting data. This is the best way to bring historical Adobe Analytics data into Customer Journey Analytics.

After you have collected enough historical data in Customer Journey Analytics with your new Web SDK implementation, you can remove the Analytics source connector entirely. Do this when you can rely solely on the historical data in you collected with the new Customer Journey Analytics Web SDK implementation.

**Note:** Adobe recommends a new implementation of the Web SDK for your Customer Journey Analytics environment, in conjunction with the Analytics source connector for historical data. [Learn more](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)

Use Data Feeds or other Adobe Analytics features
A small set of features are not yet fully available in Customer Journey Analytics. If you need access to these features, it might be necessary to use Adobe Analytics in conjunction with Customer Journey Analytics until these features are available.

Features not fully available in Customer Journey Analytics include Data Feeds and Contribution Analysis. For a complete list of features that aren’t yet available, see [Customer Journey Analytics feature support](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/cja-aa).

## Process and timeline of disabling Adobe Analytics disable-adobe-analytics

Your existing Adobe Analytics implementation is a key part of a successful upgrade to Customer Journey Analytics, as described in the section above, [Uses of Adobe Analytics during and after an upgrade](#uses-of-adobe-analytics-during-and-after-an-upgrade).

When you no longer need Adobe Analytics for the purposes described in the section above, use the following information to remove Adobe Analytics:

- Stop collecting data with Adobe Analytics. After you are satisfied with the side-by-side comparisons of your Adobe Analytics data and your Customer Journey Analytics data, you can stop collecting data with your Adobe Analytics implementation. New Adobe Analytics data will no longer flow to Customer Journey Analytics through the Analytics source connector. However, data that you collected from your Adobe Analytics environment prior to this point is still available as historical data in Customer Journey Analytics through the Analytics source connector. This process differs depending on the data collection method you used to implement Adobe Analytics: accordion AppMeasurement Disable AppMeasurement data collection . accordion Analytics extension (Tags) Disable the Analytics extension in tags. accordion API Disable API data collection. accordion Third-party Work with your tag admin to remove the AppMeasurement library from your third-party tag management system.
- Remove Adobe Analytics as a service from the datastream. With Web SDK data fully functional, work with your Platform administrator to remove Adobe Analytics as a service from the datastream. Before removing Adobe Analytics as a service, make sure that your Analytics users are using Customer Journey Analytics and not Adobe Analytics.
- Remove the Analytics source connector entirely. After you have collected enough historical data in Customer Journey Analytics with your new Web SDK implementation, you can remove the Analytics source connector entirely. Do this when you no longer need the historical data from your Adobe Analytics environment through the Analytics source connector, and you can rely solely on the historical data you collected with the new Web SDK implementation.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
