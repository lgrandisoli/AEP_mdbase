---
title: "Journey report journey-global-report"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:49.900499+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Journey report journey-global-report

Last update: May 8, 2026
- Topics:
- [Reporting](#)
- [Journeys](#)

CREATED FOR:

- Intermediate
- User

The **Journey report** functions as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your journey. This encompasses details such as the count of entered profiles and instances of failed individual journeys, offering a comprehensive insight into your journey’s effectiveness and level of engagement.

**Journey report** can be accessed directly from your journey with the **View report** button.

To learn more about Customer Journey Analytics Workspace and how to filter and analyze data, refer to [this page](/en/docs/analytics-platform/using/cja-workspace/home).

## Journey overview journey-global

The **Journey** report gives you a clear view of the most important tracking data about your journey.

### Journey KPIs journey-perfomance

The **Journey** Key Performance Indicators (KPIs) function as an all-encompassing dashboard, delivering an analysis of essential metrics associated with your journey. This encompasses details such as the count of entered profile and instances of failed individual journeys, offering a comprehensive insight into your journey’s effectiveness and level of engagement.

Learn more about Journey KPIs metrics
- Journey engagement : Total number of unique individuals who received messages sent through the journey, representing distinct profiles that reached a designated action point in the journey.
- Journey enters : Total number of individuals who reached the entry event of the journey.
- Journey exits : Total number of individuals who exited the journey.

### Journey stats journey-stats

The **Journey Statistics** table offers a detailed summary of crucial data about your journeys. It includes key metrics like the number of failures and successful entries, providing valuable insights into the performance and reach of your emails and journeys.

Learn more about Journey Statistics metrics
- Journey exclusion : Total number of individuals who were excluded from the journey due to predefined criteria or suppression rules.
- Journey engagement : Total number of unique individuals who received messages sent through the journey, representing distinct profiles that reached a designated action point in the journey.
- Journey enters : Total number of individuals who reached the entry event of the journey.
- Journey exits : Total number of individuals who exited the journey.
- Journey failures : Total number of individual journeys that were not successfully executed.
- Unique Journey enters : Total number of individuals who reached the entry event of the journey, multiple interactions of one profile are not taken into account.
- Unique Journey exits : Total number of individuals who exited the journey, multiple interactions of one profile are not taken into account.
- Unique Journey failures : Total number of individual journeys that were not successfully executed, multiple interactions of one profile are not taken into account.

## Journey exclusion journey-exclusion

The **Journey exclusion** table presents a comprehensive view of the different factors that resulted in the exclusion of user profiles. To investigate business rules-related exclusions at the Data Lake level and identify whether profiles were excluded due to a cap being reached or a lower priority, use the queries available in [this section](/en/docs/journey-optimizer/using/reporting/reports/query-examples#business-rules-queries).

## Action error action-error

The **Action errors** widget details the different errors which occurred for your journey’s actions.

## Journey canvas journey-canvas

The **Journey Canvas** widget allows you to visually trace the trajectory of your targeted profiles as they navigate through your journey. [Learn more in Customer Journey Analytics documentation](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas)

Enhance your canvas customization with the following options:

- Add or remove the desired activity type, such as messages or conditions, from the **Node type** drop-down menu.
- Adjust the **Percentage value** to determine the flow distribution among different journey paths.
- Customize your **Arrow settings** to include labels, conditions, or opt for a clean display.
- Enable the **Show fallout** option to visualize profiles that exited your journey directly on the canvas.

The following rules apply when using **Node Type** Filtering:

- When creating a segment on a node, it will still encompass nodes from earlier stages of the journey, even if those nodes have been excluded through the Node type filter.
- You cannot create segments formed from an arrow if nodes in earlier stages of the journey have been excluded via the Node type filter. In this case, the right-click functionality will be disabled on those arrows.

## Action performance action-performance

### Performance over time action-overtime

The **Performance Over time** graph allows you to identify and analyze the number of profiles that meet the criteria to be considered target profiles for your actions. This visualization provides valuable insights into the effectiveness of your strategies and helps you make data-driven decisions to optimize your performance.

### Action overview action-overview

The **Action overview** table serves as a comprehensive dashboard, offering an analysis of key metrics related to the actions in your journey. This includes crucial details such as the number of interactions and the click-through rate

Learn more about Action overview metrics
- Node enters : Total number of individuals who have entered a specific node within the journey.
- Journey failure : Total number of individual journeys that were not successfully executed.
- Click through rate : Percentage of users who interacted with the action.
- Clicks : Number of times a content was clicked on in your actions.
- Delivered : Number of actions successfully sent, in relation to the total number of sent actions.

## Events performance events-performance

### Performance over time event-overtime

The **Performance over time** graph enables you to identify and analyze the number of profiles that qualify as target profiles for your events. This powerful tool helps you track trends and patterns over time, providing valuable insights for optimizing your event strategies.

### Event overview event-overview

The **Event overview** table shows how many profiles meet your event criteria over time. This tool helps you identify patterns in qualification rates to refine your event strategy.

Learn more about Journey Statistics metrics
- **People**: Number of user profiles who qualify as target profiles for your events.

## Targeting overview targeting

If you set up **Targeting rules** for your content, the **Targeting overview** table provides a detailed view of key engagement metrics, showing how the targeted profiles for each rule interacted with your content.

➡️ [Learn more on Targeting rules](/en/docs/journey-optimizer/using/content-management/message-optimization/optimization-targeting)

Learn more about Targeting overview metrics
- People : Number of user profiles who qualify as target profiles for your events.
- Unique Clicks : Number of profiles who clicked on a content in an email.
- Unique click rate : Percentage of targeted profiles who clicked at least once.

recommendation-more-help
