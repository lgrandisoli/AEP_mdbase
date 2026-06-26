---
title: "Shared component editor"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/shared-metrics-dimensions/shared-component-editor"
category: "other"
topic: "analytics-platform/using/cja-dataviews/shared-metrics-dimensions"
created_at: "2026-06-23T20:45:30.510404+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Shared component editor

Last update: May 13, 2026
CREATED FOR:

- User
- Admin

The shared component editor allows you to create or edit shared dimensions and metrics. It shares many UI elements when [creating or editing a data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview), but these interfaces are distinct in purpose:

- The data view component editor allows you to create and edit components specific to that data view. You cannot edit shared dimensions or metrics in the data view component editor. In this interface, shared dimensions and metrics can be identified by a icon next to the component name.
- The shared component editor allows you to create and edit shared dimensions and metrics. You cannot edit components that belong to a single data view in the shared component editor.

The top right includes three buttons:

- **Close** or **Cancel**: If all changes are saved, the **Close** button closes the editor. If there are any unsaved changes, the **Cancel** button closes the editor without saving those changes.
- **Save**: Saves all components and keeps the editor open.
- **Save and finish**: Saves all components and closes the editor.

The interface includes three main columns/sections:

- Schema field selector : Locate the desired schema field(s) and drag them to the included components area. Connection : The active connection. Change the active connection in the shared metrics & dimensions manager . Component list : You can choose between selecting Schema fields (net new shared dimensions and metrics), or Metrics & Dimensions (existing shared components) from the drop-down menu. Search : Use the text search to locate the desired schema field or shared component by name. You can also use filters to narrow down the list of components. The Is not deprecated filter is active by default. Create derived field : Allows you to create a derived field .
- Included components : The components that you configure to be shared. When creating shared components, you can drag more than one schema field to this area to create multiple components simultaneously. When editing shared components, you can select multiple components to edit, which lists all selected components in this area.
- Component settings : When selecting a component in the included components area, all available settings can be configured in this column. See Component settings for all available options for dimensions and metrics. Shift + clicking multiple elements in the included components area allows you to edit any common fields simultaneously.

recommendation-more-help
