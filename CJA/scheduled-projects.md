---
title: "Scheduled projects"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/scheduled-projects-manager"
category: "other"
topic: "analytics-platform/using/cja-components/scheduled-projects-manager"
created_at: "2026-06-02T19:05:44.369105+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Scheduled projects

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

Scheduled Analysis Workspace projects can be managed in Customer Journey Analytics using **Components** > **Scheduled projects**.

In **Scheduled Projects**, you can edit and delete recurring project schedules. The [Scheduled project list](#scheduled-project-list) shows the items that a specific user has created. If the user account is disabled in the application, all scheduled deliveries will stop.

## Scheduled project list

The Scheduled projects list ➊ displays columns for:

Column
Description
When one or more scheduled projects are selected, a blue action bar appears at the bottom of the Scheduled Projects interface. See
Actions
for more details.
Select to favor
or un-favor
a scheduled project.
Schedule ID
An ID that is used mainly for debugging purposes.
Name
Name of this project.Select to see more details for the scheduled project.Select to open a context menu. From this menu you can:

- **Delete** a scheduled project.
- **Tag** a scheduled project.
- **Approve** a scheduled project.
- **Export CSV**: Export a scheduled project to a CSV file.

Owner
The person who created and owns the project.
Tags
(optional) Tagging is a good way to organize projects. All users can create tags and apply one or more tags to a project. However, you can see tags only for those projects that you own or that have been shared with you.
Delivered to
The recipients of this scheduled project.
Expiration date
You can set the expiration date to up to one year, regardless of schedule frequency.
Frequency
How often you want to have this schedule project sent to one or more recipients.
Execution Time
At what time of day this scheduled project gets sent.
Number of Queries
The number of queries against this project.
Longest Date Range
The longest date range defined for the scheduled project. This value might be relevant to investigate performance issues. See
Reporting Activity Manager
for more information.
Number of queries
The number of queries executed for the scheduled project. This value might be relevant to investigate performance issues. See
Reporting Activity Manager
for more information.
You can use to configure which columns to display.

Search for a scheduled project using . You can also see if any filters are applied from the Filters panel. To remove a filter, select for a filter. To remove all filters, select **Clear all**.

To edit a scheduled project, select the title of the scheduled project. Use the **Edit scheduled project** dialog to update the schedule details. See [Send files to other](/en/docs/analytics-platform/using/cja-workspace/export/t-schedule-report) for more details.

Select **Update** to update the schedule.

## Actions

The following are common actions in the Scheduled Projects manager. You can select actions from the context menu or from the blue action bar when selecting one or more scheduled projects.

Icon
Action
Description
x
selected
Select to unselect your selected scheduled projects.
Delete
Delete the selected scheduled projects for the project; the projects are not deleted.

For information about deleting a project, see [Projects overview](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/freeform-overview).

Tag
Tag the selected scheduled projects. In the
Tag Scheduled projects
select tags and select
Save
to save.
Approve
Approve the selected scheduled projects.
Export to CSV
Export the selected scheduled projects to a file named
Export Scheduled Projects List.csv
.
## Filter

You can filter the scheduled projects [Scheduled Project list](#scheduled-project-list) using the filter panel ➌. To show or hide the filter panel use .

The filter panel consists of the following sections.

### Tags

Tags
Description
{width="300"}
The **Tags** section lets you filter on tags.

- You use **Search Tags** to search for tags you want to use to filter.
- You can select more than one tag. The tags available depend on selections made in other sections in the filter panel.
- The numbers indicate: 7︎⃣: The number of scheduled projects associated with the specific tag.

### Owners

Owner
Description
{width="300"}
The **Owner** section lets you filter on owners.

- You use *Search Owners* to search for owners you want to use to filter.
- You can select more than one owner. The owners available depend on selections made in other sections in the filter panel.
- The numbers indicate: 4︎⃣: The number of scheduled projects associated with the specific owner.

### Other filters

Other filters
Description
{width="300"}
The **Other filters** section lets you filter on other predefined filter.

- You can select one or more of the following options: Expired : Filter on expired scheduled projects. Failed : Filter on scheduled projects for which the schedule has failed. What you can select depends on your role and permissions.
- You can select more than one other filter. The other filters available depend on selections made in other sections in the filter panel.
- The numbers indicate: 4︎⃣: The number of scheduled projects associated with the specific other filter.

recommendation-more-help
