---
title: "License usage dashboard license-usage"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:10.370107+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# License usage dashboard license-usage

Last update: May 8, 2026
- Topics:
- [Audiences](#)
- [Profiles](#)

CREATED FOR:

- Beginner
- User

The Adobe Journey Optimizer [user interface](/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface) provides a dashboard that displays important information about your organization’s license usage, as captured during a daily snapshot.

To access this dashboard, go to **Administration** > **License Usage**. This opens the **Overview** tab, which displays the dashboard.

NOTE
- To view the dashboard, you must have the View License Usage Dashboard permission.
- Certain metrics (e.g., compute hours, emails) are not displayed for development sandboxes, as indicated by N/A in the quota column. Only non-null values are displayed in the dashboard: when metrics are zero or close to zero, they are not populated.

For Adobe Journey Optimizer, the dashboard allows you to check the number of **Engageable Profiles**.

## What is an engageable profile? what-is-engageable-profile

An **Engageable Profile** is a record of information representing an individual that is stored in the Profile Service and has been engaged by journeys or campaigns.

Key characteristics of Engageable Profiles:

- 12-month rolling window : Engageable Profiles are counted based on engagement over the past 12 months. This metric shows the number of unique profiles that you have attempted to engage with using Journey Optimizer’s authoring, decisioning, delivery, experimentation, or orchestration capabilities.
- Unique count per sandbox : If a profile enters multiple journeys or campaigns within a sandbox, it is counted only once as a single Engageable Profile for that sandbox.
- Based on Addressable Audience : Engageable Profiles are calculated from your Addressable Audience. The count represents the audience engaged in the past 12 months using any of Journey Optimizer’s capabilities, out of your total Addressable Audience.
- Metric behavior : The Engageable Profiles count: Can increase when new profiles are engaged through journeys or campaigns Cannot decrease unless there is no engagement with certain profiles for over 12 months Can decrease when pseudonymous profiles are stitched to known profiles

NOTE
If you observe a sudden spike in your Engageable Profiles count, refer to the
Troubleshooting section
below for detailed guidance on understanding and resolving the issue.
## Troubleshooting: significant increase in engageable profiles count troubleshooting-engageable-profiles

If you observe a sudden spike in the Engageable Profiles count (for example, profiles increasing from hundreds of thousands to millions within a day), this section provides guidance to understand and address the issue.

### Understanding the increase

The Engageable Profiles metric reflects the number of unique profiles engaged by journeys or campaigns over the past 12 months. A sudden increase may result from:

- Large audiences being targeted by new journeys or campaigns
- Changes in datasets enabled for Profile Service
- Batch processing of audiences that haven’t been engaged recently

### Resolution steps

To address this issue, follow these steps:

- Understand profile counting logic: Engageable Profiles are calculated based on unique profiles engaged by journeys or campaigns over the past 12 months. If a profile enters multiple journeys, it is counted as one Engageable Profile for that sandbox. The metric cannot decrease unless there is no engagement with certain profiles for over 12 months or if pseudonymous profiles are stitched to known ones. Engageable Profiles are calculated using a customer’s Addressable Audience. The audience engaged in the past 12 months using any of the Journey Optimizer’s capabilities, out of the total Addressable Audience, determines the count of Engageable Profiles.
- Investigate journeys, campaigns and decisioning targeting large audiences: Review recent journeys and campaigns targeting large numbers of profiles using Engageable Profiles queries or Query Service . Identify specific journey versions that contributed to the spike in profile counts. Journeys, Campaigns and Decisioning involving new profiles are likely to lead to an increase in event counts in the Journeys datasets, contributing to the rise in the Engageable Profiles count.
- Filter audiences at journey and campaigns level: Apply filters at the audience level before initiating journeys or campaigns to prevent unnecessary increases in Engageable Profiles. Ensure only relevant audiences are targeted during engagements.
- Reduce addressable audience size: Delete pseudonymous profiles if necessary. Note that this action affects both Journey Optimizer and Real-Time Customer Data Platform. Learn more about Pseudonymous Profile data expiration in Real-Time Customer Profile Guide. Note: Pseudonymous Profile data expiration cannot be configured through the Platform UI or APIs. You must contact support to enable this feature.
- Monitor dataset changes: Verify datasets enabled for profiling and ensure they do not contain excessive ECIDs (Experience Cloud IDs). If needed, delete datasets with high ECID counts and recreate them with reduced records.
- Develop a long-term reduction strategy: The Engageable Profiles count will naturally decrease if certain profiles remain unengaged for more than 12 months.

**See also:**

- [Engageable Profiles query examples](/en/docs/journey-optimizer/using/reporting/reports/query-examples#engageable-profiles-queries) - Sample queries to monitor and analyze your Engageable Profiles
- [Adobe Experience Platform Query Service overview](/en/docs/experience-platform/query/home#_blank)

## Related documentation related-documentation

Learn more in the Adobe Experience Platform documentation:

- [License usage dashboard overview](/en/docs/experience-platform/dashboards/guides/license-usage#_blank)
- [Exploring the license usage dashboard](/en/docs/experience-platform/dashboards/guides/license-usage#exploring-the-license-usage-dashboard#_blank)
- [Available metrics](/en/docs/experience-platform/dashboards/guides/license-usage#available-metrics#_blank)
- [Pseudonymous Profile data expiration](/en/docs/experience-platform/profile/pseudonymous-profiles#_blank)

recommendation-more-help
