---
title: "Release notes release-notes"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/whats-new/release-notes"
category: "release-notes"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:44.903446+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Release notes release-notes

Last update: May 8, 2026
- Topics:
- [Release Notes](#)

CREATED FOR:

- Beginner
- Intermediate
- User

Adobe Journey Optimizer follows a continuous delivery model, allowing Adobe to deliver new capabilities, enhancements, and fixes on an ongoing basis. This approach enables a scalable, phased rollout of capabilities to ensure performance and stability across all environments.

Because of this model, release notes are updated between monthly releases. For full details about the release cycle and availability phases, see [Journey Optimizer release cycle](/en/docs/journey-optimizer/using/whats-new/releases).

Adobe Journey Optimizer is built natively on Adobe Experience Platform and inherits from its latest innovations and improvements. Learn more about these changes in [Adobe Experience Platform Release Notes](/en/docs/experience-platform/release-notes/latest#_blank).

## May '26 updates may-26-rn

Journey Fragments
You can now create **Journey Fragments** in Adobe Journey Optimizer. Journey Fragments are reusable sets of journey nodes that you can build once and drop into any journey across your sandbox. Whether it's an eligibility check, a preferred channel routing logic, or a welcome sequence, fragments help teams move faster and stay consistent — without rebuilding the same logic from scratch every time.

Once created, fragments are stored in a dedicated **Fragment Inventory** and can be inserted into any journey using the **Journey fragments** activity.

<p><img src="assets/do-not-localize/journey-fragments.gif"></p>
This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-fragments).

Availability date: May 13, 2026

Deeplinks in the Email Designer
It is now possible to add deeplinks to your email contents through a dedicated option in the Email Designer.

This ensures users are taken directly to the right in-app content instead of being redirected to browsers or app stores, preserving context and engagement.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/channels/email/configure-email/deeplinks).

Availability date: May 12, 2026

Journey simulation
You can now set your journey to **Simulation**. This mode allows you to validate your logic using **simulated users**. These are temporary profiles created specifically for the simulation, allowing you to test freely without needing to manage persistent test profiles in Adobe Experience Platform.

This capability is available to all customers as a Limited Availability with essential capabilities.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/simulate-journey).

Availability date: May 5, 2026

Decisioning rules and ranking formula AI optimization
Adobe Journey Optimizer now uses AI to detect Decisioning rules and ranking formulas that can be simplified. In the inventory, a red indicator appears on any rule for which the AI has identified an optimization opportunity. Clicking the indicator displays the original expression alongside the AI-suggested version. From there, you can download a file to review how simulated profiles are evaluated by each version and confirm they behave identically, then replace the expression with the optimized one.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/get-started/essentials/ai-features#decisioning-optimization).

Availability date: May 5, 2026

Integrations
The **Integrations** feature allows you to connect third-party data sources directly to Adobe Journey Optimizer. By simplifying how you pull in external data and **composable content**, this feature makes it easier to deliver personalized, dynamic messaging across all your channels.

Previously released in Beta, this capability is now available to all environments (General Availability).

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/content-management/combine/integrations/integrations).

Availability date: May 4, 2026

### Improvements may-26-improv

#### Decisioning

- Decisioning migration workflow APIs - The API contract for creating dependency analysis and migration workflows has been updated: pass request-level as a query parameter on the request URL ( sandbox , offer , or decision ). Request level must no longer be sent in the JSON body. Read more Availability date: May 6, 2026

#### SMS

- Character Count - In Adobe Journey Optimizer, you can now use the Character Count to monitor the length of your SMS messages in real time. It helps you see when a message will be split into multiple segments to better manage formatting and avoid unexpected increases in sending costs. Read more
- SMS inbounds to a custom dataset - In SMS API credentials , route inbound SMS to a custom, profile-enabled Experience Event dataset you select instead of only the default tracking dataset. Read more
- Webhook interface enhancement - When configuring SMS webhooks, the user interface now includes a built-in setup guide with practical examples, making it easier to align provider payloads and troubleshoot issues without leaving the configuration flow. Read more

#### WhatsApp

- **WhatsApp button support and tracking** - WhatsApp templates now support **Quick reply**, **Call to action – URL**, and **Call to action – phone**, **Copy code** is not supported. Journey Optimizer sends supported buttons and tracks interactions alongside your other channel reporting.

## April '26 release notes april-26-rn

New capabilities and improvements released earlier in April are announced with their availability date.

**Release date**: April 28-29, 2026

### New capabilities april-26-features

Incremental query activity in Orchestrated campaigns
**Orchestrated campaigns** now support an **Incremental query** activity that targets only profiles or events that are newly eligible since the last execution.

This keeps recurring campaigns focused on net-new audiences (new sign-ups, newly qualified loyalty members, and similar segments) while reducing query workloads and avoiding redundant sends over time.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/incremental-query#incremental-query-configuration).

