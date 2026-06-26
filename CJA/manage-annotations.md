---
title: "Manage annotations"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/annotations/manage-annotations"
category: "other"
topic: "analytics-platform/using/cja-components/annotations"
created_at: "2026-06-02T19:08:13.529913+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage annotations

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

You can share, filter, tag, approve, copy, delete annotations and mark annotations as favorite from a central Annotations management interface. To manage annotations:

- Select **Components** in the main interface, then select **Annotations**.

NOTE
The annotations that you create within a specific Workspace project do not appear in the Annotations manager, unless you have made the annotation available to all your projects.
## Annotations manager

The Annotations manager has the following interface elements:

### Annotations list

The annotations list ➊ displays all the annotations that you own, the annotations that have been scoped to all your projects, and the annotations that have been shared with you. The list has the following columns:

Column
Description
Select to favor
or un-favor
an annotation.
Title and description
Provided in the Annotations Builder. To edit the title and description, select the title link - opens the
Annotations builder
. A shared annotation is indicated with
.
Data view
The data views that this annotation applies to.
Owner
The owner of the annotation. As a user, you only see the annotations that you own or the annotations that are shared with you.
Applied date range
The date or date range that this annotation applies to.
Tags
The tags for this annotation.
Shared with
The individuals or groups that you shared the annotation with. Select to open the
Share Component
dialog.
Date modified
Displays the date and time that the annotation was last modified.
Use to specify which columns you want to display.

### Action bar

You can action on annotations using the action bar ➋. The action bar contains the following actions:

Icon
Action
Description
Add
Add another annotation, using the
Annotation builder
.
Search by title
When no annotation is selected in the list, search for annotations using this search field.
Tag
Tag the selected annotations. In the
Tag Component
dialog, select or de-select the tags for the selected annotations. Select
Save
to save the tags for the selected annotations.
Share
Share the selected annotations. In the
Share Component
dialog, you can
Search individuals or groups
or you can select
Organization
or
Groups
. Select
Save
to save share details for the selected annotations. See
Share annotations
for more details.
Delete
Delete the selected annotations. You are prompted for a confirmation.
Rename
Rename a single selected annotation. When selected, you can rename the annotation inline.
Copy
Copy the selected annotations. New annotations are created with the same name and suffix (Copy)
Export to CSV
Export the annotations to an
Annotations List.csv
file.
### Active filter bar

The filter bar ➌ shows the active filters (if any). You can quickly remove a filter using . If more than one filter is specified, you can remove all filters using **Remove all**.

### Filter panel

You can filter annotations using the **Filter** left panel ➍. The filter panel displays the type of filter and the number of annotations that honor the filter. Select to toggle the display of the filter panel.

To filter the list of filters:

- Select to open the Filters panel. If you need more space for the Filters list, you can select once more to close the panel.
- You can filter the annotations using any of the available filter sections . note info INFO Items refer to the annotation items displayed in the Annotations list .

#### Filter sections

Tags
Description
{width="300"}
The **Tags** section lets you filter on tags.

- You can Search Tags to search for tags you can use to filter.
- You can select more than one tag. The tags available depend on selections made in other sections in the filter panel.
- The numbers indicate: (1) : The number of selected tags (if one or more tags are selected). 2︎⃣ : The number of tags available for the items resulting from the current filter. 7︎⃣: The number of items associated with the specific tag.

Data view
Description
—
—
{width="300"}
The **Data view** section lets you filter on data views.

- You can Search Data views to search for data views you can use to filter.
- You can select more than one data view. The data views available depend on selections made in other sections in the filter panel.
- The numbers indicate: (2) : The number of selected data views (if one or more data views are selected). 3︎⃣ : The number of data views available for the items resulting from the current filter. 4︎⃣: The number of items associated with the specific data view.

Owner
Description
—
—
{width="300"}
The **Owner** section lets you filter on owners.

- You can Search Owners to search for owners you can use to filter.
- You can select more than one owner. The owners available depend on selections made in other sections in the filter panel.
- The numbers indicate: (2) : The number of selected owners (if one or more owners are selected). 3︎⃣ : The number of owners available for the items resulting from the current filter. 4︎⃣: The number of items associated with the specific owner.

Applied date range
Description
—
—
{width="300"}
The Applied date range section let you filter on a date range applicable to the items.

- Select a date range.
- In the calendar popup define a date range, or select one of the available presets.Alternatively, you can also specify a date range directly in the Date range section of the Filter panel.

- The numbers indicate: (1) : The number of modified date ranges modified from default presets. 5︎⃣ : The number of date ranges available for the items resulting from the current filter.

Other filters
Description
—
—
{width="300"}
The **Other filters** section lets you filter on other predefined filter.

- You can select one or more of the following options: Show all Shared with me Mine Approved Favorites What you can select depends on your role and permissions.
- You can select more than one other filter. The other filters available depend on selections made in other sections in the filter panel.
- The numbers indicate: (1) : The number of selected other filters (if one or more other filters are selected). 5︎⃣ : The number of other filters available for the items resulting from the current filter. 4︎⃣: The number of items associated with the specific other filter.

The [Annotations list](/en/docs/analytics-platform/using/cja-components/annotations/manage-annotations#annotations-list) is automatically updated based on your filter configuration. You can see the configured filters in the [Active filter bar](/en/docs/analytics-platform/using/cja-components/annotations/manage-annotations#active-filter-bar).

## Edit annotations

You can edit an annotation in two ways:

- In a Workspace project, use the Component info icon.
- In the Annotations list , select the title of the annotation.

You use the [Annotation builder](/en/docs/analytics-platform/using/cja-components/annotations/create-annotations#annotation-builder) to edit the annotation.

## Share annotations

The following applies when sharing annotations or working with annotations that are shared with you:

- Project-only annotations in a project you share with other users are displayed for those users. The users cannot edit or delete these project-only annotations.
- If you save an annotation and share the annotation directly with a user, that user can edit and delete the annotation only if that user has admin rights.
- If a project is shared with you, annotations created in that project show up only in that project. If an annotation is shared directly with you, the annotation shows up in all projects where that annotation can be displayed.

## Annotations and time zones

All annotations are created with a timestamp, but no hour or timezone information. At report time, the timezone of the data view configured for the panel is used.

recommendation-more-help
