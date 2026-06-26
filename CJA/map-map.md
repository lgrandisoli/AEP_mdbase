---
title: "Map map"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/map"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:07:58.997579+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Map map

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User
- Admin

markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
Can you do this?
                
                ## Add a breakdown from the map visualization
                
                You can break down a specific dimension item, metric, segment, or date range for the data within a designated area that you select in the map visualization.
                
                To add a breakdown from the map visualization:
                
                1. (Optional) Zoom in on the specific area of the map that contains the data where you want to add the breakdown.
                
                1. Click the selection tool ![map selection icon](assets/map-selection-icon.png), then drag your mouse to select the desired area.
                
                1. Select **Add breakdown**.
Can you do this?
                
                ## Export the map visualization as a PDF
                
                To export the map visualization in PDF format:
                
                1. how...
*This article documents the Map visualization in* *Customer Journey Analytics .**See Map for the* *Adobe Analytics version of this article.*

style
shade-box
The **Map** visualization in Analysis Workspace allows you to build a visual map of any metric (including calculated metrics). It is useful for identifying and comparing metric data across different geographic regions.

See [Map visualization](/en/docs/customer-journey-analytics-learn/tutorials/analysis-workspace/visualizations/configure-and-use-the-map-visualization#_blank) for a demo video.

style
shade-box
## Prerequisites

### Add context labels in data views

In Customer Journey Analytics data views settings, administrators can add [context labels](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview) to a dimension or metric and Customer Journey Analytics services like the map visualization can use these labels for their purposes.

#### Required context labels for latitude and longitude in the map visualization

Context labels are required for the map visualization to function. Without the following context labels present, the map visualization does not work, because there is no latitude and longitude data to work with.

- Geo: Latitude
- Geo: Longitude

To add these context labels:

- In Customer Journey Analytics, select Data Management > Data views .
- On the Data views page, select the data view that contains data that you want to analyze in the map visualization.
- Select the Components tab.
- (Conditional) If you are using the Web SDK and you have configured latitude and longitude to be populated in your data stream, or if you are using the Analytics Source Connector to populate event data, then latitude and longitude fields should already be available in your schema and populated with the correct context labels. Locate these Latitude and Longitude schema fields (in Event datasets > placeContext > geo > _schema ) and drag them into your data view as dimensions if they aren’t already present. When these schema fields exist as dimensions in your data view, their context labels are automatically applied, and the map visualization uses them without any additional configuration.
- (Conditional) If you have custom dimensions that you want to use for latitude and longitude data, you can configure the context labels on the custom fields: In the Dimensions section, select the dimension that contains the longitude data. In the Component settings section in the right rail, in the Context labels field, begin typing Longitude , then select it from the drop-down menu. Repeat this process to add the Latitude context label to the dimension that contains the latitude data. (Optional) By default, these dimensions are precise to the town or zip code level in the map visualization, and they show 2 decimal places in Workspace reports. You can adjust them to be precise within a single meter in the map visualization and to show 5 decimal places in Workspace reports. For more information about how to adjust the precision level, see Configure precise locations for dimensions .
- Select Save and continue > Save and finish .

#### Required context labels for geo templates

Adobe provides several [pre-built templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#web-audience) that use the map visualization. To use each template, you must add the corresponding context label to a dimension in your data view.

Following are the templates and the required context label. Without these labels present, the templates do not work, because there is no geo data to work with.

Template name
Required context label
Geo countries
Geo: Geo Country
Geo regions
Geo: Geo Region
Geo cities
Geo: Geo City
Geo US states
Geo: Geo State
Geo US DMA
Geo: Geo Dma
To add these context labels:

- In Customer Journey Analytics, select Data Management > Data views .
- On the Data views page, select the data view that contains data that you want to analyze with pre-built templates that use the map visualization. In this data view, pick five dimensions: one with the country data, one with the region data, one with the city data, one with the state data, and one with the DMA data. Then, label those dimensions with the corresponding context label.
- Select the Components tab.
- (Conditional) If you are using the Web SDK and you have configured geo fields to be populated in your data stream, or if you are using the Analytics Source Connector to populate event data, then geo fields should already be available in your schema and populated with the correct context labels. Locate the appropriate schema fields, such as City , Postal code , State or province (in Event datasets > placeContext > geo ), then drag them into your data view as dimensions if they aren’t already present. When these schema fields exist as dimensions in your data view, their context labels are automatically applied, and the geo templates use them without any additional configuration.
- (Conditional) If you have custom dimensions that you want to use for geo data, you can configure the context labels on the custom fields: Select the dimension that contains the country data. In the Component settings section in the right rail, in the Context labels field, begin typing Geo Country , then select it from the drop-down menu. Repeat this process to add the Geo: Geo Region , Geo: Geo City , Geo: Geo State , and Geo: Dma context label to each dimension that contains the corresponding data.
- Select Save and continue > Save and finish .

### Graphics drivers must support WebGL rendering

The map visualization uses WebGL for graphics display. If your graphics drivers do not support WebGL rendering, you might need to update your drivers.

## Map visualization in Customer Journey Analytics vs. Adobe Analytics

The map visualization in Customer Journey Analytics differs from the map visualization in Adobe Analytics in the following ways:

Feature
Customer Journey Analytics
Adobe Analytics
Data source
Use any segment available in your data view as your data source.
Provides the following options:

- Mobile lat/long
- Geographic DimensionRepresents geo segmentation data about visitor location based on the visitor’s IP address.

Precision
For datasets with deep precision, you can configure the dimensions in your data view to show up to 5 decimal places. This allows the map visualization to be accurate within a single meter.

For more information, see [Configure precise locations for dimensions](#configure-precise-locations-for-dimensions).

Data is accurate to the Country, Region, and City level. (It does not go to the DMA or Zip Code level.)
Create a segment from a selection
Create a segment based on a specific area that you select in the map visualization.

For more information, see [Create a segment from the map visualization](#create-a-segment-from-the-map-visualization).

Create a segment based on the data that is being reported in the map visualization in general.
Create an audience from a selection
Create an audience based on a specific area that you select in the map visualization.

For more information, see [Create an audience from the map visualization](#create-an-audience-from-the-map-visualization).

Cannot create an audience from the map visualization.
Create a trend from a selection
Create a trended line chart visualization based on a specific area that you select in the map visualization.

For more information, see [Create a trended line chart from the map visualization](#create-a-trended-line-chart-from-the-map-visualization). is this correct?

Cannot create a trend from the map visualization.
Add a breakdown from a selection
Break down a specific dimension item, metric, segment, or date range within a specific area that you select in the map visualization.

For more information, see [Add a breakdown from the map visualization](#add-a-breakdown-from-the-map-visualization).

Cannot add a breakdown from the map visualization.
## Build a map visualization begin-building-map

- Select the Visualizations icon in the left rail, then drag the Map visualization into a panel that contains a freeform table. Or Add a map visualization in any of the ways described in the Add visualizations to a panel section in Visualizations overview . {width="50%"}
- Specify the following basic information to configure the map visualization: Add metric : In the metric drop-down list, select a metric or calculated metric. (You can also drag a metric from the left rail.) note important IMPORTANT If you choose a metric that has attribution applied , the same attribution is applied to the latitude and longitude pairs within the map visualization’s current viewport. Add segment : (Optional) In the segment drop-down list, select a segment. Or drag in a segment from the list of segments. You can update this information after the visualization is built by selecting the Edit icon in the visualization header.
- Select Build . A world map visualization with bubbles is generated.
- Continue with View a map visualization and Configure visualization settings .

## View a map visualization

- If you haven’t already, build a map visualization as described in Build a map visualization .
- In the map visualization in Analysis Workspace, do any of the following: Zoom in : You can zoom in on the map to magnify certain areas in any of the following ways: Double-click the map with your mouse. Use your mouse scroll wheel or similar action on your trackpad. Select the plus icon on the map visualization. The map zooms accordingly. The required dimension (country > state > city) is automatically updated, based on the zoom level. Zoom out : You can zoom out on the map to view larger areas in any of the following ways: Hold the Shift key and double-click the map with your mouse. Use your mouse scroll wheel or similar action on your trackpad. Select the minus icon on the map visualization. The map zooms accordingly. The required dimension (country > state > city) is automatically updated, based on the zoom level. Rotate : You can rotate the map in 2D or 3D by holding the Ctrl key while dragging the map with your mouse. To reset the map to its original north alignment, select the compass icon . Selection tool : You can select an area of the map to create a segment , create a trend , or add a breakdown . Click the selection tool , then drag your mouse to select the desired area. Compare : You can compare two or more map visualizations in the same project by placing them side by side. Show period-over-period comparisons (such as year-over-year) : Show negative numbers. For example, if you are plotting a year-over-year metric, the map can show -33% over New York. With metrics that are of type percent , clustering averages the percentages together. A green and red color scheme indicates positive and negative. Additional visualization settings : Select the Settings icon in the visualization header to view additional settings for the map visualization. For more information, see Configure visualization settings .
- Save the project to save all map settings (coordinates, zoom, rotation).
- (Optional) The freeform table below the visualization can be populated by dragging in location dimensions and metrics from the left rail.

## Configure visualization settings

To configure settings for the map visualization:

- In Analysis Workspace, open an existing map visualization, or build a new one .
- Hover over the map visualization, then select the Settings icon in the visualization header. The following options are available: table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 Section Setting Description Map type Bubbles Plots events using bubbles. A bubble chart is a multi-variable graph that is a cross between a scatterplot and a proportional area chart. This view is the default. Heatmap Plots events using a heatmap. A heatmap is a graphical representation of data where the individual values contained in a matrix are represented as colors. Styles Color theme Shows the color scheme for the heat map and bubbles. You can choose among Coral, Reds, Greens or Blues. The default is Coral. Map style You can choose from Basic, Streets, Bright, Light, Dark, and Satellite. Cluster radius Groups data points together that are within the specified number of pixels. The default is 50. This option is available only when Bubbles is selected as the Map type . Custom max value Lets you alter the threshold for the max value for the map. Adjusting this value adjusts the scale for the bubbles or heatmap values (color and size) relative to the custom max value that you set. Show annotations Shows the annotations made for this visualization. Hide title Hides the title of the visualization.

## Configure precise locations for dimensions

If you have custom datasets with deep precision, you can configure the map visualization to achieve location accuracy within a single meter.

- In Customer Journey Analytics, select Data Management > Data views .
- Select the data view that contains the dimensions that you want to configure to use more precise locations.
- In the data view, select the Components tab.
- Select the dimensions that you are using for latitude and longitude that you want to configure. For more information about which dimensions you’re using, see Required context labels for latitude and longitude in the map visualization .
- Configure the level of precision for the dimension: With the dimension that you want to configure still selected, expand the Format section in the right rail. In the Decimal places field, change the number of decimals to reflect the desired level of precision: 0: Precise to the large region or country level in the map visualization. Shows 0 decimal places in Workspace reports. 1: Precise to the region or large city level in the map visualization. Shows 1 decimal place in Workspace reports. 2: Precise to the town or zip code level in the map visualization. Shows 2 decimal places in Workspace reports. This is the default selection. 3: Precise to the very small town or neighborhood level in the map visualization. Shows 3 decimal places in Workspace reports. 4: Precise to a specific parcel of land or building level in the map visualization. Shows 4 decimal places in Workspace reports. 5: Precise to a single meter in the map visualization. Shows 5 decimal places in Workspace reports.
- Select Save and continue > Save and finish .

## Create a segment from the map visualization map-create-segment

You can create a segment based on a specific area that you select in the map visualization. When you create a segment based on a selected area, any data that is within the latitude and longitude of your selection is included in the segment.

To create a segment from the map visualization:

- Zoom or pan to the area of the map that contains the data that you want to use for your segment.
- Do either of the following: To create a segment from everything currently shown in the map: Right-click anywhere on the map, then select Create segment from current view . To create a segment for a more specific area of the map: Click the selection tool , drag your mouse to select the desired area, then select Create segment from selection .
- Use the Segment builder to define the new segment. For more information, see Segment builder .

## Create an audience from the map visualization

You can create an audience based on a specific area that you select in the map visualization.

To create an audience from the map visualization:

- Zoom or pan to the area of the map that contains the data that you want to use for your audience.
- Do either of the following: To create an audience from everything currently shown in the map: Right-click anywhere on the map, then select Create audience from current view . To create an audience for a more specific area of the map: Click the selection tool , drag your mouse to select the desired area, then select Create audience from selection .
- Use the Audience builder to define the new audience. For more information, see Audience builder in Create and publish audiences

## Create a trended line chart from the map visualization

You can create a trended line chart visualization for the data within a specific area that you select in the map visualization.

To create a trended line chart from the map visualization:

- Zoom or pan to the area of the map that contains the data that you want to use for the trended line chart.
- Do either of the following: To create a trended line chart from everything currently shown in the map: Right-click anywhere on the map, then select Trend from current view . To create a trended line chart for a more specific area of the map: Click the selection tool , drag your mouse to select the desired area, then select Trend . A line visualization is built that includes a trendline. For more information about this visualization, see Line .

recommendation-more-help
