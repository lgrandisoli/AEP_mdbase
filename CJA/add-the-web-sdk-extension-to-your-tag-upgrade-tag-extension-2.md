---
title: "Add the Web SDK extension to your tag upgrade-tag-extension"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-tags/cja-upgrade-tag-extension"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:52.308998+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Add the Web SDK extension to your tag upgrade-tag-extension

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

You can use the Tags feature within Adobe Experience Platform to implement code on your site to collect data. This tag management solution lets you deploy code alongside other tagging requirements. Tags offer seamless integration with Adobe Experience Platform using the Adobe Experience Platform Web SDK extension.

The following information describes how to add the Web SDK extension to your tag. For supplemental information, see the [Configure the Web SDK tag extension](/en/docs/experience-platform/tags/extensions/client/web-sdk/web-sdk-extension-configuration) in the Experience Platform documentation. The Web SDK includes the Adobe Experience Cloud ID Service natively, so you do not need to add the ID service extension to your tag.

After you [create a tag](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-tags/cja-upgrade-tag-property), you must configure it with the Adobe Experience Platform Web SDK extension. This ensures that you can send data to Adobe Experience Platform (through your datastream).

To add the Web SDK extension to your tag:

- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- Select your newly created tag from the list of Tag Properties to open it.
- Select Extensions in the left rail.
- Select Catalog in the top bar.
- Search for or scroll to the Adobe Experience Platform Web SDK extension , then select Install to install it. {width="35%"}
- Select your sandbox and your earlier created datastream for your Production Environment and (optional) Staging Environment and Development Environment.
- Select Save .
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
