---
title: "Manage exports"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/exports/manage-exports"
category: "other"
topic: "analytics-platform/using/cja-components/exports"
created_at: "2026-06-02T19:04:26.351060+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage exports

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

After you export a full table as described in [Export Customer Journey Analytics reports to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud), the exports are available on the Exports tab on the Exports page.

You can see only the exports that you create. Administrators can view all exports by enabling the option **View exports for all users**.

## Filter and search for exports

To find information you need, you can either filter the list of exports or search for an export.

### Filter the list of exports

- In Customer Journey Analytics, select Components > Exports .
- Select the Exports tab.
- Select the Filter icon . You can filter by the following criteria: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Filter Description Account type The account type that the export is associated with. The following account types are available: AEP Data Landing Zone Amazon S3 Role ARN Azure SAS Azure RBAC Google Cloud Platform Snowflake . Status The status of the export. The following statuses are available: Active : Indicates that a scheduled export has not yet expired, or that a one-time export has not yet completed. Completed : Indicates that an export has successfully exported. For scheduled exports, this indicates that the schedule has expired. Failed The following situations can result in a failed export. Hover over the Failed status to see details about the failure. Scheduled export expiration Row limit reached for scheduled export Expired : Indicates that the export has expired. Created by The user who created the export. This option is available only to administrators when the View exports for all users option is enabled. Frequency How often the export occurs. The following frequencies are available: One time Daily Weekly Monthly Yearly

### Search for exports

- In Customer Journey Analytics, select Components > Exports .
- Select the Exports tab.
- In the search field, begin typing any information associated with the export you’re searching for. You can search for data from any column available in the table.

## Edit an export

You can edit an export’s properties, format, scheduling, and location information.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the checkbox next to the export you want to edit. This option is not available when selecting multiple exports.
- Select Edit . The Export full table dialog displays.
- Update any of the available options. For information about each option, see Export full tables from Analysis Workspace in Export Customer Journey Analytics reports to the cloud .

## Renew an export

You can renew one or more scheduled exports before or after they expire. The exports are renewed for 1 year from the date you renew them.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the checkbox next to one or more exports that you want to renew.
- Select Renew . The Export full table dialog displays.
- Update any of the available options. For information about each option, see Export full tables from Analysis Workspace in Export Customer Journey Analytics reports to the cloud .

## Duplicate an export

You can duplicate an existing export.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the checkbox next to the export you want to duplicate. This option is not available when selecting multiple exports.
- Select Duplicate . A duplicate of the export is created. The name of the new export matches the name of the original export, with - Copy appended to the file name.
- (Optional) Edit the new export , including the file name and any other properties you want to change.

## Manually initiate an export

You can manually initiate an export, either for a scheduled export or a one-time export that previously completed.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the checkbox next to the export you want to run. This option is not available when selecting multiple exports.
- Select Export now .

## Tag an export

When you apply tags to an export, you can view those tags in the Tags column on the Exports page. See [Configure columns](#configure-columns-on-the-exports-page) for more information.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the checkbox next to one or more exports that you want to tag.
- Select Edit tags .
- In the Tag export dialog, type the name of a tag to create a new tag, or choose an existing tag from the drop-down menu. Any common tags between the selected exports are shown in the tag dialog.
- Select Apply tags .

## Delete an export

You can delete exports from the Exports page. Deleting an export removes it from the exports page. Scheduled exports that are deleted are canceled and no longer be sent.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the checkbox next to one or more exports that you want to delete.
- Select Delete , then select Delete when you see the confirmation message.

## Configure columns on the Exports page

You can add or remove columns on the Exports tab to configure what information is displayed.

Select a column header to sort the exports by that column. By default, exports are sorted by the date and time the export was last modified.

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select the Customize table icon in the upper-right of the Exports page. The following columns are available: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 layout-auto Available column Description Name The name of the export. Users give exports a name when they create them, as described in Export Customer Journey Analytics reports to the cloud . ID The ID automatically assigned to the export when it is created. Data view name The name of the data view associated with the export. Users can select the data view when they create the export, as described in Export Customer Journey Analytics reports to the cloud . Status The status of the export. Available statuses are Active, Completed, and Failed. Note: For information about troubleshooting failed exports, see Troubleshoot failed exports . Tags Displays any tags that are applied to the export. For information about how to apply tags to an export, see Tag an export . Table size (last send) The size of the export the last time it was sent. Created by The user who created the export. Created The date and time the export was created. Location The location on the account where the data was exported. Account The account where the data was exported. Frequency The frequency with which the export is sent. Available options are One time, Daily, Weekly, Monthly by day of the week, Monthly by day of the month, Yearly by day of the month, and Yearly by specific date. Time sent The time the export was sent. Last sent The last time the export was sent. Last modified The last time the export was modified. Items on the Exports page are sorted by this column by default. Account type The type of cloud account where the data was exported. Available account types are Amazon S3 Role ARN, Google Cloud Platform, Azure SAS, Azure RBAC, Snowflake, and AEP Data Landing Zone.
- Ensure that any columns you want to display are selected. Selected columns appear on the Exports page and display the relevant information.

## Create an export from the Exports page

You can create an export either from Analysis Workspace, as described in [Export full tables to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud), or from the Exports page, as described in this section.

To begin creating an export from the Exports page:

- In Customer Journey Analytics, select Components > Exports .
- On the Exports tab, select Add export .
- Complete the available fields to create your export. For information about each field, as well as information about components, calculated metric functions, and other features that are supported, see Export full tables to the cloud .

recommendation-more-help
