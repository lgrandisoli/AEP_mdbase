---
title: "Content Analytics reporting overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/content-analytics/report/report"
category: "overview"
topic: "analytics-platform/using/content-analytics/report"
created_at: "2026-06-02T19:06:57.854404+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Content Analytics reporting overview

Last update: May 13, 2026
- Topics:
- [Content Analytics](#)

CREATED FOR:

- User

You report, perform analysis and gain insights on Content Analytics within [Analysis Workspace](/en/docs/analytics-platform/using/cja-workspace/home). A specific Workspace [template](#template) is available, so you can immediately access a pre-populated Workspace project with relevant content insights.

To create your own Content Analytics report from scratch, follow these steps:

- Create a [new project](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/create-projects) or open an [existing project](/en/docs/analytics-platform/using/cja-workspace/build-workspace-project/open-projects) in Workspace.
- Ensure you [select a data view](/en/docs/analytics-platform/using/cja-workspace/panels/panels#data-view) for Content Analytics reporting. Content Analytics reporting is only available for data views that are [configured](/en/docs/analytics-platform/using/content-analytics/configuration/configuration) for Content Analytics.
- Drag a [Freeform table](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table) visualization onto the canvas.
- Use [specific Content Analytics components](/en/docs/analytics-platform/using/content-analytics/report/components) and other generic [components](/en/docs/analytics-platform/using/cja-components/overview) (like segments, date ranges, annotations) to build your Content Analytics insights.
- Use other [visualizations](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations) to enhance your project.

## Thumbnails

Based on the Content Analytics specific dimensions that you use in your project, thumbnails are displayed in the following visualizations:

### Freeform table

By default, thumbnails are shown in a [freeform table](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table). To configure the display of thumbnails for a Content Analytics dimension:

- Hover over a header row for a Content Analytics dimension. For example, **Asset IDs** or **Experience IDs**.
- Select .
- In the **Row setting** popup, underneath **Settings**, check or uncheck **Show Thumbnails**.

### Bar (stacked) and Horizontal bar (stacked)

Thumbnails are displayed as part of the legend on the vertical or horizontal axis. Thumbnails are also displayed when you hover over a bar in a [bar (stacked)](/en/docs/analytics-platform/using/cja-workspace/visualizations/bar) and [horizontal bar (stacked)](/en/docs/analytics-platform/using/cja-workspace/visualizations/horizontal-bar).

### Scatter

Thumbnails are displayed when you hover over a data point in a [scatter](/en/docs/analytics-platform/using/cja-workspace/visualizations/scatterplot).

### Line

AVAILABILITY
The functionality described in this section is in the Limited Testing phase of release and might not be available yet in your environment. This note will be removed when the functionality is generally available. For information about the Customer Journey Analytics release process, see
Customer Journey Analytics feature releases
.
Thumbnails are displayed when you hover over a data point in a [line](/en/docs/analytics-platform/using/cja-workspace/visualizations/line).

## Previews

AVAILABILITY
Bar and scatter visualizations described in this section are in Limited Testing and might be unavailable in your environment. This note is removed when the functionality is generally available. For information about the Customer Journey Analytics release process, see
Customer Journey Analytics feature releases
.
You can open a preview popup window. To do so:

- Select in a [freeform table](#freeform-table).
- Select a specific bar in a [bar](#bar-and-horizontal-bar) or [horizontal bar](#bar-and-horizontal-bar) visualization, or a data point in [scatter](#scatter) visualization.

You see the following details.

Experience preview
Asset preview
Name of the dimension (for example,
Experience ID)
Name of the asset dimension (for example,
Asset ID)
Impressions (all time)
: Number of impressions for the experience.
Impressions (all times)
: Number of impressions for the asset.
Assets
: Number of assets this experience contains.
Select
Breakdown
to inspect the assets.
Experiences
: Number of experiences where this asset is shown in.
Select
Breakdown
to inspect the assets.
First impression
: Date of first impression of the experience.
First impression
: Date of first impression of the asset.
Most recent impression
: Date of most recent impression of the experience.
Most recent impression
: Date of most recent impression of the asset.
Experience attributes
: The
attributes
of the experience.
Asset attributes
: The
attributes
of the asset.
## Template

A Content Analytics [template](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates) is available to help you learn what content and content attributes are performing best. The template is part of the [Web channel and Engagement use case](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#web-engagement) and details how your content performs at a granular level. You can look at the performance of individual assets, or specific attributes.

Based on what you learn, you might do a number of things. Like promote high performing assets on your home page, personalize content for specific segments to include high performing attributes, or rotate out content that has started to get stale.

To use the template:

- Select **Workspace** from the main menu.
- Ensure you have selected a Data view that is configured for Content Analytics.
- Search for, or use segments (**Web** for **Channel** and **Engagement** for **Use Case**s) to find and select the **Content Analytics** template.
- Select **Use template**.
- In the **Set up your template** dialog, select a metric from the **Select a conversion metric** dialog. For example, **Asset CTR**.
- Select **Continue**.

A **Content Analytics Overview** project opens in [Analysis Workspace](/en/docs/analytics-platform/using/cja-workspace/home). The project consists of four [panels](/en/docs/analytics-platform/using/cja-workspace/panels/panels), where each panel provides [freeform tables](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table) and [visualizations](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations) to answer a specific question.

You can use the **Content Channel** breakdown to [break down](/en/docs/analytics-platform/using/cja-workspace/panels/panels#break-down-a-panel) the panel for the content channel you are interested in: **web** or **mobile**.

The four panels are:

- What content performs the best? This panel identifies which experiences and assets drive engagement and conversion. Experiences are full webpages captured at a specific time, or a combination of text, assets, and calls to action defined within a mobile app. Experiences . note NOTE These visualizations only show up in your template when you have configured the system to include experiences in your Content Analytics configuration. Experience CTR : a summary change visualization that shows Experience CTR. Top converting experiences : A horizontal bar visualization showing top converting experiences based on the selected conversion metric. Top performing experiences : A freeform table (including thumbnails and previews ) for the top performing experiences. Assets Asset CTR A summary change visualization that shows Asset CTR. Top converting assets A horizontal bar visualization that shows top converting assets based on the selected conversion metric. Top performing assets A freeform table (including thumbnails and previews ) for the top performing assets. Assets - views compared to conversion. A scatterplot visualization that shows a scatter plot of asset views versus assets conversions.
- Which asset attributes contribute to conversions? Content Analytics uses AI and GenAI to automatically assign metadata and attributes, such as subjects, scenes, and foreground colors, to every asset. Top converting asset attributes A horizontal bar that shows the top converting asset attributes based on the selected conversion metric. Top converting asset attributes vs prior 30 days A horizontal bar visualization that shows the top converting asset attributes, compared to the prior 30 days, based on the selected conversion metric. Top converting assets attribute data A freeform table that shows the top converting attributes based on the selected conversion metric. Select a row in the table to update the Attribute trend visualization. Attribute trend A line visualization showing the attribute trend for the selected top converting asset attribute. Asset foreground color An example freeform table that compares the performance of items from a single asset attribute category: Foreground Colors. You can replace this asset attribute with other asset attribute category dimensions.
- Which experience attributes contribute to conversions? note NOTE This panel only shows when you have included experiences in your Content Analytics configuration. While asset attributes focus on the visual qualities of images, experience attributes focus on the text of your page. The visualizations below let you explore which experience attributes contribute to conversion. These attributes are also automatically assigned using AI and GenAI models. The panel consists of the following visualizations: Top converting experience attributes A horizontal bar visualization that shows the top converting experience attributes based on the selected conversion metric. Top converting experience attributes compared to the prior 30 days A horizontal bar visualization that shows the top converting experience attributes, compared to the prior 30 days, based on the selected conversion metric. Top converting experience attribute data A freeform table that shows the top converting experiences based on the selected conversion metric. Select a row in the table to update the Line visualization. Line A line visualization showing the trend for the selected top converting experience attribute. Experience keywords A freeform table showing the top experience keywords based on the selected conversion metric.
- Where do assets appear on my site? This freeform table details where your most viewed assets appear. Use this analysis to identify high-performing pages and optimize asset placement. Where do the most viewed assets appear? You can break down any asset by dimensions to help you better understand where that image appears. In the example freeform table (including thumbnails and previews ), Asset Perception ID is used instead of Asset Id. Sometimes, the exact same image can get duplicated on your site with a different image URL. The Asset Perception ID attribute helps to group these duplicates under a single ID. Because assets can change on a page, the system breaks down each asset by Experience Id to identify the version of the page where the asset appeared. You can replace Experience Id with other dimensions that help you understand the location of an asset on your site. For example, Page name, Page URL, or Site section. You can also swap out Asset Perception ID with Asset Id to get a record of where specific image URLs are being referenced.

Related Articles
Content Analytics components
Use templates
recommendation-more-help
