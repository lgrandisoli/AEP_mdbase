---
title: "Use derived fields to report on goals"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/derived-fields/goals-using-derived-fields"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-23T20:44:27.986480+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use derived fields to report on goals

Last update: June 5, 2026
- Topics:
- [Data management](#)

CREATED FOR:

- Admin
- User

This use case describes how to use the power of derived fields to set goals for a specific dimension and then use these goals in your Workspace project.

If you are not familiar with derived fields, refer to the [tutorial](/en/docs/customer-journey-analytics-learn/tutorials/data-views/derived-fields-in-cja) and [documentation](/en/docs/analytics-platform/using/cja-dataviews/derived-fields) for an introduction.

## Define goals

To define goals, create a new derived field where you explicitly set custom numeric values directly or indirectly using the values resulting from rules earlier in your derived field definition.

### Monthly Gift Certificate Orders Goals

You want to explicitly set goals for your gift certificate orders for four months, ranging from July 2023 - October 2023. To do this:

- Create a new derived field with the name Monthly Gift Certificate Orders Goal (Incremental) .
- Set static values, using a CASE WHEN RULE, for each month, by setting a Custom numeric value . See the Monthly Product Goals rule below.

### Marketing channel revenue goals

You want to set a monthly revenue goal for each of your marketing channels. To do this:

- Create a new derived field, using the Marketing channels function template with the name Monthly Marketing Channel Revenue Goal (Incremental) .
- Define all rules to properly identify each of the marketing channels based on a combination of URL PARSE and CASE WHEN rules. For example:
- Explicitly set static values, representing monthly revenue goals, for the specific marketing channels in a final CASE WHEN rule, by setting a Custom numeric value . See the Monthly Goal rule below.

## Use goals

To use goals in your Workspace project, you use the calculated metric functionality to ‘normalize’ the derived field back to its original static value. This normalization is required as the static values you set for the derived fields defining goals, are incremented with every event.

### Monthly Gift Certificate Orders Goals

- Create a calculated metric field named Monthly Gift Certificate Orders Goal , defined as:
- You can create additional calculated fields, for example % of Monthly Gift Certificate Orders Goal , to show actual progress against goals, for example:

You can use these calculated metrics to report on progress in freeform tables and visualizations. For example:

### Marketing channel revenue goals

- Create a calculated metric field named Marketing Channel Revenue Goal , defined as:
- You can create additional calculated fields, for example % of Marketing Channel Revenue Goal , to show actual progress against goals, for example:

You can use these calculated metrics to report on progress in freeform tables and visualizations. For example:

recommendation-more-help
