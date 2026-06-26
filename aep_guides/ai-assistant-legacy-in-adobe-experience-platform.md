---
title: "AI Assistant (Legacy) in Adobe Experience Platform"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/ai-assistant/home"
category: "overview"
topic: "experience-platform/ai-assistant-in-adobe-experience-platform-guide"
created_at: "2026-06-26T17:21:57.424236+00:00"
---
Breadcrumbs: Documentation > Experience Platform > AI Assistant in Adobe Experience Platform Guide

# AI Assistant (Legacy) in Adobe Experience Platform

Last update: May 13, 2026
- Topics:
- [AI Assistant](#)

CREATED FOR:

- Admin
- User
- Developer
- Leader

IMPORTANT
This document applies to AI Assistant (Legacy). For information on AI Assistant (Next-Gen), read the
AI Assistant UI guide
in the
AI in Experience Cloud
documentation.
Refer to the following table for a comparison of AI Assistant (Legacy) and AI Assistant (Next-Gen):

Feature Area
AI Assistant (Legacy)
AI Assistant (Next-Gen)
User experience
AI Assistant (Legacy) is available in a right-rail panel only.
AI Assistant (Next-Gen) is available in both right-rail panel and immersive full-screen experience.
Scope of capabilities
You can use AI Assistant (Legacy) for both product knowledge and operational insights.
You can use AI Assistant (Next-Gen) for product knowledge, operational insights, as well as advanced agentic skills and multi-step task execution.
Platform architecture
AI Assistant (Legacy) is not built on the Agent Orchestrator stack.
AI Assistant (Next-Gen) is powered by
Adobe Experience Platform Agent Orchestrator
, enabling extensibility and advanced coordination across capabilities.
Application coverage
AI Assistant (Legacy) is an application-specific implementation.
You can use AI Assistant (Next-Gen) for a unified AI Assistant experience across all Adobe Experience Cloud applications.
Access and permission model
Application-scoped access model aligned to individual product boundaries.
All users get access to AI Assistant (Next-Gen) and associated Experience Platform agents. **Note**:

- **Adobe Experience Manager**: Your administrator must grant you the permission to access AI Assistant (Next-Gen) through the [Adobe Admin Console](https://helpx.adobe.com/enterprise/using/admin-console.html).
- **Customer Journey Analytics**: Your administrator must grant you the permission to access AI Assistant through [Customer Journey Analytics Access Control](/en/docs/analytics-platform/using/technotes/access-control?lang=en). This allows you to ask product knowledge and data insights questions.

The following video is intended to support your understanding of AI Assistant.

https://video.tv.adobe.com/v/3429845?learn=on
https://video.tv.adobe.com/vc/3429845/eng.json
Read this document to learn about AI Assistant (Legacy) in Adobe Experience Platform.

AI Assistant (Legacy) in Adobe Experience Platform is a conversational experience that you can use to accelerate your workflows in Adobe applications. You can use AI Assistant (Legacy) to better understand product knowledge, troubleshoot problems, or search through information and find operational insights. AI Assistant (Legacy) supports Experience Platform, Real-Time Customer Data Platform, Adobe Journey Optimizer and Customer Journey Analytics.

IMPORTANT
You must agree to a
user agreement
before you can use AI Assistant (Legacy). The user agreement also contains the public beta agreement. This is so that you can use additional AI Assistant (Legacy) features as they roll out in a beta capacity.
Select to view user agreement interface
## Understanding AI Assistant understanding-ai-assistant

AI Assistant (Legacy) responds to your submitted questions by querying a database and then translating data from the database into a human-readable answer.

This internal representation of underlying data is also known as the **Knowledge Graph** - a comprehensive web of concepts, data, and metadata for a given answer.

The Knowledge Graph consists of sub-graphs that are referenced whenever queries submitted:

- Customer operational insights.
- Customer operational insights across various meta-stores.
- Experience League documentation.

There are two classes of questions to consider before querying AI Assistant (Legacy):

### Product knowledge product-knowledge

Product knowledge refers to concepts and topics grounded in Experience League documentation. Product knowledge questions can be further specified into the following sub-groups:

Product knowledge
Examples
Pointed learning
- What is the difference between an identity and a primary or foreign key?
- What are lookalike audiences?

Open discovery
- How can I export this dataset?
- Are there schemas for healthcare customers?

Troubleshooting
- Why can’t I turn on a schema owned by Adobe for profile?
- Why can’t I delete a segment?

Watch the following video for additional information on AI Assistant (Legacy) product knowledge:

https://video.tv.adobe.com/v/3438032/?learn=on
https://video.tv.adobe.com/vc/3438032/eng.json
### Operational insights operational-insights

Operational insights refer to answers AI Assistant (Legacy) generates about your meta data objects (attributes, audiences, dataflows, datasets, destinations, journeys, schemas, and sources), including counts, lookups, and lineage impact. It does not look at any data within the sandbox.

- How many datasets do I have?
- How many schema attributes have never been used?
- Which audiences have been activated?

You can ask AI Assistant (Legacy) questions about your operational insights in the following domains:

Domain
Supported metadata
Unsupported metadata
Attributes
- Attribute name search
- Attribute - schema relationship
- Attribute - dataset relationship
- Attribute - audience relationship
- Attribute - destination relationship

- Attribute class
- Audit
- Deprecation status
- Labels
- Value stored in attributes

Audiences
- Audience count
- Audience type (streaming or batch)
- Creation/modification dates
- Activation status
- Profile count
- Duplicate audiences
- Audience definition search
- Audience - audience relationship
- Audience - attribute relationship
- Audience - dataset relationship
- Audience - destination relationship
- Name search
- Name and ID search

- Audience overlaps
- Audience activation
- Audience - campaign relationships
- Audit
- Create/modification
- Labels
- Profile qualification trends

Dataflows
- Dataflow counts
- Dataflow status
- Dataflow - dataset relationship
- Dataflow - source relationship

- Creation/modification
- Dataflow-batch relationships
- Ingest profile count

Datasets
- Dataset count
- Profile enable status
- Creation/modification date
- Dataset - schema relationship
- Dataset - audience relationship
- Dataset - attribute relationship
- Dataset - dataflow relationship
- Dataset size
- Number of rows
- Name search
- Name and ID search

- Audit
- Created by
- Dataset - batch relationship
- Dataset creation/modification
- Number of profiles
- Value search

Data Models (Federated Audience Composition)
- Data model counts
- Name search
- Data model and schema relationship
- Link properties
- Status
- Creation and modification dates
- Link-data model relationship

Destinations
- Configured destination counts
- Destination - audience relationship
- Destination attribute relationship

- Account set up
- Account credential information
- Unique profiles activated

Federated Databases (Federated Audience Composition)
- Database count
- Database name
- Database type
- Created/modified dates
- Status

Journeys
- Counts
- Name search
- Name and ID search
- Journey status
- Triggered status (audience vs. events)
- Creation/modification dates
- Recurring frequency

- Attributes - journey relationships
- Audit
- Creation/modification
- Created by
- Events
- Journey - dataset
- Journey - schema
- Offers
- Profile qualification trends
- Step events

Schemas
- Schema counts
- Creation/modification date
- Schema - attribute relationship
- Schema - dataset relationship
- Schema - audience relationship
- Profile enable status
- Name search
- Name and ID search

- Audit
- Creation/modification
- Created by
- Field groups
- Identities
- Identity namespaces
- Labels
- Number of profiles

Schemas (Federated Audience Composition)
- Schema counts
- Schema name/label search
- Creation and modification dates
- Schema-database relationship
- Audience type schemas

- Schema-composition relationship
- Schema properties

Sources
- Account counts
- Account status
- Active/inactive dataflows for each account
- Source connector - dataflow relationship
- Source account - dataflow relationship

- Account credentials information
- Account set up
- Data ingestion metrics
- Number of profiles
- Source - batch relationships

For operational insights questions, answers may not reflect the current state of the UI. The data that backs these questions is updated once every 24 hours. For example, changes that users make in Real-Time CDP during the daytime are synced with the data stores at night, and then they become available for user questions in the morning. You will need to log into a sandbox to inquire about specific data related to objects.

Watch the following video for additional information on AI Assistant (Legacy) operational insights:

https://video.tv.adobe.com/v/3444031?learn=on&enablevpops
https://video.tv.adobe.com/vc/3444031/eng.json
### Feature scope feature-scope

Currently, the scope of AI Assistant (Legacy) is as follows:

- [Product knowledge](/en/docs/experience-platform/ai-assistant/home#product-knowledge): AI Assistant (Legacy) can answer product knowledge questions for Experience Platform, Real-Time Customer Data Platform and Adobe Journey Optimizer. You can also delve into product knowledge topics for Customer Journey Analytics, but only through the Customer Journey Analytics UI.
- [Operational insights](/en/docs/experience-platform/ai-assistant/home#operational-insights): You can ask AI Assistant (Legacy) with questions on operational insights on the following data objects: attributes, audiences, dataflows, datasets, destinations, journeys, schemas, and sources.

## Next steps

Now that you have a general understanding of AI Assistant (Legacy), you can now proceed and use AI Assistant (Legacy) during your workflows. Refer to the following documentation for more information:

- [AI Assistant (Legacy) UI guide](/en/docs/experience-platform/ai-assistant/ui-guide)
- [Feature access](/en/docs/experience-platform/ai-assistant/access)
- [Question guide](/en/docs/experience-platform/ai-assistant/questions)
- [Privacy, Security, and Governance in AI Assistant (Legacy)](/en/docs/experience-platform/ai-assistant/privacy)
- [FAQ](/en/docs/experience-platform/ai-assistant/faq)

recommendation-more-help
