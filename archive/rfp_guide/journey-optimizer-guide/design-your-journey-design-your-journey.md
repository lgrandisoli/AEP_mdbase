---
title: "Design your journey design-your-journey"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:52.887343+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Design your journey design-your-journey

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

Adobe Journey Optimizer includes an omnichannel orchestration canvas which allows marketers to harmonize marketing outreach with one-to-one customer engagement. The user interface allows you to easily drag and drop activities from the palette into the canvas to build your journey. Note that you can also double-click on an activity to add it in the canvas, at the next available step.

Events, orchestration and action activities have a specific role and place in the process. The activities are sequenced: when an activity is finished, the flow continues and processes the next activity, and so on.

## Get started with journey design gs-journey-design

The **palette** is on the left-hand side of the screen. All available activities are sorted into several categories: [Events](#jo-event), [Orchestration](#jo-orch) and [Actions](#jo-actions). You can expand/collapse the different categories by clicking on their name. To use an activity in your journey, drag and drop it from the palette into your canvas.

When starting a new journey, elements that cannot be dropped in the canvas as the first step are hidden. This concerns all actions, the condition activity, the wait and the reaction.

The **Filter items** icon in the top left corner allows you to display the following filters:

- Show only available items : hide or display unavailable elements in the palette, for example the events that use a different namespace than the ones used in your journey. By default, unavailable items are hidden. If you choose to display them, they will appear greyed out.
- Show only recent items : this filter allows you to only display the last five events and actions used, in addition to out-of-the-box ones. This is specific to each user. By default, all items are displayed.

You can also use the **Search** field. Only events and actions are filtered.

The **canvas** is the central zone in the journey designer. It is in this zone that you can drop your activities and configure them. Click on an activity in the canvas to configure it. This opens the activity configuration pane on the right-hand side.

The **toolbar**, located in the top right corner of the canvas, allows you to show/hide the grid, zoom in/out and download a screenshot of the canvas. See this [section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#timeout_and_error).

{align="left" width="70%"}

The **activity configuration pane** appears when you click on an activity in the palette. Fill in the required fields. Click the **Delete** icon to delete the activity. Click **Cancel** to cancel the modifications or **Ok** to confirm. To delete activities, you can also select one activity (or several) and press the backspace key. Pressing the escape key will close the activity configuration pane.

By default, read-only fields are hidden. To show read-only fields, click the **Show read-only fields** icon at the top left of the activity configuration pane. This setting applies to all activities in all journeys.

Depending on the journey’s status, you can perform different actions on your journey using the buttons available in the top right corner: **Publish**, **Duplicate**, **Delete**, **Test mode**, **Manage access**, **Alerts**. These buttons appear when no activity is selected. Some buttons will appear contextually. The test mode log button appears when test mode is activated.

## Start your journey start-your-journey

When you design your journey, the first question you want to ask is how profiles will enter the journey.

There are two possibilities:

- Start with an event : when a journey is set to listen to events, individuals enter the journey unitarily in real-time. Messages included in your journey are sent to the person currently flowing into the journey. Learn more about events
- Start with a Read Audience : you can set your journey to listen to Adobe Experience Platform audiences. In this case, all individuals belonging to the specified audience enter the journey. Messages included in your journey are sent to the individuals belonging to the audience. Learn more about read audience . For more information on how to generate and target audiences in Journey Optimizer, refer to this section .

## Define the next steps define-next-steps

After your first event or Read Audiences, you can combine the different activities to build your multi-step cross-channel scenarios. Choose, from the palette, the steps you need.

### Events jo-event

Events are what trigger a personalized journey, such as an online purchase. Once someone enters a journey, they move through as an individual, and no two individuals are moving along at the same rate or along the same path.

When you start your journey with an event, the journey is triggered when the event is received. Each person in the journey then follows, individually, the next steps defined in your journey.

You can add **several events** in your journey, as long as they use the same namespace. Events are configured beforehand. [Learn more about journey events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities#event-activities)

You can also add a **Reaction** event after a message to react to tracking data related to the message. This allows you, for example, to send another message if the individual opened the previous message or clicked inside it. [Learn more about reaction events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events).

Use **Audience Qualification** event activity to make individuals enter or move forward in a journey based on Adobe Experience Platform audience entrances and exits. You can make all new silver customers enter a journey and send personalized messages. Learn more in this [section](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events).

### Orchestration jo-orch

Orchestration activities are different conditions that help determine the next step in the journey.

From the orchestration activities, use the **Read Audience** activity to set your journey to listen to an Adobe Experience Platform audience. [Learn more about the Read Audience activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience).

Use **Journey Fragments** to insert reusable sets of pre-built journey nodes directly into the canvas. Fragments help teams stay consistent and move faster by avoiding rebuilding the same logic — such as eligibility checks, channel routing, or welcome sequences — from scratch. [Learn more about Journey Fragments](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-fragments).

The other activities allow you to add conditions to your journey to define several paths, set a waiting time before executing the next activity, or end your journey. [Learn more about orchestration activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities#orchestration-activities).

### Actions jo-actions

Actions are what you want to happen as result of some kind of trigger, like sending a message. It is the piece of journey that the customer experiences. This could be an email, SMS or Push message, or a third-party action, such as a Slack message.

The channel action activities allows you to include a message designed in Journey Optimizer. [Learn more about the channel action activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action)

From the action activities, use custom actions to send messages with third-party systems. [Learn more about custom actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities#action-activities).

## Add alternative paths paths

You can define a fallback action in case of an error or timeout for the following journey activities: **Condition** and **Action**.

To add a fallback action for an activity, select the **Add an alternative path in case of a timeout or an error** box in the activity properties: another path is added after the activity. The timeout duration is defined by Admin users in the [journey properties](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties). For example, if an email takes too long to be sent or is in error, you can decide to send a push notification.

Various activities (event, action, wait) allow you to add several paths after them. To do this, place your cursor on the activity and click the “+” symbol. Only event and wait activities can be set in parallel. If several events are set in parallel, the chosen path will be the one of the first event happening.

When listening to an event, we recommend that you do not wait for the event indefinitely. It is not mandatory, just a best practice. If you want to listen to one or several events only during a certain time, you will place one or several events and a wait activity in parallel. See [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/general-events#events-specific-time).

To delete the path, place your cursor on it and click the **Delete path** icon.

In the canvas, when two activities are disconnected, a warning is displayed. Place your cursor on the warning icon to display the error message. To fix the issue, simply move the disconnected activity and connect it to the previous activity.

## Copy and paste activities copy-paste

You can copy one or several activities of a journey and paste them either in the same journey or a different one. This allows you to save time if you want to reuse numerous activities that have been already configured in a previous journey.

**Important notes**

- You can copy/paste across different tabs and browsers. You can only copy/paste activities within the same instance.
- You can not copy/paste an event if the destination journey has an event that uses a different namespace.
- Pasted activities may reference data that do not exist in the destination journey, for example if you copy/paste across different sandboxes. Always check for errors and make the required adjustments.
- Be aware that you cannot undo an action. To delete pasted activities, you will need to select and delete them. Therefore, make sure you only select the activities you need before copying them.
- You can copy activities from any journey, even ones that are in read-only.
- You can select any activity, even ones that are not linked. Linked activities will stay linked after being pasted.

Here are the steps to copy/paste activities:

- Open a journey.
- Select the activities you want to copy by moving your mouse while clicking. You can also click on each activity while pressing the **Ctrl/Command** key. Use **Ctrl/Command + A** if you want to select all activities.
- Press **Ctrl/Command + C**.If you want to only copy one activity, you can click on it and use the **Copy** icon in the top left of the activity configuration pane.
- In any journey, press **Ctrl/Command + V** to paste the activities without linking them to an existing node. Pasted activities are placed in the same order. After being pasted, activities stay selected so you can easily move them. You can also place the cursor on an empty place holder and hit **Ctrl/Command + V**. Pasted activities will be linked to the node.

recommendation-more-help
