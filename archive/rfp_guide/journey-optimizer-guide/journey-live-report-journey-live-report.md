---
title: "Journey live report journey-live-report"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/reporting/live-report/journey-live-report"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:50.950064+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Journey live report journey-live-report

Last update: May 8, 2026
- Topics:
- [Reporting](#)

CREATED FOR:

- Intermediate
- User

Live reports, accessible from the Last 24 hrs tab, display events that took place within the past 24 hours, with a minimum time interval of two minutes from the event occurrence. In comparison, Customer Journey Analytics reports focus on events that occurred at least two hours ago and cover events over a selected time period.

Access the live Journey report from the Journeys menu by opening your journey’s More actions menu and selecting View last 24hrs report.

The journey **Live report** page will be displayed with the following tabs:

- [Journey](#journey-live)
- [Email](#email-live)
- [Push](#push-live)
- [SMS](#sms-live)
- [In-app](#in-app-live)

The journey **Live report** is divided into different widgets detailing your journey’s success and errors. Each widget can be resized and deleted if needed. For more information on this, refer to this [section](/en/docs/journey-optimizer/using/reporting/live-report/live-report#modify-dashboard).

For a detailed list of every metric available in Adobe Journey Optimizer, refer to [this page](/en/docs/journey-optimizer/using/reporting/live-report/live-report#live-report).

## Journey tab journey-live

From your journey **Live report**, the **Journey** tab gives you a clear view of the most important tracking data about your journey.

### Journey’s performance journey-performance

**Journey Performance** allows you to see the path of your targeted profiles step-by-step through your journey.

Note the profile count for a node is only updated after the profile completes the node, not upon entering it. For instance, a profile on a **Wait** node is only counted once the specified date is reached and the profile has exited the node.

### Journey’s statistics journey-statistics

The **Journey Statistics** Key Performance Indicators (KPIs) function as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your journey over the last 24 hours. This encompasses details such as the count of entered profiles and instances of failed individual journeys, offering a comprehensive insight into your journey’s effectiveness and level of engagement.

Learn more about Journey's statistics metrics
- Entered profiles : Total number of individuals who reached the entry event of the journey.
- Exited profiles : Total number of individuals who exited the journey.
- Failed individual journeys : Total number of individual journeys that were not successfully executed.

### Action executed over the last 24 hours action-executed

The **Action executed over the last 24 hours** widget represents the most successful action which occurred when your actions were triggered.

Learn more about Action executed over the last 24 hours metrics
- Actions executed : Total number of actions successfully executed for a journey.
- Error in actions : Total number of errors that occurred for actions.

### Actions executed and errors actions-errors

The **Actions executed and errors** widget represents the most successful action and errors which occurred when your actions were triggered in the last 24 hours.

Learn more about Actions executed and errors metrics
- Actions executed : Total number of actions successfully executed for a journey.
- Error in actions : Total number of errors that occurred for actions.

### Actions error reasons actions-error-reasons

The **Action error reasons** table and graph offer a comprehensive overview of errors that occurred during the execution of your actions within the last 24 hours.

### Error type by actions error-type-actions

The **Error type by actions** table and graph offer a comprehensive overview of errors that occurred for each execution of your actions within the last 24 hours.

### Event executed over the last 24 hours event-executed-24hours

The **Event executed over the last 24 hours** widget enables you to identify which of your events was successfully executed within the last 24 hours.

### Events events

The **Events** widget allows you to see which one of your events was successfully executed through summary number, graph and table.

### Events by origin events-origin

The **Events by origin** table and graphs provide a detailed perspective on the successful reception of your events in the last 24 hours. Through these visual representations, you can discern precisely which of your events were effectively received, offering valuable insights into the performance and impact of individual events within your journey.

## Email tab email-live

From your journey **Live report**, the **Email** tab details the main information relative to the emails sent in your journey.

### Email - Sending performance email-sending-performance

The **Email - Sending performance** graph provides a comprehensive view of data related to sent emails in your journey, offering insights into key metrics such as delivered and bounces which happened in the last 24 hours. This enables a detailed analysis of the email sending process, providing valuable information on the efficiency and performance of your journeys.

Learn more about Email - Sending performance metrics
- Delivered : Number of emails successfully sent.
- Bounces : Total of errors cumulated during the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.
- Retries : Number of emails in the queue for retries.

### Email - Statistics email-stat

The **Email - Statistics** table provides a comprehensive summary of essential data regarding emails in your journeys over the last 24 hours. It details key metrics such as the size of the targeted audience and number of emails successfully delivered, offering valuable insights into the effectiveness and reach of your emails and journeys.

Learn more about Email Sending Statistics metrics
- Targeted : Number of profiles that qualified for the audience before exclusions, suppressions, or consent removals were applied. In journeys with re-entrance enabled, a profile may be targeted multiple times.
- Excluded : Number of profiles which have been excluded by Adobe Journey Optimizer.
- Sent : Total number of emails sent.
- Delivered : Number of emails successfully sent, in relation to the total number of sent messages.
- Bounces : Total of errors cumulated during the sending process and automatic return processing in relation to the total number of sent messages.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.
- Opens : Number of times your emails were opened.
- Clicks : Number of times a content was clicked in your emails.
- Unsubscribe : Number of clicks on the unsubscription link.
- Spam complaints : Number of times a message was declared as spam or junk.
- Retries : Number of emails in the queue for retries.

### Email - Performance by date email-perf-date

The **Email - Performance by date** widget offers a detailed overview of key information related to your emails, presented through a graph, providing insights into the performance trends over the last 24 hours.

Learn more about Email - Performance by date metrics
- Sent : Total number of emails sent.
- Delivered : Number of emails successfully sent.
- Bounces : Total of errors cumulated during the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.
- Opens : Number of times your emails were opened.
- Clicks : Number of times a content was clicked on in your emails.
- Unsubscribe : Number of clicks on the unsubscription link.
- Spam complaints : Number of times a message was declared as spam or junk.

### Email - Bounce categories and reasons email-bounce-categories

The **Bounce Reasons** and **Bounce categories** widgets compile the available data related to bounced messages, providing detailed insights into the specific reasons and categories behind email bounces over the last 24 hours.

For more information on bounces, refer to the [Suppression list](/en/docs/journey-optimizer/using/monitor/deliverability/suppression-list) page.

Learn more about Email - Bounce categories and reasons metrics
- Hard bounce : The total number of permanent errors, such as a wrong email address. This involves an error message that explicitly states that the address is invalid, such as Unknown user.
- Soft bounce : The total number of temporary errors, such as a a full inbox.
- Ignored : The total number of temporary, such as Out of office, or a technical error, for example if the sender type is postmaster.

### Email - Error reasons email-error-reasons

The **Error Reasons** graphs and table offer visibility into the specific errors that occurred during the sending process of the last 24 hours, providing valuable information on the nature and occurrence of errors.

### Email - Excluded reasons email-excluded

The **Excluded Reasons** graphs and table present a comprehensive view of the different factors that resulted in the exclusion of user profiles from the targeted audience, resulting in the message not being received in the last 24 hours.

Refer to [this page](/en/docs/journey-optimizer/using/reporting/channel-report/exclusion-list) for the comprehensive list of exclusion reasons.

### Email - Best recipient domain email-best-recipient

The **Email - Best recipient domain** graph and table offer a detailed breakdown of the domains that profiles most frequently use to open your emails within the last 24 hours. This provides valuable insights into profile behavior, helping you understand preferred platforms.

### Email- Offers email-offers

NOTE
The Offers widgets and metrics are only available if a decision was inserted in an email. For more information on Decision Management, refer to this
page
.
The **Offers statistic** and **Offers statistics over time** widgets measure your offer’s success and impact on your targeted audience. It details the main information relative to your message with KPIs.

Learn more about Email - Offers metrics
- Offer sent : Total number of sends for the offer.
- Offer impression : Number of times the offer was opened in your emails.
- Offer clicks : Number of times an offer was clicked on in your emails.

### Email - Optimization email-sto

NOTE
The
Send time optimization
and
Optimized vs non optimized
widgets are only available if the Send-Time Optimization option is activated for your delivery. For more information on Send-Time Optimization, refer to
this page
.
The **Send time optimization** and **Optimized vs non optimized** widgets detail the success of your emails depending on the sending method: optimized or normal.

Learn more about Send time optimization and Optimized vs non optimized metrics
- Delivered : Number of messages successfully sent, in relation to the total number of sent messages.
- Bounces : Total of errors cumulated during the sending process and automatic return processing in relation to the total number of sent messages.
- Sent : Total number of emails sent for the journey.
- Opens : Number of times your emails were opened in the journey.
- Clicks : Number of times a content was clicked in your emails.

## Push notification tab push-live

From your journey **Live report**, the **Push notification** tab details the main information relative to the push notification sent in your journey.

### Push notification - Sending performance push-sending-performance

The **Push notification sending performance** graph offers a thorough overview of data related to push notifications sent within the past 24 hours. It provides insights into essential metrics such as delivered and bounces, allowing for a detailed examination of the push notifications sending process.

Learn more about Push notification - Sending performance metrics
- Delivered : Number of messages successfully sent.
- Bounces : Total of errors cumulated during the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.

### Push notification - Statistics push-statistics

**Push notification - Statistics** table provides a concise summary of essential data related to your push notifications, including key metrics such as the number of targeted messages and number of successfully delivered messages within the last 24 hours.

Learn more about Push notification - Statistics metrics
- Targeted : Number of profiles targeted for any action such as send email or SMS.
- Excluded : Number of profiles which have been excluded by Adobe Journey Optimizer.
- Sent : Total number of push notifications sent.
- Delivered : Number of push notifications successfully sent.
- Bounces : Total of errors cumulated during the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.
- Opens : Number of times your push notification was opened.

### Push notification - Breakdown by platform push-breakdown

The **Push notification - Breakdown by platform** graph and table provide a detailed analysis of the success of your push notifications, offering insights based on your profile’s operating system. This breakdown enhances your understanding of how well your push notifications perform across different platforms.

### Push notification - Sending summary push-sending-summary

The **Push notification summary** graph offers a dynamic representation, displaying an analysis of your push notifications activity within the last 24 hours. This graphical representation provides a comprehensive breakdown of sent push notifications.

Learn more about Push notification - Sending summary metrics
- Sent : Total number of push notifications sent.
- Delivered : Number of push notifications successfully sent.
- Bounces : Total of errors cumulated during the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.
- Opens : Number of times your push notifications were opened.
- Clicks : Number of times a content was clicked on in your push notifications.

### Push notification - Error reasons push-error

The **Error Reasons** table and graphs provide you with the capability to identify the specific errors that occurred during the sending process of your push notifications, offering detailed insights into any issues encountered in the last 24 hours.

### Push notification - Excluded reasons push-excluded

The **Excluded Reasons** graphs and table display the different reasons that prevented user profiles, excluded from the targeted profiles, from receiving your push notifications within the last 24 hours.

Refer to [this page](/en/docs/journey-optimizer/using/reporting/channel-report/exclusion-list) for the comprehensive list of exclusion reasons.

## SMS tab sms-live

### SMS - Statistics sms-statistics

The **SMS - Statistics** table provides a concise summary of essential data related to your SMS messages, encompassing key metrics such as the number of targeted messages and the count of successfully delivered messages from the last 24 hours.

Learn more about SMS - Statistics metrics
- Targeted : Number of user profiles who qualify as target profiles.
- Excluded : Number of user profiles, excluded from the targeted profiles, who did not receive the message.
- Sent : Total number of SMS messages sent.
- Clicks : Number of times a content was clicked on in your SMS messages.
- Bounces : Total of errors cumulated during the sending process the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.

### SMS - Performance by date sms-performance

The **SMS - Performance by date** widget offers a detailed overview of key information related to your messages, presented through a graph, providing insights into the performance trends over the last 24 hours.

Learn more about SMS - Performance by date metrics
- Sent : Total number of SMS messages sent.
- Bounces : Total of errors cumulated during the sending process and automatic return processing.
- Errors : Total number of errors that occurred during the sending process preventing it from being sent to profiles.

### SMS - Bounces reasons sms-bounces

The **SMS - Bounces reasons** graphs and table provide a comprehensive overview of data related to bounced SMS messages, delivering valuable insights into the specific reasons behind instances of SMS message bounces in the last 24 hours.

### SMS - Error reasons sms-error

The **SMS - Error Reasons** graphs and table allow you to identify the specific errors that occurred during the sending process of your SMS messages, facilitating a thorough analysis of any issues encountered in the last 24 hours.

### SMS - Excluded reasons sms-excluded

The **SMS - Excluded Reasons** graphs and table visually depict the diverse factors that led to the exclusion of user profiles from the targeted audience, preventing them from receiving your SMS messages.

Refer to [this page](/en/docs/journey-optimizer/using/reporting/channel-report/exclusion-list) for the comprehensive list of exclusion reasons.

## In-app tab in-app-live

### In-app performance inapp-performance

The **In-app performance** KPIs provide essential insights into your profiles’ engagement with In-app messages in the last 24 hours, providing essential metrics to assess the effectiveness and impact of the In-app messages included in your journey.

Learn more about In-app - Performance metrics
- Impressions : total number of In-app messages delivered to all users. note NOTE To ensure that an Impression is counted, the user must meet two criteria: Qualification within the In-app experience, achieved by reaching the specific In-app activity in their journey. Meeting the conditions specified in the Trigger rules. Due to the second criterion, there may be notable variations between the number of targeted profiles and the count of unique impressions.
- Interactions : total number of engagements with your In-app message. This includes any actions taken by the users, such as clicks, dismissals, or any other interactions.

### In-app summary inapp-summary

The **In-app summary** graph illustrates the progression of your In-app impressions and interactions over the last 24 hours, providing a comprehensive overview of your In-app messages performance.

Learn more about In-app summary metrics
- Impressions : total number of In-app messages delivered to all users. note NOTE To ensure that an Impression is counted, the user must meet two criteria: Qualification within the In-app experience, achieved by reaching the specific In-app activity in their journey. Meeting the conditions specified in the Trigger rules. Due to the second criterion, there may be notable variations between the number of targeted profiles and the count of unique impressions.
- Interactions : total number of engagements with your In-app message. This includes any actions taken by the users, such as clicks, dismissals, or any other interactions.

### Interactions by type interactions-type

The **Interactions by type** graphs and table details how users interacted with your In-app message by tracking any click, dismiss, or interaction.

recommendation-more-help
