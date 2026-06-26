---
title: "Implement the loader tag for the Web SDK extension upgrade-tag-loader"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-tags/cja-upgrade-tag-loader"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:52.671135+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Implement the loader tag for the Web SDK extension upgrade-tag-loader

Last update: June 5, 2026
- Topics:
- [Administration](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

You must install your tag on the website you want to track, which implies placing code in the header tag of your website’s template.

The following process describes how to get the code that references your tag. For supplemental information, see the [Implementation guides for tags and event forwarding](/en/docs/experience-platform/tags/get-started/implementation-guides) in the Experience Platform documentation.

To get the code that references your tag:

- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- On the Tag Properties page, select your newly created tag from the list of properties to open it.
- Select Environments in the left rail.
- From the list of environments, select the correct install (box) button. In the Web Install Instructions dialog, select the copy button next to the script code that should read like: code language-none <script src="https://assets.adobedtm.com/2a518741ab24/.../launch-...-development.min.js" async></script>>
- Select Close . Instead of the code for the development environment, you could have selected another environment (staging, production) based on where you are in the process of deploying the Adobe Experience Platform Web SDK. See Environments for more information.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
