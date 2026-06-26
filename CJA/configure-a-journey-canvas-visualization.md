---
title: "Configure a Journey canvas visualization"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/configure-journey-canvas"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:07:44.091692+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure a Journey canvas visualization

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

The Journey canvas visualization allows you to analyze and gain deep insights on the journeys that you provide to your users and customers.

## Journey canvas overview

See [Journey canvas overview](/en/docs/analytics-platform/using/cja-workspace/visualizations/journey-canvas/journey-canvas) to learn more about Journey canvas, including:

- Key features
- Potential insights
- Differences between Journey canvas and Fallout
- Details about analyzing Journey Optimizer journeys
- And more

## Begin building a Journey canvas visualization

- Add a blank panel to your project, select the Visualizations icon in the left rail, then drag the Journey canvas visualization into the panel. Or Add a Journey canvas visualization in any of the ways described in the Add visualizations to a panel section in Visualizations overview .
- Specify the following basic information to configure Journey canvas: table 0-row-2 1-row-2 2-row-2 3-row-2 Field Function Primary metric Determines the metric that is used when calculating the percentage and number values on each node in the journey. Note : The scope of the data included in each percentage and number value is determined by the metric that you choose in the Journey canvas container field. For example, if Person is set as the container, then the statistics shown in the journey span multiple sessions for a given person. If Session is set as the container, then the statistics shown in the journey are constrained to a single defined session for a given person. Consider the following examples of how the primary metric affects the percentage and number values of each node: If People is the primary metric and Person is the container, then only those people who have an event that matches the criteria of each successive node in the journey move throughout the journey. Fallout occurs on a node when a person never arrived at any of the immediate next nodes in the journey. They might have performed other actions on the site, but they did not meet the criteria defined by any of the nodes that immediately follow. If People is the primary metric and Session is the container, then only those people who have an event that matches the criteria of each node in the journey within a single session move throughout the journey. Fallout occurs on a node when a person never arrived at any of the immediate next nodes in the journey within a single session. They might have performed other actions on the site within the session, but they did not meet the criteria defined by any of the nodes that immediately follow. The primary metric affects the following aspects of the Journey canvas visualization: The total number shown on each node. For example, if Events is the primary metric, each node shows the number of people who had an event that matches the criteria of that node (and each previous node leading up to it in the journey). The percentage shown on each node. (After the visualization is built, you can use the Percentage value drop-down menu to choose to show either the percentage of the total, the percentage of the previous node, or the percentage of the starting node.) For example, if Events is the primary metric, each node shows the percentage of people who had an event that matches the criteria of that node (and each previous node leading up to it in the journey). When a dimension is added to the visualization, the top 3 nodes of the visualization are added, based on the primary metric. Secondary metric Determines the secondary metric that is used when calculating the percentage and number values on each node in the journey. The secondary metric is optional. Note : The scope of the data included in each percentage and number value is determined by the metric that you choose in the Journey canvas container field. For example, if Person is set as the container, then the statistics shown in the journey span multiple sessions for a given person. If Session is set as the container, then the statistics shown in the journey are constrained to a single defined session for a given person. When a secondary metric is configured, it affects the following aspects of the Journey canvas visualization: The total number shown on each node below the primary metric. For example, if Accounts is the secondary metric, the number of accounts is shown on the node for all people who reached that node in the journey. The percentage shown on each node below the primary metric. (After the visualization is built, you can choose to show either the percentage of the total or of the starting node.) For example, if Sessions is the secondary metric, each node shows the percentage of sessions that reached that node in the journey (either the percentage of the total or of the starting node). Journey Optimizer journey Select the Journey Optimizer journey that you want to use as the basis for your analysis in Journey canvas. Journeys with any of the following statuses are available: Live, Stopped, or Finished Alternatively, you can leave this option blank if you want a blank canvas from which to build your analysis within Analysis Workspace. When you analyze a Journey Optimizer journey in Journey canvas, the journey is displayed with the same order, sequence, and structure as it has in Journey Optimizer. For more information, see Analyze Journey Optimizer journeys in Journey canvas overview . Note : This option displays only when Journey Optimizer data is detected in the same data view that is selected in the Analysis Workspace panel where you are adding the visualization. For information about changing the data view on a panel in Analysis Workspace, see Analysis Workspace overview .
- (Optional) Select Show advanced settings , then specify the following information: table 0-row-2 1-row-2 Field Function Journey canvas container Select the container that you want to focus on throughout the journey. The container that you choose determines the scope of the data captured in the journey. This affects the statistics that are displayed in the visualization. (If your container names differ from the default names shown below, they were customized in your data view.) Session: Constrains the statistics of the visualization to fall within a single defined session for a given person. This means that the numbers and percentages that appear on each node (that are based on the primary and secondary metrics) must occur within a single session for each person. In other words, one person can be represented multiple times in a single journey. This container uses the Sessions metric. Person: (Default) Allows the statistics of the visualization to span multiple sessions for a given person. This means that the numbers and percentages that appear on each node (that are based on the primary and secondary metrics) can occur across any number of sessions, as long as the sessions belong to the same person. In other words, one person can be represented only one time in a single journey. This container uses the People metric.
- Select Build . If you selected a Journey Optimizer journey, the journey is displayed with the same order, sequence, and structure as it has in Journey Optimizer. (Only users with access to Journey optimizer can select a Journey Optimizer journey.) add screen shot If you didn’t select a Journey Optimizer journey, a blank canvas displays where you can begin adding nodes to the journey. (Only users with access to Journey optimizer can select a Journey Optimizer journey.) add screen shot
- Whether you are creating a new analysis from a blank canvas or you are analyzing a Journey Optimizer journey, you can configure the journey as described in Configure visualization settings .

