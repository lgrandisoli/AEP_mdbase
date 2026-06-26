---
title: "Incremental query incremental-query"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/incremental-query"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:33.971846+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Incremental query incremental-query

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

- Topics:
- [Campaigns](#)

CREATED FOR:

- Intermediate
- User

The **Incremental query** activity is a **Targeting** activity that runs a database query each time the Orchestrated campaign runs. The important part is that it only ever outputs **new** records. Anyone already picked up in a prior run is excluded, so you avoid re-targeting the same people or re-exporting the same rows.

Use it when the campaign can run multiple times, or example, when you schedule the campaign, e.g. weekly or when it is triggered by an external signal or API. Each run targets only records that were not returned in a previous run, so you avoid duplicates.

Typical uses:

- **Messaging and audiences**: Pull only new sign-ups, new purchasers, or other “new since last run” segments into the next step (e.g. email, SMS).
- **Ongoing exports**: Send only new or updated rows to files for reporting or BI tools, without duplicating what you already exported.

When a run returns no rows, the Orchestrated campaign stops at the **Incremental query**. Activities after the Incremental query are not executed until there is data, when the campaign runs again.

## Configure the Incremental query activity incremental-query-configuration

Set the targeting dimension, build your query, and choose how the activity decides which records to exclude from future runs.

- Drop an Incremental query activity into your Orchestrated campaign.
- In Audience , pick the Targeting dimension , e.g. recipients, subscribers, and click Continue . Learn more on Targeting dimensions .
- Click Add condition to define the query. Learn how to use the rule builder .
- Under Processed data , choose your Path to the date field . The attribute must use the Date Time format. Each run returns only rows whose date is after the last execution.

## Example incremental-query-example

The following example sends a welcome email to profiles who have just become gold members. The campaign can be scheduled to run weekly, every Monday. Each run targets only profiles that qualified for gold membership since the previous run, so each recipient receives the welcome email once.

- **Incremental query**: Selects gold members. First run: all current gold members. Later runs: only profiles that became gold members since the previous execution.
- **Email delivery**: Sends the welcome email to the profiles output by the query.

recommendation-more-help
