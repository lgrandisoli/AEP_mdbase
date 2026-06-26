---
title: "Get started with journey activities about-journey-activities"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:58.387207+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with journey activities about-journey-activities

Last update: May 13, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)
- [Overview](#)

CREATED FOR:

- Beginner
- Intermediate
- User

Combine event, orchestration, and action activities to build multi-step, cross-channel scenarios.

## Event activities event-activities

Personalized journeys start with events such as an online purchase. Once a profile enters a journey, it moves through it on its own. Each profile can take a different path and pace. When you start with an event, the journey triggers when the event arrives. Each profile then follows the steps defined in your journey.

Events configured by the technical user (see [this page](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events)) appear in the first category of the palette. This category is on the left side of the screen. The following event activities are available:

- [General events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/general-events)
- [Reaction](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events)
- [Audience Qualification](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events)

To start your journey, drag and drop an event activity. You can also double-click on it.

## Orchestration activities orchestration-activities

Orchestration activities are conditions that help determine the next step in the journey. These conditions can include whether the person has an open support case or completed a purchase. They can also include the local weather forecast or whether the person reached 10,000 loyalty points.

From the palette, on the left-hand side of the screen, the following orchestration activities are available:

- [Optimize](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize)
- [Read Audience](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience)
- [Wait](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity)
- [Journey Fragments](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-fragments)
- [Content decision](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/content-decision)
- [Dataset lookup](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup)

## Action activities action-activities

Actions are what you want to happen as a result of some kind of trigger, like sending a message. It is the piece of the journey that the customer experiences.

From the palette on the left side of the screen, below **Events** and **Orchestration**, you can find the **Actions** category. The following action activities are available:

- [Built-in channel actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action) available from the **Action** activity
- [Custom actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-custom-actions)
- [Jump](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/jump)

These activities represent the different available communication channels. You can combine them to create a cross-channel scenario.

You can also set up specific actions to send messages:

- If you are using a third-party system to send messages, you can create a specific custom action. Learn more
- If you are working with Adobe Campaign and Adobe Journey Optimizer, refer to these sections: Adobe Journey Optimizer and Adobe Campaign v7/v8 Adobe Journey Optimizer and Adobe Campaign Standard Adobe Journey Optimizer and Adobe Marketo Engage

## Best practices best-practices

Use these recommendations to keep journeys readable, consistent, and easy to troubleshoot.

### Add a label

Most activities allow you to define a **Label**. This adds a suffix to the name that appears under your activity in the canvas. This is useful if you use the same activity several times in your journey and want to identify them more easily. It also makes debugging easier in case of errors and makes reports easier to read. You can also add an optional **Description**.

NOTE
For some activities, their ID is also visible in the pane. This ID can be used in reporting as a more stable key than the label, which can change.
### Manage the advanced parameters advanced-parameters

Most activities display a number of advanced and/or technical parameters that you cannot modify.

For better readability, hide these parameters using the **Hide read-only fields** button on top of the right pane.

In some particular contexts, you can override the values of these parameters for specific use. To force a value, click the **Enable parameter override** icon to the right of the field. [Learn more](/en/docs/journey-optimizer/using/configuration/primary-email-addresses#override-execution-address-journey)

NOTE
If the advanced parameters are hidden, click the
Show read-only fields
button
{width="60%"}
### Add an alternative path

When an error occurs in an action or a condition, the journey of an individual stops. The only way to make it continue is to check the box **Add an alternative path in case of a timeout or an error**. See [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer#paths)

## Troubleshooting troubleshooting

Before testing and publishing your journey, verify that all the activities are properly configured. You cannot perform tests or publications if errors are still detected by the system.

Learn how to troubleshoot errors in activities and in the journey [on this page](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting).

See also [Monitoring & troubleshooting](/en/docs/journey-optimizer/using/monitor/troubleshoot-journey-landing-page)

recommendation-more-help
