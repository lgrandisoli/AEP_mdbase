---
title: "Work with journey events about-events"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:52.705943+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with journey events about-events

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Events](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

Use events to trigger journeys individually, delivering real-time messages to each user as they enter the journey.

IMPORTANT
For event requirements and limitations (streaming, Query Service, batch ingestion), see
Journey guardrails - Events
.
In the event configuration, you configure the events expected in the journeys. The incoming events’ data is normalized following Adobe Experience Data Model (XDM). Events come from Streaming Ingestion APIs for authenticated and unauthenticated events (such as Adobe Mobile SDK events). You can use multiple events (in different steps of a journey) and several journeys can use the same event.

Event configuration is **mandatory** and must be performed by a Data engineer.

You can configure three types of events: **Unitary events**, **Business events**, and **Audience qualification events**.

➡️ [Discover this feature in video](#video)

## Unitary events unitary-events

**Unitary** events are linked to a person. They relate to the behavior of a person (for example, a person bought a product, visited a shop, exited a website, etc.) or something happening linked to a person (for example, a person reached 10,000 loyalty points). This is what Journey Optimizer will listen to in journeys to orchestrate the best next actions. Unitary events can be rule-based or system generated. To learn how to create a unitary event, refer to this [page](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating).

Unitary journeys (starting with an event or an audience qualification) include a guardrail that prevents journeys from being erroneously triggered multiple times for the same event. Profile reentrance is temporally blocked by default for 5 minutes. For instance, if an event triggers a journey at 12:01 for a specific profile and another one arrives at 12:03 (whether it is the same event or a different one triggering the same journey) that journey will not start again for this profile.

## Business events business-events

**Business** events are not linked to a specific profile. For example, it can be a news alert, a sports update, a flight change or cancelation, an inventory update, weather events, etc. While these events are not specific to a profile, they may be of interest to any number of profiles: individuals subscribed to particular news topics, passengers on a flight, shoppers interested in an out-of-stock product, etc. Business events are always rule-based. When you drop a business event in a journey, it automatically adds a **Read audience** activity right after. Learn how to create a business event [on this page](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating-business).

## Audience qualification events audience-qualification-events

An **audience qualification** event is triggered when a profile enters or exits an audience. For example, a customer crossing a loyalty spend threshold enters the Gold tier audience — that qualification triggers the journey for that profile in real time (for streaming audiences) or at the next batch evaluation. Unlike unitary events, audience qualification lets you build complex triggering logic using the full power of audience definitions, without requiring implementation changes to send a new event. Learn more on [audience qualification events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events).

NOTE
Audience qualification events are not configured in
Administration > Events
— they are selected directly on the journey canvas as the first step of a journey.
## Unitary vs business events at a glance event-comparison

Unitary event
Business event
Linked to a profile?
Yes — triggered by a specific individual’s action.
No — triggered by an external occurrence not tied to one person.
Entry behavior
One profile enters the journey in real time.
Multiple profiles enter via an automatic Read Audience step.
Typical use cases
Purchase confirmation, form submission, app login, loyalty milestone.
Flight cancellation, stock replenishment alert, breaking news, weather event.
How it starts the journey
Event-based entry — no audience needed.
Business event + automatic Read Audience (added by Journey Optimizer).
Multiple per journey?
Yes — you can listen to several unitary events across journey steps.
No — only one business event per journey, placed at the start.
Event ID type
Rule-based or system-generated.
Always rule-based.
NOTE
A journey can contain only
one
business event, which must be the first activity. Journey Optimizer automatically adds a
Read Audience
activity after it to define which profiles receive the journey triggered by that event.
## Event ID type event-id-type

For **business** events, the event ID type is always rule-based.

For **unitary** events, there are two types of event ID:

- Rule-based events: this type of event does not generate an eventID. Using the simple expression editor, you simply define a rule which will be used by the system to identify the relevant events that will trigger your journeys. This rule can be based on any field available in the event payload, for example the profile’s location or the number of items added to the profile’s cart. note caution CAUTION A capping rule is defined for rule-based events. It limits the number of qualified events that a journey can process to 5,000 per seconds for a given Organization. It corresponds to Journey Optimizer SLAs. Refer to your Journey Optimizer licensing and Journey Optimizer Product Description .
- System-generated events: these events require an eventID. This eventID field is automatically generated when creating the event. The system pushing the event should not generate an ID, it should pass the one available in the payload preview.

NOTE
Journey Optimizer requires events to be streamed to Data Collection Core Service (DCCS) to be able to trigger a journey. Events ingested in batch, events inserted via
Query Service
, or events from internal Journey Optimizer datasets (Message Feedback, Email Tracking, etc.) cannot be used to trigger a journey. For use cases where you cannot get streamed events, please build an audience based on those events and use the
Read Audience
activity instead. Audience qualification can technically be used, but can cause downstream challenges based on the actions used. This data does not necessarily need to go to the Real-Time Profile. If you would like to use the events for segmentation, we recommend you enable the dataset for profile.
## How to choose choose-event-type

Use the following criteria to select the right event type for your journey — the key question is: **are you triggering an action for one specific person, or broadcasting to many profiles?** [Learn more on journey types](/en/docs/journey-optimizer/using/orchestrate-journeys/journey#journey-types).

- Choose a unitary event when the trigger is tied to a specific individual — for example, a purchase, a form submission, or a loyalty milestone. Unitary events require a person-based primary identity in the schema and start the journey immediately for that profile. Learn how to configure a unitary event .
- Choose a business event when the trigger is a global occurrence — for example, a product restock, a price drop, or a flight cancellation — and you want to broadcast to a set of profiles related to that signal. Business events must be the first step in the journey and automatically target profiles via a Read Audience activity. They require a time-series schema with a non-people primary identity and the _id and timestamp fields. Plan for an audience export delay of 15 minutes to up to one hour. Learn how to configure a business event .
- Choose an audience qualification event when the trigger is a profile entering or exiting an audience, and you need more complex segmentation logic than a single event can provide — for example, re-engaging lapsed customers who just met a spend threshold, or triggering an offboarding flow when a VIP member drops out of the loyalty tier. Learn more on audience qualification events .

CAUTION
Business events cannot be used in the same journey as unitary events or audience qualification activities.
## Data cycle data-cycle

Events are POST API calls. Events are sent to Adobe Experience Platform through Streaming Ingestion APIs. The URL destination of events sent through transactional messaging APIs is called an “inlet”. The payload of events follows XDM formatting.

The payload contains information required by Streaming Ingestion APIs to work (in the header) and the information required by Journey Optimizer to work and information to be used in journeys (in the body, for example, the amount of an abandoned cart). There are two modes for the streaming ingestion, authenticated and unauthenticated. For details on Streaming Ingestion APIs, refer to [this link](/en/docs/experience-platform/xdm/api/getting-started#_blank).

After arriving through Streaming Ingestion APIs, events flow into an internal service called Pipeline and then in Adobe Experience Platform. If the event schema has the Real-time Customer Profile Service flag enabled and a dataset ID that also has the Real-time Customer Profile flag, it flows into the Real-time Customer Profile Service.

For system-generated events, the Pipeline filters events which have a payload containing Journey Optimizer eventIDs (see the event creation process below) provided by Journey Optimizer and contained in event payload. For rule-based events, the system identifies the event using the eventID condition. These events are listened by Journey Optimizer and the corresponding journey is triggered.

## About Journey event throughput event-thoughput

Adobe Journey Optimizer supports a peak volume of 5,000 journey events per second at an organization level, across all sandboxes. This quota applies to all events that are used in active journeys, which includes **Live**, **Dry run**, **Closed** and **Paused** journeys. When this quota is reached, new events get queued with a processing rate of 5,000 per second. The maximum time an event can spend in the queue is **24 hours**.

For more details on journey processing rates and how different journey types impact throughput, refer to [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management#journey-processing-rate).

The following types of events are counted toward the 5,000 TPS quota:

- External Unitary Events : Includes both rule-based and system-generated events. If the same raw event qualifies for multiple rule definitions, each qualified rule counts as a separate event. More details below.
- Audience Qualification Events : If the same streaming audience is used in multiple journeys, each usage counts separately. For instance, using the same audience in an audience qualification activity in two journeys results in two counted events.
- Reaction Events : Events triggered by profile reactions (email opened, email clicked, etc.) within a journey.
- Business Events : Events not tied to a specific profile, but to a business-related event.
- Analytics Events : If the integration with Adobe Analytics to trigger journeys has been enabled, these events are also included.
- Resume Events : Technical event triggered when a profile resumes from a paused journey. Learn more about resuming paused journeys .
- Wait Node Completion Events : When a profile exits a wait node, a technical event is generated to resume the journey.

NOTE
Except for wait and resume events, all other event types also count toward the quota when used in journeys based on read audiences.
### About raw events qualifying for multiple rule definitions

Same raw event can qualify for multiple rule definitions in journeys. When an event is configured in the **Administration** section, for the same event schema, multiple event rules can be defined. Let’s say for example that we have a purchase event which has fields city and purchaseValue. Let’s consider the following scenarios:

- An event E1 named newYorkPurchases is created with a rule definition saying that city=='New York' . This event might be used in 10 journeys but will still be counted only as 1 event, when it will come.
- Now let’s say that an event E2 named highValuePurchases with purchaseValue > 1000 as a rule definition is also created, on the same event schema than E1 . In this case, the same incoming event will be evaluated against two rules: newYorkPurchases and highValuePurchases . Now it may happen that a newYork purchase is also a high value purchase. In this case Journey Optimizer will create two events, E1 and E2 , out of the same incoming event, which will make this single incoming event count as two events. Note that these events start getting counted when they are used in an active journey, including Live , Dry run , Closed and Paused journey.

## Updating and deleting an event update-event

To avoid breaking existing journeys, when you edit an event used in a **Draft**, **Live** or **Closed** journey, you can only change the name, the description or add payload fields.

Any event used in **Live**, **Draft** or **Closed** journeys cannot be deleted. To delete a used event, you must stop journeys using it, and/or remove it from the Draft journeys where it are used. You can check the **Used in** field. It displays the number of journeys that use that particular event. You can click the **View journeys** button to display the list of corresponding journeys.

## How-to videos video

Learn how to configure an event, specify the streaming endpoint and the payload for an event.

https://video.tv.adobe.com/v/336253?quality=12&learn=on
Understand the applicable use cases for business events. Learn how to build a journey using a business event and which best practices to apply.

https://video.tv.adobe.com/v/334234?quality=12&learn=on
recommendation-more-help
