---
title: "2025 Customer Journey Analytics Release Notes"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/releases/2025"
category: "release-notes"
topic: "analytics-platform/using/releases/2025"
created_at: "2026-06-02T19:07:44.730356+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# 2025 Customer Journey Analytics Release Notes

Last update: May 13, 2026
- Topics:
- [Release Notes](#)

CREATED FOR:

- User
- Admin

Learn about the latest release updates for [Adobe CX Enterprise products](https://business.adobe.com/products/adobe-experience-cloud-products.html). Get the latest self-help documentation, tutorials, and courses on Experience League.

## October 2025 oct25

Feature
Description
Rollout starts
General Availability
Filter criteria included in line visualizations and sparklines
Any search filter criteria that you apply to a freeform table filter is now always included in sparklines. In addition, you can include search filter criteria in any connected line visualization.

You can configure line visualizations to include search filter criteria by selecting the sparkline in the metric column header of the connected table.

Previously, search filter criteria was not included in sparklines or connected line visualizations.

For more information, see [View trended data for a freeform table](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table-trended-data).

October 15, 2025
Data storytelling: Generate slide presentations from Workspace reports
You can now automatically generate a slide presentation (in .pptx format) that is based on an Analysis Workspace report. Workspace detects key insights in your report and converts them into stakeholder-ready slides.

This feature reduces the time and effort required to surface findings, build executive narratives, and communicate business impact.

For more information, see [Data storytelling: Generate slide presentations from Workspace reports](/en/docs/analytics-platform/using/cja-workspace/curate-share/generate-slides).

October 22, 2025
January 2026
Real-time reporting
Real-time reporting in Customer Journey Analytics
displays and updates data and visualizations within one or more panels in Analysis Workspace in real time.
September 18, 2025 (Originally planned to release on August 15, 2025)
October 22, 2025
Support for data mirror
With support for model-based schemas and change data capture (CDC) functionality for specific source connectors in Experience Platform, Customer Journey Analytics will be able to support [data mirror](/en/docs/analytics-platform/using/cja-data-mirror/data-mirror) functionality of data warehouse solutions like Snowflake, Azure Databricks, and Google BigQuery.

Contact your Adobe Account Team to access the beta.

Beta release: September 24, 2025
TBD
Stitching in connections
Simplifies Customer Journey Analytics stitching. Instead of duplicating a dataset and applying stitching on the duplicated dataset, stitching is now done on the ingestion of data into Customer Journey Analytics, which removes the requirement of duplicated datasets and schemas.

Furthermore, instead of having to request stitching through customer support, you can now [initiate stitching yourself from an updated Connections UI](/en/docs/analytics-platform/using/stitching/use-stitching-ui).

*The previously communicated releases dates are pushed due to additional efforts required. The new release dates overlap with the holiday season, which introduces additional release constraints. A phased rollout is now planned to ensure stability and minimize disruption during the holiday period.*

October 28, 2025
January 30, 2026
Streaming media services: Support schedule data
You can now upload scheduled data of past live Streaming Media content to more easily and accurately track viewership.

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

Analytics source connector: Search report suites in Experience Platform
If you do have a high number of report suites you can now
search for the report suite
you want to connect to within the Analytics Source Connector dataflow workflow.
October 30, 2025
Streaming Media: Updated XDM fields for collecting Streaming Media data into Adobe Experience Platform
When collecting Streaming Media data into Adobe Experience Platform, the XDM field paths shown under the heading of “XDM Field Path” of the Streaming Media parameters documentation should no longer be used. Instead, customers who implemented the Analytics source connector to collect Streaming Media data into Platform before May 9, 2025 must migrate their existing configurations to the mediaReporting field paths, as shown under the heading of “Reporting XDM Field Path” of the Streaming Media parameters documentation.

These field paths are found on the following pages and are marked as “Deprecated”: [Audio and video parameters](/en/docs/media-analytics/using/implementation/variables/audio-video-parameters), [Ad parameters](/en/docs/media-analytics/using/implementation/variables/ad-parameters), [Chapter parameters](/en/docs/media-analytics/using/implementation/variables/chapter-parameters), [Player state parameters](/en/docs/media-analytics/using/implementation/variables/player-state-parameters), and [Quality parameters](/en/docs/media-analytics/using/implementation/variables/quality-parameters). (No action is required for customers who implement the Analytics source connector after May 9, 2025, and are already using only mediaReporting XDM paths.)

Data ingestion on the deprecated XDM field paths will continue until the end of October 2025. After that time, deprecated field paths will be fully removed and no longer visible in the Adobe Experience Platform Schema UI, and data will be sent only using the mediaReporting field paths.

For more information, see [Migrate an Analytics Source Connector implementation to updated XDM Streaming Media fields](/en/docs/media-analytics/using/media-use-cases/xdm-updates/updated-xdm-fields).

Please contact your Adobe Consulting Services or Account team for migration support.

October 2025
## Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-400507, AN-400265, AN-399209, AN-397146, AN-394992, AN-390795**Components**:**Content Analytics**:**Exports**: AN-399012, AN-388578**Guided Analysis**:**Implementation**: AN-397551, AN-397550, AN-397190, AN-396127**Report Builder**: AN-401127, AN-400618, AN-392971, AN-391692**Reporting**:**Segmentation**:**Scheduled reports**:**Shared metrics and dimensions**:**Other**:

## September 2025 sept25

Feature
Description
Rollout starts
General Availability
Updates to the Usage interface
The [Usage interface](/en/docs/analytics-platform/using/cja-connections/manage-connections#usage) now adds information about core data volume and average row size.

For more information, see [Manage connections](/en/docs/analytics-platform/using/cja-connections/manage-connections#usage).

September 4, 2025
Improvements when migrating projects and components to Customer Journey Analytics
The following improvements are now available when migrating projects and components from Adobe Analytics to Customer Journey Analytics:

- Migrate multiple projects at one time.You can migrate up to 20 projects at one time.Previously, you could migrate only one project at a time.
- Update mappings for dimensions and metrics that were already mapped with a previous project migration.You can now update these mappings each time you migrate a project, even if the same dimensions and metrics were previously mapped with a prior migration.Previously, any mappings you chose were permanent for all future project migrations.
- Improved performance for organizations with high numbers of projects.

This feature is available from the Adobe Analytics interface. For more information, see [Migrate components and projects from Adobe Analytics to Customer Journey Analytics](/en/docs/analytics/admin/admin-tools/component-migration/component-migration).

September 15, 2025
September 18, 2025
Lookup keys limit increased up to 1 billion
The maximum number of unique keys for a lookup dataset is now up to 1 billion, depending on your Customer Journey Analytics entitlement.

Previously, the maximum number was 10 million for all entitlements.

For more information, see [Guardrails](/en/docs/analytics-platform/using/technotes/guardrails).

September 25, 2025
Support for ad hoc and relational schemas
Ad hoc
and
relational schemas
are used in data ingestion and data mirror workflows for Experience Platform.
September 23, 2025 (Originally planned to release on August 28, 2025)
## Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-389683; AN-389534; AN-389207; AN-389066; AN-388687; AN-388478; AN-387089; AN-384865; AN-384560; AN-383486; AN-365768; AN-351639**Components**:**Content Analytics**:**Guided Analysis**: AN-384426**Platform**: AN-384410**Report Builder**: AN-389336; AN-382775**Reporting**:**Segmentation**:**Shared metrics and dimensions**:**Other**: AN-388222; AN-384898; AN-387169

## August 2025 aug25

Feature
Description
Rollout starts
General Availability
Map visualization
The map visualization is a visualization in Analysis Workspace that allows you to build a visual map of any metric (including calculated metrics). It is useful for identifying and comparing metric data across different geographic regions.

Previously, the map visualization was available only in Adobe Analytics.

The map visualization in Customer Journey Analytics contains the following improvements from the map visualization in Adobe Analytics:

- Use any segment from your data view as a data source.
- Accuracy up to a single meter by configuring the dimension in your data view.
- A new selection tool allows you to create a segment, audience, trend, or breakdown from any area you select in the visualization.

For more information, see [Map](/en/docs/analytics-platform/using/cja-workspace/visualizations/map).

August 13, 2025
August 25, 2025
B2B templates
If you license the Customer Journey Analytics B2B Edition, the following additional B2B templates are now available from the Adobe templates UI:

- B2B Account Engagement Overview
- B2B Opportunity Engagement Overview
- B2B Buying Group Activity

For more information, see [B2B templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#b2b-templates) in [Use templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates).

August 15, 2025
Projects downloaded as PDFs are downloaded to your workstation
When downloading a project as a PDF, the PDF is downloaded to the downloads folder on your workstation.

Previously, downloading a project as a PDF launched the PDF in a new browser tab with a unique URL.

For more information, see [Download projects and data](/en/docs/analytics-platform/using/cja-workspace/export/download-send).

August 25, 2025
Extending lookup keys limit
Depending on your Customer Journey Analytics package, you can now have up to a maximum of 1 billion unique keys in a lookup dataset.

For more information, see [Data transfer limits](/en/docs/analytics-platform/using/technotes/guardrails#data-transfer-limits) in the Customer Journey Analytics [Guardrails](/en/docs/analytics-platform/using/technotes/guardrails) documentation.

August 29, 2025
Create metrics and dimensions based on user-defined map fields from the Platform schema
User-defined map fields that you define in your Experience Platform schema are now available for use in Customer Journey Analytics.

You can use the following map fields when creating metrics and dimensions in Customer Journey Analytics:

- String to String
- String to Integer

For more information, see [Component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview).

For more information about map fields in Experience Platform, see [Define map fields in the UI](/en/docs/experience-platform/xdm/ui/fields/map).

End of August 2025
Deleted projects are immediately unavailable by URL and are deleted from scheduled deliveries
Projects that are deleted are immediately deleted from scheduled deliveries and are no longer accessible by their URL.

Previously, projects were included in scheduled deliveries and could be accessed with their URL for 60 days after being deleted.

For more information about deleting projects, see [Projects overview](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/freeform-overview).

End of August 2025
## Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-389683; AN-389534; AN-389207; AN-389066; AN-388687; AN-388478; AN-387089; AN-384865; AN-384560; AN-383486; AN-365768; AN-351639**Components**:**Content Analytics**:**Guided Analysis**: AN-384426**Platform**: AN-384410**Report Builder**: AN-389336; AN-382775**Reporting**:**Segmentation**:**Shared metrics and dimensions**:**Other**: AN-388222; AN-384898; AN-387169

## July 2025

Feature
Description
Rollout starts
General Availability
Add and view comments in Analysis Workspace projects
A new [commenting feature](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/comment-projects) in Analysis Workspace allows you to share insights and ask questions within the context of an Analysis Workspace project. This can streamline discussions about the data, keeping conversations within the context of the data that is being discussed. You can

- Comment on any Analysis Workspace project to which you have access
- Comment on a specific point in a visualization or make general comments about a project
- Tag other users to notify them about your comments
- Manage existing comments (edit, pin, resolve, and so forth)

Customer Journey Analytics administrators can [disable commenting at the organization level](/en/docs/analytics-platform/using/cja-workspace/user-preferences#ims-organization-preferences). Project owners can [disable commenting at the project level](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects).

June 25, 2025
July 22, 2025

(previously May 29, 2025)

Projects downloaded as PDFs are downloaded to your workstation
When downloading a project as a PDF, the PDF is downloaded to the downloads folder on your workstation. Previously, downloading a project as a PDF launched the PDF in a new browser tab with a unique URL. (Documentation link to follow)
August 25, 2025
Derived fields - Date Math function
The
Date Math
derived field function provides the ability to return the difference between two Date or Date-time fields.
August 4, 2025
August 8, 2025
Derived Fields - Depth Function
The
Depth
derived field function provides the ability to return the depth of a field, similar to what is possible with the out-of-the-box standard Event Depth dimension.
August 4, 2025
August 8, 2025
Derived fields - Typecast function
The
Typecast
derived field function provides the ability to change a field type on the fly and to make the field available for additional transformations within Customer Journey Analytics.
August 4, 2025
August 8, 2025
## June 2025 jun25

Feature
Description
Rollout starts
General Availability
Analysis Workspace left panel no longer opens and closes on hover
The left panel in Analysis Workspace is used to add things like components, panels, and visualizations to your project. The option to temporarily open the left panel by hovering over one of the icons on the far left is no longer available. Instead, simply click one of these icons to keep the panel open, then click the same icon to close it.
June 2, 2025

(Originally planned to release on May 29, 2025)

Customer Journey Analytics B2B Edition
Customer Journey Analytics B2B Edition helps B2B companies align their marketing, sales, and product teams by providing actionable account insights that drive revenue growth. With the account placed at the center of the data model, all analysis focuses on the account journey. Adding a new layer of entities (accounts, opportunities, and buying groups) on top of person and time-based events, creates a complete picture of the B2B marketing and revenue lifecycle.
Learn more
June 18, 2025
Support for secure cloud destinations in Report Builder
You can now export reports from Report Builder to the following cloud storage destinations:

- Amazon S3 Role ARN
- Google Cloud Platform
- Azure SAS
- Azure RBAC

Previously, you could share workbooks to other users via email, but you could not export reports from Report Builder to cloud destinations.

For more information, see [Schedule workbooks by exporting to cloud destinations](/en/docs/analytics-platform/using/cja-reportbuilder/report-builder-export).

June 19,2025 (Originally June 18, 2025)
New preview experience
The preview panel, that is used when you create a segment or configure the settings of a data view, now uses a horizontal bar visualization instead of a donut visualisation.
June 18, 2025
Modified attribution model dialog
You can now define the container and time period separately in the attribution model dialog.
June 18,2025
Connection map
A new
connection map interface
is available to visually display your connection configuration.
June 18, 2025
Add and view comments in Analysis Workspace projects
A new [commenting feature](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/comment-projects) in Analysis Workspace allows you to share insights and ask questions within the context of an Analysis Workspace project. This can streamline discussions about the data, keeping conversations within the context of the data that is being discussed. You can

- Comment on any Analysis Workspace project to which you have access
- Comment on a specific point in a visualization or make general comments about a project
- Tag other users to notify them about your comments
- Manage existing comments (edit, pin, resolve, and so forth)

Customer Journey Analytics administrators can [disable commenting at the organization level](/en/docs/analytics-platform/using/cja-workspace/user-preferences#ims-organization-preferences). Project owners can [disable commenting at the project level](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects).

June 25, 2025
July 11, 2025

(Originally planned to release on May 29, 2025)

Support for Chrome pre-rendering
Control how data collection libraries behave when Chrome pre-renders a page. (Documentation link to follow)
July 31, 2025 (previously June 30, 2025)
### Fixes in Customer Journey Analytics

**Alerts**: AN-379554**Analysis Workspace**: AN-339607; AN-379222; AN-381138; AN-383291**B2B**: AN-376028**BI Extension for Tableau**: AN-377488**Components**: AN-376174**Data views**: AN-379011**Export locations**: AN-382191**Full table export**: AN-375646; AN-376986; AN-380355; AN-381310**Journey canvas**: AN-375865; AN-378011**Report Builder**: AN-369786; AN-371395; AN-372809**Reporting**: AN-372615; AN-378578;

## May 2025 may25

Feature
Description
Rollout starts
General Availability
Updated XDM fields for collecting Streaming Media data into Adobe Experience Platform
When collecting Streaming Media data into Adobe Experience Platform, the XDM field paths shown under the heading of “XDM Field Path” of the Streaming Media parameters documentation should no longer be used. These field paths are found on the following pages and are marked as “Deprecated”: [Audio and video parameters](/en/docs/media-analytics/using/implementation/variables/audio-video-parameters), [Ad parameters](/en/docs/media-analytics/using/implementation/variables/ad-parameters), [Chapter parameters](/en/docs/media-analytics/using/implementation/variables/chapter-parameters), [Player state parameters](/en/docs/media-analytics/using/implementation/variables/player-state-parameters), and [Quality parameters](/en/docs/media-analytics/using/implementation/variables/quality-parameters).

Instead, customers should migrate to the mediaReporting field paths, as shown under the heading of “Reporting XDM Field Path” of the Streaming Media parameters documentation referenced above.

During a transitional period of three months, data ingestion on the deprecated XDM field paths will continue. However, at the end of July 2025, deprecated field paths will be fully removed and no longer visible in the Adobe Experience Platform Schema UI, and data will be sent only using the mediaReporting field paths.

Customers who implemented the Analytics source connector to collect Streaming Media data into Platform before April 22, 2025 must migrate their existing configurations to use the new field paths. This migration must be complete by the end of July 2025. Please contact your Adobe Consulting Services or Account team for migration support. No action is required for customers who implement the Analytics source connector after April 22, 2025.

April 22, 2025
Stitching: Retrieve persistent and transient IDs from XDM IdentityMap
This feature provides support for using identities stored in the XDM identityMap in the stitching process. The identityMap can be used for the persistent or transient ID for field-based stitching and can be used for the persistent ID for graph-based stitching. You can use either a specific namespace or primary identity from the identityMap. Learn more
here
and
here
April 28, 2025
Shared metrics and dimensions across data views
Allows you to apply dimension and metric settings across multiple data views. Changes made to a shared dimension or metric apply to all instances of that dimension or metric across all applicable data views. This interface allows Customer Journey Analytics admins to more easily manage components when many data views are used.
Learn more
April 30, 2025
Increase in full table export limits
Adobe increased the number of columns you can use with
full table export
from 5 dimensions and 5 metrics to 10 dimensions and 10 metrics. This applies to all Customer Journey Analytics tiers. There is no change in the entitlements for the number of rows which can be exported.
April 30, 2025
Event Depth dimension
A new
Event Depth dimension
was added to the list of required standard components for a data view.
May 8, 2025
Disable the manifest file when exporting full tables
Will allow you to disable the manifest file that is included by default when exporting full tables from Analysis Workspace.
Learn more
May 20, 2025
Data Insights Agent
The Data Insights Agent, part of the AI Assistant in Customer Journey Analytics, is a generative AI conversation agent. It uses components from your data view and your actual data to quickly and efficiently answer data-centric questions by building relevant visualizations in Analysis Workspace.
Learn more
May 28, 2025
Dimension format defaults to 2 for Double type dimensions
For schemas with Double data types, the dimension format now defaults to 2 decimal places. You can change this number to 0 through 5 decimal places.

Previously, the format defaulted to 0 decimal places.

This means that if you are using double-type dimensions in your Analysis Workspace reports, no decimal places were shown by default. These same reports will now show 2 decimal places.

For more information about how to update the number of decimal places that are shown for double-type dimensions, see [Format component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/format).

May 29, 2025
Analysis Workspace left panel no longer opens and closes on hover
The left panel in Analysis Workspace is used to add things like components, panels, and visualizations to your project. The option to temporarily open the left panel by hovering over one of the icons on the far left is no longer available. Instead, simply click one of these icons to keep the panel open, then click the same icon to close it.
June 2, 2025

(Originally planned to release on May 29, 2025)

Customer Journey Analytics B2B Edition
Customer Journey Analytics B2B Edition helps B2B companies align their marketing, sales, and product teams by providing actionable account insights that drive revenue growth. With the account placed at the center of the data model, all analysis focuses on the account journey. Adding a new layer of entities (accounts, opportunities, and buying groups) on top of person and time-based events, creates a complete picture of the B2B marketing and revenue lifecycle.
Learn more
June 18, 2025
Add and view comments in Analysis Workspace projects
A new [commenting feature](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/comment-projects) in Analysis Workspace allows you to share insights and ask questions within the context of an Analysis Workspace project. This can streamline discussions about the data, keeping conversations within the context of the data that is being discussed. You can

- Comment on any Analysis Workspace project to which you have access
- Comment on a specific point in a visualization or make general comments about a project
- Tag other users to notify them about your comments
- Manage existing comments (edit, pin, resolve, and so forth)

Customer Journey Analytics administrators can [disable commenting at the organization level](/en/docs/analytics-platform/using/cja-workspace/user-preferences#ims-organization-preferences). Project owners can [disable commenting at the project level](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects).

June 25, 2025

(Originally planned to release on May 29, 2025)

### Fixes in Customer Journey Analytics

**Analysis Workspace**: AN-361874; AN-371360; AN-373079; AN-374382; AN-374447; AN-375277; AN-375680**Audiences**: AN-372343**Audit Log**: AN-378168**Connections**: AN-373121; AN-372996**Data deletion**: AN-375450**Derived fields**: AN-373689; AN-377852**Export locations**: AN-374167**Journey canvas**: AN-373319**Report Builder**: AN-369786**Reporting**: AN-377326; AN-378051**Reporting activity manager**: AN-377148

## April 2025 apr25

Feature
Description
Rollout starts
General Availability
Increase in full table export limits
We are increasing the number of columns customers can use with full table export from 5 dimensions and 5 metrics to 10 dimensions and 10 metrics. This applies to all Customer Journey Analytics tiers. There is no change in the entitlements for the number of rows which can be exported.
April 30, 2025
Updates to “No Value” line item on numeric dimensions
For numeric dimensions, this update lets you

- Use the “No Value” dimension item in a segment.
- Perform a breakdown in a report on the “No Value” line item.

[Learn more](/en/docs/analytics-platform/using/cja-dataviews/component-settings/no-value-options#numeric)

March 27, 2025
Adobe Content Analytics
Adobe Content Analytics allows you to quickly and easily investigate large volumes of content data to uncover trends, spot anomalies, identify content fatigue, and gain insights from content exposure.

Out of the box, you can save time with pre-built reporting templates and new features like Asset Inspector. This capability lets you not only visualize the asset in-line with your data, but also open each asset for summarized details including performance, placements, attributes and more.

You can investigate this new set of content data within the context of the complete customer journey to answer important business questions, assess content performance, enhance segmentation, identify optimization opportunities, and define new audiences for activation.

Content Analytics is an add-on to Customer Journey Analytics. [Learn more](/en/docs/analytics-platform/using/content-analytics/content-analytics)

March 27, 2025
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector automatically maps streaming media data in Adobe Analytics to the same fields used by the Web SDK. Previously, data was mapped to both the old and new locations, but only the new location will be used in the future.
Learn more
March 31, 2025
Updated XDM fields for collecting Streaming Media data into Adobe Experience Platform
When collecting Streaming Media data into Adobe Experience Platform, the XDM field paths shown under the heading of “XDM Field Path” of the Streaming Media parameters documentation should no longer be used. These field paths are found on the following pages and are marked as “Deprecated”: [Audio and video parameters](/en/docs/media-analytics/using/implementation/variables/audio-video-parameters), [Ad parameters](/en/docs/media-analytics/using/implementation/variables/ad-parameters), [Chapter parameters](/en/docs/media-analytics/using/implementation/variables/chapter-parameters), [Player state parameters](/en/docs/media-analytics/using/implementation/variables/player-state-parameters), and [Quality parameters](/en/docs/media-analytics/using/implementation/variables/quality-parameters).

Instead, customers should migrate to the mediaReporting field paths, as shown under the heading of “Reporting XDM Field Path” of the Streaming Media parameters documentation referenced above.

During a transitional period of three months, data ingestion on the deprecated XDM field paths will continue. However, at the end of July 2025, deprecated field paths will be fully removed and no longer visible in the Adobe Experience Platform Schema UI, and data will be sent only using the mediaReporting field paths.

Customers who implemented the Analytics source connector to collect Streaming Media data into Platform before April 22, 2025 must migrate their existing configurations to use the new field paths. This migration must be complete by the end of July 2025. Please contact your Adobe Consulting Services or Account team for migration support. No action is required for customers who implement the Analytics source connector after April 22, 2025.

April 22, 2025
Terminology change: “Filters” to “Segments”
Previously, Adobe Customer Journey Analytics referred to segments as “filters”. This terminology has now been brought in line with Adobe Analytics. “Filters” are now called “segments”. (Obviously, search filters are still called “filters”.) The UI and documentation have been updated.
April 16, 2025
Stitching: Retrieve persistent and transient IDs from XDM IdentityMap
This feature provides support for using identities stored in the XDM identityMap in the stitching process. The identityMap can be used for the persistent or transient ID for field-based stitching and can be used for the persistent ID for graph-based stitching. You can use either a specific namespace or primary identity from the identityMap. Learn more
here
and
here
April 28, 2025
Shared metrics and dimensions across data views
Allows you to apply dimension and metric settings across multiple data views. Changes made to a shared dimension or metric apply to all instances of that dimension or metric across all applicable data views. This interface allows Customer Journey Analytics admins to more easily manage components when many data views are used.
Learn more
April 30, 2025
### Fixes in Customer Journey Analytics

**Admin Console**: AN-370228**Analysis Workspace**: AN-371933; AN- 371933; AN-371979**Audiences**: AN-373032**Component settings**: AN-367400**Derived fields**: AN-370614; AN-370959**Export locations**: AN-371670**Full table export**: AN-360492; AN-369204; AN-370755;AN-372294; AN-372363; AN-372754; AN-373040; AN-373081; AN-373168**Journey canvas**: AN-373294**Mobile app**: AN-363169; AN-368496; AN-371766**Product usage**: AN-369501**Reporting**: AN-369085; AN-371094; AN-372580

## March 2025 mar25

Feature
Description
Rollout starts
General Availability
Product Usage template
A new Workspace template allows you to view how the Customer Journey Analytics product is used within your organization.
Learn more
.
March 5, 2025
Customer Journey Analytics upgrade guide
Lets you generate a step-by-step guide for upgrading from Adobe Analytics to Customer Journey Analytics. This guide is tailored to your organization and takes into consideration your current Adobe Analytics environment, your intended uses for Customer Journey Analytics, and any time-saving tradeoffs your organization wants to make.

To start generating your custom guide, log in to Customer Journey Analytics, then select **Upgrade to Customer Journey Analytics** on the **Workspace** tab.

[Learn more](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations#recommended-upgrade-steps-for-most-organizations)

March 11, 2025
Updates to “No Value” line item on numeric dimensions
For numeric dimensions, this update lets you

- Use the “No Value” dimension item in a segment.
- Perform a breakdown in a report on the “No Value” line item.

[Learn more](/en/docs/analytics-platform/using/cja-dataviews/component-settings/no-value-options#numeric)

March 27, 2025
Adobe Content Analytics
Adobe Content Analytics allows you to quickly and easily investigate large volumes of content data to uncover trends, spot anomalies, identify content fatigue, and gain insights from content exposure.

Out of the box, you can save time with pre-built reporting templates and new features like Asset Inspector. This capability lets you not only visualize the asset in-line with your data, but also open each asset for summarized details including performance, placements, attributes and more.

You can investigate this new set of content data within the context of the complete customer journey to answer important business questions, assess content performance, enhance segmentation, identify optimization opportunities, and define new audiences for activation.

Content Analytics is an add-on to Customer Journey Analytics. [Learn more](/en/docs/analytics-platform/using/content-analytics/content-analytics)

March 27, 2025
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector automatically maps streaming media data in Adobe Analytics to the same fields used by the Web SDK. Previously, data was mapped to both the old and new locations, but only the new location will be used in the future.
Learn more
March 31, 2025
### Fixes in Customer Journey Analytics

**Alerts**: AN-368098**Analysis Workspace**: AN-333301; AN-365796; AN-368023**Audit Log**: AN-368100**Data Views**: AN-369504**Filters**: AN-369037**Full Table Export**: AN-369330**Mobile App**: AN-369365

### Important notices for Customer Journey Analytics Administrators

Notice
Notice added or updated
Description
N/A
## February 2025 feb25

Feature
Description
Rollout starts
General Availability
BI Extension - expanded support
The Customer Journey Analytics BI extension now
supports Looker, Jupyter Notebook and R Studio
.
January 24, 2025
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector automatically maps streaming media data in Adobe Analytics to the same fields used by the Web SDK. Previously, data was mapped to both the old and new locations, but only the new location will be used in the future.
Learn more
March 31, 2025
### Fixes in Customer Journey Analytics

**Audiences**: AN-365687; AN-366674**Data Ingestion**: AN-368376**Data Views**: AN-368443**Derived Fields**: AN-368441**Guided Analysis**: AN-367697**Journey canvas**: AN-367890**Mobile App**: AN-367137**Power BI extension**: AN-367643**Workspace**: AN-352828; AN-359248; AN-368583

## January 2025 jan25

Feature
Description
Rollout starts
General Availability
Updated Connections Usage experience
The
Usage
tab in Connection now provides enhanced visualizations for these types of reportable rows: core, ingested and historical data. You can also view and break down the usage data by connection, dataset, sandbox, or tag.
Learn more
January 15, 2025
API for migrating Adobe Analytics projects and any included components to Customer Journey Analytics
An API is now available for migrating your Adobe Analytics projects and included components to Customer Journey Analytics. Previously, project and component migration was available only through the user interface.
Learn more
. Select
CJA Migration APIs
from the drop-down menu.
January 15, 2025
Use custom templates from Customer Journey Analytics on the Reports page in Journey Optimizer
You can now customize the new reporting interface in Adobe Journey Optimizer by creating or editing a template in Customer Journey Analytics, then saving the template to be used on the Reports page in Journey Optimizer. Previously, the new reporting interface in Adobe Journey Optimizer couldn’t be customized.

For more information, see “Create a template” or “Edit or delete a template” in [Create and manage templates](/en/docs/analytics-platform/using/cja-workspace/templates/create-templates).

January 15, 2025
Templates in Analysis Workspace
Templates are now available in Customer Journey Analytics.

- **Pre-built templates**: A large selection of pre-built templates are available. You can use these templates to gain quick insights into the most common reporting scenarios. Pre-built templates can be used as they are. Or, they can be used as a starting point for a project, which can then be customized to better suit a specific purpose. [Learn more](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates)
- **Company templates**: Administrators can create company templates to meet the needs of use cases specific to their organization. Company templates that administrators create are available to users in their organization. [Learn more](/en/docs/analytics-platform/using/cja-workspace/templates/create-templates)

January 15
January 30, 2025
Product usage
See how your organization uses Customer Journey Analytics. Enabling this feature creates a dataset in Adobe Experience Platform that collects data when anyone in your organization uses Analysis Workspace. A connection and a data view are also automatically created, giving you access to dimensions like top project types, most active users, and most popular components used in projects.
Learn more
October 23, 2024
January 22, 2025
Intelligent Captions v2
Intelligent captions are now supported for the following visualizations: Multi-line, Bar, Horizontal bar, Donut, Area, Flow, and Fallout. You can select to show all intelligent captions at once in an expanded view, or you can show individual intelligent captions in a one-by-one view.
Learn more
January 22, 2025
Add guided analyses to projects from within Guided Analysis
Lets you add guided analyses to Workspace projects from within Guided Analysis. You can also add guided analyses directly in Analysis Workspace.
Learn more
January 22, 2025
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector will automatically map streaming media data in Adobe Analytics to the same fields used by the Web SDK. Currently, data is mapped to both the old and new locations, but only the new location will be used in the future.
Learn more
January 30, 2025
## Fixes in Customer Journey Analytics

Alerts: AN-363263; AN-364880; AN-365029; AN-365960Audiences: AN-362564; AN-363254;Data ingestion: AN-362359; AN-362751Data Views: AN-362089; AN-365213; AN-365770; AN-366171; AN-366681Derived Fields: AN-359711; AN-362496Export Locations: AN-363999Full table export: AN-363055Report Builder: AN-362937Workspace: AN-359012; AN-359145; AN-359914; AN-361455; AN-361934; AN-362469; AN-363460; AN-364714; AN-364918; AN-366277;

recommendation-more-help
