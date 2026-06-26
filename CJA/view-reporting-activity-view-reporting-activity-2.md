---
title: "View reporting activity view-reporting-activity"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity"
category: "other"
topic: "analytics-platform/using/reporting-activity-manager/reporting-activity"
created_at: "2026-06-23T20:44:36.375683+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# View reporting activity view-reporting-activity

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

The Reporting Activity Manager enables administrators to quickly diagnose and fix reporting capacity issues during peak reporting times.

For more information about Reporting Activity manager, including key benefits and permission requirements, see [Reporting Activity Manager overview](/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity-overview).

## For all connections view-all-report-suites

- In Customer Journey Analytics, go to Tools > Reporting Activity Manager . A list of your enabled base connections is displayed.
- To view the total number of report requests for all connections in your organization, expand Show more to view the Monthly report requests graph. You can view the number of report requests within your organization for the current month and the previous month.
- (Optional) You can search or filter the list of connections: Use the search field to search for a specific connection. Begin typing the connection name or ID and the list of connections updates as you type. Select to expand the list of segment options. You can filter by Favorites or Status . To mark a connection as a favorite, select the star icon to the left of the connection name.
- View utilization information about each connection. The data shown in the table represents the reporting activity for the connection at the time the page was last loaded. The following columns are available: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 layout-auto UI Element Description Connection The connection whose reporting activity you are monitoring. Data Views Shows all data views that use the connection. Data view configuration can add complexity to reporting requests. Capacity utilization The percentage of the connection’s reporting capacity that is being used, in real time. Note A usage capacity that is at 100% doesn’t necessarily suggest that you should immediately start cancelling reporting requests. 100% usage capacity can be healthy if the average wait time is reasonable. On the other hand, 100% usage capacity could suggest a problem if the number of queued requests is also growing. Queued requests The number of requests waiting to be processed. Queue wait time The average wait time before requests begin to process. Status The possible statuses are: Active (blue): Reports have been run on the connection in the last 2 hours. The data shown in the table represents the reporting capacity for the connection at the time the page was last loaded. Inactive (gray): No reports have ever been run on the connection in the last 2 hours, so no data is displayed for the connection.

## For a single connection

- In Customer Journey Analytics, select Tools > Reporting Activity Manager .
- Select the linked title of the connection for which you want to view details. Reporting activity data is displayed for the connection that you selected.
- (Optional) When a connection first loads in the Reporting Activity Manager, the data displayed represent the current utilization metrics. To see updated metrics after the initial load, select the Refresh button to manually refresh the page. Need to update this screenshot: ![connection](assets/indiv-report-ste.png)
- Use the available graphs and table to understand reporting activity in the connection. View graphs View table

### View graphs

The following graphs are available to help you better understand the activity happening in the connection.

If graphs are not visible, select the **Show graphs** button.

#### Utilization graph utilization

The Utilization graph shows reporting utilization for the selected connection over the last 2 hours.

Hover over the chart to view points in time where the usage capacity percentage was highest for that minute.

- X-axis : The reporting usage capacity over the last 2 hours.
- Y-axis : The reporting usage capacity percentage, by minute.

#### Distinct Users graph

The Distinct Users graph shows the reporting activity for the selected connection over the last 2 hours.

Hover over the chart to view points in time where the maximum number of users was highest for that minute.

- X-axis : The reporting activity over the last 2-hour time frame.
- Y-axis : The number of users who have made reporting requests, by minute.

#### Requests graph

The Requests graph shows the number of processed and queued requests for the selected connection over the last 2 hours.

Hover over the chart to view points in time where the maximum number of requests was highest for that minute.

- X-axis : The number of processed and queued requests over the last 2-hour time frame.
- Y-axis : The number of processed requests (in green) and queued requests (in purple), by minute.

#### Queueing graph

The Queueing graph shows the average queue wait time (in seconds) for reporting requests for the selected connection over the last 2 hours.

Hover over the chart to view points in time where the maximum average wait time was highest for that minute.

- X-axis : The average queue wait time for reporting requests over the last a 2-hour time frame.
- Y-axis : The average wait time (in seconds).

### View table view-table

When viewing the table, consider the following:

- You can choose to view data by choosing any of the following tabs at the top of the data table: Request , User , Project , or Application .
- You can search or filter the list of connections: Use the search field to search for a specific connection. Begin typing the connection name or ID and the list of connections updates as you type. Select the Filter icon to expand the list of filter options. You can filter by Status , Complexity , Application , User , or Project . You can select Hide graphs to show only the table.

#### View data by request

When you select the **Request** tab, the following columns are available in the table:

Column
Description
Request ID
A unique ID that can be used for troubleshooting purposes. To copy the ID, select the request, then select the option,
Copy request IDs
.
Time run
How long the request has been running.
Start time
When the request started processing (based on the administrator’s local time).
Wait time
How long the request has been waiting before being processed. This value is generally at “0” when there is enough capacity.
Application
The applications supported by the Reporting Activity Manager are:

