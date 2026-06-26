---
title: "Net growth analysis net-growth"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/net-growth"
category: "guides"
topic: "analytics-platform/using/guided-analysis/net-growth"
created_at: "2026-06-23T20:44:03.578310+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Net growth analysis net-growth

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- User

The **Net growth** analysis provides insights around the rate at which you gain or lose users over a specific period. The horizontal axis is a time interval, while the vertical axis is the measurement of growth.

Each data point represents net growth, which is calculated using the following formula:

([New users] + [Return users]) / [Dormant users]

The result of this formula is a ratio. A net growth of 1 represents an equilibrium; the product gained the same number of users it lost. A net growth greater than 1 represents positive growth; there were more new + return users than dormant users. Likewise, a net growth less than 1 represents a loss; there were more dormant users than new + return users.

Similar to the [Active](/en/docs/analytics-platform/using/guided-analysis/active-growth) analysis, users are defined as the following:

- **New**: The user was active during the current period, but not previously. See how far the analysis looks back to determine a new user by hovering over ‘New users’ in the chart legend. The lookback range is dynamically determined based on the selected date range and interval.
- **Return**: The user was active in the current period and not active in the immediately previous period, but were formerly active at some point. See how far the analysis looks back to determine a return user by hovering over ‘Return users’ in the chart legend. The lookback range is dynamically determined based on the selected date range and interval.
- **Dormant**: The user was active in the immediately previous period, but is not active in the current period. Dormant users do not count toward the total number of active users.

NOTE
Repeat users are not factored into this calculation, as they do not represent any gain or loss of users.
https://video.tv.adobe.com/v/3421664/?quality=12&learn=on
## Use cases

Use cases for this analysis include:

- **Performance evaluation**: Allows you to assess the overall performance of your product in terms of acquiring new users. By tracking growth trends, you can better understand if your product is attracting and retaining users at a desired pace.
- **User acquisition analysis**: Allows you to assess the effectiveness of your user acquisition strategies. Analyzing the sources of user growth, such as search engines, campaigns, or other marketing channels, allows you to identify the most significant sources of growth so you can allocate resources accordingly.
- **Churn analysis**: Net growth includes attrition in its formula (dormant users). You can assess the overall health of your user base over time. If net growth is consistently below 1, it indicates a high amount of attrition which could prompt implementing retention strategies.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- View : Switch between this analysis and Active growth .
- Events : The event that you want to measure. Since this analysis is user-based, a user who interacts with the event once within the period is counted as an active user. You can include one event in a query.
- Counted as : The counting method that you want to apply to the selected events. Options include Number of users and Percentage of users. [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} Additional B2B options are available for Customer Journey Analytics B2B Edition: Global accounts, Accounts, Buying groups, Opportunities, Percentage of global accounts, Percentage of accounts, Percentage of buying groups, and Percentage of opportunities.
- Segments : The segment that you want to measure. You can include one segment in a query.

### Time comparison

You can compare the current time period to a previous time period. If you select an option in this menu, every data point receives a similarly colored dotted-lined counterpart. This counterpart represents that same metric in the selected previous date range. Setting this option doubles the number of items on the chart and rows in the table.

Available time comparison options include the previous period, 13 weeks prior, 52 weeks prior, and a Customized date range. If you select Customized date range, additional options appear to let you select the number and granularity. If you select None, the date comparison is removed.

### Date range

The desired date range for your analysis. There are two components to this setting:

- **Interval**: The date granularity that you want to view trended data by. Valid options include Hourly, Daily, Weekly, Monthly, and Quarterly. The same date range can have different intervals which affect the number of data points in the chart and the number of columns in the table. For example, viewing an analysis spanning three days with daily granularity would show only three data points, while an analysis spanning three days with hourly granularity would show 72 data points.
- **Date**: The starting and ending date. Rolling date range presets and previously saved custom ranges are available for your convenience, or you can use the calendar selector to choose a fixed date range.

recommendation-more-help
