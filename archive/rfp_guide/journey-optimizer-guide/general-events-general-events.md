---
title: "General events general-events"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/general-events"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:49.892553+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# General events general-events

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Events](#)

CREATED FOR:

- Intermediate
- User

Events allow you to trigger your journeys unitarily to send messages, in real-time, to the individual flowing into the journey.

For this type of event, you can only add a label and a description. The rest of the configuration cannot be edited. It was performed by the technical user. See [this page](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).

Learn more about event throughput and journey processing rates in [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management#journey-processing-rate).

When you drop a business event, it automatically adds a **Read Audience** activity. For more information on business events, refer to [this section](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events)

## Listening to events during a specific time events-specific-time

An event activity positioned in the journey listens to events indefinitely. To listen to an event only during a certain time, you must configure a timeout for the event.

The journey will then listen to the event during the time specified in the timeout. If an event is received during that period, the person will flow in the event path. If not, the customer will either flow into the timeout path if it is defined, or will continue that journey.

If no timeout path is defined, the timeout setting will act as a wait activity, making the profile wait for a period of time, which could be stopped if an event happens before the end of that wait. If you want profiles to be excluded from that journey after timeout, you will have to set a timeout path.

To configure a timeout for an event, follow these steps:

- Activate the Define the event timeout option from the event properties.
- Specify the amount of time the journey will wait for the event. The maximum duration is 90 days .
- When no event is received within the specified timeout, best practice is to send the individuals into a timeout path. For this, enable the Set a timeout path option. In that case, the journey continues for the individual once the timeout is reached. We recommend that you always enable the Set a timeout path option.

In this example, the journey sends a first welcome email to a customer after he/she enters the lobby. It then sends a meal discount email only if the customer enters the restaurant within the next day. We therefore configured the restaurant event with a 1-day timeout:

- If the restaurant event is received less than 1 day after the welcome email, the meal discount email is sent.
- If no restaurant event is received within the next day, the person flows through the timeout path.

Note that if you want to configure a timeout on multiple events positioned after a **Wait** activity, you need to configure the timeout on one of these events only.

The defined timeout applies to all the events positioned after the **Wait** activity:

- If one event is received within the timeout duration, the individual flows into the received event’s path.
- If no event is received within the timeout duration, the individual flows into the timeout branch of the event where the timeout has been defined.

recommendation-more-help
