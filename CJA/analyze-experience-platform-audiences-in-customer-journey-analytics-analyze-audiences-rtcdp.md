---
title: "Analyze Experience Platform audiences in Customer Journey Analytics analyze-audiences-RTCDP"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/audience-analysis/analyze-audiences"
category: "other"
topic: "analytics-platform/using/cja-connections/audience-analysis"
created_at: "2026-06-02T19:04:27.526225+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Analyze Experience Platform audiences in Customer Journey Analytics analyze-audiences-RTCDP

Last update: May 13, 2026
- Topics:
- [Audiences](#)

CREATED FOR:

- Admin

After you [create an audience analysis configuration](/en/docs/analytics-platform/using/cja-connections/audience-analysis/audience-analysis-configure), audience data becomes available as new dimensions in the data views where you configure them to be created. You can use the new audience dimensions anywhere in Analysis Workspace if you have access to a data view where the audience analysis dimensions were added.

## Use the Audience overview template

An Audience overview template is available in Customer Journey Analytics.

For information about how to access the Audience overview template, see [Access and run a template](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#access-and-run-a-template) in [Use templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates).

The Audience overview template contains the following panels:

## Usage overview panel

Shows data for all audiences with usage events that are associated with the selected data view. Audience membership data is updated daily from Experience Platform. Data is always shown for yesterday, so changing the panel date range results in inaccurate data.

Use the table in this panel to better understand audience behavior. Drag the Audience Description dimension from the selected data view and add it as a breakdown. Or use any other interaction dimension (such as Page, Action, and so forth) as the breakdown.

## Top audience origins panel

Shows where the audience was created, whether in RTCDP, Customer Journey Analytics, and so forth.

Use the table in this panel to better understand how the audience origin might affect other factors. Drag the Audience Name dimension from the selected data view and add it as a breakdown. Or use any other interaction dimension (such as Page, Action, and so forth) as the breakdown.

## Audience overlap panel

Shows data for all audiences with usage events that are associated with the selected data view. Data is always shown for yesterday, so changing the panel date range results in inaccurate data.

Select up to three audiences in the table in this panel to see how they overlap in the corresponding Venn diagram.

## Exited audience usage panel

Shows data for all exited audiences with usage events that are associated with the selected data view. Data is always shown for yesterday, so changing the panel date range results in inaccurate data. “Exited audiences” are audiences in which people with usage events left or exited yesterday.

Use the table in this panel to better understand audience behavior. Drag the Exited Audience Description dimension from the selected data view and add it as a breakdown. Or use any other interaction dimension or metric (such as Page, Action, and so forth) as the breakdown.

## Top exited audience origins panel

Shows where each audience that exited was originally created, whether in RTCDP, Customer Journey Analytics, and so forth.

Use the table in this panel to better understand how the audience origin might affect other factors. Drag the Exited Audience Name dimension from the selected data view and add it as a breakdown. Or use any other interaction dimension or metric (such as Page, Action, and so forth) as the breakdown.

recommendation-more-help
