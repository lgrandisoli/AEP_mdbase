---
title: "Components overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/overview"
category: "overview"
topic: "analytics-platform/using/cja-components/overview"
created_at: "2026-06-23T20:43:05.402271+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Components overview

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

Components are features in Customer Journey Analytics that can be used in visualizations (like Freeform table), or to complement reporting features.

To manage components from the main Customer Journey Analytics interface:

- Select **Components** from the top bar.
- Select **Components** to see an overview of the components you can manage, or directly select the component you want to manage from the menu.

You can manage the following components:

- [Segments](/en/docs/analytics-platform/using/cja-components/segments/seg-overview): Build, manage, share, and apply powerful, focused audience segments to your reports. Segments let you identify subsets of persons based on characteristics or interactions.
- [Calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/calc-metr-overview): Use metrics and formulas as new components for use in reporting
- [Date ranges](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/create): Customize and refine the date ranges Analysis Workspace offers.
- [Annotations](/en/docs/analytics-platform/using/cja-components/annotations/overview): Communicate contextual data nuances and insights to your organization.
- [Intelligent alerts](/en/docs/analytics-platform/using/cja-components/alerts/intelligent-alerts): Allow you to be notified based on changed percentages or specific data points.
- [Scheduled projects](/en/docs/analytics-platform/using/cja-workspace/export/t-schedule-report#scheduled-projects-manager): Manage your scheduled projects.
- [Preferences](/en/docs/analytics-platform/using/cja-workspace/user-preferences): Manage the preferences for Analysis Workspace.
- [Audiences](/en/docs/analytics-platform/using/cja-components/audiences/audiences-overview): Create and publish audiences from Customer Journey Analytics to [Real-Time Customer Data Platform](/en/docs/experience-platform/profile/home) in Experience Platform for targeting and personalization.
- [Exports](/en/docs/analytics-platform/using/cja-components/exports/manage-export-locations): Manage your export account and locations.

## Analysis Workspace components

Components in Analysis Workspace consist of metrics, dimensions, segments, and date ranges that you can drag-and-drop onto panels and visualizations in your Workspace project. Custom components that you create are added to these panels, such as a calculated metric, or a custom date range.

To access the Components panel, select **Components** in the button panel.

See [Create a project](/en/docs/analytics-platform/using/cja-workspace/home) for information on how to use components in a project.

## Manage components actions

You can quickly create a new component using the **Components** menu in Analysis Workspace. See the [Analysis Workspace menu](/en/docs/analytics-platform/using/cja-workspace/home#menu) for more details.

You can manage components (individually or by selecting more than one).

- Select one or more components.
- From the context menu, or from the Component actions button (at the top of Components), select one of the following actions. note tip TIP You can select multiple components by holding Shift , or by holding Command (on macOS) or Ctrl (on Windows). {width="100%"} table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Component action Description Tag Organize or manage components by applying tags to them. You can then search by tag in the left panel by selecting the filter or typing # . Tags also act as filters in the component managers. Favorite Add the component to your list of favorites. Like tags, you can search by Favorites in the left panel and filter by them in the component managers. Un-favorite Remove the component from your list of favorites. Approve Mark components as Approved to signal to your users that the component is organization-approved. Like tags, you can search and filter by Approved in the left panel. A identifies approved components. Share Share components to users in your organization. This option is available for custom components only, such as segments or calculated metrics. Delete Delete components that you no longer need. This option is available for custom components only, such as segments or calculated metrics.

Custom components can also be managed through their respective Component managers. For example, see [Manage segments](/en/docs/analytics-platform/using/cja-components/segments/seg-manage).

## Manage the component list

You can search, filter, and sort the component list in the left panel of Analysis Workspace to locate a particular component.

### Search

- Select Components in the left panel.
- In the search field, begin typing the name of the component you want to use in your project. A color and icon identify the type of component. Dimensions are orange, Segments are blue, Date ranges are purple, and Metrics are green. The Adobe icon indicates either a calculated metric template or a segment template. The calculator icon indicates a calculated metric that an administrator in your organization has created.
- Select the component from the drop-down menu.

### Filter

- Select the Components icon in the left panel.
- Select Filter , or enter # in the search field.
- Select any of the following filter options to filter the list of components: table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 Icon Filter option Description Approved Show only components that are marked as Approved by an administrator. Favorites Show only components that are in your list of Favorites. For information about adding components to your list of favorites, see Manage components . Dimensions Show only components that are Dimensions. Metrics Show only components that are Metrics. Segments Show only components that are segments. Date ranges Show only components that are Date ranges. Tag name Show only components with the specific selected tags. A dedicated tag is available for Adobe Template which are the default calculated metrics from Adobe. Select in a filter to remove the filter.
- You can optionally sort the component list, as described in Sort the component list .

### Sort

- (Optional) Apply any filters to the component list, as described in Filter the component list .
- Select Components in the left panel.
- Select Sort , then select any of the following filter options to sort the list of components.

The following sort options are available:

Option
Function
Recommended
Sort components for each type (dimension, metric, segment and date range) based on their recommendation. Components that are used most frequently and most recently by you or by others in your organization are shown higher in each list.
Last modified
Sort components for each type (dimension, metric, segment and date range) based on their last modified date. Components that are modified most recently are shown highter in each list.
Alphabetical
Sort components for each type (dimension, metric, segment and date range) in ascending alphabetic order.
Categorical
Sort components for each type (dimension, metric, segment and date range) based on their category. For example Curated versus Non-curated data view components.
## Access permissions

In Analysis Workspace, administrators can [curate](/en/docs/analytics-platform/using/cja-workspace/curate-share/curate) which components are exposed to users in reporting.

recommendation-more-help