## Configure visualization settings

Various configuration options are available in the Journey canvas header.

To configure settings for the Journey canvas visualization:

- In Analysis Workspace, open an existing Journey canvas visualization, or begin building a new one . Options that allow you to configure the Journey canvas visualization are available in the header:
- Configure any of the following settings that are displayed across the top of the visualization: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Setting Function Percentage value The percentage value shown on each node in the journey. Consider the following when configuring the percentage values shown on nodes in the journey: A percentage is shown on each node for the primary metric. A percentage is also shown for the secondary metric if one is configured. (For more information about the primary and secondary metric settings, see Begin building a Journey canvas visualization .) Percentages include all people or sessions that are included in the data view within the panel’s date range. Whether people or sessions is used depends on the container setting. (For more information about the container setting, see Begin building a Journey canvas visualization .) Choose from the following options: Percent of start node : Calculates the percentages shown on each node in relation to the start node. Percentages are based on the primary and secondary metric that you selected. A start node is a node that has no connected nodes preceding it. A journey can contain multiple start nodes. However, Percent of total is used if the journey contains 2 or more start nodes that lead to a common node. If you want to use Percent of start node , update the journey so that each node in the journey can be traced back to a single start node. Percent of previous node : Calculates the percentages shown on each node in relation to the previous node. Percentages are based on the primary and secondary metric that you selected. Percent of total : Calculates the percentages shown on each node in relation to all data in the data view. Percentages are based on the primary and secondary metric that you selected. Arrow settings The arrows that appear between nodes in Journey canvas can be configured to show custom labels and values. Labels are custom names that appear on arrows. Only a single label is shown on a given arrow. Labels can be any of the following, and are shown in this order of preference: A custom name added from Journey canvas (as described in Add or update a label on an arrow ) A Journey Optimizer label A Journey Optimizer condition Values are the numbers and percentages that appear on arrows, and they indicate the people or sessions who moved from one node to the next node in the journey. (In other words, those who did not fall out of the journey at a given step.) The following options are available for journeys that did not originate from Journey Optimizer and for Journey Optimizer journeys that have not been significantly modified in Journey canvas: (Significant modifications include adding or removing nodes, adding or removing arrows, or changing the components of a node.) No labels : No labels are shown on arrows in the journey. This option is available only if the journey has been modified in Labels only : Labels are shown on arrows in the journey. The following options are available for Journey Optimizer journeys that have been significantly modified in Journey canvas: (Significant modifications include adding or removing nodes, adding or removing arrows, or changing the components of a node.)( Note : These options display only when Journey Optimizer data is detected in the same data view that is selected in the Analysis Workspace panel where you are adding the visualization. For information about changing the data view on a panel in Analysis Workspace, see Analysis Workspace overview .) No labels or values : No labels or values are shown on arrows in the journey. Labels only : Only labels are shown on arrows in the journey. Values are not shown. Values only : Only values are shown on arrows in the journey. Labels are not shown. Values and labels : Both labels and values are shown on arrows in the journey. Show fallout Fallout data shows a percentage and number falling out of each node of the journey. Fallout data is based on the metric associated with the journey’s container settings; it is not based on the primary or secondary metric. By default, the container is Person , so the metric used for fallout data is People . If the container is changed to Session , the metric used for fallout data is Sessions , and so on. For example, with Person as the container setting, fallout shows the percentage and number of people on each node of the journey who never arrived at any of the immediate next nodes. They might have performed other actions on the site, but they did not meet the criteria defined by any of the nodes that immediately follow. For more information about the Journey canvas container setting, see Begin building a Journey canvas visualization . Zoom controls The following zoom controls are available in the upper-right corner of the canvas: Zoom in : Enlarges specific areas of the visualization. You can also use mouse controls, such as pinching on a trackpad. Zoom out : Shrinks the visualization to allow more room on the canvas. You can also use mouse controls, such as pinching on a trackpad. Fit screen : Adjusts current zoom and pan settings to fill the screen with the full visualization. To pan across the canvas after zooming in or out, click your mouse and drag to the desired location.
- Continue with Add nodes .

