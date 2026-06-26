---
title: "Funnel analysis funnel"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/guided-analysis/funnel/friction"
category: "guides"
topic: "analytics-platform/using/guided-analysis/funnel"
created_at: "2026-06-23T20:46:02.722256+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Funnel analysis funnel

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- User

The **Funnel** analysis provides a visual representation of a critical user journey in your product. The horizontal axis represents each step that a user must pass through. The vertical axis represents the percentage of users or sessions at each step. All steps must be done in eventual order, but can happen at any time within the reporting window.

https://video.tv.adobe.com/v/3421663/?quality=12&learn=on
## Use cases

Use cases for this analysis include:

- **Conversion analysis**: You can analyze conversions at each stage of the funnel, such as a retail checkout, account sign-up, subscription flow, or some other critical journey within your product experience. By tracking the number of users who progress from one step to the next, you can identify bottlenecks that have unusual or undesired conversion rates. This information is valuable to understand where you can improve your product journey for immediate results.
- **Experimentation analysis**: You can compare conversion rates across a funnel that has optional steps or steps where an A/B experiment is being run. This information can help you determine which variation of the funnel leads to the highest conversion rate so that you can encourage more users down that path.
- **Onboarding optimization**: Optimize your product’s onboarding process by examining user behavior around key events. You can identify which steps that users struggle with or fail to complete.
- **Feature adoption and engagement**: Understand how users interact with specific features in your product. Analyzing the progression of users through feature-related steps lets you see adoption rates and identify areas where users might underuse certain features. You can then use this information to focus on feature improvements to increase adoption rates.
- **Marketing channel effectiveness**: Measure the effectiveness of marketing channels. You can create a segment that focuses on users that interacted with different marketing channels, such as paid search, display, natural search, or direct. You can then compare their journeys to see which channel leads to the best product outcomes.

## Interface

See [Interface](/en/docs/analytics-platform/using/guided-analysis/overview#interface) for an overview of the Guided analysis interface. The following settings are specific to this analysis:

### Query rail

The query rail allows you to configure the following components:

- View : Switch between this analysis and Conversion trends .
- Steps : The event touchpoints that you want to track. Each bar in the chart represents a step. You can include up to ten steps. Compare: Each step provides an option to compare multiple events in a single funnel step, creating a “forked funnel.” This feature allows you to compare the friction of two journeys side-by-side without creating two separate analyses. It is useful when there are step options or an A/B experiment is being run within the funnel. See Funnel in Customer Journey Analytics tutorials for a video that explains how to compare funnels.
- Counted as : The scope that you want applied to the funnel. Options include Sessions and Users. Sessions: All steps must happen within the same session to be counted. Users: All steps must happen within the selected reporting window to be counted.
- Segments : The segments that you want to compare the funnel across. Each segment selected splits each step into multiple bars. Each color represents a different segment. You can include up to three segments.

### Chart settings

The Funnel analysis offers the following chart settings, which can be adjusted in the menu above the chart:

- **Chart type**: The type of visualization that you want to use. Options include Steps.
- **Conversion from**: Determines the percentage calculation from step to step. Options include calculating conversion from the First step or Previous step.

### Time comparison

You can compare the current time period to a previous time period. If you select an option in this menu, every data point receives a similarly colored dotted-lined counterpart. This counterpart represents that same metric in the selected previous date range. Setting this option doubles the number of items on the chart and rows in the table.

Available time comparison options include the previous period, 13 weeks prior, 52 weeks prior, and a Customized date range. If you select Customized date range, additional options appear to let you select the number and granularity. If you select None, the date comparison is removed.

### Date range

The desired date range for your analysis. There are two components to this setting:

- **Interval**: The date granularity that you want to view trended data by. This setting does not impact non-trended analyses such as [Funnel](/en/docs/analytics-platform/using/guided-analysis/funnel).
- **Date**: The starting and ending date. Rolling date range presets and previously saved custom ranges are available for your convenience, or you can use the calendar selector to choose a fixed date range.

recommendation-more-help