Availability date: April 30, 2026

Sender parameters in email header
With Journey Optimizer, you can now send emails where the transmitting entity (Sender) differs from the authoring entity (From). Email clients that support this will typically render it as "Sender on behalf of From" or show a "via" indicator. Fill in the optional **Sender headers** fields in the email channel settings to configure this capability.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/channels/email/configure-email/header-parameters#sender-header).

CC field in email channel settings
You can now configure an optional CC (carbon copy) field in your email channel settings. Unlike BCC, CC recipients are visible to the primary recipient, enabling transparent communication and clearer ownership.

This allows you to automatically copy the right stakeholder on each message—such as a relationship manager or account owner—while ensuring the customer knows who to contact for follow-up.

The CC field supports personalization, so a single configuration can dynamically route copies based on profile data, making it scalable across multiple use cases without additional setup.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/configuration/cc-email-field).

Copy orchestrated campaigns across sandboxes
Sandbox Tooling now supports packaging and copying orchestrated campaigns from one sandbox to another. This eliminates the need to manually rebuild campaigns in each environment. When a campaign is packaged, its core dependent objects such as merge policies, messages, are automatically included, so the imported campaign arrives ready to configure and validate. To protect production environments, all imported campaigns land in draft status in the target sandbox, giving teams a review and approval step before any campaign goes live.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/connect-systems/sandbox/copy-objects-to-sandbox).

Journey Optimizer AI Agent Integration via MCP
Adobe Journey Optimizer now provides an **MCP (Model Context Protocol) server** that surfaces campaign, channel configuration, and sandbox operations directly inside any MCP-compatible application. With this integration, different personas can collaborate around the same orchestration data. Instead of writing queries against the Adobe Journey Optimizer REST API or navigating multiple UI screens, you can describe your intent conversationally and let the LLM invoke the appropriate MCP tools. This capability is currently available in Claude Web and Desktop.

This capability is available to all customers in Public Beta.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/content-management/combine/ajo-mcp).

Journey Arbitration – AI Models
You can now use **AI models** in your ranking formulas to automatically boost journey priority scores based on customer profile attributes and contextual factors, ensuring customers enter the most relevant journeys.

This capability is only available for a set of organizations (Limited Availability). To gain access, contact your Adobe representative.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/conflict-prioritization/journey-arbitration/journey-ai-models).

Adobe Express integration
The **Adobe Express integration** in Adobe Journey Optimizer lets you use Adobe Express's editing tools directly during content creation, enabling you to resize, remove backgrounds, crop, and convert assets to JPEG or PNG.

Previously released in Limited Availability, this capability is now available to all environments (General Availability).

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/content-management/combine/express).

Availability date: April 23, 2026

Optimize email for AI inboxes
Adobe Journey Optimizer now includes a new capability that ensures your emails are optimally structured for AI-powered inboxes such as Apple Intelligence and Google Gemini in Gmail.

As AI assistants increasingly control how recipients read and act on email, this feature helps you generate and author content that performs well across downstream AI tasks including summarization, triage, prioritization, and intent extraction.

For more information, refer to [Optimize email for AI inboxes](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/llm-email-optimizer).

Availability date: April 17, 2026

AI Assistant for Personalization Expressions
Adobe Journey Optimizer now includes **AI Assistant** directly in the personalization editor and the Email Designer that converts natural-language prompts into valid personalization expressions and conditional logic, no syntax expertise required. Describe the personalization you want to achieve, and AI generates ready-to-use code you can apply immediately or refine through follow-up prompts.

The assistant also works in reverse. Select any existing expression and ask it to explain the logic, identify issues, or suggest improvements. This makes it useful not just for authoring new expressions, but for reviewing and debugging existing ones across your team.

For more information, refer to [AI Assistant for Personalization Expressions](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-personalization-expressions).

Availability date: April 13, 2026

Journey path experimentation
Use the new **Optimize** node to run A/B tests or multi-armed bandit experiments to determine the best path to meet your business-centric KPIs. This tool allows you to test and vary, and customize communications, sequencing, and timing to best reach your customers.

Previously released in Limited Availability, this capability is now available to all environments (General Availability).

As part of the General Availability, this release introduces **experiment type** selection (A/B or multi-armed bandit) and **Scale the winner** for unitary journeys.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/path-experimentation).

Availability date: April 7, 2026

Inbox
**Inbox** is a mobile functionality, available with Content Cards, that enables customers to create a centralized location within their app or website to display messages sent to their users. This extends the lifetime of marketing communications by ensuring messages remain accessible even after they are dismissed.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/channels/inbox/inbox-gs).

Availability date: April 7, 2026

