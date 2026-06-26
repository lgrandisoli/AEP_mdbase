---
title: "Create a marketing channel derived field for Customer Journey Analytics create-marketing-channel-derived-field"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-marketing-channel"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:08:41.727525+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create a marketing channel derived field for Customer Journey Analytics create-marketing-channel-derived-field

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

When using the Analytics source connector, marketing channels data flows into Customer Journey Analytics through that connector. Marketing Channel rules are configured in traditional Adobe Analytics and some rules are not supported. For more information, see [Use marketing channel dimensions](/en/docs/analytics-platform/using/cja-usecases/aa-data/marketing-channels).

In order to use marketing channels in Customer Journey Analytics when using the Experience Platform Web SDK, you can use derived fields in a data view to re-create the same marketing channels and processing rules for Customer Journey Analytics.

- In Customer Journey Analytics, select the data view where you want to add marketing channels.
- In the data view, select the Components tab.
- Select Create derived field in the left rail.
- In the Create derived field dialog box, select Function templates from the drop-down menu.
- Drag the Marketing channels template onto the blank canvas.
- Customize the logic for each marketing channel to ensure it matches the logic you use to identify each channel in your Adobe Analytics environment. You can modify the output channel names or add logic to identify additional channels specific to your organization.
- In the right column, specify a name and a description for the marketing channel.
- Select Save . Your new derived field is added to the Derived fields > container, as part of Schema fields in the left rail of your Data view.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
