---
title: "Line line"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/line"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:06:06.349607+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Line line

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

markdownlint-disable MD034
markdownlint-enable MD034
*This article documents the Line visualization in* *Customer Journey Analytics .**See Line for the* *Adobe Analytics version of this article.*

style
shade-box
The **Line** visualization represents metrics using a line to show how values change over a period of time. A line visualization can be used only when time is used as a dimension.

## Settings

As part of the [visualization settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-analysis-visualizations#settings), specific line visualization settings are available.

Setting
Description
Granularity
Select from the granularity drop-down to change a trended visualization from daily to weekly to monthly, etc. The granularity is also updated in the data source table.
Show min
Show max
You can overlay a min and max value label to highlight the minimum and maximum values in a metric. The min/max values are derived from the visible data points in the visualization, not the full set of values within a dimension.
Show trendline
You can choose to add a regression or moving average trendline to your line series. Trendlines help to depict a clearer pattern in the data. When selected, select a model from the list. See [Models](#models) for an overview and description of available models. .

**TIP:** It is recommended that trendlines be applied to data that does not include today (partial data) or future dates. Today or future dates skew the trendline. If you need to include future dates, however, remove zeroes from the data to prevent skewing for those days. Go to the visualization’s data source table, choose your metric column, then enable **Column Settings** > **Interpret zero as no value**.

### Models

All regression model trendlines are fit using ordinary least squares:

Model
Description
Linear
Create a best-fit straight line for simple linear datasets and is useful when the data increases or decreases at a steady rate. Equation:
y = a + b * x
Logarithmic
Create a best-fit curved line and is useful when the rate of change in the data increases or decreases quickly and then levels out. A logarithmic trendline can use negative and positive values. Equation:
y = a + b * log(x)
Exponential
Create a curved line and is useful when data rises or falls at constantly increasing rates. This option should not be used if your data contains zero or negative values. Equation:
y = a + e^(b * x)
Power
Create a curved line and is useful for datasets that compare measurements that increase at a specific rate. This option should not be used if your data contains zero or negative values. Equation:
y = a * x^b
Quadratic
Finds the best-fit for a dataset shaped like a parabola (concave up or down). Equation:
y = a + b * x + c * x^2
Moving average
Create a smooth trendline based on a set of averages. Also known as a rolling average, a moving average uses a specific number of data points (determined by your Granularity selection), averages them, and uses the average as a point in the line. Examples include a seven day moving average or a four week moving average.
See [Line](/en/docs/customer-journey-analytics-learn/tutorials/analysis-workspace/visualizations/line-visualization#_blank) for a demo video.

style
shade-box
Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
