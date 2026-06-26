---
title: "Segmented metrics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/metrics-with-segments"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-02T19:08:25.857144+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Segmented metrics

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User
- Admin

In the [Calculated metric builder](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics#definition-builder), you can apply segments within your metric definition. Applying segments is helpful if you want to use metrics for a subset of your data in your analysis.

NOTE
Segment definitions are updated through the
Segment builder
. If you make a change to a segment, the segment is automatically updated everywhere it is used, including if the segment is part of a calculated metric definition.
You want to compare metrics for German people interacting with your brand versus people outside of Germany. So, you can answer questions like:

- How many German versus international people are visiting your most [popular pages](#popular-pages).
- How many German versus international people in [total](#totals) have interacted online with your brand this month.
- What are the [percentages](#percentages) of Germans and international people that have visited your popular pages?

See the sections below to illustrate how segmented metrics can help you answer these questions. Where appropriate, references are made to more detailed documentation.

## Popular pages

- Create a calculated metric from a Workspace project, named German people .
- From within the Calculated metric builder , create a segment , titled Germany , that is using the CRM Country field from your CRM data to determine where a person is coming from. note tip TIP In the Calculated metric builder, you can create a segment directly using the Components panel. Your segment could look like.
- Back in the Calculated metric builder, use the segment to update the calculated metric.

Repeat the steps above for the international version of your calculated metric.

- Create a calculated metric from your Workspace project, titled International people .
- From within the Calculated metric builder, create a segment, titled Not Germany , that is using the CRM Country field from your CRM data to determine where a person is coming from. Your segment should look like.
- Back in the Calculated metric builder, use the segment to update the calculated metric.
- Create a project in Analysis Workspace, where you look at pages visited by German and International people.

## Totals

- Create two new calculated metrics based on Grand Total. Open each of the segments created earlier, rename the segment, set the Metric type for People to Grand Total and use Save As to save the segment using the new name. For example:
- Add a new Freeform table visualization to your Workspace project, showing the total pages for this month.

## Percentages

- Create two new calculated metrics that calculate a percentage from the calculated metrics you created earlier.
- Update your Workspace project.

See [Use a segmented calculated metric as an implementationless metric](/en/docs/analytics-learn/tutorials/components/calculated-metrics/calculated-metrics-segmented-metrics#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
recommendation-more-help
