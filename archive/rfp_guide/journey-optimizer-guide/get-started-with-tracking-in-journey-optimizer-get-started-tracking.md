---
title: "Get started with tracking in Journey Optimizer get-started-tracking"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/monitor/get-started-tracking"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:48.839646+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with tracking in Journey Optimizer get-started-tracking

Last update: May 8, 2026
- Topics:
- [Monitoring](#)

CREATED FOR:

- Beginner
- User

Tracking enables you to measure campaign effectiveness, optimize customer experiences, and ensure messages reach their intended recipients. Journey Optimizer provides comprehensive tracking capabilities that capture customer interactions, delivery performance, and system health—helping you make data-driven decisions while respecting privacy and maintaining compliance.

Most tracking is automatically configured when you create messages and journeys. For advanced scenarios, you can set up custom metrics, configure URL parameters, and integrate with external analytics platforms. Access your tracking data through built-in reports or export it for deeper analysis in Customer Journey Analytics.

What you can track in Journey Optimizer:

📧 **Email interactions** - Opens, clicks, and link performance

🌐 **Web behavior** - Page views, clicks, and engagement patterns

🛤️ **Journey performance** - Custom metrics, step events, and conversion paths

📊 **Deliverability health** - Bounce rates, spam complaints, and sender reputation

⚙️ **System operations** - Alerts, errors, and custom action performance

style
shade-box
To help you get started, explore these essential tracking and monitoring topics:

**Configure success metrics**

*Track custom KPIs aligned with your business objectives*

**Monitor deliverability**

*Ensure your messages reach customer inboxes*

**Explore reporting**

*Access live and historical reports for your journeys and campaigns*

## Track customer interactions across channels tracking-by-channel

Journey Optimizer provides channel-specific tracking capabilities. Here’s how to configure and use tracking for each channel.

Email tracking
Email tracking is automatically enabled when you create an email message. Journey Optimizer tracks opens, clicks, and unsubscribes by default—no additional configuration needed.

**Configure tracking options:**

- Enable/disable tracking - Control tracking at the message level when designing your email. You can choose to track opens, clicks, or both. Learn more
- Set up URL tracking parameters - Configure tracking parameters at the surface level to automatically append campaign identifiers (utm_campaign, utm_source, etc.) to all email links. This enables attribution tracking across your entire digital ecosystem. Learn more
- Track links in saved fragments - When you save a fragment from content that has tracking enabled, the links in that fragment remain tracked when you reuse it in other journeys or campaigns. Learn more
- Add mirror page tracking - Enable mirror page option to create a web version of your email with automatic tracking of who views it. Learn more

**Monitor performance:** View real-time metrics in campaign and journey reports including opens, clicks, and link-level performance. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-email) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-email)

Web tracking
Web tracking requires explicit configuration to track user interactions with your web modifications.

**Set up click tracking:**

When authoring a web page, you can select specific elements (buttons, images, links) that you want to track. This enables click tracking for those elements without requiring additional code. [Learn more](/en/docs/journey-optimizer/using/channels/web/author-web-pages/monitor-web-experiences)

- **Track any clickable element** - Select buttons, images, links, or any interactive element in your web personalization.
- **Automatic data collection** - Once configured, Journey Optimizer automatically captures click events and associates them with profiles.
- **Monitor in real-time** - Track user interactions as they happen to validate personalization effectiveness.

**View tracking data:** Access display metrics, click-through rates, and element-level performance in reports. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-web) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-web)

Push notification tracking
Push tracking is automatically enabled and captures impressions (delivered), clicks (tapped), and opens (app launched). To maximize tracking value, configure clickable elements in your push content.

**Configure tracked elements:**

- Body click behavior - Set what happens when users tap the notification: open app, navigate to a deeplink, or open a web URL. Each action is automatically tracked. Learn more
- Add action buttons - Include up to 3 buttons (Android) or multiple buttons (iOS) with independent tracking for each button action (open app, deeplink, web URL). Learn more
- Enable tracking - Verify tracking is enabled in your push journey activity or campaign tracking settings. Learn more

| note |
| --- |
| NOTE |
| Push tracking requires mobile SDK implementation. Ensure your app has the Adobe Experience Platform Mobile SDK properly configured. [Learn more](/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration#integrate-mobile-app) |

**Analyze engagement:** View click-through rates, button performance, and tracked link details in reports. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-push) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-push)

