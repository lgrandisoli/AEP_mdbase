---
title: "Ingest Google Analytics historical data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/third-party/ga/backfill"
category: "other"
topic: "analytics-platform/using/cja-usecases/third-party"
created_at: "2026-06-02T19:09:11.332377+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest Google Analytics historical data

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- Admin

This page focuses on how to ingest your Google Analytics historical data into Adobe Experience Platform as a dataset, allowing you to reference that dataset in a Data View within Customer Journey Analytics. You can combine the steps on this page with [Configuring a live Google Analytics implementation](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/streaming), which generates a recurring dataset. Combine this historical dataset with your current implementation’s dataset to get a seamless view of data in Customer Journey Analytics with both current and backfilled data.

## Prerequisites

In order to accomplish these tasks, you need the following access and permissions:

- Access to Adobe Experience Platform
- Access to Google Analytics (GA Standard or GA 360)
- [Admin Access](/en/docs/analytics-platform/using/technotes/access-control) to Customer Journey Analytics

## Set up a BigQuery Export

The data structure in Universal Analytics properties is different from the data structure in Google Analytics 4 properties. Set up a BigQuery Export based on the property type that you want to export data from:

- [Set up a BigQuery Export for a Universal Analytics property](https://support.google.com/analytics/answer/3416092)
- [Set up a BigQuery Export for a Google Analytics 4 property](https://support.google.com/analytics/answer/9823238)

### Additional requirements for Universal Analytics properties

NOTE
This section only applies to Universal Analytics properties. If you are exporting from a GA4 property, you can proceed to
Export data to Google Cloud Platform
.
Universal Analytics properties store each record in their data as a user’s session instead of individual events. A SQL query to transform the Universal Analytics data into a format compatible with Adobe Experience Platform is required. Apply the UNNEST function to the hits field in the GA schema, and save it as a BigQuery table.

See [From Google Analytics to Customer Journey Analytics - BigQuery](https://video.tv.adobe.com/v/332634?quality=12&learn=on#_blank) for a demo video.

style
shade-box
```
SELECT
   *,
   timestamp_seconds(`visitStartTime` + hit.time) AS `timestamp`
FROM
   (
      SELECT
         fullVisitorId,
         visitNumber,
         visitId,
         visitStartTime,
         trafficSource,
         socialEngagementType,
         channelGrouping,
         device,
         geoNetwork,
         hit
      FROM
         `example_bq_table_*`,
         UNNEST(hits) AS hit
   )
```

## Export data to Google Cloud Platform export-gcp

In Google Cloud Platform, navigate to **Export > Export to GCS**. Once the data is in Google Cloud Storage, it is ready to be pulled into Adobe Experience Platform.

## Import the data from Google Cloud Storage into Experience Platform

- In Adobe Experience Platform, select **Sources** on the left.
- Under the Catalog, locate **Google Cloud Storage** option. Click **Add data**.

See [Import Google Analytics data into Adobe Experience Platform](https://video.tv.adobe.com/v/332676?quality=12&learn=on#_blank) for a demo video.

style
shade-box
TIP
If you plan to import both historical and live streaming Google Analytics data, make sure that you use the same schema for both datasets. You can merge the datasets in a Customer Journey Analytics using a
Combined dataset
.
You can map the GA event data into an existing dataset that you created previously, or create a dataset, using whichever XDM schema you choose. Once you have selected the schema, the Experience Platform applies machine learning to automatically pre-map each of the fields in the Google Analytics data to your [XDM schema](/en/docs/experience-platform/xdm/home#ui).

Once you are finished mapping the fields into your XDM schema, you can schedule this import on a recurring basis and apply error validation during the ingestion process. This validation ensures that there aren’t any issues with the data you have imported.

## Required XDM fields

Certain XDM fields in Platform require the correct format in order for data to be correctly processed.

- timestamp : Create a special calculated field in the Experience Platform schema UI. Click Add calculated field and wrap the timestamp string in a date function: date(timestamp, "yyyy-MM-dd HH:mm:ssZ") Save the calculated field to the timestamp data structure in the schema:
- _id : This field must have a value in it - Customer Journey Analytics does not care what the value is. You can add a “1” to the field:

## Next steps

- If you have current data that you want to stream into Adobe Experience Platform, see [Set up streaming for Google Analytics data](/en/docs/analytics-platform/using/cja-usecases/third-party/ga/streaming).
- If you want to begin reporting on backfilled data, see [Create a connection](/en/docs/analytics-platform/using/cja-connections/create-connection).

recommendation-more-help
