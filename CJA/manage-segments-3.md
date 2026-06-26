---
title: "Manage segments"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-filters/manage-filters?lang=en"
category: "other"
topic: "analytics-platform/using/cja-components/cja-filters"
created_at: "2026-06-02T19:07:13.376103+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage segments

Last update: May 13, 2026
- Topics:
- [Filters](#)
- [Segments](#)

CREATED FOR:

- User

You can [share](/en/docs/analytics-platform/using/cja-components/segments/seg-share), [segment](/en/docs/analytics-platform/using/cja-components/segments/seg-filter), [tag](/en/docs/analytics-platform/using/cja-components/segments/seg-tag), [approve](/en/docs/analytics-platform/using/cja-components/segments/seg-approve), rename, [copy](/en/docs/analytics-platform/using/cja-components/segments/seg-copy), delete, export segments and mark segments as [favorite](/en/docs/analytics-platform/using/cja-components/segments/seg-favorite) from a central Segment management interface. To manage segments:

- Select **Components** in the main interface, then select **Segments**.

NOTE
The quick segments that you create within a specific Workspace project do not appear in the Segment manager, unless you have made the segment available to all your projects.
## Segment manager

The Segment manager has the following interface elements:

### Segment list

The segments list ➊ displays all the segments that you own, the segments that have been scoped to all your projects, and the segments that have been shared with you. The list has the following columns:

Column
Description
Select to favor
or un-favor
a segment. See
Mark segment as favorite
Title and description
To edit the segment, select the title link, which opens the
Segment builder
. A shared segment is indicated with
.
Data view
The data views that this segment applies to.
Owner
The owner of the segment. As a user, you only see the segments that you own or the annotations that are shared with you.
Tags
The tags for this segment.
Shared with
How many individuals or groups that you shared the segment with. Select to open the
Share Component
dialog. See
Share segments
for more information.
Date modified
The date and time that the segment was last modified.
Used in
Show where segments are currently being used, and how many times they are being used in each area.

For example, if the segment is being used in 40 projects and 2 alerts, then the value of this column shows as **42 components**.

Select the value in this column to see the breakdown of where the segments are being used (for example, **Projects (40)**, **Mobile Scorecards (2)**). Furthermore, you can view the list of items where the segments are being used. For example, so see the list of projects where they are being used, select the **Projects (40)** link.

Each of the following areas shows the number of instances of segments being used in that area:

- Projects Contains segments that were created in the segment builder and are available for all projects.
- Ad hoc components Contains segments that were created as quick segments and are available only within a single project.
- Scheduled projects
- Mobile Scorecards
- Annotations
- Calculated metrics
- Report Builder Selecting this option downloads a CSV file with the following columns of data: Report Builder Name Last accessed Last accessed IMS User ID Last accessed user name

This information helps you to determine whether a component is valuable to users in your organization, where the component is used, and if the component needs to be deleted or modified.

Consider the following when viewing this column:

- This information is available only to system administrators.
- The **Used in** column does not display by default. Use to configure the display of this column.
- This information does not include usage from the API or Data Warehouse.
- If there is no data in this column for a given component but the component has a **Last used** date, the component might have been used in an analysis without being saved.
- Usage information is available starting in September 2023.

You can use the [Data Dictionary](/en/docs/analytics-platform/using/cja-components/data-dictionary/data-dictionary-overview) along with this information to help you keep track of and better understand how components are being used in your organization.

Last Used
When the segment was last used.
Use to specify which columns you want to display.

### Action bar

You can action on segments using the action bar ➋. The action bar contains the following actions:

Action
Description
Add
Add another segment, using the
Segment builder
.
Search by title
When no segment is selected in the list, search for segments using this search field.
Tag
Tag the selected segments. In the
Tag Segment
dialog, select or de-select the tags for the selected segments. Select
Save
to save the tags for the selected segments. See
Tag segments
for more information.
Share
Share the selected segments. In the
Share Segment
dialog, you can
Search individuals or groups
or you can select
Organization
or
Groups
. Select
Save
to save share details for the selected segments. See
Share segments
for more information.
Delete
Delete the selected segments. You are prompted for a confirmation.When you delete a segment, be aware that:

- Scheduled reports and projects that have this segment applied continue to work normally.
- Scheduled reports do not update when you edit a segment with the same name.

Rename
Rename a single selected segment. When selected, you can rename the segment inline.
Approve
Approve the selected segments. See
Approve segments
for more information.
Copy
Copy the selected segment. New segments are created with the same name and suffix
(Copy)
.
Export to CSV
Export the segments to a
Segments List.csv
file.
### Active filter bar

The filter bar ➌ shows the active segments applied from the filter panel to the list of segments (if any). You can quickly remove a filter using . If more than one filter is specified, you can remove all filter using **Remove all**.

### Filter panel

You can filter the list of segments using the **Filter** left panel ➍. The filter panel displays the type of filter and the number of segments that honor the specific filter. Select to toggle the display of the Filter panel.

See [Filter the list of segments](/en/docs/analytics-platform/using/cja-components/segments/seg-filter) for more information.

recommendation-more-help
