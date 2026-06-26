---
title: "Work with journey entry and exit criteria entry-exit-criteria-guide"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/entry-exit-criteria-guide"
category: "guides"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:51.244269+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with journey entry and exit criteria entry-exit-criteria-guide

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Profiles](#)

CREATED FOR:

- Intermediate
- User

In customer experience orchestration, delivering the right message at the right time requires precise control over when customers enter and exit your journeys. Understanding and properly configuring entry and exit criteria can make the difference between a successful, engaging campaign and missed opportunities or message fatigue.

This guide provides practical guidance, real-world examples, and best practices for managing journey entry and exit criteria in Adobe Journey Optimizer.

## What are entry and exit criteria? what-are-criteria

**Entry criteria** determine the conditions under which a [customer profile](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/get-started-profiles) qualifies to enter a specific journey. Profiles can enter based on:

- Customer behavior - Actions taken by customers trigger journey entry in real-time, such as making a purchase, abandoning a cart, or opening your mobile app.
- Profile attributes - Customer characteristics determine eligibility based on data stored in their profile, like loyalty tier, location, age, or communication preferences.
- External events - Business or environmental triggers that affect multiple customers simultaneously, such as low inventory alerts, weather conditions, or price changes.
- Audience membership - Belonging to a specific audience segment enables targeted journeys for groups like high-value customers, inactive users, or new subscribers.

**Exit criteria** define when and how a profile leaves or is removed from a journey:

- Journey completion - Profiles automatically exit when they reach the end of all journey paths , completing the designed experience.
- Success metric achievement - Profiles exit when they complete the journey objective , such as making a purchase or downloading an app, eliminating unnecessary follow-up communications.
- Condition-based - Profiles exit when specific conditions are met, like inactivity over a set period or changes in profile attributes.
- Event-based - Profiles exit when specific events occur , such as subscription cancelation or product return.
- Audience disqualification - Profiles exit when they no longer meet the target audience criteria , ensuring messages remain relevant.

## Why entry and exit criteria matter why-they-matter

Properly defining entry and exit criteria delivers significant business value:

- Relevance : Only the right customers enter the journey, increasing engagement and conversion rates by targeting the most appropriate audience at the optimal time.
- Efficiency : Prevents customers from staying in irrelevant journeys, reducing unnecessary communications, operational costs, and customer annoyance.
- Personalization : Enables dynamic tailoring of experiences based on real-time data and behavior, creating more meaningful customer interactions.
- Compliance : Helps manage frequency capping and avoid over-communication, respecting customer preferences and regulatory requirements while maintaining brand reputation.

## Real-world examples of journey entry and exit real-world-examples

Here are common scenarios that demonstrate how entry and exit criteria work in practice:

**Welcome campaign for new subscribers**

Create a personalized first impression by automatically guiding new subscribers through an introduction to your brand, products, and services.

- **Entry**: Profiles enter the journey when they subscribe to a newsletter
- **Exit**: Profiles exit once they have completed a welcome series of emails or after a set time if they do not engage
- **Benefit**: Ensures new subscribers receive timely onboarding while avoiding repetitive messaging

**Abandoned cart recovery**

Recapture lost revenue by reminding customers about items they left behind and providing incentives to complete their purchase.

- **Entry**: Customers enter the journey if they add items to a cart but do not complete checkout within 24 hours
- **Exit**: Profiles exit when they complete the purchase or after 7 days if no purchase is made
- **Benefit**: Drives conversions by timely reminders without spamming uninterested customers

**Loyalty program engagement**

Reward your most valuable customers with exclusive benefits and personalized communications that strengthen brand loyalty and increase lifetime value.

- **Entry**: Customers join the journey after reaching a certain loyalty points threshold
- **Exit**: Profiles exit after redeeming rewards or if inactive for 60 days
- **Benefit**: Keeps high-value customers engaged with personalized offers and avoids communication fatigue

**Product feedback collection**

Gather insights about customer satisfaction and product performance by requesting feedback at the optimal moment after delivery.

- **Entry**: Customers enter the journey after receiving a product delivery confirmation event
- **Exit**: Profiles exit once feedback is submitted or after 10 days if no response
- **Benefit**: Captures valuable feedback promptly without annoying customers with persistent requests

## How to configure journey entry criteria configure-entry

**Learn everything you need to know about Entry Criteria here:**

- Event-Based Triggers : Use events like “profile creation,” “transaction completed,” or custom events to kick off a journey. Configure events in Administration > Events and define event schema and fields . Then add the event from the Events palette in the journey designer .
- Audience-Based Entry : Target journeys to profiles who belong to specific audiences, either as a one-time batch or on a recurring schedule. Create audiences in the Audiences menu, then add a Read Audience activity and configure the schedule . After entry, use conditions to segment, exclude, or merge branches .
- Audience Qualification Entry : Trigger journeys when profiles qualify for or exit from specific audiences in real-time. Define streaming audiences , add an Audience Qualification event from the Events palette, and choose the trigger type.
- Attribute Filters : Refine entry criteria by combining events or audiences with profile attributes and context using AND/OR logic. Use conditions to reference profile attributes , events, or external data .
- Time Windows and Scheduling : Set temporal constraints to keep journeys timely and relevant. Configure schedules on Read Audience activities , use Wait activities , and add time-based conditions to control timing.

style
shade-box
## How to set up journey exit criteria configure-exit

**Learn everything you need to know about Exit Criteria here:**

- Journey Completion : Profiles automatically exit after they reach the final journey step. Design journey paths to end at End activities.
- Success Metric Achievement : Define success metrics (like purchase or subscription) and exit profiles upon completion. Click Show exit criteria icon, select Add exit criteria , and choose an Event or Audience as the exit trigger.
- Inactivity Timeouts : Exit profiles if no engagement occurs within a set timeframe. Use Exit Criteria with audiences that check last engagement date, set Wait activities with defined durations, and use conditions to check for activity.
- Re-entry Rules : Decide if profiles can re-enter the journey multiple times or only once, depending on your campaign strategy. Configure Re-entrance settings in journey Properties to set wait periods, enable forced re-entrance, or use supplemental identifiers for context-specific re-entrance.

style
shade-box
## Detailed journey examples journey-examples

For step-by-step implementation guidance with complete technical details, explore these documented use cases:

- Customer onboarding journey - Build personalized welcome experiences with audience qualification, event timeout, and goal-based exits
- Abandoned cart recovery - Recover lost sales with event-triggered journeys, playbooks, and channel routing
- Re-engagement campaigns - Win back inactive customers with behavioral targeting and paid media activation
- Send messages to subscribers - Target subscription lists with Read Audience and personalized content
- Send multi-channel messages - Combine email and push with reaction events and multi-path logic
- Send emails only on weekdays - Schedule communications using time-based conditions and wait formulas

TIP
Browse all available use cases in the
Journey use cases library
for more patterns and implementations. Examples include
ramp up deliveries
,
experience event patterns
, and
removing profiles from live journeys
.
## Best practices for managing entry and exit best-practices

**Clear definition**

Establish clear documentation and naming conventions to ensure your team understands how profiles move through your journeys:

- Document your entry and exit logic before building journeys to align marketing and analytics teams
- Create flowcharts showing entry points, journey paths, and exit conditions
- Define business rules clearly: “Profiles exit when X happens OR after Y days”
- Use descriptive labels: “Exit - Purchase Completed” not “Exit 1”
- [Tag journeys](/en/docs/journey-optimizer/using/get-started/work-efficiently/search-filter-categorize#tags) consistently for reporting and filtering

**Avoid overlapping journeys**

Prevent customer confusion and message conflicts by coordinating your journey strategy across campaigns:

- [Audit active journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/journey-ui) before launching similar ones to prevent conflicts
- Leverage [conflict management](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts) and [priority scores](/en/docs/journey-optimizer/using/conflict-prioritization/priority-scores) to resolve overlaps and prioritize journeys
- Design journeys that complement rather than compete with each other

NOTE
For advanced scenarios like automatically removing profiles when they qualify for higher-priority journeys, use
journey capping & arbitration
instead of exit criteria.
**Monitor and optimize**

Continuously evaluate journey performance and refine your entry and exit criteria based on real customer behavior:

- Track entry rate, exit rate, and completion rate for each journey using [journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja)
- Monitor [success metrics](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/success-metrics): percentage exiting via success metric completion vs. timeout
- [Test entry and exit criteria](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) with various profile scenarios before launching
- Adjust based on data: If high early exits, review entry criteria relevance; if low success metric completion, analyze content and timing
- Review all active journeys quarterly

**Respect frequency caps**

Maintain customer trust and engagement by controlling message frequency across all your journey communications:

- Set appropriate [re-entrance wait periods](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management) or disable re-entrance for one-time journeys
- Use [frequency capping rules](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets) to prevent over-communication
- Monitor frequency metrics in reporting to ensure compliance

NOTE
To manage frequency limits and journey entry caps across multiple journeys, use
journey capping & arbitration
and
frequency capping by channel
.
## Conclusion conclusion

Journey entry and exit criteria are foundational to delivering personalized, timely, and effective customer experiences with Adobe Journey Optimizer. By carefully crafting these conditions, marketers can boost engagement, reduce friction, and build stronger customer relationships.

Start by clearly mapping your customer triggers and exit points, test thoroughly, and monitor results to continuously refine your journey orchestration.

## Related resources related-resources

**Technical documentation**

[Profile entrance management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management) | [Journey properties and exit criteria](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties) | [How journeys end](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey) | [Supplemental identifiers](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/supplemental-identifier) | [Journey designer](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer)

**Tutorials and examples**

[Journey use cases](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/jo-use-cases) | [Customer onboarding video](/en/docs/journey-optimizer-learn/tutorials/use-cases/customer-onboarding) | [Abandoned cart video](/en/docs/journey-optimizer-learn/tutorials/use-cases/abandoned-cart) | [Community blog: Entry and Exit Criteria](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/mastering-journey-entry-and-exit-criteria-in-adobe-journey/ba-p/760958)

**Related capabilities**

[Audience qualification events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events) | [Success metrics and goals](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/success-metrics) | [Conflict management](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts) | [Frequency capping](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets) | [Testing journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) | [Optimize activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize) | [Reaction events](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events) | [Wait activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity)

recommendation-more-help
