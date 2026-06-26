---
title: "Create a push notification create-push-notification"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/push/create-push"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:50.627649+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create a push notification create-push-notification

Last update: May 8, 2026
- Topics:
- [Push](#)

CREATED FOR:

- Beginner
- User

You can create push notifications for mobile devices (iOS and Android) and web browsers. This page guides you through the process of setting up a push notification in a journey or campaign.

## Create the push notification in a journey or campaign create

To create a push notification, follow the steps below:

Add a Push to a Journey
- Open your journey then drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select Push as the action type.
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the push configuration to use. Learn more
- Additionally: You can apply capping rules to your push action by selecting a rule set in the Business rules drop-down list. Learn more You can use the Send time optimization option to predict the best time to send the message to maximize engagement based on historical open and click rates. Learn how
- Use the Rapid delivery mode to send your push notification in large volumes. Learn how
- Select the Edit content button and create your content as desired. Learn more
- Once your message content has been defined, you can use test profiles or sample input data uploaded from a CSV / JSON file, or added manually to preview its content. Learn how
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more note NOTE To track the behavior of your recipients through push openings and/or interactions, make sure that the dedicated options in the tracking section are enabled in the email activity .

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

Add a Push to a Campaign
- Access the Campaigns menu, then click Create campaign .
- Select the type of campaign that you want to execute Scheduled - Marketing : execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface. API-triggered - Marketing/Transactional : execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing, or transactional messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc.
- From the Properties section, edit your Campaign’s Title and Description .
- Click the Select audience button to define the audience to target from the list of available Adobe Experience Platform audiences. Learn more .
- In the Identity namespace field, choose the namespace to use in order to identify the individuals from the selected audience. Learn more .
- In the Actions section, choose the Push notification and select or create a new configuration. Learn more about Push configuration for mobile on this page and for web on this page .
- Click Create experiment to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. Learn more
- Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the Schedule of your campaign in this section .
- From the Action triggers menu, choose the Frequency of your push notification: Once Daily Weekly Monthly
- From the campaign configuration screen, click the Edit content button to configure the push content. Design a push notification
- Once your message content has been defined, you can use test profiles or sample input data uploaded from a CSV / JSON file, or added manually to preview its content. Learn how
- When your push is ready, complete the configuration of your campaign to send it. To track the behavior of your recipients through push openings and/or interactions, make sure that the dedicated options in the tracking section are enabled in the campaign .

For more information on how to create, configure and activate a campaign, refer to [this page](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns).

**Related topics**

- [Configure push channel](/en/docs/journey-optimizer/using/channels/push/push-config/push-gs)
- [Add a message in a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action)

## Rapid delivery mode rapid-delivery

Rapid delivery mode is a Journey Optimizer add-on that allows very fast push message sending in large volumes though campaigns.

Rapid delivery is used when delay in message delivery is business-critical, when you want to send an urgent push alert on mobile phones, for example a breaking news to users who have installed your news channel app.

For more information on performances when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html#_blank).

### Prerequisites prerequisites

Rapid delivery messaging comes with the following requirements:

- Rapid delivery is available for **Scheduled** campaigns only, and is not available for API-triggered campaigns,
- No personalization is allowed in the push message,
- The target audience must contain less than 30M profiles,
- You can execute up to 5 campaigns simultaneously using the Rapid delivery mode.

### Activate Rapid delivery mode

- Create a push notification campaign and toggle on the Rapid delivery option.
- Configure the message content and select the audience to target. Learn how to create a campaign note important IMPORTANT Ensure that the message content does not include any personalization, and that the audience contains less than 30M profiles.
- Review and activate your campaign as usual. Note that, in test mode, messages are not sent via the Rapid delivery mode.

recommendation-more-help
