---
title: "Integrate with Adobe Campaign Standard using_adobe_campaign_standard"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/acs-action"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:59.928964+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Integrate with Adobe Campaign Standard using_adobe_campaign_standard

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Actions](#)
- [Custom Actions](#)

CREATED FOR:

- Intermediate
- Developer
- Admin

If you have Adobe Campaign Standard, a built-in action is available to allow the connection to Adobe Campaign Standard. You can send emails, push notifications and SMS using the Adobe Campaign Standard’s Transactional Messaging capabilities.

The Campaign Standard transactional message and its associated event must be published in order to be used in Journey Optimizer. If the event is published but the message is not, it will not be visible in the Journey Optimizer interface. If the message is published but its associated event is not, it will be visible in the Journey Optimizer interface but it will not be usable.

## Guardrails and limitations important-notes

- A capping rule of 4,000 calls per 5 minutes is automatically defined for Adobe Campaign Standard actions. Read more about transactional messaging SLAs in Adobe Campaign Standard Product Description .
- Adobe Campaign Standard integration is set up through a dedicated built-in action in the action list. This must be configured for each sandbox.
- You cannot use a Campaign Standard action with an Audience qualification or Read audience activity.
- A journey cannot use both built-in channel actions and Campaign Standard actions .

## Configure the action configure-action

In Journey Optimizer, you must configure one action per transactional message.

To configure a Campaign Standard action, follow these steps:

- Select Configurations in the ADMINISTRATION menu section.
- In the Actions section, click Manage . The list of actions is displayed.
- Select the built-in AdobeCampaignStandard action. The action configuration pane opens on the right side of the screen.
- Copy your Adobe Campaign Standard instance URL and paste it in the URL field.
- Click the Test the instance URL to test the validity of the instance. note NOTE This test verifies that: The host is “.campaign.adobe.com”, “.campaign-sandbox.adobe.com”, “.campaign-demo.adobe.com”, “.ats.adobe.com” or “.adls.adobe.com” The URL starts with https The Organization associated with this Adobe Campaign Standard instance is the same as the Journey Optimizer Organization

Once this configuration is done, three actions are available in the **Action** category when designing a journey: **Email**, **Push**, **SMS**. [Learn how to use them](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-adobe-campaign-standard).

Use a **Reactions** event to react to tracking data related to a Campaign Standard message sent within the same journey:

- For push notifications, journeys can react to clicked, sent or failed messages.
- For SMS messages, journeys can react to sent or failed messages.
- For emails, journeys can react to clicked, sent, opened or failed messages. Learn more about reactions events .

When using a third-party system to send messages, you must add and configure a custom action. [Learn more about custom action configuration](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration).

recommendation-more-help
