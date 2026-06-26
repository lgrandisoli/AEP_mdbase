---
title: "Upgrade alternative: Use the Analytics source connector exclusively to upgrade to Customer Journey Analytics use-source-connector-exclusively"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-source-connector"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:42.765074+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Upgrade alternative: Use the Analytics source connector exclusively to upgrade to Customer Journey Analytics use-source-connector-exclusively

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
Though it is not recommended, you can use the Analytics source connector as the sole implementation path for Customer Journey Analytics. However, because of the inherent disadvantages associated with this type of upgrade, Adobe recommends using the Analytics source connector in conjunction with a new implementation of the Experience Platform Web SDK. For more information about this recommended upgrade path, see [Recommended path when upgrading from Adobe Analytics to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations).

## Advantages and disadvantages

Use the information in the table below to understand the advantages and disadvantages of using the source connector exclusively when upgrading to Customer Journey Analytics.

Advantages
Disadvantages
- Least time-consuming and demanding upgrade path. Data is migrated to Customer Journey Analytics quickly and easily.

- Data is not sent to Edge Network : This results in the following disadvantages: Highest level of latency in reporting across all upgrade paths; not optimized for real-time personalization use cases. Data cannot be shared with other Adobe Experience Platform applications; it is constrained to Customer Journey Analytics only Reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth)
- Difficult to move to the Web SDK in the future : Eventually, you will likely want access to the advantages provided by the Experience Platform Web SDK. In order to start using the Experience Platform Web SDK, you must do a new implementation.
- Uses the Analytics Experience Event field group in your schema : This field group adds many Adobe Analytics events that are not needed in your Customer Journey Analytics schema. This can lead to a more cluttered, complex schema than what is otherwise needed for Customer Journey Analytics.
- Requires licenses for both Adobe Analytics and Customer Journey Analytics : Using the Analytics source connector requires that you pay for both Adobe Analytics and Customer Journey Analytics.

## Basic steps

If you decide to use the Analytics source connector as the sole implementation path for Customer Journey Analytics, follow the implementation steps described in [Ingest and use data using source connectors](/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/sources).

recommendation-more-help
