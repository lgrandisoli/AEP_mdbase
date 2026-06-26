---
title: "Manage calculated metrics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-manager?lang=en"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-02T19:07:11.398533+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage calculated metrics

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User
- Admin

You can share, filter, tag, approve, rename, copy, delete, export calculated metrics and mark calculated metrics as favorite from a central Calculated metrics management interface. To manage calculated metrics:

- Select **Components** in the main interface, then select **Calculated metrics**.

## Calculated metrics manager

The Calculated metrics manager has the following interface elements:

### Calculated metrics list

The calculated metrics list ➊ displays all the calculated metrics that you own or that have been shared with you. The list has the following columns:

Column
Description
Select to favor
or un-favor
a calculated metric. See
Mark calculated metric as favorite
Title and description
To edit the calculated metric, select the title link, which opens the
Calculated metrics builder
. A shared calculated metric is indicated with
.
Data view
The data views that this calculated metric applies to.
Owner
Owner of the calculated metric. As a user, you only see the annotations that you own or the annotations that are shared with you.
Tags
Lists the tags for this calculated metric.
Shared with
Lists how many individuals or groups that you shared the calculated metric with. Select to open the
Share Calculated metric
dialog. See
Share calculated metrics
for more information.
Date modified
The date and time that the calculated metric was last modified.
Used in
Shows where calculated metrics are currently being used, and how many times they are being used in each area.

For example, if the calculated metric is being used in 40 projects and 2 alerts, then the value of this column shows as **42 components**.

Select the value in this column to see the breakdown of where the calculated metrics are being used (for example, **Projects (40)**, **Mobile Scorecards (2)**). Furthermore, you can view the list of items where the calculated metrics are being used. For example, so see the list of projects where they are being used, select the **Projects (40)** link.

Each of the following areas shows the number of instances of calculated metrics being used in that area:

- Projects Contains calculated metrics that were created in the calculated metric builder and are available for all projects.
- Ad hoc components Contains calculated metrics that were created as quick calculated metrics and are available only within a single project.
- Scheduled projects
- Mobile Scorecards
- Annotations
- Report Builder Selecting this option downloads a CSV file, with the following columns of data: Report Builder Name Last accessed Last accessed IMS User ID Last accessed user name

This information can help you determine whether a component is valuable to users in your organization, where it is used, and if it needs to be deleted or modified.

Consider the following when viewing this column:

- This information is available only to system administrators.
- The **Used in** column does not display by default. Use to configure the display of this column.
- This information does not include usage from the API or Data Warehouse.
- If there is no data in this column for a given component but it has a **Last used** date, the component might have been used in an analysis without being saved.
- Usage information is available starting in September 2023.

You can use the [Data Dictionary](/en/docs/analytics-platform/using/cja-components/data-dictionary/data-dictionary-overview) along with this information to help you keep track of and better understand how components are being used in your organization.

Last Used
When the calculated metric was last used.
Use to specify which columns you want to display.

### Action bar

You can action on filters using the action bar ➋. The action bar contains the following actions:

Icon
Action
Description
Add
Add another calculated metrics, using the
Calculated metric builder
.
Search by title
When no calculated metric is selected in the list, search for filters using this search field.
Tag
Tag the selected calculated metrics. In the
Tag Calculated metric
dialog, select or de-select the tags for the selected calculated metric. Select
Save
to save the tags for the selected calculated metrics. See
Tag calculated metrics
for more information.
Share
Share the selected calculated metrics. In the
Share Calculated metrics
dialog, you can
Search individuals or groups
or you can select
Organization
or
Groups
. Select
Save
to save share details for the selected calculated metrics. See
Share calculated metrics
for more information.
Delete
Delete the selected calculated metrics. You are prompted for a confirmation.
Rename
Rename a single selected calculated metric. When selected, you can rename the calculated metric inline.
Approve
Approve the selected calculated metrics. See
Approve calculated metrics
.
Copy
Copy the selected calculated metrics. New calculated metrics are created with the same name and suffix
(Copy)
Export to CSV
Export the calculated metrics to a
Calculated metric List.csv
file.
### Active filter bar

The filter bar ➌ shows the active filters applied from the filter panel to the list of calculated metrics (if any). You can quickly remove a filter using . If more than one filter is specified, you can remove all filters using **Remove all**.

### Filter panel

You can filter the list of calculated metric using the **Filter** left panel ➍. The filter panel displays the type of filter and the number of calculated metrics that honor the specific filter. Select to toggle the display of the filter panel.

See [Filter the list of calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-filter) for more information.

recommendation-more-help
