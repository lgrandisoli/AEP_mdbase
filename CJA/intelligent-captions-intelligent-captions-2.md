---
title: "Intelligent captions intelligent-captions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/intelligent-captions?lang=en"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:07:34.700778+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Intelligent captions intelligent-captions

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

The Intelligent captions functionality uses advanced Generative AI to provide key insights for the most frequently used Workspace visualizations in natural language.

Intelligent captions are geared towards:

- Analysts, who need narratives to share with other users. Analysts need these insights to be able to provide context to their users.
- Business users, who want to discover high-level takeaways quickly.

Here is an example of what intelligent captions could look like:
                
                ![Intelligent captions for Line visualization including Seasonality, Min, Max, Spike, and Decline.](assets/captions.png)
See [Intelligent captions](/en/docs/customer-journey-analytics-learn/tutorials/analysis-workspace/visualizations/intelligent-captions#_blank) for a demo video.

style
shade-box
## Launch intelligent captions launch

To launch auto-generated intelligent captions for a visualization, select at the top right of the visualization. This selection generates natural-language insights.

Keep in mind that:

- You need a minimum of 3 data points to generate captions successfully. Otherwise, you might get an error like Not enough data to analyze .
- Captions are generated every time the underlying selected data changes in the table that powers the visualization.
- If there are multiple metrics in an associated freeform table, captions are only generated for the first metric or the metric currently selected by the user. However, captions can be generated for multiple metrics for the line and area visualizations.
- If you save the project at a specific point, and re-load it later, the captions are auto-updated with new data. The same applies to scheduled projects and PDF files exported from a project.

## Visualizations visualizations

Intelligent captions are supported on the following visualizations:

- [Line](/en/docs/analytics-platform/using/cja-workspace/visualizations/line) (including multi-line)
- [Bar](/en/docs/analytics-platform/using/cja-workspace/visualizations/bar)
- [Horizontal bar](/en/docs/analytics-platform/using/cja-workspace/visualizations/horizontal-bar)
- [Area](/en/docs/analytics-platform/using/cja-workspace/visualizations/area) (including multiple Area lines)
- [Donut](/en/docs/analytics-platform/using/cja-workspace/visualizations/donut)
- [Fallout](/en/docs/analytics-platform/using/cja-workspace/visualizations/fallout/fallout-flow)
- [Flow](/en/docs/analytics-platform/using/cja-workspace/visualizations/flow/flow)

## Actions

You can perform the following actions on intelligent captions:

### Copy to clipboard copy

You can copy the captions to a clipboard and paste them into a PowerPoint or other tools. You can copy individual captions in the one-by-one view, or you can copy all captions at once in the expanded caption view.

- To copy the captions, select at the top right of the captions dialog.

### Show all or individual intelligent captions show-all-or-individual

You can show all intelligent captions at once in an expanded view, or you can show individual inteliigent captions in a one-by-one view.

- To show all intelligent captions, select .
- To show individual intelligent captions, one-by-one, select .

### Edit display edit

You can edit the display of captions, such as hiding or unhiding a particular category of insights.

- Select in the Intelligent captions dialog.
- Toggle between to display a specific insight (like Min ), or to hide a specific insight (like Spike ).
- Select Apply .

### Provide feedback

You can provide feedback on the generated intelligent captions (feedback can only be provided in the expanded caption view).

- Select in the Intelligent captions dialog.
- Select Good response , Bad response , or Report .
- In the Thank you for your feedback dialog, provide your feedback and select Submit to submit the feedback.

### Export export

You can export intelligent captions as part of a PDF, as long as the project is saved with the intelligent captions generated.

### Toggle off toggle

If you would rather not show intelligent captions, you can toggle the feature off.

- Go to Visualizations preferences .
- Uncheck Show intelligent captions .
- Select Save to save the preference.

## Intelligent captions in Mobile Scorecards

Intelligent captions are also available in Customer Journey Analytics [mobile scorecards](/en/docs/analytics-platform/using/cja-dashboards/manage-scorecard#captions).

## Feature Access

The following parameters govern access to Intelligent captions:

- Solution access : The Intelligent captions feature is available in Customer Journey Analytics, but not in Adobe Analytics.
- Contractual access : If you are not able to use Intelligent captions, please contact your organization’s administrator or Adobe Account Representative (Admin). Before you can use Intelligent captions in your organization, you must agree to certain Generative AI related legal terms.
- Permissions : In the Adobe Admin Console, the Reporting Tools Intelligent Captions permission determines access. A product profile admin needs to follow these steps in the Admin Console: Navigate to Admin Console > Products and services > Customer Journey Analytics > Product Profiles . Select the title of the product profile for which you want to provide access to Intelligent captions. In the specific product profile, select Permissions . Select to edit Reporting Tools . Select to add Intelligent Captions to Included permission items . Select Save to save the permissions.

See [Access control](/en/docs/analytics-platform/using/technotes/access-control#access-control) for more information.

recommendation-more-help
