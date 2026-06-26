---
title: "About Orchestrated campaign activities orchestrated-campaign-activities"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/about-activities"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:07.343229+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# About Orchestrated campaign activities orchestrated-campaign-activities

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

Orchestrated campaign activities are grouped into three categories. Depending on the context, available activities may differ.

All activities are detailed in the sections below:

- [Targeting activities](#targeting)
- [Channel activities](#channel)
- [Flow control activities](#flow-control)

{align="left" width="80%"}

NOTE
- Depending on your licensing model, your permissions and your implementation, available activities may differ.
- The number of activities in an Orchestrated campaign is limited to 500.

## Targeting activities targeting

These activities are specific to targeting. They let you build one or more targets by defining an audience and splitting or combining these audiences using intersection, union or exclusion operations.

{align="left" width="40%"}

Available targeting activities are:

- [Build audience](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/build-audience): Define your target population. You can either select an existing audience or use the rule builder to define your own query.
- [Change dimension](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/change-dimension): Change the targeting dimension as you are building your Orchestrated campaign.
- [Combine](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/combine): Perform segmentation on your inbound population. You can use a union, an intersection or an exclusion.
- [Deduplication](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/deduplication): Delete duplicates in the result(s) of the inbound activities.
- [Enrichment](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/enrichment): Define additional data to process in your Orchestrated campaign. With this activity, you can leverage the inbound transition and configure the activity to complete the output transition with additional data.
- [Reconciliation](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/reconciliation): Define the link between the data in Journey Optimizer data and the data in a work table, for example data loaded from an external file.
- [Split](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/split): Segment incoming population into several subsets.

## Channel activities channel

Adobe Journey Optimizer allows you to automate and execute marketing campaigns across multiple channels. You can combine [channel activities](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels) into the canvas to create cross-channel Orchestrated campaign that can trigger actions based on customer behavior.

Learn how to [create a channel action in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels).

## Flow control activities flow-control

The following activities are specific to organizing and executing Orchestrated campaigns. Their main task is to coordinate the other activities.

{align="left" width="20%"}

Available flow control activities are:

- [And-join](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/and-join): Synchronize multiple execution branches of an Orchestrated campaign.
- [Fork](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/fork): Create outbound transitions to start several activities at the same time.
- [Wait](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/wait): Momentarily pause execution of a part of an Orchestrated campaign.

NOTE
The
End
activity graphically marks the end of an Orchestrated campaign. This activity has no functional impact and is therefore optional
recommendation-more-help
