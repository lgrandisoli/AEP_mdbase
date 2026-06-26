---
title: "About experienceevent schemas for Journey Optimizer events about-experienceevent-schemas"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/events-journeys/experience-event-schema"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:53.778256+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# About experienceevent schemas for Journey Optimizer events about-experienceevent-schemas

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Events](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

Journey Optimizer events are XDM Experience Events that are sent to Adobe Experience Platform via Streaming Ingestion.

As such, an important prerequisite for setting up events for Journey Optimizer is that you are familiar with Adobe Experience Platform’s Experience Data Model (or XDM) and how to compose XDM Experience Event schemas, as well as how to stream XDM-formatted data to Adobe Experience Platform.

CAUTION
Starting July 8, 2025, new customer organizations cannot create expressions using experience event attributes in journey conditions. Starting April 1, 2026, organizations that have not accessed experience events via journey expressions in the last 90 days will no longer have access to this capability. Alternative approaches and best practices are listed in
Experience event lookup in journeys
.
Accessing context from the starting event of a journey is not impacted.
## Schema requirements for Journey Optimizer Events schema-requirements

The first step in setting up an event for Journey Optimizer is to ensure that you have an XDM schema defined to represent the event, and a dataset created to record instances of the event on Adobe Experience Platform. Having a dataset for your events is not strictly necessary, but sending the events to a specific dataset will allow you to maintain users’ event history for future reference and analysis, so it is always a good idea. If you do not already have a suitable schema and dataset for your event, both of those tasks can be done in Adobe Experience Platform web interface.

Any XDM schema that will be used for Journey Optimizer events should meet the following requirements:

- The schema must be of the XDM ExperienceEvent class.
- For system-generated events, the schema must include the Orchestration eventID field group. Journey Optimizer uses this field to identify events used in journeys.
- Declare an identity field for identifying individual profiles in the event. If no identity is specified, an identity map can be used. This is not recommended.
- If you would like this data to be available for profile, mark the schema and dataset for profile. Learn more
- Feel free to include data fields to capture any other context data you want to include with the event, such as information about the user, the device from which the event was generated, location, or any other meaningful circumstances related to the event.

recommendation-more-help
