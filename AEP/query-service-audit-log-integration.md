---
title: "Query Service audit log integration"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/query/data-governance/audit-log-guide"
category: "guides"
topic: "experience-platform/query-service-guide"
created_at: "2026-05-29T17:06:38.319008+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Query Service Guide

# Query Service audit log integration

Last update: May 23, 2026
- Topics:
- [Queries](#)

CREATED FOR:

- User
- Developer

The Adobe Experience Platform Query Service audit log integration provides records of query-related user actions. Audit logs are an essential tool for troubleshooting and adhering to corporate data stewardship policies and regulatory requirements. The capability allows you to return an action log for many event types and filter and export the records. The logs can be accessed either through the Experience Platform UI or the [Audit Query API](https://www.adobe.io/experience-platform-apis/references/audit-query/) and downloaded in either CSV or JSON file formats.

To learn more about the audit logs user interface, refer to the [audit logs overview document](/en/docs/experience-platform/landing/governance-privacy-security/audit-logs/overview). To learn more about making calls to Experience Platform APIs, refer to the [audit logs API guide](/en/docs/experience-platform/landing/platform-apis/api-guide).

NOTE
Session eviction actions are logged. For UI workflows, see
Manage Query Service sessions
.
## Prerequisites

You must have the Data Governance View User Activity Log permission enabled to view the audit log dashboard within the Experience Platform UI. The permission is enabled through the Adobe [Admin Console](https://adminconsole.adobe.com/). Please contact your organization’s administrator if you do not have administrator privileges to enable this permission. See the access control documentation for [full instructions on adding permissions through Admin Console](/en/docs/experience-platform/access-control/home).

## Query Service audit log categories audit-log-categories

The audit log categories provided by Query Service are as follows.

Category
Description
Query
This category allows you to audit query executions.
Query template
This category allows you to audit the various actions (create, update, and delete) taken on a query template.
Scheduled query
This category allows you to audit the schedules that have been created, updated, or deleted within Query Service.
## Perform a Query Service audit log perform-an-audit-log

To perform an audit for Query Service activities, select **Audits** from the left navigation, followed by the funnel icon ( ) to display a list of filter controls to help narrow results.

From the Audits dashboard Activity log tab, you can filter all the recorded Experience Platform actions by any of the Query Service categories. The log results can be further filtered based on the time period they were executed, the action/function taken, or the user that enacted the query. See the audit log documentation for [full instructions on how to filter the logs based on category, action, user, and status](/en/docs/experience-platform/landing/governance-privacy-security/audit-logs/overview#managing-audit-logs-in-the-ui).

The returned audit log data contains the following information on all queries that meet your chosen filter criteria.

Column name
Description
Timestamp
The exact date and time of the action performed in a
month/day/year hour:minute AM/PM
format.
Asset Name
The value for the Asset Name field depends on the category chosen as a filter. When using the Scheduled query category this is the
schedule name
. When using the Query template category, this is the
template name
. When using the Query category, this is the
session ID
Category
This field matches the category selected by you in the filter dropdown.
Action
This can be either create, delete, update, or execute. The available actions depend on the category chosen as a filter.
User
This field provides the user ID that executed the query.
NOTE
More query details are provided by downloading the log results in either CSV or JSON file formats, than are displayed by default in the audit log dashboard.
## Details panel

Select any row of audit log results to open a details panel to the right of the screen.

The details panel can be used to find the Asset ID and the Event status.

The value of the Asset ID changes depending on the category used in the audit.

- When using the Query category, the Asset ID is the **session ID**.
- When using the Query template category, the Asset ID is the **template ID** and prefixed with templateID:.
- When using the Scheduled query category, the Asset ID is the **schedule ID** and prefixed with scheduleID:.

The value of the Event status changes depending on the category used in the audit.

- When using the Query category, the Event status field provides a list of all **query IDs** executed by the user within that session.
- When using the Query template category, the Event status field provides the **template name** as a prefix for the event status.
- When using the Query schedule category, the Event status field provides the **schedule name** as a prefix for the event status.

## Available filters for Query Service audit log categories available-filters

Available filters vary depending on the category selected in the dropdown. The following table details the filters available for [Query Service audit log categories](#audit-log-categories).

Filter
Description
Category
See the
Query Service audit log categories
section for a complete list of available categories.
Action
When referring to Query Service audit categories, update is a
modification to the existing form
, delete is the
removal of the schedule or template
, create is
creating a new schedule or template
, and execute is
running a query
.
User
Enter the complete user ID (for example, johndoe@acme.com) to filter by user.
Status
The Allow, Success, and Failure options filter the logs based on the “Status” or “Event Status” whereas the Deny option will filter out
all
logs.
Date
Select a start date and/or an end date to define a date range to filter results by.
## Next steps

By reading this document, you have a better understanding of the Query Service audit log capability and how it can be used to filter your Query Service user actions.

If you are using the Query Service audit log capability for troubleshooting purposes, you are recommended to read the [troubleshooting guide](/en/docs/experience-platform/query/troubleshooting-guide).

recommendation-more-help
