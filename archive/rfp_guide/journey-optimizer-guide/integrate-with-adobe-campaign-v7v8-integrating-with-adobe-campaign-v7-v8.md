---
title: "Integrate with Adobe Campaign v7/v8 integrating-with-adobe-campaign-v7-v8"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/acc-action"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:59.418112+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Integrate with Adobe Campaign v7/v8 integrating-with-adobe-campaign-v7-v8

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Actions](#)
- [Custom Actions](#)

CREATED FOR:

- Intermediate
- Developer
- Admin

If you have Adobe Campaign Classic v7 or Campaign v8, a specific custom action is available in your journeys to integrate Adobe Journey Optimizer and Adobe Campaign. This integration allows you to send emails, push notifications and SMS using Adobe Campaign Transactional Messaging capabilities. Learn more in this [end-to-end use case](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/ajo-ac).

For each action configured, a [Campaign action activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-adobe-campaign-v7-v8) is available in the journey designer palette.

## Activation access

When requested, the connection between the Journey Optimizer and Adobe Campaign environments is setup by Adobe at provisioning time. If you have not requested the connection at provisioning time, contact Adobe Journey Optimizer support to request the activation. You must provide the following details:

For Adobe Journey Optimizer
- Organisation ID (Adobe OrgID)
- Sandbox Name

For Adobe Campaign
- Campaign Server URL
- Real-Time Server URL
- Your Adobe Campaign version

## Guardrails and limitations important-notes

- There is no throttling of messages. The system caps the number of messages that can be sent over to 4,000 per 5 minutes, based on the current Campaign SLA. For this reason, Journey Optimizer should only be used in unitary use cases (individual events, not audiences).
- You must configure one action on the canvas per template to use. You need to configure one action in Journey Optimizer for each template you wish to use from Adobe Campaign.
- We recommend that you use a dedicated Message Center hosted or Managed Services instance for this integration to avoid impacting any other Campaign operations that you may have going on. The marketing server can be hosted or on-premise.
- There is no validation that the payload or Campaign message is correct.
- You cannot use a Campaign action with an audience qualification event.

## Prerequisites prerequisites

In Adobe Campaign, you must create and publish a transactional message and its associated event. Refer to the [Adobe Campaign documentation](/en/docs/campaign/campaign-v8/send/real-time/transactional#_blank).

You can build your JSON payload corresponding to each message following the pattern below. You will then paste this payload when configuring the action in Journey Optimizer (see below).

Example
| code language-json |
| --- |
| { "channel": "email", "eventType": "welcome", "email": "Email address", "ctx": { "firstName": "First name" } } |

- **channel**: the channel defined for your Campaign transactional template
- **eventType**: the internal name of your Campaign event
- **ctx**: variable based on the personalization you have in your message

## Configure the action configure-action

In Journey Optimizer, you must configure one action per transactional message.

To create a Campaign action, follow these steps:

- Create a new action. [Learn how to create custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action).
- Enter a name and description.
- In the **Action type** field, select **Adobe Campaign Classic**.
- Click in the **Payload** field and paste an example of the JSON payload corresponding to the Campaign message. Contact Adobe to get this payload.
- Set each field as either static or variable based on whether you want it to be mapped on the Journey canvas. For example, fields like email channel parameters and personalization fields (ctx) should typically be set as variables so they can dynamically adapt within the journey.
- Click **Save**.

## Update an existing action update-action

If you need to update an existing Campaign v7/v8 custom action, for example when the Real-Time (RT) endpoint changes after initial setup, follow these steps:

- From the **Administration** menu, select **Configurations**, then go to **Actions**.
- Locate and select the Campaign action you want to update from the actions list.
- Click **Edit** to open the action configuration.
- Update the **URL** field with the new RT endpoint URL. Ensure the endpoint format is correct and reachable.
- If needed, update the **Payload** configuration to match any changes in the Campaign transactional message structure.
- Click **Test** to validate the connection to the new endpoint. Verify that the test returns a successful response before proceeding.
- Once validated, click **Save** to apply your changes.

NOTE
Any journeys that use this action will automatically use the updated configuration. If you have live journeys using this action, monitor them closely after updating the endpoint to ensure proper message delivery.
recommendation-more-help
