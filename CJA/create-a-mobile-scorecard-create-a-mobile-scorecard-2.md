---
title: "Create a mobile scorecard create-a-mobile-scorecard"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dashboards/create-scorecard"
category: "other"
topic: "analytics-platform/using/cja-dashboards/create-scorecard"
created_at: "2026-06-23T20:42:37.711277+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create a mobile scorecard create-a-mobile-scorecard

Last update: May 13, 2026
- Topics:
- [Analytics Dashboards](#)

CREATED FOR:

- User
- Admin

The following information instructs curators of Customer Journey Analytics data on how to configure and present dashboards for executive users. To start with, you can view the Analytics dashboards scorecard builder video:

See [Createa mobile scorecard](/en/docs/customer-journey-analytics-learn/tutorials/dashboards/create-a-mobile-scorecard#_blank) for a demo video.

style
shade-box
NOTE
Analytics scorecard screen shots for this page were taken from the Adobe Analytics UI, not from Customer Journey Analytics. The UIs are almost identical.
An Analytics scorecard displays key data visualizations for executive users in a tiled layout, as shown below:

As a curator of this scorecard, you can use the scorecard builder to configure which tiles appear on the scorecard for your executive consumer. You also configure how the detailed views, or the breakdowns, can be adjusted once the tiles are tapped. The scorecard builder interface is shown below:

To create the scorecard, you need to do the following:

- Access the Blank mobile scorecard template in Workspace.
- Configure the scorecard with data and save it.

## Access the Blank Mobile Scorecard template template

You can access the Blank Mobile Scorecard template either by creating a new project, or from the Tools menu.

### Create a new project create

- Open Customer Journey Analytics and click the **Workspace** tab.
- In the left rail, click **Projects**.
- Click **Create project** and select the **Blank mobile scorecard** project template.
- Click **Create**.

### Tools menu

- From the **Tools** menu, select **Analytics dashboards (Mobile App)**.
- On the subsequent screen, click **Create new scorecard**.

## Configure the scorecard with data and save it configure

To implement the scorecard template:

- Under Scorecard properties (in the right-hand rail), specify a Project data view from which you want to use data.
- To add a new tile to your scorecard, drag a metric from the left panel and drop it into the Drag and Drop Metrics Here zone. You can also insert a metric between two tiles using a similar workflow.
- From each tile, you can access a detailed view that displays additional information about the metric, such as top items for a list of related dimensions.

## Add dimensions or metrics dimsmetrics

To add a related dimension to a metric, drag a dimension from the left panel and drop it onto a tile.

For example, you can add appropriate dimensions (like **Marketing Channel**, in this example) to the **Unique Visitors** metric by dragging and dropping it onto the tile. Dimensions breakdowns appear under the Drill Ins (breakdown) section of the tile-specific **Properties**. You can add multiple dimensions to each tile.

## Apply segments segments

To apply segments to individual tiles, drag a segment from the left panel and drop it directly on top of the tile.

If you want to apply the segment to all the tiles in the scorecard, drop the tile on top of the scorecard. Or, you can also apply segments by selecting them in the segment menu beneath the date ranges. You [configure and apply segments for your scorecards](/en/docs/analytics-learn/tutorials/analysis-workspace/using-panels/using-drop-down-filters) the same way you would in Customer Journey Analytics Workspace.

## Add date ranges dates

Add and remove date range combinations that can be selected in your scorecard by selecting the date range drop down.

Each new scorecard starts with 6 date range combinations focusing on the data from today and yesterday. You can remove unnecessary date ranges by clicking on the x, or you can edit each date range combination by clicking the pencil.

To create or change a primary date, use the drop down to select from available date ranges or drag and drop a date component from the right rail into the drop zone.

To create a comparison date, you can select from convenient pre-sets for common time comparisons in the drop-down menu. You can also drag and drop a date component from the right rail.

If the date range you want hasn’t been created yet, you can create a new one by clicking the calendar icon.

This will take you to the date range builder where you can create and save a new date range component.

### Show or Hide comparison date ranges show-comparison-dates

To include comparison date ranges, toggle the **Include comparison dates** setting.

The setting is *on* by default. Toggle it to *off* if you don’t want to view comparison dates.

## Apply visualizations viz

Analytics dashboards offer four visualizations that give you great insight into dimension items and metrics. Change to a different visualization by changing the chart type of a tile’s Properties. Just select the right tile and then change the chart type.

Or, click the Visualizations icon in the left rail and drag and drop the right visualization onto the tile:

### Summary Number

Use the Summary Number visualization to highlight a large number that is important in a project.

### Donut

Similar to a pie chart, this visualization shows data as parts of a whole. Use a donut graph when comparing percentages of a total. For example, you want to see which ad platform contributed to the total number of unique persons:

### Line

The Line visualization represents metrics using a line in order to show how values change over a period of time. A line chart shows dimensions over time but works with any visualization. You are visualizing the product category dimension in this example.

### Horizontal Bar

This visualization shows horizontal bars representing various values across one or more metrics. For example, to easily see what your top products are, use Horizontal Bar for your preferred visualization.

## Name scorecards name

To name the scorecard, click the namespace in the upper-left of the screen and type the new name.

### Remove Unspecified dimension item remove-dims

If you want to remove Unspecified dimension items from your data, do the following:

- Select the correct tile.
- In the right rail, under Drill ins , select the right-arrow next to the dimension item whose Unspecified items you want to remove.
- Click the icon next to Unspecified to remove unspecified data from your reporting. (You can also remove any other dimension item.)

## View and configure tile properties tiles

When you click a tile in the scorecard builder, the right-hand rail displays the properties and characteristics associated with that tile and its detail slide. In this rail, you can provide a new **Title** for the tile and alternatively configure the tile by applying segments.

## View detail slides view-detail-slides

When you click on tiles, a dynamic pop-up window displays how the detail slide appears to the executive user in the app. You can add dimensions to break down your data for your specific needs. If a dimension hasn’t been applied, the breakdown dimension will be **hour** or **days**, depending on the default date range.

Breakdowns refine your analysis by breaking down metrics by dimension items such as the following:

- Unique Visitors metric broken down by Ad Platform (AMO ID)
- Visits broken down by Product Category (Retail)
- Total Revenue broken down by Product Name

Each dimension added to the tile will show up in a drop-down menu in the detailed view of the app. The executive user can then choose among the options listed in the drop-down menu.

## Customize detail slides customize-detail-slide

Custom detail slides allow you to be even more targeted about what information you share with your audience.

See [Custom detail views](/en/docs/customer-journey-analytics-learn/tutorials/visitor-id/stitching-enablement-and-validation#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
You can modify the layout for each detail slide and add text to better explain what the end user may see in the data. You can also change the chart type using the drop-down menu.

### Change the slide layout

Change the slide layout to focus on the most important information. For example, you can change the layout to show just a chart or just a table. To change the slide layout, select one of the pre-designed formats.

You can also change the slide layout by dragging and dropping visualization components from the left-hand rail onto the canvas. Each detail slide may only accommodate two visualizations at a time.

### Add descriptive text to a slide

You can add text to provide meaningful information about what is contained in the charts or nuances about the data.

To add text to a detail slide, select a layout that shows the T symbol, or drag and drop the Text visualization component over from the left rail. The text editor will automatically open when adding a new text visualization or choosing a slide layout with text. The Text editor provides all standard options for formatting your text. You can apply text styles such as paragraph, headings, and subheadings, and apply bold and italicized font. You can justify text, add bulleted and numbered lists, and add links. When you’re finished editing, select the minimize button in the upper-right corner of the text editor to close it. To edit text you already added, select the pencil icon to open the text editor again.

## Remove components remove

Similarly, to remove a component that is applied to the entire scorecard, click anywhere on the scorecard outside of the tiles and then remove it by clicking the **x** that appears when you hover over the component, as shown below for the **First Time Visits**:

## Create data stories create-data-story

A data story is a collection of supporting data points, business context, and related metrics built around a central theme or metric.

For example, if you focus on web traffic, your most important metric may be visits, but you may also be interested in new persons, unique persons, and you may want to see data broken down by web page or by what device type the traffic is coming from. Data stories in mobile scorecard projects let you put your most important metrics front and center while telling the whole story behind the metrics with multiple detail slides.

Watch the video to learn more about creating data stories in mobile scorecard projects in Analysis Workspace.

See [Data stories for a Mobile scorecard project](/en/docs/customer-journey-analytics-learn/tutorials/dashboards/create-a-mobile-scorecard#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
**To create a data story**

Build your data story by adding multiple detail slides to a tile.

- Start with a mobile scorecard project.
- Select a tile that you want to create a story from. {width=".50%"}
- Add slides to build your data story. Your first slide is generated by default. To add new slides, either hover over or click on a slide, then select from the available options: Tap the + sign to create a new slide. Tap the duplicate icon to duplicate the existing slide.
- If you create a blank slide, drag and drop components from the left rail, or choose a layout to automatically populate the slide with the data from the tile. To delete a slide, tap the trash icon.

### Customize a data story customize-data-story

Data stories allow you to customize everything so you can share information that you want to share and exclude everything that you don’t need. You can customize tiles and individual slides to add segments, show breakdowns, change the layout, and change the visualizations.

**To customize tiles**

- Tap a tile. The selected tile is outlined in blue, and the right panel shows the Tile properties.
- Change the title, chart type, and other tile options.
- Drag a component onto the tile. When you drag and drop a component such as a visualization onto a tile, the component is applied to all data story slides.
- To apply a change only to the title, hold the Shift key to apply the change.

NOTE
Slides inherit components from the tile, but tiles don’t inherit components from slides.
**To customize individual slides**

You can change the visualization for individual slides in a data story. For example, you can change a horizontal bar to a doughnut graph for a specific slide. You can also change the layout. See [Customize detail slides](#customize-detail-slide).

### Preview a data story preview-data-story

After you create a data story, use the **Preview** button to view and interact with a data story as if you were an app user. For information about previewing your data story, see [Preview a scorecard](#preview)

### Navigate between tiles and slides navigate-tiles-slides

The navigation bar displays icons that represent what’s on each slide. The navigation bar makes it easy to navigate to a specific slide if you have a lot of slides.

To move between the tile and slides, tap the navigation bar. {width="45%"}

You can also navigate back and forth by using the arrows on your keyboard or by selecting a component and holding it to the left or right of your screen to scroll.

## Preview scorecards preview

You can preview how the scorecard will look and function once it is published in the Adobe Analytics dashboards app.

- Click Preview in the upper right hand corner of the screen.
- To view what the scorecard will look like on different devices, select a device from the Device preview drop-down menu.
- To interact with the preview, you can: Left click to simulate tapping on the phone screen. Use your computer’s scroll function to simulate scrolling the phone screen with your finger. Click and hold to simulate pressing and holding your finger on the phone screen. This is useful for interacting with the visualizations in the detailed view.

## Share scorecards share

To share the scorecard with an executive user:

- Click the Share menu and select Share scorecard .
- In the Share Mobile Scorecard form, complete the fields by: Providing the name of the scorecard Providing a description of the scorecard Adding relevant tags Specifying the recipients for the scorecard
- Click Share .

After you have shared a scorecard, your recipients can access it on their Analytics dashboards. If you make subsequent changes to the scorecard in the scorecard builder, they will be automatically updated in the shared scorecard. Executive users will then see the changes after refreshing the scorecard on their app.

If you update the scorecard by adding new components, you may want to share the scorecard again (and check the **Share embedded components** option) in order to make sure that your executive users have access to these changes.

### Share scorecards using a shareable link

Using a shareable link makes it easy to share a scorecard in an email, document, or text message app. The shareable link lets recipients open the scorecard on their desktop or on the dashboards mobile app. Shareable deep linking makes it even easier to share projects and boost engagement with your stakeholders.

To share a scorecard using a shareable link

- Click the Share menu and select Share scorecard .
- Copy the link and paste it into an email, document, or IM app. When a recipient uses a desktop app or browser to open the link, the mobile scorecard project will open in Workspace. When a recipient opens the link on a mobile device, the scorecard will open directly in the Adobe Analytics dashboards app. If a recipient hasn’t downloaded the mobile app, they’ll be directed to the app listing in the App Store or Google Play Store where they can download it.

recommendation-more-help
