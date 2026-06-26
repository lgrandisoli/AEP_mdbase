---
title: "Standard component reference"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-reference"
category: "reference"
topic: "analytics-platform/using/cja-dataviews/component-reference"
created_at: "2026-06-02T19:04:39.154344+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Standard component reference

Last update: May 13, 2026
- Topics:
- [Data Views](#)

CREATED FOR:

- Admin

Most dimensions and metrics in Customer Journey Analytics are based on schema elements from your Adobe Experience Platform dataset. However, several components are available to add to a data view regardless of the connection that you use.

Standard components are components that are not generated from dataset schema fields but are instead system generated. Some system components are required to facilitate reporting capabilities in Analysis Workspace, while other system components are optional.

## Required standard components required

These required standard components are added to each data view by default. They are essential to the reporting capabilities that Customer Journey Analytics offers.

### Standard dimensions

Component Name
Notes
15 Minute
Each 15 minutes that a given event happened (rounded down). The first dimension item is the first 15 minutes in the date range, and the last dimension item is the last 15 minutes in the date range.
30 Minute
Each 30 minutes that a given event happened (rounded down). The first dimension item is the first 30 minutes in the date range, and the last dimension item is the last 30 minutes in the date range.
5 Minute
Each 5 minutes that a given event happened (rounded down). The first dimension item is the first 15 minutes in the date range, and the last dimension item is the last 5 minutes in the date range.
Day
The day that a given event happened. The first dimension item is the first day in the date range, and the last dimension item is the last day in the date range.
Day of Week
The day of the week that a given event happened. The first dimension item is the first day of the week in the date range, and the last dimension item is the last day of the week in the date range.
Day of Month
The day of the month that a given event happened. The first dimension item is the first day of the month in the date range, and the last dimension item is the last day of the month in the date range.
Event Depth
Assigns sequential numerical values (1, 2, 3, etc.) to each event interaction within a session. With this dimension you can enable detailed tracking and analysis of where specific events occur in the sequential flow of user interactions within the
bounded experience session you have defined for your data view
. You can track the progression of events from start to finish within a bounded session. As an example: A visitor lands on your homepage (event 1, session start), uses the search function (event 2), views a product details page (event 3), adds to cart (event 4), proceeds to checkout (event 5), and completes a purchase (event 6, session end). You can use Event depth now in a segment definition to segment data based on interaction depth.
Hour
The hour that a given event happened (rounded down). The first dimension item is the first hour in the date range, and the last dimension item is the last hour in the date range.
Hour of Day
The hour of the day that a given event happened (rounded down). The first dimension item is the first hour of the day in the date range, and the last dimension item is the last hour of the day in the date range.
Minute
The minute that a given event happened (rounded down). The first dimension item is the first minute in the date range, and the last dimension item is the last minute in the date range.
Minute of Hour
The minute of the hour that a given event happened (rounded down). The first dimension item is the first minute of the hour in the date range, and the last dimension item is the last minute of the hour in the date range.
Month
The month that a given event happened. The first dimension item is the first month in the date range, and the last dimension item is the last month in the date range.
Month of Year
The month of the year that a given event happened. The first dimension item is the first month of the year in the date range, and the last dimension item is the last month of the year in the date range.
Quarter
The quarter that a given event happened. The first dimension item is the first quarter in the date range, and the last dimension item is the last quarter in the date range.
Quarter of Year
The quarter of the year that a given event happened. The first dimension item is the first quarterof the year in the date range, and the last dimension item is the last quarter of the year in the date range.
Second
The second that a given event happened (rounded down). The first dimension item is the first second in the date range, and the last dimension item is the last second in the date range.
Week
The week that a given event happened. The first dimension item is the first week in the date range, and the last dimension item is the last week in the date range.
Week of year
The week of year that a given event happened. The first dimension item is the first week of year in the date range, and the last dimension item is the last week of year in the date range.
Year
The year that a given event happened. The first dimension item is the first year in the date range, and the last dimension item is the most recent year in the date range.
### Standard metrics

Component Name
Notes
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Accounts
Based on the Account ID specified in a Connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Buying Group
The buying groups, based on the Buying group ID specified in the Connection.
Events
The number of rows from all event datasets in a Connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Global Accounts
Based on the Global Accounts ID specified in the Connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Opportunities
The opportunities, based on the Opportunity ID specified in the Connection.
People
Based on the person ID specified in a Connection.
Session Ends
The number of events that were the last event of a session. Similar to Session Starts, it can also be used in a segment definition to segment things down to the last event of every session.

This component must be included in your data view for the following [calculated metric](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) to be available in Workspace:

- Session End Rate

Session Starts
The number of events that were the first event of a session. When used in a segment definition (for example, ‘Session Starts exists’), it segments down to just the first event of every session.

This component must be included in your data view for the following [calculated metric](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) to be available in Workspace:

- Session Start Rate

Sessions
Based on the data view’s session settings.
Time Spent (seconds)
Sums the time between two different values for a dimension.

This component must be included in your data view for the following [calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics) to be available in Workspace:

- Time Spent Per Person
- Time Spent Per Session

## Optional standard components optional

Optional Standard components are available under **Data views** > **Edit data view** > **Components** tab > **Standard Components** tab.

Component Name
Dimension or Metric
Notes and values
AM/PM
Time-parting dimension
AM or PM
Batch ID
Dimension
Identifier for the Experience Platform batch that an Event was part of.
Dataset ID
Dimension
Identifier for the Experience Platform dataset that an Event was part of.
Day of Month
Time-parting dimension
1-31
Day of Week
Time-parting dimension
Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
Day of Year
Time-parting dimension
1-366
Hour of Day
Time-parting dimension
0-23
Month of Year
Time-parting dimension
January - December
First-time Sessions
Metric
A person’s defined first session within the reporting window.
Learn more
Return Sessions
Metric
The number of sessions that were not a person’s first-time session.
Learn more
Person ID
Dimension
Each dataset schema defined in the Experience Platform can have its own set of one or more identities defined and associated with an Identity Namespace. Any of these identities can be used as the Person ID. Examples include Cookie ID, Stitched ID, User ID, Tracking Code, and so on. The Person ID dimension is the foundation of combining datasets and identifying unique persons in Customer Journey Analytics.

Possible use cases include:

- Create a segment on a specific person ID value to segment everything down to that user’s behavior.
- Debugging: making sure that the data for a specific cookie ID (or a specific customer ID) is there.
- Identifying the users who called in to a call center.

Person ID namespace
Dimension
Which type of ID the Person ID consists of. Examples are:
email address
,
cookie ID
,
Analytics ID
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Global Account ID
Dimension
The Global Account ID, when you use the Global Account container in your connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Account ID
Dimension
The Account ID, when you use the Account container in your connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Opportunity ID
Dimension
The Opportunity ID, when you use the Opportunity container in your connection.
[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}
Buying Group ID
Dimension
The Buying Group ID, when you use the Buying group container in your connection.
Quarter of Year
Time-parting dimension
Q1, Q2, Q3, Q4
Repeat session
Metric
The number of sessions that were not a person’s first-ever session.
Learn more
Session Type
Dimension
This dimension has two values: 1. First-Time and 2. Returning. The First-time line item includes all behavior (metrics against this dimension) from a session that has been determined to be a person’s defined first session. Everything else is included in the Returning line item (assuming everything belongs to a session). Where metrics are not part of any session, they would fall into the ‘Not applicable’ bucket for this dimension.
Learn more
Time Spent per Event
Dimension
Buckets the Time Spent metric into Event buckets.
Time Spent per Session
Dimension
Buckets the Time Spent metric into Session buckets.
Time Spent per Person
Dimension
Buckets the Time Spent metric into Person buckets.
Weekend/Weekday
Time-parting dimension
Weekend or Weekday
Related Articles
Discover Deeper Customer Insights with the Event Depth Feature
recommendation-more-help
