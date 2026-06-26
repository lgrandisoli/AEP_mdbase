---
title: "View anomalies"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/anomaly-detection/view-anomalies"
category: "other"
topic: "analytics-platform/using/cja-workspace/anomaly-detection"
created_at: "2026-06-02T19:08:07.737632+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# View anomalies

Last update: May 13, 2026
- Topics:
- [Anomaly Detection](#)

CREATED FOR:

- User

You can view anomalies in Analysis Workspace in a table or in a line chart.

## View anomalies in a table section_869A87B92B574A38B017A980ED8A29C5

You can view anomalies in a time-series Freeform Table.

- Select the in the column header, then ensure that the Show anomalies option is selected in the list of options. For more information, see Column settings .
- Anomalies are shown in the table as follows: A ◥ appears in the upper-right corner of each row where a data anomaly is detected. The colored vertical line in each row ➋ indicates the expected value. The colored shaded area in each row ➊ indicates the actual value. How the line (expected value) compares with the shaded area (actual value) determines whether there is an anomaly. (An observation is considered anomalous based on the advanced statistical techniques described in Statistical techniques used in anomaly detection .)
- Select ◥ in the upper-right corner of a row to view details about the anomaly. This shows the extent (as a percentage) to which the actual value diverges either above or below the expected value.

## View anomalies in a line chart

Line charts are the only visualization that allows you to view anomalies.

To view anomalies in a line chart:

- Select in the visualization header, then ensure that the Show anomalies option is selected in the list of options. For more information, see Line .
- (Optional) To allow the confidence interval to scale the chart, select in the visualization header, then select the option, Allow anomalies to Scale Y-axis . This option is not selected by default because it can sometimes make the chart less legible. Anomalies are shown in the line chart as follows: A white dot appears on the line wherever a data anomaly is detected. (An observation is considered anomalous based on the advanced statistical techniques described in Statistical techniques used in anomaly detection .) The light shaded area is the confidence band, or expected range, where values should occur. Any value that falls outside of this expected range is an anomaly. If you have multiple metrics in the line chart, only the anomalies are shown and you have to hover over each anomaly to see the confidence band for that metric. The dotted line is the exact expected value.
- Select an anomaly (white dot) to view the following information: The date the anomaly occurred. The raw value of the anomaly. The percentage value above or below the expected value, which is represented by the solid green line.

recommendation-more-help
