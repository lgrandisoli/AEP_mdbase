---
title: "Cohort table overview cohort-table-overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/cohort-table/cohort-analysis"
category: "overview"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:20.730729+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Cohort table overview cohort-table-overview

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
*This article documents the Cohort table in* *Customer Journey Analytics .**See Cohort table for the* *Adobe Analytics version of this article.*

style
shade-box
A *cohort* is a group of people sharing common characteristics over a specified period. A **Cohort table** visualization is useful, for example, when you want to learn how a cohort engages with a brand. You can easily spot changes in trends, then respond accordingly. (Explanations of Cohort Analysis are available on the web, such as at [Cohort Analysis 101](https://en.wikipedia.org/wiki/Cohort_analysis).)

After creating a cohort report, you can curate its components (specific dimensions, metrics, and segments), then share the cohort report with anyone. See [Curate and Share](/en/docs/analytics-platform/using/cja-workspace/curate-share/curate).

Examples of what you can do with a Cohort table:

- Launch campaigns designed to spur a desired action.
- Shift marketing budget at exactly the right time in the customer lifecycle.
- Recognize when to end a trial or an offer to maximize value.
- Gain ideas for A/B testing in areas such as pricing, upgrade path, and so on.

Cohort table is available for all Customer Journey Analytics customers with access rights to Analysis Workspace.

See [Cohort analysis in Analysis Workspace](/en/docs/analytics-learn/tutorials/analysis-workspace/cohort-analysis/cohort-analysis-workspace#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
IMPORTANT
Cohort Analysis does not support non-segmentable metrics (including calculated metrics), non-integer metrics (such as Revenue), or Occurrences. Only metrics that can be used in segments can be used in Cohort Analysis, and they can only be incremented 1 at a time.
Cohort tables in Customer Journey Analytics support double-based (or any numeric-based) metric. For example, Purchase.Value (a double) can be used as an Inclusion/Return Metric. In addition, all metrics that are passed into Adobe Experience Platform via the Analytics Source Connector are also doubles.

## Cohort table capabilities

The following sections describe Cohort Analysis features that allow for fine-tuned control over the cohorts you are building.

For more detailed information about creating a cohort and running a Cohort Analysis report, see [Configure a Cohort table](/en/docs/analytics-platform/using/cja-workspace/visualizations/cohort-table/t-cohort).

### Retention table

A Retention cohort table returns persons: each data cell shows the raw number and percentage of persons in the cohort who did the action during that time period. You can include up to 3 metrics and up to 10 segments.

### Churn table

A Churn cohort table is the inverse of a retention table and shows the persons who fell out or never met the return criteria for your cohort over time. You can include up to 3 metrics and up to 10 segments.

### Rolling calculation

You can calculate retention or churn based on the previous column, not the included column, which is referred to as rolling calculation.

### Latency table

A latency table measures the time that has elapsed before and after the inclusion event occurred. Measuring latency is an excellent tool for pre- and post analysis. The **Included** column is in the center of the table and time periods before and after the inclusion event are shown on both sides.

### Custom dimension cohort

You can create cohorts based on a selected dimension, and not time-based cohorts (which are the default). Use dimensions such as City geo, Marketing channel, campaign, product, page, region, or any other dimension to show how retention changes. Based on the different values of these dimensions.

Related Articles
Configure a Cohort table
.
recommendation-more-help