In-app message tracking
In-app messages automatically track displays and user interactions. Configure triggers and content to maximize tracking effectiveness.

**Set up tracking:**

- Define display rules - Set when and where in-app messages appear using triggers (app launch, screen load), frequency rules, and audience conditions. Proper configuration ensures accurate tracking of both triggered and displayed messages.
- Add tracked elements - Include buttons, links, and interactive elements in your message content. Each interaction is automatically tracked with detailed labels.
- Optimize display timing - Configure day-of-week and time-of-day rules to maximize the likelihood that triggered messages are actually displayed to users.

[Learn how to configure In-app messages](/en/docs/journey-optimizer/using/channels/in-app/create-in-app)

**What gets tracked:** Journey Optimizer automatically captures displays, button clicks, dismissals, triggered vs. displayed metrics, and link performance. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-inapp) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-inapp)

SMS & MMS tracking
SMS tracking requires minimal setup—Journey Optimizer automatically shortens and tracks links you include in messages.

**How it works:**

- Automatic link tracking - Add any URL to your SMS content using the URL helper function. Journey Optimizer automatically shortens the link and tracks clicks without additional configuration. To use URL shortening, you must first configure an SMS subdomain. Learn more
- Inbound message tracking - Replies from recipients are automatically captured, allowing you to monitor two-way conversations and response patterns. Learn more

**View metrics:** Access link click data, inbound message volumes, and message type performance in reports. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-sms) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-sms)

Code-based experience tracking
Code-based experiences require implementation setup to send tracking data to Adobe Experience Platform.

**Prerequisites:**

Before tracking will work, you need to configure your implementation to send interaction events (displays, clicks) to Adobe Experience Platform. This requires:

- Setting up a datastream configured for Adobe Experience Platform. [Learn more](/en/docs/experience-platform/datastreams/overview)
- Implementing event collection in your code using Web SDK or Mobile SDK.
- Sending display and interaction events when content is shown or clicked.

[Learn more about implementation prerequisites](/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/code-based-prerequisites#reporting-prerequisites)

**What gets tracked:** Once implemented, track displays, clicks, click-through rates, and element-level performance across any digital touchpoint (websites, mobile apps, IoT devices, etc.). [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-code) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-code)

Content card tracking
Content cards automatically track user interactions. Configure content and display rules to control tracking behavior.

**How to implement:**

- Design tracked content - Add buttons and links to your content card. Each interactive element is automatically tracked with labels and URLs.
- Configure persistence - Content cards persist across app sessions, allowing you to track long-term engagement patterns. Set expiration rules to control how long cards remain trackable.
- Set up display rules - Define when and where cards appear to ensure accurate tracking of displays vs. interactions.

[Learn how to configure content cards](/en/docs/journey-optimizer/using/channels/content-card/create-content-card)

**Monitor engagement:** Track displays, clicks, click-through rates, and engagement patterns across multiple sessions. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-content) | [Journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-content)

Landing page tracking
Landing pages come with built-in tracking that requires no additional setup. Journey Optimizer automatically captures visits, conversions, and bounce rates.

**What’s tracked automatically:**

- **Visits** - Total and unique visits to measure reach
- **Conversions** - Form submissions, subscription confirmations, or other defined actions
- **Bounce rate** - Percentage of visitors who leave without interacting
- **Performance trends** - Time-series data showing how metrics evolve

[Learn how to configure landing pages](/en/docs/journey-optimizer/using/content-management/landing-pages/create-lp)

**Monitor performance:** Track visit patterns, conversion rates, and bounce rates over time to understand how users interact with your forms and identify areas for improvement. [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/lp-report-global-cja)

## Track your journey and campaign activity journey-campaign-tracking

Beyond channel-level tracking, configure tracking to measure overall performance and understand customer behavior across your marketing initiatives.

