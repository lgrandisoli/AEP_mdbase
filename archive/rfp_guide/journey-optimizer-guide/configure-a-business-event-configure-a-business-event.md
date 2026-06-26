---
title: "Configure a business event configure-a-business-event"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating-business"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:43.854813+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Configure a business event configure-a-business-event

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Events](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

Unlike unitary events, business events are not linked to a specific profile. The event ID type is always rule-based. Read more on business events in [this section](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).

Read audience based journeys can be triggered in one-shot, by a scheduler on a regular basis or by a business event, when the event occurs.

Business events can be “a product is back in stock”, “the stock price of a company reaches a certain value”, etc.

NOTE
You can also watch the business event use case
tutorial
. Note that the schema does not need to be enabled for profile.
## Important notes important-notes

- Only time series schemas are available. Experience Events, Decision Events and Journey Step Events schemas are not available.
- The event schema must contain a non-people based primary identity. The following fields must be selected when defining the event: _id and timestamp
- Business events can only be dropped as the first step of a journey.
- When dropping a business event as the first step of a journey, the scheduler type of the journey will be “business event”.
- Only a read audience activity can be dropped after a business event. It is automatically added as the next step.
- To allow multiple business event executions, activate the corresponding option in the **Execution** section of the journey properties.
- After a business event is triggered, there will be a delay to have the audience exported from 15 minutes to up to one hour.
- When testing a business event, you have to pass the event parameters and the identifier of the test profile that will enter the journey in test. Also, when testing a business event based journey, you can only trigger single profile entrance. See [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey#test-business). In test mode, there is no “Code view” mode available.
- What happens to individuals that are currently in the journey if a new business event arrives? It behaves the same way as when individuals are still in a recurring journey when a new recurrence happens. Their path is ended. As a result, marketers must pay attention to avoid building too long journeys if they expect frequent business events.
- Business events cannot be used in conjunction with unitary events or audience qualification activities.

## Multiple business events multiple-business-events

Here are a few important notes that apply when multiple business events are received in a row.

**What is the behavior when receiving a business event while the journey is processing?**

Business events follow reentrance rules in the same way as for unitary events. If a journey allows reentrance, the next business event will be processed.

**What are the guardrails to avoid over-loading materialized audiences?**

In the case of on-shot business events, for a given journey, data pushed by the first event job is reused during a 1-hour time window. For scheduled journeys, there is no guardrail. Learn more about audiences in the [Adobe Experience Platform Segmentation Service documentation](/en/docs/experience-platform/segmentation/home#_blank).

## Get started with business events gs-business-events

Here are the first steps to configure a business event:

- In the ADMINISTRATION menu section, select Configurations . In the Events section, click Manage . The list of events is displayed.
- Click Create Event to create a new event. The event configuration pane opens on the right side of the screen.
- Enter the name of your event. You can also add a description. note NOTE Only alphanumeric characters and underscores are allowed. The maximum length is 30 characters.
- In the Type field, choose Business .
- The number of journeys that use this event is displayed in the Used in field. You can click the View journeys icon to display the list of journeys using this event.
- Define the schema and payload fields: this is where you select the event information (or payload) journeys expects to receive. You will use this information later in your journey. See this section . Only time series schemas are available. Experience Events , Decision Events and Journey Step Events schemas are not available. The event schema must contain a non-people based primary identity. The following fields must be selected when defining the event: _id and timestamp
- Click inside the Event ID condition field. Use the simple expression editor to define the condition which is used by the system to identify the events that trigger your journey. In our example, we wrote a condition based on the product’s id. This means that whenever the system receives an event that matches this condition, it will pass it to journeys. note NOTE In the simple expression editor, not all operators are available, they depend on the data type. For example, for a string type of field, you can use “contains” or “equal to”.
- Click Save . The event is now configured and ready to be dropped into a journey. Additional configuration steps are required to receive events. Learn more on this page .

## Define the payload fields define-the-payload-fields

The payload definition allows you to choose the information the system expects to receive from the event in your journey and the key to identify which person is associated to the event. The payload is based on the Experience Cloud XDM field definition. For more information on XDM, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/xdm/home#_blank).

- Select an XDM schema from the list and click on the Fields field or on the Edit icon. All the fields defined in the schema are displayed. The list of fields varies from one schema to another. You can search for a specific field or use the filters to display all nodes and fields or only the selected fields. According to the schema definition, some fields may be mandatory and pre-selected. You cannot unselect them. All fields that are mandatory for the event to be received properly by journeys are selected by default. note NOTE Make sure that the following fields are selected: _id and timestamp
- Select the fields that you expect to receive from the event. These are the fields which the business user will leverage in the journey.
- When you are done selecting the needed fields, click Save or press Enter . The number of selected fields appears in Fields .

## Preview the payload preview-the-payload

Use the payload preview to validate the payload definition.

- Click the View Payload icon to preview the payload expected by the system. You can notice that the fields selected are displayed.
- Check the preview to validate the payload definition.
- Then, you can share the payload preview with to the person responsible for the event sending. This payload can help them design the setup of an event pushing to Journey Optimizer. See this page .

recommendation-more-help
