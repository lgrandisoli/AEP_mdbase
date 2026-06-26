---
title: "Summary number and change"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/summary-number-change"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:17.003914+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Summary number and change

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
The green and red color of the Summary Change can be controlled through [custom event polarity](https://experienceleague.adobe.com/docs/analytics/admin/admin/c-manage-report-suites/c-edit-report-suites/conversion-var-admin/c-success-events/success-event.md) or a calculated metric's [Show Upward Trend As](https://experienceleague.adobe.com/docs/analytics/components/calculated-metrics/calcmetric-workflow/cm-build-metrics.html) option.
*This article documents the Summary number and Summary change visualizations in* *Customer Journey Analytics .**See Summary number and Summary change for the* *Adobe Analytics version of this article.*

style
shade-box
See [Summary number and Summary change visualization](/en/docs/customer-journey-analytics-learn/tutorials/analysis-workspace/visualizations/use-summary-visualizations#_blank) for a demo video.

style
shade-box
## Summary number summary-number

Use the **Summary number** visualization to highlight a large number that is important in a project. This visualization behaves in the following ways, using the associated data source:

- Selects the total of the column if no cell is selected.
- If a single cell is selected, it shows the summary for that cell.
- If more than one cell is selected, it shows the first cell selected.
- If the column is selected, it picks the first cell value in the column.

As part of the visualization settings, specific Summary number options are available.

Option
Definition
Abbreviate value
Select **Abbreviate value** to abbreviate intelligently the number value. When selected, enter a number to define the amount of abbreviation. For example:

| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 html-authored no-header |  |  |
| --- | --- | --- |
| **Original value** | **Abbreviation value** | **Result** |
| $12,011,141.25 | Not selected | $12,011,141.25 |
| $12,011,141.25 | Selected, set to 0 | $12M |
| $12,011,141.25 | Selected, set to 1 | $12.0M |
| $12,011,141.25 | Selected, set to 2 | $12.01M |
| $12,011,141.25 | Selected, set to 3 | $12.011M |

Summarize value by
Choose to display the max, min, mean, median, or sum for a selection of data.
## Summary change summary-change

Use the **Summary Change** visualization to show the delta (change) between two numbers. This is applicable for AA, not CJA: The green and red color of the Summary Change can be controlled through [custom event polarity](https://experienceleague.adobe.com/docs/analytics/admin/admin-tools/success-events/success-event.html) or a calculated metric's [Show Upward Trend As](https://experienceleague.adobe.com/docs/analytics/components/calculated-metrics/calcmetric-workflow/cm-build-metrics.html) option.

This visualization behaves in the following ways:

- If no cell is selected, it compares the first two cell values in the column.
- If one cell is selected, it shows 0, because it compares the cell value to itself.
- If two cells are selected, the first selected cell is taken as numerator and the second as denominator.
- If more than two cells are selected, it only considers the first two for comparison.
- If a range of cells is selected, it compares the first to the last cells selected in the range.
- If the column is selected, it compares the first value to itself, which shows a change of 0.

As part of the visualization settings, specific **Summary change options** are available.

Option
Definition
Show percent change
Show the percent change between the 2 numbers.
Show raw difference
Show the raw difference between the 2 numbers. You can also abbreviate values and show up to 3 decimal places with this option.
Abbreviate value
Select **Abbreviate value** to abbreviate intelligently the changed value. When selected, enter a number to define the amount of abbreviation. For example:

| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 html-authored no-header |  |  |
| --- | --- | --- |
| **Original value** | **Abbreviation value** | **Result** |
| $12,011,141.25 | Not selected | $12,011,141.25 |
| $12,011,141.25 | Selected, set to 0 | $12M |
| $12,011,141.25 | Selected, set to 1 | $12.0M |
| $12,011,141.25 | Selected, set to 2 | $12.01M |
| $12,011,141.25 | Selected, set to 3 | $12.011M |

Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