## Add nodes

Nodes in a Journey canvas visualization represent the events or actions of a user journey.

You create nodes in the following ways: by dragging Workspace components from the left rail to the canvas; by allowing Journey canvas to choose the top next or previous nodes based on existing nodes; or by duplicating existing nodes.

### Drag components from the left rail

- In Analysis Workspace, open an existing Journey canvas visualization, or begin building a new one .
- Drag metrics, dimensions, dimension items, segments, or date ranges from the left rail onto the canvas. Metrics that are based on a derived field are supported. However, calculated metrics, as well as any metrics or dimensions that are based on a summary dataset are not supported. You can select multiple components in the left rail by holding Shift, or by holding Command (on Mac) or Ctrl (on Windows). The visualization is updated based on the primary metric, as follows (depending on the component type and the area of the canvas where you place it): table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 12-row-3 13-row-3 14-row-3 15-row-3 16-row-3 17-row-3 18-row-3 Component type Placement of component Visualization updates after node is added Metric Blank area of the canvas The node displays where the component was dropped, unconnected with any existing nodes. Metric An existing node The component is automatically combined with the existing node. (See Combine nodes for more information.) Metric An arrow between 2 existing nodes The node displays between the two existing nodes where the component was dropped and is connected to both existing nodes. (See Connect nodes for more information.) Dimension Blank area of the canvas 3 nodes are created for the top 3 dimension items where the component was dropped, unconnected with any existing nodes. ( Note: If only 1 or 2 nodes display, it means that data is available for only 1 or 2 of the dimension items. If no nodes display, it means that data is not available for any of the dimension items. In this case, try adding it to a different point of the journey, adjust the visualization’s date range, or choose a different dimension.) Hold the Shift key when you drop the dimension onto the canvas to add it as a single node with 3 dimension items. Dimension An existing node A breakdown is automatically applied to the node with the top 5 dimension items displayed. To view the breakdown in a new freeform table visualization, select the Open in a freeform table link on the node. Dimension An arrow that connects 2 existing nodes 3 nodes are created for the top 3 dimension items that follow the first event after the first node (of people/sessions who eventually reach the second node). The nodes display between the two existing nodes where the component was dropped and each node is connected to both existing nodes. ( Note: If only 1 or 2 nodes display, it means that data is available for only 1 or 2 of the dimension items. If no nodes display, it means that data is not available for any of the dimension items. In this case, try adding it to a different point of the journey, adjust the visualization’s date range, or choose a different dimension.) Hold the Shift key when you drop the dimension onto the canvas to add it as a single node with 3 dimension items. (See Connect nodes for more information.) Dimension item Blank area of the canvas The node displays where the component was dropped, unconnected with any existing nodes. Dimension item An existing node The component is automatically combined with the existing node. Dimension item An arrow that connects 2 existing nodes The node displays between the two existing nodes where the component was dropped and is connected to both existing nodes. (See Connect nodes for more information.) Segment Blank area of the canvas The node displays where the component was dropped unconnected with any other nodes. The number and percentage that appear on the node include the total of the primary metric, segmented by the segment you selected. For example, if People is selected as the primary metric for the journey, then adding a segment of Today to a blank area of the canvas shows all the people who had an event today. Segment An existing node Applies the segment to the existing node. Segment An arrow that connects 2 nodes The node displays between the two existing nodes where the component was dropped and is connected to both existing nodes. (See Connect nodes for more information.) Applies the segment to the point on the path where the component was dropped. Date range Blank area of the canvas The node displays where the component was dropped, unconnected with any other nodes. The number and percentage that appear on the node include the total of the primary metric, segmented by the date range you selected. For example, if People is selected as the primary metric for the journey, then adding a date range of This month to a blank area of the canvas shows all the people who had an event during the current month. Date range An existing node Applies the date range to the existing node. Date range An arrow that connects 2 nodes The node displays between the two existing nodes where the component was dropped and is connected to both existing nodes. (See Connect nodes for more information.) Applies the date range to the point on the path where the component was dropped. Multiple components A blank area of the canvas If none of the components are dimensions: Each component displays as a separate node where the components were dropped, unconnected with any existing nodes. Hold the Shift key when you drop the components onto the canvas to add them as one combined node. If any of the components you are adding are dimensions: Each component displays as a separate node where the components were dropped, unconnected with any existing nodes. Only one dimension can be added at a time. When the dimension is added, 3 nodes are created for the top 3 dimension items where the component was dropped. Hold the Shift key when you drop the components onto the canvas to add them as one combined node. The top 3 dimension items are combined with each node. (See Combine nodes for more information.) Multiple components An existing node All components are combined with the existing node. If any of the components you are adding are dimensions, then the top 3 dimension items are combined with the node. Only one dimension can be added at a time. Multiple components An arrow that connects 2 existing nodes If none of the components are dimensions: Each component displays as a separate node where the components were dropped and each node is connected to both existing nodes. (See Connect nodes for more information.) Hold the Shift key when you drop the components onto the canvas to add them as one combined node. (Components must be of the same type to be combined into a single node.) (See Combine nodes for more information.) If any of the components you are adding are dimensions: Each component displays as a separate node where the components were dropped and each node is connected to both existing nodes. Only one dimension can be added at a time. When the dimension is added, 3 nodes are created for the dimension’s top 3 items that follow the first event after the first node (of people or sessions who eventually reach the second node). Each node is connected to both existing nodes. (See Connect nodes for more information.) Hold the Shift key when you drop the components onto the canvas to add them as one combined node. The top 3 dimension items are combined with each node, and each node is connected to both existing nodes. (See Combine nodes for more information.) Nodes display as a rectangular box with the following information: Component name The component type (such as metric or dimension) Primary metric statistics (total and percent) Secondary metric statistics (total and percent) A pulsing or glowing node indicates that data is loading for that node.
- Repeat this process to continue adding nodes to build out your journey.
- Continue customizing the journey as described in the sections below. You can connect nodes, rename nodes, apply breakdowns, create audiences, add time constraints, and more.

