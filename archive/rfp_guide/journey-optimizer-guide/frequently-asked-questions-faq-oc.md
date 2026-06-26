---
title: "Frequently asked questions faq-oc"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/orchestrated-campaigns-faq"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:12.524309+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Frequently asked questions faq-oc

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

You will find below Frequently Asked Questions about Adobe Journey Optimizer Orchestrated campaigns.

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en#_blank).

What is Campaign orchestration?
Campaign Orchestration is a feature of Journey Optimizer that supports single-step or multi-step workflows that leverage the Relational Datastore to build and segment audiences for the purpose of batch engagement.

It brings a new type of campaigns to Journey Optimizer: **Orchestrated campaigns**. Orchestrated campaigns help brands run complex, one-to-many marketing campaigns at scale. They are designed for brand-initiated engagement, such as promotions, seasonal campaigns, or account-based communications.

Compared with single-send/action campaigns, they bring **orchestration and sequencing** to outbound marketing: audiences move through a multi-step workflow together, rather than receiving a one-off blast.

**Learn more**

- [Get started with Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns)
- [Create your first Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/gs-campaign-creation)

What can I do with an Orchestrated campaign?
Key capabilities include:

- **On-Demand Audiences**: Instantly build and refine target groups using relational queries.
- **Multi-Entity Segmentation**: Create precise audiences by connecting customer data with related entities (e.g., accounts, purchases, bookings).
- **Pre-Send Visibility**: See accurate audience counts before launching to optimize targeting.
- **Multi-Step Workflows**: Run sequenced campaigns such as seasonal promotions, product launches, or loyalty offers.

**Best practices**

- Define a **clear campaign objective** before designing workflows.
- Start with a **pilot audience** to validate counts and logic before scaling.
- Keep segmentation rules **as simple as possible** to optimize performance and transparency.
- Use **consistent naming conventions** for audiences and campaigns to make management easier.

**Learn more**

- [Create an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/create-orchestrated-campaign)
- [Work with campaign activities](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/about-activities)
- [Build your rule using the query modeler](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/build-query)

How to get access Campaign orchestration?
To access Campaign Orchestration, your license must include either the **Journey Optimizer – Campaigns & Journeys** or the **Journey Optimizer - Campaigns** package. Contact your Adobe representative to confirm your license and update if needed.

**Learn more**

- [Get started with Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns)
- [Adobe Journey Optimizer product description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html#_blank)

How are Orchestrated campaigns different from Journeys?
- **Orchestrated campaigns**: Best for **batch, one-to-many** campaigns. Audiences progress in bulk, on a schedule.
- **Journeys**: Best for **real-time, one-to-one** engagement. Each customer moves through the journey at their own pace, triggered by behavior or events.

**Best practice**: Use them together — Journeys for triggered, reactive experiences, and Orchestrated campaigns for planned, calendar-based initiatives.

**Learn more**

- [Get started with Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns)
- [Create your first journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs)
- [Get started with campaigns](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns)

What is multi-entity segmentation?
Campaign Orchestration in Adobe Journey Optimizer uses a relational database. This type of data model has separate schemas of data that are connected via 1:1 or 1:many relationships. This enables users to start a query on any schema – not just at recipient level- and then flip back and forth to other related schemas, such as purchases, products, bookings or recipient details providing great flexibility in how segments and audiences can be created and refined.

**Example** - Target all recipients with subscriptions expiring in the next 30 days. In Campaign Orchestration the query can start with the Subscriptions schema, search just the expiry date column of that schema and return all subscriptions due to expire, then roll up to the recipient data that is related to those specific subscriptions IDs returning results faster and more efficiently than data models that begin each query at the recipient level.

**Learn more**

- [Get started with schemas and datasets](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)
- [Configure a targeting dimension](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/target-dimension)
- [Build your rule using the query modeler](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/build-query)

How does the data model work?
Campaigns use a **relational database**. This allows you to query across different data sets (e.g., customers, products, subscriptions) and connect them flexibly for advanced segmentation.

**Best practices**

- Organize datasets so that **relationships (joins)** reflect business logic.
- Avoid unnecessary joins to keep queries performant.
- Validate sample results before running large-scale extractions.

**Learn more**

- [Get started with schemas and datasets](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)
- [Create a schema manually](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/manual-schema)
- [Ingest data](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/ingest-data)

Can I personalize messages with relational data?
Yes. In Campaign Orchestration a recipient profile known as the ‘People Entity’ can be updated and that data used for personalization. Additionally, enriched data from linked entities in the relational database can also be used for personalization. You can use customer profiles along with linked data (like purchases or subscriptions) to personalize content across all supported channels.

**Recommendations**

- Use **transactional and behavioral data** to make offers relevant.
- Combine **static attributes** (e.g., loyalty tier) with **dynamic ones** (e.g., last purchase date).
- Keep personalization concise—overloading messages with data can harm readability.

**Learn more**

- [Use the Enrichment activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/enrichment)
- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)

