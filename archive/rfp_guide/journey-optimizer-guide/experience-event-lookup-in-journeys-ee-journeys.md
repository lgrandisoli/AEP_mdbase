---
title: "Experience event lookup in journeys ee-journeys"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/exp-event-lookup"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:08.821460+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Experience event lookup in journeys ee-journeys

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

CAUTION
Starting July 8 2025, in new customer organizations, creating expressions using experience events is no longer supported in the expression editor used in journey conditions. As a result, experience events in the
Experience Platform data source
cannot be used for creating expressions.
Starting April 1, 2026, the use of experience event attributes in journey expressions will no longer be supported for organizations that have not used this capability in the last 90 days. Alternative approaches and best practices for creating expressions/logic with experience events are referenced below.
Need more details?
Read out the FAQ
.
This page outlines common patterns and scalable approaches to help you make the most of Experience Events in Adobe Journey Optimizer. These use cases are designed to help you solve frequent challenges such as managing opt-outs, controlling message frequency, personalizing content based on user behavior, and reacting to real-time signals.

By leveraging these strategies, you can turn behavioral data into meaningful actions—suppressing, qualifying, or excluding profiles based on the events they trigger or the attributes they carry. Whether you’re building logic for purchase thresholds, abandonment triggers, or bounce handling, these examples offer practical guidance you can adapt to your needs.

As you evaluate which approach fits best, consider the latency requirements of your use case to ensure your journeys remain responsive and effective.

## Opt-out suppression

To suppress profiles that have opted out of marketing communications, use built-in consent management. Opt-out preferences are automatically captured in the profile’s consent fields; they can be referenced directly in journey conditions and are automatically enforced by Journey Optimizer during message delivery.

Learn more:

- [Manage consent](/en/docs/journey-optimizer/using/privacy/consent/opt-out)
- [Email opt-out management](/en/docs/journey-optimizer/using/channels/email/email-opt-out)
- [Opt-out management for text messages](/en/docs/journey-optimizer/using/channels/sms/sms-opt-out)

## Bounce-based suppression

To exclude profiles that have experienced email bounces, leverage Adobe Journey Optimizer’s automatic suppression list for bounced addresses. This built-in mechanism ensures that invalid or unreachable emails are excluded from future sends without requiring custom logic.

Learn more:

- [Manage the suppression list](/en/docs/journey-optimizer/using/configuration/monitor-reputation/manage-suppression-list)

## Generic suppression

To suppress profiles that have demonstrated certain behaviors, use batch audiences with event-based logic to capture profiles that meet the suppression criteria. Reference this audience in journey conditions.

Learn more:

- Adobe Experience Platform Segment builder - Events
- Adobe Experience Platform Segment builder – Time constraints
- Using audiences in conditions
- inAudience() function

## Communications-received exclusion

To prevent sending messages to profiles who have received any communications within a recent time window:

- Use batch audiences with time-based criteria and reference them in journey conditions.
- Apply frequency capping business rules to enforce daily or weekly message limits.

Learn more using audiences:

- Adobe Experience Platform Segment builder - Events
- Adobe Experience Platform Segment builder – Time constraints
- Using audiences in conditions
- inAudience() function

See also:

- [Frequency capping by channel and communication type](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/channel-capping)

## Message-specific inclusion/exclusion

To include or exclude profiles based on whether they received a specific message, create batch audiences that encapsulate this logic and reference them in journey conditions.

Learn more:

- Adobe Experience Platform Segment builder - Events
- Adobe Experience Platform Segment builder – Time constraints
- Using audiences in conditions
- inAudience() function

## Cart or browse abandonment personalization

To personalize communications based on the latest cart or browse events across multiple cart types or product views:

- If you have access to [Adobe Experience Platform Data Distiller](/en/docs/experience-platform/query/data-distiller/overview#_blank), configure automated queries to extract the required data from the event, manipulate it to fit the use case, and write it back to a [profile-enabled dataset](/en/docs/experience-platform/catalog/datasets/user-guide#enable-profile#_blank) for activation.
- If the abandonment data can be modeled on the profile with scalar attributes, consider using Computed attributes to capture the latest information and then reference these attributes in the journey to construct the communication. [Learn more in Adobe Experience Platform documentation](/en/docs/experience-platform/profile/computed-attributes/overview#_blank)

## Behavior-based journey exit

To remove profiles from journey when they exhibit a particular behavior, utilize exit criteria to exit the profile from the journey when a particular event is received or the profile qualifies for a specific audience.

Learn more:

- [Set your journey properties - Exit criteria](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#exit-criteria)

## Purchase-based qualification with value thresholds

To trigger journeys based on purchases and suppress if value is above/below a threshold, define computed attributes to sum purchases over a specific time period. Create an audience that includes profiles whose spending amount meets certain criteria.

Learn more:

- Adobe Experience Platform [Computed attributes overview](/en/docs/experience-platform/profile/computed-attributes/overview#_blank)

## Frequently asked questions faq-ee

This FAQ focuses on the timeline for retiring experience event usage in journey expressions and who is impacted. For guidance on alternative approaches, see the use cases and best practices above.

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with the [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en#_blank).

What specific capabilities are impacted?
Only the lookup of experience events in the expression editor is impacted. The following capabilities are **not** impacted and remain the same:

- Observing the experience events associated with a specific profile in the profile UI
- Using experience events in computed attribute rules and accessing the computed attributes in a journey
- Triggering a journey with a unitary or business event
- Using journey context data from the events that trigger the journey in the expression and personalization editors
- Listening to an event within a journey
- Configuring events to trigger a journey
- Detecting end user reaction events to marketing communications (e.g., email open)

Are my existing Adobe Organization impacted by this update?
Starting July 8, 2025, new customer organizations cannot create expressions using experience event attributes. Starting April 1, 2026, organizations that have not accessed experience events via journey expressions in the last 90 days will no longer have access to this capability.
I have a new Adobe Organization. How can I solve my use case requiring experience event data?
Alternative approaches and best practices involving experience events are available above to achieve desired use cases.
What if alternative approaches do not work for my use case?
If your use case cannot be solved using one of the alternative approaches listed above, please reach out to your Adobe representative.
recommendation-more-help