- Analysis Workspace UI
- Workspace scheduled projects
- Report Builder
- Builder UIs: Segment, Calculated Metrics, Annotations, Audiences, and so forth.
- API calls from the 2.0 API
- Alerts
- Full table export
- Share with anyone links
- Guided analysis
- Any other application that queries the Analytics reporting engine

**Note:** If the value of this column is **Unknown**, this means that the request metadata is not available for the user.

User
The user who initiated the request.

**Note:** If the value of this column is **Unknown**, this means that the request metadata is not available for the user.

Project
Saved Workspace project names, API Report IDs, and so forth. (Metadata can vary across various applications.)

**Note:** If the value of this column is **Unknown**, this means that the project has not been saved or that the request metadata is not available for the user.

Status
Status indicators:

- **Running**: Request is currently being processed.
- **Pending**: Request is waiting to be processed.

Complexity
Not all requests require the same amount of time to process. Request complexity can help provide a general idea about the time required to process the request.

Possible values include:

- **Low**
- **Medium**
- **High**

This value is influenced by the values in the following columns:

- **Month boundaries**
- **Columns**
- **Segments**

Month boundaries
The number of months that are included in a request. More month boundaries adds to the complexity of the request.
Columns
The number of metrics and breakdowns in the request. More columns adds to the complexity of the request.
Segments
The number of segments applied to the request. More segments adds to the complexity of the request.
#### View data by user

When you select the **User** tab, the following columns are available in the table:

Column
Description
User
The user who initiated the request. If the value of this column is
Unrecognized
, this means that the user is in a login company where you do not have administrative permissions.
Number of requests
The number of requests initiated by the user.
Number of projects
The number of projects associated with the user.
???
Application
The applications supported by the Reporting Activity Manager are:

- Analysis Workspace UI
- Workspace scheduled projects
- Report Builder
- Builder UIs: Segment, Calculated Metrics, Annotations, Audiences, and so forth.
- API calls from the 2.0 API
- Alerts
- Full table export
- Share with anyone links
- Guided analysis
- Any other application that queries the Analytics reporting engine

Avg Complexity
The average complexity of requests initiated by the user.

Not all requests require the same amount of time to process. Request complexity can help provide a general idea about the time required to process the request.

The value in this column is based on a score that is determined by the values in the following columns:

- **Avg Month boundaries**
- **Avg Columns**
- **Avg Segments**

Avg Month boundaries
The average number of months that are included in the requests. More month boundaries adds to the complexity of the request.
Avg Columns
The average number of metrics and breakdowns in the included requests. More columns adds to the complexity of the request.
Avg Segments
The average number of segments applied to the included requests. More segments adds to the complexity of the request.
#### View data by project

When you select the **Project** tab, the following columns are available in the table:

Column
Description
Project
The project where the requests were initiated.
Number of requests
The number of requests associated with the project.
Number of users
The number of users associated with the project.
???
Application
The applications supported by the Reporting Activity Manager are:

- Analysis Workspace UI
- Workspace scheduled projects
- Report Builder
- Builder UIs: Segment, Calculated Metrics, Annotations, Audiences, and so forth.
- API calls from the 2.0 API
- Alerts
- Full table export
- Share with anyone links
- Guided analysis
- Any other application that queries the Analytics reporting engine

Avg Complexity
The average complexity of requests included in the project.

Not all requests require the same amount of time to process. Request complexity can help provide a general idea about the time required to process the request.

The value in this column is based on a score that is determined by the values in the following columns:

- **Avg Month boundaries**
- **Avg Columns**
- **Avg Segments**

Avg Month boundaries
The average number of months that are included in the requests. More month boundaries adds to the complexity of the request.
Avg Columns
The average number of metrics and breakdowns in the included requests. More columns adds to the complexity of the request.
Avg Segments
The average number of segments applied to the included requests. More segments adds to the complexity of the request.
#### View data by application

When you select the **Application** tab, the following columns are available in the table:

Column
Description
Application
The application where the requests were initiated.
Number of requests
The number of requests associated with the application.
Number of users
The number of users associated with the application.
???
Number of projects
The number of projects associated with the application.
???
Avg Complexity
The average complexity of requests associated with the application.

Not all requests require the same amount of time to process. Request complexity can help provide a general idea about the time required to process the request.

The value in this column is based on a score that is determined by the values in the following columns:

The value in this column is based on a score that is determined by the values in the following columns:

- **Avg Month Boundaries**
- **Avg Columns**
- **Avg Segments**

Avg Month boundaries
The average number of months that are included in the requests. More month boundaries adds to the complexity of the request.
Avg Columns
The average number of metrics and breakdowns in the included requests. More columns adds to the complexity of the request.
Avg Segments
The average number of segments applied to the included requests. More segments adds to the complexity of the request.
recommendation-more-help
