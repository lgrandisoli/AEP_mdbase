---
title: "Manage published audiences"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/audiences/manage"
category: "other"
topic: "analytics-platform/using/cja-components/audiences"
created_at: "2026-06-02T19:08:15.366107+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage published audiences

Last update: May 13, 2026
- Topics:
- [Audiences](#)

CREATED FOR:

- User

Audiences can be managed in Customer Journey Analytics using **Components** > **Audiences**.

## Understand audience management tasks

Managing previously created audiences lets you:

- **Schedule or de-schedule** automatic audience refresh/update. The maximum expiration on the schedule is 1 year.
- **Renew an audience refresh schedule** when it is about to expire. Expiring audiences are treated similarly to expiring scheduled reports - the admin gets an email a month before the schedule expires.
- View the **refresh interval** and the **last time that an audience was updated**
- Gain insight into the **amount of time it took to produce an audience** from Customer Journey Analytics. And the amount of time it took to have the audience appear in Real-time Customer Platform for activation purposes.
- See whether the audiences in Customer Journey Analytics are **being actively used by Real-time Customer Platform**. Or (ideally) any Experience Platform applications that consume the audiences created by Customer Journey Analytics.

If you do have [Audience View](/en/docs/analytics-platform/using/technotes/access-control#user-level-access) access, you can view audiences. If you do have [Audience Create](/en/docs/analytics-platform/using/technotes/access-control#user-level-access) access, you can edit and delete audiences.

## View audiences in the Audiences list

The Audiences list ➊ shows the existing audiences.

To view the Audience list:

- In Customer Journey Analytics, select Components > Published audiences .
- (Optional) Use to configure which columns to display.
- (Optional) Search for an audience using . The following columns are available with information about each audience: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 Column Description When one or more audiences are selected, a blue action bar appears at the bottom of the Audiences interface. See Actions for more details. Title & Description The title and description you entered when you created the audience. Data view The data view in which this audience was created. Audience size The total number of people in this audience. Owner The owner of the audience - the person who created the audience. Refresh frequency The refresh interval configured when the audience was created. Tags Any tags that are applied to this audience. Publishing status Can show Ready , In progress , or Error . Last refreshed Timestamp when the audience was last refreshed. Last modified Timestamp when the audience was last edited or modified.

## Edit audiences

You can edit the settings of an audience at any time. When you edit an audience (either a one-time audience or a recurring audience), a republish is required.

To edit an audience:

- In Customer Journey Analytics, select Components > Published audiences . The Audiences page is displayed.
- Select the title of the audience that you want to edit. The Edit audience dialog displays.
- You can update any of the available fields for the audience. For information about the fields you can update, see Audience builder in the article, Create and publish audiences .
- Select Republish .

## Actions

The following are common actions in the Scheduled Projects manager. You can select actions from the context menu:

Icon
Action
Description
Tag
Tag the selected audiences. In the
Update tags:
audience name
dialog, select tags from the drop-down menu or type one or more new tags. Select
Save
to save.
Delete
Delete the selected audiences.
Rename
Rename the selected audience. Use the
Rename:
audience name
dialog to rename the audience and select
Save
to save.
The following actions are available from the blue action bar when selecting one or more scheduled projects.

Icon
Action
Description
x
selected
Select to unselect your selected audiences.
Delete
Delete the selected audiences.
Export to CSV
Export the selected audiences to a file named
audiences.csv
.
## Filter the audience list

You can filter the [Audiences list](#audiences-list) using the filter panel ➋. To show or hide the filter panel use .

The filter panel consists of the following sections.

### Data view

Data view
Description
{width="300"}
The **Data view** section lets you filter on data views.

- You use to search for data views you want to use to filter.
- You can select more than one data view.

### Owners

Owner
Description
{width="300"}
The **Owner** section lets you filter on owners.

- You use to search for owners you want to use to filter.
- You can select more than one owner.

## Refresh frequency

Refresh frequency
Description
{width="300"}
The **Refresh frequency** section lets you filter on refresh frequency.

- You use to search for refresh frequency you want to use to filter.
- Only the refresh frequencies defined for the audiencesin the [Audiences list](#audiences-list) are shown as available options.

### Tags

Tags
Description
{width="300"}
The **Tags** section lets you filter on tags.

- You use to search for tags you want to use to filter.

recommendation-more-help
