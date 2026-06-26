---
title: "Work with journey step events work-with-journey-step-events"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/journey-step-events-overview"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:51.993315+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with journey step events work-with-journey-step-events

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Reporting](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin
- User

Journey step events are automatically generated events that capture detailed information about each step a [profile](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/get-started-profiles) takes as they progress through a [journey](/en/docs/journey-optimizer/using/orchestrate-journeys/journey) in Adobe Journey Optimizer. These events provide comprehensive visibility into [journey performance](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/report-journey) and enable powerful analytics capabilities.

## What are journey step events what-are-step-events

Journey step events are system-generated [XDM (Experience Data Model)](/en/docs/experience-platform/xdm/home#_blank) events that Adobe Journey Optimizer automatically creates and sends to [Adobe Experience Platform](/en/docs/experience-platform/landing/home#_blank) whenever a profile moves from one node to another in a journey. Each event corresponds to a specific [journey activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities) or transition in the customer’s journey experience.

There are two main types of journey step events:

- **journeyStepEvent**: Events related to individual profile progression through journey steps
- **journeyStepProfileEvent**: Events that include additional profile context information

### What triggers journey step events? event-triggers

Journey step events are generated automatically for various journey activities:

- **Entry events**: When a profile [enters a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management)
- **Action execution**: When [messages are sent](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action) or [custom actions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-custom-actions) are performed
- **Condition evaluation**: When profiles pass through [conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions) and decision points
- **Wait activities**: When profiles enter and exit [wait nodes](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity)
- **Exit events**: When profiles complete or [exit a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey)
- **Error handling**: When errors occur during journey execution

NOTE
Journey step events are activated by default on all instances. You cannot modify or update the
schemas and datasets
that have been created during provisioning for step events. These schemas and datasets are in read-only mode.
Learn more about [journey step event schemas](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list).

## Why journey step events matter why-step-events-matter

Journey step events provide critical value for organizations using Adobe Journey Optimizer:

### Real-time analytics and monitoring real-time-analytics

- **Journey performance tracking**: Monitor how profiles flow through your journeys in real-time using [live reports](/en/docs/journey-optimizer/using/reporting/live-report/live-report)
- **Conversion analysis**: Understand drop-off points and successful conversion paths with [journey analytics](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja)
- **Error detection**: Identify and troubleshoot issues as they occur through [monitoring and alerts](/en/docs/journey-optimizer/using/monitor/monitor-alerts-errors/alerts)

### Data integration and insights data-integration

- **Cross-platform analysis**: Combine journey data with other [Adobe Experience Platform data sources](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/adobe-experience-platform-data-source)
- **Customer 360 view**: Create comprehensive [customer profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/get-started-profiles) that include journey interactions
- **Attribution modeling**: Connect journey touch points to downstream business outcomes using [Customer Journey Analytics](/en/docs/journey-optimizer/using/reporting/channel-report/cja-ajo)

### Optimization opportunities optimization

- **A/B testing insights**: Analyze the performance of different journey paths using [experimentation](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-experimentation)
- **Personalization enhancement**: Use journey behavior data to improve future experiences with [dynamic content](/en/docs/journey-optimizer/using/content-management/dynamic/dynamic-content)
- **Operational efficiency**: Identify bottlenecks and optimize [journey design](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer)

## How to use journey step events how-to-use-step-events

### Accessing journey step event data accessing-data

Journey step event data is automatically stored in Adobe Experience Platform and can be accessed through:

- **Data Lake queries**: Use SQL to query the journey_step_events dataset with [Query Service](/en/docs/experience-platform/query/home#_blank)
- **Customer Journey Analytics**: Analyze journey data through [advanced analytics tools](/en/docs/journey-optimizer/using/reporting/channel-report/cja-ajo)
- **Real-time reporting**: Access data through Journey Optimizer’s [built-in reporting capabilities](/en/docs/journey-optimizer/using/reporting/gs-reports)
- **APIs**: Programmatically access event data for custom applications

Learn more about [accessing datasets](/en/docs/journey-optimizer/using/data-management/datasets/datasets-query-examples).

### Key data points available key-data-points

Journey step events capture comprehensive information including:

- **Journey identification**: [Journey ID, version, and name](/en/docs/journey-optimizer/using/reporting/reports/legacy-step-event-fields/sharing-journey-fields)
- **Profile information**: [Profile ID and associated identities](/en/docs/journey-optimizer/using/reporting/reports/legacy-step-event-fields/sharing-identity-fields)
- **Step details**: [Node name, step type, and execution status](/en/docs/journey-optimizer/using/reporting/reports/legacy-step-event-fields/sharing-common-fields)
- **Timestamps**: Precise timing of each journey step
- **Action results**: [Success/failure status and execution details](/en/docs/journey-optimizer/using/reporting/reports/legacy-step-event-fields/sharing-execution-fields)
- **Error information**: Detailed [error codes and descriptions](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events) when issues occur

Explore all [available field definitions](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list).

### Common use cases common-use-cases

**Performance monitoring**

```
-- Example: Count profiles entering a journey in the last 24 hours
SELECT count(distinct _experience.journeyOrchestration.stepEvents.profileID)
FROM journey_step_events
WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-id>'
AND _experience.journeyOrchestration.stepEvents.nodeType='start'
AND DATE(timestamp) > (now() - interval '24' hour);
```

**Error analysis**

```
-- Example: Identify errors by journey node
SELECT _experience.journeyOrchestration.stepEvents.nodeName,
       count(distinct _experience.journeyOrchestration.stepEvents.profileID)
FROM journey_step_events
WHERE _experience.journeyOrchestration.stepEvents.actionExecutionError IS NOT NULL
GROUP BY _experience.journeyOrchestration.stepEvents.nodeName;
```

**Journey funnel analysis**

- Track conversion rates at each journey step
- Identify where profiles most commonly exit the journey
- Measure time spent in different journey phases

Learn more [query techniques for funnel analysis](/en/docs/journey-optimizer/using/reporting/reports/query-examples#common-queries).

## Samples and resources samples-resources

### Query examples and templates query-examples

Explore comprehensive query examples for common journey step event analysis:

- **Journey step event query examples**: Ready-to-use SQL queries for common analytics scenarios
- **Dataset query samples**: Examples of querying journey step event datasets
- **Profile-based queries**: Track individual profile journeys and interactions

### Field documentation field-documentation

Understand the complete data structure of journey step events:

- **Journey step event field list**: Comprehensive reference of all available fields
- **Common fields**: Shared fields across journeyStepEvent and journeyStepProfileEvent
- **Action execution fields**: Fields specific to action execution tracking
- **Journey fields**: Journey-specific metadata and identifiers

### Best practices and troubleshooting best-practices

**Performance optimization**

- Use journeyVersionID instead of journeyVersionName for better query performance ([learn more about journey properties](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/journey-properties))
- Filter by date ranges to improve query speed on large datasets
- Leverage profile identities that match your [journey namespace configuration](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management)

**Data quality**

- Regularly monitor for [discarded events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events) to identify data issues
- Validate that event schemas match your analysis requirements
- Implement proper error handling in custom queries

**Analytics strategies**

- Combine journey step events with [message feedback data](/en/docs/journey-optimizer/using/data-management/datasets/datasets-query-examples#message-feedback-event-dataset) for complete attribution
- Use time-based analysis to understand journey velocity and bottlenecks

### Advanced analytics capabilities advanced-analytics

**Customer Journey Analytics integration**Journey step events can be analyzed using [Customer Journey Analytics](/en/docs/journey-optimizer/using/reporting/channel-report/cja-ajo) for:

- Advanced attribution modeling
- Cross-channel journey visualization
- Predictive analytics on journey outcomes

Learn how to [configure Customer Journey Analytics](/en/docs/journey-optimizer/using/reporting/channel-report/report-gs-cja) for Journey Optimizer data.

## Additional resources additional-resources

### Documentation links documentation-links

- **Journey step sharing overview**: Understanding how journey data flows to Adobe Experience Platform
- **Built-in schemas dictionary**: Complete XDM schema reference
- **Journey Optimizer reporting**: Overview of reporting capabilities in Journey Optimizer

### Integration guides integration-guides

- **Adobe Customer Journey Analytics**: Analyzing Journey Optimizer data in CJA
- **Data management**: Exporting and managing journey data
- **Privacy and governance**: Data governance considerations for journey events

**Next steps:**

- Start with [creating your first journey reports](/en/docs/journey-optimizer/using/reporting/reports/sharing-overview)
- Explore [query examples](/en/docs/journey-optimizer/using/reporting/reports/query-examples) for specific use cases
- Learn about [journey management best practices](/en/docs/journey-optimizer/using/orchestrate-journeys/journey)

recommendation-more-help
