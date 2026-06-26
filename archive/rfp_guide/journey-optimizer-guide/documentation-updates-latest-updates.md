---
title: "Documentation updates latest-updates"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/whats-new/documentation-updates"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:20.870449+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Documentation updates latest-updates

Last update: May 8, 2026
- Topics:
- [Release Notes](#)

CREATED FOR:

- Beginner
- Intermediate
- User

This page lists all the latest changes in Journey Optimizer documentation, in addition to the updates related to the Monthly release features and improvements.

## May 2026 may-2026

- The Get started with datasets page has been updated with a new Inbound entry in the system datasets section, documenting the AJO Inbound Activity Event Dataset . A note has been added to clarify that a profile must have at least one message sent from Journey Optimizer before incoming messages are captured in this dataset. Read more
- The Export message content documentation has been expanded with a Message Export FAQ (personalized content, images and media, tracked links, PII, retention, use cases, etc.), and sample exported JSON examples for SMS and email. Read more
- A new AJO Message Export schema page documents every field in the AJO Message Export Dataset, with data types and hierarchy for the exported email and SMS payload. Read more
- A new Personalize URLs in emails page has been added, consolidating guidance on dynamic URL personalization, complete/base URL personalization, URL tracking parameter personalization, and key guardrails. Read more
- A new Business rules queries section has been added to the query examples page, providing a Data Lake query to check all profile discards due to journey frequency capping exclusions on a specific journey after a specific date. The query includes the eventCodeReason field to identify whether profiles were excluded because a cap was reached ( CAP_REACHED ) or due to a lower priority ( LOWER_PRIORITY ). Read more
- The Journey properties documentation has been updated to document the new Current journey payload size indicator in the journey properties panel. This read-only field shows the current size of the journey payload compared to the configured limit (e.g. 1.5 MB out of 2 MB), helping you monitor journey complexity before publishing and avoid size-related publication errors. Read more

## April 2026 april-2026

- The Change dimension activity documentation has been updated to clarify that while the activity uses an external join and keeps all records at the dimension-change step, records without a matching profile in the new targeting dimension are silently excluded at message delivery time. Read more
- The guardrails in the Add a CC field to emails documentation have been enhanced. They now specify that the CC address is not checked against consent or suppression, and that opens and click-throughs from emails sent to the CC address are taken into account in the total opens and clicks from the send analysis. Read more
- The Channel activities documentation has been updated with a new Marketing vs Transactional messages section explaining the behavioral differences between the two channel categories: opt-in requirements, business rule application, channel configuration type, and recommended use cases. Read more
- The Fork activity documentation has been enriched with a new Examples section illustrating how to use the Fork activity to split an audience across two parallel email branches — one Marketing and one Transactional — in a single campaign run. Read more
- The Build audience activity documentation has been enriched with a new example showing how to filter profiles by a subscription plan attribute using the rule builder. Read more
- The Get started with Orchestrated campaigns page documents the entry-level Build audience → Fork → Channel A + Channel B pattern in What’s inside an Orchestrated campaign? , with cross-references to the Fork activity and Marketing vs Transactional messages pages. Read more
- The Edit email content with the advanced HTML editor page has been moved from the Content management section to the Email section of the documentation. The page now documents that the advanced HTML editor is available in the Email Designer for email messages as well as for email content templates. Read more
- The Start and monitor Orchestrated campaigns documentation has been updated with a new section detailing the internal publication-time execution sequence, along with a campaign lifecycle status table, a pre-publication checklist, and a sending confirmation warning for non-recurring campaigns. Read more
- The Save audience activity documentation has been updated with a note clarifying that Save Audience activities always execute before message activities at publication time. Read more
- Three new Q&As have been added to the Orchestrated campaigns FAQ : what happens internally at publication time, a 7-point checklist of reasons why messages may not send after publishing, and how profile snapshot lookup differs from real-time profile resolution. Read more
- A new Events discarded due to a blocked journey instance section has been added to the journey troubleshooting documentation, explaining the maxInstanceStackEventsReached discard reason, when it occurs, and how to mitigate it. The guardrails and step event field list pages have also been updated accordingly.
- The Leverage fragments in decision policies documentation now includes guardrail notes for the Email channel: Simulate content does not display expression fragments from the decision item, while Send proof and activated campaigns do. The page also states that Visual fragments cannot be assigned to a decision item — only expression fragments are supported in this context. Read more

## March 2026 march-2026

- Documentation for previewing code-based experiences with Experience Decisioning now clarifies that Simulate content is content preview only. Context data from live Edge requests is not simulated in authoring preview. Read more
- The Use Adobe Experience Platform data documentation has been updated: the guardrails no longer state that dataset lookups cannot be chained, reflecting current product behavior. Read more
- The Update Profile activity documentation has been updated to document support for updating up to five profile attributes in a single action. Read more
- The Read Audience activity and Journey properties documentation have been updated to clarify the 91-day journey lifecycle for always-on recurring journeys. The schedule section now explicitly confirms that recurring journeys with no end date remain Live past 91 days, and the global timeout FAQ has been expanded to distinguish the 91-day profile TTL from the 91-day reporting window. Read more
- The Dataset lookup activity documentation has been updated to clarify that the lookup key must be configured in advanced mode for the @datasetLookup{} syntax to work in downstream condition activities. A troubleshooting section has been added with guidance on resolving the “Dataset lookup not found” error. Read more
- The Date Time functions documentation has been updated with a new example showing how to format a timestamp from a context event attribute, including the toDateTime() requirement, backtick syntax for numeric event IDs, and a common error callout for the PQL “mismatched input” error. Read more
- The Orchestrated campaigns guardrails and limitations and Get started with Sources connectors documentation have been updated to clarify that for file-based Change Data Capture, the _change_request_type field is required and its values must be lowercase u (upsert) or d (delete), not uppercase. Read more
- The Add links & track messages documentation has been updated with guidance on how tracking identifiers (urlID) are generated: a unique urlID is only assigned when both the URL and the label are unique. To track the same URL across multiple emails (or multiple times in one email), users must use a unique label for each similar URL; otherwise, Journey Optimizer cannot determine which link was clicked. Read more
- The Create test profiles documentation has been updated with an important note about identity descriptor requirements: when a dataset is deleted and recreated, the schema must retain the correct identity descriptor on the primary identity field. Without it, ingested profiles will not be flagged as testProfile = true even if ingestion completes successfully. A troubleshooting checklist has been added. Read more
- The Read Audience activity documentation has been updated to clarify that a Business Event activity is an exception to the rule that Read Audience must be the first activity in a journey. A note has also been added referencing the Optimize activity as an advanced alternative for controlling audience targeting. Read more
- Send using waves in journeys is now generally available. The Limited Availability flag has been removed from the documentation. Read more
- The Jump activity documentation has been enriched with a new design strategy section — Bite-sized sub-journeys — explaining how to break complex end-to-end flows into smaller, focused sub-journeys connected via the Jump activity. Read more
- The Tags documentation has been updated with guidance on using tag categories as an alternative to complex naming conventions. A new section explains how to set up tag categories for scalable journey management. Read more
- The About data sources documentation now includes a new section helping practitioners choose between three data access strategies: accessing external data via custom actions, using a dataset not enabled for Profile, or using a profile-enabled dataset. Each option is described with trade-offs and recommended use cases. Read more
- The Push notification design documentation has been updated with a note clarifying the behavior of universal links on iOS: if the notification URL is registered as a universal link, the associated app will open regardless of the chosen Web URL action. Guidance has been added on how to force a browser open. Read more
- A new Monitor your AI models page is now available in the Decisioning documentation. It explains how to track the health, training status, and performance of personalized optimization models directly in Journey Optimizer. Read more
- The advanced HTML editor (expert mode) for email templates is now available in Limited Availability. The documentation page is now publicly accessible. This capability lets you view and edit the raw HTML source of email content templates directly from the Email Designer. Read more
- The URL tracking and Journey troubleshooting documentation have been updated to document the behavior of context.system.source.actionId in closed journeys. Closed or un-republished journeys may produce empty {} placeholders in tracking URLs. Guidance has been added on how to resolve the issue by republishing the journey or removing the affected parameter. Read more
- The Adobe Experience Platform data source documentation has been updated with a note that only XDM Individual Profile-based schemas are supported in the Data Source configuration. Read more
- The Datasets Time-to-live (TTL) guardrails documentation has been enhanced with a new FAQ entry to clearly identify which datasets are subject to TTL. TTL applies exclusively to time-series datasets — record-type datasets such as entity datasets, classification datasets, and decision object repositories are not subject to TTL and will not be impacted by the guardrail rollout. Read more
- The Journey properties and Pause a journey documentation have been updated to document the new pause and resume fields now available in the journey technical details. The Copy technical details button now includes lastPausedAt , lastPausedBy , lastPausedById , lastResumedAt , lastResumedBy , and lastResumedById , in addition to the existing pausedJourneySettings block. A new section has also been added to the Pause a journey page explaining how to view pause and resume timestamps directly from journey properties. Read more

## February 2026 february-2026

- A new page is now available for Decision management. It lists all operators, helpers, and functions supported when personalizing offer content (representations) with the personalization editor. Use this list to avoid runtime errors. Only the documented functions are supported when personalizing content in Offer Decisioning. Read more
- The Create decision policies and Use decision policies in messages documentation has been updated for Email: a note now explains that when the same offer can be selected by more than one decision policy in the email body, the engine deduplicates offers (each placement receives a different offer). To display the same offer in multiple placements (for example, header and footer), use Reuse decision output . Read more
- The Decision items page has been updated with information on Push channel and Custom event capping. Read more
- The Experience event lookup in journeys documentation has been updated with the deprecation timeline: starting April 1, 2026, organizations that have not used experience event attributes in journey expressions in the last 90 days will no longer have access to this capability. The FAQ now focuses on the retirement timeline and who is impacted, and the Experience event schema page has been aligned with a direct link to alternative approaches. Read more
- The Decisioning documentation has been updated for dataset lookup with Adobe Experience Platform data: the supported channels guardrail now states that dataset lookup works for all channels where Decisioning is available (code-based experience, Email, Push, SMS, and the Content Decision activity in journeys). Limited Availability and public beta notes have been removed from the decision rules, ranking formulas, and decision items pages. Read more
- The External systems integration page has been updated with links to custom data sources and custom actions, and clarifies that the egress proxy provides a static IP for outbound calls from Custom actions to your external systems. Read more
- The Journey Dry run documentation has been clarified: the step event attributes inDryRun and dryRunID now document that they return true /instance ID when in Dry run mode and null for test or live journeys. Guidance for excluding Dry run step events in reporting queries has been updated accordingly. Read more
- Web push is now generally available. The push notification documentation has been restructured and updated accordingly (get started, design, send, create). Read more
- The Web push configuration page is now available in the documentation. Read more
- Documentation on using fragments in Decisioning has been updated: notes have been added in the Fragments and Decisioning sections, and the Fragments in decision policies page has been updated. Read more
- The SMS webhook documentation has been updated: Twilio webhook content has been removed. Read more
- The Convert images to content templates documentation has been enhanced with expanded guardrails and recommendations, common use cases, and clearer guidance for converting image designs into editable HTML content templates. It also mentions the fact that you can now use a theme as input for the conversion. Read more
- The Decisioning migration API documentation has been updated. Read more
- The Content Decision activity is now generally available. The Content Decision activity page has been updated with a section on Decisioning data available in step events. Read more
- Links to the loyalty challenge API documentation have been added to the Loyalty challenges section (get started, create challenges, create tasks, access loyalty challenges). Read more
- The supported channels information in the campaign creation wizard documentation has been corrected. The Get started with channels and Orchestrated campaigns FAQ pages have been updated accordingly. Read more
- The permissions documentation has been corrected regarding Journey Manage and Approve permissions. Read more
- The AEM (Adobe Experience Manager) integrations documentation has been updated with revised naming (AEM dynamic content and AEM fragments). Read more
- A new exclusion reason has been added to the exclusions list: UnsubscribeLinkNotValid (error code 050081). This exclusion is generated when the List-Unsubscribe mailTo subject length is greater than the RFC limit of 998 characters. Read more
- The formatDate helper function documentation has been enhanced with a note that the function requires a date-time field type (not a string) and with multiple examples: formatting a date-time field, converting a string to date first, full date with day name, dynamic date from system time, and day-of-week format including lowercase output. Read more
- The text version email documentation has been enhanced with comprehensive use case guidance, including decision criteria for when to use custom plain text versus auto-sync, practical examples with real-world scenarios, and an FAQ section with common questions. Read more
- The Email Designer themes documentation has been updated with information about web fonts support limitations and the importance of fallback fonts. Read more
- A limitation has been added to the Execution Metadata helper documentation to clarify that metadata is not captured for profiles excluded from the action. Read more
- The code-based implementation samples documentation has been updated to include the tokens field in the propositionAction for accurate tracking and attribution in Decisioning. Read more
- A note has been added to the URL tracking and List unsubscribe documentation to clarify that the order of URL tracking parameters appended to URLs is random and cannot be controlled. Read more

## January 2026 january-2026

- The License usage dashboard documentation has been clarified with updated guidance about Engageable Profiles , including definition details and troubleshooting guidance. Read more
- A note has been added to the Email Designer themes documentation to clarify web fonts support limitations. Read more
- A new guardrail section has been added to document journey payload size validation, including warning and error thresholds and guidance on how to optimize journeys. Read more
- The Decisioning guardrails documentation has been updated to include decision items size limitations (1KB for items including attributes with max of 30 attributes). Read more
- A note has been added to the decision policy creation documentation to inform users that once a decision policy is created, any changes can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. Read more
- A note has been added to the fragments documentation to warn that when both the button label and URL are made editable in a fragment, the tracking dataset logs the URL value instead of the label value. Read more
- A new page is now available describing the benefits of migrating from Decision management to Decisioning, including information about upcoming migration tooling APIs. Read more
- Added a guardrail to clarify that lookup datasets are available for inbound edge-based activation only in the region where the dataset’s sandbox resides. Read more
- A new section has been added to the Orchestrated campaigns channel configuration documentation explaining how to use contextual attributes (such as campaign ID, name, and action details) in URL tracking parameters for analytics and reporting purposes. Read more
- The Content optimization documentation has been restructured for better clarity. The main optimization page has been split into four focused subpages: an get started page, a dedicated page for targeting, one for experimentation, and another for combining both approaches. Read more
- The Limited Availability notes have been removed from three journey alerts (Journey Published, Journey Finished, and Custom Action Capping Triggered) as these features are now generally available. Read more
- The Test, validate & approve landing page has been enhanced with new sections including testing capabilities overview, common questions FAQ, decision tree with navigation links, and enhanced terminology with documentation links. Read more
- A new section has been added to the personalization syntax documentation to clarify how to use reserved keywords in personalization expressions. Certain PQL keywords such as next , last , and this must be escaped with backticks when used as field names in your XDM schema. Read more
- The Get started with campaigns and Manage campaigns pages have been restructured with improved information architecture, including a comprehensive workflow with type-specific guides, enhanced campaign type comparisons, and consolidated status table.
- The Journeys landing page has been redesigned to facilitate onboarding with a new 6-step workflow, enhanced journey type comparisons, and improved navigation throughout the documentation. Read more
- A detailed section has been added to help users generate Base64-encoded OpenSSH private keys for SFTP authentication when configuring file routing for Direct Mail to avoid connection errors. Read more
- A note has been added to the subdomain delegation documentation to inform users to allow 24-48 hours for DNS propagation before attempting delegation to Adobe. Read more

## December 2025 december-2025

- The Custom upload audiences for decisioning documentation has been updated to include a required API flag for retrieving enrichment data. When using CSV-uploaded audiences in offer decisioning, you must include "xdm:enrichedAudience": true in your API request payload to retrieve enrichment attributes in the offer decision response. Read more
- A note has been added in the proof sending documentation to clarify that frequency capping rules apply to proofs. The page now includes a “Must-read” section with important considerations about frequency capping behavior, mirror page limitations, and asset accessibility rules. Read more
- A new communication channels availability table has been added to the Get started with channels page, showing which channels are supported across journeys and campaigns (Action campaigns, API-triggered campaigns, and Orchestrated campaigns). Read more
- A new comprehensive tracking landing page has been created to help users discover and access all tracking and monitoring capabilities available in Journey Optimizer. Read more
- The Email opt-out management page has been enhanced with detailed information about the unsubscribe flow, explaining the expected order of events for landing page opt-out. Read more
- The Subscription list documentation has been updated to include information about streaming segment eligibility criteria. Read more
- A new IP warmup deliverability guide is available, providing comprehensive guidance on reputation fundamentals, pre-flight preparation, monitoring metrics, and best practices for transitioning from zero reputation to successful inbox placement. Read more
- A warning has been added to the Landing page and Email opt-out sections to clarify that clicking an unsubscribe link only opens the landing page, but users must submit the form to complete the opt-out process. Read more
- A new journey use cases library is now available, bringing together a collection of practical use cases including tactical patterns (suppression logic, personalization techniques, journey exit strategies) and complete end-to-end scenarios covering marketing and technical workflows. Read more
- A new use case is now available demonstrating how to configure a journey to send emails only on weekdays (Monday-Friday), with automatic queuing for weekend entries to be sent on Monday at a specified time. Read more
- A new page is now available explaining Journey Optimizer’s decision capabilities, including the differences between the next-generation Decisioning framework and the established Decision management solution, and their key benefits for delivering personalized offers across channels. Read more
- A new section has been added to the Audience activation documentation explaining how to activate non-supported audience types (such as Customer Journey Analytics audiences) in Journey Optimizer by wrapping them in a new segment definition in the Audience portal. Read more
- A new section has been added to the Wait activity documentation explaining how profiles parked at a Wait activity in Read Audience journeys automatically refresh their attributes from the Unified Profile Service (UPS). This clarifies that profile data may change during journey execution after a wait node, which can produce unexpected results if you expect consistent snapshot data throughout the journey. Read more
- A caution note has been added to the Path Experimentation section warning users not to edit the metadata of a path experiment once it has been published, as this will disrupt the calculation and reporting of experiment results. Read more
- A note has been added to the Create a form preset section to specify the requirements for streaming connections to display in the selection drop-down list. Read more
- A new page is now available in the Decisioning section on how to configure data collection for tracking impressions, clicks, and custom events. Read more
- The Content generation with AI assistant documentation has been reorganized for improved clarity and usability. The previous five channel-specific pages (Email, Push, SMS, Web, and Landing Page) have been consolidated into three generation-type pages: Generate full content , Generate text , and Generate images .

## November 2025 november-2025

- A new Decisioning FAQ page is now available, covering topics such as capping rules, AI model configuration, traffic requirements, and offer optimization strategies. Read more
- The Get started with email design page has been updated to clarify how to access the Email Designer. Read more
- A troubleshooting section has been added to the DMARC record page to address DNS propagation latency. Read more
- The Work with GenStudio for Performance Marketing page has been improved with new sections including key capabilities, common use cases, prerequisites, and frequently asked questions. Read more
- A guardrail on targeting pseudonymous profiles with inbound channels has been added to the Guardrails and limitations page: targeting unauthenticated visitors increases your total engageable profile count, so Adobe recommends setting a Time-To-Live (TTL) for automatic profile deletion to manage the associated costs. Read more
- Two tutorials about configuring the Web SDK for decisioning and code-based experiences are now referenced on the Code-based implementation methods samples page. Read more
- A note has been added to specify that assets and images remain accessible for up to 2 years (730 days) from first publication and require re-publishing after expiry. Read more
- A comprehensive AI Assistant content prompting guide is now available. This guide teaches you how to craft effective prompts to create high-converting, brand-aligned marketing content. Learn best practices for writing marketing objectives, using brand assets, and optimizing content for different channels. Read more
- A note has been added to the segment definition documentation to clarify that the frequencyMap attribute is not supported for use in segment definitions and cannot be used as part of audience segmentation criteria. For frequency-based targeting, consider using frequency capping rules under business rules. Read more
- A new example showing how to use custom action responses in native channels has been added to the API call responses documentation. The example demonstrates how to iterate over nested arrays from custom action responses using Handlebars syntax in email, push, and SMS messages. Read more
- A new section has been added to the Campaign v7/v8 integration documentation explaining how to update existing custom actions when the Real-Time (RT) endpoint changes. The section includes step-by-step instructions for updating the endpoint URL, testing the connection, and validating changes before saving. Read more
- New limitations and best practices sections have been added to the visual fragments documentation to warn users about unsupported nesting of fragments containing Dynamic Content inside other unlocked fragments with Dynamic Content. The guidance includes troubleshooting steps for compatibility mode issues and recommendations for proper email structure design. Read more
- A troubleshooting section has been added to the journey live reporting documentation to help users resolve missing reporting data issues. The section covers journey name synchronization with reporting datasets, data refresh timing, access permissions verification, and journey status requirements. Read more
- Three new FAQ items have been added to the assets documentation explaining asset expiration and lifecycle management. Topics covered include the Time-To-Live (TTL) policy for AEM assets (730 days), how to resolve broken images due to asset expiration, and information about upcoming improvements to asset expiration logic. Read more
- A comprehensive troubleshooting section has been added to the Read Audience activity documentation to address audience count mismatches between estimated and actual profiles entering journeys. The section covers timing and data propagation issues, data validation and monitoring techniques, and best practices including the use of the “Trigger after batch audience evaluation” option. Read more
- A note has been added to the Audience Qualification events documentation to clarify streaming segmentation latency (up to 2 hours) and recommend adding a Wait activity or buffer time for time-sensitive journeys. Read more
- A new section has been added to the email guardrails documenting the 2MB message content size limit for journey publication, including best practices to keep authored content under 1MB to allow for backend processing overhead. Read more
- Enhanced documentation for the Incremental read option in Read Audience activities to clarify snapshot timing dependencies and the 24-hour look-back limitation, including recommendations to prevent missing profiles. Read more
- A note was added to the dataset lookup guardrails to specify that lookups cannot be chained together. Read more
- WhatsApp and LINE channels are now available for Action campaigns. Read more
- A comprehensive new section on journey processing rate has been added to the entry management documentation, covering profile entrance rates, events and audience qualifications inside journeys, wait activities impact, and action activities impact. Read more
- When designing email messages, the system now checks for key settings and displays alerts for warnings and errors. Information about email alerts and validation requirements has been added to the Guardrails page. Read more
- The caution note stating that frequency capping cannot be enabled or disabled for previously created offers has been removed from the Add constraints to an offer page. Read more
- Documentation on how to work with journey step events is now available. Read more
- A new comprehensive guide on journey entry and exit criteria is now available, covering best practices, real-world examples, and practical guidance for managing when profiles enter and exit journeys in Adobe Journey Optimizer. Read more
- A new page explaining how to iterate over contextual data in messages is now available. This guide covers how to use Handlebars syntax to display dynamic lists from events, custom action responses, dataset lookups, and other context sources in your personalization. Read more
- The query for identifying discarded events in journeys has been corrected to include proper filters for segment export job errors, dispatcher discards, and state machine discards. Read more
- Introductory sentences have been added to all 37 query examples in the query examples documentation to provide better context and explain what each query does before presenting the SQL code. This improves user understanding and provides clearer guidance on when to use each query. Read more

## October 2025 october-2025

- You can now convert images to HTML templates using the image to HTML converter. Read more
- Information about the Adobe Journey Optimizer release cycle is now available. Read more
- A new Journeys Frequently Asked Questions page is now available. Read more
- Monitor your custom actions functionality is now available. Read more
- High throughput mode for API triggered campaigns is now available. Read more
- An error codes reference for journeys is now available. Read more
- Journey Optimizer Experimentation Accelerator documentation is now available. Read more
- A new section has been added to the formatDate helper function documentation. This section clarifies the meaning of key pattern symbols such as y, Y, M, d, and D. Read more
- A PQL example was added to the Decisioning ranking formula section, to show on how to boost offers based on a profile’s ZIP code and annual income. Read more
- A limitation was added to the journey test mode section to mention that the test mode does not support custom upload audience attribute enrichment. Read more
- A new section was added to the Decision management guardrails & limitations and Decisioning guardrails & limitations pages to specify the maximum number of supported configurations (20,000), corresponding to the total number of capping rules that exist in your sandbox.
- Added a note in the journey’s Condition activity section to document that condition evaluation will fail for profiles containing more than two cross-device identities. Read more
- A new page was added to describe how you can use consent policies to honor your customers’ preferences based on their choices, while respecting their consent. Read more
- A note has been added to the Get started with profiles and Guardrails pages to specify that when ingesting data, emails are case-sensitive, meaning that duplicate profiles may be created and used when targeting the corresponding recipient. Read more
- A new render attribute was introduced in the personalization editor. Set it to false in cases you want to hide the content of an expression fragment. Read more
- A list of guardrails was added to the section describing how to leverage fragments attached to decision items within decision policies. Read more
- Added best practices for dataset lookups: keep toggles on to avoid indexing issues, and understand how batch deletions affect lookup data. Read more
- Added a limitation noting that only Unified Profile Service audiences are supported when using Read audience journeys with supplemental identifiers. Read more
- Documentation for the Experimentation Accelerator has been relocated to a separate collection. Read more

## September 2025 september-2025

- A new Inbound channel section has been added to the Guardrails and limitations page to gather all limitations applying to the web, In-app, code-based experiences and content cards channels. It includes the peak volume limit of 5,000 inbound requests per second for all inbound requests, and the maximum of 500 active inbound actions. Read more
- A Frequently Asked Questions page has been released for Orchestrated campaigns. Read more
- A troubleshooting section has been added to the Journey Step events documentation with definitions, common causes, and troubleshooting steps for the most frequent discard eventTypes. Read more
- The documentation on how to use supplemental identifiers in journeys now includes a table that details how profiles behave when exit criteria are applied in journeys using supplemental IDs. Read more
- A troubleshooting section has been added to understant profile discards in paused journeys. Read more
- Information has been added in the schemas overview documentation to differentiate standard and relational schemas used for Orchestrated campaigns. Read more
- Information has been added in the Decisioning and Decision management documentation on the requirements to successfully train auto-optimization and personalized optimization models.
- Clarified that Interactive Message Execution REST API calls have a 60-second timeout, with internal retries to ensure delivery. Read more
- The Decisioning item collections page was updated to clarify the behavior of the CONTAINS operator when defining rules. Read more
- The Assign priority scores page was updated with the specific steps to define a priority score for inbound channel actions within the Action activity. Read more

## August 2025 august-2025

- A new page listing the best practices for designing accessible email and landing page content with Journey Optimizer was added. Read more
- The documentation for supplemental identifiers in journeys has been updated with the following clarifications: After adding a supplemental identifier to a schema, a new event (for event-triggered journeys) or a new field group (for Read audience journeys) must be created. Existing entities do not refresh automatically and will not recognize the new identifier. Supplemental identifiers are not validated against Data Usage Labeling & Enforcement (DULE) policies and are not considered during data governance checks in journeys. Read more
- The Optimization in campaigns page was updated to reflect the fact that optimization is now also available in journeys. Read more
- A link to the tutorial video describing how to leverage message optimization in a campaign was added. Read more

## July 2025 july-2025

- The campaigns interface now features two separate tabs: Action and API Triggered . The documentation has been updated accordingly, with information for each campaign type organized into dedicated sections to improve clarity and usability. Read more
- The Get started with subdomain delegation and Delegate a subdomain pages have been updated to better present the different delegation methods and the steps to set them up.
- A note has been added to the Fragments section, specifying that when tracking is enabled in a journey or a campaign, if links are present in a fragment and if this fragment is used in a message, these links are tracked such as all other links included in the message. Learn more
- The guardrails and limitations applying to subdomain delegation in Journey Optimizer have been enriched and consolidated into one dedicated section. Read more
- A note has been added to the Create fallback offers and Create decision pages to mention that fallback offers should contain all representations used within a decision. Read more
- The guardrails applying to fragments have been enriched. Read more .
- A note has been added to specify that links added to messages expire after 25 months and links to mirror pages after 90 days. Read more

## June 2025 june-2025

- Added a new section on how to add and use rich text such as line breaks, bold, italics etc., to customizable fragments by using HTML components. Read more
- The Decisioning part has been updated with a specific section dedicated to building AI models. Read more
- Added a recommendation about the usage of the actionExecutionTime field in the journeyStep events action. Read more
- Added a note about the messageID which may not be unique for each individual delivery. Read more
- Added a recommendation about historical events management in data hygiene operations. Read more
- Added a guardrail about landing pages not being supported for migration between sandboxes. Read more
- Added a caution note about nested JSON objects not supported in custom authentication for custom actions. Read more
- Added a caution note about conditional content variant naming in the Email designer. Read more
- Updated the “Undelegate a landing page subdomain” section. Read more
- Clarified journey reentrance rules when using supplemental identifiers. Read more
- Added a new note to clarify that you must use the expression editor in Advanced mode when selecting the supplemental identifier attribute during event configuration. Learn more
- Added clarification on how journey reentrance works with supplemental identifiers. Learn more

## May 2025 may-2025

- Adobe integrations available with Journey Optimizer are now listed in the “Connect your systems and environments” section. Read more
- The content integrations are now grouped in the Content Management section. Read more
- Architecture diagrams for Adobe Experience Platform and Journey Optimizer have been updated. Read more
- Added a video about the personalization editor playground to help you learn how to write and test personalization code using sample data. Read more
- The maximum number of addresses in a seed list has been increased from 50 to 300. Read more
- A new step detailing how to wrap code when using decision policies in the code-based experience editor has been added to the Create decision policies page. Read more
- A note has been added to the Code-based experiences documentation to specify that when you have multiple code-based experience actions running on the same surface, the campaign or journey’s priority score determines what is delivered to the end-user if they qualify for more than one action. Read more
- A new page on troubleshooting inbound actions in journeys provides a step-by-step guide to identify and resolve issues independently before reaching out to support. Read more
- A new page has been added to describe how to add the following flags to your client implementation when using decisioning in code-based experiences: Adding the dryRun flag to test decisioning in code-based experiences. Read more Apply deduplication to decisioning requests in code-based experiences. Read more

## April 2025 apr-2025

- The Configuration chapter is now split into three chapters: [Channel configuration](/en/docs/journey-optimizer/using/configuration/get-started-configuration), [Journey configuration](/en/docs/journey-optimizer/using/configure-journeys/about-data-sources-events-actions), and [Connect your systems](/en/docs/journey-optimizer/using/connect-systems/ajo-apis).
- Added a caution note about using experience events in journey expressions and conditions. [Read more](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced#discovering-the-interface)
- Added a note on the Direct mail configuration page about temporary storage of the output file. [Read more](/en/docs/journey-optimizer/using/channels/direct-mail/direct-mail-configuration)
- Added a tip in the journey advanced expression editor section about the condition format guidelines. [Read more](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced)
- Added a caution note in the inAudience function section about impacts and best practices when renaming an audience. [Read more](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/functioninaudience)
- Added a recommendation about the native keywords usage when using two-way SMS. [Read more](/en/docs/journey-optimizer/using/channels/sms/sms-opt-out)
- Updated the journey test page with a note about the need for including an identity namespace in the event used. [Read more](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)
- Currently, you cannot undelegate subdomains through the Journey Optimizer user interface - you must reach out to your Adobe representative. Steps to undelegate a subdomain are now detailed for [Emails](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomain#undelegate-subdomain), [SMS](/en/docs/journey-optimizer/using/channels/sms/sms-subdomains#undelegate-subdomain), [Web experiences](/en/docs/journey-optimizer/using/channels/web/configure-web-channel/web-delegated-subdomains#undelegate-subdomain), and [Landing pages](/en/docs/journey-optimizer/using/content-management/landing-pages/lp-configuration/lp-subdomains#undelegate-subdomain).[Read more](../configuration/delegate-subdomain.md#undelegate-subdomain)
- Added clarification about the optional maxHttpConnections parameter in the journeys Capping API, including guidance on how to use it alongside throttling configurations for the same endpoint. [Read more](/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling)
- In the Decisioning section, added guidance explaining that approved offer items cannot be deleted if they are used in a collection or a decision. Included steps to change their status to “Draft” using the **Undo approve** option. [Read more](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/manage-decision-items/items#manage)
- Information on sandboxes have been grouped together into a new “Sandboxes management” section. This new section provides information on how to use and assign sandboxes, and how to use package export and import capabilitie to copy objects such as journeys, content templates, or fragments, across multiple sandboxes. [Read more](/en/docs/journey-optimizer/using/connect-systems/sandbox/sandboxes)

## March 2025 mar-2025

- The page about Audience Qualification events has been updated with new recommendations. [Read more](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events)
- Custom action troubleshooting capability is now available to all customers (GA). [Read more](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshoot-custom-action)
- Data Hygiene is now Data Lifecycle in the product user interface. The documentation has been updated to reflect this change. [Read more](/en/docs/journey-optimizer/using/privacy/data-hygiene)
- The missing Landing Page built-in permissions have been added to the documentation. [Read more](/en/docs/journey-optimizer/using/access-control/ootb-permissions)
- A note has been added about scheduling recurring campaigns. [Read more](/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign)
- The section about inserting links and enabling tracking in an email message has been updated and reorganized. [Read more](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/message-tracking)
- The section about personalization capabilities into Adobe Journey Optimizer has been reorganized and improved. [Read more](/en/docs/journey-optimizer/using/content-management/personalization/personalize)
- Decision management API to list personalized offers has been updated with a sample to perform pagination if multiple personalized offers are missing from the response. [Read more](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/api-reference/offers-api/personalized-offers/offers-list)
- A new page gathering all information regarding the List unsubscribe feature has been created for improved clarity. [Read more](/en/docs/journey-optimizer/using/channels/email/configure-email/list-unsubscribe)
- The Frequency capping section has been updated with information on how the frequency capping counter is updated for the Decisioning and Batch Decisioning APIs, in addition to the Edge Decisioning API. [Read more](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/managing-offers-in-the-offer-library/configure-offers/add-constraints#frequency-capping)

## February 2025 feb-2025

- The Read Audience activity guardrails have been updated to specify that only one activity can be used in a journey and that it can target only one audience. Read more
- Journey guardrails when using Adobe Campaign activities have been updated. Read more
- Steps to create your first journeys have been detailed, and links to documentation section have been added. Read more
- A new page is now available to detail the journey dashboard and filtering user interface. Read more
- Documentation for Send-Time optimization and its related FAQ have been updated, improved and moved to a new dedicated page. Read more
- New guardrails have been added for journey events. Read more
- The built-in channel actions page has been reorganized. Read more
- Guardrails & limitations have been added in the Decisioning and Decision management sections. Decisioning guardrails & limitations Decision management guardrails & limitations
- A new section on context data has been added in the Decision management documentation. It provides information on how to leverage context data in the decisioning engine, for example to design a decision rule that requires the current weather to be ≥80 degrees at the time the decision request is made. Read more

## January 2025 jan-2025

- A new section on the Execution address option in the email configuration has been added. The primary address is defined at the sandbox level, but the default setting can be overidden for a specific email configuration. Read more
- The Get started with deliverability page has been updated with the possibility to create IP warmup workflows directly from the user interface. Read more
- The Header parameters section has been updated to reflect the new labels and changes in the user interface. Read more
- The Forward email section has been updated to specify that all emails sent to the From email address are forwarded to the forward email address. If no forward email is specified, these emails are discarded. Read more
- The maximum size of contextual attributes passed into an API-triggered campaign request has been updated to 200kb. Read more
- A new section has been added to the Manage fragments page to describe how to add new attributes to a live fragment. The whole page has also been improved. Read more
- A “Guardrails & limitations” section has been added to the conflict management & prioritizations tools documentation. Read more
- A new end-to-end use case has been added to present all the steps needed to use Decisioning in content experiments with the Journey Optimizer code-based experience channel. Read more
- The Configure email settings page has been divided into several sub-pages for improved readability, including new standalone pages dedicated to List unsubscribe , Header parameters and URL tracking .

2024
## December 2024 nov-2024

- A note has been added to help troubleshoot a potential error message when making an API call to enable datasets for personalization using Adobe Experience Platform data. [Read more](/en/docs/journey-optimizer/using/content-management/personalization/aep-data-perso)

## October 2024 oct-2024

- All new features and improvements coming with Journey Optimizer October '24 release have been detailed in the documentation. [Read more](/en/docs/journey-optimizer/using/whats-new/release-notes)
- All communication channels available in Journey Optimizer are now grouped in a dedicated section of the documentation. [Read more](/en/docs/journey-optimizer/using/channels/gs-channels)
- The **Configure your code-based experience** page has been improved to make the process clearer, including the section explaining what a surface URI is. [Read more](/en/docs/journey-optimizer/using/channels/code-based-experience/configure-code-based-channel/code-based-configuration)
- The **Create web channel configuration** page has been updated to clarify the steps when creating a pages matching rule, which also apply to Code-based experience configuration. [Read more](/en/docs/journey-optimizer/using/channels/web/configure-web-channel/web-configuration#web-page-matching-rule)
- A note about the upcoming time-to-live (TTL) guardrail for system-generated datasets has been added. [Read more](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets)
- A new section has been added to describe how to preview your code-based personalized experiences right on your browser or on your mobile devices, using the **Preview on device** option when simulating content in a journey or a campaign. [Read more](/en/docs/journey-optimizer/using/channels/code-based-experience/create-code-based-experiences/test-code-based#preview-on-device)
- A new page has been added on how to leverage Custom upload audiences for decisioning. [Read more](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/get-started-decision/custom-upload-decisioning)
- A new page has been added to introduce the decision capabilities available in Journey Optimizer. [Read more](/en/docs/journey-optimizer/using/decisioning/gs-decision)
- Guardrails and limitations have been added to the Decisioning documentation. [Read more](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/gs-experience-decisioning#guardrails)

## September 2024 sept-2024

- All new features and improvements coming with Journey Optimizer Sept '24 release have been detailed in the documentation. [Read more](/en/docs/journey-optimizer/using/whats-new/release-notes)
- Added a section about journey retry management. [Read more](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience#read-audience-retry)
- The FAQ about Capping/throttling rule for custom actions has been updated to mention the default capping rule. [Read more](/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems#faq)
- The Control access section has been updated with permissions related to AI Assistant Content Generator. [Read more](/en/docs/journey-optimizer/using/access-control/high-low-permissions#ai-orchestrated-campaign)
- A video about AI Assistant Content Generator for email generation has been added. [Read more](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-full-content#video)

recommendation-more-help
