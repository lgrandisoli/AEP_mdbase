---
title: "Add Platform as a service to your datastream upgrade-addplatform-datastream"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-datastream/cja-upgrade-datastream-addplatform"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:51.841168+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Add Platform as a service to your datastream upgrade-addplatform-datastream

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Administration](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

A datastream should already exist before you complete the steps in this section. When and how the datastream was created depends on your Adobe Analytics implementation, as follows:

- If your Adobe Analytics implementation uses the Web SDK or the Web SDK Extension, the datastream was available for your Adobe Analytics environment, prior to the upgrade process.
- For other Adobe Analytics implementations, creating a datastream is part of the upgrade process, as described in Create a datastream to use with Customer Journey Analytics .

With the datastream available, you need to add Platform as a service:

- In the Adobe Experience Platform UI, select Datastreams from DATA COLLECTION in the left rail.
- Select the datastream that was previously configured.
- Select Add Service .
- In the Add Service screen: Select Adobe Experience Platform from the Service list. Ensure Enabled is selected. Select your dataset from the Event Dataset list. Leave the other settings and select Save to save the datastream. Your datastream is now configured to forward the data collected from your website to your dataset in Adobe Experience Platform. See Datastreams overview for more information on how to configure a datastream and how to handle sensitive data.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
