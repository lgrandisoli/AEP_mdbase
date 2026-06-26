---
title: "Troubleshooting FAQ ajo-troubleshooting"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshooting"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:18.984079+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Troubleshooting FAQ ajo-troubleshooting

Last update: May 8, 2026
- Topics:
- [Get Started](#)
- [Monitoring](#)

CREATED FOR:

- Intermediate
- User

The following is a list of troubleshooting articles for Adobe Journey Optimizer. Each troubleshooting section provides answers to frequently asked questions and solutions to problems.

When contacting Adobe support for unresolved issues, include environment details, impact level, replication steps, logs or screenshots, and relevant IDs. [Learn what to include in support tickets](/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface#support-ticket-guidelines).

## Email channel ajo-troubleshooting-email

How to prevent email formatting issues in Adobe Journey Optimizer using themes?
In Adobe Journey Optimizer (AJO), modifying the default CSS blocks in the email header can lead to unexpected formatting issues—especially after removing content fragments. These issues are more noticeable on mobile devices and may result in layout shifts or styling inconsistencies. To prevent this, use the Themes feature to apply custom CSS safely without altering system generated CSS styles.

Learn more about email formatting [on this page](/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design).

Why are fragments with editable fields not working?
In Adobe Journey Optimizer, fragments with editable fields may fail to load correctly or duplicate unexpectedly when added to templates. The problem typically affects specific fragments across environments. To resolve this, verify fragment configuration, check for conflicting editable field definitions, and test in a development sandbox before republishing.

Learn more about customizable fragments [on this page](/en/docs/journey-optimizer/using/content-management/fragments/customizable-fragments).

Why are HTML fragments not displaying correctly in emails?
HTML fragments may fail to render properly in emails, often appearing as **fragment IDs** rather than actual content. Unlike visual fragments, HTML fragments require careful configuration. To resolve this, follow best practices for using both **visual and HTML expression fragments** in your email campaigns.

Learn more about HTML fragments [on this page](/en/docs/journey-optimizer/using/content-management/fragments/fragments).

Why are email templates and content disappearing from unpublished journeys?
When editing email templates in an unpublished journey, the content and templates of certain emails may unexpectedly disappear. This can cause rework and delays. To reduce the risk of this issue, avoid simultaneous edits, limit the number of open tabs, and save changes frequently.

Learn more about templates [on this page](/en/docs/journey-optimizer/using/channels/email/design-email/start-creating-content/use-email-templates).

Why is the Email Preheader field not displaying in 'Code your own' mode?
In **‘Code your own’** mode under the **Edit Email Body** feature, the Preheader input field does not appear. To include preheader text, users must **manually code the preheader** within their custom HTML content.

Learn more about Email preheader configuration [on this page](/en/docs/journey-optimizer/using/channels/email/configure-email/header-parameters).

Why is there a discrepancy in link behavior when using an HTML component in email templates?
When adding an **HTML component** to an email template, links may behave differently depending on the **email client**, **viewing mode**, or **device/browser**. For example, anchor links can function differently in **Outlook’s side-by-side view** compared to full-screen view. Be aware of these variations when designing email templates and test across multiple clients and devices.

See also Email design best practices [on this page](/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design).

How to prevent missing email tracking links in reporting?
Missing link tracking in Adobe Journey Optimizer occurs when email URLs use dynamic variables and don’t start with http, or when logic statements are placed in the URL field. To resolve this, ensure all URLs begin with http, avoid using logic in the URL field, and move complex personalization logic to the HTML content or pre-processed attributes.

Learn more about email tracking [on this page](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/message-tracking).

How do I resolve a Mail Exchanger error when setting up API-triggered transactional email campaigns?
If you encounter a Mail Exchanger (MX) error while creating a channel configuration for an API-triggered transactional email campaign in Adobe Journey Optimizer, it may be due to **DNS misconfigurations** or **DMARC policy limitations**. To resolve this, ensure that your DNS is correctly configured and verify that your domain complies with **Domain-based Message Authentication, Reporting, and Conformance (DMARC)** requirements.

Learn more about email DMARC policies [on this page](/en/docs/journey-optimizer/using/monitor/deliverability/dmarc-record-update).

See also [API-triggered campaigns documentation](/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/api-triggered-campaigns).

## Push channel ajo-troubleshooting-push

Can a profile have multiple push tokens in Adobe Journey Optimizer?
When implementing push notifications in Journey Optimizer, a single profile can indeed have multiple push tokens associated with different devices. During a push notification campaign, Journey Optimizer is designed to manage these tokens and ensure that the targeted profile can be reached across all associated devices.

Learn more about push configuration [on this page](/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration).

See also [push notification data flow](/en/docs/journey-optimizer/using/channels/push/push-config/push-gs) to understand how tokens are registered and managed end-to-end.

Why does clicking on a push message not redirect me to the configured web URL?
If push messages are not redirecting to the intended web URL, it may be due to incorrect click action configuration or disabled push notification settings. Ensure that the **click action** for the push message is correctly set and that **automatic display and tracking** of push notifications are enabled to resolve this issue.

Learn more about push configuration [on this page](/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration).

Why are push notifications failing after updating app credentials?
Expired or misconfigured push credentials — such as an APNs certificate for iOS or an FCM key for Android — cause delivery failures silently. Journey Optimizer cannot send notifications if the credentials stored in the push channel configuration no longer match those registered with the device platform. Update the credentials in the push channel configuration and verify that the associated mobile app surface is republished.

Learn how to configure push credentials [on this page](/en/docs/journey-optimizer/using/channels/push/push-config/push-gs).

See also the [push channel configuration documentation](/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration).

## SMS channel ajo-troubleshooting-sms

Why are my transactional SMS not delivered even though consent is set to
marketing.sms.value=y
?
If a recipient responds **STOP** to an SMS, all future messages from that short number are blocked — including transactional messages. To guarantee uninterrupted delivery of transactional SMS, configure and send them through a **separate short number** that recipients have not previously opted out from.

Learn more about SMS opt-out configuration [on this page](/en/docs/journey-optimizer/using/channels/sms/sms-opt-out).

Why is SMS delivery failing even though the channel is configured?
SMS delivery failures after channel setup are most commonly caused by incorrect provider API credentials, a mismatch between the sender ID and what the provider has registered, or routing restrictions at the provider level. Verify that the API key, password, and sender details entered in Journey Optimizer match exactly what your SMS provider has provisioned. Then send a test message to confirm connectivity before launching a campaign.

Learn how to configure your SMS provider [on this page](/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration).

How do I verify that a profile has opted out of SMS communications?
When a profile texts STOP, Journey Optimizer updates the profile’s SMS consent attribute. To verify the current opt-out status, open the profile in the Experience Platform UI and inspect the consent fields under **Privacy** > **Consents**. For campaign troubleshooting, also check the exclusion reasons in the campaign report — opted-out profiles appear under the **Excluded** count with the reason “Opted out.”

Learn more about SMS opt-out handling [on this page](/en/docs/journey-optimizer/using/channels/sms/sms-opt-out).

## In-app channel ajo-troubleshooting-inapp

Why can't I report on the In-app channel in Customer Journey Analytics?
Difficulties reporting on the **In-app channel** in Adobe Customer Journey Analytics often arise from misconfigured **data views**, **datasets**, or **schema updates**. Ensure these configurations are correctly applied to resolve the issue.

See also the [Journey Optimizer All-time reports documentation](/en/docs/journey-optimizer/using/reporting/channel-report/report-gs-cja).

Why is my in-app message not displaying to users?
In-app messages require the Adobe Experience Platform Mobile SDK to be correctly installed and the Messaging extension to be registered in your app. If the message is not appearing, verify that the SDK is initialized before the app attempts to fetch in-app messages, that the correct app surface (bundle ID) is configured in Journey Optimizer, and that the campaign is in **Live** status. Also confirm that the profile meets the audience criteria and has not already been capped by a frequency rule.

Learn how to configure the In-app channel [on this page](/en/docs/journey-optimizer/using/channels/in-app/inapp-configuration).

Why is my in-app campaign not triggering on the expected event?
In-app campaigns trigger based on event names that must match exactly between your app’s SDK implementation and the trigger condition defined in Journey Optimizer. A mismatch in capitalization, spelling, or event payload structure will prevent the trigger from firing. Use the Adobe Experience Platform Assurance tool to inspect live SDK events and compare them against your campaign’s trigger configuration.

Learn how to create and configure an in-app message [on this page](/en/docs/journey-optimizer/using/channels/in-app/create-in-app).

## Content cards ajo-troubleshooting-content-cards

Why are content cards not displaying in the app?
Content cards require the Adobe Experience Platform Mobile SDK and the **Messaging SDK** to be installed, registered, and configured in the app. Unlike push or in-app messages, content cards are not rendered automatically — your app must explicitly call the Messaging SDK APIs to fetch available cards and then render them in your UI. If cards are not appearing, use **Adobe Experience Platform Assurance** to verify that decision requests are going out when the target event fires and that responses are coming back from the Edge Network.

Learn how to configure content cards support in the Mobile SDK [on this page](/en/docs/journey-optimizer/using/channels/content-card/configure/content-card-configuration-sdk).

Do content cards require the user to grant push notification permissions?
No. Content cards are silent and persistent — they do not rely on OS-level push permissions and are not affected by a user’s notification opt-in status. This makes them a useful fallback channel for reaching users who have disabled push notifications. Cards are fetched from the Edge Network while the user is in-session and displayed within your app’s own UI.

Learn more about the content card channel [on this page](../content-card/get-started-content-card).

Why are content card impressions not appearing in campaign reports?
Content card impressions and interactions (clicks, dismissals) are not tracked automatically. Your app must explicitly send tracking events back to Adobe via the Messaging SDK after rendering a card and after any user interaction with it. If these tracking calls are missing from the implementation, reports will show zero impressions even when cards are being served correctly. Verify the tracking calls are firing in **Assurance** before investigating the campaign configuration.

Learn how to access content card reports [on this page](../content-card/content-card-report).

See also the [content card SDK configuration](/en/docs/journey-optimizer/using/channels/content-card/configure/content-card-configuration-sdk) for the required tracking calls.

## WhatsApp ajo-troubleshooting-whatsapp

Why are my WhatsApp messages not being sent?
WhatsApp message delivery requires two conditions to be met: the recipient must have explicitly opted in to receive WhatsApp communications from your brand, and the message must use a **pre-approved message template** registered with the WhatsApp Business API. If either condition is not met, the message will be silently blocked by the WhatsApp platform before delivery. Verify opt-in status in the recipient’s profile consent attributes and confirm the template is in **Approved** status in your WhatsApp Business account.

Learn how to configure the WhatsApp channel [on this page](/en/docs/journey-optimizer/using/channels/whatsapp/whatsapp-configuration).

Why is my WhatsApp message rejected with a template error?
The WhatsApp Business API only allows pre-approved message templates for outbound business-initiated messages. Free-form messages are only permitted within a **24-hour customer service window** — that is, within 24 hours of the customer sending a message to your brand first. If your message is being rejected, verify that the template has been submitted to and approved by Meta, that the template variables (placeholders) in the Journey Optimizer message exactly match the approved template structure, and that the correct template is selected in the campaign or journey action.

Learn how to create WhatsApp messages [on this page](/en/docs/journey-optimizer/using/channels/whatsapp/create-whatsapp).

How do I collect and verify WhatsApp opt-in from users?
WhatsApp requires explicit opt-in before you can send marketing messages. Opt-in can be collected through any channel your brand controls — such as a web form, SMS double opt-in, or in-app consent screen — as long as the process is clear and documented. Once collected, update the profile’s WhatsApp consent attribute in Adobe Experience Platform. To verify current consent status for a profile, open the profile in the Experience Platform UI and inspect the **Consents** section. Sending to profiles without valid consent violates WhatsApp Business policies and can result in your account being suspended.

Learn how to get started with the WhatsApp channel [on this page](/en/docs/journey-optimizer/using/channels/whatsapp/get-started-whatsapp).

## Data management ajo-troubleshooting-data-management

How do Time-to-Live (TTL) settings apply to Profile and Data Lake datasets when you create a new sandbox?
Organizations provisioning new sandboxes in Adobe Journey Optimizer have raised questions about how Time-to-Live (TTL) settings apply to Profile and Data Lake datasets. TTL settings do not affect existing sandboxes and are automatically applied only to newly provisioned ones.

Learn more about dataset Time-to-live [on this page](/en/docs/journey-optimizer/using/data-management/datasets/datasets-ttl).

Why is a dataset not being enabled for Real-time Customer Profile?
For a dataset to power profile-based personalization and journey conditions in Journey Optimizer, two requirements must both be met: the underlying XDM schema must have **Profile** enabled, and the dataset itself must be toggled on for **Real-time Customer Profile** in the Experience Platform UI. If either is missing, the data will be ingested into the Data Lake but will not be merged into unified profiles. Also ensure that the dataset contains at least one identity field mapped to a recognized namespace.

Learn how to configure datasets [on this page](/en/docs/journey-optimizer/using/data-management/datasets/get-started-datasets).

See also the [data management overview](/en/docs/journey-optimizer/using/data-management/gs-data) for the full setup checklist.

How do I monitor and resolve data ingestion failures?
Ingestion failures appear in the **Monitoring** dashboard of Adobe Experience Platform under **Sources** > **Dataflows**. Common causes include schema validation errors (a field in the source data does not match the XDM schema), missing required identity fields, or malformed JSON payloads. Open the failed batch record to see the specific error code and affected rows. Correct the source data and re-ingest, or adjust the schema mapping if the source format has changed.

Learn more about schemas and data setup [on this page](/en/docs/journey-optimizer/using/data-management/gs-data).

## Profiles and Audience management ajo-troubleshooting-audiences

How to resolve audience count discrepancies?
The number of processed entries in the **Read Audience** feature of Adobe Journey Optimizer can be lower than the expected audience count. This issue often arises due to incorrect namespace configurations, leading to profiles being excluded from journeys. The resolution involves checking and correcting namespace configurations, reviewing relevant documentation, and adjusting priorities to ensure smoother operations in Adobe Journey Optimizer.

Learn more about the **Read Audience** activity in journeys [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience).

Why are profile updates failing?
In Adobe Journey Optimizer, certain field values may not update correctly after running through an **Update Profile** activity in a journey. In some cases, updated fields can disappear or revert to their previous state. To address this, check for conflicting rules or conditions, review permissions settings, use a unique dataset for the **Update Profile** activity, and ensure no other ingestion process is writing to the same profile at the same time.

Learn more about the **Update Profile** activity in journeys [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/update-profiles).

Why is there a mismatch in profile count entering a journey vs. in the associated audience?
The discrepancy can happen when the journey uses a previous day’s profile snapshot if the current day’s snapshot is not available at the time of journey execution. To investigate, check when your daily segmentation job last ran and whether the journey was triggered before the snapshot was ready.

Learn more about the **Read Audience** activity and scheduling behavior [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience).

Why does the audience picker show different profile counts in Campaigns versus Journeys?
You may notice that the same audience displays different profile counts when viewed in Campaigns compared to Journeys. This happens because each feature uses different APIs to retrieve audience data, which can return different values.

This is expected behavior and does not impact your campaign execution - the correct profiles will still be targeted. To check the actual audience size, go to **Customer** > **Audiences** and select your audience.

How to resolve audience population issues?
Audience population problems can occur when components or resources are missing, often due to entitlement, provisioning, or permission misconfigurations. To fix these issues, start by verifying entitlements, ensuring correct provisioning, and reviewing permissions. If the problem persists, escalate the case and coordinate with support teams for a complete resolution.

Learn more about managing audiences [on this page](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences).

Why has the Engageable Profiles count increased significantly in a short period?
The **Engageable Profiles** metric reflects the number of unique profiles engaged by journeys or campaigns over the past 12 months. A sudden increase may result from journeys or campaigns targeting large audiences that haven’t been engaged recently, or from changes in datasets enabled for Profile Service.

To investigate and resolve this issue, you need to understand the profile counting logic, investigate journeys and campaigns targeting large audiences, filter audiences appropriately, monitor dataset changes, and potentially reduce your addressable audience size.

Learn how to troubleshoot and resolve Engageable Profiles increases and monitor your organization’s license usage in the [License Usage Dashboard documentation](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage#troubleshooting-engageable-profiles).

Why are emails sent to individuals outside the intended audience based on date functions?
Emails may be sent to recipients who **do not meet the specified audience criteria**. For example, members with redemption dates **before July 4th, 2025** may receive emails intended only for those after that date. This behavior can result from **misconfigured audience segmentation** or **unexpected changes in profile qualification logic**. Review the audience definition and test with sample profiles to verify the date logic is applied correctly.

Learn more about date functions [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/date-functions).

Why do Delivered + Exclusions exceed my targeted audience size in campaign reports?
In campaign reports, you may notice that the sum of **Delivered** and **Exclusions** exceeds the original targeted audience size. This occurs because the **Exclusions** metric counts all exclusion events, including duplicate exclusion events for the same profile. If a profile is excluded multiple times during a campaign, each event is counted separately.

**Example**: A campaign targeting 94,000 profiles shows 69,000 delivered and 37,000 exclusions, totaling 106,000—which exceeds the original 94,000 targeted profiles. This is expected behavior.

To understand the difference between total exclusion events and unique profile exclusions, refer to the [Exclusion counting explanation](/en/docs/journey-optimizer/using/reporting/channel-report/exclusion-list#exclusion-list).

Learn more about [Campaign reports](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja) and [Report metrics](/en/docs/journey-optimizer/using/reporting/channel-report/global-report-components-cja).

How do I resolve audience selection issues and Chrome errors when saving journeys?
Adding audiences to journey conditions may sometimes cause **application crashes** or display an **Aw Snap error** in Chrome, including errors when saving journeys. These issues are often related to **Chromium services**. To resolve them, apply a **browser update**, clear the browser cache, or try a different browser session.

Learn more about [navigating the Journey Optimizer interface](/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface).

## Journeys ajo-troubleshooting-journeys

For Journeys, refer to the following troubleshooting sections:

- [Troubleshoot errors before testing your journey](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting)
- [Troubleshoot inbound actions in journeys](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-inbound)
- [Troubleshoot your live journey execution](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution)
- [Troubleshoot custom actions](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshoot-custom-action)

Why are expressions lost when creating a new journey version?
When creating a new version of a journey, **expressions in specific steps** may be lost, causing errors and requiring manual re-entry. To resolve this, **duplicate the journey**, test for reproducibility, **avoid browser reloads**, and use the **updated canvas** for older journeys.

Learn how to duplicate a journey [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/journey-ui#duplicate-a-journey).

Why do profiles exit journeys prematurely?
Profiles may exit a journey unexpectedly without passing through a designated node when the **condition checking feedback status** of sent messages is misconfigured. To resolve this, review the **condition logic**, implement **alternative logic**, or consult with your **implementation team**.

See also [Journey design guidelines](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer).

Why are profiles exiting journeys unexpectedly?
Profiles may exit a journey unexpectedly when **event capping** occurs, causing some profiles to be discarded if the number of events processed exceeds system capacity. To reduce profile exits, understand the **system limits**, monitor for **event spikes**, and optimize **data flow** to prevent exceeding thresholds.

See also [Journey guardrails](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#decisioning-guardrails).

Why is my event not triggering the intended journey?
Events may fail to trigger a journey even if all criteria are met when they are **created through query services** rather than being streamed to the **Data Collection Core Service (DCCS)**. To resolve this, review the event configuration, ensure events are **streamed directly to DCCS**, and verify functionality using **test mode**.

Learn more about events [on this page](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).

See also [Journey Event guardrails](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#events-g).

How do I resolve journey trigger issues after audience changes in Adobe Journey Optimizer?
If a journey stops triggering after modifications to its associated audience — such as changes to the merge policy — you may experience interrupted flows. To resolve this, **duplicate and republish the journey** with the updated audience settings to ensure triggers function correctly.

Learn how to duplicate a journey [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/journey-ui#duplicate-a-journey).

Why does a custom action calling an external third-party endpoint time out?
Timeout errors can occur when a **custom action** calls an external third-party endpoint. To resolve this, verify that the **endpoint is accessible**, check **server logs**, ensure there is **no blocking from Adobe**, update endpoint configurations as needed, and **test after updates**. Also, be mindful of **API call timeout specifications**.

Learn more about Journey Throttling API [on this page](/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling).

See also the [Integration with external systems documentation](/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems).

What steps should you take if you encounter a 403 error with the message
invalid<>access
or
No access to this dataId=XX granted
when publishing an audience from a journey?
To resolve this error, ask your administrator to verify that your user profile has access to the required data views for audience publishing, then try publishing the audience again.

Refer to [the permissions documentation](/en/docs/journey-optimizer/using/access-control/permissions) to learn steps to resolve this issue.

## Rules ajo-troubleshooting-rules

Why is the Capping rules dropdown not working?
Issues with the **Capping rules dropdown** often occur when rule sets are **misconfigured** or **inaccessible**. Ensure that all rule sets are correctly configured and available to resolve the problem.

Learn how to apply capping rules [in this section](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets).

Why is a frequency capping rule not being applied to my campaign or journey?
Frequency capping rules only take effect when the rule set is explicitly attached to the campaign or journey. If capping is not working, verify that the correct rule set is selected in the campaign or journey settings, that the rule’s channel type matches the channel being used, and that the rule is in **Active** status. Also check whether the profile already reached the cap in a previous run, which would prevent further messages even if the rule appears correctly configured.

Learn how to configure channel capping rules [on this page](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/channel-capping).

How do I configure quiet hours to prevent messages from being sent at night?
Quiet hours are time-based exclusion rules configured within a **Channel rule set**. Define the blackout window (for example, 10 PM to 8 AM) and apply the rule set to the relevant campaigns or journeys. When a message is scheduled to send during quiet hours, Journey Optimizer either holds the message until the next allowed window or discards it, depending on the rule configuration.

Learn how to set up quiet hours [on this page](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/quiet-hours).

## Decisioning ajo-troubleshooting-decisioning

How do I resolve issues when creating offer collections?
Difficulties creating offer collections often occur when **catalogs have not been provisioned** for your organization. To resolve this, verify that all required catalogs are correctly provisioned before attempting to create offer collections.

Learn more about offer collections [on this page](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/managing-offers-in-the-offer-library/creating-collections).

Why am I unable to access Offer Decisioning?
When integrating Adobe Target into an application using Adobe Journey Optimizer, the **Offer Decisioning** option may be inaccessible within the Datastream configuration. This typically occurs due to **permission settings** or **provisioning constraints**. To resolve the issue, verify user permissions and ensure the necessary provisioning is in place.

Learn more about required permissions for Offer Decisioning [on this page](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/get-started-decision/starting-offer-decisioning#granting-acess-to-decision-management).

Why is an offer not being returned even though it meets the eligibility criteria?
If a qualifying offer is not appearing in a decisioning response, check the following in order: verify the offer is in **Approved** (not Draft) status; confirm the placement ID in the request matches the offer’s representation surface; check whether any capping limit (total or per profile) has been reached for that offer; and ensure the collection and decision scope are correctly configured. Use the **Simulation** tool in Experience Decisioning to test offer responses against a specific profile without sending live traffic.

Learn how to get started with Experience Decisioning [on this page](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/gs-experience-decisioning).

## Multilingual ajo-troubleshooting-multilingual

How to resolve this issue
Message validation error (CJMMAS - 1069-500)
?
In Adobe Journey Optimizer, a Message Validation Error (CJMMAS - 1069-500) linked to the multilingual feature prevents journeys from being set to Test mode or Published. Verify that all locale content is complete, that the primary language is correctly set, and that no required translation fields are empty before attempting to publish.

Learn more about multilingual content [on this page](/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-gs).

Why is the translation provider not connecting in Journey Optimizer?
Translation provider connection failures are usually caused by incorrect API credentials or a missing provider configuration in the multilingual settings. Verify that the API key, endpoint URL, and any required authentication tokens entered in Journey Optimizer match exactly what your translation vendor has provisioned. If credentials are correct, check whether the provider account has sufficient quota or active subscription status, then save and retest the connection.

Learn how to configure a translation provider [on this page](/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-provider).

What happens when a translation is missing for a locale?
If a translation has not been provided for a specific locale, Journey Optimizer falls back to the content defined in the **primary language** (fallback locale) configured in your language settings. If no fallback is configured, the message may render as empty or fail validation before sending. To prevent this, always define a fallback locale in your multilingual project settings and verify that all locales have approved translations before activating the campaign or journey.

Learn more about multilingual content setup [on this page](/en/docs/journey-optimizer/using/content-management/content-multilingual/multilingual-gs).

## Configuration ajo-troubleshooting-config

How do I enable TLS v1.3 for Custom Actions?
To maintain **data integrity and security** when connecting to third-party systems, ensure that Transport Layer Security (**TLS**) v1.3 is enabled for your custom actions. This helps protect communications and prevents potential security vulnerabilities.

Learn more about custom action configuration [on this page](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration).

Why am I unable to create a dashboard directly from a query in Adobe Journey Optimizer?
In Adobe Journey Optimizer, dashboards cannot be created directly from queries. To build dashboards, use the available **dashboard creation functionalities** within Adobe Experience Platform, which allow you to visualize and analyze query data effectively.

Learn more about queries in Journey Optimizer [on this page](/en/docs/journey-optimizer/using/data-management/get-started-queries).

Why are my messages being blocked by the suppression list?
Addresses are automatically added to the suppression list after hard bounces, spam complaints, or manual additions by an administrator. Once suppressed, a profile will not receive any messages from that channel regardless of campaign or journey targeting. To investigate, open **Administration** > **Channels** > **Suppression list** and search for the address. If the suppression was added in error, it can be removed directly from the interface. For hard-bounce suppressions, also review the underlying deliverability issue before removing the address.

Learn how to manage the suppression list [on this page](/en/docs/journey-optimizer/using/configuration/monitor-reputation/manage-suppression-list).

## APIs ajo-troubleshooting-apis

How do I resolve access issues with the Query Service API?
Access errors when using the **Query Service API** via Postman or similar tools are usually caused by **insufficient permissions**. To resolve this, verify user permissions, check API credentials against the roles configured in your organization, and provide detailed information to support if needed.

Learn more about permissions in Journey Optimizer [on this page](/en/docs/journey-optimizer/using/access-control/permissions).

How do I resolve 429 Too Many Requests errors when calling Journey Optimizer APIs?
A 429 response means your integration has exceeded the API rate limit for the endpoint. Each Journey Optimizer API has defined throughput thresholds. To resolve this, implement **exponential backoff** logic in your integration: wait for the duration specified in the Retry-After response header before retrying. For sustained high-volume use cases, review the throttling and capping configuration for your custom actions and data sources to align API call rates with system limits.

Learn more about Journey Optimizer throttling [on this page](/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling).

See also the [external systems integration documentation](/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems).

Why is my API-triggered campaign not executing after the API call?
If an API-triggered campaign is not executing, verify the following: the campaign is in **Live** status (not draft or stopped); the API call includes the correct campaign ID in the endpoint path; the request payload matches the profile identifier schema expected by the campaign; and the API credentials used have the **Manage Campaigns** permission. Check the campaign’s execution logs in the reporting dashboard to identify whether the profile was received but excluded, or whether the call did not reach the campaign at all.

Learn more about API-triggered campaigns [on this page](/en/docs/journey-optimizer/using/campaigns/api-triggered-campaigns/api-triggered-campaigns).

recommendation-more-help
