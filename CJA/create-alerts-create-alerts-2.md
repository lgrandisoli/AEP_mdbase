---
title: "Create alerts create-alerts"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/alerts/alert-builder"
category: "other"
topic: "analytics-platform/using/cja-components/alerts"
created_at: "2026-06-23T20:45:28.560262+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create alerts create-alerts

Last update: May 13, 2026
- Topics:
- [Workspace Basics](#)

CREATED FOR:

- User
- Admin

NOTE
Using alerts with anomaly detection (also known as
Intelligent Alerts
) is available only to organizations with a Customer Journey Analytics Prime or Ultimate package.
Alerts in Customer Journey Analytics allow you to be notified based on changed percentages or specific data points. Depending on your Customer Journey Analytics package, you can also use alerts to be triggered based on anomaly thresholds.

For more detailed information about alerts, see [Alerts overview](/en/docs/analytics-platform/using/cja-components/alerts/intelligent-alerts).

To create an alert:

- In Customer Journey Analytics, select Components > Alerts . In the Alerts manager , select Add to create a new alert, or select any of the alerts listed to modify an existing alert.
- In Analysis Workspace, select one or more line items in a freeform table, select Create alert from selection from the context menu. This action instantly pre-populates the alert builder to create an alert with the correct metrics and segments.

The [Alert builder](#alert-builder) interface displays.

## Alert builder

The Alert builder interface is familiar to the interface that you use when you build segments or calculated metrics in Customer Journey Analytics:

Specify the following details in the Alerts builder for an alert:

Element
Description
Title
Specify a name for the alert. The alert name might contain the name of the report or the metrics threshold.
Description (optional)
Specify a description for the alert.
Time granularity
Select how often you want the metric to be checked: Daily, Weekly, or Monthly.

**Note**: For data views with a [custom calendar](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#calendar), monthly granularity is not supported in the Alert Builder.true?

Recipients
Specify where the alert can be sent. An alert can be sent to an Analytics user, an Analytics group, a raw email address, or to a phone number.

**Important**: The phone number must be preceded by a + and a [country code](https://countrycode.org/).

The email that a user receives after an alert:

Expiration date
Set the date and time when you want the alert to expire.
Delay
The time required before data is complete and available to be reported on in Customer Journey Analytics varies by organization, typically ranging from 3 to 9 hours past the data event time. For alerts to be accurate, event data for a given event range must be complete, meaning that Adobe is no longer receiving any event data for the specified event range.

To account for this delay in ingestion time, alerts have a default delay of 9 hours before they are sent.

You can adjust the default delay of 9 hours to anywhere between 0 and 24 hours. However, decreasing the delay below 9 hours can mean that you are reporting on incomplete data, which results in inaccurate alert information.

Consider the following when decreasing the delay time:

- Understand data availability versus data completeness : Batch data is ingested into an Experience Platform dataset only after a period of 3 to 9 hours. For alerts to be accurate, data ingestion must be complete, with all batch data available in the dataset.
- Determine how long it takes for your data to be complete and available in the dataset : Data ingestion times differ by organization. Make sure that the delay time you choose for alert delivery is the same or less frequent than the time it takes for the batch data to be available in the Platform datasetadd link? .
- Tip: The most accurate way of knowing the time required for all batch data to be complete and ingested into the Experience Platform dataset is to consult the data engineers in your organization. Alternatively, you can get a general idea of how long it takes for the batch delivery in your organization to be available in the Platform dataset. Create the following freeform table in Analysis Workspace: In a freeform table in Analysis Workspace, add an Events metric and a Day dimension. Break down the Day dimension using an Hours dimension. Hours that have no data show as 0. Account for errors in your calculations : If you decrease the default delay time, configure the delay for at least an hour longer than the time it takes your organization for data ingestion completeness. For example, if there is a 3-hour delay before your data ingestion is complete, then you should set the delay to 4 hours.

For more information, see [Data ingestion times vary in Customer Journey Analytics](/en/docs/analytics-platform/using/cja-components/alerts/alerts-feature-comparison#data-ingestion-times-vary-in-customer-journey-analytics) in the article [Alerts feature comparison: Customer Journey Analytics and Adobe Analytics](/en/docs/analytics-platform/using/cja-components/alerts/alerts-feature-comparison).

Send an alert when
**Any of these metrics trigger**:

- Drag and drop metrics (including calculated metrics) to create triggers for the alert. An incompatible components message appears if not all the metrics, dimensions, or segments in the alert are compatible with the currently selected report suite. Determine the threshold (for an anomaly) that the metric must exceed or the value (in case of above, below, equals or percentage change) to use before an alert is set.
- Select one of the following conditions: anomaly exists anomaly is above expected anomaly is below expected is above or equals is below or equals changes by
- Select a treshold value or enter a value.

**With all of these filters**: Drag and drop segments or dimensions to add filters to the alert. For example, adding a *Mobile Devices Only* segment would mean that the rule triggers only for mobile devices. You can add additional filters by using an AND statement. You can add AND or OR rules by clicking the gear icon.

See [Alerts - use cases](/en/docs/analytics-platform/using/cja-components/alerts/alerts-use-cases) for example uses cases.

Preview
The interactive alert preview shows you how often, approximately, an alert fires based on past experience.

For example, if you set the time granularity to daily, the preview can tell you that the alert would have been triggered for a certain metric x times during the last 30 or 31 days.

If you find that too many alerts are triggered, you can adjust the threshold in the [Manage alerts](/en/docs/analytics-platform/using/cja-components/alerts/alert-manager).

{width="50%"}

recommendation-more-help
