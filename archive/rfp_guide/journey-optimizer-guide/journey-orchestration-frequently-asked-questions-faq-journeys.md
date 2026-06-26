---
title: "Journey orchestration - frequently asked questions faq-journeys"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-faq"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:13.092866+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Journey orchestration - frequently asked questions faq-journeys

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Get Started](#)

CREATED FOR:

- Beginner
- Intermediate
- User

Find answers to common questions about Journey Orchestration in Adobe Journey Optimizer.

Need more details? Use the feedback options at the bottom of this page to raise your question. You can also connect with the [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en#_blank).

## General concepts

What is a journey in Adobe Journey Optimizer?
A journey is a multi-step orchestration that allows you to design and execute real-time customer experiences across multiple channels. Journeys combine events, orchestration activities, actions, and messages to create personalized, contextual experiences based on customer behavior and business events.

Learn more about [journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/journey).

What are the different types of journeys?
Adobe Journey Optimizer supports four types of journeys:

- **Unitary journeys**: Triggered individually by an event (e.g., a purchase, app sign-in). Profiles enter the journey one at a time when the event occurs.
- **Read Audience journeys**: Start with an audience from Adobe Experience Platform and send messages in batch to all profiles in that audience.
- **Audience Qualification journeys**: Triggered when profiles qualify for (or exit from) a specific audience segment. Profiles enter the journey as they meet the audience criteria.
- **Business event journeys**: Triggered by business events (e.g., stock updates, weather alerts) that affect multiple profiles simultaneously.

Learn more about [journey types](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management#types-of-journeys).

What's the difference between a journey and a campaign?
**Journeys** are multi-step orchestrations that react to events or target audiences, allowing for complex logic, conditions, wait times, and multiple touch points across the customer lifecycle.

**Campaigns** come in three types:

- **Action campaigns**: One-time or recurring communications sent to a specific audience, ideal for standalone messages like promotional announcements or newsletters.
- **API-triggered campaigns**: Campaigns triggered via API calls, enabling integration with external systems to send messages based on real-time events or business logic.
- **Orchestrated campaigns**: Multi-step, audience-based campaigns built on a canvas that can include conditions, wait times, and multiple actions to create scheduled, coordinated experiences.

**Best practice**: Use [journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/journey) for complex, event-triggered engagement with advanced orchestration. Use [action campaigns](/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign) for scheduled, audience-based communications. Use [API-triggered campaigns](/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/api-triggered-campaigns) for programmatic triggering from external systems. Use [orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns) for multi-step communications with campaign-specific requirements.

What are the main components of a journey?
A journey consists of:

- **Events**: Entry points that trigger the journey (e.g., profile qualification, business events)
- **Orchestration activities**: Logic components like conditions, wait, read audience, journey fragments, and end
- **Actions**: Activities that perform tasks, such as sending messages, updating profiles, or calling external APIs
- **Built-in channel actions**: Native messaging capabilities for email, SMS, push, and other channels
- **Custom actions**: Integration with third-party systems

Learn more about [journey activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities).

What types of audiences are supported in journeys and what are their limitations?
Adobe Journey Optimizer supports four types of audiences, each with different characteristics and guardrails:

**1. Streaming audiences**

- Description : Audiences that evaluate in real-time as profile data changes
- Evaluation : Continuous evaluation when profile attributes or events match segment criteria
- Journey usage : Supported in Read Audience, Audience Qualification, and Condition activities
- Best for : Real-time engagement based on behavioral changes or profile updates
- Guardrails : Maximum audience size depends on your Journey Optimizer license Evaluation latency typically under 5 minutes Complex segment logic may impact evaluation performance

**2. Batch audiences**

- Description : Audiences evaluated on a scheduled basis (typically daily)
- Evaluation : Processed in batch jobs at scheduled intervals
- Journey usage : Supported in Read Audience and Condition activities; limited support in Audience Qualification journeys
- Best for : Regular campaigns, newsletters, scheduled communications
- Guardrails : Evaluation occurs once per day (default) or at configured schedule Profiles may not reflect real-time changes until next evaluation Read Audience activity can process large batch audiences efficiently

**3. Upload audiences (Custom upload)**

- Description : Audiences created by uploading CSV files with profile identifiers
- Evaluation : Static list updated only when new files are uploaded
- Journey usage : Supported in Read Audience and Condition activities; not supported in Audience Qualification journeys
- Best for : One-time campaigns, external list imports, targeted communications
- Guardrails : CSV file size limits apply (check product documentation for current limits) Audience members are static until refreshed with new upload Identity namespace must match journey namespace Profiles must exist in Adobe Experience Platform

**4. Federated Audience Composition (FAC) audiences**

- Description : Audiences created using federated data, allowing you to query and compose audiences from external data warehouses without copying data into Adobe Experience Platform
- Evaluation : Static composition updated when the federated audience composition is executed
- Journey usage : Supported in Read Audience and Condition activities; not supported in Audience Qualification journeys (similar to upload audiences from a backend perspective)
- Best for : Enterprise data warehouse integration, audience composition using external data sources, scenarios requiring data to remain in external systems
- Guardrails : Audience members are static until next federated composition execution Identity namespace must match journey namespace Performance depends on external data warehouse query capabilities Requires Federated Audience Composition add-on

**Customer Journey Analytics (CJA) audiences**:

While CJA audiences are not directly supported in journeys, you can use a **workaround** by “wrapping” a CJA audience in a segmentation rule. This creates a batch UPS (Unified Profile Service) audience that references the CJA audience, making it available for use in journeys as a batch audience type.

**Journey-specific considerations**:

- **Read Audience journeys**: All four audience types supported; batch export occurs when journey runs
- **Audience Qualification journeys**: Streaming audiences recommended; batch audiences have delayed qualification detection; upload and FAC audiences not supported
- **Condition activities**: All audience types can be used to check membership
- **Namespace alignment**: Audience identity namespace must match the journey’s namespace for proper profile identification

**Best practices**:

- Use **streaming audiences** for real-time, event-driven journeys requiring immediate response
- Use **batch audiences** for scheduled communications where daily evaluation is sufficient
- Use **upload audiences** for targeted one-time campaigns with external lists
- Use **FAC audiences** when you need to leverage enterprise data warehouse capabilities without data duplication
- Monitor audience size and evaluation performance in large-scale deployments
- Consider audience refresh rates when designing journey timing and entry conditions

Learn more about [audiences](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences), [creating segments](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/creating-a-segment-definition), [custom upload audiences](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/custom-upload), and [Federated Audience Composition](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/federated-audience-composition).

How do I choose between a unitary journey and a read audience journey?
Use **unitary journeys** when:

- You need to react to individual customer actions in real-time (e.g., purchase confirmation, cart abandonment)
- Each customer should progress at their own pace
- You want to trigger based on specific events

Use **read audience journeys** when:

- You’re sending batch communications to a group (e.g., monthly newsletter, promotional campaigns)
- All customers should receive the message around the same time
- You’re targeting a pre-defined audience segment

## Building journeys

How do I start building my first journey?
Follow these key steps:

- **Set up prerequisites**: Configure events, data sources, and actions as needed
- **Create the journey**: Navigate to the Journeys menu and click “Create Journey”
- **Define journey properties**: Set the journey name, description, and other settings
- **Design the journey**: Drag and drop activities from the palette into the canvas
- **Test the journey**: Use test mode to validate your journey logic
- **Dry run the journey**: Use Dry run to test the journey using real production data without contacting real customers or updating profile information
- **Publish the journey**: Activate the journey to make it live

Follow the [step-by-step guide](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

What prerequisites are needed before building a journey?
Prerequisites depend on your journey type:

- **Event-triggered journeys**: Configure events to define when profiles should enter the journey
- **Audience-based journeys**: Create audiences in Adobe Experience Platform
- **Data enrichment**: Set up data sources to retrieve additional information
- **Third-party integrations**: Configure custom actions if using external systems

Learn more about [journey configuration](/en/docs/journey-optimizer/using/configure-journeys/about-data-sources-events-actions).

Can I use data from external systems in my journey?
Yes, there are several approaches to leverage external data:

**Best practices**:

- **Custom actions**: Call external APIs through custom actions to retrieve or send data to third-party systems. This is the recommended approach for real-time interactions with external systems.
- **Dataset lookup**: If you can load data from external systems into Adobe Experience Platform, use the dataset lookup feature to retrieve information stored in Experience Platform datasets.
- **External data sources**: Configure external data sources to retrieve information from third-party API services (less recommended than the above approaches).

These options allow you to enrich the customer experience with data from your CRM, loyalty systems, weather services, or other external platforms.

Learn more about [custom actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-custom-actions) and [dataset lookup](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup).

How do I add conditions to my journey?
You can add conditions using the **Condition activity** from the orchestration palette. Conditions allow you to:

- Create simple or advanced conditions using the expression editor
- Split the journey into multiple paths based on profile attributes, audience membership, events, or contextual data
- Define timeout paths for profiles that don’t meet the condition within a specified time

Learn more about [conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions).

Can I send messages to profiles in a journey?
Yes. Journey Optimizer includes **built-in channel actions** that allow you to send messages through email, push notifications, SMS/MMS/RCS, in-app messages, web experiences, code-based experiences, content cards, WhatsApp, and LINE. You can design message content directly in Journey Optimizer and add them as action activities in your journey.

For channels not natively supported, you can use **custom actions** to integrate with external messaging platforms and send messages through any third-party channel.

Learn more about [messages in journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action) and [custom actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-custom-actions).

How do I wait for a specific time or event in a journey?
Use the **Wait activity** to pause the journey for a specified duration or until a specific date/time. Wait activities are useful for:

- Sending follow-up messages after a delay (e.g., 3 days after purchase)
- Creating drip campaigns with timed intervals
- Combining with conditions to create timeout scenarios

Learn more about [wait activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity).

Can I update profile information within a journey?
Yes. Use the **Update Profile** activity to modify profile attributes in Adobe Experience Platform based on journey events or conditions. This is useful for updating loyalty points, recording journey milestones, changing preference settings, or tracking customer engagement scores.

Learn more about [profile updates](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/update-profiles).

How do I send an email immediately after someone makes a purchase?
Create a **unitary event-triggered journey**:

- Configure a “Purchase” event with the order details
- Add the event as your journey entry point
- Immediately follow with an Email action
- Design your order confirmation email with personalized order details
- Publish the journey

The journey will automatically trigger whenever a purchase event is received, sending the confirmation email in real-time.

Learn more about [event configuration](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events) and [email actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action).

Can I resend a message if someone doesn't open or click it?
Yes. Use a **Reaction** event with a **Timeout**:

- After sending your message, add a Reaction event immediately after the channel action (without any Wait activity in between)
- Configure a timeout period (e.g., 3 days) on the Reaction event to listen for email opens or clicks
- Create two paths: If opened/clicked : Continue with next steps or end the journey Timeout path (not opened/clicked) : Send a reminder email with different subject line

**Best practice**: Limit the number of resends to avoid appearing spammy (typically 1-2 reminders maximum).

Learn more about [Reaction events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events).

How do I create a cart abandonment journey?
Create an event-triggered journey using a **Reaction** event with a Timeout:

- Configure a “Cart Abandoned” event : Triggered when items are added but checkout isn’t completed within a timeframe
- Send an initial message (optional): Email acknowledging cart items
- Add a Reaction event immediately after the channel action : Configure it to listen for a Purchase event
- Set a timeout period : Define a timeout (e.g., 1-2 hours) on the Reaction event to give the customer time to complete naturally
- Create two paths : If Purchase event occurs : End the journey or continue with post-purchase flow Timeout path (no purchase) : Send an abandonment reminder email with cart contents
- Optional : Add another Reaction event immediately after the reminder email with timeout (24 hours) and send a second reminder with an incentive (e.g., 10% discount)

| note important |
| --- |
| IMPORTANT |
| **Reaction** events must be placed immediately after [channel actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action). Do not place **Wait** activities between the channel action and the **Reaction** activity. |

Learn more about [journey use cases](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/jo-use-cases) and [reaction events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events).

How do I split customers into different paths based on their purchase history?
Use a **Condition activity** with audience membership or profile attributes:

- Add a Condition activity to your journey
- Create multiple paths based on criteria: Path 1 : High-value customers (total purchases > $1000) Path 2 : Regular customers (total purchases $100-$1000) Path 3 : New customers (total purchases < $100)
- Add different messages or offers for each path

Learn more about [conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize#conditions) and [audience qualification](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events).

How do I handle different time zones in my journey?
Journey Optimizer provides several options for timezone management:

- **Profile timezone**: Messages are sent based on each individual’s timezone stored in their profile
- **Fixed timezone**: All messages use a specific timezone you define

Learn more about [timezone management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management).

How long should I wait between messages in my journey?
**Best practices for wait times**:

- **Transactional messages** (order confirmations): Send immediately
- **Welcome series**: 1-3 days between emails
- **Educational content**: 3-7 days between messages
- **Promotional campaigns**: At least 7 days between offers
- **Re-engagement**: 14-30 days for inactive users

**Factors to consider**:

- Industry standards and customer expectations
- Message urgency and importance
- Your overall messaging frequency across all channels
- Customer engagement patterns

**Tip**: Use journey capping rules to limit the total number of messages a customer receives across all journeys.

Learn more about [wait activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity) and [journey capping](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/journey-capping).

What are Journey Fragments and when should I use them?
**Journey Fragments** are reusable sets of journey nodes that you build once and insert into any journey across your sandbox. They are available as an orchestration activity in the journey canvas.

**When to use Journey Fragments**:

- You have logic that repeats across multiple journeys (e.g., eligibility checks, preferred channel routing, welcome sequences)
- You want to enforce consistency across teams — define the pattern once, reuse it everywhere
- You want to speed up journey creation by avoiding rebuilding common node sequences from scratch

**Key behaviors to be aware of**:

- Inserting a fragment creates a **static copy** of its nodes — updates to the original fragment are **not** propagated to journeys that already use it
- Only **Active** fragments can be inserted into a journey
- Fragments are sandox-scoped and support a maximum of 20 nodes and 200 active fragments per sandbox
- [Jump](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/jump) activities are not allowed inside a fragment

**Difference from the Jump activity**: The [Jump activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/jump) redirects profiles to another live journey at runtime. Journey Fragments copy nodes into the current journey at design time — they are a build-time reuse mechanism, not a runtime routing mechanism.

Learn more about [Journey Fragments](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-fragments).

## Testing and publishing

How do I test my journey before publishing it?
Journey Optimizer offers two testing approaches:

- **Test mode**: Simulate individual profiles moving through the journey step by step, allowing you to verify logic, conditions, and actions before going live.
- **Dry run mode**: Execute your journey using real production data without contacting actual customers or updating profile information. This gives you confidence in audience targeting and journey design.

**Best practice**: Always test journeys before publishing to ensure they work as expected and to identify any issues early.

Learn more about [test mode](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) and [dry run](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run).

What happens when I publish a journey?
When you publish a journey:

- The journey becomes **Live** and ready to accept new profiles
- Profiles can enter based on the entry criteria (event or audience)
- Messages and actions start executing for profiles moving through the journey
- You can only edit limited things on a published journey (you must create a new version if you want to edit more)

Learn more about [publishing journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey).

Can I modify a journey that is already published?
Yes, but with limitations. You can edit certain elements of a Live journey:

**What you can edit**:

- Journey properties (name, description)
- Message content within existing message activities
- Some journey settings

**What you cannot edit**:

- Journey structure (adding/removing activities)
- Entry conditions
- Journey canvas logic

**To make structural changes**:

- **Create a new version**: Duplicate the published journey to create a draft version
- **Make your changes**: Edit the draft version as needed
- **Test the new version**: Use test mode to validate changes
- **Publish the new version**: This automatically closes the previous version and activates the new one

Profiles already in the journey will complete the original version, while new profiles will enter the new version.

Learn more about [journey versions](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/journey-ui#journey-filter).

How do I stop a journey?
You can manage journey execution in several ways:

- **Close to new entrances**: Stop new profiles from entering while allowing existing profiles to complete their journey
- **Stop immediately**: End the journey and exit all profiles currently in it
- **Pause**: Temporarily halt the journey and resume it later

Learn more about [ending journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey).

What's the difference between "Close to new entrances" and "Stop"?
**Close to new entrances**:

- New profiles cannot enter the journey
- Profiles already in the journey continue and complete their path
- Use this when you want to gracefully wind down a journey
- Example: Seasonal campaign that has ended but you want existing customers to complete their experience

**Stop**:

- Immediately ends the journey for all profiles
- All profiles currently in the journey are exited
- Use this for urgent situations or critical errors
- Example: Product recall requiring immediate halt of promotional messages

Learn more about [ending journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey) and [publishing journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey).

## Journey execution and monitoring

How can I track profile progress through a journey?
You can monitor journey execution using:

- **Journey Live Report**: View real-time metrics and KPIs for your journey. You can also review dry run test execution results here.
- **Journey All Time Report**: Analyze journey performance using Customer Journey Analytics. You can also review dry run test execution results here.
- **Journey Step Events**: Access detailed execution data for custom reporting

Learn more about [journey reporting](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/report-journey).

Why didn't a profile enter my journey?
Common reasons profiles may not enter a journey:

- **Event not received**: The triggering event was not sent or properly configured
- **Audience criteria not met**: The profile doesn’t qualify for the entry audience
- **Re-entrance rules**: The profile recently completed the journey and re-entrance is blocked
- **Journey not published**: The journey is in draft status
- **Invalid namespace**: The journey namespace doesn’t match the profile identity
- **Journey closed**: The journey is no longer accepting new entrances
- **Streaming audience qualification timing**: For journeys using Audience Qualification with streaming audiences, profiles may not enter if they were already in the audience before the journey was published. They can also be delayed if the journey has not completed its activation period (up to 10 minutes after publishing).

Learn more about [entry management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management) and [streaming audience qualification timing considerations](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events#streaming-entry-caveats).

What are journey step events and how can I use them?
Journey step events are automatically generated datasets that capture detailed information about every step a profile takes in a journey. They include entry and exit events, action execution (messages sent, custom actions called), journey transitions (moving between activities), and errors and timeouts.

**Use cases**:

- Build custom reports in Customer Journey Analytics or BI tools
- Debug journey execution issues
- Track detailed profile behavior
- Create advanced analytics and attribution models

Learn more about [journey step events](/en/docs/journey-optimizer/using/reporting/reports/sharing-overview).

How can I troubleshoot a journey that isn't working as expected?
Journey Optimizer provides several troubleshooting resources:

- **Error indicators**: Visual alerts in the journey canvas highlight configuration issues
- **Test mode**: Step through the journey to identify where problems occur
- **Dry run mode**: Test the journey using real production data without contacting customers to validate targeting and execution
- **Journey reports**: Review execution metrics to find bottlenecks or errors
- **Journey step events**: Analyze detailed execution data to understand profile behavior

**Common issues**:

- Incorrectly configured events or audiences
- Missing data source connections
- Invalid expressions in conditions or personalization
- Timeout settings that are too short

Learn more about [troubleshooting journeys](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting).

Can I see who is currently in my journey right now?
Yes. Use the **Journey Live Report** to view:

- Number of profiles currently in the journey
- Number of profiles at each activity
- Profiles who entered in the last 24 hours
- Real-time execution metrics

To see individual profiles, use **journey step events** in Customer Journey Analytics or query the step event datasets directly.

Learn more about [journey live reporting](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/report-journey).

Why are my messages not being sent in my journey?
**Common reasons and solutions**:

- Consent issues : Recipients haven’t opted in to receive communications Solution: Check consent policies and opt-in status
- Suppression list : Email addresses are on the suppression list Solution: Review the suppression list for bounces or complaints
- Invalid contact information : Missing or malformed email addresses/phone numbers Solution: Validate profile data quality
- Journey not published : The journey is still in draft mode Solution: Publish the journey to activate it <ul> <li><strong>Message not approved</strong>: Message content requires approval before sending<br> Solution: Submit for approval or check approval status<br> –></li> </ul> </li> <li> <p><strong>Channel configuration issue</strong>: Email/SMS configuration is incorrect<br> Solution: Verify channel configurations and authentication</p> </li> </ul> <p>Learn more about <a href="troubleshooting.md">troubleshooting</a> and <a href="../action/consent.md">consent management</a>.</p> </details> <details> <summary><span class="details-marker"></span>How do I personalize messages in my journey?</summary><p>You can personalize messages using the <strong>personalization editor</strong>:</p> <p><strong>Available personalization data</strong>:</p> <ul> <li><strong>Profile attributes</strong>: First name, last name, email, custom fields</li> <li><strong>Event data</strong>: Purchase details, browsing behavior, app activity</li> <li><strong>Contextual data</strong>: Journey variables, external API data</li> <li><strong>Audience membership</strong>: Segment qualifications</li> <li><strong>Computed attributes</strong>: Pre-calculated values</li> </ul> <p><strong>Example personalization</strong>:</p> <ul> <li>“Hi <code>{{profile.firstName}}</code>, thanks for your purchase of <code>{{event.productName}}</code>”</li> <li>“Based on your loyalty tier (<code>{{profile.loyaltyTier}}</code>), here’s a special offer”</li> <li>Dynamic content blocks that change based on customer preferences</li> </ul> <p>Learn more about <a href="../personalization/personalize.md">personalization</a>.</p> </details> <details> <summary><span class="details-marker"></span>Can I send different messages based on preferred channel?</summary><p>Yes. Use an <strong><a href="conditions.md">Optimize activity</a></strong> to route profiles based on their preferred channel:</p> <ol> <li>Add an <a href="optimize.md">Optimize activity</a> in your journey</li> <li>Create a path for each channel by checking the preferred channel profile attribute (e.g., <code>profile.preferredChannel</code>)</li> <li>Configure channel-specific paths: <ul> <li><strong>Email path</strong>: Add an <a href="../email/create-email.md">email action</a> with email-optimized content</li> <li><strong>SMS path</strong>: Add an <a href="../sms/create-sms.md">SMS action</a> with concise messaging</li> <li><strong>Push path</strong>: Add a <a href="../push/create-push.md">push notification action</a> with short, actionable content</li> <li><strong>In-app path</strong>: Add an <a href="../in-app/create-in-app.md">in-app message action</a> for engaged app users</li> </ul> </li> <li>Add a default path for profiles without a preference, routing them to your primary channel</li> </ol> <p><strong>Best practices</strong>:</p> <ul> <li>Ensure your profile data includes accurate channel preferences</li> <li>Design content appropriate for each channel’s strengths and limitations</li> <li>Use <a href="../configuration/channel-surfaces.md">channel surfaces</a> to manage channel configurations</li> <li>Test all paths to ensure proper message delivery</li> </ul> <p>Learn more about <a href="conditions.md">conditions</a>, <a href="journey-action.md">message actions</a>, and <a href="../channels/gs-channels.md">channel selection</a>.</p> </details> <details> <summary><span class="details-marker"></span>Can I exclude certain customers from my journey?</summary><p>Yes, there are several ways to exclude customers:</p> <p><strong>At journey entry</strong>:</p> <ul> <li>Use <a href="../audience/creating-a-segment-definition.md">audience definitions</a> with exclusion rules</li> <li>Add <a href="entry-management.md">entry conditions</a> that filter out specific profiles</li> <li>Configure <a href="journey-properties.md">profile attribute based exit criteria</a> in journey properties to automatically exclude profiles based on specific attributes</li> </ul> <p><strong>Within the journey</strong>:</p> <ul> <li>Add an <a href="conditions.md">Optimize activity</a> early in the journey to exit unwanted profiles</li> <li>Check for exclusion attributes (e.g., VIP status, test accounts)</li> <li>Use <a href="audience-qualification-events.md">audience qualification</a> to identify profiles to exclude</li> </ul> <p><strong>Example exclusion scenarios</strong>:</p> <ul> <li>Exclude customers who recently purchased</li> <li>Exclude VIP customers from standard promotions</li> <li>Exclude employees and test accounts</li> <li>Exclude customers in specific regions</li> </ul> </details> <h2 id="-4" tabindex="-1">Advanced concepts</h2> <details> <summary><span class="details-marker"></span>What is a journey namespace and why does it matter?</summary><p>A <strong>namespace</strong> is an identity type (e.g., email, ECID, phone number) that determines how profiles are identified in the journey. The namespace defines which identifier is used to match profiles, must be consistent across events, audiences, and profile data, and affects journey entry and re-entrance behavior.</p> <p><strong>Best practice</strong>: Choose a namespace that reliably identifies your customers across all touch points.</p> <p>Learn more about <a href="../audience/get-started-identity.md">identity namespaces</a>.</p> </details> <details> <summary><span class="details-marker"></span>Can profiles enter the same journey multiple times?</summary><p>Yes, depending on the <strong>re-entrance settings</strong>:</p> <ul> <li><strong>Allow re-entrance</strong>: Profiles can enter the journey multiple times after completing it</li> <li><strong>Re-entrance wait period</strong>: Define a minimum time between journey entries (e.g., 7 days)</li> <li><strong>Force re-entrance on event</strong>: Trigger a new journey instance even if the profile is already in the journey</li> <li><strong>Supplemental identifier</strong>: Use a supplemental ID to allow profiles to re-enter the journey multiple times for different entities (e.g., different orders, bookings, or transactions), even while they’re already in the journey</li> </ul> <p><strong>Best practice</strong>: Use re-entrance rules to prevent message fatigue and ensure appropriate pacing. Consider using supplemental identifiers for transactional journeys where profiles need to enter multiple times for different transactions.</p> <p>Learn more about <a href="entry-management.md">entry management</a> and <a href="supplemental-identifier.md">supplemental identifiers</a>.</p> </details> <details> <summary><span class="details-marker"></span>What is send-time optimization?</summary><p><strong>Send-Time Optimization (STO)</strong> uses AI to predict the best time to send a message to each individual profile, maximizing open rates and engagement. STO analyzes historical engagement patterns to determine when each recipient is most likely to interact with your message.</p> <p><strong>Benefits</strong>:</p> <ul> <li>Improved open and click rates</li> <li>Better customer experience through optimally-timed messages</li> <li>Reduced unsubscribe rates</li> </ul> <p>Learn more about <a href="send-time-optimization.md">send-time optimization</a>.</p> </details> <details> <summary><span class="details-marker"></span>What are journey capping rules?</summary><p><strong>Journey capping</strong> allows you to control how profiles interact with journeys, preventing message fatigue and ensuring optimal customer experience:</p> <ul> <li><strong>Entry capping</strong>: Limit the number of times a profile can enter journeys within a specified time period</li> <li><strong>Concurrency capping</strong>: Limit the number of journeys a profile can be in simultaneously</li> </ul> <p>You can set maximum entries or concurrency per profile across journeys or specific journeys, define time windows (daily, weekly, monthly), and prioritize journeys when multiple journeys compete for the same profile.</p> <p>Learn more about <a href="../conflict-prioritization/journey-capping.md">journey capping</a>.</p> </details> <details> <summary><span class="details-marker"></span>Can I integrate my journey with external systems?</summary><p>Yes. Use <strong>custom actions</strong> to call third-party APIs (CRM, marketing automation, loyalty systems), send data to external systems, retrieve real-time information for decisioning, and trigger workflows in external platforms.</p> <p>Custom actions support authentication (API key, custom authentication), request/response payload customization, error handling and timeouts, and dynamic parameters from journey context.</p> <p>Learn more about <a href="using-custom-actions.md">custom actions</a>.</p> </details> <details> <summary><span class="details-marker"></span>How can I use Adobe Campaign with journeys?</summary><p>Journey Optimizer integrates natively with Adobe Campaign to leverage its advanced capabilities:</p> <ul> <li><strong>Adobe Campaign Standard</strong>: Use Campaign Standard actions to send transactional messages</li> <li><strong>Adobe Campaign v7/v8</strong>: Trigger Campaign workflows and use Campaign’s delivery infrastructure</li> </ul> <p><strong>Best practice</strong>: Use this integration if you have existing Campaign templates, data models, or require Campaign-specific features.</p> <p>Learn more about <a href="ajo-ac.md">Campaign integration</a>.</p> </details> <details> <summary><span class="details-marker"></span>What is the Jump activity?</summary><p>The <strong>Jump activity</strong> allows you to transition profiles from one journey to another, enabling reusable journey patterns, journey orchestration across multiple journeys, simplified journey maintenance, and progressive engagement strategies.</p> <p>When a profile reaches a Jump activity, they exit the current journey and enter the target journey at its starting point.</p> <p>Learn more about <a href="jump.md">the Jump activity</a>.</p> </details> <details> <summary><span class="details-marker"></span>How do I create a welcome series journey?</summary><p>A typical welcome series includes multiple touchpoints over several days:</p> <p><strong>Example structure</strong>:</p> <ol> <li><strong>Entry</strong>: Audience of new subscribers or event when someone signs up</li> <li><strong>Email 1 - Immediate welcome</strong>: Thank you and introduction</li> <li><strong>Wait</strong>: 2 days</li> <li><strong>Email 2 - Getting started</strong>: Tutorial or product guide</li> <li><strong>Wait</strong>: 3 days</li> <li><strong>Condition</strong>: Has the customer made a purchase? <ul> <li><strong>Yes</strong>: End or move to customer journey</li> <li><strong>No</strong>: Continue welcome series</li> </ul> </li> <li><strong>Email 3 - Incentive</strong>: Special first-time buyer discount</li> <li><strong>Wait</strong>: 5 days</li> <li><strong>Email 4 - Engagement</strong>: Best-sellers or popular content</li> </ol> <p><strong>Best practices</strong>:</p> <ul> <li>Keep it to 3-5 emails over 2-3 weeks</li> <li>Each email should have a clear purpose and call-to-action</li> <li>Monitor open rates and adjust timing/content accordingly</li> <li>Exit customers early if they convert or engage deeply</li> </ul> <p>Learn more about <a href="jo-use-cases.md">journey use cases</a>.</p> </details> <details> <summary><span class="details-marker"></span>Can I A/B test different paths in my journey?</summary><p>Yes. Use the <strong>Optimize activity</strong> (Limited Availability) or manually create test splits:</p> <p><strong>Using Optimize activity</strong> with the Experiment method:</p> <ul> <li>Randomly splits traffic between different paths to determine which performs best</li> <li>Tests different messages, offers, wait times, or entire journey paths</li> <li>Measures performance based on predefined success metrics and declares a winner</li> </ul> <p><strong>Using Optimize activity</strong> with the Data source condition method:</p> <ul> <li>Create a condition that randomly splits profiles (e.g., using a random number function)</li> <li>Send different experiences to each split</li> <li>Measure results using journey reports</li> </ul> <p><strong>What you can test</strong>:</p> <ul> <li>Different email subject lines</li> <li>Alternative message content</li> <li>Different wait times</li> <li>Various offers or incentives</li> <li>Entirely different journey paths</li> </ul> <p>Learn more about <a href="optimize.md">optimize activity</a> and <a href="../content-management/content-experiment.md">content experiments</a>.</p> </details> <details> <summary><span class="details-marker"></span>How do I trigger a journey when inventory is low?</summary><p>Create a <strong>business event journey</strong>:</p> <ol> <li><strong>Configure a business event</strong>: Set up an event triggered by your inventory system when stock falls below a threshold</li> <li><strong>Select target audience</strong>: Choose profiles to notify (e.g., customers who viewed the product, subscribers to restock alerts)</li> <li><strong>Add message action</strong>: Send notification email or push</li> <li><strong>Personalize content</strong>: Include product details, current inventory level, urgency messaging</li> </ol> <p><strong>Example business events</strong>:</p> <ul> <li>Low inventory alert</li> <li>Price drop notification</li> <li>Product back in stock</li> <li>Flash sale announcement</li> <li>Weather-based promotions</li> </ul> <p>Learn more about <a href="general-events.md">business events</a>.</p> </details> <details> <summary><span class="details-marker"></span>What are merge policies and how do they affect journeys?</summary><p><strong>Merge policies</strong> determine how Adobe Experience Platform combines data from multiple sources to create a unified profile view. They define rules for data prioritization and identity stitching when profile fragments exist across different datasets.</p> <p><strong>Impact on journeys</strong>:</p> <ul> <li> <p>Journeys use the merge policy associated with the audience or event to determine which profile data is available</p> <ul> <li>In Read audience or audience qualification journeys: the merge policy from the audience is used</li> <li>In Unitary event journeys: the default merge policy is used</li> <li>In Business event journeys: the merge policy from the targeted audience in the following Read audience activity is used</li> </ul> </li> <li> <p>The merge policy affects which attributes are accessible in journey conditions, personalization, and actions</p> </li> <li> <p>Different merge policies can result in different profile data being used in the journey</p> </li> </ul> <p><strong>Best practices</strong>:</p> <ul> <li>Ensure the merge policy used by your journey aligns with your data governance requirements</li> <li>Understand which datasets are included in your merge policy to know what data is available</li> <li>Use consistent merge policies across related audiences and journeys for predictable results</li> </ul> <p>Learn more about <a href="../audience/get-started-profiles.md">merge policies</a> and <a href="../audience/get-started-identity.md">identity management</a>.</p> </details> <details> <summary><span class="details-marker"></span>What's the difference between a Condition and a Wait activity?</summary><table> <thead> <tr> <th></th> <th><strong>Condition Activity</strong></th> <th><strong>Wait Activity</strong></th> </tr> </thead> <tbody> <tr> <td><strong>Purpose</strong></td> <td>Creates different paths based on logic (if/then)</td> <td>Pauses the journey for a period of time</td> </tr> <tr> <td><strong>Function</strong></td> <td>Evaluates data and routes profiles accordingly</td> <td>Holds profiles at a specific point before continuing</td> </tr> <tr> <td><strong>Use case</strong></td> <td>Segment customers, check status, branch based on behavior</td> <td>Timing between messages, waiting for business hours, creating delays</td> </tr> <tr> <td><strong>Example</strong></td> <td>If customer is VIP, send premium offer; otherwise send standard offer</td> <td>Wait 3 days after welcome email before sending next message</td> </tr> </tbody> </table> <p><strong>They work together</strong>:</p> <ul> <li>Wait for a period, then use a Condition to check if something happened during the wait</li> <li>Example: Wait 7 days, then check if customer made a purchase</li> </ul> <p>Learn more about <a href="optimize.md#conditions">conditions</a> and <a href="wait-activity.md">wait activities</a>.</p> </details> <h2 id="-5" tabindex="-1">Best practices and limitations</h2> <details> <summary><span class="details-marker"></span>What are the key limitations I should be aware of?</summary><p>Important guardrails include:</p> <ul> <li><strong>Journey complexity</strong>: Maximum activities, paths, and nesting levels</li> <li><strong>Throughput</strong>: Message sending rates and API call limits</li> <li><strong>Time-to-live</strong>: Maximum journey duration (e.g., 91 days)</li> <li><strong>Audience size</strong>: Limits on read audience batch sizes</li> <li><strong>Expression complexity</strong>: Character limits in conditions and personalization</li> </ul> <p>View complete <a href="../start/guardrails.md">guardrails and limitations</a>.</p> </details> <details> <summary><span class="details-marker"></span>What are best practices for journey design?</summary><p><strong>Structure and organization</strong>:</p> <ul> <li>Keep journeys focused on specific use cases</li> <li>Use descriptive naming for activities</li> <li>Add descriptions and labels for complex logic</li> <li>Group related journeys with tags</li> </ul> <p><strong>Performance</strong>:</p> <ul> <li>Optimize wait times to balance engagement and volume</li> <li>Limit external API calls to essential use cases</li> <li>Use capping rules to prevent message fatigue</li> <li>Monitor journey metrics regularly</li> </ul> <p><strong>Testing</strong>:</p> <ul> <li>Always test journeys before publishing</li> <li>Use test mode to validate journey logic and step through the journey</li> <li>Use dry run mode to test with real production data without contacting customers</li> <li>Test all conditional paths and scenarios</li> <li>Use realistic test profiles</li> <li>Validate personalization and dynamic content</li> </ul> <p><strong>Maintenance</strong>:</p> <ul> <li>Regularly review journey performance</li> <li>Stop or close unused journeys</li> <li>Document journey logic and business rules</li> <li>Plan for journey versioning</li> </ul> <p>Learn more about <a href="using-the-journey-designer.md">journey design best practices</a>.</p> </details> <details> <summary><span class="details-marker"></span>How many activities can I add to a journey?</summary><p>Journeys are limited to a maximum of 50 activities. However, we recommend keeping your journeys simpler for better maintainability and performance.</p> <p>As journeys approach 50 activities, they can become very complex and difficult to maintain, troubleshoot, and understand. Large journeys with many branches and conditions may also impact processing time, readability, and team collaboration.</p> <p><strong>Best practice</strong>: Keep your journeys focused and manageable. If your journey is becoming complex, consider:</p> <ul> <li>Breaking it into multiple journeys using the <a href="jump.md">Jump activity</a></li> <li>Extracting repeated logic into <a href="journey-fragments.md">Journey Fragments</a> to reuse across journeys without rebuilding from scratch</li> <li>Simplifying logic with more efficient conditions</li> <li>Reviewing if all activities are necessary</li> </ul> <p>Learn more about <a href="using-the-journey-designer.md">journey design</a> and <a href="../start/guardrails.md">guardrails and limitations</a>.</p> </details> <details> <summary><span class="details-marker"></span>How do I ensure my journey performs well at scale?</summary><p><strong>Design considerations</strong>:</p> <ul> <li>Use <a href="read-audience.md">audience-based entry</a> for batch communications instead of individual events</li> <li>Implement appropriate <a href="wait-activity.md">wait times</a> to spread message volume</li> <li>Leverage <a href="../conflict-prioritization/journey-capping.md">capping rules</a> to prevent system overload</li> <li>Optimize <a href="conditions.md">condition logic</a> to reduce processing complexity</li> </ul> <p><strong>Monitoring</strong>:</p> <ul> <li>Track <a href="report-journey.md">journey metrics</a> regularly</li> <li>Monitor API performance for <a href="using-custom-actions.md">custom actions</a></li> <li>Review error rates and timeout occurrences using <a href="troubleshooting.md">troubleshooting tools</a></li> <li>Subscribe to <a href="../reports/alerts.md">journey alerts</a> critical journey failures</li> </ul> <p><strong>Optimization</strong>:</p> <ul> <li>Use <a href="testing-the-journey.md">test mode</a> and <a href="journey-dry-run.md">dry run</a> to validate performance before publishing</li> <li>Minimize external API calls through <a href="using-custom-actions.md">custom actions</a> to avoid latency and dependency on third-party systems</li> <li>Store frequently used data in Adobe Experience Platform using <a href="dataset-lookup.md">dataset lookup</a> instead of doing external calls, when possible</li> <li>Review and optimize <a href="journey-action.md">message delivery</a> performance</li> </ul> <p>Learn more about <a href="../start/guardrails.md">guardrails and limitations</a>.</p> </details> <h2 id="-6" tabindex="-1">Additional Resources</h2> <p>For more learning and updates, explore the following resources:</p> <ul> <li><a href="journey.md">Get started with journeys</a></li> <li><a href="journey-gs.md">Create your first journey</a></li> <li><a href="troubleshooting.md">Troubleshooting guides</a></li> <li><a href="jo-use-cases.md">Journey use cases</a></li> <li><a href="https://helpx.adobe.com/legal/product-descriptions/adobe-journey-optimizer.html" target="_blank">Journey Optimizer Product Description</a></li> </ul>

recommendation-more-help
