---
title: "Summary data group component settings summary-data-group-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/summary-data-group"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-23T20:42:50.655318+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Summary data group component settings summary-data-group-component-settings

Last update: June 5, 2026
- Topics:
- [Data management](#)
- [Analysis Workspace](#)

CREATED FOR:

- Admin

A summary data group creates an association between all dimensions in the grouping and is used to combine dimensions from summary datasets with other dimensions for reporting.

To create a grouping of dimensions:

- Select a dimension.
- Select **Summary data group**.
- Enable **Create grouping**.
- Select a dimension from the **Dimension** drop-down menu, that you want to group with the selected dimension from the first step. Note that only dimensions you have already added to the data view are available from the drop-down menu.
- Optionally, enable **Hide in reporting** to hide the grouped dimension from reporting. Enabling this option is similar as configuring **Hide in reporting** on the grouped dimension separately. See [Component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview) for more information.
- Optionally, to add additional dimensions to the grouping, select **Add dimension to group**.You can add up to nine dimensions, as a summary data group has a limit of ten dimensions.

## Same component settings

When grouping dimensions, you must ensure the settings for Substring, Behavior (Lower case), and Include exclude values, for each of the dimensions that are part of the group, are the same. Otherwise, each dimension of the group can potentially return different results prior to the grouping.For example:

- You have created a summary data group for campaign_code (part of summary data) and tracking_code(part of your event data).
- You have applied Behavior (Lower case) to the campaign_code but not to the tracking_code dimension.

Values in tracking_code can potentially show up as different from campaign_code.

IMPORTANT
Ensure you do the grouping of dimensions from one dimension only, and not apply grouping from multiple dimensions. For example, if you create a grouping by adding the
campaign_name
dimension to the
tracking_code
dimension, do not also create a grouping for the
campaign_name
dimension.
recommendation-more-help
