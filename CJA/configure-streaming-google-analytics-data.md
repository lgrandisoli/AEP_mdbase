---
title: "Configure streaming Google Analytics data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/third-party/ga/streaming"
category: "other"
topic: "analytics-platform/using/cja-usecases/third-party"
created_at: "2026-06-02T19:09:11.749536+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure streaming Google Analytics data

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- Admin

This page focuses on how to ingest your live Google Analytics data into Adobe Experience Platform, allowing you to reference that dataset in a Data View within Customer Journey Analytics. You can combine the steps on this page with [Ingest Google Analytics historical data into Adobe Experience Platform](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/backfill), which generates a dataset containing historical data. Combine a streaming dataset with a backfill dataset to get a seamless view of past and present data in Customer Journey Analytics.

Configuring data collection involves the following steps:

- Implement [Tags for Adobe Experience Platform](/en/docs/experience-platform/tags/home). See the [Quickstart guide](/en/docs/experience-platform/tags/get-started/quick-start) to get a basic implementation up and running.
- Install the [Google Data Layer extension](/en/docs/experience-platform/tags/extensions/client/google-data-layer/overview). This extension acts as an alternative to installing the Web SDK extension, geared specifically towards a Google data layer.
- [Create a Datastream](/en/docs/experience-platform/datastreams/overview) in Adobe Experience Platform Data Collection. Configure the Datastream to send data to Adobe Experience Platform. You must currently map each Google data layer object to an applicable XDM field here. Adobe plans to simplify this mapping workflow in the future.

Once you implement and publish the desired tags on your site, you can then proceed to [create a connection](/en/docs/analytics-platform/using/cja-connections/create-connection), then [create a data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview).

recommendation-more-help
