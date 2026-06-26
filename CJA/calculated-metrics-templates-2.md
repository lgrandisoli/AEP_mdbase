---
title: "Calculated metrics templates"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/default-calcmetrics"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-23T20:42:40.304059+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Calculated metrics templates

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User

Customer Journey Analytics provides the following calculated metrics templates to cover the most common use cases. These Adobe-defined calculated metrics are identified by a small logo. To quickly filter these metrics, select **Adobe Template** in the [Components filter](/en/docs/analytics-platform/using/cja-components/overview#filter).

Calculated metric name
Description
Formula
Session start rate
The percent that any dimension item occurred on the first event of a session.

This calculated metric is automatically added to Workspace when you include the Session Starts [standard component](/en/docs/analytics-platform/using/cja-dataviews/component-reference) in your [data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview).

Summary: **(** **Session starts** **Sessions** **)**

Time spent per person
The average amount of time a person spent on any given dimension item.

This calculated metric is automatically added to Workspace when you include the Time Spent (seconds) [standard component](/en/docs/analytics-platform/using/cja-dataviews/component-reference) in your [data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview). The segment Exclude Last Event of Session is applied to the People metric. The segment excludes the last event of each session in a dataset. This exclusion can help you analyze user behavior leading up to an event or action, such as a purchase or form submission, while excluding the final action itself.

Summary: **(** **Time spent (seconds)** **Exclude last event of session(** **People ) )**

Sessions per person
The average number of Sessions per Person.

Summary: **(** **Sessions** **People** **)**

Time spent per session
The average amount of time a person spent per Session on any given dimension item.

This calculated metric is automatically added to Workspace when you include the Time Spent (seconds) [standard component](/en/docs/analytics-platform/using/cja-dataviews/component-reference) in your [data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview). The segment Exclude Last Event of Session is applied to the Sessions metric. The segment excludes the last event of each session in a dataset. This exclusion can help you analyze user behavior leading up to an event or action, such as a purchase or form submission, while excluding the final action itself.

Summary: **(** **Time spent (seconds)** **Exclude last event of session(** **Sessions ) )**

Session end rate
The percent that any dimension item occurred on the last event of a session.

This calculated metric is automatically added to Workspace when you include the Session Ends [standard component](/en/docs/analytics-platform/using/cja-dataviews/component-reference) in your [data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview).

Summary: **(** **Session ends** **Sessions** **)**

Web sessions
The number of sessions that occurred on the website.
Survey completion rate
The rate at which people completed a survey after starting it.
Multi-channel session rate
The ratio of sessions that occurred that included multiple channels (such as web traffic and mobile traffic), compared to those that included only a single channel.
Multi-channel person rate
The ratio of people who have particicpated in multiple channels, compared to those who have only participated in a single channel.
Mobile app sessions
The number of sessions that occurred on the mobile app.
Web+app cross-channel sessions
The number of sessions that occured that included both web traffic and mobile traffic.
Cost of calls
The total cost for call center calls.
<p>Summary: Call length</p>
Average call duration
The average duration of calls made to the call center.
Average cost per call
The average cost of calls made to the call center.
Average call survey score
The average survey score regarding calls made to the call center.
recommendation-more-help
