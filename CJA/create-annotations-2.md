---
title: "Create annotations"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/annotations/create-annotations"
category: "other"
topic: "analytics-platform/using/cja-components/annotations"
created_at: "2026-06-23T20:45:04.838917+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create annotations

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User
- Admin

By default, only administrators can create annotations. Users have rights to view annotations, similar to how users view other components (such as segments, calculated metrics, etc.).

However, administrators can give the **Annotation Creation** permission for **Reporting Tools** in **Edit permissions for CJA Workspace Access** to users via the Admin Console. See [User-level access control](/en/docs/analytics-platform/using/technotes/access-control#user-level-access) for more information.

You can create an annotation in the following ways:

- **A**. In the main interface, select **Components** and select **Annotations**. Select **Add** from the [Annotations manager](/en/docs/analytics-platform/using/cja-components/annotations/manage-annotations).
- **B**. In a Workspace project, from the context menu in a visualization, select **Create annotation from selection**.
- **C**. In a Workspace project, from the context menu in a line graph, select **Annotate Selection**.
- **D**. In a Workspace project, select **Components** from the menu, and select **Create annotation**.
- **E**. In a Workspace project, use the shortcut **ctrl+shift+o** (Windows) or **shift+command+o** (macOS)

To define the annotation, you use the [Annotation builder](#annotation-builder).

## Annotation builder annotation-builder

The **Annotations builder** dialog is used to create new or edit existing annotations. The dialog is titled **New annotation** or **Edit annotation** for annotations that you create or manage from the [Annotations manager](/en/docs/analytics-platform/using/cja-components/annotations/manage-annotations).

Annotation builder
{modal="regular"}
Edit annotation
{modal="regular"}
- Specify the following details ( is required): table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 layout-auto Element Description Data view You can select the data view for the annotation. The annotation you define is available as an annotation in the Workspace projects based on the selected data view. This selection is overruled when you have enabled Apply to all data views. Project-only Annotation An info box to explain that the annotation you create is only visible in the Workspace project you are working on. Enable Make this Annotation available to all your projects , to make the annotation visible to all your projects. This info box is only visible when you create an annotation from within a Workspace project. Title Name the annotation, for example, Needs further investigation . Description Provide a description for the annotation, for example, We never expected such a fluctuation in numbers. . Tags Organize the annotation by creating or applying one or more tags. Start typing to find existing tags you can select. Or press Enter to add a new tag. Select to remove a tag. Applied date Select the date or date range that needs to be present for the annotation to be visible. When you create an annotation using the shortcut, the annotation defaults to a date range for just the day. When you create an annotation using a selection in a visualization, the annotation defaults to the date range based on the date range for the panel the visualization belongs to. Color Apply a color to the annotation. The annotation appears in the project with the selected color. Color can be used to categorize annotations, such as public holidays, external events, tracking issues, etc. Scope Drag and drop metrics from the component panel that trigger the annotation. For example, People, Sessions and Events. Then drag and drop any dimensions or segments from the component panel that act as segments to determine whether to display or not to display the annotation. If you don’t specify a scope, the annotation applies to all your data. You have two options: Any of these metrics are present : Drag and drop up to 10 metrics that trigger the annotation to show. For example, the Revenue metric has stopped collecting data for a specific date range. Drag the Revenue metric into this box. With all of these segments : Drag and drop up to 10 dimensions or segments that segment whether the annotation shows. Note: Any annotation applied to a component that is then subsequently used as part of a calculated metric or segment definition does NOT automatically inherit the annotation. The desired calculated metric must also be added to the scope section to display the annotation. However, a new annotation should be created for any segment that you wish to annotate with the same information. For example, you apply an annotation to Orders on a specific day. You then use Orders in a calculated metric for the same date range. The new calculated metric does not automatically display the annotation for orders. Also add the calculated metric to the scope section for the annotation to display. Apply to all data views By default, the annotation applies to the originating data view. By checking this box, you can make the annotation apply to all data views in the company.
- Select Save to save the annotation. Save As to save a copy of the annotation. Delete to delete an annotation. Cancel to cancel any changes you made to an annotation or cancel the creation of a new annotation.

recommendation-more-help
