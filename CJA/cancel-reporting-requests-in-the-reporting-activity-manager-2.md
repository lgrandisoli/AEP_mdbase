---
title: "Cancel reporting requests in the Reporting Activity Manager"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity-cancel-requests"
category: "other"
topic: "analytics-platform/using/reporting-activity-manager/reporting-activity-cancel-requests"
created_at: "2026-06-23T20:44:36.944054+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Cancel reporting requests in the Reporting Activity Manager

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

The Reporting Activity Manager enables administrators to quickly diagnose and cancel reporting requests in order to fix reporting capacity issues during peak reporting times.

Consider the following when cancelling reporting requests:

- You can cancel specific requests, cancel all requests from a specific user, or cancel all requests related to a specific project.
- When you cancel requests, you can also choose to restrict subsequent requests for a given time period. When you restrict a subsequent request, the action is recorded in the Audit Log with the action name of EMBARGO.
- You cannot cancel a request if the User column of a request shows as Unrecognized . When this occurs, it means that the user is in a login company where you do not have administrative permissions.

For more information about Reporting Activity manager, including key benefits and permission requirements, see [Reporting Activity Manager overview](/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity-overview).

## Cancel specific requests

You can cancel individual requests that are consuming a large amount of reporting capacity. When canceling a request, you can choose to further restrict it for a given time period.

- In Customer Journey Analytics, go to Tools > Reporting Activity Manager .
- Select the connection where you want to cancel reporting requests. For more information about the data available on this page, see View reporting activity in the Reporting Activity Manager .
- Select the Requests tab, then select one or more requests. add screenshot
- Select Cancel requests . The Cancel x report requests dialog box displays.
- The Cancellation message field shows the message that displays to users when their requests are cancelled. A default message is provided. You can update the default message to provide additional details.
- (Optional) To restrict future requests for a given time period: Enable the option to Restrict subsequent requests . Choose from the following options: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Option Function User & project Users associated with the selected requests will be temporarily restricted from running reporting requests for the associated projects. User Users associated with the selected requests will be temporarily restricted from making any reporting requests. Project Projects associated with the selected requests will be temporarily restricted from all reporting requests. Restricted for Choose for how long requests will be restricted. You can choose 1 minute (default), 5 minutes, 10 minutes, 15 minutes, or 30 minutes. You cannot remove a restriction early after it is set.
- Select Continue with cancellation . A notification is displayed in Analysis Workspace, informing users that the request has been cancelled. For more information about how this appears in Analysis Workspace, see Experience when users access a cancelled report .

## Cancel requests by user

You can cancel all requests that are associated with one or more users. When canceling requests associated with a user, you can choose to further restrict requests from that user for a given time period.

- In Customer Journey Analytics, go to Tools > Reporting Activity Manager .
- Select the connection where you want to cancel reporting requests. For more information about the data available on this page, see View reporting activity in the Reporting Activity Manager .
- Select the Users tab, then select one or more users. add screenshot
- Select Cancel requests . The Cancel x report requests from x users dialog box displays.
- The Cancellation message field shows the message that displays to users when their requests are cancelled. A default message is provided. You can update the default message to provide additional details.
- (Optional) To restrict future requests for a given time period: Enable the option to Restrict subsequent requests Choose from the following options: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Option Function User & project Selected users will be temporarily restricted from making any reporting requests for the associated projects. This is the least restrictive option. User Selected users will be temporarily restricted from making any reporting requests. Project Projects associated with the selected users will be restricted from any reporting requests made by any user. Restricted for Choose for how long requests will be restricted. You can choose 1 minute (default), 5 minutes, 10 minutes, 15 minutes, or 30 minutes. You cannot remove a restriction early after it is set.
- Select Continue with cancellation . A notification is displayed in Analysis Workspace, informing users that the request has been cancelled. For more information about how this appears in Analysis Workspace, see Experience when users access a cancelled report .

## Cancel requests by project

You can cancel all requests that are associated with one or more projects. When canceling requests associated with a project, you can choose to further restrict requests associated with that project for a given time period.

- In Customer Journey Analytics, go to Tools > Reporting Activity Manager .
- Select the connection where you want to cancel reporting requests. For more information about the data available on this page, see View reporting activity in the Reporting Activity Manager .
- Select the Projects tab, then select one or more projects. add screenshot
- Select Cancel requests . The Cancel x report requests from x projects dialog box displays.
- The Cancellation message field shows the message that displays to users when their requests are cancelled. A default message is provided. You can update the default message to provide additional details.
- (Optional) To restrict future requests for a given time period: Enable the option to Restrict subsequent requests . Choose from the following options: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Option Function User & project Selected projects will be temporarily restricted from any reporting requests made by the associated users. This is the least restrictive option. User Users associated with the selected projects will be restricted from making any reporting requests. Project Selected projects will be temporarily restricted from any reporting requests made by any user. Restricted for Choose for how long requests will be restricted. You can choose 1 minute (default), 5 minutes, 10 minutes, 15 minutes, or 30 minutes. You cannot remove a restriction early after it is set.
- Select Continue with cancellation . A notification is displayed in Analysis Workspace, informing users that the request has been cancelled. For more information about how this appears in Analysis Workspace, see Experience when users access a cancelled report .

## Cancel requests by application

You can cancel all requests that are associated with one or more applications. When canceling requests associated with an application, you can choose to further restrict requests associated with that application for a given time period.

Applications include the following:

- Analysis Workspace UI
- Workspace scheduled projects
- Report Builder
- Builder UIs: Segment, Calculated Metrics, Annotations, Audiences, etc.
- API calls from the 2.0 API
- Alerts
- Full table export
- Share with anyone links
- Guided analysis
- Any other application that queries the Analytics reporting engine

To cancel requests by application:

- In Customer Journey Analytics, go to Tools > Reporting Activity Manager .
- Select the connection where you want to cancel reporting requests. For more information about the data available on this page, see View reporting activity in the Reporting Activity Manager .
- Select the Applications tab, then select one or more applications. add screenshot
- Select Cancel requests . The Cancel x report requests from x projects dialog box displays.
- The Cancellation message field shows the message that displays to users when their requests are cancelled. A default message is provided. You can update the default message to provide additional details.
- (Optional) To restrict future requests for a given time period: Enable the option to Restrict subsequent requests Choose from the following options: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Option Function User & project Selected applications will be temporarily restricted from any reporting requests made by the associated users and projects. This is the least restrictive option. User Users associated with the selected applications will be restricted from making any reporting requests. Project Projects associated with the selected applications will be restricted from any reporting requests made by any user. Restricted for Choose for how long requests will be restricted. You can choose 1 minute (default), 5 minutes, 10 minutes, 15 minutes, or 30 minutes. You cannot remove a restriction early after it is set.
- Select Continue with cancellation . A notification is displayed in the application (such as in Analysis Workspace), informing users that the request has been cancelled. For more information about how this appears in Analysis Workspace, see Experience when users access a cancelled report .

## Experience when users access a cancelled report

In Analysis Workspace, users see the following messages when they attempt to access a report or visualization that is affected by a cancellation:

### Message on the project

When users attempt to access a project that is affected by a cancellation, they see a message informing them that the report is temporarily restricted:

### Message on the visualization

When users attempt to access a visualization that is affected by a cancellation, they see a message informing them that data processing for the report is temporarily restricted:

recommendation-more-help
