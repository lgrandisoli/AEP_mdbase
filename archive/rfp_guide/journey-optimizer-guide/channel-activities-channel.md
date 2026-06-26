---
title: "Channel activities channel"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:57.744467+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Channel activities channel

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

Adobe Journey Optimizer allows you to automate and execute campaigns across channels—email, SMS, push notifications, and direct mail—for both marketing and transactional messages. You can combine these channel activities into the campaign canvas to create cross-channel Orchestrated campaigns. These campaigns can trigger actions based on customer behavior and data.

For example:

- Send a welcome series through email, SMS, push and direct mail.
- Deliver a follow-up email post-purchase.
- Send personalized birthday greetings via SMS.

By using channel activities, you can create comprehensive and personalized campaigns that engage customers across multiple touchpoints and drive conversions.

CAUTION
Only SMS, Push, Email and Direct mail channels are supported in Orchestrated campaigns.
## Add a channel activity and define its properties add

PREREQUISITES
Before adding a channel activity, define the target audience using a
Build audience
or a
Read audience
activity.
- Add a channel activity into the canvas. Available channel activities are Email , SMS , Push and Direct mail .
- In the right rail, use the Category field to choose Marketing or Transactional for this message. Transactional messages do not require opt-in and are suited for time-sensitive communications such as disruptions, emergencies, or cancellations.
- Select the activity and click Edit email , Edit SMS , Edit Push , or Edit direct mail depending on the chosen channel.
- In the Properties tab, enter a description then switch to the Actions tab to configure the activity.

## Marketing vs Transactional messages marketing-vs-transactional

Choosing the right category determines how messages are delivered and which rules apply:

Marketing
Transactional
Opt-in required
Yes
No
Business rules
Applied (frequency capping, fatigue rules)
Bypassed
Channel configuration type
Marketing channel configuration
Transactional channel configuration
Typical use cases
Promotions, newsletters, seasonal campaigns
Order confirmations, password resets, disruption alerts
Audience
Opted-in subscribers only
Any profile, regardless of opt-in status
NOTE
Use Transactional only for operational or time-sensitive communications. Misclassifying a promotional message as Transactional bypasses consent and business rules, which may violate regulatory requirements.
## Set up the channel configuration and settings configuration

Use the **Actions** tab to select a channel configuration for your message and configure additional settings such as tracking, content experiment, or multilingual content.

- Select a channel configuration A configuration is defined by a System Administrator . It contains all the technical parameters for sending the message, such as header parameters, subdomain, mobile apps, etc. Learn how to set up channel configurations
- Apply capping rules In the Rule set drop-down list, select a channel rule set to apply capping rules to your campaign. Leveraging channel rule sets allows you to set frequency capping by communication type to prevent overloading customers with similar messages. Learn how to work with rule sets .
- Create a content experiment Use the Content experiment section to define multiple delivery treatments in order to measure which one performs best for your target audience. Click the Create experiment button then follow the steps detailed in this section: Create a content experiment .
- Add multilingual content Use the Languages section to create content in multiple languages within your campaign. To do so, click the Add languages button and select the desired Language settings . Detailed information on how to set up and use multilingual capabilities are available in this section: Get started with multilingual content .

Additional settings are available depending on the selected communication channel. Expand the sections below for more information.

