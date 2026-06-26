---
title: "Reaction events reaction-events"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:48.982147+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Reaction events reaction-events

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

## Overview overview

Among the different event activities available in the palette, you will find the built-in **Reactions** event. This activity allows you to react to tracking data related to a message sent within the same journey. We capture this information in real-time at the moment it is shared with Adobe Experience Platform.

You can react to clicked or opened messages. For example, you can send another message if an individual opened the previous email or clicked inside it, or send a different follow-up message if they did not engage with your communication.

See [Action activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities#action-activities).

You can use the **Reaction** activity to perform an action when there is no reaction to your messages. To do this, create a second path parallel to the **Reaction** activity and add a **Wait** activity. If there is no reaction during the period defined in the **Wait** activity, the second path will be chosen. You can choose to send, for example, a follow-up message.

## How to configure reaction events configure

Follow these steps to configure the reaction events:

- Place a **Reaction** activity **immediately** after a [channel action activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action) on the journey canvas.
- Add a **Label** to the reaction. This step is optional.
- From the drop-down list, select the action activity you want to react to. You can select any action activity positioned in the previous steps of the path.
- Depending on the action you selected, choose what you want to react to.
- You can define an event timeout (between 40 seconds and 90 days) and a timeout path. This creates a second path for individuals who did not react within the defined duration. When testing a journey that uses a reaction event, the test mode **Wait time** default and minimum value is 40 seconds. See [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey).

## Guardrails and limitations guardrails-limitations

- A **Reaction** activity must be placed **immediately** after a [channel action activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action) in the journey canvas.
- You cannot use a **Reaction** activity if there is no channel action activity before it.
- Placing a **Wait** activity or any other activity between the channel action and the **Reaction** activity is not supported and may result in the Reaction not working as expected.
- Reaction events can only track messages sent within the same journey. They cannot track messages that take place in a different journey.
- Reaction events track clicks on links of the type “tracked”. Unsubscription and mirror page links are not taken into account.
- Email opens are tracked using a 0-pixel image included in the email. If email clients (such as Gmail) block images, email opens will not be taken into account.

recommendation-more-help
