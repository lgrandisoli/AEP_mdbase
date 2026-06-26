---
title: "Active growth analysis active-growth"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/user-growth/active"
category: "guides"
topic: "analytics-platform/using/guided-analysis/user-growth"
created_at: "2026-06-02T19:09:22.270866+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Active growth analysis active-growth

Last update: May 13, 2026
- Topics:
- [Adobe Product Analytics](#)
- [Guided Analysis](#)

CREATED FOR:

- User

The **Active growth** analysis provides insights into the growth and acquisition of users over a specific period. The horizontal axis is a time interval, while the vertical axis is a measurement of users. Users are split into four categories:

- **New**: The user was active during the current period, but not previously. See how far that the analysis looks back by hovering over *New users* in the chart legend. The lookback range is dynamically determined based on the selected date range and interval.
- **Repeat**: The user was active in the current and immediately previous period.
- **Return**: The user was active in the current period and not active in the immediately previous period, but were formerly active at some point. See how far that the analysis looks back by hovering over *Return users* in the chart legend. The lookback range is dynamically determined based on the selected date range and interval.
- **Dormant**: The user was active in the immediately previous period, but is not active in the current period. Dormant users do not count toward the total number of active users.

All active users (new + repeat + return) appear as a shade of teal above the horizontal axis, while all dormant users appear in orange below the horizontal axis.

https://experienceleague.adobe.com/en/docs/customer-journey-analytics-learn/tutorials/guided-analysis/active-growth
## Use cases

Use cases for this analysis include:

- **User retention and churn:** Provides a clear visualization of periods of high or low user retention. Recognizing these periods of high or low retention can help you make product decisions to encourage high retention or help minimize churn.
- **Campaign assessment**: Viewing a specific campaign can help you understand how much traffic it generated, and how well it helped users remain engaged.
- **User lifecycle analysis**: Analyzing active user growth throughout the user lifecycle can help identify specific stages where user engagement dips. For example, if there is a high ratio of dormant users for individuals in an onboarding stage, it can indicate usability issues or a need for better in-product guidance.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- View : Switch between this analysis and Net growth .
- Events : The event that you want to measure. Since this analysis is user-based, a user who interacts with the event once within the period is counted as an active user. You can include one event in a query.
- Counted as : The counting method that you want to apply to the selected events. Options include Number of users and Percentage of users. [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} Additional B2B options are available for Customer Journey Analytics B2B Edition: Global accounts, Accounts, Buying groups, Opportunities, Percentage of global accounts, Percentage of accounts, Percentage of buying groups, and Percentage of opportunities.
- Segments : The segment that you want to segment data by. You can include one segment in a query.

### Chart settings

The Active growth analysis offers the following chart settings, which can be adjusted in the menu above the chart:

- **Chart type**: The type of visualization that you want to use. Options include Stacked bar and Stacked area.

### Time comparison

You can compare the current time period to a previous time period. If you select an option in this menu, every data point receives a similarly colored dotted-lined counterpart. This counterpart represents that same metric in the selected previous date range. Setting this option doubles the number of items on the chart and rows in the table.

Available time comparison options include the previous period, 13 weeks prior, 52 weeks prior, and a Customized date range. If you select Customized date range, additional options appear to let you select the number and granularity. If you select None, the date comparison is removed.

### Date range

The desired date range for your analysis. There are two components to this setting:

- **Interval**: The date granularity that you want to view trended data by. Valid options include Hourly, Daily, Weekly, Monthly, and Quarterly. The same date range can have different intervals, which affect the number of data points in the chart and the number of columns in the table. For example, viewing an analysis spanning three days with daily granularity would show only three data points, while an analysis spanning three days with hourly granularity would show 72 data points.
- **Date**: The starting and ending date. Rolling date range presets and previously saved custom ranges are available for your convenience, or you can use the calendar selector to choose a fixed date range.

recommendation-more-help
