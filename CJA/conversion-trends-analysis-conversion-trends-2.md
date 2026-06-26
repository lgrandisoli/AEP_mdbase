---
title: "Conversion trends analysis conversion-trends"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/funnel/conversion-trends"
category: "guides"
topic: "analytics-platform/using/guided-analysis/funnel"
created_at: "2026-06-02T19:09:22.680274+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Conversion trends analysis conversion-trends

Last update: May 13, 2026
- Topics:
- [Adobe Product Analytics](#)
- [Guided Analysis](#)

CREATED FOR:

- User

The **Conversion trends** analysis provides a trended visualization of conversion rates over time. The horizontal axis is a time interval, while the vertical axis represents the conversion rate.

https://experienceleague.adobe.com/en/docs/customer-journey-analytics-learn/tutorials/guided-analysis/conversion-trends
## Use cases

Use cases for this analysis include:

- **Track optimization efforts**: After identifying key bottlenecks that you want to improve using the [Funnel](/en/docs/analytics-platform/using/guided-analysis/funnel) analysis, you can use this analysis to track how those optimizations impact conversion rate over time.
- **A/B testing evaluation**: Evaluate the effectiveness of A/B tests or experiments conducted within the context of a funnel. By comparing conversion rates between different variations, you can easily determine which tests provide higher conversion rates, leading to data-driven decisions around which variations to implement permanently.
- **Campaign evaluation over time**: Measure the effectiveness of marketing campaigns over time. You can create a segment that focuses on users that touched a given campaign, and compare their conversion rates with other campaigns. You can also compare current conversion rates with similar campaigns that were run in the past.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- **View**: Switch between this analysis and [Funnel](/en/docs/analytics-platform/using/guided-analysis/funnel).
- **Steps**: The event touchpoints that you want to track. Each bar in the chart represents a step. You can include up to ten steps.
- **Counted as**: The counting method that you want to apply to the selected events. Options include Users and Sessions.
- **Segments**: The segments that you want to compare the funnel across. Each segment selected splits each step into multiple bars. Each color represents a different segment. You can include up to three segments.

### Chart settings

The Conversion trends analysis offers the following chart settings, which can be adjusted in the menu above the chart:

- **Chart type**: The type of visualization that you want to use. Options include Line.
- **Conversion from**: Determines the percentage calculation from step to step. Options include calculating conversion from the First step or Previous step.

NOTE
The
Average
column in the Conversion trends analysis table differs from the
Total
column in the
Funnel analysis
table. The former is an average of the interval columns (for example, average of daily conversion rates), while the latter is an aggregated calculation across the full date range.
### Time comparison

You can compare the current time period to a previous time period. If you select an option in this menu, every data point receives a similarly colored dotted-lined counterpart. This counterpart represents that same metric in the selected previous date range. Setting this option doubles the number of items on the chart and rows in the table.

Available time comparison options include the previous period, 13 weeks prior, 52 weeks prior, and a Customized date range. If you select Customized date range, additional options appear to let you select the number and granularity. If you select None, the date comparison is removed.

### Date range

The desired date range for your analysis. There are two components to this setting:

- **Interval**: The date granularity that you want to view trended data by. Valid options include Hourly, Daily, Weekly, Monthly, and Quarterly. The same date range can have different intervals, which affect the number of data points in the chart and the number of columns in the table. For example, viewing an analysis spanning three days with daily granularity would show only three data points, while an analysis spanning three days with hourly granularity would show 72 data points.
- **Date**: The starting and ending date. Rolling date range presets and previously saved custom ranges are available for your convenience, or you can use the calendar selector to choose a fixed date range.

recommendation-more-help
