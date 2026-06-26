---
title: "Configure a flow visualization configure-a-flow-visualization"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/create-flow"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:44:31.405290+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure a flow visualization configure-a-flow-visualization

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)

CREATED FOR:

- User

Flow visualizations help you understand the journey originating from a specific conversion event on your website or your app. Or leading up to a specific conversion event. The visualization traces a path through your dimensions (and dimension items) or metrics.

You can configure the start or end of the path you are interested in. Or analyze all paths that flow through a dimension or dimension item.

## Use

- Add a Flow visualization. See Add a visualization to a panel .
- Anchor your Flow visualization using one of the following options: Starts with (metrics, dimensions, or items), or Contains (dimensions, or items), or Ends with (metrics, dimensions, or items) Each of these categories is shown onscreen as a drop zone . You can populate the drop zone in 3 ways: Use the drop-down menu to select metrics or dimensions. Drag dimensions or metrics from the left panel. Begin typing the name of a dimension or metric, then select it when it appears in the drop-down menu. note important IMPORTANT Calculated metrics cannot be used in the Starts with or Ends with fields.
- If you choose a metric, you also need to provide a Pathing Dimension to use as your path leading to or coming from your selected component, as shown here. The default is Page .
- (Optional) Select Show advanced settings to configure any of the following options: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Setting Description Wrap labels Normally, the labels on the Flow elements are truncated to save screen real estate, but you can make the entire label visible by checking this box. Default = unchecked. Include repeat instances Flow visualizations are based on instances of a dimension. This setting gives you the option to include or exclude repeated instances, for example, Page reloads. However, repeats cannot be removed from Flow visualizations that include multi-valued dimensions, such as listVars, listProps, s.product, merchandising eVars, etc. This option is disabled by default. Limit to first/last occurrence Limit paths to paths that start or end with the first or last occurrence of a dimension, item, or metric. See Limit to first/last occurrence for a more detailed explanation. Number of columns The number of columns you want in your Flow diagram. You can specify a maximum of 5 columns. Items expanded per column The number of items you want in each column. You can specify a maximum of 10 items expanded per column. Flow container You can switch between Global Account [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} , Account [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} , Opportunity [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} , Buying Group [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} , Sessions and Person to analyze pathing. These settings help you understand engagement at a specific container level (across sessions), or constrain the analysis to a single session. note important IMPORTANT The combination of Number of columns and Items expanded per column determine the number of underlying requests required to create the flow visualization. The higher those numbers, the longer it takes to render a visualization.
- Select Build .

### Example

Suppose that you want to trace the path that users took both to and from the most popular pages on your site.

- Create a flow visualization as described above.
- Drag the **Page** dimension into the **Contains** field, then select **Build**.
- The Flow visualization builds, with the most-viewed page visible in the focus node, at the center of the visualization. You also see the top pages leading into that page (to the left of the focus node) as well as the top pages leading out of that page (to the right of the focus node).
- Analyze data in the flow, as described in [Configure](#configure).

## Configure

A summary of the Flow configuration appears at the top of the visualizations. The paths in the diagram are proportional. Paths with more activity appear thicker.

To drill down further into the data, you have several options:

- The flow diagram is interactive. Mouse over the diagram to change the details that are shown.
- When you select a node in the diagram, the details for that node appear. Select the node again to collapse it. Leaving multiple nodes expanded in a flow visualization can affect reporting time. As a general guideline, no more than 10 nodes should remain expanded at a given time.
- You can filter a column to display only certain results, such as including and excluding, specifying criteria, etc.
- Select on the left or right side to expand a column.
- To customize the output, use the context menu options.
- To edit the flow or rebuild it with different options, select next to the configuration summary.

## Filter

Above each column, a filter appears when you hover over it. By selecting the filter, you get the same filter dialog that exists in the Freeform table. See [Filter and sort](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/filter-and-sort).

- Use **Show advanced** to configure advanced settings to include or exclude certain criteria with a list of operators. See [Filters and sort](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/filter-and-sort) for more information.
- Once you have filtered a column, that specific column reflects the filtering. A blue indicates that the column is filtered. The filter either reduces the column to show only the item allowed in the filter. Or it removes all items, except for the one item you want in the filter.
- All downstream and upstream columns persist, as long as there is data flowing into the remaining nodes.
- To remove a filter, select to open the filter menu. Remove any filters applied and then select **Save**. The flow should return to its previous, unfiltered state.

## Context menu

Use a context menu on any node in the flow visualization with the following options:

Option
Description
Focus on this node
Change the focus to the selected node. The focus node appears at the center of the Flow diagram.
Start over
Return you to the Freeform diagram builder, where you can build a new Flow diagram.
Create a segment for this path
Create a segment. This selection takes you into the Segment builder, where you can configure the new segment.
Breakdown
Break the node down by available Dimensions, Metrics, or Time.
Filter column
The same filter options appear as are available in the Freeform table. For more information about the available options, see the section “Apply a simple or advanced filter to a table” in
Filter and sort tables
.
Exclude item
or
Restore excluded items
Removes a specific node from the column and automatically creates it as a filter at the top of the column. To restore the excluded item, from the context menu select
Restore Excluded Item
. you can also open the segment at the top of the column and remove the pillbox with the item you just excluded.
Trend
Create a trended diagram for the node.
Show next column
/
Show previous column
Reveals the next (right) or previous (left) column of the visualization.
Hide column
n
Hides the selected column from the visualization.
Expand entire column
Expand a column to show all nodes. By default, only the top five nodes display.
Create audience from selection
Creates an audience based on the column that is selected.
Collapse entire column
Hide all nodes in a column.
## Limit to first/last occurrence

When using this option, keep in mind that:

- Limit to first/last occurrence counts only the first/last occurrence in the series. All other occurrences of the Starts with or Ends with criteria are discarded.
- If used with a Starts with flow, only the first occurrence that matches the start criteria is included. In the example below, all occurrences of Add to cart and Product main category in each step of the flow are included. In the example below, only the first occurrences of Add to cart and Product main category in each step of the flow are included.
- If used with an Ends with flow, only the last occurrence that matches the end criteria is included. In the example below, all occurrences of Product main category and Add to cart in each step of the flow are included. In the example below, only the last occurrences of Product main category and Add to cart in each step of the flow are included.
- The series used differs based on the container. If you use the Session container, the series of events are limited to a session. If you use any of the other containers (for example, Person , or Account [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} , or Opportunity [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} ), the series of events are based on the specified container and potentially span multiple sessions.
- The Limit to first/last occurrence option can be configured in the advanced settings when using a Metric or Dimension Item in the Starts with or Ends with fields.

Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
