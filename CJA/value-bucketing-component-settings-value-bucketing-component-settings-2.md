---
title: "Value Bucketing component settings value-bucketing-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/value-bucketing"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-23T20:42:45.897264+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Value Bucketing component settings value-bucketing-component-settings

Last update: June 5, 2026
- Topics:
- [Data management](#)

CREATED FOR:

- Admin

When creating or editing a data view, value bucketing allows you to combine numeric values based on a range. It is only available for dimensions using Integer or Double schema data types.

Value bucketing is valuable when you want to group ranges together instead of treating every unique number as a separate dimension item. For example, a bucket of ‘Between 5 and up to 10’ appears as a line item ‘5 to 10’ in Analysis Workspace.

If you would like the flexibility of reporting on both a bucketed and non-bucketed dimension, drag two copies of the component into the available dimensions list. Enable bucketing on one dimension, and disable it on the other.

Setting
Description
Bucket value
A checkbox that lets you enable bucketing.
Less than
The upper boundary of the first dimension bucket.
Including and less than
Boundaries of subsequent buckets.
Greater than or equal to
The lower boundary of the last dimension bucket.
Add bucket
Lets you add another bucket to numeric dimension bucketing. You can add up to 20 buckets in a single dimension.
recommendation-more-help