How do I test a signal-triggered orchestrated campaign before publishing?
While the campaign is in
Draft
, you can test it by defining
parameters
in the schedule and providing
test values
for each. Start the workflow, then call the trigger API (using the sample request from the schedule configuration or your own request with the same endpoint) to run the campaign with those test values.
Learn how to complete and test a signal-triggered campaign
.
Can I revert a live orchestrated campaign back to draft?
Yes, in specific situations. The **Back to draft** option is designed as a recovery mechanism to unpublish and revert a campaign to draft status.

This option is available for scheduled campaigns awaiting execution, or for live campaigns with execution errors. [Learn how to revert a live campaign back to draft](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/start-monitor-campaigns#back-to-draft)

What happens internally when I publish an Orchestrated campaign?
When you click **Publish**, the following sequence occurs:

- **Scheduler activation** — If a schedule is configured, the scheduler kicks in and triggers execution at the defined time.
- **Save Audience activities run first** — Any Save audience activities execute before message activities. The audience shell is created in the Audience Portal and qualified profiles begin ingesting.
- **Message execution begins** — Channel activities start processing for the first message activity in the workflow.
- **Profile snapshot lookup** — Profile data is resolved against a snapshot taken at publication time, not the real-time profile, ensuring consistency across the entire execution.
- **Consent evaluation** — Consent is honored directly from the profile record and is not re-evaluated at send time.
- **Profile reconciliation** — Recipients are reconciled against Adobe Experience Platform Profiles at send time.
- **Delivery log creation** — Delivery events are recorded in the ajo_message_feedback_event dataset.

**Learn more**

- [Publication-time execution sequence](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/start-monitor-campaigns#publication-sequence)
- [Start and monitor your Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/start-monitor-campaigns)

Why are my messages not sending after I publish the campaign?
Several situations can prevent messages from being sent after publication. Check the following in order:

- Sending confirmation pending (most common) — For non-recurring campaigns, message delivery is paused by default until you explicitly confirm the send from the channel activity’s properties pane. The campaign shows as Live but no messages go out until confirmed. Learn more
- Campaign is scheduled for a future time — If a schedule is configured, the campaign is Live but execution has not started yet. Check the schedule settings and wait for the configured start time. Learn more
- Save Audience activities still ingesting — Save Audience activities run before message activities at publication time. If audience ingestion is still in progress, message execution has not started yet. Monitor the activity status indicators in the canvas. Learn more
- Audience is empty — The targeting query returned zero profiles. Review your segmentation rules and validate the audience count before republishing.
- All profiles opted out — Consent is evaluated at send time against each profile. If all targeted profiles have opted out on the relevant channel, no messages are sent. Learn more
- Channel activity in error state — An orange or red status indicator on the channel activity signals a blocking issue. Open the Logs for details on the error and how to resolve it. Learn more
- Rate control throttling delivery — If rate control is enabled on the channel activity, delivery may be slower than expected. Check the rate control settings in the channel activity properties pane. Learn more

**Learn more**

- [Start and monitor your Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/start-monitor-campaigns)
- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)

Does publication use the real-time profile or a snapshot?
At publication time, profile data is resolved against a **snapshot taken at publication time**, not the real-time profile. This ensures consistency across the entire campaign execution — all activities process the same profile state regardless of how long the campaign runs.

Consent, however, is always honored from the current profile record and is not re-evaluated at send time.

Note that segmentation in Orchestrated campaigns is performed on Recipients (relational store), while message sending and consent checks are resolved against the Adobe Experience Platform Profile.

**Learn more**

- [Publication-time execution sequence](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/start-monitor-campaigns#publication-sequence)
- [What is the relationship between Recipient and Profile Entities?](#faq-oc)
- [Work with consent policies](/en/docs/journey-optimizer/using/privacy/consent/consent)

Which channels are supported?
You can create Orchestrated campaigns to send **emails**, **SMS**, **push notifications** and **direct mails**.

**Learn more**

- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)
- [Work with campaign activities](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/about-activities)

Can multiple communications and different channels be launched within the same Orchestrated campaign?
Yes, Orchestrated campaigns supports cross-channel orchestration. You can combine email, SMS, push notification, and direct mail activities into a multi-step campaign canvas to create comprehensive customer experiences.

**Learn more**

- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)
- [Work with campaign activities](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/about-activities)

Are Orchestrated campaign templates available?
No, you cannot define or use campaign templates, but you can use content templates for your communications.

**Learn more**

- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)
- [Create an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/create-orchestrated-campaign)

