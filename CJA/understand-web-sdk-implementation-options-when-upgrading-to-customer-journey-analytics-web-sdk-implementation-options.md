---
title: "Understand Web SDK implementation options when upgrading to Customer Journey Analytics web-sdk-implementation-options"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/additional-information/cja-upgrade-websdk-implementation"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:41.423588+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Understand Web SDK implementation options when upgrading to Customer Journey Analytics web-sdk-implementation-options

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
The recommended process of upgrading from Adobe Analytics to Customer Journey Analytics is a new implementation of the Experience Platform Web SDK, which is the preferred data collection method for Customer Journey Analytics.

There are three supported ways to use Adobe Experience Platform Web SDK:

- Web SDK tag extension : Adobe recommends using this method. Install a tag loader on your site, then use the Adobe Experience Platform Data Collection UI to configure your implementation.
- Web SDK JavaScript library : Reference a CDN-hosted library file, or host the library file using your own infrastructure. Make calls to the library within code on your site.
- NPM : Install the Web SDK on your site using the NPM package manager.

For more information, see [Web SDK installation overview](/en/docs/experience-platform/web-sdk/install/overview) in the Experience Platform Web SDK Guide.

recommendation-more-help
