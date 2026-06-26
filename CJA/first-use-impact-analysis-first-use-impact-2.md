---
title: "First use impact analysis first-use-impact"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/impact/first-use"
category: "guides"
topic: "analytics-platform/using/guided-analysis/impact"
created_at: "2026-06-02T19:09:23.311054+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# First use impact analysis first-use-impact

Last update: May 13, 2026
- Topics:
- [Adobe Product Analytics](#)
- [Guided Analysis](#)

CREATED FOR:

- User

The **First use impact** analysis shows a comparison of how key indicators performed before and after a user uses a product feature for the first time. The horizontal axis of this report is a relative time interval before and after the event, while the vertical axis measures the desired key indicators. A vertical bar in the middle of the chart represents day 0 for when a feature is first used by a given user. Because users do not always adopt features on the same day and your rollouts can potentially happen over several days, day 0 can mean something different for each individual user.

https://experienceleague.adobe.com/en/docs/customer-journey-analytics-learn/tutorials/guided-analysis/first-use-impact
## Use cases

Use cases for this analysis include:

- New feature analysis : If you’re launching a new feature within your product, you can compare how key indicators performed before and after users were exposed to that new feature for the first time.
- Phased rollouts : Because the analysis looks for first use of the feature rather than a fixed date, this analysis is helpful if you phase the rollout of your features over time.
- New product version analysis : If you’re launching a new version of your product, you can compare how key indicators performed before and after users were exposed to that new version for the first time. Select “any event” as your first-use event and filter it to your Version number property.
- Existing feature improvements : If you’re making improvements to an existing feature within your product, you can compare how key indicators performed before and after users were exposed to those new improvements for the first time. You can accomplish this analysis in one or more ways depending on your feature instrumentation. Select an event that represents the improvement as your first-use event Select the date when the changes started to roll out Segment the analysis to the group of people exposed to the improvements
- Campaign effectiveness : When a user clicks through from a given campaign, you can compare how key indicators performed before and after the user interacted with that campaign.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- View : Switch between this analysis and Release .
- Key indicators : The events that you want to measure per user. Each selected key indicator is represented as a colored line. A row representing the event is added to the table. You can include up to three events.
- Counted as : The counting method that you want to apply to the selected events. Options include Events per user, Events, Sessions, and Users.
- Factors : There are two factors for this analysis: Date : How far back you want to start looking for the first time use event to have occurred. Event : The event that you want to look for first use of, to center the analysis on.
- Segments : The segment that you want to measure. The selected segment filters your data to focus only on the individuals who match your segment criteria. A single segment is supported for this analysis.

### Chart settings

The First use impact analysis offers the following chart settings, which can be adjusted in the menu above the chart:

- **Chart type**: The type of visualization that you want to use. Options include Line.

### Date range

Date selections in the First use impact analysis operates differently than other analyses, since the analysis revolves around the date specified in the query rail. The following options are available:

- **Interval**: The date granularity that you want to view trended data by. Valid options include Daily, Weekly, Monthly, and Quarterly. Changing the interval affects the options available for the Before and after period.
- **Before and after period**: The amount of time to analyze before and after the first use event specified in the query rail. Available options depend on the Interval selection.

recommendation-more-help