### Show the top nodes based on existing nodes

You can automatically show the top immediate nodes based on the nodes that are already on the canvas. You can add the top nodes to Journey canvas or view them in a freeform table.

Journey canvas uses the primary metric when determining which nodes to show.

This option is available for the following objects on the canvas:

- Individual nodes
- The arrow between nodes

#### Show top nodes after an existing node

You can select a node and show the top dimension items that come immediately after it in the journey. You can add the top 3 dimension items to Journey canvas as separate nodes, or you can view all top dimension items in a freeform table.

- Right-click the node where you want to show the top dimension items that come after it in the journey. The node cannot have any existing nodes going out of it in the journey.
- Select Show top nodes after this node .
- Select where you want to show the dimension items: In Journey canvas : Adds the top 3 nodes to the canvas that come after this node in the journey. Each node is connected to the node that you selected as a separate branch on the canvas. In a Freeform table : Creates a freeform table visualization showing all top dimension items that come after this node in the journey.
- Select the desired dimension from the list of dimensions. Depending on what you chose in the previous step, the top 3 dimension items are added to the canvas as 3 separate nodes, or all top dimension items are shown in a freeform table.

#### Show top nodes before an existing node

You can select a node and show the top dimension items that come immediately before it in the journey. You can add the top 3 dimension items to Journey canvas as separate nodes, or you can view all top dimension items in a freeform table.

