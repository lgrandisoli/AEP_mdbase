---
title: "Transition guide"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-transition"
category: "overview"
topic: "analytics-platform/using/cja-overview/cja-b2b"
created_at: "2026-06-23T20:42:53.890523+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

[B2B Edition]{class="badge informative"}

# Transition guide

Last update: June 18, 2026
- Topics:
- [Analysis Workspace](#)
- [Administration](#)
- [Data management](#)

CREATED FOR:

- User
- Admin

This guide discusses how to transition from Customer Journey Analytics to the B2B Edition of Customer Journey Analytics.

The article assumes you already use Customer Journey Analytics to some extent:

- You have [connections](/en/docs/analytics-platform/using/cja-connections/overview) that ingest data into Customer Journey Analytics.
- You have [data views](/en/docs/analytics-platform/using/cja-dataviews/data-views) that use the data from these connections.
- You have [projects](/en/docs/analytics-platform/using/cja-workspace/home) with reports and visualizations leveraging these data views.

If you have not used Customer Journey Analytics before, refer to the [B2B Edition quick start guide](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-quick-start-guide).

If you are an Adobe Analytics user and plan to use Customer Journey Analytics B2B Edition, first refer to the [upgrade from Adobe Analytics to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations) documentation.

## Existing implementation

The existing implementation of Customer Journey Analytics does not change at all once you are licensed and provisioned for Customer Journey Analytics B2B Edition.

All existing connections are considered [person-based connections](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-concepts-features#connections-and-identifiers) and continue to work without any update. Everything that relies on the data from these person-based connections, such as data views, workspace projects, segments, scheduled exports, alerts, and more, continue to work as originally planned and intended.

IMPORTANT
You are not able to change existing person-based connections to an account-based connection. A new account-based connection is required to make use of the B2B Edition features.
## Implement B2B features

To implement B2B features in your existing implementation, you need to follow these steps:

- Model your B2B data. You can use the Adobe Experience Data Model (XDM) to standardize B2B data and define schemas for your B2B data. You can base your schemas on the standard classes that are provided in Real-time CDP B2B Edition or you can use your own custom classes and schemas. The use cases articles use Real-time CDP B2B Edition classes and schemas, however, a Real-time CDP B2B Edition license is not required to utilize the standard classes and schemas. Customer Journey Analytics B2B Edition assumes at least account-based time-series event data, and benefits from additional profile or lookup record data. Such as account data, buying group data, opportunity data, marketing list member data, and more. Define which identifier you want to use as the primary account identifier (Account ID). Often an existing CRM or other tool (for example: Demandbase) helps you to determine that identifier. Identify additional identifiers for the other B2B data you plan to use: global account identifier, opportunity identifier, buying group identifier, and person identifier.
- Prepare your B2B data. Ensure you add and collect account identifiers across all time-series event data and relevant record data. Similarly, ensure your time-series event data and lookup record contains other identifiers for relevant events. For example: an event that signals the move to another sales stage, should have an opportunity identifier. And that identifier should be part of your opportunity lookup data.
- Create a new account-based connection . Select which optional containers you want to include, add datasets and define the settings for each dataset . Use match by container for lookup record datasets whenever that is possible.
- Create data views based on your new connection. Ensure you add all relevant fields as metrics or dimensions from the data you have ingested. Apply component settings (like persistence, attribution, and more) if so required. Add additional derived fields where appropriate.
- Create workspace projects to report and gain insights on your B2B data. Use specific B2B features, like containers , to gain deep insights. You can combine B2B (person-based) and B2B (account-based) reports and insights, through the use of multiple panels , in one workspace project.

recommendation-more-help
