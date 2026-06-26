---
title: "Data views use cases"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/data-views-usecases"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-23T20:42:40.759092+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Data views use cases

Last update: May 13, 2026
- Topics:
- [Data Views](#)

CREATED FOR:

- User

These use cases illustrate the flexibility and power of data views in Customer Journey Analytics.

## Use binding dimensions metrics

See the [Use binding dimensions metrics](/en/docs/analytics-platform/using/cja-usecases/data-views/binding-dimensions-metrics) use case for more details.

## Use summary data

See the [Use summary data](/en/docs/analytics-platform/using/cja-usecases/data-views/summary-data) use case for more details.

## BI extension use cases

See the [BI extension use cases](/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/bi-extension-usecases) on how to accomplish a number of use cases using the Customer Journey Analytics BI extension.

## Create a metric from a string schema field string

For example, when creating a data view, you could create an Orders metric from a Page Title schema field that is a string.

- On the Components tab, drag the Page Title into the Metrics section under Included components.
- Highlight the metric you just dragged in and rename it to Orders in the Component Settings on
- Open the Include/Exclude Values section and specify the following: Enable Set include exclude values . Select If all criteria are met from Match . Specify confirmation . The text for the page_title indicates that this page is related to placing an order. After reviewing all the page titles where those criteria are met, a 1 will be counted for each instance. The result is a new metric (not a calculated metric.) A metric that has included/excluded values can be used everywhere any other metric can be used. These metrics work with attribution, segments, and everywhere else you can use standard metrics. {width="100%"}
- You can further specify an attribution model for this metric, such as Last Touch, with a Lookback window of Session. You can also create another Orders metric from the same field and specify a different attribution model. Such as First Touch, and a different Lookback window, such as 30 days.

Another example would be to use the Person ID, a dimension, as a metric to determine how many Person IDs your company has.

## Use integers as dimensions integers

Previously, integers would automatically be treated as metrics in Customer Journey Analytics. Now, numerics (including custom events from Adobe Analytics) can be treated as dimensions. Here is an example:

- Drag the **Duration** integer into the **Dimensions** section under Included Components:
- You can now add **Value Bucketing** to present this dimension in a bucketed fashion in reporting. Without bucketing, each instance of this dimension would appear as a line item in Workspace reporting. {width="100%"}

## Use numeric dimensions as metrics in flow diagrams numeric

You can use a numeric dimension to get metrics into your Flow visualization.

- On the Data Views [Components](/en/docs/analytics-platform/using/cja-dataviews/create-dataview) tab, drag the Marketing Channels schema field into the Metrics area under Included components.
- In Workspace reporting, this flow shows Marketing Channels flowing into Orders:

## Do sub-event filtering sub-event

This capability is specifically applicable to array-based fields. The include/exclude functionality lets you filter at the sub-event level, whereas segments built in the Segment builder only give you segmentation at the event level. You can do sub-event filtering by using include/exclude in Data views, and then reference that new metric/dimension in a segment at the event level.

For example, use the include/exclude functionality in Data views to focus only on products that generated sales of more than $50. So, if you have an order that includes a $50 product purchase and a $25 product purchase, the include/exclude functionality removes the $25 product purchase, not the entire order.

- On the Data Views [Components](/en/docs/analytics-platform/using/cja-dataviews/create-dataview) tab, drag the **Revenue** schema field into the **Metrics** area under Included components.
- Select the metric and configure the following on the right side:a. Under **Format**, select **Currency**.b. Under **Currency**, select **USD**.c. Under **Include/Exclude Values**, select the checkbox next to **Set include/exclude values**.d. Under **Match**, select **If all criteria are met**.e. Under **Criteria**, select **is greater than or equal**.f. Specify 50 as the value.

These new settings allow you to view only high-value revenue and filter out anything below $50.

## Use the No value options setting no-value

Your company may have spent time training your users to expect “Unspecified” for dimensions in reports. The default for dimensions in Data views is *No value*. However, you can specify per dimension how No value should be reported. See the **No value** options for a dimension component.

{width="100%"}

## Create multiple metrics with different attribution settings attribution

Using the **Duplicate** feature at the top right, to create a number of Total Revenue metrics with different attribution settings like **First Touch**, **Last Touch**, and **Algorithmic**.

Don’t forget to rename each metric to reflect the differences, such as Total Revenue (Algorithmic)

{width="100%"}

For more information on other data views settings, see [Create data views](/en/docs/analytics-platform/using/cja-dataviews/create-dataview).For a conceptual overview of data views, see [Data views overview](/en/docs/analytics-platform/using/cja-dataviews/data-views).

## New session and return session reporting new-repeat

You can determine whether a session is indeed the first-ever session for a user or a return session. Based on the reporting window that you defined for this data view and a 13-month lookback window. This reporting lets you determine, for example:

- What percentage of your orders are coming from new or return sessions?
- For a given marketing channel, or a specific campaign, are you targeting first-time users or return users? How does this choice influence conversion rates?

One dimension and two metrics facilitates this reporting:

- Session type - This dimension has two values: New and Returning. The New line item includes all the behavior (that is, metrics against this dimension) from a session that has been determined to be a person’s defined first session. Everything else is included in the Returning line item (assuming everything belongs to a session). Where metrics are not part of any session, they fall into the ‘Not applicable’ bucket for this dimension.
- First-time Sessions . The First-time Sessions metric is defined as a person’s defined first session within the reporting window.
- Return Sessions The Return Sessions metric is the number of sessions that were not a person’s first-time session.–>

To access the components:

- Go into the data view editor.
- Select the **Components** tab and then select **Standard components** from the left rail.
- Drag the **Session type**, **First-time Sessions**, and **Return Sessions** components into your data view.

New sessions are reported accurately almost always. The only exceptions are:

- When a first session occurred before the 13-month lookback window.This session is ignored.
- When a session spans both the lookback window and the reporting window.For example, you run a report from June 1, 2022 to June 15, 2022. The lookback window would span from May 1, 2021 to May 31, 2022. If a session starts on May 30, 2022 and ends on June 1, 2022, the session is included in the lookback window. And all sessions in the reporting window are counted as return sessions.

## Use the Date and Date-Time functionality date

Schemas in Adobe Experience Platform contain Date and Date-Time fields. Customer Journey Analytics data views now support these fields. When you drag these fields into a data view as a dimension, you can specify their [format](/en/docs/analytics-platform/using/cja-dataviews/component-settings/format). This format setting determines how the fields are displayed in reporting. For example:

- For the Date format, if you select Day with the format Month, Day, Year , an example output in reporting might look like: August 23, 2022.
- For the Date-Time format, if you select Minute of Day with the format Hour:Minute , your output might look like: 20:20.

Dates after Jan 1, 1900 (with the single exception of Jan 1, 1970) and date-time values after Jan 1, 2000 00:00:00 are supported.

### Date and Date-Time use cases

- Date: A travel company collects the departure date for trips as a field in their data. The company would like to have a report, which compares the Day of Week for all departure dates collected to understand which is most popular. And the company would like to do the same for the Month of Year.
- Date-Time: A retail company collects the time for each of their in-store point-of-sale (POS) purchases. Over a given month, the company would like to understand the busiest shopping periods by Hour of Day.

Related Articles
Date and Date-Time in the Format component setting
recommendation-more-help
