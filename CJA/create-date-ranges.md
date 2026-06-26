---
title: "Create date ranges"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-date-ranges/create"
category: "other"
topic: "analytics-platform/using/cja-components/cja-date-ranges"
created_at: "2026-06-02T19:08:18.950487+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create date ranges

Last update: May 13, 2026
- Topics:
- [Calendar](#)

CREATED FOR:

- User

Anyone can create a custom date range. You create a date range in the following ways:

- **A** - In the main interface, select **Components** and select **Date range**. Select **Add** from the [Date range manager](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/manage).
- **B** - In a Workspace project, from the context menu in a visualization, select **Custom date range to this date range**.
- **C** - In a Workspace project, select **Components** from the menu, and select **Create date range**
- **D** - In a Workspace project, use the shortcut **ctrl+shift+d** (Windows) or **shift+command+d** (macOS).
- **E** - In a Workspace project, from the Components left panel, select at **Date ranges**.
- **F** - In a supported visualization, like a line visualization, from the context menu on a data point, select **Annotate Selection**.

To define the annotation, you use the [Date range builder](#annotation-builder).

## Date range builder date-range-builder

The **New date range** or **Edit date range** dialog is used to create new or edit existing date ranges.

- Specify a Title for the date range. For example, Quarterly .
- Optionally, specify a Description .
- Organize the segment by creating or applying one or more Tags . Start typing to find existing tags you can select. Or press ENTER to add a new tag. Select to remove a tag. |
- Select a Date Range by selecting first the start date and then the end date. Alternatively, you can select a Preset from the Select a preset drop-down menu.
- Optionally, select Show advanced settings to: Specify Start time and End time other than the default 12:00 AM ( 0:00 ) and 11:59 PM ( 23:59 ). End times always include 59 seconds. For a date range that spans many days, the start time applies to the first day of the date range and the end time applies to the last day in your date range. Use (Reset time values) to reset start and end time to their defaults. Use rolling dates . If enabled, preset date ranges like Last 7 full days dynamically update as the current date and time progress. If disabled, such presets are not updated once applied. You can select the text in brackets (for example fixed start - rolling quarterly ) to extend the panel and specify details for Start and End . Select Start of , End of , or Fixed day . When you have selected Start of or End of , you can build a full expression. For example: End of current quarter minus 20 days . Pick the appropriate value for each individual part of the expression. Select a value for current. For example, current quarter . Select a value for additional calculation. For example, minus . When you have specified an additional calculation, specify a value. For example, 20 . When you have specified an additional calculation, select the time period to use for the calculation. For example, days . Select Hide details to hide the details for rolling dates calculation.
- Select : Save to save the date range. Save As to save a copy of the date range. Cancel to cancel any changes you made to the date range or cancel the creation of a new date range.

recommendation-more-help
