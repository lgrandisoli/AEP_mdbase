---
title: "Current Customer Journey Analytics release notes (May 2026)"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/releases/latest"
category: "release-notes"
topic: "analytics-platform/using/releases/latest"
created_at: "2026-06-02T19:04:59.682784+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Current Customer Journey Analytics release notes (May 2026)

Last update: May 13, 2026
- Topics:
- [Release Notes](#)

CREATED FOR:

- User
- Admin

**Last update**: May 13 , 2026

These release notes cover the May 2026 release period. Adobe Customer Journey Analytics releases operate on a [continuous delivery model](/en/docs/analytics-platform/using/releases/releases), which allows for a more scalable, phased approach to feature deployment. Accordingly, these release notes get updated several times a month. Please check them regularly.

## New or updated features

Feature and description
Rollout starts
General Availability
**CJA API Postman Collections**A downloadable Postman collection is available for calling CJA API endpoints.

For more information, see the [analytics-cja-postman-collections Github repository](https://github.com/AdobeDocs/analytics-cja-postman-collections).

May 1, 2026
**MCP servers for Customer Journey Analytics**The Analytics MCP (Model Context Protocol) servers allow you to connect a supported MCP client to Adobe Customer Journey Analytics. Once connected, your MCP client can invoke product-specific tools to retrieve data, run queries, or perform supported operations as part of an LLM or agentic workflow. For more information, see [Analytics MCP servers](https://developer.adobe.com/analytics-mcp/docs/).

If you used these MCP servers during the beta period, please note that there are different URLs between beta and production endpoints. Ensure that any agentic workflows created during the beta period are updated to use the production endpoints before May 31.

May 5, 2026
**Content Analytics support for native mobile app experiences**Organizations can extend their content performance analysis to iOS and Android apps, capturing image assets and granular experience elements to understand which in-app content drives user engagement and business outcomes.

[Documentation](/en/docs/analytics-platform/using/content-analytics/content-analytics) is updated to describe the mobile channel capabilities and configuration. Information about the [Content Analytics Mobile SDK extension](https://developer.adobe.com/client-sdks/solution/adobe-content-analytics/) is available on [Adobe Developer](https://developer.adobe.com/).

Insights are available for all Adobe Content Analytics customers.

May 6, 2026
**Journey canvas enhancements**The following enhancements are available in Journey canvas visualizations:

- [Exclude nodes](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/configure-journey-canvas#exclude-nodes) from a journey.
- Use a node’s fallout data to [create segments](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/configure-journey-canvas#create-a-segment-based-on-a-node-or-arrow), [trends](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/configure-journey-canvas#view-trend-data), [audiences](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/configure-journey-canvas#create-an-audience), and [breakdowns](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/configure-journey-canvas#apply-a-breakdown).

May 18, 2026
**Data validation in the Adobe Engineering Agent**New data validation skills are available within the Data Engineering Agent. These skills help teams quickly assess data quality directly in Adobe Experience Platform, before the data is analyzed in Customer Journey Analytics.

Data validation skills enable on‑demand, field‑level, and dataset‑level validation, combining statistical summaries with intelligent detection of invalid or anomalous values.

Using data validation skills reduces manual QA effort and accelerates trusted data onboarding and transformations across data engineering workflows.

(Documentation link to follow.)For more information, see [Data Engineering Agent]() (will be in this repo: https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/cja-data-insights-agent).

May 19, 2026

(Originally planned to release on March 31, 2026)

Content Analytics: Line visualization thumbnails and previews
Thumbnails and previews
are now available for assets and experiences in line visualizations for Content Analytics.
May 20, 2026
**Streaming media services: Support schedule data**You can now upload schedule data of past live Streaming Media content to more easily and accurately track viewership.

The following are examples of live content that are supported with schedule data upload:

- FAST (Free Ad Supported TV) platforms
- Local streams
- Live sports

Uploading schedule data allows you to track viewership data for individual programs that ran during the time you designate in the upload file. You can even gather viewership data for specific topics or program segments.

These capabilities are available regardless of how you implemented Streaming Media Collection.

Previously, it was difficult to accurately tie a given session to specific programs when analyzing live content, and it wasn’t possible to tie a given session to individual topics or program segments.

For more information, see [Upload schedule data to track live content](/en/docs/media-analytics/using/media-use-cases/track-schedule-data)

October 29, 2025
First half of 2026

(Originally planned to release on October 29, 2025)

## Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-446522, AN-445779, AN-445759, AN-444676, AN-442813, AN-441943, AN-441717, AN-441538, AN-441123, AN-440976, AN-440952, AN-440919, AN-439797, AN-434855, AN-429777, AN-429048, AN-428892, AN-428189, AN-425215**Components**:**Connections**: AN-449652, AN-444560, AN-442824, AN-440937, AN-440092, AN-439823, AN-429781**Content Analytics**:**Guided analysis**:**Exports**: AN-438953, AN-437115**Data views**: AN-442809**Implementation**:**Report Builder**: AN-448697, AN-447128, AN-441148, AN-441136, AN-438147, AN-425150**Reporting**: AN-445123, AN-442231, AN-442169, AN-441811, AN-441733, AN-440505, AN-440300, AN-434824, AN-434210, AN-424000, AN-423359, AN-406242**Segmentation**:**Scheduled reports**:**Shared metrics and dimensions**:**Other**: AN-449159, AN-444661, AN-443900, AN-397985

## Related resources

- [Previous Customer Journey Analytics release notes for 2025](/en/docs/analytics-platform/using/releases/2025)
- [Adobe Analytics release notes](/en/docs/analytics/release-notes/latest)
- [Streaming Media Collection release notes](/en/docs/media-analytics/using/release-notes/release-notes)
- [CX Enterprise release notes](/en/docs/release-notes/experience-cloud/current)
- [Customer Journey Analytics documentation updates](/en/docs/analytics-platform/using/releases/doc-changes)

recommendation-more-help
