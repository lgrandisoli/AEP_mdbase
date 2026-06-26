---
title: "Get started with Orchestrated campaigns orchestrated-camp"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:47.352886+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with Orchestrated campaigns orchestrated-camp

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

Campaign Orchestration in Adobe Journey Optimizer powers sophisticated, brand-initiated campaigns across channels—both **marketing** and **transactional**. Marketing campaigns help you drive engagement, revenue, and customer loyalty at scale. Transactional messages do not require opt-in and are suited for time-sensitive communications such as disruptions, emergencies, or cancellations.

IMPORTANT
To access Campaign Orchestration, your license must include either the
Journey Optimizer – Campaigns & Journeys
or the
Journey Optimizer - Campaigns
package. Contact your Adobe representative to confirm your license and update if needed.
While cross-channel marketing is essential, Orchestrated campaigns make it seamless. With a visual, drag-and-drop interface, you can design and automate complex marketing workflows, from segmentation to message delivery, across multiple channels. Everything happens in one intuitive environment, built for speed, control, and efficiency.

{modal="regular"}

➡️ [Discover Orchestrated campaigns in video](#video-oc)

## Core capabilities

Campaign Orchestration is built around four key pillars:

{width="150px"}
On-Demand Audiences
Instantly query across datasets to create audience segments using any combination of data types and dimensions.
{width="150px"}
Multi-entity segmentation & sending
Go beyond person-based campaigns—use entities like product catalogs, store locations, or service data to target with precision.
Support multi-level sending, where one message is sent per Profile and per associated secondary entity. These secondary entities can include contact addresses, bookings, subscriptions, contracts, or other linked data. For example, this enables campaigns to be sent to all known addresses of a Profile or for each booking associated with that Profile.
{width="150px"}
Pre-send visibility & precision
Get exact segmentation counts and full campaign scope before launch, ensuring accuracy and confidence.
{width="150px"}
Multi-step campaign workflows
Design multi-steps campaigns, from daily messages to complex campaigns like seasonal promotions or major product launches.
NOTE
For more information on the supported channels, refer to the table in this section:
Channels in journeys & campaigns
.
Available channels vary based on your licensing model and add-ons.
## Orchestrated campaigns & journeys

Even though the Orchestrated campaigns visualization has similarities to journeys, it solves different purposes and use cases:

- Journeys - 1 to 1 canvas where each profile travels through the different steps at their own pace. The state of each customer is maintained within its context to trigger real-time actions.
- Orchestrated campaigns - Unlike journeys, Orchestrated campaigns operate using a batch canvas that calculates segments. All profiles are processed together at the same time.

Both canvases are optimized for their respective use cases: Journey canvas publishes journey that tend to live for a longer period of time, while Campaign canvas is designed for iterative and incremental runs of a batch campaign.

## What’s inside an Orchestrated campaign? gs-ms-campaign-inside

The Orchestrated campaign canvas is a representation of what is supposed to happen. It describes the various tasks to be performed and how they are linked together.

Each Orchestrated campaign contains:

- Activities : An activity is a task to be performed. The various activities are represented on the canvas by icons. Each activity has specific properties and other properties that are common to all activities. In an Orchestrated campaign canvas, a given activity can produce multiple tasks, in particular when there is a loop or recurrent actions.
- Transitions : Transitions link a source activity to a destination activity and define their sequence.
- Worktables : The worktable contains all the information carried by the transition. Each Orchestrated campaign uses several worktables. The data conveyed in these tables can be used throughout the Orchestrated campaign’s life cycle.

A typical entry-level Orchestrated campaign follows this pattern: **Build audience → Fork → Channel A + Channel B**.

This approach lets you target the same audience with two parallel branches in a single campaign run — for example, one branch using a Marketing email and another using a Transactional email. Each branch is independent and can use a different channel configuration, message content, or category.

➡️ [Learn how to use the Fork activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/fork)

➡️ [Understand Marketing vs Transactional messages](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels#marketing-vs-transactional)

## Introduction video video-oc

Learn key concepts and capabilities available with Orchestrated campaigns.

https://video.tv.adobe.com/v/3471538/?learn=on&enablevpops
## Let’s dive deeper

Now that you have an understanding of what orchestrated campaigns are, it’s time to dive deeper into these documentation sections to start working with the feature.

**Configuration steps**

**Create an Orchestrated campaign**

**Work with activities**

## Additional resources

- **Build your first rule** - Master the rule builder to create targeted queries and segment your audiences with precision using relational data.
- **Create relational schemas** - Understand how to set up and configure relational schemas to leverage multi-entity data in your campaigns.
- **Reporting for Orchestrated campaigns** - Track and analyze your campaign performance with detailed reporting metrics and insights.
- **Start and monitor campaigns** - Learn best practices for launching campaigns and monitoring their execution in real-time.
- **Guardrails and limitations** - Review important guardrails, limitations, and best practices to ensure optimal campaign performance.
- **Frequently Asked Questions** - Find answers to common questions about Orchestrated campaigns features, capabilities, and use cases.
- **Orchestrated campaign tutorials** - Explore step-by-step video tutorials covering features and best practices.

recommendation-more-help
