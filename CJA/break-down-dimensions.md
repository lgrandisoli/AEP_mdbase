---
title: "Break down dimensions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/dimensions/t-breakdown-fa"
category: "other"
topic: "analytics-platform/using/cja-components/dimensions"
created_at: "2026-06-02T19:06:20.027958+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Break down dimensions

Last update: May 13, 2026
- Topics:
- [Dimensions](#)

CREATED FOR:

- User

You can break down your data in Analysis Workspace in unlimited ways for your specific needs; build queries using relevant metrics, dimensions, segments, time lines, and other analysis breakdown values.

- In a Freeform table , from the context menu of one or more selected rows, select Breakdown .
- From the submenu select Dimensions , Metrics , Segments or Date ranges and then select an item. Or simply search for a component in the Search field.

You can break down metrics by dimension items or audience segments across selected time periods. You can also drill down further to a more granular level.

The number of breakdowns to show in the table is limited to 400. This limit increases for exporting breakdowns.
## Breakdown by position

By default, breakdowns are fixed to static row items. For example, imagine you breakdown the top 3 Page dimension items (Homepage, Search Results, Checkout) by Marketing Channel. Then, you leave the project and return two weeks later. Upon opening the project again, the top 3 pages have changed, and now Homepage, Search Results and Checkout are the top 4-6 pages instead. By default, your Marketing Channel breakdowns still appear under Homepage, Search Results and Checkout, even though they are now in rows 4-6.

In contrast, **Breakdown by position**, always breaks down the top 3 items, regardless of what thse items are. Referring back to the example, when you re-open your project, the Marketing Channel breakdowns are tied to the top 3 pages in the table. And not to Homepage, Search Results and Checkout, which are now in rows 4-6. See [Row settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/table-settings) how to configure this setting.

## Apply attribution models to breakdowns

Any breakdown within a table can also have any attribution model applied to it. This attribution model can be the same or different from the parent column. For example, you can analyze linear Orders on your Marketing Channels dimension but apply U-Shaped Orders to the specific tracking codes within a Channel. To edit the attribution model applied to a breakdown, hover over the breakdown model and select **Edit**.

This is the expected behavior when applying attribution models to breakdowns or editing them:

- If you apply an attribution when no other attributions exist, then the attribution applies to the entire column tree.
- If you add a breakdown after an attribution has been applied, it will use the default for the given breakdown that was added (if that dimension has a default). Otherwise it will use the breakdown from the parent column. Some dimensions have a default allocation. For example, Time dimensions and Referrer use Same Touch. The Product dimension uses Last Touch. Other dimensions don’t have a default, and will use the parent column allocation.
- If there are already attributions in the column tree, changing the attribution only impacts the one you are editing.

See [Dimension in Analysis Workspace](/en/docs/analytics-learn/tutorials/analysis-workspace/dimensions/adding-dimensions-and-metrics-to-your-project-in-analysis-workspace#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
See [Dimension breakdowns](https://video.tv.adobe.com/v/23969?quality=12&learn=on#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
See [Adding dimensions and metrics](/en/docs/analytics-learn/tutorials/analysis-workspace/dimensions/adding-dimensions-and-metrics-to-your-project-in-analysis-workspace#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
See [Working with dimensions in a Freeform Table](/en/docs/analytics-learn/tutorials/analysis-workspace/building-freeform-tables/working-with-dimensions-in-a-freeform-table#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
See [Dimension breakdown by position](https://video.tv.adobe.com/v/24033#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
recommendation-more-help
