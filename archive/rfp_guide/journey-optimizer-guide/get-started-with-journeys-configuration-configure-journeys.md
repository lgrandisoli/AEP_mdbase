---
title: "Get started with journeys configuration configure-journeys"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/about-data-sources-events-actions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:26.443589+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with journeys configuration configure-journeys

Last update: May 8, 2026
- Topics:
- [Application Settings](#)

CREATED FOR:

- Intermediate
- Admin

To send messages with journeys, it is necessary to configure **Data Sources**, **Events** and **Actions**. Data Sources enable you to establish a connection to a system to retrieve additional information that will be utilized in your journeys, such as in conditions. Events allow for the triggering of your journeys when an event is received. Custom Actions facilitate the connection to a third-party system to send your messages. If you are using Journey Optimizer’s built-in messaging capabilities, configuring an action is not required.

You can also configure connections to external systems via custom data sources and custom actions. This allows you, for example, to enrich your journeys with data coming from an external reservation system, or send messages using a third-party system such as Epsilon or Facebook. Learn how to [integrate Journey Optimizer with external systems](/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems).

## Data Sources data-sources

The Data Source configuration allows you to define a connection to a system to retrieve additional information that will be used in your journeys. [Learn more](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources)

## Events events

Events allow you to trigger your journeys unitarily to send messages, in real-time, to the individual flowing into the journey.

In the event configuration, you configure the events expected in the journeys. The incoming events’ data is normalized following Adobe Experience Data Model (XDM). Events come from Streaming Ingestion APIs for authenticated and unauthenticated events (such as Adobe Mobile SDK events). [Learn more](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events)

## Actions actions

Journey Optimizer message capabilities are built-in: you only need to add a channel action activity to your journey. If you are using a third-party system to send your messages, you can create a custom action. [Learn more](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action)

## Browse through Adobe Experience Platform fields friendly-names-display

When defining [event payload](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating#define-the-payload-fields), [field group payload](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/configure-data-sources#define-field-groups) and selecting fields in the [expression editor](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced), the display name is displayed in addition to the field name. This information is retrieved from the schema definition in the Experience Data Model.

If descriptors such as “xdm:alternateDisplayInfo” are provided while setting up schemas, the user-friendly names will replace display names. It is especially useful when working with “eVars” and generic fields. You can configure friendly name descriptors via an API call. For more information, see the [Schema Registry developer guide](/en/docs/experience-platform/xdm/api/getting-started#_blank).

If a friendly name is available, then the field will be displayed as <friendly-name>(<name>). If no friendly name is available, the display name will appear, for example <display-name>(<name>). If none of them are defined, only the technical name of the field will be displayed <name>.

NOTE
Friendly names are not retrieved when you select fields from a union of schemas.
recommendation-more-help
