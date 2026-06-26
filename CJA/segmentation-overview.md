---
title: "Segmentation overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/segments/seg-overview"
category: "overview"
topic: "analytics-platform/using/cja-components/segments"
created_at: "2026-06-02T19:05:26.531462+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Segmentation overview

Last update: May 13, 2026
- Topics:
- [Filters](#)
- [Segments](#)

CREATED FOR:

- User

Customer Journey Analytics lets you build, manage, share, and apply powerful, focused audience segments to your reports. Segments let you identify subsets of persons, sessions or events based on characteristics or interactions. Segments are designed as codified audience insights that you can build for your specific needs, and then verify, edit, and share with other team members.

Segments can be based on:

- attributes (browser type, device, number of visits, country, gender),
- interactions (campaigns, keyword search, search engine),
- exits and entries (persons from Facebook, a defined landing page, referring domain, geofence event),
- custom variables (form field, defined categories, customer ID),
- and other criteria.

See [Create segments](/en/docs/analytics-platform/using/cja-components/segments/seg-create) for the various options available to create segments. You then build, modify, and save the definition of a segment in the [Segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder). Alternatively, you can create quick segments using the [Quick segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-quick). And you can also generate segments from visualizations in Workspace, for example using the [Fallout](/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/configuring-fallout#context-menu) visualization.

You use the [Segment manager](/en/docs/analytics-platform/using/cja-components/segments/seg-manage) to manage segments.

## Plan segments

Especially, as an administrator, the proper planning of segments improves the chances that the segments are used. Consider the following when planning segments:

- Audience : Who will use your segments? Ensure you provide a good segment description so the audience understands: What is this segment useful for? When should I use this segment?
- Scope : Which Segment container best represents the data you are after? Use the smallest container possible.
- Components : Decide which components to include in the segment definition, and against which values the conditions should validate.
- Process : Consider an approval process for your segments. There is no approval workflow in Customer Journey Analytics but you can still organize a process to determine whether you approve a segment or not.
- Modularity : Define segments with modularity in mind. The users of your segments should be able to easily stack segments to create powerful new segments.

## Segment types

You can create three types of segments:

### Quick segments

Quick segments allow you to explore data easily within a given Workspace project, without the need of creating a segment in the [Segment Builder](/en/docs/analytics-platform/using/cja-components/segments/seg-create). You define your segment within the Workspace interface directly. See [Quick segments](/en/docs/analytics-platform/using/cja-components/segments/seg-quick) for more information.

### Regular segments

Regular segments let you identify data (persons, sessions, events) based on one or more conditions. If you have more than one condition, you use logical operators like And and Or to define the segment further. You can use containers to group conditions and build more complex segments. See [Segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder) for more information.

### Sequential segments

IMPORTANT
You must have the
Select
package to create cross-channel sequential segments. Contact your administrator if you’re unsure which Customer Journey Analytics package you have.
Sequential segments let you identify data (persons, sessions, events) based on navigation (page views across your site, interactions with scenes in your mobile app, or using a menu on a set-top box). Sequential segments help you identify, for example, what a person likes and what a person avoids. You use the Then logical operator to define a sequential segment. See [Sequential segments](/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build) for more information.

## Segment containers containers

Segments are based on a Person-, Session-, and Event-level hierarchy using a nested container model. The nested containers allow you to define conditions between and within the containers.

Person
Session
Event
NOTE
For Adobe Analytics users:
- The **Person** container is known in Adobe Analytics as the **Visitor** container.
- The **Session** container is known in Adobe Analytics as the **Visit** container.
- The **Event** container is known in Adobe Analytics as the **Hit** container.

A segment sets conditions to segment persons, sessions or events based on conditions. For example, conditions to segment persons are based on person characteristics and navigation traits. To further break down the data, you can segment on specific sessions, page view events, screen taps, menu choices on a set-top box, and more. You can also segment on attributes that you have ingested from a CRM or loyalty system. The [Segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder) provides a simple interface to build these subsets and apply conditions in nested, hierarchical Person, Session, or Event containers.

The container architecture employed in the [Segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder) defines Person as the outermost container. This container contains overarching data specific for the person across sessions and events like page views, mobile application screens, or menu screens on a set-top box. A nested Session container lets you set rules to break down the person’s data based on sessions. A nested Event container lets you break down person information based on individual interactions. Each container lets you report across a person’s history, interactions broken down by sessions, or break down individual events.

### Person container

The Person container includes every session and every event for the persons that qualify for the condition specified in the container. When you define a segment with a simple condition like Page Name equals Checkout, then the Person container resolves to:

- All persons that have visited the page with name Checkout.
- All sessions for these persons.
- All event data for these persons.

As the most broadly defined container, reports generated at the Person container level return events and sessions for all persons that qualify for the segment. The Person container is the most susceptible to change based on defined date ranges.Person containers can include values based on a person’s overall history:

- Days before the first purchase.
- Original entry page or mobile app home screen.
- Original referring domains.

### Session container

The Session container lets you identify page interactions or mobile app interactions, campaigns, or conversions for a specific session. The Session container is the most commonly used container because it captures behaviors for the entire session once the rule is met. The Session container also lets you define which sessions you want to include or exclude in building and applying a segment. When you define a segment with a simple condition like Page Name equals Checkout, then the Session container resolves to:

- All sessions where a page with name Checkout is visited.
- All event data for those sessions.

The session container can help you answer the following questions:

- How many sessions involved both web and call center data sources?
- Which pages contributed to a successful conversion to a sale?

Session containers include values based on events per session:

- Session type.
- Entry page.
- Return frequency.
- Participation metrics.
- Linearly allocated metrics.

Data views in Customer Journey Analytics let you determine how long a session lasts, but also when a new session should be created. For example, you can define a new mobile app session based on every time a user launches your mobile app. See [Session settings](/en/docs/analytics-platform/using/cja-dataviews/session-settings) for more information.

### Event container

The Event container defines which page, mobile application, or other type of events you would like to include or exclude from a segment. It is the most narrow of the containers available. It lets you identify specific clicks, page view, taps on button in a mobile app where a condition is true. The Event container lets you view a single tracking code, or isolate behavior within a particular area of your mobile app. You may also want to pinpoint a specific value when an action occurs, such as the marketing channel when an order was placed. When you define a segment with a simple condition like Page Name equals Checkout, then the Event container resolves to:

- All page view events where the page name equals Checkout.

Event containers include value-based, single page breakdowns for:

- Products
- List Props
- List dimensions
- Merchandising dimensions (in the context of events)

### B2B containers

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)

When you do have access to [Customer Journey Analytics B2B Edition](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition), additional containers for use in segments are available. You can find more details on the use of these additional containers in [B2B concepts and features](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-concepts-features).

### Logic group container

Logic Group enables you to group conditions into a single sequential segment checkpoint. As part of the sequence, the logic defined in the container identified as Logic Group is evaluated after any prior sequential checkpoint and before any following sequential checkpoint. See [Logic Group](/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build#logic-group) for more information.

### Nest containers

When creating containers within other containers, you are actually creating a segment within a segment. The following logic is applied to nested containers:

- Determine what data is included using the outermost container. Any data that does not match this outer rule is discarded in the report.
- Apply the nested segment definition to the remaining data. The nested segment definition does NOT apply to any data that the first definition discarded.
- Repeat until all nested-container segment definitions have been calculated. The remaining data is then included in the result and used for reporting.

NOTE
When you nest a segment within a segment (for example, you drag a segment from the Components panel onto your segment definition), a container is created with a copy (not a reference) of the dragged segment definition.
Related Articles
Create segments
Segment builder
Quick segments
Sequential segments
Manage segments
recommendation-more-help
