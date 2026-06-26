---
title: "Send and schedule projects"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/export/t-schedule-report"
category: "other"
topic: "analytics-platform/using/cja-workspace/export"
created_at: "2026-06-02T19:05:47.759277+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Send and schedule projects

Last update: May 13, 2026
- Topics:
- [Curate and Share](#)

CREATED FOR:

- User

You can send Customer Journey Analytics projects as files to selected users by email. You can send files ad hoc, or you can configure projects to be sent on a schedule.

Consider the following when sending files:

- Files can be sent in CSV or PDF format.
- Any tags applied to the project are automatically applied to the export.

Other methods of exporting Customer Journey Analytics data are also available, as described in [Export overview](/en/docs/analytics-platform/using/cja-workspace/export/export-project-overview).

## Send file

To send a file to recipients by email:

- Select Share > Send file .
- Specify the file type: CSV : Choose this option if you want plain-text data. PDF : Choose this option if you want the downloaded file to contain all the displayed (visible) tables and visualizations in the project.
- (Optional) Use Description to add a description to include in the email.
- Add recipients or groups. You can also enter email addresses.
- (Only for Healthcare Shield customers) Provide a password to password-protect a scheduled report .
- (Optional) Select Show scheduling options to schedule a file export .
- Click Send Now . Select Cancel to cancel.

## Schedule file export schedule

To send a file on a schedule to recipients by email:

- Select Share > Schedule file export .
- Specify the file type: CSV : Choose this option if you want plain-text data. PDF : Choose this option if you want the downloaded file to contain all the displayed (visible) tables and visualizations in the project.
- (Optional) Use Description to add a description to include in the email.
- Add recipients or groups. You can also enter email addresses.
- (Only for Healthcare Shield customers) Provide a password to password-protect a scheduled report .
- Ensure Show scheduling options is selected.
- Select a Frequency . You can select between: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Frequency Options Send hourly Enter a value for Send every number of hours . Send daily Select a Daily frequency : Send every day , Send every weekday , or Custom frequency . If you select Custom frequency , enter a value for Send every number of days . Send weekly Enter a value for Send every number of weeks . And select a Day of week . Send monthly by day of the week Select a Day of week and a Week of month . Send monthly by day of the month Select a value from Send on this day of the month . Send yearly by day of the month Select a Day of week , select a Week of month , and select a Monthly of year . Send yearly by specific date Select a Month of year and select a value from Send on this day of the month .
- Enter a start date in Starting on . Alternatively, select to pick a start date from the calendar.
- Enter an end date in Ending on . Alternatively, select to pick an end date from the calendar.
- Select Send on schedule . Select Cancel to cancel.

## Password-protect a scheduled project password

NOTE
The option to password-protect a scheduled project appears only for Customer Journey Analytics customers who have purchased the
Healthcare Shield
add-on product.
Adobe uses the password to encrypt scheduled projects, whether they are sent in .pdf or .csv formats.

After your company has purchased the Healthcare Shield SKU and has been enabled for it, the prompt to create a password for a scheduled project is displayed in the following circumstances:

- When someone creates a new scheduled project.
- When an existing scheduled project is about to be sent. The currently scheduled project is disabled until password protection is in place. The owner of the scheduled project receives an email informing them of this requirement.

### Password requirements

The password requirements conform to the Adobe standards, requiring a minimum of 8 characters with at least one number and one special character.

### Password-protect a new scheduled project

- After you save your project, go to **Share** > **Send file now**, or **Share** > **Send file on schedule**.
- Follow the instructions above, under [Send file now](/en/docs/analytics-platform/using/cja-workspace/export/t-schedule-report#now) or [Send file on schedule](/en/docs/analytics-platform/using/cja-workspace/export/t-schedule-report#schedule).

### Password-protect an existing scheduled project

When you password-protect an existing scheduled project, the project owner receives an email similar to this:

- Log in to Customer Journey Analytics.
- Select **View Scheduled Project**.
- In the **Edit scheduled project** dialog, enter and re-enter a password.
- Let the recipients of the scheduled project know about this password. Do not distribute the password to people who are not recipients of the scheduled project.

## Scheduled projects manager manager

Scheduled Analysis Workspace projects can be managed from the main interface, using **Components** > **Scheduled Projects**. For more information, see [Scheduled projects](/en/docs/analytics-platform/using/cja-components/scheduled-projects-manager).

recommendation-more-help
