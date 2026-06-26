---
title: "Understand your Adobe Analytics implementation and how it affects your upgrade to Customer Journey Analytics implementation-affects-upgrade"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/additional-information/cja-upgrade-analytics-implementation"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:44.530893+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Understand your Adobe Analytics implementation and how it affects your upgrade to Customer Journey Analytics implementation-affects-upgrade

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Integrations](#)
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
There are various ways that Adobe Analytics can be implemented. When upgrading to Customer Journey Analytics, not all upgrade paths are available for all Adobe Analytics implementations. However, the recommended upgrade path is available regardless of how Adobe Analytics is implemented in your organization.

Use the information below to learn about your current Adobe Analytics implementation and which upgrade paths are available to your organization.

Contact your Adobe representative if you need more specific advice, guidance, or support.

Existing Adobe Analytics implementation
Description
Available upgrade paths
AppMeasurement
AppMeasurement for JavaScript has historically been a common method to implement Adobe Analytics.

For more information about this implementation type, see [Implement Adobe Analytics with AppMeasurement for JavaScript](/en/docs/analytics/implementation/js/overview).

- [(Recommended) New implementation of the Experience Platform Web SDK for ongoing data collection; the Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)
- [New implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk)
- [Migrate Adobe Analytics to the Web SDK](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-appmeasurement)
- [Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-source-connector)

Adobe Analytics extension (tags)
Tags in Adobe Experience Platform is a tag management solution that lets you deploy Analytics code alongside other tagging requirements. Adobe offers integrations with other solutions and products, and lets you deploy custom code. All of these tasks can be done without relying on any development teams in your organization to update code on your site.

For more information about this implementation type, see [Implement Adobe Analytics using the Analytics extension](/en/docs/analytics/implementation/launch/overview).

- [(Recommended) New implementation of the Experience Platform Web SDK for ongoing data collection; the Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)
- [New implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk)
- [Migrate Adobe Analytics to the Web SDK](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-appmeasurement)
- [Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-source-connector)

Experience Platform Web SDK (alloy.js)
The Experience Platform Web SDK is Adobe’s current recommended method to implement Adobe Analytics. The Adobe Experience Platform Edge Network allows you to send data destined to multiple products to a centralized location.

For more information about this implementation type, see [Implement Adobe Analytics with the Adobe Experience Platform Edge Network](/en/docs/analytics/implementation/aep-edge/overview).

- [(Recommended) New implementation of the Experience Platform Web SDK for ongoing data collection; the Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)
- [New implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk)
- [Configure the Adobe Analytics Web SDK implementation to send data to Platform](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/additional-information/cja-upgrade-existing-adobe-analytics-websdk)

Experience Platform Web SDK extension (tags)
The Experience Platform Web SDK is Adobe’s current recommended method to implement Adobe Analytics for web data. The Adobe Experience Platform Edge Network allows you to send data destined to multiple products to a centralized location.

For more information about this implementation type, see [Implement Adobe Analytics using the Adobe Experience Platform Web SDK](/en/docs/analytics/implementation/aep-edge/web-sdk/overview)

- [(Recommended) New implementation of the Experience Platform Web SDK for ongoing data collection; the Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)
- [New implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk)
- [Configure the Adobe Analytics Web SDK implementation to send data to Platform](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/additional-information/cja-upgrade-existing-adobe-analytics-websdk)

Experience Platform Mobile SDK
The Experience Platform Mobile SDK is Adobe’s current recommended method to implement Adobe Analytics for mobile data. The Adobe Experience Platform Edge Network allows you to send data destined to multiple products to a centralized location.

The Adobe Experience Platform Mobile SDK helps power Adobe’s CX Enterprise solutions and services in your mobile apps.

For more information about this implementation type, see [Implement Adobe Analytics using the Adobe Experience Platform Mobile SDK](/en/docs/analytics/implementation/aep-edge/mobile-sdk/overview)

- [(Recommended) New implementation of the Experience Platform Web SDK for ongoing data collection; the Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)
- [New implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk)
- [Configure the Adobe Analytics Web SDK implementation to send data to Platform](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/additional-information/cja-upgrade-existing-adobe-analytics-websdk)

Bulk Data Insertion API
The Bulk Data Insertion API (BDIA) is an Adobe Analytics capability that lets you upload server call data in batches of files instead of using client-side libraries such as AppMeasurement.

For more information about this implementation type, see [Bulk Data Insertion API](https://developer.adobe.com/analytics-apis/docs/2.0/guides/endpoints/bulk-data-insertion/).

- [(Recommended) New implementation of the Experience Platform Web SDK for ongoing data collection; the Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations)
- [New implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk)
- [Adobe Experience Platform Edge Network Server API and Edge Network](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/serverapi)

recommendation-more-help
