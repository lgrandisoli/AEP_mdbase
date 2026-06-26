---
title: "Basic functions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-functions"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-02T19:08:14.472155+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Basic functions

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User

The [Calculated metrics builder](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics) lets you apply statistical and mathematical functions. This article documents alphabetical list of the functions and their definitions.

NOTE
Where metric is identified as an argument in a function, other expressions of metrics are also allowed. For example,
COLUMN MAXIMUM(metrics)
also allows for
COLUMN MAXIMUM(PageViews + Sessions)
.
## Table functions versus row functions

A table function is one where the output is the same for every row of the table. A row function is one where the output is different for every row of the table.

Where applicable and relevant, a function is annotated with the type of function: [Table]{class="badge neutral"} or [Row]{class="badge neutral"}

## What does the include-zeros parameter mean?

It tells whether to include zeros in the computation. Sometimes zero means *nothing*, but sometimes it’s important.

For example, if you have a Revenue metric, and then add a Page Views metric to the report, there are suddenly more rows for your revenue, which are all zero. You probably don’t want that additional metric to affect any **MEAN**, **ROW MINIMUM**, **QUARTILE**, and more calculations that you have in the revenue column. In this case, you would check the include-zeros parameter.

An alternative scenario is that you have two metrics of interest and one has a higher average or minimum because some of the rows are zeros. In that case, you can opt not to check the parameter to include zeros

## Absolute Value absolute-value

**ABSOLUTE VALUE(metric)**

[Row]{class="badge neutral"} Returns the absolute value of a number. The absolute value of a number is the number with a positive value.

Argument
Description
metric
The metric for which you want to calculate the absolute value.
**Use case**: Ensure all results are positive when analyzing metrics that might produce negative values, such as revenue deltas or percentage changes. This helps focus on the magnitude of change without regard to direction.

**In the Calculated Metric Builder**: Wrap your metric or expression in the **Absolute Value** function, for example: **Absolute Value**(Current Revenue - Prior Revenue). This converts any negative differences to positive values.

TIP
Use this for measuring absolute differences between two time periods or segments, regardless of whether performance increased or decreased.
## Column Maximum column-maximum

**COLUMN MAXIMUM(metric, include_zeros)**

Returns the largest value in a set of dimension elements for a metric column. MAXV evaluates vertically within a single column (metric) across dimension elements.

Argument
Description
metric
Requires at least one metric but can take any number of metrics as parameters.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Identify the highest value within a breakdown, such as the day with the most visits or the product with the highest revenue. This helps highlight peak performance across categories.

**In the Calculated Metric Builder**: Apply **Column Maximum** to a metric like *Revenue* or *Sessions* when breaking down by *Day* or *Product*. The function returns the largest value in that column for each row.

TIP
Use an
IF
statement such as
IF
(
Revenue
=
Column Maximum
*(Revenue*), 1, 0) to highlight the top-performing item in your breakdown.
## Column Minimum column-minimum

**COLUMN MINIMUM(metric, include_zeros)**

Returns the smallest value in a set of dimension elements for a metric column. MINV evaluates vertically within a single column (metric) across dimension elements.

Argument
Description
metric
Requires at least one metric but can take any number of metrics as parameters.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Identify the lowest-performing value within a breakdown, such as the campaign with the fewest conversions or the day with the lowest revenue. This helps quickly surface underperforming segments.

**In the Calculated Metric Builder**: Apply **Column Minimum** to a metric like *Revenue* or *Conversion Rate* when breaking down by *Campaign* or *Day*. The function returns the smallest value in that column for each row.

TIP
Use an
IF
statement such as
IF
(
Revenue
=
Column Minimum
*(Revenue*), 1, 0) to highlight the lowest-performing item in your breakdown.
## Column Sum column-sum

**COLUMN SUM(metric)**

Adds all numeric values for a metric within a column (across the elements of a dimension).

Argument
Description
metric
Requires at least one metric but can take any number of metrics as parameters.
**Use case**: Calculate the total of all values within a breakdown, such as total revenue across all products or total visits across all days. This helps when you need an overall total to compare against individual row values.

**In the Calculated Metric Builder**: Apply **Column Sum** to a metric like *Revenue* or *Sessions* while breaking down by *Product* or *Day*. The function returns the total of all values in that column for each row.

TIP
Use when you need a reference to the overall total in order to calculate shares or percentages of total performance.
## Count count