- Right-click the node where you want to show the top dimension items that come before it in the journey. This node cannot have any existing nodes coming into it in the journey.
- Select Show top nodes before this node .
- Select where you want to show the dimension items: In Journey canvas : Adds the top 3 nodes to the canvas that come before this node in the journey. Each node is connected to the node that you selected as a separate branch on the canvas. In a Freeform table : Creates a freeform table visualization showing all top dimension items that come before this node in the journey.
- Select the desired dimension from the list of dimensions. Depending on what you chose in the previous step, the top 3 dimension items are added to the canvas as 3 separate nodes, or all top dimension items are shown in a freeform table.

#### Show top nodes between existing nodes

You can select an arrow and show the top dimension items that come between 2 existing nodes in the journey. You can add the top 3 dimension items to Journey canvas as separate nodes, or you can view all top dimension items in a freeform table.

- Right-click the arrow between the 2 nodes where you want to show the top dimension items.
- Select Show top nodes between these nodes .
- Select where you want to show the dimension items: In Journey canvas : Adds the top 3 nodes to the canvas that come between the 2 existing nodes. Each node is connected to the surrounding nodes as a separate branch on the canvas. In a Freeform table : Creates a freeform table visualization showing all top dimension items that come between the 2 existing nodes.
- Select the desired dimension from the list of dimensions. Depending on what you chose in the previous step, the top 3 dimension items are added to the canvas as 3 separate nodes, or all top dimension items are shown in a freeform table.

### Duplicate nodes

The option to duplicate is available for the following objects on the canvas:

- Individual nodes
- Multiple nodes

To duplicate nodes:

- Select one or more nodes that you want to duplicate. To select multiple nodes, hold Command (on Mac) or Ctrl (on Windows).
- Right-click one of the selected nodes, then select Duplicate .

## Design the journey

The order of nodes and the connections between them affect Journey canvas data. Journeys should visually and accurately reflect the sequence of events that you want to report on.

After nodes are added to the canvas, you can rearrange them, combine them, connect them, and add time constraints between them.

### Rearrange nodes

Journeys in Journey canvas consist of a flexible graph of nodes and arrows representing any combination of events, dimension items, and segments.

You can drag nodes on the canvas to rearrange the events and conditions of the journey.

As you rearrange the order of nodes in the journey, data updates accordingly.

### Combine nodes

A combined node in Journey canvas is a single point in the user journey (node) that contains 2 or more components that are joined together through logic.

#### Create combined nodes

You can do any of the following to combine nodes in Journey canvas:

- From the left rail, drag a single component onto a node on the canvas.
- From the left rail, drag multiple components simultaneously onto a node on the canvas.
- From the left rail, drag multiple components simultaneously onto a blank area of the canvas while holding the Shift key.

#### Logic when combining nodes

The logic that is applied to nodes when they are combined differs depending on which component types you are combining, as follows:

TIP
You can view the logic of a combined node by right-clicking the node, then selecting
Create segment from node
. The logic is shown in the
Definition
section.
Component types to combine
Logic (operator) used
Metric + Metric
Joined with OR
Dimension item + Dimension item (from the same parent dimension)
Joined with OR
Dimension item + Dimension item (from different parent dimensions)
Joined with AND
Segment + Segment
Joined with AND
Dimension + Metric, Date range, or Segment
Joined with AND
Date range + Metric, Segment, or Dimension
Joined with AND
Segment + Metric, Date range, or Dimension
Joined with AND
### Connect nodes

You can connect nodes that are already on the canvas, or you can connect a node when adding it to the canvas.

You connect nodes to define the journey’s sequence of events.

#### Arrows between nodes

Nodes are connected by an arrow. Both the arrow direction and width have significance:

- Direction : Indicates the sequence of events of the journey
- Width : Indicates percentage volume from one node to another

#### Logic when connecting nodes

When you connect nodes in Journey canvas, they are connected using the THEN operator. This is also known as [sequential segmenting](/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build).