Is the content designer for messages specific to Orchestrated campaigns?
No, the content designer, including the Email Designer, is common across all Journey Optimizer capabilities.

**Learn more**

- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)
- [Use the Enrichment activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/enrichment)

How are the different channels connected in Orchestrated campaigns?
The channel component & runtime are common to all Journey Optimizer campaigns, however, supported channels differ. Orchestrated campaigns support email, SMS, push notifications, and direct mail.

**Learn more**

- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)
- [Guardrails and limitations](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails)

Can Orchestrated campaigns connect with outbound channels (web, inApp)?
No, inbound channels like web and in-app are not supported in Orchestrated campaigns. Only outbound channels (email, SMS, push notifications, and direct mail) are supported.

**Learn more**

- [Guardrails and limitations](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails)
- [Add a channel activity in an Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels)

What about permissions and consent?
Permissions and consent for Orchestrated campaigns and journeys are managed centrally in Adobe Experience Platform. These settings are applied across both solutions for each recipient prior to send.

**Best practices**

- Apply **centralized governance**—avoid managing consent separately at campaign level.
- Periodically audit consent data to detect inconsistencies.
- Respect **channel-specific opt-outs** — do not assume global consent covers all channels.

**Learn more**

- [Get started with Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns)
- [Guardrails and limitations](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails)

Can I do ad-hoc segmentation in Orchestrated campaigns?
In Campaign Orchestration, we refer to ad-hoc segmentation as ‘Live segmentation’ where you can access all the data available in the relational store in real time, build a complex query on top of it and get the result for instant activation through outbound channels (ex: Email + SMS).

**Tips**

- Use ad-hoc segmentation for **time-sensitive needs** (e.g., flash promotions).
- Save and document useful queries so they can be reused in future campaigns.
- Validate the audience count before activation to prevent under- or over-sending.

**Learn more**

- [Build your rule using the query modeler](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/build-query)
- [Use the Build audience activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/build-audience)
- [Configure a targeting dimension](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/target-dimension)

Does Campaign Orchestration only access data loaded via batch, or can it also query real-time updated tables (such as Analytics data)?
Journey Optimizer Campaign Orchestration can build ad-hoc queries on top of relational Schemas. Relational Schemas support Batch Sources only for now. In addition, it supports Read audience activities from any type of Adobe Experience Platform Audience.

**Learn more**

- [Get started with schemas and datasets](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)
- [Ingest data](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/ingest-data)
- [Use the Read audience activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/read-audience)

Do Orchestrated campaigns support decisioning?
No, Orchestrated campaigns do not support decisioning capabilities. For decisioning features, use standard Journey Optimizer journeys or action campaigns instead.

**Learn more**

- [Get started with Experience Decisioning](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/gs-experience-decisioning)
- [Create your first journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs)
- [Get started with campaigns](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns)

