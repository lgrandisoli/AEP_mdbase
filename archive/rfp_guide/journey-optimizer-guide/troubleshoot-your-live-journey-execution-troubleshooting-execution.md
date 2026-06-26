---
title: "Troubleshoot your live journey execution troubleshooting-execution"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:16.349727+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Troubleshoot your live journey execution troubleshooting-execution

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Monitoring](#)

CREATED FOR:

- Intermediate
- User

In this section, learn how to troubleshoot journey events, check if profiles entered your journey, how they navigate through it, and if messages are sent.

You can also troubleshoot errors before testing or publishing a journey. Learn how [on this page](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting).

If you are using inbound actions, learn how to troubleshoot them [on this page](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-inbound).

## Check that events are properly sent checking-that-events-are-properly-sent

The starting point of a journey is always an event. You can perform tests using tools such as Postman.

You can check if the API call you send through these tools is sent correctly or not. If you get an error back, it means that your call has an issue. Check the payload again, the header (and especially the organization ID) and the destination URL. You can ask your administrator what is the right URL to hit.

Events are not pushed directly from the source to journeys. Indeed, journeys rely on Adobe Experience Platform’s streaming ingestion APIs. As a result, in case of event related issues, you can refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/ingestion/streaming/troubleshooting#_blank) for Streaming ingestion APIs troubleshooting.

If your journey fails to enable test mode with error ERR_MODEL_RULES_16, ensure the event used includes an [identity namespace](/en/docs/journey-optimizer/using/audiences-profiles-identities/get-started-identity) when using a channel action.

The identity namespace is used to uniquely identify the test profiles. For example, if email is used to identify the test profiles, the identity namespace **Email** should be selected. If the unique identifier is the phone number, then the identity namespace **Phone** should be selected.

## Check if people enter the journey checking-if-people-enter-the-journey

Journey reporting measures people’s entrances in a journey in real-time.

If you are successfully sending the event but see no entrance in the journey, it means that something goes wrong between the event sending and the event reception in the journey.

You can start troubleshooting with the questions below:

- Are you sure the journey where you expect the incoming event is in test mode or live?
- Did you save your event before copying the payload from the payload preview?
- Does your event payload contain an event id?
- Did you hit the right URL?
- Did you follow the Streaming Ingestion APIs payload structure, using the payload structure preview in the event configuration pane? See this page .
- Did you use the right key-value pairs in the header of your event? code language-none X-gw-ims-org-id - your organization's ID Content-type - application/json
- Event condition and schema data types - Ensure the data types used in your event condition (rule) match the event schema. Mismatched types (for example, string vs. integer) cause rule evaluation to fail and events to be dropped. See Verify event identity .
- Event discarded – qualification condition not met - For rule-based events, if the qualification condition is not satisfied by the event payload (for example, a required field is empty or missing, or a condition such as isNotEmpty on a field fails), the event is received but discarded and the journey is not triggered. Logs and Splunk traces can show that the event was received but discarded because it did not meet the qualification condition, with discard codes such as notSuitableInitialEvent . This is expected behavior: if the qualification condition is not met, the event will be discarded and the journey will not be triggered for that profile. Verify your event payload contains the expected fields and values, and that the rule in the event configuration matches the data you send. If the event is triggered by a custom action from another journey, see Handling discard events and idle-timeouts in custom action troubleshooting.

**For Audience Qualification journeys with streaming audiences**: If you’re using an Audience Qualification activity as the journey entry point, be aware that not all profiles qualifying for the audience will necessarily enter the journey due to timing factors, quick exits from the audience, or if profiles were already in the audience before publishing. Learn more about [streaming audience qualification timing considerations](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events#streaming-entry-caveats).

### Verify event identity verify-event-identity-and-rule-data-types

When configuring an event-based journey, confirm that the payload’s identity field matches the [namespace selected in the event](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating#select-the-namespace). If the event includes fields for profile matching, verify the **letter case** and **data type** in the event condition exactly match the inbound data. For example, if the event schema defines roStatus as a string, the journey rule must also evaluate it as a string. Mismatched data types (for example, string vs. integer) cause rule evaluation to fail and valid events to be dropped. Similarly, if the event has a **qualification condition** (for example, a field must be non-empty), events that do not satisfy that condition are **discarded** and do not trigger the journey; logs may show discard codes such as notSuitableInitialEvent.

To validate your event condition in Journey Optimizer, use the payload preview in the event configuration and ensure the types and values in the rule match the payload structure. Learn how to [preview the payload](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating#preview-the-payload) and [configure rule-based events](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating).

## Troubleshoot test mode transitions troubleshooting-test-transitions

If test profiles fail to progress through your journey in test mode or the visual flow does not display green arrows indicating step progression, the issue may be related to transition validation. This section provides guidance on diagnosing and resolving common test mode issues.

### Test profiles not progressing

If test profiles enter the journey but do not advance past the initial step, check the following:

- Journey start date - The most common cause is when the journey’s start date is set in the future. Test profiles are immediately discarded if the current time falls outside the journey’s configured start and end dates/time window. To resolve: Verify the journey start date is not set in the future Ensure the current time falls within the journey’s active date window If necessary, update the journey properties to adjust the start date
- Test profile configuration - Confirm that the profile is correctly flagged as a test profile in Adobe Experience Platform. See how to create test profiles for more information.
- Identity namespace - Ensure the identity namespace used in the event configuration matches the namespace of your test profile.

### Null transition indicators

During technical troubleshooting, you may encounter an isValidTransition property set to null in the journey’s technical details. This UI-only property does not impact backend processing or journey performance. However, a null value can indicate:

- **Journey misconfiguration** - The journey start date is set in the future, causing test events to be silently discarded
- **Corrupted transition** - In rare cases, journey nodes may need to be reconnected

If you encounter persistent transition issues:

- Verify the journey start date is current
- Deactivate and reactivate test mode
- If the issue persists, consider duplicating the affected journey nodes and reconnecting them
- For unresolved cases, [contact support](/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface#support-ticket-guidelines) with journey logs, the impacted profile IDs, and details about the null transition

NOTE
Remember that events sent outside the journey’s active date window are silently discarded with no error message. Always verify your journey timing configuration first when troubleshooting test profile progression.
## Check how people navigate through the journey checking-how-people-navigate-through-the-journey

Journey reporting measures the progress of individuals inside a journey. It’s easy to identify where and why a person got stopped.

Here are a few things to check:

- Is it due to a condition excluding the person? For example, the condition is “gender = male” and the person is a woman. This check can be performed by a business user if the condition is not too complex.
- Is it due to a call to a data source not responding? When the journey is in test, this information can be seen in test mode logs. When the journey is live, an administrator can test direct calls to the data source and check the answer received. An administrator can also duplicate the journey and test it.

## Events discarded due to a blocked journey instance max-instance-stack-events-reached

If you see events discarded with the maxInstanceStackEventsReached reason, the journey runtime has reached its internal per-profile event stack limit of 10 events for a specific journey version. This is a safety guardrail that prevents too many pending events from stacking up while another event for the same profile is still being processed.

This is **not** a time-window or throughput limit. It occurs when the profile’s journey instance is blocked on a long-running step (for example, a long wait, enrichment, or custom action retries) and events for the same profile, also being used in that journey, pile up beyond the 10-event limit.

To identify it, query journey step events where the discard reason equals maxInstanceStackEventsReached (for example, in serviceEvents.stateMachine.eventType or similar fields). Learn more about discarded event types in the [step event field list](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

**What you can do**

- Reduce long waits or slow steps on paths that can re-trigger frequently.
- Deduplicate or debounce upstream events when possible.
- Split long-running scenarios into multiple journeys to avoid stacking.

## Check that messages are sent successfully checking-that-messages-are-sent-successfully

If individuals flow the right way in the journey but do not receive messages they should receive, you can check if:

- Journey Optimizer has correctly taken into account the request to send the message. Business users can access the message supposed to be sent and check if the time of the latest execution corresponds to the execution time of your journey. They can also check the latest API calls/events received.
- Journey Optimizer has successfully sent the message. Check the journey reporting to make sure that there are no errors.

In case of a message sent via a custom action, the only thing that can be checked during journey test is the fact that the call of the custom action’s system leads to an error or not. If the call to the external system associated with the custom action does not lead to an error but does not lead to a message sending, some investigations should be done on the external system’s side.

## Understanding duplicate entries in Journey step events duplicate-step-events

Use this section to understand why duplicate rows can appear in Journey Step Events.

### Why do i see multiple entries with the same journey instance, profile, node, and request ids?

When querying Journey Step Events data, you may occasionally observe what appears to be duplicate log entries for the same journey execution. These entries share identical values for:

- profileID - The profile identity
- instanceID - The journey instance identifier
- nodeID - The specific journey node
- requestID - The request identifier

However, these entries have **different _id values**, which is the key indicator that distinguishes this scenario from actual data duplication.

### What causes this behavior?

This occurs due to backend auto-scaling operations (also called “rebalancing”) in Adobe Journey Optimizer’s microservices architecture. During periods of high load or system optimization:

- A journey step event begins processing and is logged to the Journey Step Events dataset
- An auto-scaling operation redistributes workload across service instances
- The same event may be reprocessed by another service instance, creating a second log entry with a different _id

This is an expected system behavior and is **working as designed**.

### Is there any impact on journey execution or message delivery?

**No.** The impact is limited to logging only. Adobe Journey Optimizer has built-in deduplication mechanisms at the message execution layer that ensure:

- Only one message (email, SMS, push notification, etc.) is sent to each profile
- Actions are executed only once
- Journey execution proceeds correctly

You can verify this by querying the ajo_message_feedback_event_dataset or checking action execution logs - you’ll see that only one message was actually sent, despite the duplicate journey step event entries.

### How can I identify these cases in my queries?

When analyzing Journey Step Events data:

- Check the _id field : True system-level duplicates would have the same _id . Different _id values indicate separate log entries from the rebalancing scenario described above.
- Verify message delivery : Cross-reference with message feedback data to confirm only one message was sent: code language-sql SELECT timestamp, _experience.customerJourneyManagement.messageExecution.messageExecutionID, _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus FROM ajo_message_feedback_event_dataset WHERE _experience.customerJourneyManagement.messageExecution.journeyVersionID = '<journeyVersionID>' AND TO_JSON(identityMap) like '%<profileID>%' ORDER BY timestamp DESC;
- Group by unique identifiers : When counting executions, use _id to get accurate counts: code language-sql SELECT COUNT(DISTINCT _id) as unique_executions FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journeyVersionID>' AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID>'

### What should i do if i observe this?

This is normal system behavior and **no action is required**. The duplicate logging does not indicate a problem with your journey configuration or message delivery.

If you’re building reports or analytics based on Journey Step Events:

- Use _id as the primary key for counting unique events
- Cross-reference with message feedback datasets when analyzing message delivery
- Be aware that timing analysis may show entries clustered within a few seconds of each other

For more information about querying Journey Step Events, see [Examples of queries](/en/docs/journey-optimizer/using/reporting/reports/query-examples).

## Troubleshoot dashboard metric discrepancies dashboard-metrics

If the metrics displayed in the **Overview** dashboard do not match the actual number of journeys in the **Browse** tab, verify the following:

- Ensure the journeys in question have had traffic in the last 24 hours, as journeys without recent activity are excluded from the dashboard.
- Check that you have the appropriate access permissions to view all journeys in your organization.
- Allow up to 30 minutes for metrics to refresh after making changes to your journeys.

If discrepancies persist, [contact Adobe Support](/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface#support-ticket-guidelines) with screenshots of both the Overview and Browse tabs for investigation.

## Tracking parameters showing empty placeholders in closed journeys tracking-parameters-closed-journeys

If tracking URLs in sent emails contain empty placeholders such as cid=em-acou-adob{}, this may indicate that a context field such as context.system.source.actionId could not be resolved. This typically happens when a journey was closed and has not been republished after a relevant product change — only republished journeys correctly populate these context fields in tracking URLs.

To resolve this, either republish the journey ([create a new version and publish it](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey#journey-create-new-version)), or remove the reference to the affected context field from the [URL tracking parameters](/en/docs/journey-optimizer/using/channels/email/configure-email/url-tracking) in the channel configuration or email content.

recommendation-more-help
