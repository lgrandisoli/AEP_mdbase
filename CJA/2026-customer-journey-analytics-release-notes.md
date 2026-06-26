---
title: "2026 Customer Journey Analytics Release Notes"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/releases/2026"
category: "release-notes"
topic: "analytics-platform/using/releases/2026"
created_at: "2026-06-23T20:44:40.536896+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# 2026 Customer Journey Analytics Release Notes

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)
- [Administration](#)

CREATED FOR:

- Admin
- User

Learn about the latest release updates for [Adobe CX Enterprise products](https://business.adobe.com/products/adobe-experience-cloud-products.html). Get the latest self-help documentation, tutorials, and courses on Experience League.

## May 2026

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

### Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-446522, AN-445779, AN-445759, AN-444676, AN-442813, AN-441943, AN-441717, AN-441538, AN-441123, AN-440976, AN-440952, AN-440919, AN-439797, AN-434855, AN-429777, AN-429048, AN-428892, AN-428189, AN-425215**Connections**: AN-449652, AN-444560, AN-442824, AN-440937, AN-440092, AN-439823, AN-429781**Exports**: AN-438953, AN-437115**Data views**: AN-442809**Report Builder**: AN-448697, AN-447128, AN-441148, AN-441136, AN-438147, AN-425150**Reporting**: AN-445123, AN-442231, AN-442169, AN-441811, AN-441733, AN-440505, AN-440300, AN-434824, AN-434210, AN-424000, AN-423359, AN-406242**Other**: AN-449159, AN-444661, AN-443900, AN-397985

## April 2026 apr26

Feature and description
Rollout starts
General Availability
**Italian language support**The Italian locale (it-IT) is now supported in Analysis Workspace in Customer Journey Analytics.

Customer Journey Analytics supports all languages that are supported in the Experience Platform UI, as described in [Browser and language support for the Experience Platform UI](/en/docs/experience-platform/landing/platform-ui/browser-language-support#language-support).

You can [change your default language](/en/docs/experience-platform/landing/platform-ui/browser-language-support#change-default-language) in Experience Platform.

April 8, 2026
### Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-442813, AN-442410, AN-442231, AN-441943, AN-441717, AN-434855, AN-429777, AN-429048, AN-428892, AN-428189, AN-425215**Connections**: AN-442824, AN-440937, AN-440092, AN-429781**Data views**: AN-442809, AN-434824, AN-434210, AN-424000**Report Builder**: AN-441136, AN-438147, AN-425150**Reporting**: AN-443900, AN-441811, AN-441506, AN-440919, AN-440545, AN-440505, AN-440300**Other**: AN-423359, AN-406242, AN-397985

## March 2026 mar26

Feature and description
Rollout starts
General Availability
**Include multiple dimension columns in a freeform table**You can now include up to 5 dimension columns in a freeform table, allowing you to view multiple dimension items side by side. Each row of dimension items behaves like a single concatenated dimension item.

You can apply filters, sorting, breakdowns, and more to freeform tables with multiple dimension columns to create a deeper and more custom analysis.

Previously, you could include only 1 dimension column in a freeform table.

For more information, see [Include multiple dimension columns in a freeform table](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table-multidimensions).

January 28, 2026
March 4, 2026

(Originally planned for February 18, 2026)

**Sort tables by multiple columns**You can now sort the data of a freeform table by multiple columns in Analysis Workspace, whether they are dimensions or metrics.

When you sort data for multiple columns, data is sorted according to the priority you assign to each column. Priority numbering is displayed next to the sort icon.

For more information, see [Filter and sort freeform tables](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/filter-and-sort).

January 28, 2026
March 4, 2026

(Originally planned for February 18, 2026)

Content Analytics: Scatter visualization thumbnails and previews
Thumbnails and previews
are available for assets and experiences in scatter visualizations for Content Analytics.
February 17, 2026
March 2, 2026
Content Analytics: Bar visualization thumbnails and previews
Thumbnails and previews
are available for assets and experiences in bar (stacked) and horizontal bar (stacked) visualizations for Content Analytics.
February 23, 2026
March 9, 2026
**Report Builder: Administrator visibility to all scheduled workbooks**The Report Builder Excel Add-in includes a new filter option that allows administrators to see all scheduled workbooks for a given org, regardless of who scheduled them. This filter option is available only for Analytics administrators. It is available on both the Workbook tab and the Legacy tab when viewing scheduled workbooks.

The ability to view all scheduled workbooks is especially useful when migrating workbooks across distributed teams, because it allows administrators to easily locate all legacy workbooks prior to migrating them.

Previously, administrators could see only the workbooks they scheduled, not those scheduled by other users.For more information, see [Manage scheduled workbooks](/en/docs/analytics-platform/using/cja-reportbuilder/manage-schedules-reportbuilder).

March 10, 2026
**Update to the Approximate Count Distinct function**The HLL probabilistic algorithm used in the Approximate Count Distinct function will soon be updated. The resulting output for numbers utilizing this function might change slightly from historical numbers, as follows:

- When counting very small amounts of unique values, the results will be improved to use exact counts rather than using estimates.
- When counting anything larger, count estimates will retain the same accuracy as prior to this update (estimates are accurate within 5 percent of the exact number, 95 percent of the time).

For more information about the Approximate Count Distinct function, see [Approximate Count Distinct](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-adv-functions#approximate-count-distinct) in [Advanced functions](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-adv-functions)

March 10, 2026
**Full table export improvements**Full table export includes the following enhancements:

Export creation and configuration enhancements

- Create an export from the Exports page. Previously, you could only create an export from Analysis Workspace by right-clicking the table.
- Add a new account or location when creating an export.
- Automate file name creation and folder placement of exported files. This allows file names to be predictable and organized into folders in a logical way. Previously, file names were unpredictable and grouped into a single folder.
- Support for exporting data as Parquet files for improved data warehouse compatibility. Previously, only CSV and JSON were supported.

Export management enhancements

- Renew or cancel one or more exports from the Exports page.
- Resend one or more exports from the Logs page.
- Email individual users or groups when an export fails or is about to expire.
- More precise error messages for failed exports.

Calculated metric, segment, and dimension enhancements

- Support for more calculated metric functions. Previously, only simple math functions were supported.
- Apply segments when creating an export.
- Support for double-data type dimensions for improved precision.

Administrative enhancements

- Administrators can now view all exports and logs, regardless of who created them.

For more information, see the following resources:

- [Export full tables to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud)
- [Configure cloud export accounts](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-accounts)
- [Configure cloud export locations](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-locations)
- [Manage exports](/en/docs/analytics-platform/using/cja-components/exports/manage-exports)
- [Manage cloud export locations and accounts](/en/docs/analytics-platform/using/cja-components/exports/manage-export-locations)
- [Manage export logs](/en/docs/analytics-platform/using/cja-components/exports/manage-export-logs)

February 25, 2026
March 11, 2026

(Originally planned for March 4, 2026)

**Hands-on tutorial for Analysis Workspace**A new hands-on tutorial is now available to guide new users through the basics of using panels, visualizations, and components in Analysis Workspace.

For more information, see [Customer Journey Analytics landing page](/en/docs/analytics-platform/using/cja-overview/cja-b2c-overview/landing).

March 18, 2026
**Fallout visualization improvements**The Fallout visualization includes the following enhancements:

- An improved drag-and-drop experience.Simply hover over a touchpoint and drag it to a new location within the visualization.Previously, you had to click the edit icon on the touchpoint before dragging it.
- Clearer language when combining touchpoints using drag-and-drop.When dragging a touchpoint onto another touchpoint, “Combine” text displays, indicating that the two touchpoints are being combined.Previously, “Add” text displayed, regardless of whether the touchpoint was being moved to a new location within the visualization or combined with another touchpoint.
- Redesigned tooltips.The tooltips that display when hovering over a touchpoint are more intuitive and legible.
- A more discoverable context menu.Tooltips include a new “Click to analyze” option, which provides convenient access to the touchpoint’s context menu.Previously, the context menu was available only when right-clicking a touchpoint.

For more information, see [Configure a fallout visualization](/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/configuring-fallout).

March 25, 2026
**Support for data mirror**With support for model-based schemas and change data capture (CDC) functionality for specific source connectors in Experience Platform, Customer Journey Analytics will be able to support [data mirror](/en/docs/analytics-platform/using/cja-data-mirror/data-mirror) functionality of data warehouse solutions like Snowflake, Azure Databricks, and Google BigQuery.

Contact your Adobe Account Team to access the beta.

Beta release: September 24, 2025
March 25, 2026
**Data Insights Agent integration with Copilot**The Data Insights Agent is now integrated with Microsoft Copilot, allowing you to interact with Customer Journey Analytics data using natural language prompts, directly within Microsoft tools, including Teams, Powerpoint, and more.

For more information, see [Adobe Marketing Agent for Microsoft 365 Copilot](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ama-ms).

March 26, 2026
Datasets preview redesign in Connections
When you
add
or
edit
datasets in a person-based connection, the experience to preview data is improved. For stitching enabled datasets, additional
stitching metrics
and
information on bad ids
are available.
March 6, 2026
March 31, 2026
Panel breakdown
The drop zone for a panel now offers the additional feature to
break down
(instead of segment) a panel based on a dimension.
March 31, 2026
March 31, 2026
Multiple dimension API reporting
Report multiple dimensions in a single API request and perform dimension-level searches.
Learn more
March 2026
Multi-column API sorting
Sort multiple dimension and metric objects in an API request. Mix dimensions and metrics in the same sort definition.
Learn more
March 2026
## February 2026 feb26

Feature and description
Rollout starts
General Availability
**Header overrides**

You can specify a header name and secret header value in Content Analytics. This [header overrides configuration](/en/docs/analytics-platform/using/content-analytics/configuration/guided#header-overrides) ensures that Content Analytics sends custom HTTP headers to bypass any bot detection or gate traffic technologies you have implemented.

February 2, 2026
**Combine report suites from multiple IMS orgs**

You can use the Analytics Source Connector to combine report suites from multiple IMS orgs. This [cross-IMS data mapping](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/mapping-data-ims-orgs) feature allows organzations to have a combined view of their customer data, even when that customer data is spread across multiple IMS organizations.

**Note:** This configuration is available only by submitting a request to Adobe Customer Care.

February 12, 2026
### Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-421930, AN-424997, AN-424194, AN-425515, AN-425254, AN-423174, AN-428834, AN-306540, AN-426014, AN-427801**Exports**: AN-422041, AN-421599, AN-422112**Report Builder**: AN-391415, AN-425125**Reporting**: AN-425817, AN-424362, AN-425752, AN-425278, AN-422249, AN-403446, AN-424727, AN-426791, AN-427985**Segmentation**: AN-428905, AN-428232**Scheduled reports**: AN-425484, AN-425137**Other**: AN-428833, AN-425074

## January 2026 jan26

Feature and description
Rollout starts
General Availability
**Analyze audiences from Experience Platform Profile datasets in Customer Journey Analytics**You can now ingest audience membership data from Experience Platform Profile datasets into a Customer Journey Analytics connection. Audiences become available as new dimensions for use in Analysis Workspace.

This is made possible through a new capability in Customer Journey Analytics to ingest XDM object-maps, which makes it possible to ingest Profile AudienceIDs.

Previously, only simple XDM maps could be ingested into Customer Journey Analytics.

In addition to being able to add audience data as dimensions to any project in Analysis Workspace, the following new Workspace templates are also available:

- Audience Analytics Overview
- Consent Policy Overview

For more information, see [Audience analysis overview](/en/docs/analytics-platform/using/cja-connections/audience-analysis/audience-analysis-overview).

October 22, 2025
January 22, 2026
**Data storytelling: Generate slide presentations from Workspace reports**You can now automatically generate a slide presentation (in .pptx format) that is based on an Analysis Workspace report. Workspace detects key insights in your report and converts them into stakeholder-ready slides.

This feature reduces the time and effort required to surface findings, build executive narratives, and communicate business impact.

For more information, see [Data storytelling: Generate slide presentations from Workspace reports](/en/docs/analytics-platform/using/cja-workspace/curate-share/generate-slides).

October 22, 2025
January 28, 2026
**Stitching in connections**The stitching process in Customer Journey Analytics is now more simple. Instead of duplicating a dataset and applying stitching on the duplicated dataset, stitching is now done on the ingestion of data into Customer Journey Analytics, which removes the requirement of duplicated datasets and schemas.

Furthermore, you [initiate stitching yourself through an updated Connections interface](/en/docs/analytics-platform/using/stitching/use-stitching-ui), instead of having to request stitching through Adobe Customer Care.

October 28, 2025
January 30, 2026
### Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-400507, AN-400265, AN-399209, AN-397146, AN-394992, AN-390795**Exports**: AN-399012, AN-388578**Implementation**: AN-397551, AN-397550, AN-397190, AN-396127**Report Builder**: AN-401127, AN-400618, AN-392971, AN-391692

recommendation-more-help