Nodes are connected as an “eventual path,” which means that visitors are counted as long as they eventually move from one node to the other, regardless of any events occurring between the 2 nodes. The time allotted for users to move along the path is determined by the container setting. It can also be controlled by [adding a time constraint](#add-a-time-constraint-between-nodes).

You can view the logic of connected nodes by right-clicking the node, then selecting **Create segment from node**. The logic is shown in the **Definition** section.

#### Connect existing nodes

Journeys cannot be circular, looping back to previously connected nodes.

To connect nodes in Journey canvas:

- In a Journey canvas visualization, hover over the node that comes first in the journey sequence that you want to connect to another node. 4 blue dots appear on each side of the selected node.
- Drag any of the 4 blue dots to any of the 4 sides of the node that you want to connect to. An arrow appears, connecting the 2 nodes. See Arrows between nodes for more information.

#### Connect nodes when adding a node

When adding a node to the canvas, you can place it between two connected nodes. The node is added to the journey’s flow between the 2 existing nodes.

For more information, see [Add nodes](#add-nodes).

## Manage nodes or arrows

### Rename a node

When you drag a component to a Journey canvas visualization, it creates a node with the same name as the component name. You can rename the node to better match the step of the journey that the node represents.

The option to rename is available for the following objects on the canvas:

- Individual nodes

To rename a node:

- In a Journey canvas visualization, right-click the node that you want to rename.
- Select Rename .
- Specify a new name, then press Enter.

### Add or update a label on an arrow

The arrows that appear between nodes in Journey canvas can be configured to show custom labels and values.

Labels are custom names that appear on arrows. Only a single label is shown on a given arrow.

For more information about the labels and values that appear on arrows, see “Arrow settings” in [Configure visualization settings](#configure-visualization-settings).

The option to add or update a label is available for the following objects on the canvas:

- The arrow between nodes

To add a label to an arrow:

- In a Journey canvas visualization, right-click the arrow where you want to add a label.
- Select Add label .
- Specify a name for the label, then press Enter. If arrow settings are currently configured to hide labels, a message displays, prompting you to show labels.

To update an existing label on an arrow:

- In a Journey canvas visualization, right-click the arrow where you want to add a label.
- Select Update label .
- Specify a name for the label, then press Enter. If arrow settings are currently configured to hide labels, a message displays, prompting you to show labels.

### Apply a breakdown

The option to apply a breakdown to your data is available for the following objects on the canvas:

- Individual nodes
- Multiple nodes
- The arrow between nodes
- Multiple arrows between nodes
- Fallout data (when fallout is shown on a node)

Consider the following when applying a breakdown:

- Breakdowns are applied to the primary metric. The secondary metric is not affected.
- Applying a breakdown does not change the journey. Rather, it simply shows a breakdown of the data for the node where it is applied.
- If a node already has a breakdown, applying a new breakdown replaces the existing one.
- Breakdown data is updated if changes are made at an earlier point in the journey.

#### Apply a breakdown to nodes, arrows, or fallout data

- In a Journey canvas visualization, do any of the following: Right-click the fallout that is coming off a node (when fallout is shown) for which you want to apply a breakdown. Select one or more nodes for which you want to apply a breakdown, then right-click one of the selected nodes. Select one or more arrows between 2 nodes for which you want to apply a breakdown, then right-click one of the selected arrows. To select multiple nodes or arrows, hold Command (on Mac) or Ctrl (on Windows).
- Select Breakdown .
- Select where you want to view the breakdown: In Journey canvas In a freeform table
- Select the dimension that you want to use for the breakdown. If you chose to view the breakdown in Journey canvas, the top 5 dimension items are shown on the node. An option is available on the node to open the breakdown in a freeform table. If you chose to view the breakdown in a freeform table, the top dimension items are shown in a new freeform table immediately above the Journey canvas visualization.

#### Apply a breakdown to an individual node

You can drag a dimension from the left rail onto the node on the canvas where you want to apply the breakdown.

For more information, see [Add nodes](#add-nodes).

#### Remove a breakdown

To remove a breakdown that has been applied:

- Right-click the node that has the breakdown applied.
- Select Remove breakdown .

### Create an audience

The option to create an audience is available for the following objects on the canvas:

- Individual nodes
- Multiple nodes
- The arrow between nodes
- Multiple arrows between nodes
- Fallout data (when fallout is shown on a node)

When you create an audience from multiple nodes or arrows, they are joined with the OR operator.

To create an audience:

- In a Journey canvas visualization, do any of the following: Right-click the fallout that is coming off a node (when fallout is shown) for which you want to create an audience. Select one or more nodes for which you want to create an audience, then right-click one of the selected nodes. Select one or more arrows between 2 nodes for which you want to create an audience, then right-click one of the selected arrows. To select multiple nodes or arrows, hold Command (on Mac) or Ctrl (on Windows). note NOTE Audiences cannot include calculated metrics or any metrics that are based on a summary dataset . If you try to create an audience from any area of Journey canvas that contains a calculated metric or a metric that is based on a summary dataset, the calculated metric will not be included in the audience definition.
- Select Create audience from node or Create audience from arrow .
- Continue creating and publishing the audience as described in Create and publish audiences .

### View trend data

You can view the trend data in a line graph for objects in Journey canvas., with some prebuilt anomaly detection data (this is the definition in Fallout)

The option to trend is available for the following objects on the canvas:

- Individual nodes
- Multiple nodes
- The arrows between nodes
- Multiple arrows between nodes
- Fallout data (when fallout is shown on a node)

To view trend data:

- In a Journey canvas visualization, do any of the following: Right-click the fallout that is coming off a node (when fallout is shown) for which you want to view trend data. Select one or more nodes for which you want to view trend data, then right-click one of the selected nodes. Select one or more arrows between 2 nodes for which you want to view trend data, then right-click one of the selected arrows. To select multiple nodes or arrows, hold Command (on Mac) or Ctrl (on Windows).
- Select Trend .

### Create a segment based on a node, arrow, or fallout data

The option to create a segment is available for the following objects on the canvas:

- Individual nodes
- The arrows between nodes
- Fallout data (when fallout is shown on a node)

After the segment is created, you can use it anywhere in Analysis Workspace.

Segments created from Journey canvas use [sequential segmenting](/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build). This means that the segment uses the THEN operator to link together the sequence of events (the journey) that people flowed through, leading up to the selected node or arrow. All events that match the selected node or arrow are included in the segment.

If you create a segment based on a node that has multiple paths flowing into it, all paths are included in the segment. Separate paths are joined with the OR operator.

To create a segment:

- In a Journey canvas visualization, right-click the node, arrow, or fallout data that you want to use to create the segment.
- Select Create segment from node , Create segment from arrow , or Create segment from fallout . The Segment builder displays. In the Definition section, the segment definition is created based on the node, arrow, or fallout you selected and its context within the journey.
- Specify a title for the segment and make any other changes. For more information about creating a segment, see Segment builder .
- Select Save to save the segment.

### Delete nodes

You can delete one or more nodes at a time within a journey. When you delete a node that is connected between 2 nodes within the journey, the 2 remaining nodes become directly connected.

To delete nodes in Journey canvas:

- In a Journey canvas visualization, select one or more nodes that you want to delete, then right-click one of the selected nodes.
- Select Delete .

### Exclude nodes

When you exclude a node from a journey, the journey data is updated to exclude journeys that went through that node. The segment definition for the journey is also updated to exclude journeys that went through that node.

To exclude a node from a journey:

- In a Journey canvas visualization, right-click the node that you want to exclude.
- Select Exclude from journey .

To re-include an excluded node in the journey:

- In a Journey canvas visualization, right-click the excluded node.
- Select Remove journey exclusion .

### Delete arrows between nodes

You can delete one or more arrows at a time within a journey. When you delete an arrow between 2 nodes, the nodes are no longer connected. If the arrow was part of a longer path, the path is disconnected.

To delete arrows between nodes in Journey canvas:

- In a Journey canvas visualization, select one or more arrows between 2 nodes that you want to delete, then right-click one of the selected arrows.
- Select Delete .

## Open a journey from Journey Optimizer

When viewing a journey in Journey Optimizer, you can choose to view it in Journey canvas.

- In Journey Optimizer, open the journey that you want to analyze in Journey canvas.
- Select Analyze in CJA .

recommendation-more-help
