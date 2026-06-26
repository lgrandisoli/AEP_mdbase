---
title: "Get started with data management about-data"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/data-management/gs-data"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:15.621241+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with data management about-data

Last update: May 8, 2026
- Topics:
- [Data Management](#)

CREATED FOR:

- Beginner
- Intermediate
- Developer
- Admin
- User

Data is the foundation of every journey, decision, and message you deliver with Adobe Journey Optimizer.

This page gives you a practical starting point to understand:

- The core data building blocks used by Journey Optimizer (schemas, datasets, identities, profiles)
- How Journey Optimizer uses Adobe Experience Platform data
- Which data setup steps your team must complete before building journeys and campaigns
- Where to go next for detailed configuration and best practices

Use this guide together with your data engineers, administrators, and marketers so everyone shares a common picture of how data flows into and out of Journey Optimizer.

TIP
New to data management in Journey Optimizer? Watch the
Set up data overview tutorial
for a practical, beginner-friendly walkthrough of schemas, datasets, and sources.
## How Journey Optimizer uses Adobe Experience Platform data aep-data

Adobe Journey Optimizer is built on Adobe Experience Platform. It does not maintain a separate, isolated data store. Instead, it uses the same data foundation as other Experience Cloud applications.

Schemas and datasets live in Adobe Experience Platform. Identities and the [Real-Time Customer Profile](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/get-started-profiles) are managed by Identity Service and Profile Service. Journey Optimizer reads profile and event data from Adobe Experience Platform to evaluate journey conditions, personalize messages, and select offers. It writes interaction data — such as send, open, click, and bounce events, and journey step events — back into Experience Platform datasets. It can also look up additional datasets at runtime without copying that data into the profile.

TIP
Think of Adobe Experience Platform as your central data layer, and Journey Optimizer as an application that orchestrates journeys and messages using that shared data foundation.
➡️ [Learn more about Journey Optimizer architecture](/en/docs/journey-optimizer/using/get-started/essentials/understanding-ajo#architecture-details#_blank)

## Key data concepts in Journey Optimizer key-concepts

When you work with data in Journey Optimizer, you will encounter several related concepts. The table below gives you a quick overview; the sections that follow explain each concept in more detail.

Concept
What it is
Primary use in Journey Optimizer
XDM schema
Rules that represent, validate, and format your data (built from a class + field groups)
Model profile attributes and behavioral events
Dataset
Storage table for data conforming to a schema
Hold profile, event, and system-generated data
Source connector
Streams or batches data from external systems into AEP
Ingest CRM, analytics, and web data
Data source
Exposes AEP or external fields inside journeys
Power journey conditions and message personalization
Identity
Identifier that uniquely represents an individual customer
Stitch profiles across channels
Lookup dataset
Runtime reference to AEP data without profile storage
Enrich messages with live reference data
### Schema (XDM schema) schema

A schema is a set of rules that represent, validate, and format your data. It is comprised of a **class** (which defines the base behavior: record or time-series) and optional **field groups** (which add specific fields). Schemas are defined using Experience Data Model (XDM) standards and live in Adobe Experience Platform.

XDM exists to solve a real problem: the same concept — a customer, a purchase, a product — is named and structured differently across source systems. XDM provides a shared language that unifies these concepts under a single definition, regardless of where the data originates. This is what allows Journey Optimizer to work consistently with data from your CRM, your website, your mobile app, and your data warehouse at the same time.

In Journey Optimizer, you typically work with **XDM Individual Profile** schemas for customer attributes (name, preferences, consent) and **XDM ExperienceEvent** schemas for behavioral events (purchases, page views, sign-ups).

➡️ [Learn more about schemas](/en/docs/journey-optimizer/using/data-management/get-started-schemas)

### Dataset dataset

A dataset is a storage and management construct for data that conforms to a schema — think of it as a table with a defined set of columns and rows. All data used by Journey Optimizer is stored in Adobe Experience Platform datasets. These can be profile datasets (contributing to Real-Time Customer Profile), event datasets (storing behavioral data for journeys and analysis), or system datasets automatically created by Journey Optimizer for tracking, feedback, and journey step events.

➡️ [Learn more about datasets](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets)

### Source connector source-connector

A source connector (also known as a **source**) helps you ingest data from multiple systems — such as Adobe Analytics, Adobe Experience Platform Web SDK, cloud storage (S3, Azure Blob), or CRM databases — into Adobe Experience Platform. Beyond raw ingestion, connectors enable the structuring, labeling, and enhancement of data using Experience Platform services, including field mapping to your XDM schemas and data governance labeling.

➡️ [Learn more about source connectors](/en/docs/journey-optimizer/using/connect-systems/get-started-sources)

### Data source (Journey Optimizer) data-source

A data source in Journey Optimizer defines which fields from Adobe Experience Platform (or external APIs) are exposed inside journeys and messages. Configured in the Journey Optimizer UI, data sources typically include the built-in Adobe Experience Platform data source (exposing Real-Time Customer Profile attributes) and optional external or custom data sources called at journey runtime for additional enrichment. They are used for journey conditions, custom actions, and message personalization.

➡️ [Learn more about data sources](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources)

NOTE
The
Adobe Experience Platform Glossary
defines “data source” generically as the origin of data (a CRM, mobile app, etc.). In Journey Optimizer,
data source
has a specific meaning: a UI configuration that controls which fields are exposed inside journeys and messages.
### Identity and real-time customer profile identity

An identity is an identifier that uniquely represents an individual customer, such as a cookie ID, device ID, email address, or CRM ID. Identities are organized into namespaces (Email, ECID, CRMID), and multiple identities for the same person are stitched into a unified identity graph. Real-Time Customer Profile uses that graph to maintain a holistic view of each individual customer by combining data from multiple channels — including online, offline, CRM, and third-party sources.

A key concept for beginners is the **profile fragment** model. Each time a customer interacts with your brand on a specific device or channel — your website, mobile app, a store — that interaction is recorded as a profile fragment: a partial view of that customer based on that specific touchpoint. Real-Time Customer Profile continuously stitches these fragments together based on shared identity values, building a complete, up-to-date profile. Journey Optimizer reads from this assembled profile to evaluate conditions, select offers, and personalize messages in real time.

➡️ [Learn more about identities in Journey Optimizer](/en/docs/journey-optimizer/using/audiences-profiles-identities/get-started-identity)

### Lookup dataset lookup-dataset

A lookup dataset lets Journey Optimizer retrieve reference or transactional data at runtime from an Adobe Experience Platform dataset, without storing that data on the Real-Time Customer Profile. This is useful for frequently changing reference data (prices, inventory, store hours) or transactional data that is needed at message time but does not belong on the profile. Journey Optimizer performs the lookup during journey or message execution based on a key such as a product ID.

➡️ [Learn more about lookup datasets](/en/docs/journey-optimizer/using/data-management/lookup-aep-data)

## Data readiness checklist checklist

Before marketers start building journeys and campaigns, your organization should complete a set of data readiness steps. This ensures that Journey Optimizer can use the right data, at the right time, and in a compliant way.

NOTE
The steps below involve multiple roles: data engineers, administrators, and marketers. Use this checklist as a shared plan to prepare your environment. Steps 1–4 are completed in Adobe Experience Platform; Steps 5–6 are configured in Journey Optimizer.
The six steps below walk you through the full data setup process, from identity configuration to verifying that data flows correctly into Journey Optimizer:

- Define your identity strategy
- Design schemas for profile and event data
- Create profile-enabled datasets
- Ingest data from your sources
- Configure data sources in Journey Optimizer
- Verify tracking, feedback, and journey datasets

Define your identity strategy
Choose a primary identity for your customers (such as ECID, email, or CRMID) and configure the corresponding namespaces in Adobe Experience Platform Identity Service. Make sure identity fields are present in your profile-enabled schemas and validate that profiles are correctly stitched into the identity graph.

➡️ [Learn more about identities in Journey Optimizer](/en/docs/journey-optimizer/using/audiences-profiles-identities/get-started-identity)

Design schemas for profile and event data
Create **XDM Individual Profile** schemas to capture customer attributes such as name and contact information, preferences and interests, and lifecycle stage or consent state. Create **XDM ExperienceEvent** schemas to capture behavioral and transactional data such as web and app events, purchases, and offline interactions. Mark the correct fields as identities and profile attributes where appropriate.

➡️ [Learn more about schemas](/en/docs/journey-optimizer/using/data-management/get-started-schemas)

Create profile-enabled datasets
In Adobe Experience Platform, create datasets based on your XDM schemas and enable Profile on any dataset that should contribute to Real-Time Customer Profile. Confirm that system-generated datasets created by Journey Optimizer are visible in the Datasets workspace.

➡️ [Learn more about datasets](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets)

Ingest data from your sources
Configure source connectors for your enterprise systems — such as Adobe Analytics, Adobe Experience Platform Web SDK, or your CRM and POS platforms — and map incoming fields to your XDM schemas. Validate that data lands in the correct datasets and appears in Real-Time Customer Profile where expected.

➡️ [Learn more about source connectors](/en/docs/journey-optimizer/using/connect-systems/get-started-sources)

➡️ [Tutorial: Create datasets and ingest data](/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data#_blank)

Configure data sources in Journey Optimizer
Data sources are a Journey Optimizer-specific concept: they are not where your data lives, but where you declare which fields Journey Optimizer is allowed to read during journey and message execution. Before a journey can evaluate a condition like “is the customer a loyalty member?” or personalize a message with a first name, the relevant profile fields must be exposed through a data source configuration.

Journey Optimizer includes a built-in [Adobe Experience Platform data source](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/adobe-experience-platform-data-source) that gives direct access to Real-Time Customer Profile attributes. This covers the vast majority of use cases: reading profile attributes for personalization or checking consent and preference fields. You can also configure [external data sources](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/external-data-sources) to call third-party APIs at journey runtime — for example, to retrieve a real-time loyalty score, a product recommendation, or a store inventory level that is not stored in Adobe Experience Platform.

| note |
| --- |
| NOTE |
| Direct access to experience event data via the built-in Adobe Experience Platform data source is deprecated and being progressively disabled. [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/exp-event-lookup#_blank). |

Configuring data sources is an administrative task that unlocks the full data layer for journey authors and marketers. Once a field is exposed through a data source, it becomes available in the journey condition builder, in message personalization editors, and in offer decisioning rules — without requiring any additional engineering work at journey-build time.

➡️ [Learn more about data source configuration](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources)

Verify tracking, feedback, and journey datasets
Confirm that Journey Optimizer system-generated datasets are available in the Datasets workspace. Run test journeys and campaigns, then use Query Editor to verify that send, open, click, and bounce events are recorded and that journey step events and states are captured correctly. Use these datasets for ongoing monitoring, troubleshooting, and journey optimization.

➡️ [Learn more about queries in Journey Optimizer](/en/docs/journey-optimizer/using/data-management/get-started-queries)

## Guardrails and data design considerations guardrails

Some product guardrails and limitations can influence how you design your data model and journeys. Review these early to avoid rework later.

IMPORTANT
Always refer to the
Journey Optimizer guardrails and limitations
page for the latest information. The summaries below highlight key items but may evolve over time.
### Journey Optimizer system datasets and TTL datasets-ttl

Journey Optimizer creates several system-generated datasets for tracking, feedback, and journey step events. As of February 2025, a time-to-live (TTL) guardrail is being rolled out to some of these datasets, which may affect how long data is retained for analysis and troubleshooting.

➡️ [Learn more about dataset TTL guardrails](/en/docs/journey-optimizer/using/data-management/datasets/datasets-ttl)

### Streaming segmentation and Journey Optimizer events streaming-segmentation

As of November 1st, 2024, streaming segmentation no longer supports send and open events from Journey Optimizer tracking and feedback datasets. For use cases such as frequency capping and fatigue management, use [Business Rules](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets) instead of streaming segments based on send/open events.

➡️ [Learn more about datasets](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets)

### Dataset lookup and decisioning lookup-guardrails

Dataset lookup is ideal for frequently changing attributes (inventory, pricing, weather) or data that does not need to be stored on the Real-Time Customer Profile. Review product-specific guardrails such as dataset size limits and query caps in the relevant documentation before designing your lookup strategy.

➡️ [Learn more about lookup datasets](/en/docs/journey-optimizer/using/data-management/lookup-aep-data)

## Example: preparing data for a welcome journey example

The following example shows how the concepts on this page work together in a simple scenario.

- A data engineer creates an [XDM Individual Profile schema](/en/docs/journey-optimizer/using/data-management/get-started-schemas) for customer attributes (name, email, loyalty tier, consent) and an XDM ExperienceEvent schema for web sign-up events.
- [Profile-enabled datasets](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets) are created for each schema: one for CRM attributes and one for sign-up events.
- Web and mobile teams stream sign-up events via Adobe Experience Platform Web SDK; CRM data is ingested via a [source connector](/en/docs/journey-optimizer/using/connect-systems/get-started-sources).
- An administrator configures the [Adobe Experience Platform data source](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/adobe-experience-platform-data-source) in Journey Optimizer and exposes fields such as profile.person.name.firstName, profile.personalEmail.address, and profile.loyaltyTier.
- A marketer [creates a welcome journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs) that listens for a sign-up event and uses those profile attributes to [personalize the welcome email](/en/docs/journey-optimizer/using/content-management/personalization/personalize). Journey Optimizer writes send and open events to tracking datasets and logs journey progress in journey step event datasets.
- A developer uses [Query Editor](/en/docs/journey-optimizer/using/data-management/get-started-queries) to verify that events are flowing correctly and analyzes performance (opens, clicks, time-to-send). The team adjusts the journey and content based on these insights.

This flow illustrates how schemas, datasets, sources, data sources, and queries work together in a complete, beginner-friendly use case.

## Related resources related-resources

**Get started with schemas**

Learn how to create XDM schemas in Adobe Experience Platform, choose the right class and field groups, and model your profile attributes and behavioral events.

[Learn more](/en/docs/journey-optimizer/using/data-management/get-started-schemas)

**Work with datasets**

Understand how to create profile-enabled and event datasets, monitor data ingestion, and explore the system-generated datasets that Journey Optimizer creates automatically for tracking, feedback, and journey step events.

[Learn more](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets)

**Configure data sources**

Step-by-step guidance on setting up the built-in Adobe Experience Platform data source and optional external data sources to expose profile fields and external API responses inside your journeys.

[Learn more](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources)

**Use Adobe Experience Platform data (lookup)**

Discover how to enrich messages at runtime with reference or transactional data from AEP datasets, without storing that data on the Real-Time Customer Profile.

[Learn more](/en/docs/journey-optimizer/using/data-management/lookup-aep-data)

**Get started with queries**

Use Query Service to analyze Journey Optimizer datasets, verify that events are flowing correctly, and build reporting queries on send, open, click, and bounce data.

[Learn more](/en/docs/journey-optimizer/using/data-management/get-started-queries)

**Get started with profiles**

Explore how Real-Time Customer Profile works in Journey Optimizer and how to browse, inspect, and validate individual customer profiles in the Platform UI.

[Learn more](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/get-started-profiles)

**Set up data overview tutorial**

A beginner-friendly video walkthrough of data setup in Journey Optimizer, covering schemas, datasets, and sources end to end.

[Watch tutorial](/en/docs/journey-optimizer-learn/tutorials/data-management/set-up-data-overview){target="_blank"}

**Create datasets and ingest data tutorial**

A hands-on tutorial showing how to create datasets in Adobe Experience Platform and ingest data using source connectors, with step-by-step instructions you can follow in your own sandbox.

[Watch tutorial](/en/docs/journey-optimizer-learn/tutorials/data-management/create-datasets-and-ingest-data){target="_blank"}

recommendation-more-help
