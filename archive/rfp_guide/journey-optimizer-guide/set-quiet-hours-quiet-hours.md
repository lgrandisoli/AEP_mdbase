---
title: "Set quiet hours quiet-hours"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/quiet-hours"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:31.669560+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Set quiet hours quiet-hours

Last update: May 8, 2026
- Topics:
- [Rules](#)

CREATED FOR:

- Intermediate
- User

## What are quiet hours

**Quiet hours** let you define time-based exclusions for **Email**, **SMS**, **Push**, and **WhatsApp** channels. They ensure that no messages are sent during specific periods of time, helping you respect customer preferences and compliance requirements.

You can apply quiet hours through **rule sets**, which can be assigned to individual actions in campaigns or journeys for precise control.

By streamlining these processes, you can enhance customer experience, save time, and ensure compliance with communication rules:

- **Don’t wake up your customer** - *The right customer, right channel, right time* is the mantra of many marketers, so it makes sense that timing is a critical part of the customer journey. By setting a Quiet hours rule, brands have better control over when contacts are receiving messages, ensuring they are getting them when they’re more likely to take action on your message.
- **Convenience** - Easily intercept communications across campaigns & journeys when you need to prevent an audience from receiving a message without needing to stop the entire journey or campaign.
- **Time Saving** - Manage exclusions in one place by creating a **time-based rule**, instead of adding multiple condition nodes with custom expressions.

➡️ [Discover this feature in video](#video)

## Guardrails & limitations

- **Supported channels** - Email, SMS, Push, and WhatsApp.
- **Orchestrated campaigns** - Quiet hours are not supported for Orchestrated campaigns.
- **Propagation delay** – Updates to a quiet hours rule may take up to 12 hours to be applied to channel actions that already use that rule.
- **High-volume latency** – In cases of high-volume communications, the system may take additional time to begin successfully enforcing quiet hour suppressions.

## Create Quiet hours rules

To set quiet hours, create a rule inside a custom rule set. [Learn how to create rule sets](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets#Create). Follow these steps:

- Navigate to Business rules to access the rule sets inventory.
- Choose an existing custom rule set or create a new one: accordion Create a Quiet hours rule in an existing rule set Select the rule set from the inventory. Quiet hours rules can only be added to rule sets with the “channel” domain. You can check this information in the Domain column. accordion Create a Quiet hours rule in a new rule set Click Create rule set , enter a unique name, and select “Channel” from the Rule Set Domain drop-down. note NOTE Quiet hours can only be defined in custom rule sets . The global rule set does not support quiet hours configuration.
- In the rule set screen, click Add Rule and provide a unique name for the rule.
- The Category field specifies the category of message the rule applies to. For now, this field is read-only and defaults to Marketing .
- In the Rule type drop-down, select Quiet hours .
- In the Dates & times section, define when to apply quiet hours: In the Time zone drop-down, apply a standard time zone to all recipients in the audience, regardless of their individual time zones. To use the time zone field from each profile, select Use recipients local time zone . Learn more on time zone management in journeys note important IMPORTANT If a profile has no time zone value, quiet hours are not enforced for that profile. Specify the time period at which quiet hours should apply. Weekly - Choose specific days of the week and a timeslot. You can also enforce the rule All day . Custom date - Choose specific dates in the calendar and a timeslot. You can also enforce the rule All day . Click the Add more dates button to add up to 5 separate periods.
- In the Handling actions during quiet hours section, choose how messages are treated during the selected period of time: Queue message - Messages are sent at the completion of the quiet hours period unless in Paused state. note NOTE If a message remains in a queued state for a profile for more than 7 days, the message will be discarded. Discard message - Messages are never sent. note NOTE If you select Discard and apply this rule to a journey action, the profile is removed from the message delivery and exited from the journey.

The rule now displays in the rule set. You can select it to display its details in the properties pane.

If your rule is ready, activate it and complete the configuration of your rule set. [Learn how to create and activate rule sets](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets#Create)

## Apply Quiet hours to journeys and campaigns apply

Once your rule is saved and the rule set is activated, you can apply it to actions in journeys and campaigns. Supported channels: **Email, SMS, Push, WhatsApp**. Browse the tabs below for more details.

Apply Quiet hours channel actions in journeys
- Open your journey, select a channel action and edit the content of your message.
- Click the Add Business Rule button and select the rule set containing the Quiet hours rule. note NOTE Only activated rule sets display in the list.
- Activate your journey.

Apply Quiet hours to campaign actions
- Edit your campaign and access the Actions tab.
- In the Business rules section, select the rule set containing the Quiet hours rule. note NOTE Only activated rule sets display in the list.
- Activate your campaign.

## Next steps

Once your journey or campaigns has been activated and executed, you can view the number of profiles excluded from the communication in the [Customer Journey Analytics report](/en/docs/journey-optimizer/using/reporting/channel-report/report-gs-cja), and in the [Live report](/en/docs/journey-optimizer/using/reporting/live-report/live-report), where Quiet hours rules will be listed as a possible reason for users excluded from delivery.

## How-to video video

Learn how to use the quiet hours feature in Adobe Journey Optimizer.

https://video.tv.adobe.com/v/3475851?quality=12&learn=on
recommendation-more-help