Decisioning support in email channel
You can now use **Decisioning** to personalize and optimize the content of your email messages. Leverage Priority Scores, Formulas, or AI Models to display the most relevant offers and content to each recipient.

Previously released in Limited Availability, this capability is now available to all environments (General Availability). With this General Availability release, mirror pages are now supported.

For more information, refer to the [detailed documentation](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/create-decision-policy).

Availability date: April 6, 2026

### Improvements april-26-improv

#### AI

- Prompt Assistant enhancement - Prompt Assistant enhances AI content generation by analyzing user prompts in real time and identifying gaps in clarity, completeness, and context. It suggests improved rewrites and provides actionable guidance to enrich prompts with key details like audience, tone, and intent. The feature also asks targeted clarifying questions to help users refine their inputs before generation. This results in more accurate, high-quality outputs with fewer iterations. Learn more Availability date: May 5, 2026

#### Push

- **Personalize App id in channel settings** - In the Push channel configuration settings, you can now personalize the **App id** field so that each recipient can receive a push notification from the appropriate brand based on their profile information. [Read more](/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration#app-id-personalization)

#### Decisioning

- Decisioning migration workflow APIs - The API contract for creating dependency analysis and migration workflows has been updated: pass request-level as a query parameter on the request URL ( sandbox , offer , or decision ). Request level must no longer be sent in the JSON body. Read more Availability date: May 6, 2026
- Attach fragments to decision items - Journey Optimizer now provides the ability to attach fragments to decision items which can be leveraged in code-based experience and email campaigns through decision policies. Read more Previously released in Limited Availability, this capability is now available to all environments (General Availability).
- Temporarily unavailable fragments are skipped - When using fragments in decision items, if a fragment is temporarily unavailable on Edge, it is skipped and the journey or campaign continues rendering instead of failing. Read more Availability date: April 14, 2026

#### Adobe Experience Manager Integrations

- Adobe Experience Manager Content fragment Varition Support - You can select Content Fragment variations (for example language or channel variants) when inserting Adobe Experience Manager Content Fragments, with improved handling for locale and multilingual scenarios. Read more Previously released in Limited Availability, this capability is now available to all environments (General Availability).
- Adobe Experience Manager Content Fragment context while authoring - Your Content Fragment selection stays active as you move between text fields and content blocks, so you can add more fragment fields without reopening Open AEM Content advisor each time. Read more Previously released in Limited Availability, this capability is now available to all environments (General Availability).

#### Email design

- Advanced HTML editor for email content - Advanced HTML mode lets you edit the HTML source of your content in the Email Designer, add advanced expressions (such as conditions) in the source, and toggle between HTML view and Desktop view without losing your changes. Previously available for email content templates only, this capability is now deployed to email content in the Email Designer (for example, emails authored in journeys and campaigns), in addition to email content templates. It is currently in Limited Availability — contact your Adobe representative to gain access. Read more Availability date: April 9, 2026

#### Journeys

- Current journey payload size visible in journey properties - The journey properties panel now displays the current size of the journey payload compared to the configured limit — for example, 1.5 MB (out of 4 MB) . This read-only indicator helps you monitor journey complexity before publishing and avoid errors caused by the payload size limit being exceeded. Read more Availability date: April 30, 2026

#### Journey Path Optimization

- Experiment type - You can now choose between A/B experiment (fixed split at the start) or Multi-armed bandit (automatic split with weekly weight updates) when configuring a path experiment. Read more Availability date: April 7, 2026
- Path experimentation: Scale the Winner - You can now automatically or manually roll out the winning path of an experiment to your full audience. Once a winner is determined, you can amplify its reach and effectiveness without constantly monitoring the experiment. Read more This capability is available only in unitary journeys (event-triggered and Audience qualifications). It is not available for Read audience journeys. Availability date: April 7, 2026
- Conditions - The Optimize activity is the new vehicle for creating conditional paths in journeys. It replaces the former Condition activity, which has been removed from the UI. All conditional logic is retained and is now handled through the Optimize activity’s conditions. Read more Previously released in Limited Availability, this capability is now available to all environments (General Availability). Availability date: April 7, 2026

#### Orchestrated campaigns

- **Global variables in Orchestrated Campaigns** - Orchestrated Campaigns now support global variables that can be defined once and reused across all activities within a workflow, simplifying configuration and ensuring consistency in dynamic values, expressions, and content personalization. [Read more](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/orchestrated-advanced/global-variables)
- **Data Modeler enhancements** - Orchestrated relational schemas now support composite keys spanning multiple fields. Loading a schema from a DDL file also brings in enumerations, and loading from either a DDL or Excel file automatically creates composite relationships between tables. In the entity relationship view, composite links now display the full set of field pairings between tables after a file is uploaded. [Read more](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas)

recommendation-more-help
