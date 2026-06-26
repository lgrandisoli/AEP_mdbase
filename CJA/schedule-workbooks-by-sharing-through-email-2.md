---
title: "Schedule workbooks by sharing through email"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-reportbuilder/schedule-reportbuilder"
category: "other"
topic: "analytics-platform/using/cja-reportbuilder/schedule-reportbuilder"
created_at: "2026-06-23T20:44:23.133382+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Schedule workbooks by sharing through email

Last update: May 13, 2026
- Topics:
- [Report Builder](#)

CREATED FOR:

- User

After you saved your workbook and completed your analysis, you can share your workbook with others on your team using the scheduling feature. The schedule feature allows you to create a schedule that automatically refreshes the data in the workbook. And emails the Excel workbook file as an attachment to your specified audience at a specific date and time. Setting up a schedule provides recipients with regular updates automatically. You can also use the schedule feature to send out the workbook once without scheduling automatic updates.

You can create multiple schedules for a single workbook. For example, you create two schedules to send a workbook to your team daily and to your manager once a week.

The schedule feature also allows you to set up password protection for a workbook and edit previously scheduled workbooks.

Does no longer seem to be an option? 
                1. (Optional) Select **.zip compression** to compress the file and set up password protection on the file.
                
                    When you make this selection, you're prompted to enter a password to open the file. This is helpful if you have concerns about data security and you want to password protect the workbook. Protecting the file with a password requires you to select **.zip compression**. The password must be at least 8 characters and contain a number and a special character.
                
                    ![Enter a password in the Password protect the workbook field.](./assets/zip-compression.png){zoomable="yes"}{width="55%"}
See [Schedule Workbooks](/en/docs/customer-journey-analytics-learn/tutorials/exporting/report-builder/schedule-cja-workbooks-using-report-builder#_blank) for a demo video.

style
shade-box
## Schedule a workbook

To schedule a workbook:

- Select Schedule in the Report Builder hub to create a schedule so that you can automatically distribute a workbook Excel file (.xlsx) to an individual or a group. {modal="regular"}
- Select Schedule Workbook or to create a new scheduled workbook. {modal="regular"} The scheduling pane displays some pre-defined information about the workbook such as the workbook name and the last date that the workbook was modified.

### File

In the **File** section, you provide details of the file type, name and a password to protect the file.

{modal="regular"}

- Use to select the current workbook, if not already selected.
- (Optional) Enter a File name . The workbook file name defaults to the name of the workbook but you can change the file name if you want.
- Select a File type . Excel PDF CSV When you select CSV , be aware that the scheduled workbook is sent as a zip attachment. Some corporate email administrations may block email with zip attachments. You see a warning accordingly.
- (Optional) Select Append time-stamp to file name . You can append a timestamp to the file name to identify the date the workbook was updated. A timestamp is helpful to see which version of a workbook was sent on a specific date. When selected, you can choose between: ISO Date format , which results in YYYY-MM-DD being appended to the filename. ISO Date format + time stamp , which results in YYYY-MM-DD_HH-MM-SS being appended to the filename.

- Enter a password in **Password protect the workbook**. A valid password requires at least 8 characters, a number, and a special character. Select to display the password and to hide the password (default).

### Email

In the **Email** section, you provide the recipients, subject and description of the email.

{modal="regular"}

- Enter Recipients . You can enter the name of a person that is recognized in your organization. Or you can enter an email address of a person that is outside of your organization.
- Enter the Subject of the email and a description for your recipients. The subject defaults to the workbook file name but you can modify the subject if needed. You can add details in the description section.
- You can optionally enter a description in the Description text area.

### Schedule

In the **Schedule** section, you can define the schedule to send the emails with the workbook to your recipients.

{modal="regular"}

- Select Show scheduling options to define a schedule.
- Enter a start date in Starting on . Alternatively, select to pick a start date from the calendar.
- Enter an end date in Ending on . Alternatively, select to pick an end date from the calendar.
- Select a Frequency . Depending on the frequency selected, you do have additional options. See table below. table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Frequency Options Send hourly Enter a value for Send every number of hours . Send daily Select a Daily frequency : Send every day , Send every weekday , or Custom frequency . If you select Custom frequency , enter a value for Send every number of days . Send weekly Enter a value for Send every number of weeks . And select a Day of week . Send monthly by day of the week Select a Day of week and a Week of month . Send monthly by day of the month Select a value from Send on this day of the month . Send yearly by day of the month Select a Day of week , select a Week of month , and select a Monthly of year . Send yearly by specific date Select a Month of year and select a value from Send on this day of the month .

### Send

To send the workbook:

- If you have not defined a schedule using **Show scheduling options**, select **Send now** to send the workbook by email immediately.
- If you have defined a schedule using **Show scheduling options**, select **Send on schedule** to send the workbook by email using the schedule you defined.

In both cases, you see a confirmation toast at the bottom of the Report Builder hub.

To cancel sending the workbook, select **Cancel**.

## Manage scheduled workbooks

For information about managing workbooks that are already scheduled, see [Manage scheduled workbooks](/en/docs/analytics-platform/using/cja-reportbuilder/manage-schedules-reportbuilder).

recommendation-more-help
