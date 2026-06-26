---
title: "Migrate data from Google Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/third-party/ga/overview"
category: "overview"
topic: "analytics-platform/using/cja-usecases/third-party"
created_at: "2026-06-02T19:07:31.196395+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Migrate data from Google Analytics

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- Admin

If you are new to Customer Journey Analytics, it is possible that your organization has existing data on another Analytics platform, such as Google Analytics. You can follow these overarching steps to move that data into Adobe Experience Platform, allowing you to view reports in Customer Journey Analytics.

Workflows are provided for both historical data and current data collection. You can follow one or both of these workflows, depending on your organization’s data needs.

## Bring historical data from Google Analytics into Adobe Experience Platform

Ingesting historical (backfill) data involves exporting data from Google and importing that data into Adobe Experience Platform. See [Ingest Google Analytics data in Adobe Experience Platform](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/backfill).

Once you successfully bring historical data into Platform, you can either [Configure streaming current data](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/streaming), or immediately start reporting on backfilled data in Customer Journey Analytics by [Creating a connection](/en/docs/analytics-platform/using/cja-connections/create-connection).

## Configure an existing Google Analytics implementation for Adobe Experience Platform configure

Ingesting current (streaming) data involves sending data to the Adobe Experience Platform Edge Network, which then forwards that data to Adobe Experience Platform. See [Set up streaming Google Analytics data in Adobe Experience Platform](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/streaming).

## Configure a Connection and Data View in Customer Journey Analytics

Once you successfully ingest historical data and/or configure data collection to Adobe Experience Platform, you can [Create a connection](/en/docs/analytics-platform/using/cja-connections/create-connection) to allow Customer Journey Analytics to reference that data.

Use the connection to create one or more [Data Views](/en/docs/analytics-platform/using/cja-dataviews/create-dataview) for use in Analysis Workspace.

## Create reports

After configuring dimensions and metrics within a Data View, you can begin using Analysis Workspace to generate the desired reports. See [Report on Google Analytics data in Customer Journey Analytics](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/report).

recommendation-more-help
