---
title: "Audit logs audit-logs"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-privacy/audit-log"
category: "other"
topic: "analytics-platform/using/cja-privacy/audit-log"
created_at: "2026-06-23T20:44:21.699398+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Audit logs audit-logs

Last update: June 5, 2026
- Topics:
- [Data governance](#)

CREATED FOR:

- Admin

To increase the transparency and visibility of activities performed in the system, Adobe Customer Journey Analytics allows you to audit user activity for various services and capabilities in the form of “audit logs”. These logs form an audit trail that can help with troubleshooting issues, and help your business effectively comply with corporate data stewardship policies and regulatory requirements, such as the Health Insurance Portability and Accountability Act (HIPAA).

In a basic sense, an audit log tells **who** performed **what** action, and **when**. Each action recorded in a log contains metadata that indicates the action type, date and time, the email ID of the user who performed the action, and additional attributes relevant to the action type.

Audit logs are retained for 90 days. After that, audit logs are automatically deleted.

This topic covers audit logs in Customer Journey Analytics, including how to view and manage them in the UI.

## Access to audit logs

When the feature is enabled for your organization, audit logs are automatically collected as activity occurs. You do not need to manually enable log collection.

In order to view and export audit logs, you must have been granted the **Audit Logs Access** access control permission in Adobe Console. To learn how to manage individual permissions for Customer Journey Analytics features, please refer to the [access control documentation](/en/docs/analytics-platform/using/technotes/access-control).

## View the audit log in the UI

In Customer Journey Analytics, navigate to **Tools** > **Audit Logs**.

The audit log for today and yesterday are shown by default.

You can select which columns are visible by going to the column selector at the top right.

## View information about individual log entries

Double click the info (i) button next to a description.

The following items are shown:

- Action Name : The action taken. Possible values include: API_REQUEST: Any action triggers a backend API request. Details are displayed about what the API request was. APPROVE: An “approval” action was performed. CREATE: A “create” action was performed. DELETE: A “delete” action was performed. EDIT: An “edit” action was performed. EMBARGO: When you restrict a request in the Reporting Activity Manager , the action is recorded in the Audit Log under EMBARGO. EXPORT: An “export” action was performed. ORG_CHANGE: An organization change action was performed. REFRESH: A “refresh” action was performed. SHARE: A “share” action was performed. TRANSFER: A transfer action was performed. UNAPPROVE: An “unapprove” action was performed. UNSHARE: An “unshare” action was performed.
- Date Created : The date and time that the action was taken.
- Description : A summary of the action.
- User Name : The user that took the action. Sometimes, the user name might be missing. Consider using the Product Usage feature, since it always includes the login user name.
- Email : The email address of the user that took the action.
- Component Name : The component that the user took action on.
- Component Type : The type of component. Possible values include: ANNOTATION AUDIENCE CALCULATED_METRIC CONNECTION DATA_GROUP DATA_VIEW DATASET_STITCHING DATE_RANGE FEATURE_ACCESS FILTER IMS_ORG MOBILE PROJECT (Workspace) REPORT SCHEDULED_PROJECT USER USER_GROUP
- Component ID : The ID of the component that the user took action on.
- IMS Org ID : The organization’s IMS ID, in the format of ABC123@AdobeOrg .
- Log ID : A unique ID identifying this log entry.
- User ID : The unique ID identifying the user that took the action.
- User Type : The authentication type used. Valid values include: IMS OKTA

### Filter audit logs

Select the funnel icon ( ) to display a list of filter controls to help narrow results. Only the last 1,000 records are displayed, irrespective of the various filters selected.

The following filters are available for audit events in the UI:

Filter
Description
Date Range
Filter on a different date range by selecting a different date or selecting a date range by dragging the cursor across multiple dates. By default, today’s and yesterday’s date are selected.
Action
Filter on any action name listed above.
User ID
Filter on a specific user by their user ID. The user ID can be found by selecting the info (i) button next to a user name.
Email
Filter on a specific user’s email address. The email can be found by selecting the info (i) button next to a user name.
Component ID
Filter on a specific Component ID. The user ID can be found by selecting the info (i) button for a desired component.
Component Type
Filter on any component type listed above.
## Event types captured by audit logs

The following table outlines which actions on which component types are recorded by audit logs:

Component Type
Actions
Annotation
- Create
- Delete
- Edit

Audience
- API_Request
- Create
- Delete
- Edit
- Export
- Refresh

Calculated Metric
- API_Request
- Create
- Delete
- Edit

Connection
- API_Request
- Create
- Delete
- Edit

Data View
- API_Request
- Create
- Delete
- Edit

Date Range
- API_Request
- Create
- Delete
- Edit

Filter
- API_Request
- Create
- Delete
- Edit

IMS Org
- API_Request
- Create
- Delete
- Edit

Project
- API_Request
- Create
- Delete
- Edit

Report
- API_Request

Scheduled Project
- API_Request
- Create
- Delete
- Edit

User
- API_Request
- Create
- Delete
- Edit

User Group
- API_Request
- Create
- Delete
- Edit

## Download audit logs

You can download audit logs in CSV or JSON formats. Any filters applied or columns selected are reflected in the downloaded files.

- Click **Download** at the top right of the screen.
- Specify the format.
- Click **Download** again.

## Manage audit logs in the API

All actions that you can perform in the UI can also be done using API calls. See the [Customer Journey Analytics API reference document](https://developer.adobe.com/cja-apis/docs/api/#tag/Audit-Logs) for more information.

recommendation-more-help
