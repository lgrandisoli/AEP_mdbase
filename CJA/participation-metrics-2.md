---
title: "Participation metrics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/participation-metric"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-23T20:45:57.759221+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Participation metrics

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User
- Admin

Participation metrics are used to quantify how individual values for a dimension (like Page Views) contribute to, or participate in sessions that contain a specific metric (like Orders).

NOTE
Administrators can create metrics with non-default attribution models, such as Participation, as part of a
data view
. See
Attribution component settings
for more details.
The steps below show how any user with [Create calculated metric permission](/en/docs/analytics-platform/using/technotes/access-control#user-level-access) can create a participation metric.

- Create a calculated metric , and in the Calculated metrics builder , name the metric Participation or something similar.
- Drag a metric containing a success event, for example Orders, into Definition area.
- Select for the metric.
- In the popup that appears, select Use a non-default attribution model to define the attribution model of that event to Participation and select Session for the Container. Select Apply to confirm. (Partipation|Session) is added to the metric component name.
- Select Save to save the metric.
- Use the calculated metric in your report. For example, use the calculated Orders (Session Participation) metric in a report to show which Customer Tier contributed to (or participated in) sessions that contained an order.

recommendation-more-help