- Define custom success metrics - Configure specific KPIs aligned with your business objectives (purchases, sign-ups, renewals, etc.) beyond standard engagement metrics. Learn more
- Enable journey step events - Activate detailed tracking of every action customers take as they move through journeys. This provides granular visibility into entry/exit points, path selection, and drop-off locations. Learn more
- Set up scheduling - Configure send-time optimization to track performance across different timing strategies and identify optimal send windows. Learn more
- Configure custom actions monitoring - Set up tracking for integrations with external systems to monitor API calls, response times, and error patterns. Learn more
- Create custom reports and export data - Build tailored reports and export tracking data to external systems for deeper analysis. Learn more
- View unified performance: Access comprehensive reports for both campaigns and journeys to compare performance across email, push, SMS, and other channels, and to understand which combinations drive the best results. Campaign reports | Journey reports

## Track optimization & decisioning performance optimization-decisioning-tracking

Journey Optimizer automatically tracks optimization experiments, targeting strategies, and decisioning performance. Configure your settings to ensure proper data collection.

### Set up optimization tracking optimization-tracking

- Optimization in your campaigns and journeys : When creating experiments, define which metrics to track (conversions, clicks, custom events). Journey Optimizer automatically collects performance data for each treatment. Learn more Create targeting rules to deliver different content to different audience segments. Journey Optimizer automatically tracks engagement metrics for each targeted group, allowing you to compare performance across segments. Learn more
- Journey path optimization : Add an Optimize activity to your journey and configure multiple paths. Journey Optimizer automatically tracks which paths profiles take and measures performance. Learn more

To analyze results: view conversion rates, statistical significance, and lift between treatments in experimentation reports, or compare engagement metrics across targeted segments. [Experimentation campaign report](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-experimentation) | [Experimentation journey report](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-experimentation) | [Journey targeting report](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja#targeting)

### Track decisioning performance decisioning-tracking

When using Decisioning to personalize content, Journey Optimizer automatically tracks decision events, impressions, and clicks with no additional configuration required.

- **Automatic event capture** - Journey Optimizer automatically captures decision events whenever a decision item is selected for a profile.
- **Impression tracking** - For emails, impressions are tracked automatically. For code-based experiences, you need to implement proposition display events in your code. [Learn more](/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/code-based-implementation-samples#client-side-how)
- **Click tracking** - Clicks on decision items are automatically tracked in emails; code-based experiences require implementing click events.

NOTE
To track decisioning in
code-based experiences
, ensure your implementation sends proposition interaction events (displays and clicks) to Adobe Experience Platform using Web SDK or Mobile SDK.
Learn more
To monitor performance: view decisioning KPIs, compare decision items, analyze selection strategies, and monitor AI model performance in reports. [Learn more](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/cja-reporting)

## Control tracking data usage data-governance

Data governance policies allow you to control how tracking data can be used across your organization:

- Label sensitive tracking data - Apply governance labels to tracked behavioral data (e.g., clicks on health content, financial product interactions) to mark it as sensitive or regulated.
- Restrict data usage - Create policies that prevent labeled tracking data from being used in certain channels, exported to third-party systems, or used for specific personalization scenarios.
- Automatic enforcement - Journey Optimizer automatically checks governance policies when you build journeys and campaigns, blocking publication if tracked data is being used in violation of defined policies.

Data governance ensures compliance with regulations like GDPR and CCPA while still allowing you to track and analyze customer behavior within approved boundaries. [Learn more](/en/docs/journey-optimizer/using/privacy/action-privacy)

## Monitor deliverability & system health monitoring-capabilities

Beyond tracking engagement, configure monitoring to ensure messages reach inboxes and systems perform optimally.

Deliverability monitoring helps ensure your messages reach recipients’ inboxes and maintain healthy sender reputation by tracking key indicators:

- Review the suppression list regularly to understand why addresses are blocked and maintain list hygiene. Learn more
- Analyze delivery errors to diagnose failures and take corrective action. Learn more
- Follow best practices for DMARC, SPF, and DKIM to maximize inbox placement. Learn more

Set up proactive monitoring to receive real-time notifications about critical events and system issues, enabling you to respond quickly before they impact your customer experiences:

- Configure alerts - Set up real-time notifications for journey errors, custom action failures, and critical issues to respond quickly to problems. Learn more
- Enable audit logs - Activate audit logging to track all actions on resources for compliance and troubleshooting. Learn more
- Monitor integrations - Track custom action performance and external system connectivity to identify integration issues early. Learn more

recommendation-more-help