**COUNT(metric)**

[Table]{class="badge neutral"} Returns the number, or count, of non-zero values for a metric within a column (the number of unique elements reported within a dimension).

Argument
Description
metric
The metric you want to count.
**Use case**: Count the number of data points included in a calculation, such as the number of days in a date range or the number of products in a breakdown. This helps when you need to know how many items contribute to an aggregated value.

**In the Calculated Metric Builder**: Apply **Count** to a metric like *Sessions* or *Revenue* to return the total number of rows (or data points) included in the current breakdown or date range.

TIP
Use together with
Column Sum
to calculate averages manually (for example,
Column Sum
(
Revenue
) /
Count
(Revenue)).
## Exponent exponent

**EXPONENT(metric)**

[Row]{class="badge neutral"} Returns *e* raised to the power of a given number. The constant *e* equals 2.71828182845904, the base of the natural logarithm. EXPONENT is the inverse of LN, the natural logarithm of a number.

Argument
Description
metric
The exponent applied to the base
e
.
**Use case**: Raises *e* to the power of a given number or metric. This is useful when modeling growth trends or scaling a metric exponentially.

**In the Calculated Metric Builder**: Use **Exponent** with a metric. For example: **Exponent**(*Sessions*) raises *e* to the power of the *Sessions* metric.

TIP
Combine with
Logarithm
for advanced modeling or to smooth out highly variable data when comparing growth patterns.
## Mean mean

**MEAN(metric, include_zeros)**

[Table]{class="badge neutral"} Returns the arithmetic mean, or average, for a metric in a column.

Argument
Description
metric
The metric for which you want to calculate the average.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Calculate the arithmetic average of a set of values, such as the average daily revenue or the average number of visits per campaign. This helps establish a baseline for comparing individual values within a dataset.

**In the Calculated Metric Builder**: Apply **Mean** to a metric like *Revenue* or *Sessions* to return the average value across all data points in the selected breakdown or date range.

TIP
Use to understand overall performance trends, or combine it with
Standard Deviation
to measure consistency around the average.
## Median median

**MEDIAN(metric, include_zeros)**

[Table]{class="badge neutral"} Returns the median for a metric in a column. The median is the number in the middle of a set of numbers. That is, half the numbers have values that are greater than or equal to the median, and half are less than or equal to the median.

Argument
Description
metric
The metric for which you want to calculate the median.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Identify the middle value in a set of data, such as the median daily revenue or median page views per visit. This is helpful when you want to reduce the impact of outliers and see the central tendency of your data.

**In the Calculated Metric Builder**: Apply Median to a metric like Revenue or Page Views to return the midpoint value across all data points in the selected breakdown or date range.

TIP
Use instead of
Mean
when your data contains extreme highs or lows that might skew the average.
## Modulo modulo

**MODULO(metric_X, metric_Y)**

Returns the remainder after dividing x by y using Euclidean division.

Argument
Description
metric_X
The first metric that you would like to divide.
metric_Y
The second metric that you would like to divide.
**Use case**: Return the remainder after dividing one number by another. This can be useful for cyclical or repeating patterns, such as identifying every nth day or campaign in a sequence.

**In the Calculated Metric Builder**: Use **Modulo** with two numeric inputs. For example: **Modulo**(*Day Number*, 7) returns the remainder after dividing the day number by seven, which can help group data by week.

TIP
Combine with conditional logic to highlight recurring intervals or to segment data based on repeating cycles.
### More Examples

The return value has the same sign as the input (or is zero).

```
MODULO(4,3) = 1
MODULO(-4,3) = -1
MODULO(-3,3) = 0
```

To ensure you always get a positive number, use

```
MODULO(MODULO(x,y)+y,y)
```

## Percentile percentile

**PERCENTILE(metric, k, include_zeros)**

[Table]{class="badge neutral"} Returns the nth percentile, which is a value between 0 and 100. When n < 0, the function uses zero. When n > 100, the function returns 100.

Argument
Description
metric
The percentile value in the range 0 to 100, inclusive.
k
The metric column that defines relative standing.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Identify the value below which a given percentage of data points fall, such as the 90th percentile of daily revenue or page views. This helps measure distribution and detect high-performing outliers.

**In the Calculated Metric Builder**: Apply **Percentile** to a metric like *Revenue* or *Sessions*, and specify the desired percentile value (for example, **Percentile**(*Revenue*, 90)). The result shows the threshold that 90% of data points fall below.

