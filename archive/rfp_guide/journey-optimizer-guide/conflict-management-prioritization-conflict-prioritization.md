---
title: "Conflict management & prioritization conflict-prioritization"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/gs-conflict-prioritization"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:42.444875+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Conflict management & prioritization conflict-prioritization

Last update: May 8, 2026
CREATED FOR:

- Beginner
- User

In Journey Optimizer, managing the volume and timing of campaigns and journeys is essential to avoid overwhelming customers with too many interactions. Conflict management and prioritization tools help you deliver thoughtful, well-timed communications—preventing customer fatigue and ensuring the right messages reach your audience. By using conflict detection, priority scores, and rule sets, you can streamline campaigns and journeys to avoid overlaps and balance frequency across channels.

These tools are available for campaigns and for unitary, Audience Qualification, and Read audience journeys. Whether you’re setting limits on how often messages are sent or deciding which campaigns take precedence, these features work together to simplify decision-making and optimize your marketing strategy.

## Where to start where-to-start

Your goal
Tool
Action
See if journeys or campaigns overlap (timeline, audience, channel)
Conflict detection
Identify potential conflicts
Decide which message wins when a profile qualifies for several
Priority scores
Assign priority scores
Limit how often or how many messages a profile receives
Rule sets
(frequency capping, journey capping, quiet hours)
Set message & journey capping rules
**Typical flow:** Use conflict detection to spot overlaps, then apply priority scores and rule sets to control which messages are sent and how often.

## Conflict management & prioritization tools tools

### Conflict detection tool

With the **conflict detection tool**, you can identify potential overlaps in journeys and campaigns. This is crucial as too many simultaneous communications can lead to customer fatigue. Journey Optimizer allows you to monitor elements such as timelines, audience overlap, and channel configurations. By identifying conflicts early, you can refine your campaigns to avoid bombarding customers with multiple messages at the same time.

[Learn how to detect potential conflicts in journeys & campaigns](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts)

### Priority scores

**Priority scores** help you control which campaigns or journeys take precedence when a customer qualifies for multiple communications. This is especially useful for inbound channels such as web and mobile, where only one campaign can be shown at any given time. By assigning a priority score to each journey or campaign, you can ensure that the most important message is delivered first.

[Learn how to assign priority scores to journeys & campaigns](/en/docs/journey-optimizer/using/conflict-prioritization/priority-scores)

### Rule sets

Rule sets allow you to **group together multiple rules** and apply them to the journeys and campaigns of your choice. This provides improved granularity to limit how often and how many journeys a customer can enter within a certain time frame, or to control how often users receive messages depending on the type of communication.

- Journey capping & arbitration – Limit how often and how many journeys a customer can enter within a certain time frame. You can cap the number of journey entries for a profile or limit the number of journeys a customer can be enrolled in at the same time. Use arbitration settings to decide which journey a customer should enter if they qualify for multiple journeys, using priority scores to determine the best fit. Learn how to work with journey capping & arbitration
- Frequency capping by channel and communication type – Set frequency capping by communication type (e.g., Sales, Promotional) to prevent overloading customers with similar messages. Control frequency across multiple channels, automatically excluding over-solicited profiles. Learn how to set frequency capping by channel and communication type
- Quiet hours – Define time-based exclusions so no messages are sent during specific periods (Email, SMS, Push, WhatsApp). Learn how to set quiet hours

[Learn how to work with rule sets](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets)

## Guardrails & limitations guardrails

- Campaigns & priority scores - In campaigns, priority score is available for the web , in-app , and code-based inbound channels only.
- Profile counter update latency - It can take up to 10 minutes after a customer has entered a journey for the profile counter value to be updated. If a profile enters two journeys within a short window, the second journey may not correctly recognize that the frequency cap has already been reached, potentially allowing the profile to enter both journeys.
- Namespace priority for journey entry capping - Entry capping is only supported if the namespace selected in the journey is the highest priority namespace defined in the sandbox. If namespace priority hasn’t been explicitly configured, the default highest priority is email.
- Simultaneous activations in audience qualification journeys - When multiple audience qualification journeys are activated by the same audience qualification event, counts for entry capping will not be accurate. If counts are below the cap, the journey will continue to arbitrate, but it will not be able to get the most up-to-date counts with simultaneous activations.

## Additional resources

- **Identify potential conflicts** - Learn how to detect and resolve conflicts between overlapping campaigns and journeys.
- **Assign priority scores** - Understand how to assign and use priority scores to control message delivery precedence.
- **Work with rule sets** - Learn how to build and apply rule sets for conflict management and message governance.
- **Journey capping & arbitration** - Set up journey-level capping rules and arbitration.
- **Frequency capping by channel** - Set channel-level frequency caps to prevent over-messaging.
- **Set quiet hours** - Define time-based exclusions for message delivery.
- **Conflict management tutorials** - Step-by-step video tutorials.

recommendation-more-help
