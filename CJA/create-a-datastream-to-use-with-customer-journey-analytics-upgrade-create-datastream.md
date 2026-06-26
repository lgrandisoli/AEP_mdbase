---
title: "Create a datastream to use with Customer Journey Analytics upgrade-create-datastream"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-datastream/cja-upgrade-datastream"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:48.192108+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create a datastream to use with Customer Journey Analytics upgrade-create-datastream

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

A datastream represents the server-side configuration when implementing the Adobe Experience Platform Web and Mobile SDKs. When collecting data with the Adobe Experience Platform SDKs, data is sent to the Adobe Experience Platform Edge Network. It is the datastream that determines to which services that data is forwarded.

In your setup, you want to configure the datastream to send the collected data to your dataset in Adobe Experience Platform.

NOTE
The following steps are required only for Adobe Analytics implementations using AppMeasurement or the Analytics extension (tags).
If your Adobe Analytics implementation uses the Web SDK or the Web SDK Extension, the datastream already exists in your Adobe Analytics environment.
To set up your datastream:

- In Adobe Experience Platform, select Datastreams from DATA COLLECTION in the left rail.
- Select New Datastream .
- Name and describe your datastream. Select your schema from the Event Schema list.
- Select Save .
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
