---
title: "Fallout overview fallout-overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/fallout-flow"
category: "overview"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:43:18.627511+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Fallout overview fallout-overview

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
Information in this snippet is shared between Journey canvas, Fallout, and Flow visualization docs
*This article documents the Fallout visualization in* *Customer Journey Analytics .**See Fallout for the* *Adobe Analytics version of this article.*

style
shade-box
A **Fallout** visualization shows where persons left (fell out) and continued through (fell through) a predefined sequence of pages.

See [Create a fallout visualization report](/en/docs/analytics-learn/tutorials/analysis-workspace/analyzing-customer-journeys/fallout-visualization#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
Fallout visualizations let you:

- Perform side-by-side comparisons of two different segments in the same report.
- Drag and drop (and rearrange) funnel steps (touchpoints).
- Mix and match values from different dimensions and metrics.
- Create a multi-dimensional fallout report.
- Identify where customers go immediately after falling out.

Fallout displays conversion and fallout rates between each step or touchpoint in a sequence.

For example, you can track a person’s fallout points during a purchase process. Just select a beginning touchpoint and a conclusion touchpoint, and add intermediate touchpoints to create a website navigation path. But you can also do multi-dimensional fallouts.

## Choose between Fallout, Flow, and Journey canvas visualizations

The Fallout visualization has similarities with the [Flow visualization](/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/flow) and the [Journey canvas visualization](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas).

### Understand the differences

Various visualizations in Customer Journey analytics are designed to analyze the journeys you provide to your customers.

Use the following information to choose the visualization that best meets your needs.

Function
Journey canvas
Fallout
Flow
Predefined sequence of pages
Yes
Combines predefined and exploratory analysis. The eventual path is used when using predefined nodes on the path (visitors are counted as long as they eventually move from one predefined node to the other). The immediate (not eventual) next nodes can also be shown by
showing the top nodes based on existing nodes
.
Yes
The path can be an eventual path or can be constrained to the next touchpoint
No
Exploratory sequence of pages (ad hoc analysis)
Yes
Combines predefined and exploratory analysis. The eventual path is used when using predefined nodes on the path (visitors are counted as long as they eventually move from one predefined node to the other). The immediate (not eventual) next nodes can also be shown by
showing the top nodes based on existing nodes
.
Limited
Allows you to right-click and view immediate fallout in a Freeform table.
Yes
Exploratory analysis only. Always within one dimension instance between nodes. This means that each node shows the immediate (not eventual) next touchpoint along the path.
Shows where people left (fell out) and continued through (fell through)
Yes
Shows for both predefined and exploratory journeys.
Yes
Shows predefined journeys
Yes
Shows for exploratory journeys
Linear journeys
Yes
Yes
No
Non-linear journeys with multiple entry points and paths
Yes
No
Yes
Primary metric
Any metric, including calculated metrics.
Only Session or Person
Only Occurrences (Path views)
Secondary metric
Yes

Any metric, including calculated metrics.

No
No
Component support in nodes or touchpoints
Metrics, dimension items, segments, and date ranges.
Metrics, dimension items, segments, and date ranges.
Only dimension items (except for the starting and ending touchpoint)
Compare segments
No
Yes

Perform side-by-side comparisons of two different segments in the same report.

No
Drag-and-drop component interaction
Yes
Yes
No
Adobe Journey Optimizer journeys
Yes
Open journeys from Journey Optimizer for deeper analysis and customization.
No
No
### When to use Fallout

Both Fallout and [Journey canvas](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas) visualizations are useful for analyzing:

- Conversion rates through specific processes on your site (such as a purchase or registration process).
- General, wider-scope traffic flows: Of the people who visited the home page, this flow shows how many performed a search. And then how many of them eventually looked at a specific item.
- Correlations between events on your site. Correlations show what percentage of people who looked at your privacy policy went on to purchase a product.

Fallout visualizations are best suited for:

- Fallout analysis involving journeys with a predefined sequence of pages and a single entry point and path. (Use Journey canvas for journeys with multiple entry points and paths.)
- Journeys where you need to perform side-by-side comparisons of two different segments in the same report.

Use [the table above](#understand-the-differences) to understand the differences between Journey canvas, Fallout, and Flow visualizations.

Related Articles
Configure a fallout visualization
recommendation-more-help
