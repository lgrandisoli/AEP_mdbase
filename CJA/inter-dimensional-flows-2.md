---
title: "Inter-dimensional flows"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/multi-dimensional-flow"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:45:23.437137+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Inter-dimensional flows

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)

CREATED FOR:

- User

An inter-dimensional flow lets you examine user paths across various dimensions. This article shows how to use this flow for two use cases: mobile app interactions and events, and how campaigns drive web visits

## Mobile app interactions and events

The Screen Name dimension is used in this example flow to see how users use the various screens (scenes) in the app. The top screen returned is **luma: content: ios: en: home**, which is the home page of the app:

To explore the interaction between screens and event types (like add to cart, purchases, and others) in this app, drag and drop the **Event Types** dimension:

- On top of any available step in the flow, to replace that dimension:
- Outside of the current flow visualization, to add the dimension:

The flow visualization below shows the result of adding the **Event Types** dimension. The visualization provides insights to how mobile app users move through various screens in the app before adding products to a cart, close the application, are presented an offer, and more.

## How campaigns drive web visits

You want to analyze which campaigns drive visits to the web site. You create a flow visualization with the **Campaign Name** as the dimension

You replace the last **Campaign Name** dimension with the **Formatted Page Name** dimension and add another **Formatted Page Name** dimension at the end of the flow visualization.

You can hover over any of the flows to see more details. For example which campaigns have resulted in a Cart checkout.

recommendation-more-help
