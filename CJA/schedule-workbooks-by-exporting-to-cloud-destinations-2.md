---
title: "Schedule workbooks by exporting to cloud destinations"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-reportbuilder/report-builder-export"
category: "other"
topic: "analytics-platform/using/cja-reportbuilder/report-builder-export"
created_at: "2026-06-23T20:45:37.137869+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Schedule workbooks by exporting to cloud destinations

Last update: May 13, 2026
- Topics:
- [Report Builder](#)

CREATED FOR:

- User
- Admin

You can export Customer Journey Analytics workbooks from Report Builder to cloud providers like Google, Azure, and Amazon.

[Advantages of exporting reports from report builder to the cloud](#advantages-of-exporting-to-the-cloud) include the ability to use reports in third-party tools or combine them with outside data.

Before you export workbooks from Report Builder to a cloud destination, make sure that your data blocks, your environment, and your permissions meet the [export requirements](#export-requirements).

## Understand the export process

Use the following process when exporting workbooks from Report Builder to the cloud:

- Configure a cloud account
- Configure a location on the account
- Export a report from Report Builder
- Access data in your cloud account and Manage exports in Adobe

## Export a report from Report Builder

NOTE
Before you export data as described in this section, learn more about
the export process
in the section above.
To export reports from Report Builder:

- If you haven’t already, configure an export account and location, as described in Configure cloud export accounts .
- In the Excel spreadsheet that contains the data that you want to export, open the Adobe Report Builder right panel.
- Select Schedule .
- On the Workbooks tab, select the plus icon to create a new schedule Or To export the workbook on a schedule that you already created, select the schedule from the list of schedules, then select Send on schedule .
- In the Adobe Report Builder right panel, specify the following information to continue creating a new schedule: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 layout-auto Field name Function File Displays the workbook file that is currently selected for export. Select the workbook icon next to the file name to choose the current workbook if it is not already selected. Filename Allows you to change the filename before exporting the workbook. The workbook file name defaults to the name of the workbook File type Choose the file type for the exported file. You can choose Excel, PDF, or CSV. When you select CSV , be aware that the scheduled workbook is sent as a ZIP attachment. Some corporate email administrations may block email with ZIP attachments. You see a warning accordingly. Append time stamp to file name Select this option to append a timestamp to the file name to identify the date the workbook was updated. A timestamp is helpful to see which version of a workbook was sent on a specific date. When selected, you can choose between: Filename preview Shows a preview of how the file name will appear after the export. Password protect the workbook Specify a password to protect the exported file so only people with the password can access it. Passwords must be at least 8 characters and contain at least 1 number and 1 special character (such as ! , @ , # , and $ ). Email Select this option to send the file to a specific email address. For more information, see Schedule workbooks by sharing through email . Other deliveries Select this option to send the file to a cloud account, then use the Account and Location drop-down menus that are described below to select the account and location. Account Select the cloud export account where you want the data to be sent to. Or, if you haven’t already configured a cloud account that you want to use, you can configure a new account: Select Add account , then specify the following information: Location account name : Specify a name for the location account. This name appears when creating a location Location account description : Provide a short description of the account to help differentiate it from other accounts of the same account type. Make account available to all users in your organization : Select this option to allow other users in your organization to use the account. Consider the following when sharing accounts: Accounts that you share cannot be unshared. Shared accounts can be edited only by the owner of the account. Anyone can create a location for the shared account. Account type : Select the type of cloud account that you are exporting to. Available account types are Amazon S3 Role ARN, Google Cloud Platform, Azure SAS, and Azure RBAC. To finish configuring your account, continue with the link below that corresponds to the Account type you selected: Amazon S3 Role ARN Google Cloud Platform Azure SAS Azure RBAC Location Select the location on the account where you want the export data to be sent. Or, if you haven’t already configured the location that you want to use on the account that you selected, you can configure a new location: Select Add location , then specify the following information: Name : The name of the location. Description : Provide a short description of the location to help differentiate it from other locations on the account. Make location available to all users in your organization : Select this option to allow other users in your organization to use the location. Consider the following when sharing accounts: Locations that you share cannot be unshared. Shared locations can be edited only by the owner of the account. Locations can be shared only if the account that the location is associated with is also shared. Location account : Select the account where you want to create the location. To finish configuring your location, continue with the link below that corresponds to the account type that you selected in the Location account field: Amazon S3 Role ARN Google Cloud Platform Azure SAS Azure RBAC Show scheduling options Select this option to view additional options for scheduling the export. Leave this option unselected if you want to send the export only once. When this option is unselected, the export is initiated immediately. Starting on The day and time that the scheduled export should begin. This option is available only when choosing a scheduled export frequency. Ending on The day and time that the scheduled export expires. The scheduled export no longer runs after the date and time that you set. This option is available only when choosing a scheduled export frequency. Frequency You can set the frequency to be hourly, daily, weekly, monthly, or yearly on a specific day. For example, you can set up a schedule to send the workbook on the first Sunday night of the month so that your recipients have the email in their inbox first thing on Monday morning.
- Select Send on schedule to export the workbook. Data is sent to the cloud account that you specified at the frequency that you specified.
- (Optional) After you create the export, whether you chose to send it now or on a defined schedule, you can view and manage it on the Exports page and view it in the Export logs .

## Manage exports

After data is exported from Analysis Workspace, you can edit, re-export, duplicate, tag, or delete existing exports, as described in [Manage exports](/en/docs/analytics-platform/using/cja-components/exports/manage-exports).

## Advantages of exporting to the cloud

Exporting Customer Journey Analytics data to the cloud allows you to:

- Export to a shared location, such as Google Cloud Platform, Microsoft Azure, and Amazon S3.
- Store large amounts of historical data. This type of data can be used to detect long-term trends in order to gain business intelligence, and ultimately lead to better business decision-making.
- Include calculated metrics in the exported Customer Journey Analytics data.
- Structure data output as concatenated values.
- Export one-time or on a schedule.
- Export files in Excel, PDF, or CSV format.
- Export data blocks that include multiple dimensions.

## Export requirements export-requirements

Make sure that your data blocks, your environment, and your permissions meet the following requirements:

- Data blocks: All data blocks must include at least one component to a column, row, or value.
- Environment: Ensure that the IP addresses and Domains used by Customer Journey Analytics are allowed through their organization’s firewall.

recommendation-more-help