Track engagement
(Email and SMS).
Use the
Action tracking
section to track how your recipients react to your email or SMS deliveries. Tracking results are accessible from the campaign report once the campaign has been executed.
Learn more about campaign reports
Enable Rapid delivery mode
(Push).
Rapid delivery mode is a Journey Optimizer add-on that allows very fast push message sending in large volumes through campaigns. Rapid delivery is used when delay in message delivery is business-critical. For instance, you want to send an urgent push alert on mobile phones, such as breaking news to users who have installed your news channel app. Learn how to enable Rapid delivery mode for Push notifications [on this page](/en/docs/journey-optimizer/using/channels/push/create-push#rapid-delivery).

For more information on performance when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html#_blank).

When your channel activity has been configured, select the **Content** tab to define its content.

## Define the content content

### Create the message content

Switch to the **Content** tab to create your message. The process steps vary based on the selected channel. Learn detailed steps to create your message content in the following pages.

Create an email
Create an SMS
Create a push notification
Create a direct mail
### Add personalization

Personalization in Orchestrated campaigns works similarly to other Journey Optimizer campaigns or journeys, with a few key differences specific to the orchestrated canvas.

When you access the personalization editor from an Orchestrated campaign, two main folders contain attributes available for personalization detailed below.

- Profile attributes This folder includes all profile-related data from Adobe Experience Platform. These are standard attributes such as name, email address, location, or any other traits captured in the user profile.
- Target attributes (specific to Orchestrated campaigns) This folder is unique to Orchestrated campaigns. It contains attributes calculated directly within the campaign canvas. It contains two subfolders: <Targeting dimension> (e.g., “Recipients”, “Purchases”): Contains all attributes related to the dimension targeted by your campaign. Enrichment : Includes data added via Enrichment activities in your canvas. This allows you to personalize messages based on external datasets or additional logic incorporated during orchestration. Learn how to use an Enrichment activity

For a detailed overview of how to use the personalization editor, refer to [Get started with personalization](/en/docs/journey-optimizer/using/content-management/personalization/personalize).

### Check and test your content simulate-content-test-profiles

Once the content is created, use the **Simulate Content** button to preview and test your content with test profiles or sample input data uploaded from a CSV / JSON file, or added manually. [Learn more](/en/docs/journey-optimizer/using/test/preview-test/preview-test)

When you simulate content with **test profiles** in an Orchestrated campaign, two important constraints apply:

- Execution must have reached the channel activity in test - Run the campaign in test using the Start button so the workflow reaches the channel activity you want to simulate. In test mode, the workflow pauses at the channel activity, so a channel activity that comes after another channel activity is never reached. You cannot use Simulate Content for those downstream channel activities. See Test your campaign before publishing .
- The test profile must match the channel activity target - Use a test profile that belongs to the audience targeted by that channel activity. If the profile is not in that audience, selecting it will not render a preview of your content. See Select test profiles .

## Confirm message sending

By default, for non-recurring orchestrated campaigns, message delivery is paused until you explicitly approve the send. After publishing the campaign, confirm the send request from the channel activity’s properties pane.

Sending confirmation can be disabled before publishing the orchestrated campaign. To do so, select the channel activity in the canvas to display its properties, and turn on **Send without confirmation**.

## Set rate control rate-control

Journey Optimizer allows you to enable rate control for outbound actions in Orchestrated campaigns.

This feature is particularly useful for preventing overload on downstream systems, such as landing pages or customer care platforms. For example, you can set a rate limit of 165 messages per second to ensure steady delivery without overwhelming downstream systems.

To set rate control, follow these steps:

- Select an outbound channel activity in the canvas and click Edit email , Edit SMS , or Edit Push depending on the chosen channel.
- Navigate to the Schedule tab, and enable the Throttle delivery option in the Delivery settings section.
- Specify the desired Delivery rate per second. Minimum delivery rate supported: 1 per second. Maximum delivery rate supported: 2000 per second when the “Throttle delivery” option is enabled.

IMPORTANT
When setting a delivery rate, the maximum timeframe for which a campaign audience can execute is 12 hours. If the delivery rate is set to a value that does not allow all the audience to be sent the message in the 12-hour timeframe, then the remaining profiles will be excluded from the campaign. You can see the count of these excluded profiles in the campaign report.
## Next steps next

When the message content is ready, navigate back to your Orchestrated campaign using the **Back** arrow. You can then complete the activities orchestration in the canvas and publish the campaign to start sending messages. [Learn how to start and monitor Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/start-monitor-campaigns)

recommendation-more-help
