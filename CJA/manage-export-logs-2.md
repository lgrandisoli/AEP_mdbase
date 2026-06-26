---
title: "Manage export logs"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/exports/manage-export-logs"
category: "other"
topic: "analytics-platform/using/cja-components/exports"
created_at: "2026-06-23T20:44:46.189059+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage export logs

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

Export logs provide details about each export, and are generated any time Analysis Workspace data is exported to the cloud. (For information about how data can be exported to the cloud, see [Export Customer Journey Analytics reports to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud).)

For scheduled exports, logs reflect the export settings as they were when the log was sent. Logs cannot be deleted.

## View export logs

- In Customer Journey Analytics, select Components > Exports .
- Select the Logs tab. Details for each log are displayed in the available columns.
- Do any of the following: System administrators can enable the option to View logs for all users . When this option is enabled, all logs are shown, regardless of which user created the export. Customize the columns that are displayed. Select the Information icon next to the log name to view the export that is associated with the log. Select the Edit export icon next to the log name to edit the export that is associated with the log. For more information about editing an export, see Export Customer Journey Analytics reports to the cloud .

## Filter and search for logs

To find the information that you need, you can either filter the list of logs or search for a log.

### Filter the list of logs

- In Customer Journey Analytics, select Components > Exports .
- Select the Logs tab.
- Select the Filter icon. You can filter by the following criteria: table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto Filter Description Export ID Specify the export ID of the export log that you want to view. Account type The account type that the log is associated with. The following account types are available: AEP Data Landing Zone Amazon S3 Role ARN Azure SAS Azure RBAC Google Cloud Platform Snowflake . Status The status of the export. The following statuses are available: Pending : A specific instance of an export has been started but is not yet complete. Re-running an export that has a status of Pending delays the export process. Completed : A specific instance of an export has finished processing and is available in the export account. Failed Various situations can result in a failed export. Hover over the Failed status to see details about the failure. For more information about possible reasons for a failure, see Troubleshoot failed exports .

### Search for logs

- In Customer Journey Analytics, select Components > Exports .
- Select the Logs tab.
- In the search field, begin typing any information associated with the log you’re searching for. You can search for data from any column available in the table.

## Edit an export

You can edit the export associated with a specific log.

This option is not available when selecting multiple logs.

- In Customer Journey Analytics, select Components > Exports .
- Select the Logs tab.
- Locate the log that is associated with the export you want to edit.
- Select the Edit export icon next to the log name. Or Select the checkbox next to the log, then select Edit export .

## Rerun a completed or failed export

You can rerun one or more exports associated with specific export logs. To rerun an export, the export log must have a status of Completed or Failed and be no more than 7 days old.

- Select the checkbox next to one or more export jobs that you want to rerun.
- Select Rerun .

## Configure columns

You can add or remove columns in the Logs tab to configure what information is displayed.

Select a column header to sort the logs by that column. By default, logs are sorted by the date and time the export started.

To configure columns in the Logs tab:

- In Customer Journey Analytics, select Components > Exports .
- Select the Logs tab.
- Select the Customize table icon in the upper-right of the Logs page. The following columns are available: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 layout-auto Available column Description Export name The name of the export. Users give exports a name when they create them, as described in Export Customer Journey Analytics reports to the cloud . Export ID The ID automatically assigned to the export when it is created. Instance ID The ID of the Customer Journey Analytics instance. Data view name The name of the data view associated with the export. Users can select the data view when they create the export, as described in Export Customer Journey Analytics reports to the cloud . Number of files The number of files included in the export. Size The size of the export. The file size is calculated with a base of 1024, which is sometimes represented as KiB and MiB. If your cloud provider calculates size with a base of 1000, it may result in the size displayed in your cloud provider being slightly different from the size displayed here. Location The location on the account where the data was exported. Account The account where the data was exported. Status The status of the export. Available statuses are Pending, Completed, and Failed. Date delivered The date when the export took place. Date started The date when the export started. Account type The type of cloud account where the data was exported. Available account types are Amazon S3 Role ARN, Google Cloud Platform, Azure SAS, Azure RBAC, Snowflake, and AEP Data Landing Zone. Number of rows The number of rows included in the exported table.
- Ensure that any columns you want to display are selected. Selected columns appear on the Logs page and display the relevant information.

## View audit logs

Full-table exports are also tracked in the [Customer Journey Analytics audit logs](/en/docs/analytics-platform/using/cja-privacy/audit-log). Need to see what the Component Type for full-table export will be and add it here. Also, under "Event type captured by audit logs" there would be a new event type called "Full-table export". 4 actions would be "Create, Delete, Edit, Export" and "API_Request"? Also information about the locations. Probably have a different component for the location credentials.

recommendation-more-help
