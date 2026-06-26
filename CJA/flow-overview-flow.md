---
title: "Flow overview flow"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/flow"
category: "overview"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:15.754631+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Flow overview flow

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
Information in this snippet is shared between Journey canvas, Fallout, and Flow visualization docs
*This article documents the Flow visualization in* *Customer Journey Analytics .**See Flow for the* *Adobe Analytics version of this article.*

style
shade-box
The **Flow** visualization shows customer paths through your websites and apps.

With the visualization you can:

- Visualize the customer journey through your website or application.
- Analyze where customers go before and after specified checkpoints, such as entry, a specific dimension, or exit.
- Create segments by designating a specific point in a chosen path.

See [Create a flow visualization](/en/docs/analytics-learn/tutorials/analysis-workspace/analyzing-customer-journeys/flow-visualization#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
## Inter-dimensional flows

You can show the [flow between dimensions](/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/multi-dimensional-flow). For example, you might combine pages and departments in one diagram. In this case, your flow might go from the home page, to the Men page, then to the Shoes department.

Each column could show a different dimension. Drag a dimension and drop in a drop zone to add that dimension to the diagram.

Related Articles
Configure a flow visualization
.
## Choose between Flow, Fallout, or Journey canvas visualizations

The Flow visualization has similarities with the [Fallout visualization](/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/fallout-flow) and the [Journey canvas visualization](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas), but with important differences.

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
### When to use Flow

Flow visualizations are best suited for:

- Exploratory, ad hoc analysis for the immediate next touchpoint on the path. (Use Journey canvas for journeys with a predefined sequence of pages, or those that use an eventual path.)
- Non-linear journeys with multiple entry points and paths. (Use Journey canvas for journeys with a predefined sequence of pages.)

Use [the table above](#understand-the-differences) to understand the differences between Flow, Fallout, and Journey canvas.

recommendation-more-help
