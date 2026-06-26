---
title: "Audience publishing overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/audiences/audiences-overview"
category: "overview"
topic: "analytics-platform/using/cja-components/audiences"
created_at: "2026-06-02T19:05:53.330900+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Audience publishing overview

Last update: May 13, 2026
- Topics:
- [Audiences](#)

CREATED FOR:

- User
- Admin

NOTE
Understand the difference between audience analysis and audience publishing:
- **Audience analysis**: Allows you to ingest audience membership data from Experience Platform Profile datasets into a Customer Journey Analytics connection. For information about audience analysis, see [Audience analysis overview](/en/docs/analytics-platform/using/cja-connections/audience-analysis/audience-analysis-overview).
- **Audience publishing**: Allows you to create and publish audiences discovered in Customer Journey Analytics to Adobe Experience Platform for customer targeting and personalization.

You can create and publish audiences discovered in Customer Journey Analytics to [Real-Time Customer Profile](/en/docs/experience-platform/profile/home) in Adobe Experience Platform for customer targeting and personalization. (For information about ingesting audience membership data from Experience Platform Profile datasets into a Customer Journey Analytics connection, see [Audience analysis overview](/en/docs/analytics-platform/using/cja-connections/audience-analysis/audience-analysis-overview).)

Publishing audiences provides a clear way to activate and to take action on insights found within Customer Journey Analytics. These actions might include:

- Using the audience for a journey in Adobe Journey Optimizer.For more information about using audiences that are published to Experience Platform, see [Get started with audiences](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences) in the Journey Optimizer documentation.
- Exporting the audience to a 3rd-party through an Experience Platform destination.
- Enriching the Real-time customer profile with useful attributes derived from event-based data in Customer Journey Analytics.
- Doing all this with minimal latency after publishing the audience.For more information, see [Latency considerations](/en/docs/analytics-platform/using/cja-components/audiences/publish#latency-considerations) in [Create and publish audiences](/en/docs/analytics-platform/using/cja-components/audiences/publish).
- Publishing one-time audiences or recurring audiences.

The audiences you create in Customer Journey Analytics do not have to be based on datasets enabled for profile. You can ingest historical data into Experience Platform without enabling associated datasets and schemas for profile. Then use these datasets to discover relevant audiences in Customer Journey Analytics and publish these audiences to Real-time Customer Profile in Experience Platform for activation purposes.

## Key terminology

**Audience**: A set or list of identities that have both a namespace and a specific ID related to that namespace. Audiences are transportable from the Adobe Experience Platform and applications that sit on top of it (such as Customer Journey Analytics). Audiences can contain mixed namespaces.

**Segment**: A set of rules that, when evaluated over a set of data for a time period, produces a subset of data. A segment can be used in the process of creating an audience when coupled with other supporting services. Segments are defined and maintained in Customer Journey Analytics.

## Permissions

- Administrators are automatically granted the Audience Publishing permission in Adobe Admin Console.
- Administrators and product profile administrators can grant the Audience Creation and Audience View permission to individual users. See User-level access control for more information.
- Administrators also need the Manage Profiles permission in Adobe Experience Platform.

## Data governance and consent

When you publish an audience in Customer Journey Analytics, the Data Governance labels and policies attached to the fields used in the audience are recorded. When the audience is activated in any Adobe Experience App, all associated Data Governance labels and policies are available for that audience and appropriate enforcement can be applied. [Learn more about consent](/en/docs/experience-platform/data-governance/policies/user-guide#consent-policy).

## Next steps

- [Create and publish audiences](/en/docs/analytics-platform/using/cja-components/audiences/publish)
- [Manage audiences](/en/docs/analytics-platform/using/cja-components/audiences/manage)

recommendation-more-help