TIP
Use to set performance benchmarks or to filter for top-performing days, campaigns, or products.
## Power Operator power-operator

**POWER OPERATOR(metric_X, metrix_Y)**

Returns x raised to the y power.

Argument
Description
metric_X
The metric that you would like to raise to the metric_Y power.
metric_Y
The power you would like to raise metric_X to.
**Use case**: Raise one number or metric to the power of another, such as squaring a value or applying an exponential weight. This is helpful when modeling growth, scaling values, or performing advanced mathematical transformations.

**In the Calculated Metric Builder**: Use **Power Operator** between two numeric values or metrics. For example: *Revenue* ^ 2 raises the *Revenue* value to the second power.

TIP
Similar to the
Exponent
function but expressed as a mathematical operator, allowing for more compact formulas within calculated metrics.
## Quartile quartile

**QUARTILE(metric, quartile, include_zeros)**

[Table]{class="badge neutral"} Returns the quartile of values for a metric. For example, quartiles can be used to find the top 25% of products driving the most revenue. [COLUMN MINIMUM](#column-minimum), [MEDIAN](#median), and [COLUMN MAXIMUM](#column-maximum) return the same value as [QUARTILE](#quartile) when quartile is equal to 0 (zero), 2, and 4, respectively.

Argument
Description
metric
The metric for which you want to calculate the quartile value.
quartile
Indicates which quartile value to return.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Divide a dataset into four equal parts to understand how values are distributed, such as identifying the top 25% of days by revenue or visits. This helps segment performance into ranked groups for deeper comparison.

**In the Calculated Metric Builder**: Apply **Quartile** to a metric like *Revenue* or *Sessions*, and specify which quartile to return (for example, **Quartile**(*Revenue*, 3) to find the threshold for the third quartile, or top 25%).

TIP
Use to group values into performance tiers such as low-, mid-, and high-performing campaigns or products.
## Round round

**ROUND(metric, number)**

Round without a *number* parameter is the same as round with a *number* parameter of 0, namely round to the nearest integer. With a *number* parameter, ROUND returns the *number* digits to the right of the decimal. If *number* is negative, it returns 0’s to the left of the decimal.

Argument
Description
metric
The metric that you want to round.
number
How many digits to the right of the decimal to return. (If negative returns zeros to the left of the decimal).
**Use case**: Simplify numeric results by rounding them to a specified number of decimal places. This is helpful for creating cleaner visualizations or making calculated metrics easier to read in reports.

**In the Calculated Metric Builder**: Apply **Round** to a metric or expression and specify the number of decimal places. For example: **Round**(*Conversion Rate*, 2) rounds the value to two decimal places.

TIP
Use to standardize metric formatting across reports, especially when displaying percentages or currency values.
### More Examples

```
ROUND( 314.15, 0) = 314
ROUND( 314.15, 1) = 314.1
ROUND( 314.15, -1) = 310
ROUND( 314.15, -2) = 300
```

## Row Count row-count

**ROW COUNT()**

Returns the count of rows for a given column (the number of unique elements reported within a dimension). *Uniques exceeded* is counted as 1.

**Use case**: Count the total number of rows returned in a breakdown or dataset, such as the number of days, campaigns, or products included in a report. This helps understand how many items contribute to your analysis.

**In the Calculated Metric Builder**: Apply **Row Count** to return the total number of rows in the current breakdown or segment. For example, when viewing *Revenue* by *Product*, **Row Count** returns the number of products shown.

TIP
Use with other functions like
Column Sum
to calculate averages manually (for example,
Column Sum
(
Revenue
) /
Row Count
()).
## Row Max row-max

**ROW MAX(metric, include_zeros)**

Maximum of the columns of each row.

Argument
Description
metric
Requires at least one metric but can take any number of metrics as parameters.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Identify the highest value across all metrics in a single row, such as determining which metric (for example, *Revenue*, *Orders*, or *Sessions*) has the greatest value for a specific day or segment. This helps highlight which metric leads within each row of data.

**In the Calculated Metric Builder**: Apply **Row Maximum** when multiple metrics are included in a calculated metric. For example: **Row Maximum**(*Revenue*, *Orders*, *Sessions*) returns the largest value among those metrics for each row.

TIP
Use to compare related metrics side by side and identify which contributes the most to performance within each row.
## Row Min row-min

**ROW MIN(metric, include_zeros)**

Minimum of the columns of each row.

Argument
Description
metric
Requires at least one metric but can take any number of metrics as parameters.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Identify the lowest value across all metrics in a single row, such as finding which metric (for example, *Revenue*, *Orders*, or *Sessions*) has the smallest value for a particular day or segment. This helps spot the weakest-performing metric within each row of data.

**In the Calculated Metric Builder**: Apply **Row Minimum** when comparing multiple metrics. For example: **Row Minimum**(*Revenue*, *Orders*, *Sessions*) returns the smallest value among those metrics for each row.

TIP
Combine with Row Maximum to calculate performance ranges or to highlight underperforming metrics in a side-by-side comparison.
## Row Sum row-sum

**ROW SUM(metric, include_zeros)**

Sum of the columns of each row.

Argument
Description
metric
Requires at least one metric but can take any number of metrics as parameters.
**Use case**: Add together the values of multiple metrics within a single row, such as summing *Revenue* and *Tax* to calculate total transaction value, or combining *Sessions* from different sources. This helps consolidate related metrics into one total.

**In the Calculated Metric Builder**: Apply **Row Sum** to combine multiple metrics. For example: **Row Sum**(*Revenue*, *Tax*) adds those two metrics for each row in your breakdown.

TIP
Use to create combined totals or to group related performance indicators into a single calculated metric.
## Square Root square-root

**SQUARE ROOT(metric, include_zeros)**

[Row]{class="badge neutral"} Returns the positive square root of a number. The square root of a number is the value of that number raised to the power of 1/2.

Argument
Description
metric
The metric for which you want to calculate the square root.
**Use case**: Return the square root of a number or metric, such as finding the root of variance when calculating standard deviation or normalizing values in a dataset. This is useful for advanced statistical or data transformation calculations.

**In the Calculated Metric Builder**: Apply **Square Root** to a metric or expression. For example: **Square Root**(Variance(*Revenue*)) returns the standard deviation of *Revenue*.

TIP
Use when you need to scale metrics proportionally or to support other statistical functions that rely on root values.
## Standard Deviation standard-deviation

**STANDARD DEVIATION(metric, include_zeros)**

[Table]{class="badge neutral"} Returns the standard deviation, or square root of the variance, based on a sample population of data.

Argument
Description
The metric for which you want to calculate the standard deviation.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Measure how much values vary from the average, such as evaluating how consistent daily revenue or visits are over time. This helps identify volatility, stability, or unusual fluctuations in performance.

**In the Calculated Metric Builder**: Apply **Standard Deviation** to a metric like *Revenue* or *Sessions* to calculate the spread of values within the selected breakdown or date range. For example: **Standard Deviation**(*Revenue*) shows how much daily revenue deviates from the mean.

TIP
Use with
Mean
to detect anomalies or compare the consistency of performance across campaigns, products, or segments.
## Variance variance

**VARIANCE(metric, include_zeros)**

[Table]{class="badge neutral"} Returns the variance based on a sample population of data.

Argument
Description
metric
The metric for which you want to calculate the variance.
include_zeros
Whether or not to include zero values in the calculations.
**Use case**: Measure how far values in a dataset spread out from the mean, such as analyzing how much daily revenue or session duration varies over time. This helps quantify the degree of consistency or fluctuation in performance.

**In the Calculated Metric Builder**: Apply **Variance** to a metric like *Revenue* or *Time Spent per Visit* to calculate the average squared deviation from the mean. For example: **Variance**(*Revenue*) shows how much revenue values differ from the average over the selected range.

TIP
Use with
Standard Deviation
to better understand data variability and identify areas of unpredictable performance.
The equation for VARIANCE is:

{width="100"}

Where *x* is the sample mean, [MEAN( metric )](#mean), and *n* is the sample size.

To calculate a variance, you look at an entire column of numbers. From that list of numbers you first calculate the average. Once you have the average, you go through each entry and do the following:

- Subtract the average from the number.
- Square the result.
- Add that to the total.

Once you have iterated over the entire column, you have a single total. You then divide that total by the number of items in the column. That number is the variance for the column. It is a single number. It is, however, displayed as a column of numbers.

In the example of the following three-item column:

column
1
2
3
The average of this column is 2. The variance for the column is ((1 - 2)2 + (2 - 2)2 + (3 - 2)2/3) = 2/3.

recommendation-more-help
