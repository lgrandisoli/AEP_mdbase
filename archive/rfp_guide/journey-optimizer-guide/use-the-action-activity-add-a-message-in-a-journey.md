---
title: "Use the Action activity add-a-message-in-a-journey"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:54.758633+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use the Action activity add-a-message-in-a-journey

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)
- [Channels Activity](#)

CREATED FOR:

- Intermediate
- User

The **Action** activity is the single entry point for all channel actions in the journey canvas.

It replaces the previous individual built-in channel activities and consolidates Email, Push, SMS, In-app, Web, Code-based experience, and Content Card into one unified activity type.

Use it to:

- Configure any built-in channel action from a single, streamlined interface.
- Build multi-action inbound action groups.
- Apply optimization to any channel action.

NOTE
You can also set up custom actions to send your messages in Journey Optimizer.
Learn more
## About legacy channel activities

Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are **deprecated as of the March 2026 release**.

Existing journeys using these activities continue to work without any changes—no migration is required.

Legacy native channel activities are also preserved in these cases:

- **Duplicate a journey** — The duplicated journey continues to use legacy activities. You can edit and publish it as is; no migration is required.
- **Create a new journey version** — The new version continues to use legacy activities. You can edit and publish it as is; no migration is required.
- **Copy and paste legacy activities in a journey** — Pasted activities remain legacy activities. You can edit and publish them as is; no migration is required.

## Add a built-in channel action to a journey add-action

To add a built-in channel action to your journey using the **Action** activity, follow the steps below.

NOTE
For more information on the channels available in journeys, refer to the table in this section:
Channels in journeys & campaigns
.
- Start your journey with an Event or a Read Audience activity.
- From the Actions section of the palette, drag and drop an Action activity into the canvas.
- Select the built-in channel activity you want to leverage in your journey.
- Add a label to your action and select Configure action . {width="80%"}
- You are directed to the Actions tab of the journey action configuration screen. Select the configuration to use for the selected channel.
- If you selected an inbound channel, you can add multiple actions. Learn more
- Configure your activity according to the selected channel. Detailed configuration guidelines are available in the links below. Learn the detailed steps to create your outbound action as follows: table 0-row-3 0-border-0 layout-fixed html-authored no-header Create emails Create push notifications Create text messages (SMS/MMS) Learn the detailed steps to create your inbound action as follows: table 0-row-4 0-border-0 layout-fixed html-authored no-header Create In-app messages Create web experiences Create content cards Create code-based experiences note NOTE Each inbound experience action comes with a 3-days Wait activity. Learn more For emails and push notifications, you can enable Send-Time Optimization. Learn more
- Depending on the activity, you can display advanced parameters specific to the selected channel, and override some default values such as the execution address. Learn more note NOTE If the advanced parameters are hidden, click the Show read-only fields button on top of the right pane.
- Use the Optimization section to run content experiments, leverage targeting rules, or use advanced combinations of both experimentation and targeting. These different options and the steps to follow are detailed in this section .
- Use the Languages section to create content in multiple languages within your journey action. To do so, click the Add languages button and select the desired Language settings . Detailed information on how to set up and use multilingual capabilities are available in this section .

Additional settings are available depending on the selected communication channel. Expand the sections below for more information.

Apply capping rules
(Email, Push, SMS)
In the **Business rules** drop-down list, select a rule set to apply capping rules to your journey action.

Leveraging channel rule sets allows you to set frequency capping by communication type to prevent overloading customers with similar messages.

[Learn how to work with rule sets](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets)

Track engagement
(Email, SMS).
Use the **Action tracking** section to track how your recipients react to your email or SMS deliveries.

Tracking results are accessible from the journey report once the journey has been executed.

[Learn more about journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja)

Enable Rapid delivery mode
(Push).
Rapid delivery mode is a Journey Optimizer add-on that allows very fast push message sending in large volumes though campaigns.

Rapid delivery is used when delay in message delivery is business-critical, when you want to send an urgent push alert on mobile phones, for example a breaking news to users who have installed your news channel app.

Learn how to enable Rapid delivery mode for Push notifications [on this page](/en/docs/journey-optimizer/using/channels/push/create-push#rapid-delivery).

For more information on performances when using Rapid delivery mode, refer to [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html#_blank).

Assign priority scores
(Web, In-app, Code-based)
In the **Conflict management** section, you can assign a priority score to the journey action, allowing you to prioritize an inbound action when there are multiple journey actions or campaigns using the same channel configuration.

By default, the priority score for the action is inherited from the overall priority score for the journey.

[Learn how to assign priority scores to channel actions](/en/docs/journey-optimizer/using/conflict-prioritization/priority-scores#priority-action)

Set additional delivery rules
(Content cards)
For content card journeys, you can enable additional delivery rules to choose the event(s) and criteria which trigger your message.

[Learn how to create content cards](/en/docs/journey-optimizer/using/channels/content-card/create-content-card)

Define triggers
(In-app)
For in-app messages, you can use the **Edit triggers** button to choose the event(s) and criteria which trigger your message.

[Learn how to create an In-app message](/en/docs/journey-optimizer/using/channels/in-app/create-in-app)

## Add multiple inbound actions multi-action

To simplify your journey orchestration, you can define several inbound actions inside a single journey action.

NOTE
This capacity is only available for inbound channels. Currently outbound channels such as Email are not supported.
This capacity enables you to deliver various Code-based experiences, In-app messages, Content Cards or Web actions to different locations at the same time, without the need to create multiple journey actions. It makes the deployment of your journey easier and allows for smoother reporting, with all the data consolidated into one single journey.

For example, you can send a code-based experience to multiple endpoints with slightly different contents. To do this, create multiple code-based actions within the same journey action, each with a different endpoint configuration.

To define several inbound actions in a single journey action node, follow the steps below.

- Start your journey with an Event or a Read Audience activity.
- From the Actions section of the palette, drag and drop an Action activity into the canvas.
- Select Multi action as the action type.
- Add a label if needed and select Configure action . {width="60%"}
- You are directed to the Actions tab of the journey action configuration screen. {width="70%"}
- Select an inbound action ( Code-based experience , In-app message , Content Card or Web ) from the Actions section.
- Select the channel configuration and define a specific content for that action.
- Use the Add action button to select another inbound action from the drop-down list. {width="80%"}
- Proceed similarly to add more actions. You can add up to 10 inbound actions in a journey action group.

Once the journey is [live](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey), all actions are activated simultaneously.

## Update a live content update-live-content

You can update the content of a built-in channel action in a live journey.

Any changes made to the content are not reflected in the journey until you save the action’s properties. [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities#advanced-parameters)

To do this, open your live journey, select the channel activity and click **Edit content**.

However, you cannot change the attributes used in personalization, whether they are profile attributes or contextual data (from event or journey properties).

- If you modified contextual data, the following error message will be displayed: ERR_AUTHORING_JOURNEYVERSION_201
- If you modified profile attributes, the following error message will be displayed: ERR_AUTHORING_JOURNEYVERSION_202

Note that for the In-app activity, any changes can be made to the content while the journey is live, but In-app triggers cannot be modified.

## Send with custom actions recommendation

Instead of using the built-in message capabilities, you can use custom actions to configure connection of a third-party system to send messages or API calls.

- If you are using a third-party system to send your messages, you can create a custom action. Learn more
- If you are working with Adobe Campaign, refer to these sections: Journey Optimizer and Campaign v7/v8 Journey Optimizer and Campaign Standard

recommendation-more-help