How does deployment across environments work?
Objects created in Orchestrated campaigns (for example, audiences and workflows) belong to the sandbox where they were created. To reuse an orchestrated campaign in another sandbox (for example, dev, stage, or production), copy it with **Sandbox tooling**: add the campaign to a package, publish the package, and import it into the target sandbox. The imported copy is created in **draft**, and **re-importing the same package creates a new campaign** rather than updating an existing one. A complete move often takes **more than one step**: you may need to align **channel configurations** (matching names in the target), **schemas**, and **datasets** through the same package or additional package imports—channel configurations are not copied with the campaign. There is no full pre-export checklist in the UI; use the import mapping flow and **post-import alerts** to finish setup. For details and limitations, see [Copy Journey Optimizer objects between sandboxes](/en/docs/journey-optimizer/using/connect-systems/sandbox/copy-objects-to-sandbox).

**Best practices**

- Maintain **separate sandboxes** for experimentation, QA, and production.
- After each import, validate the campaign end to end in the target sandbox before you publish.
- Document configurations and align with governance teams to reduce configuration drift between environments.

**Learn more**

- [Copy Journey Optimizer objects between sandboxes](/en/docs/journey-optimizer/using/connect-systems/sandbox/copy-objects-to-sandbox)
- [Get started with Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns)
- [Guardrails and limitations](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails)

What is the relationship between Recipient and Profile Entities?
Segmentation is performed on Recipients while sending against the Adobe Experience Platform Profile. The Recipient target dimension extends the unified Profile with additional data that is used for segmentation within Orchestrated campaigns, while Recipient is reconciled with Profile at runtime for sending messages and check the consent policy and business rules. This reconciliation is useful for unifying business rules and consent application at profile level.

**Learn more**

- [Configure a targeting dimension](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/target-dimension)
- [Get started with schemas and datasets](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)
- [Build your rule using the query modeler](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/build-query)

In which cases is it recommended to use Recipient vs. Profile Entities?
Answering ‘Yes’ suggests the best data store - but always confirm the best approach based on your use case and constraints with your Adobe representative.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| Relational Store | Real-Time Customer Profile |
| Is the source the data relational already? | Is the source of the data streaming? |
| Do you plan to ingest data as-it for marketing use cases? | Is data freshness a major requirement? |
| Is there a large volume of historical data (> 2 months) that is needed for marketing activation use cases? | Are there scenarios where in-the-moment action or decision require data? |
| Are there ad-hoc needs for audience creation, evaluation, and activation? | Can the behavioral data be limited to < 90 days using pre-computed aggregates? |
|  | Is data needed for personalizing messages in real-time? |

**Learn more**

- [Configure a targeting dimension](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/target-dimension)
- [Get started with schemas and datasets](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)
- [Build your rule using the query modeler](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/build-query)

What is the maximum number of activities per Orchestrated campaign?
The number of activities in an Orchestrated campaign is limited to 500.

**Learn more**

- [Guardrails and limitations](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails)
- [Work with campaign activities](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/about-activities)

Is it possible to perform enrichments to add additional data?
Yes, you can enrich data from the relational store and from Adobe Experience Platform audiences. Use the Enrichment activity to enhance your audience data with additional attributes from related schemas.

**Learn more**

- [Use the Enrichment activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/enrichment)
- [Use the Reconciliation activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/reconciliation)

Must all filters be defined via audiences, or can some type of filter be configured?
Orchestrated campaigns support predefined filters: you can define and save a query as a filter, add it to your favorites, and reuse it in further segmentation tasks. Predefined filters can include parameters so you can enter values at time of use. [Learn how to work with predefined filters](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/predefined-filters).

**Learn more**

- [Build your rule using the query modeler](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/build-query)
- [Use the Build audience activity](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/build-audience)
- [Work with predefined filters](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/query-database/orchestrated-rule-builder)

## Additional Resources

For more learning and updates, explore the following resources:

- [Orchestrated campaigns guardrails & limitations](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/guardrails)
- [Get started with schemas and datasets in Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)
- [Create your first Orchestrated campaign](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/gs-campaign-creation)
- [Journey Optimizer Product Description](https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html#_blank)

recommendation-more-help
