---
title: "Customer Journey Analytics - documentation updates"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/releases/doc-changes"
category: "other"
topic: "analytics-platform/using/releases/doc-changes"
created_at: "2026-06-02T19:04:58.926705+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Customer Journey Analytics - documentation updates

Last update: May 13, 2026
- Topics:
- [Release Notes](#)

CREATED FOR:

- User
- Admin

The following updates were made to the Customer Journey Analytics documentation since its inception.

## 2026

Feature
Description
May 2026
Javascript library for Content Analytics
Documentation on how to implement Content Analytics for the web channel using the
Content Analytics Javascript library
without requiring Experience Platform Data Collection Tags.
Data Mirror consideratons
Documentation
that describes factors you should consider when you set up
Data Mirror datasets
.
Content Analytics mobile channel
Updates to
Content Analytics documentation
to describe the capabilities and configuration of the Content Analytics mobile channel.
April 2026
Derived fields guidelines
Added article with
guidelines
(best practices, guardrails, and common pitfalls) for working with derived fields.
Added missing documentation for two datasets that can be included when integrating Journey Optimizer
Two additional non-profile, system-generated datasets
are included in the connection when the High Throughput transactional messaging add-on is enabled for your IMS Org.
Updated cohort analysis use cases
Based on feedback added Analyis Workspace examples to the cohort analysis use cases.
March 2026
Break down a panel
Restructured the documentation around the
drop zone for a panel
to support the new
break down
functionality.
Technote on Bad IDs (BAVIDs)
New
technote on Bad IDs
. The technote explains the definition of a Bad ID, where in the Customer Journey Analytics interface Bad IDs are used, and how to investigate data in your connection for Bad IDs.
Datasets preview redesign in Connections
Updated documentation for an improved data preview experience when you
add
or
edit
datasets in a person-based connections, including documentation on additional
stitching preview information
for stitching-enabled datasets.
Content Analytics thumbnails and previews
Documentation on
thumbnails
and
previews
for additional visualizations in Content Analytics.
February 2026
Header overrides
Documentation on the additional
header overrides configuration
for Content Analytics.
Calculated metrics guardrail
Updated the
guardral for the maximum number of calculated metrics for an organization
. The maximum is now 50,000.
Standalone Content Analytics
Added documentation for a
standalone configuration of Content Analytics
.
January 2026
Architect a schema
Added substantial information and context to
Architect your schema for use with Customer Journey Analytics
.
## 2025

Feature
Description
December 2025
Implications of sandbox changes
Added the implications of a sandbox deletion or reset to the
Deletion and reset implications
article.
November 2025
Guardrail for rows per day in a connection
Added
guardrail information for data transfer limits
about the maximum average number of rows per day in a connection.
October 2025
Manage access to the Data Insights Agent
The
permission requirements and process for enabling data views
has been updated.
Attribution configuration
Additional updates to reflect the new attribution configuration options for model, container and lookback window.
Ingest and use Experience Platform audiences
Updated use case article on how to
ingest and use Experience Platform audiences
.
Prepare your organization to upgrade to Customer Journey Analytics
Added information about how to
prepare an organization to upgrade to Customer Journey Analytics
.
Report on LLM and AI-generated traffic
Added
use case article
on how to report on LLM and AI-generated traffic using derived fields as the foundation. The article is based on the blog article
Tracking and Analyzing LLM and AI-Generated Traffic in Adobe Customer Journey Analytics
.
September 2025
Dates before 1900
Added a
note
on how dates before 1900 are handled by Customer Journey Analytics.
Real-time reporting
Added documentation about
real-time reporting
in Customer Journey Analytics.
Usage interface
Added documentation for updated
Usage interface
in Connections.
Stitching Journey Optimizer datasets
Documented
list of automatically generated Journey Optimzer datasets
that can be used in stitching.
Context labels
Added more background information on the use and purpose of
context labels
in data view components.
August 2025
New integration with Adobe Advertising
Added information about
integrating with Adobe Advertising
.
New derived field functions
Documentation for the new derived field functions:
Date Math
,
Depth
, and
Typecast
.
July 2025
Debugger
New article on how to enable, use and disable the project debugger in Analysis Workspace.
Flow visualization performance recommendation
Added information stating that leaving more than 10 nodes expanded in a single flow visualization can affect reporting time.
Alternate method for granting the Adobe Azure App access to your key
Added information about granting permissions via authorization consent when
setting up customer-managed keys
for Customer Journey Analytics on Azure.
June 2025
New shortcut actions
New keyboard shortcuts in Analysis Workspace now allow you to
move Workspace panels
up and down in a project.
May 2025
Customer Journey Analytics
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Draft documentation on the upcoming Customer Journey Analytics B2B Edition, including:

- new [overview](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition), [concepts and features](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-concepts-features), [quick start guide](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-quick-start-guide), [transition guide](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-transition), and [use cases](/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/use-cases-overview) articles, and
- numerous updates to existing documentation.

The Customer Journey B2B Edition documentation, articles and features are labeled with a [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank) badge.

Validate stitching
Added documentation to
validate
how identify stitching affects authentication success rates and overall person identification performance.
Event Depth dimension
Documentation for the new Event Depth dimension, as part of the
standard dimensions
for a data view.
April 2025
Increased full table export limits
Changed the
number of columns
customers can use with full table export from 5 dimensions and 5 metrics to 10 dimensions and 10 metrics.
Connections
Reworked and updated the Customer Journey Connections documentation for upcoming Customer Journey B2B Edition.
Product analysis use case
Added
Product analysis in Customer Journey Analytics
.
Shared metrics & dimensions
Added documentation for the
Shared metrics & dimensions
feature.
Report Builder
Reviewed and updated the
Report Builder
documentation.
View and manage usage
Reworked the documentation on how to
view
and
manage
Customer Journey Analytics usage
Adobe Content Analytics
Content Analytics
allows you to quickly and easily investigate large volumes of content data to uncover trends, spot anomalies, identify content fatigue, and gain insights from content exposure.
Updated XDM fields for collecting Streaming Media data into Adobe Experience Platform
When collecting Streaming Media data into Adobe Experience Platform, the XDM field paths shown under the heading of “XDM Field Path” of the Streaming Media parameters documentation should no longer be used. These field paths are found on the following pages and are marked as “Deprecated”:
Audio and video parameters
,
Ad parameters
,
Chapter parameters
,
Player state parameters
, and
Quality parameters
.
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector automatically maps streaming media data in Adobe Analytics to the same fields used by the Web SDK. Previously, data was mapped to both the old and new locations, but only the new location will be used in the future.
Learn more
Terminology change: “Filters” to “Segments”
Previously, Adobe Customer Journey Analytics referred to segments as “filters”. This terminology has now been brought in line with Adobe Analytics. “Filters” are now called “segments”. (Obviously, search filters are still called “filters”.) The UI and documentation have been updated.
March 2025
Quantum Metric use cases
Added use cases for collecting data from
Quantum Metric
.
Product Usage template
A new Workspace template allows you to view how the Customer Journey Analytics product is used within your organization.
Learn more
.
Customer Journey Analytics upgrade guide
Lets you generate a step-by-step guide for upgrading from Adobe Analytics to Customer Journey Analytics. To start generating your custom guide, log in to Customer Journey Analytics, then select
Upgrade to Customer Journey Analytics
on the
Workspace
tab.
Learn more
Updates to “No Value” line item on numeric dimensions
For numeric dimensions, this update lets you use the “No Value” dimension item in a segment and perform a breakdown in a report on the “No Value” line item.
Learn more
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector automatically maps streaming media data in Adobe Analytics to the same fields used by the Web SDK. Previously, data was mapped to both the old and new locations, but only the new location will be used in the future.
Learn more
February 2025
Media Collection: Adobe Source Connector updates for new Media Reporting XDM
The Analytics Source Connector automatically
maps streaming media data in Adobe Analytics
to the same fields used by the Web SDK. Previously, data was mapped to both the old and new locations, but only the new location will be used in the future.
BI Extension - expanded support
The Customer Journey Analytics BI extension now supports
Looker, Jupyter Notebook and R Studio
.
January 2025
Updated Connections Usage experience
The
Usage
tab in Connection now provides enhanced visualizations for these types of reportable rows: core, ingested and historical data. You can also view and break down the usage data by connection, dataset, sandbox, or tag.
Usage metrics
Updated documentation on the improved
usage metrics
interface.
Product usage
Product usage
shows you how your organization uses Customer Journey Analytics.
Guided analysis
Updated documentation with the availability of
Guided Analysis
from within Guided Analysis.
Documentation on using custom templates from Customer Journey Analytics on the Reports page in Journey Optimizer
You can now customize the new reporting interface in Adobe Journey Optimizer by
creating or editing a template in Customer Journey Analytics
, then saving the template to be used on the Reports page in Journey Optimizer. Previously, the new reporting interface in Adobe Journey Optimizer couldn’t be customized.
Templates in Analysis Workspace
Prebuilt templates
and
company templates
are now available in Customer Journey Analytics.
Intelligent Captions v2
Intelligent captions
are now supported for the following visualizations: Multi-line, Bar, Horizontal bar, Donut, Area, Flow, and Fallout. You can select to show all intelligent captions at once in an expanded view, or you can show individual intelligent captions in a one-by-one view.
## 2024

Feature
Description
November 2024
BI extension use cases
Documentation of several
BI extension use cases
for BI tools like Power BI Desktop and Tableau Desktop.
Stitching and privacy requests
Added notice on
upcoming changes in the unstitching process
that are the result of privacy requests.
October 2024
Journey canvas visualization
Journey canvas
is a visualization in Analysis workspace that allows you to analyze how people proceed through or fall out of a defined journey.
Asset transfer
Lets you
transfer ownership
of components such as projects, segments, and calculated metrics to other users to ensure continuity and appropriate access.
Improved Usage interface
Updated the article on the improved interface to show your
usage of ingested and reportable rows across all connections
Shared devices
Added a
use case article
that provides context on shared devices, how to handle and mitigate data from shared devices using stitching, and understand shared device exposure in your data using Query Service.
New information about Request factors in Analysis Workspace Performance
A new
Request factors
section in the
Optimize Analysis Workspace performance
article explains how requests are processed and the various factors that influence processing times.
Workspace and components
Refreshed the documentation on Analysis Workspace projects (projects, visualizations, and panels) and conponents (annotations, dimensions, (calculated) metrics, segments, date ranges, alerts, scheduled projects and audiences).
Guided analysis
Updated documentation with the availability of
Guided Analysis
from within Analysis Workspace.
Updated Audience documentation
When
creating an audience
from a visualization within Analysis Workspace, panel segments and column segments are now included as additional criteria.
September 2024
Summary data update
Updated summary data articles with information on how to properly use
lookup data
when reporting on summary data.
BI extension update
Added
defaults and limitation
section to the BI extension documentation.
Alerts
Added documentation for the
Alerts
functionality now available in Customer Journey Analytics.
Additional information in the “Used in” column in the calculated metric manager and segment manager
The “Used in” column in the
calculated metric manager
and
segment manager
contains the following new reporting areas: Report Builder and Ad-hoc components
August 2024
An example B2B project
Added a
use case
documenting how to set up, configure and report on profile (person) level based B2B data in Customer Journey Analytics, using the new
transform datasets for B2B lookups
functionality.
Updated Data export use cases
Added more detailed query examples to
Query Service (Data Distiller) & Export datasets
to illustrate how to properly apply attribution across sessions using a lookback window.
Summary data
Added documentation on
summary data
,
summary data group component settings
and a
summary data use case
.
July 2024
Added information about quick calculated metrics
Updated information in [Metrics](/en/docs/analytics-platform/using/cja-components/apply-create-metrics) to clarify the difference between [calculated metrics that are created in the calculated metrics builder](/en/docs/analytics-platform/using/cja-components/apply-create-metrics#create-calculated-metrics-for-all-projects) and [those that are created as quick calculated metrics within a single project](/en/docs/analytics-platform/using/cja-components/apply-create-metrics#create-calculated-metrics-for-a-single-project). Also added more details about hose to create quick calculated metrics.

Calculated metrics that are created in the calculated metrics builder are available in the component list and can be applied to projects throughout the organization, while calculated metrics that are created as quick calculated metrics are available only within the project where they were created.

Also updated information in [Build metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics) to make similar clarifications.

Derived field deduplicate function
Added documentation on the derived field
deduplicate
function.
Updated common error messages
Made minor updates to the
common error messages
.
June 2024
Updated product name that refers to streaming media features
Replaced instances of “Media Analytics” and “Streaming Media” with the name “Streaming Media Collection Add-on” and “Streaming Media Collection” when referring to the set of streaming media features that collect streaming media data and surface it in Analysis Workspace.

These updates are available throughout the Customer Journey Analytics documentation as well as the [Streaming Media Collection documentation](/en/docs/media-analytics/using/media-overview).

Graph-based stitching
Updated and restructured
stitching documentation
with the introduction of graph-based stitching.
AI Assistant
Added
documentation
on the AI Assistant for Customer Journey Analytics.
Transform datasets for B2B lookups
Added documentation on how to support
person-based lookups on B2B data
(including accounts, opportunities, marketing lists and campaigns) using transformation of B2B lookup datasets.
Derived field functions and function templates
Added documentation on the additional derived field functions (
Math
,
Next or Previous
, and
Summarize
) and
function templates
.
May 2024
Target integration
Added
article to Adobe integration section
on how to integrate Target with Customer Journey Analytics.
Required information when exporting Customer Journey Analytics reports to Google Cloud Platform while using organization policy constraints
Added the Adobe-owned Google Cloud Platform organization ID to the [Configure cloud export locations](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-locations) documentation for exporting Customer Journey Analytics reports to Google Cloud Platform.

This information is required only for organizations that are using [Organization policy constraints](https://cloud.google.com/storage/docs/org-policy-constraints) in Google Cloud Platform.

Documentation about adding components to projects
Added general information about how to
add the various types of components to projects in Analysis Workspace
.
Data export use cases
Set of new articles describing
data export use cases
and how to use Experience Platform and Customer Journey Analytics functionalities to implement these use cases
New documentation for upgrading from Adobe Analytics to Customer Journey Analytics
For organizations upgrading from Adobe Analytics to Customer Journey Analytics, there are multiple upgrade options and many considerations to keep in mind based on an organization’s current Adobe Analytics implementation and long-term goals.

New documentation resources are now available to help you better understand:

- The various upgrade paths that exist
- Which upgrade paths are available based on an organization’s current Adobe Analytics implementation
- The advantages and disadvantages of each upgrade path
- Step-by-step guidance for each upgrade path
- Considerations for handling historical data
- And more!

[Get started with the upgrade to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-getstarted).

Updated documentation about custom date ranges
Updated screenshots and procedures related to
example date ranges
in order to match the current product features and design.
Overview information about Dimensions
Added information about
dimensions
.
Examples of source connectors
Added examples of source connectors that are available when describing how to
use a source connector
for ingesting data.
April 2024
Forecasting statistical techniques
Added article describing the
statistical techniques used in forecasting service
.
Added information recommending Full Table Export for high cardinality dimensions
Added bullet in
Best practices for high cardinality dimensions
to recommend using Full Table Export for high cardinality dimensions.
Added documentation on Intelligent Captions in mobile scorecards
Intelligent Captions
can help non-analysts better make sense of their data without the help of analysts.
New documentation for Adobe Product Analytics features
- [Feature matrix](/en/docs/analytics-platform/using/guided-analysis/funnel)
- Enhanced [Retention](/en/docs/analytics-platform/using/guided-analysis/retention)
- [Enhanced Insights in Funnel](/en/docs/analytics-platform/using/guided-analysis/funnel)
- Compare events within a single Funnel step

March 2024
Usage information regarding the “Used in” column is available only starting in September 2023.
Clarified that usage information regarding the
Used in
column on the
projects landing page
goes back only as far as September 2023.
Added documentation on permissions enhancement for project-only Workspace components
If you share a project with other users, those users can edit
quick segments
and other project-only components that are embedded in the shared project.
February 2024
Updates to project sharing documentation
Added information about how to [view projects that are shared with you](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects#view-projects-shared-with-you).

Also streamlined information about [sharing individual or multiple projects](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects#share-a-specific-project-role).

Added permission requirements for uploading files to Azure SAS and Azure RBAC when configuring cloud export locations
Added exact permission requirements for uploading files to Azure SAS and Azure RBAC when
configuring cloud export accounts
and
configuring cloud export locations
.
Added permission requirements for uploading files to Amazon S3 Role ARN and GCP buckets when configuring cloud export locations
Added exact permission requirements for uploading files to Amazon S3 Role ARN and Google Cloud Platform buckets when
configuring cloud export locations
.
Clarified that Product Admins always have access to export full tables
Made the following changes to clarify that users who are assigned the Product Admin role have access to export full tables from Analysis Workspace by default:

- Added a new bullet to [Product Admin default permissions](/en/docs/analytics-platform/using/technotes/access-control#product-admin-default-permissions).
- Added a note under the [minimum requirements for exporting full tables to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud#minimum-requirements).

Clarified that segments are re-created during component migration from Adobe Analytics
In the
User Guide for Adobe Analytics users
, clarified that segments are automatically re-created in Adobe Analytics as part of the component migration process, and don’t need to be manually re-created.
Skipped record details
Added documentation on the skipped record details functionality in Connections. See
Connection details
for more information.
January 2024
Forecasting
Added documentation on
forecasting
, the new Analysis Workspace feature to forecast a standard or calculated metric with any supported time granularity (hourly, daily, weekly, monthly and yearly) for freeform tables and line charts.
Updated the documentation for adding accounts and locations when exporting full tables
Updated the documentation to reflect minor interface updates when configuring a new account or location when [exporting full tables from Analysis Workspace](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud#export-full-tables-from-analysis-workspace).

A new **Add account** option is now available in the **Account** drop-down menu. The **Add location** option that was previously available as a button next to the **Location name** drop-down menu is now available within the menu itself.

New component migration information when migrating from Adobe Analytics
Added information to
Evolution from Adobe Analytics
that references the new
component migration
capabilities that are documented in the Adobe Analytics Admin Guide.
Clarified that certain information is available only to administrators
Added information stating that the “Last used” and “Used in” columns that are described in
Calculated metrics manager
and the
Segment manager
are available only to system administrators.
Permissions required for exporting datasets
Added information explaining the
permissions required
to export datasets to cloud destinations.
Manage connections
Updated the
Manage connections
article, based on customer feedback.
Derived fields
Added summary of function
limitations
and explanation on how to determine number of
operators
used in a function.
## 2023

Feature
Description
December 2023
Data centers
Added an article on Customer Journey Analytics
hosting locations
.
Guardrails
Added article listing Customer Journey Analytics
guardrails
.
Currency conversion updates
Clarified documentation about how to
configure currency conversion
.
Updates to Anomaly Detection documentation
The documentation for Anomaly Detection was previously located in a section about Virtual Analyst. The following changes were made:

- The term Virtual Analyst was removed from the documentation.
- The section about [Anomaly Detection](/en/docs/analytics-platform/using/cja-workspace/anomaly-detection/anomaly-detection) was moved directly beneath the Analysis Workspace section.

October 2023
Using derived field for setting goals / targets
Added
use case
article illustrating how to use derived fields for setting goals / targets and reporting on these.
Export full tables to the cloud
Added documentation about exporting full tables with millions of Workspace rows to cloud destinations.

Exporting full tables offers one-time or scheduled delivery of data tables designed within Workspace with support for up to five breakdowns, five metrics, segments, and calculated metrics, all in a concatenated table. It is the evolution of Data Warehouse reports in Adobe Analytics, with many new, often-requested features that are not available in Data Warehouse today.

For more information, see [Export Customer Journey Analytics reports to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud).

Reporting Activity Manager
Added documentation for the Reporting Activity Manager.

The Reporting Activity Manager lets you see the reporting capacity for each connection in your organization. It provides administrators with detailed visibility into reporting consumption in order to easily diagnose and fix capacity issues during peak reporting times.

The following new articles were added:

- [Reporting Activity Manager overview](/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity-overview)
- [View reporting activity in the Reporting Activity Manager](/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity)
- [Cancel requests in the Reporting Activity Manager](/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity-cancel-requests)

New columns on management pages
Documented new columns that are now available in the
Calculated metrics manager
and the
Segment manager
.
Comparison with Adobe Analytics
Added an
overview page
as an introduction on comparing and understanding the differences between Customer Journey Analytics and Adobe Analytics.
Additional derived fields functionality
Updated documentation for the new
Lookup
function.
September 2023
Updated structure of articles for the Media Playback Time Spent panel
Removed the folder called Media Playback Time Spent, and combined the contents of the folder into a single article: [Media Playback Time Spent panel](/en/docs/analytics-platform/using/cja-workspace/panels/media-playback-time-spent).

This change is more in line with the documentation for other panels.

Additional derived fields functionality
Updated documentation for the new
Lowercase
and
Trim
functions and for the additional CSV capabilities added to the
Classify
function.
Regional data collection
Updated
FAQ
with information on regional data collection when using Customer Journey Analytics.
August 2023
Media Playback Time Spent panel
Updated content for
Media Playback Time Spent panel
to improve readability.
Report Builder enhancements
Updated content for
Schedule workbooks
to provide information for downloading scheduled tasks. Updated content for
Create a data block
to provide information for using Start date as a dimension.
Moved content about managing scheduled projects
Created a new article in the Analytics Components Guide called
Scheduled projects
. This content was previously located in the
Schedule projects
article in the Analytics Tools Guide.
Adobe Customer Journey Analytics feature support
Added more information in the
Supported in a new way
table on the sessionization capabilities in Customer Journey Analytics compared to Adobe Analytics.
Learn more
Evolution from Adobe Analytics
Updated the
(Re-)Configure Marketing Channels
section with a reference to the Derived fields Marketing channels function template.
Learn more
Data ingestion quick start guides for mobile applications and other platforms
Added additional data ingestion quick start guides outlining how to ingest and use data from mobile applications or other platforms (like desktop applications, games on consoles, applications on set-top boxes and IoT devices) in Customer Journey Analytics.
Learn more
July 2023
Session settings
Added a topic for this data view setting.
Learn more
Adobe Product Analytics
Adobe Product Analytics is a new way to interact with cross-channel data and insights in Customer Journey Analytics. These new capabilities enable Product teams to self-serve data and insights about their product experience through
guided analysis
workflows​.
Derived fields
A
derived field
allows you to define (often complex) data manipulations on the fly, through a customizable rule builder.
Expanded lookup support for Profile and Lookup data
Provides the ability to add datasets as lookups of fields within Profile or Lookup datasets. Previously, only Event datasets were supported.
Learn more
Report Builder enhancements
- [Filter from cell for multiple data blocks](/en/docs/analytics-platform/using/cja-reportbuilder/select-data-view)
- [Show and hide row and column headers](/en/docs/analytics-platform/using/cja-reportbuilder/create-a-data-block#build-the-data-block)

Edge Network geo lookups
Datastream settings
how has a geo lookup service that provides unified geographic data.
June 2023
Cross-channel analysis and stitching
In anticipation of the upcoming changes to enable stitching and to further clarify how cross-channel analysis can be elevated using stitching, documentation related to Cross-Channel Analytics functionality is edited to refer to
cross-channel analysis
as the Customer Journey Analytics capability and use case, and
Stitching
as an important functionality to accomplish this.
PowerBI & Tableau access to Customer Journey Analytics data views
The Customer Journey Analytics BI extension enables SQL access to data views that you have defined in Customer Journey Analytics.
Learn more
Adobe Journey Optimizer data views
Customer Journey Analytics Admins have access to some extra data views in Customer Journey Analytics, entitled “AJO Data view (Sandbox-name)”.
Learn more
.
Currency conversion
Updated documentation for
currency conversion
support.
Calculated metrics updates
The following updates were made to calculated metrics documentation in order to align it with current Customer Journey Analytics functionality:

- Updated the list of [default calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) available in Customer Journey Analytics
- Updated screen shots and procedures in various calculated metrics articles

May 2023
Deep Linking (Mobile App) documentation
Allows users to send links to scorecards that will lead them directly to the scorecard project in the app.
Learn more
Doc on “Select data view from cell” in Report Builder
This feature allows users to select the data view for a data block from a cell.
Learn more
Documentation for updated Home screen for the Analytics dashboards app (Mobile App)
The new updated Home screen allows you to view all of your scorecards in one consolidated scorecard list.
Learn more
Optimization update
Updated article on
Optimizing Customer Journey Analytics performance
Analysis Workspace overview
Updated
Analysis Workspace overview
to include more general overview information and links to relevant content.
Create projects
Created a new article that explains in detail how to
Create projects
in Analysis Workspace.
Sort components in the left rail
Added information about sorting the list of components in the left rail.See the “Search, filter, and sort the component list” section in
Components overview
.
Delete rows containing dynamic dimensions from a Freeform table
Added information about how to quickly delete specific rows that contain dynamic dimensions using the x icon. See the “Quickly exclude specific rows from a table” section in
Filter and sort tables
.
Button to add a visualization within a panel
Added information about a new button at the bottom of each panel in Analysis Workspace that allows you to quickly add a visualization. See the “Add visualizations to a panel” section in
Visualizations overview
.
Intelligent captions documentation
Enrich storytelling for users with
natural-language summaries
of a Line visualization.
Derived fields
Added documentation for
derived fields
functionality.
April 2023
Video about using segments as dimensions
Updated the video about using segments as dimension.

This video is linked from the [Create segments](/en/docs/analytics-platform/using/cja-components/segments/seg-create) page.

Following is a direct link to the video: [Use segments as dimensions in Analysis Workspace](/en/docs/customer-journey-analytics-learn/tutorials/components/filters/use-filters-as-dimensions).

Segment documentation
Added article about using the [Segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder).

Streamlined documentation in [Create segments](/en/docs/analytics-platform/using/cja-components/segments/seg-create) and [Segmentation overview](/en/docs/analytics-platform/using/cja-components/segments/seg-overview).

Update to Experimentation panel documentation
Added a section on
interpreting non-randomized dimensions
.
Project segments (Ad hoc and quick segments)
Streamlined documentation about project segments and removed duplicated information. The steps for creating ad hoc segments are now combined with the steps for
creating quick segments
.
March 2023
Integrate Decision Management data
Added content explaining how to
integrate Adobe Journey Optimizer Decision Management data in Customer Journey Analytics
.
Create data stories in mobile scorecards
A
data story
is a collection of supporting data points, business context, and related metrics built around a central theme or metric.
Updated feature support
Updated
Customer Journey Analytics feature support
with a table of features available in Customer Journey Analytics but not available or supported in AA.
Default calculated metrics
Added content explaining the
default calculated metrics provided by Adobe
.
Data Dictionary
Added new documentation for the Data Dictionary, including an [Overview](/en/docs/analytics-platform/using/cja-components/data-dictionary/data-dictionary-overview), [Viewing](/en/docs/analytics-platform/using/cja-components/data-dictionary/view-data-dictionary), [Editing](/en/docs/analytics-platform/using/cja-components/data-dictionary/edit-entries-data-dictionary), and [Monitoring](/en/docs/analytics-platform/using/cja-components/data-dictionary/monitor-data-dictionary-health) the Data Dictionary.

Information in [Adding component descriptions](/en/docs/analytics-platform/using/cja-components/add-component-descriptions) was updated to account for Data Dictionary functionality.

Link sharing for projects (no login required)
Updated existing documentation to explain how to share a read-only link of a project with people who do not have access to Analysis Workspace.

Updated user documentation includes [Share projects](/en/docs/analytics-platform/using/cja-workspace/curate-share/share-projects) and [Create shareable links](/en/docs/analytics-platform/using/cja-workspace/curate-share/shareable-links).

Options for administrators were added to [Preferences](/en/docs/analytics-platform/using/cja-workspace/user-preferences).

February 2023
Compare Customer Journey Analytics to BI solutions
New document on a
comparison
of Customer Journey Analytics to typical BI solutions.
Update to Audiences documentation
New section on
latency considerations
.
Update to Audiences documentation
After you have created an audience, Adobe creates an Experience Platform
streaming segment for each new Customer Journey Analytics Audience
.
Workspace calendars and date ranges
Updated content to describe relative date ranges, formula calculation updates, and calendar UI changes. See
About relative panel date ranges
.
Mobile scorecards
New documentation section to describe how to show and hide comparison date ranges. See
Show comparison date ranges
in Customer Journey Analytics.
January 2023
Filter and sort tables
Updated content (including adding procedures and explaining available options) in the
Filter and sort tables
article. Renamed this article from “Pagination, filtering and sorting tables.”
Data ingestion quick start guides
New documentation section on how to
ingest and use data
in Customer Journey Analytics.
Workspace Folders
Dedicated pages for
Folders management
.
Workspace User preferences
Many additional user preferences are now available in
Preferences
.
Auto-save for Workspace projects
Updated content to include auto-save functionality in
Save projects
.
Landing page
New landing page updates
landing page
.
Schedule Workbooks
Dedicated page to describe how to
Schedule Workbooks
in Report Builder.
Object array support for profile and lookup datasets
Updated
Use arrays of objects
and
Ingest Adobe Experience Platform audiences
to reflect object array support for profile and lookup datasets.
## 2022

Date
Update description
December 2022
December 16, 2022
New topic on
managing your Customer Journey Analytics data usage
.
October 2022
October 2022
New topic on
password protection of scheduled projects
. This feature is in support of
HIPAA readiness
.
October 2022
New topic on
Customer Managed Keys
. This feature is in support of
HIPAA readiness
.
October 2022
New topic on
Customer Journey Analytics Audit Log
.
October 2022
New topic on
Key metric summary
visualization.
October 2022
New section on
date and date-time functionality in data views
October 2022
Mobile app: New topic on
custom detail views
.
October 2022
Updates to the
Customer Journey Analytics feature support
topic.
September 2022
September 2022
New use case on
Migrating Google Analytics data to Customer Journey Analytics
.
September 2022
New topic on
Combo charts
in Workspace.
September 2022
New topic on
Experimentation panel
in Workspace.
August 2022
August 2022
Adobe Experience Platform article on
Cross-region support for Analytics source connector
.
August 2022
Significantly updated article on
Customer Journey Analytics access control
.
August 2022
New article on
Customer Journey Analytics support for Data Governance labels and policies
.
August 2022
New article on
Comparing terminology for Analytics data passed through the Analytics source connector
.
August 2022
New documentation on
Audience publishing to Real-time Customer Profile
.
July 2022
July 2022
Media Playback Time Spent panel
documentation.
July 2022
Media Concurrent Viewer panel
documentation.
July 2022
First Session
reporting documentation.
June 2022
June 2022
New article on
AAID, ECID, AACUSTOMID and the Analytics source connector
June 2022
New article on
Adobe Analytics processing rules, VISTA and classifications vs. Data Prep for the Analytics source connector
.
June 2022
New article on
virtual reporting environments and sandbox environments
.
June 2022
New article on
comparing data processing across Adobe Analytics and Customer Journey Analytics reporting features
.
June 2022
New article on
combining report suites with different schemas
.
June 2022
New article on
sharing annotations in Mobile scorecards
.
June 2022
New article on
Analytics Labs in Customer Journey Analytics
.
June 2022
New section on
support for numeric fields as lookup keys and lookup values
.
June 2022
Updates to the
Flow visualization workflow
.
May 2022
May 2022
Significantly updated article on
creating connections
in Customer Journey Analytics.
May 2022
New article on how to
manage data blocks in Customer Journey Analytics Report Builder
.
May 2022
New article on
ingesting Adobe Experience Platform audiences into Customer Journey Analytics
.
April 2022
April 2022
Documentation on
dimension substrings
.
April 2022
New
Customer Journey Analytics User Guide for Adobe Analytics users
.
March 2022
March 2022
New
Customer Journey Analytics Annotations API documentation
.
March 2022
New documentation on
Annotations in Workspace
.
March 2022
Significantly updated content on
estimating connection size
.
February 2022
February 2022
A new guide aimed at Administrators who are moving from Adobe Analytics to Customer Journey Analytics:
Adobe Analytics to Customer Journey Analytics evolution
January 2022
January 2022
New use case for
Using binding dimensions and metrics in Customer Journey Analytics
January 2022
Added new feature documentation on
binding dimensions and metrics
and on new
First Known and Last Known allocation settings
January 2022
New article on
comparing your Adobe Analytics data to Analytics data in Customer Journey Analytics
## 2021

Date
Update description
November 2021
November 2021
Updated documentation for
Records skipped
on the Connections Details page.
October 2021
October 2021
Documentation for
Report Builder
in Customer Journey Analytics.
October 2021
Customer Journey Analytics
Audit Log
API documentation
October 2021
Documented
Visualizations for Analytics dashboards
October 2021
Doc for rolling window for Connection
data retention
.
September 2021
September 2021
Metric deduplication
doc
September 2021
Daylight Savings Time support in reporting
September 2021
Customer calendars
documentation
September 2021
Boolean fields
documentation
September 2021
Broke out the component settings in data views into individual files:

- [Component settings overview](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview)
- [Attribution component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/attribution)
- [Behavior component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/behavior)
- [Format component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/format)
- [Include/exclude component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/include-exclude-values)
- [Metric deduplication component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/metric-deduplication)
- [No value component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/no-value-options)
- [Persistence component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/persistence)
- [Value bucketing component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/value-bucketing)

September 2021
New section on the
implications of merging report suites
in Customer Journey Analytics.
August 2021
August 2021
New section on the enhanced
Connections
experience in Customer Journey Analytics.
August 2021
New section on
case sensitivity in Data View dimensions
.
June 2021
June 2021
New documentation on
previous project versions
in Workspace.
April 2021
April 2021
New topic on
persistence
.
April 2021
New documentation on support for scheduled projects in Workspace.
April 2021
New topics on the
enhanced Data Views experience
.
April 2021
New topics on
ingesting Google Analytics data
and
analyzing that data
.
April 2021
Added topic on
scheduled reports
in Workspace.
April 2021
New topic on
high-cardinality dimensions in Customer Journey Analytics
.
March 2021
March 2021
Added topic on support for
Analytics dashboards
(mobile app).
March 2021
New topic on
user preferences
in Workspace.
February 2021
February 2021
New topic on using
Marketing Channel dimensions in Adobe Experience Platform
.
February 2021
Published the new
Customer Journey Analytics API
documentation.
January 2021
January 2021
New topic on
adding standard lookups to your dataset
.
## 2020

Date
Update description
November 13, 2020
New topics on
Cross-Channel Analysis
, which allows you to rekey a dataset’s person ID, and enables a seamless combination of multiple datasets.
November 13, 2020
A new use case on
importing call center and web data
was added.
November 10, 2020
Added a section on the implications of deleting data components to the
FAQ
.
November 2, 2020
Updates to the
Customer Journey Analytics feature support
page.
November 2020
Added content on
removing backfill limitations
for connections.
October 7, 2020
Added a topic on
combined event datasets
.
September 15, 2020
Added a topic on
data ingestion
.
September 2, 2020
Updated section on
user permissions
.
July 2020
Added information on
Identity Map option for Person ID
.
July 2020
New topic on
object arrays
or ‘data hierarchies’ added.
April 14, 2020
Updates to the latest UI in the
Create Connections
topic.
February 27, 2020
Updates to the
Customer Journey Analytics feature support
December 2019
First draft of Customer Journey Analytics documentation
recommendation-more-help
