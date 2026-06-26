---
title: "Alerts overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/alerts/intelligent-alerts"
category: "overview"
topic: "analytics-platform/using/cja-components/alerts"
created_at: "2026-06-23T20:43:34.868321+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Alerts overview

Last update: May 13, 2026
- Topics:
- [Workspace Basics](#)

CREATED FOR:

- User
- Admin

Alerts in Customer Journey Analytics allow you to be notified based on changed percentages or specific data points.

Depending on your Customer Journey Analytics package, you can also use alerts to be triggered based on anomaly thresholds. These alerts (also known as *Intelligent Alerts*), provide granular controls that integrate with [Anomaly Detection](/en/docs/analytics-platform/using/cja-workspace/anomaly-detection/anomaly-detection), triggering when you need them most.

- Preview how often an alert triggers.
- Send alerts by e-mail or SMS with links to auto-generated Analysis Workspace projects.
- Create stacked alerts that capture multiple metrics in a single alert.
- Build alerts based on: Anomalies in metrics that exist, are above, or below expected threshold values. Anomaly detection builds an expected value plus an upper and lower bound using historical data. If the actual metric value goes above the upper bound or below the lower bound defined as the threshold value, that event is considered an anomaly at the threshold confidence level and does trigger the alert. A higher threshold (for example: 99% or 99.9%) implies a wider band, which results in fewer alerts that are caused by more extreme anomalies. A lower threshold (for example: 90%) implies a narrower band, which results in more alerts that are caused by less extreme anomalies. Changes in metrics by a specific percentage. Metrics that are above, below, or equal to a specific value. (available only to Adobe Analytics customers with a Select, Prime, or Ultimate package)

This [video tutorial](/en/docs/analytics-learn/tutorials/data-science/intelligent-alerts) provides a basic overview of alerts.

## Understand how alerts differ

The process of using alerts in Customer Journey Analytics is nearly identical to using alerts in Adobe Analytics. However, there are important differences.

For more information, see [Alerts feature comparison: Customer Journey Analytics and Adobe Analytics](/en/docs/analytics-platform/using/cja-components/alerts/alerts-feature-comparison).

## Anomaly lookback for alerts

NOTE
Using alerts with anomaly detection (also known as
Intelligent Alerts
) is available only to organizations with a Customer Journey Analytics Select, Prime, or Ultimate package.
If an alert uses anomaly detection, the training period varies based on the granularity selected for the alert.

- Monthly granularity: 15 months + same range last year
- Weekly granularity: 15 weeks + same range last year
- Daily granularity: 35 days + same range last year
- Hourly granularity: 336 hours

For more information, see [Statistical techniques used in Anomaly Detection](/en/docs/analytics-platform/using/cja-workspace/anomaly-detection/statistics-anomaly-detection).

## Create alerts

For information about how to create alerts in Customer Journey Analytics, see [Create alerts](/en/docs/analytics-platform/using/cja-components/alerts/alert-builder).

IMPORTANT
Using timestamped data to create alerts can cause alerts to fire incorrectly. Adobe recommends using non-timestamped data for alerts.
## Manage alerts

You can manage existing alerts in the Alerts manager. You can perform various management tasks on alerts, such as tagging, renaming, deleting, and more.

For more information about how to manage existing alerts in Customer Journey Analytics, see [Manage alerts](/en/docs/analytics-platform/using/cja-components/alerts/alert-manager).

recommendation-more-help
