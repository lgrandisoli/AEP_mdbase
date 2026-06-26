---
title: "Manage alerts"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/alerts/alert-manager"
category: "other"
topic: "analytics-platform/using/cja-components/alerts"
created_at: "2026-06-02T19:08:38.983859+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage alerts

Last update: May 22, 2026
- Topics:
- [Workspace Basics](#)

CREATED FOR:

- User
- Admin

You can filter, tag, delete, rename, copy, enable, disable renew, and export alerts from a central Alerts management interface. To manage alerts:

- Select **Components** in the main interface, then select **Alerts**.

The Alerts manager is structured like the [Segment manager](/en/docs/analytics-platform/using/cja-components/segments/seg-manage) and the [Calculated metric manager](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-manager).

## Alerts manager

The Alerts manager has the following interface elements:

### Alerts list

The alerts list ➊ displays the alerts that you have created. If you are an administrator, you see all alerts.

The list has the following columns:

Column
Description
Select to favor
or un-favor
an alert.
Title and description
To edit the alert, select the title link, which opens the
Alerts builder
.
Type
Shows whether the alert is a Customer Journey Analytics data alert or a Server call usage alert.
Enabled
Indicates whether the alert is enabled or disabled.
Data view
The data views that this alert applies to.
Owner
The owner of the alert. As a non-administrator, you only see alerts that you own. An administrator can see all alerts.
Tags
The tags for this alert.
Expiration Date
The date and time when the alert is set to expire.
Date modified
The date and time that the alert was last modified.
Use to specify which columns you want to display.

### Action bar

You can action on alerts using the action bar ➋. The action bar contains the following actions:

Icon
Action
Description
Add
Add another alert, using the
Alert builder
.
Search by title
When no alert is selected in the list, search for alerts using this search field.
Tag
Tag the selected alerts. In the
Tag Alert
dialog, select or de-select the tags for the selected alerts. Select
Save
to save the tags for the selected alerts.
Delete
Delete the selected alerts. You are prompted for a confirmation.
Rename
Rename a single selected alert. When selected, you can rename the alert inline.
Copy
Copy the selected alert. New alerts are created with the same name and suffix
(Copy)
.
Enable
or
Disable
Enable or disable the selected alerts.
Renew
Renews the alert expiration date. The expiration date extends 1 year from the day you select this option, regardless of the original expiration date.
Export to CSV
Export the alerts to an
Alerts List.csv
file.
### Active filter bar

The filter bar ➌ shows the active filters applied from the filter panel to the list of alerts (if any). You can quickly remove a filter using . If more than one filter is specified, you can remove all filters using **Remove all**.

### Filter panel

You can filter the list of alerts using the **Filter** left panel ➍. The filter panel displays the type of filter and the number of alerts that honor the specific filter.

- Select to open the Filters panel. If you need more space for the Alerts list, you can select once more to close the panel.
- Select filters from any of the available filter sections.

#### Tags filter section

Tags
Description
{width="300"}
The **Tags** section lets you filter on tags.

- You can Search Tags to search for tags you can use to filter.
- You can select more than one tag. The tags available depend on selections made in other sections in the filter panel.
- The numbers indicate: (1) : The number of selected tags (if one or more tags are selected). 2︎⃣ : The number of tags available for the items resulting from the current filter. 7︎⃣: The number of items associated with the specific tag.

#### Data view filter section

Data view
Description
{width="300"}
The **Data view** section lets you filter on data views.

- You can Search Data views to search for data views you can use to filter.
- You can select more than one data view. The data views available depend on selections made in other sections in the filter panel.
- The numbers indicate: (2) : The number of selected data views (if one or more data views are selected). 3︎⃣ : The number of data views available for the items resulting from the current filter. 4︎⃣: The number of items associated with the specific data view.

#### Owners filter section

Owner
Description
{width="300"}
The **Owner** section lets you filter on owners.

- You can Search Owners to search for owners you can use to filter.
- You can select more than one owner. The owners available depend on selections made in other sections in the filter panel.
- The numbers indicate: (2) : The number of selected owners (if one or more owners are selected). 3︎⃣ : The number of owners available for the items resulting from the current filter. 4︎⃣: The number of items associated with the specific owner.

#### Enabled status filter section

Enabled status
Description
{width="300"}
The **Enabled status** section lets you filter on enabled status.

- You can select more than one status.
- The numbers indicate: (2) : The number of selected statuses (if one or more statuses are selected). 2︎⃣ : The number of statuses available for the items resulting from the current filter. 1︎⃣: The number of items associated with the specific status.

#### Type filter section

Type
Description
{width="300"}
The **Type** section lets you filter on type.

- You can select more than one type.
- The numbers indicate: (2) : The number of selected types (if one or more types are selected). 1︎⃣ : The number of types available for the items resulting from the current filter. 3︎⃣: The number of items associated with the specific type.

#### Other filters filter section

Other filters
Description
{width="300"}
The **Other filters** section lets you filter on other predefined filter.

- You can select one or more of the following options: Show all Shared with me Mine Approved Favorites What you can select depends on your role and permissions.
- You can select more than one other filter. The other filters available depend on selections made in other sections in the filter panel.
- The numbers indicate: (1) : The number of selected other filters (if one or more other filters are selected). 5︎⃣ : The number of other filters available for the items resulting from the current filter. 4︎⃣: The number of items associated with the specific other filter.

## Edit alerts

You can edit an alert

- In the [Alert list](#alerts-list), select the title of the alert.

You use the [Alert builder](/en/docs/analytics-platform/using/cja-components/alerts/alert-builder#alert-builder) to edit the alert.

## Troubleshoot an alert

When troubleshooting an issue with an alert, provide the JID (Job Instance ID) number to Adobe Support. The JID number is located at the bottom of the alert email notification you receive.

recommendation-more-help
