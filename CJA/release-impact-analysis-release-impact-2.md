---
title: "Release impact analysis release-impact"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/impact/release"
category: "guides"
topic: "analytics-platform/using/guided-analysis/impact"
created_at: "2026-06-02T19:09:25.086309+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Release impact analysis release-impact

Last update: May 13, 2026
- Topics:
- [Adobe Product Analytics](#)
- [Guided Analysis](#)

CREATED FOR:

- User

The **Release impact** analysis shows a comparison of how key indicators performed before and after a given date. The horizontal axis of this report is a time interval, while the vertical axis measures the desired key indicators. A vertical bar in the middle of the chart represents the date that you want to compare before and after. This date typically represents a notable change to the product that you want to measure against, such as an update to the product or a campaign launch.

https://experienceleague.adobe.com/en/docs/customer-journey-analytics-learn/tutorials/guided-analysis/release-impact
## Use cases

Use cases for this analysis include:

- **Overall performance evaluation:** Comparing overall key indicators, such as engagement measures, can help you determine if a given release was overall successful.
- **Monitoring**: Track vital metrics that you would expect to remain flat when changes are made, such as load time or number of logins. Use this analysis to compare them before and after a release to ensure that it didn’t have any unintended consequences.
- **Feature adoption**: If a product update is focused on improving a certain feature, you can use this analysis to directly compare that feature’s usage before and after the product update.
- **Bug detection**: Tracking the number of errors before and after a release can provide an early indicator of customer issues. If you notice an increase of errors immediately following a release, you can work with engineering or development teams to identify and correct the issue, preventing further impact to customers.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- **View**: Switch between this analysis and [First use impact](/en/docs/analytics-platform/using/guided-analysis/first-use-impact).
- **Key indicators**: The events that you want to measure per user. Each selected key indicator is represented as a colored line. A row representing the event is added to the table. You can include up to three events.
- **Counted as**: The counting method that you want to apply to the selected events. Options include Events per user, Percentage of users, Events, Sessions, and Users.
- **Factors**: The date that you want to compare before and after.
- **Segments**: The segment that you want to measure. The selected segment filters your data to focus only on the individuals who match your segment criteria.

### Chart settings

The Release impact analysis offers the following chart settings, which can be adjusted in the menu above the chart:

- **Chart type**: The type of visualization that you want to use. Options include Line and Bar.

### Date range

Date selection in Impact analysis operates differently than other analyses, since the report revolves around the date specified in the query rail. The following options are available:

- **Interval**: The date granularity that you want to view trended data by. Valid options include Daily, Weekly, Monthly, and Quarterly. Changing the interval affects the options available for the Before and after period.
- **Before and after period**: The amount of time to analyze before and after the date specified in the query rail. Available options depend on the Interval selection.

recommendation-more-help
