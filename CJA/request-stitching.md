---
title: "Request stitching"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/stitching/use-stitching"
category: "other"
topic: "analytics-platform/using/stitching/use-stitching"
created_at: "2026-06-02T19:05:17.106644+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Request stitching

Last update: May 13, 2026
- Topics:
- [Stitching](#)
- [Cross-Channel Analysis](#)

CREATED FOR:

- Admin

IMPORTANT
Request stitching through Adobe is no longer required and this method is deprecated.
Enable stitching in the Connections UI
.
## Request support

- Contact Adobe Customer Support with the following information: A request to enable stitching. The dataset ID for the dataset that you want to rekey. The column name (identity path and namespace) of the persistent ID for the desired dataset (the identifier that appears on every row). If the dataset supports identityMap : For field-based stitching, specify the namespace for both the persistent and person IDs. For graph-based stitching, specify the namespace for the persistent ID and the identity namespace to use for querying the identity graph. If the dataset does not support identityMap : For field-based stitching, the column name of the person ID for the desired dataset (the person identifier, which also acts as a link between datasets in the context of a connection). For graph-based stitching, the identity namespace that you want to use for querying the identity graph. Your preference of lookback window and replay frequency. See your Customer Journey Analytics package for the options available. Sandbox name.
- The Adobe Customer Support works with Adobe engineering to enable stitching upon receiving your request. Once enabled, a rekeyed dataset that contains a stitched ID column appears in Adobe Experience Platform. Adobe Customer Support can provide the new dataset’s ID.
- When first turned on, Adobe provides a backfill of stitched data. See your Customer Journey Analytics package for the option available.
- If you want to use the stitched dataset in a cross-channel analysis, you need to add the stitched dataset to a connection in Customer Journey Analytics. Then add any other datasets required for cross-channel analysis, and select the correct person ID for each dataset.
- Create a data view based on the connection.

Once the data view is set up, you can run your Customer Journey Analytics reporting analysis across channels and devices.

## Limitations

- Apply any change that you make to the source event dataset schema also to the new stitched dataset schema.
- If you remove the source dataset, the stitched dataset stops processing and gets removed by the system.
- Data usage labels are not automatically propagated to the stitched dataset schema. If you have data usage labels applied to the source dataset schema, you need to apply these data usage labels manually to the stitched dataset schema. See Managing data usage labels in Experience Platform for more information.

recommendation-more-help
