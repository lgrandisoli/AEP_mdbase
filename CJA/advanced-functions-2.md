---
title: "Advanced functions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-adv-functions"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-23T20:45:14.713788+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Advanced functions

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User

The [Calculated metrics builder](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/cm-build-metrics) lets you apply statistical and mathematical functions. This article documents alphabetical list of the advanced functions and their definitions.

Access these functions by selecting **Show all** below **Functions** list in the Components panel. Scroll down to see the list of **Advanced functions**.

## Table functions versus row functions

A table function is one where the output is the same for every row of the table. A row function is one where the output is different for every row of the table.

Where applicable and relevant, a function is annotated with the type of function: [Table]{class="badge neutral"} or [Row]{class="badge neutral"}

## What does the include-zeros parameter mean?

It tells whether to include zeros in the computation. Sometimes zero means *nothing*, but sometimes it’s important.

For example, if you have a Revenue metric, and then add a Page Views metric to the report, there are suddenly more rows for your revenue, which are all zero. You probably don’t want that additional metric to affect any **MEAN**, **ROW MINIMUM**, **QUARTILE**, and more calculations that you have in the revenue column. In this case, you would check the include-zeros parameter.

An alternative scenario is that you have two metrics of interest and one has a higher average or minimum because some of the rows are zeros. In that case, you can opt not to check the parameter to include zeros.

## And and

**AND(logical_test)**

Conjunction. Not equal to zero is considered to be true and equals zero is considered to be false. The output is either a 0 (false) or 1 (true).

Argument
Description
logical_test
Requires at least one parameter, but can take any number of parameters. Any value or expression that can be evaluated to TRUE or FALSE
## Approximate Count Distinct approximate_count_distinct

**APPROXIMATE COUNT DISTINCT(dimension)**

Returns the approximated distinct count of dimension items for the selected dimension.

Argument
Description
dimension
The dimension for which you want to calculate the approximated distinct item count
### Example

A common use case for this function is when you want to get an approximate number of customers.

## Arc Cosine arc-cosine

**ARC COSINE(metric)**

[Row]{class="badge neutral"} Returns the arccosine, or inverse of the cosine, of a metric. The arccosine is the angle whose cosine is number. The returned angle is given in radians in the range 0 (zero) to pi. If you want to convert the result from radians to degrees, multiply it by 180/PI().

Argument
Description
metric
The cosine of the angle you want from -1 to 1
## Arc Sine arc-sine

**ARC SINE(metric)**

[Row]{class="badge neutral"} Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is a number. The returned angle is given in radians in the range -pi/2 to pi/2. To express the arcsine in degrees, multiply the result by 180/PI().

Argument
Description
metric
The sine of the angle you want from -1 to 1
## Arc Tangent arc-tangent

**ARC TANGENT(metric)**

[Row]{class="badge neutral"} Returns the arctangent, or inverse tangent, of a number. The arctangent is the angle whose tangent is a number. The returned angle is given in radians in the range -pi/2 to pi/2. To express the arctangent in degrees, multiply the result by 180/PI().

Argument
Description
metric
The tangent of the angle you want from -1 to 1
## Cdf-T cdf-t

**CDF-T(metric, number)**

Returns the probability that a random variable with student-t distribution with n degrees of freedom have a z-score less than col.

Argument
Description
metric
The metric for which you would like the Cumulative Distribution Function of the student t-distribution
number
The degrees of freedom for the Cumulative Distribution Function of the student t-distribution
### Example

```
CDF-T(-∞, n) = 0
CDF-T(∞, n) = 1
CDF-T(3, 5) ? 0.99865
CDF-T(-2, 7) ? 0.0227501
CDF-T(x, ∞) ? cdf_z(x)
```

## Cdf-Z cdf-z

**CDF-Z(metric, number)**

Returns the probability that a random variable with a normal distribution has a z-score less than col.

Argument
Description
metric
The metric for which you would like the Cumulative Distribution Function of the Standard Normal Distribution
### Examples

```
CDF-Z(-∞) = 0
CDF-Z(∞) = 1
CDF-Z(0) = 0.5
CDF-Z(2) ? 0.97725
CDF-Z(-3) ? 0.0013499
```

## Ceiling ceiling

**CEILING(metric)**

[Row]{class="badge neutral"} Returns the smallest integer not less than a given value. For example, if you want to avoid reporting currency decimals for revenue and a product has $569.34, use the formula CEILING(Revenue) to round revenue up to the nearest dollar, or $570.

Argument
Description
metric
The metric that you want to round
## Confidence confidence

**CONFIDENCE(normalizing-container, success-metric, control, significance-treshold)**

Calculate the any-time-valid confidence using the WASKR method as described in [Time-uniform central limit theory and asymptotic confidence sequences](https://arxiv.org/pdf/2103.06476).

Confidence is a probabilistic measure of how much evidence there is that a given variant is the same as the control variant. A higher confidence indicates less evidence for the assumption that control and non-control variant have equal performance.

Argument
Description
normalizing-container
The basis (People, Sessions, or Events) on which a test is run.
success-metric
The metric or metrics that a user is comparing variants with.
control
The variant that all other variants in the experiment are being compared with. Enter the name of the control variant dimension item.
significance-threshold
The threshold in this function is set to a default of 95%.
## Confidence (Lower) confidence-lower

**CONFIDENCE(normalizing-container, success-metric, control, significance-treshold)**

Calculate the any-time-valid confidence **lower** using the WASKR method as described in [Time-uniform central limit theory and asymptotic confidence sequences](https://arxiv.org/pdf/2103.06476).

Confidence is a probabilistic measure of how much evidence there is that a given variant is the same as the control variant. A higher confidence indicates less evidence for the assumption that control and non-control variant have equal performance.

Argument
Description
normalizing-container
The basis (People, Sessions, or Events) on which a test is run.
success-metric
The metric or metrics that a user is comparing variants with.
control
The variant that all other variants in the experiment are being compared with. Enter the name of the control variant dimension item.
significance-threshold
The threshold in this function is set to a default of 95%.
## Confidence (Upper) confidence-upper

**CONFIDENCE(normalizing-container, success-metric, control, significance-treshold)**

Calculate the any-time-valid confidence **upper** using the WASKR method as described in [Time-uniform central limit theory and asymptotic confidence sequences](https://arxiv.org/pdf/2103.06476).

Confidence is a probabilistic measure of how much evidence there is that a given variant is the same as the control variant. A higher confidence indicates less evidence for the assumption that control and non-control variant have equal performance.

Argument
Description
normalizing-container
The basis (People, Sessions, or Events) on which a test is run.
success-metric
The metric or metrics that a user is comparing variants with.
control
The variant that all other variants in the experiment are being compared with. Enter the name of the control variant dimension item.
significance-threshold
The threshold in this function is set to a default of 95%.
## Cosine cosine

**COSINE(metric)**

[Row]{class="badge neutral"} Returns the cosine of the given angle. If the angle is in degrees, multiply the angle by PI()/180.

Argument
Description
metric
The angle in radians for which you want the cosine
## Cube Root cube-root

**CUBE ROOT(metric)**

Returns the positive cube root of a number. The cube root of a number is the value of that number raised to the power of 1/3.

Argument
Description
metric
The metric for which you want to calculate the cube root
## Cumulative cumulative

**CUMULATIVE(number, metric)**

Returns the sum of the last n elements of column x. If n > 0, sum the last n elements or x. If n < 0, sum the preceding elements.

Argument
Description
number
The last N number of rows to return the sum for. If N <= 0 use all previous rows.
metric
The metric for which you would like the Cumulative Sum.
### Examples

Date
Revenue
CUMULATIVE(0, Revenue)
CUMULATIVE(2, Revenue)
May
$500
$500
$500
June
$200
$700
$700
July
$400
$1100
$600
## Cumulative (Average) cumulative-average

**CUMULATIVE AVERAGE(number, metric)**

Returns the average of the last n elements of column x. If n > 0, sum the last n elements or x. If n < 0, sum the preceding elements.

Argument
Description
number
The last N number of rows to return the average for. If N <= 0 use all previous rows.
metric
The metric for which you would like the Cumulative Average.
NOTE
This function does not work with rate metrics like revenue per person. The function averages the rates instead of summing revenue over the last N and summing persons over the last N and then dividing them.
Instead, use
CUMULATIVE(revenue)
CUMULATIVE(person)
.
## Equal equal

**EQUAL()**

Equal. The output is either a 0 (false) or 1 (true).

Argument
Description
metric_X
The metric you want to use to compare.
metric_Y
The metric you want to use to compare against.
### Example

Metric 1 = Metric 2

## Exponential regression: Correlation coefficient exponential-regression-correlation-coefficient

**EXPONENTIAL REGRESSION: CORRELATION COEFFICIENT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Exponential regression: Y = b * exp(aX). Returns the correlation coefficient.

Argument
Description
metric_X
A metric that you would like to correlate with metric_Y
metric_Y
A metric that you would like to correlate with metric_X
include_zeros
Whether or not to include zero values in the calculations
## Exponential Regression: Predicted Y exponential-regression-predicted-y

**EXPONENTIAL REGRESSION: PREDICTED Y(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Exponential regression: Y = b * exp(aX). Returns Y.

Argument
Description
metric_X
A metric that you would like to designate as the independent data.
metric_Y
A metric that you would like to designate as the dependent data.
include_zeros
Whether or not to include zero values in the calculations
## Exponential Regression: Intercept exponential-regression-intercept

**EXPONENTIAL REGRESSION: INTERCEPT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Exponential regression: Y = b * exp(aX). Returns b.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Exponential Regression: Slope exponential-regression-slope

**EXPONENTIAL REGRESSION: SLOPE(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Exponential regression: Y = b * exp(aX). Returns a.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Floor floor

**FLOOR(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Returns the largest integer not greater than a given value. For example, if you want to avoid reporting currency decimals for revenue and a product has $569.34, use the formula FLOOR(Revenue) to round revenue down to the nearest dollar, or $569.

Argument
Description
metric
The metric that you want to round.
## Greater Than greather-than

**GREATER THAN()**

The output is either a 0 (false) or 1 (true).

Argument
Description
metric_X
The base metric you want to use to compare.
metric_Y
The metric you want to use to compare against.
### Example

Metric 1 > Metric 2

## Greater Than or Equal greater-than-or-equal

**GREATER THAN OR EQUAL()**

Greater than or equal. The output is either a 0 (false) or 1 (true).

Argument
Description
metric_X
The base metric you want to use to compare.
metric_Y
The metric you want to use to compare against.
### Example

Metric 1 >= Metric 2

## Hyperbolic Cosine hyperbolic-cosine

**HYPERBOLIC COSINE(metric)**

[Row]{class="badge neutral"} Returns the hyperbolic cosine of a number.

Argument
Description
metric
The angle in radians for which you want to find the hyperbolic cosine
## Hyperbolic Sine hyperbolic-sine

**HYPERBOLIC SINE(metric)**

[Row]{class="badge neutral"} Returns the hyperbolic sine of a number.

Argument
Description
metric
The angle in radians for which you want to find the hyperbolic sine
## Hyperbolic Tangent hyperbolic-tangent

**HYPERBOLIC TANGENT(metric)**

[Row]{class="badge neutral"} Returns the hyperbolic tangent of a number.

Argument
Description
metric
The angle in radians for which you want to find the hyperbolic tangent
## If if

**IF(logical_test, value_if_true, value_if_false)**

[Row]{class="badge neutral"} If the value of the condition parameter is non-zero (true), the result is the value of the value_if_true parameter. Otherwise, it is the value of the value_if_false parameter.

Argument
Description
logical_test
Required. Any value or expression that can be evaluated to TRUE or FALSE
value_if_true
The value that you want to be returned if the logical_test argument evaluates to TRUE. (This argument defaults to 0 if not included.)
value_if_false
The value that you want to be returned if the logical_test argument evaluates to FALSE. (This argument defaults to 0 if not included.)
## Less Than less-than

**LESS THAN()**

The output is either a 0 (false) or 1 (true).

Argument
Description
metric_X
The metric you want to use to compare.
metric_Y
The metric you want to use to compare against.
### Example

Metric 1 < Metric 2

## Less Than or Equal less-than-or-equal

**LESS THAN OR EQUAL()**

Less than or equal. The output is either a 0 (false) or 1 (true).

Argument
Description
metric_X
The metric you want to use to compare.
metric_Y
The metric you want to use to compare against.
### Example

Metric 1 <= Metric 2

## Lift lift

**LIFT(normalizing-container, success-metric, control)**

The lift of the ratio compared to the control value.

Argument
Description
normalizing-container
The basis (People, Sessions, or Events) on which a test is run.
success-metric
The metric or metrics that a user is comparing variants with.
control
The variant that all other variants in the experiment are being compared with. Enter the name of the control variant dimension item.
## Linear Regression: Correlation coefficient linear-regression-correlation-coefficient

**LINEAR REGRESSION: CORRELATION COEFFICIENT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Linear regression: Y = a X + b. Returns the correlation coefficient.

Argument
Description
metric_X
A metric that you would like to correlate with metric_Y
metric_Y
A metric that you would like to correlate with metric_X
include_zeros
Whether or not to include zero values in the calculations
## Linear Regression: Intercept linear-regression-intercept

**LINEAR REGRESSION: INTERCEPT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Linear regression: Y = a X + b. Returns b.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Linear Regression: Predicted Y linear-regression-predicted-y

**LINEAR REGRESSION: PREDICTED Y(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Linear regression: Y = a X + b. Returns Y.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Linear Regression: Slope linear-regression-slope

**LINEAR REGRESSION: SLOPE(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Linear regression: Y = a X + b. Returns a.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Log Base 10 log-base-ten

**LOG BASE 10(metric)**

[Row]{class="badge neutral"} Returns the base-10 logarithm of a number.

Argument
Description
metric
The positive real number for which you want the base-10 logarithm
## Log Regression: Correlation coefficient log-regression-correlation-coefficient

**LOG REGRESSION: CORRELATION COEFFICIENT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Log regression: Y = a ln(X) + b. Returns the correlation coefficient.

Argument
Description
metric_X
A metric that you would like to correlate with metric_Y
metric_Y
A metric that you would like to correlate with metric_X
include_zeros
Whether or not to include zero values in the calculations
## Log Regression: Intercept log-regression-intercept

**LOG REGRESSION: INTERCEPT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Log regression: Y = a ln(X) + b. Returns b.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Log Regression: Predicted Y log-regression-predicted-y

**LOG REGRESSION: PREDICTED Y(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Log regression: Y = a ln(X) + b. Returns Y.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Log Regression: Slope log-regression-slope

**LOG REGRESSION: SLOPE(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Log regression: Y = a ln(X) + b. Returns a.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Natural Log natural-log

**NATURAL LOG(metric)**

Returns the natural logarithm of a number. Natural logarithms are based on the constant e (2.71828182845904). LN is the inverse of the EXP function.

Argument
Description
metric
The positive real number for which you want the natural logarithm
## Not not

**NOT(logical)**

Negation as a boolean. The output is either 0 (false) or 1 (true).

Argument
Description
logical
Required. A value or expression that can be evaluated to TRUE or FALSE
## Not Equal not-equal

**NOT EQUAL()**

Not Equal. The output is either a 0 (false) or 1 (true).

Argument
Description
metric_X
The metric you want to use to compare.
metric_Y
The metric you want to use to compare against.
### Example

Metric 1 != Metric 2

## Or or

**OR(logical_test)**

[Row]{class="badge neutral"} Disjunction. Not equal to zero is considered to be true and equals zero is considered to be false. The output is either a 0 (false) or 1 (true).

Argument
Description
logical_test
Requires at least one parameter but can take any number of parameters. Any value or expression that can be evaluated to TRUE or FALSE
NOTE
0 (zero) means False, and any other value is True.
## Pi pi

**PI()**

Returns Pi: 3.14159…

## Power Regression: Correlation coefficient power-regression-correlation-coefficient

**POWER REGRESSION: CORRELATION COEFFICIENT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Power regression: Y = b X ^ a. Returns the correlation coefficient.

Argument
Description
metric_X
A metric that you would like to correlate with metric_Y
metric_Y
A metric that you would like to correlate with metric_X
include_zeros
Whether or not to include zero values in the calculations
## Power Regression: Intercept power-regression-intercept

**POWER REGRESSION: INTERCEPT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Power regression: Y = b X ^ a. Returns b.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Power Regression: Predicted Y power-regression-predicted-y

**POWER REGRESSION: PREDICTED Y(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Power regression: Y = b X ^ a. Returns Y.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Power Regression: Slope power-regression-slope

**POWER REGRESSION: SLOPE(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Power regression: Y = b X ^ a. Returns a.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Quadratic Regression: Correlation coefficient quadratic-regression-correlation-coefficient

**QUADRATIC REGRESSION: CORRELATION COEFFICIENT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Quadratic regression: Y = (a + bX) ^ 2, Returns the correlation coefficient.

Argument
Description
metric_X
A metric that you would like to correlate with metric_Y
metric_Y
A metric that you would like to correlate with metric_X
include_zeros
Whether or not to include zero values in the calculations
## Quadratic Regression: Intercept quadratic-regression-intercept

**QUADRATIC REGRESSION: INTERCEPT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Quadratic regression: Y = (a + bX) ^ 2, Returns a.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Quadratic Regression: Predicted Y quadratic-regression-predicted-y

**QUADRATIC REGRESSION: PREDICTED Y(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Quadratic regression: Y = (a + bX) ^ 2, Returns Y.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Quadratic Regression: Slope quadratic-regression-slope

**QUADRATIC REGRESSION: SLOPE(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Quadratic regression: Y = (a + bX) ^ 2, Returns b.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Reciprocal Regression: Correlation coefficient reciprocal-regression-correlation-coefficient

**RECIPROCAL REGRESSION: CORRELATION COEFFICIENT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Reciprocal regression: Y = a + b X ^ -1. Returns the correlation coefficient.

Argument
Description
metric_X
A metric that you would like to correlate with metric_Y
metric_Y
A metric that you would like to correlate with metric_X
include_zeros
Whether or not to include zero values in the calculations
## Reciprocal Regression: Intercept reciprocal-regression-intercept

**RECIPROCAL REGRESSION: INTERCEPT(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Reciprocal regression: Y = a + b X ^ -1. Returns a.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Reciprocal Regression: Predicted Y reciprocal-regression-predicted-y

**RECIPROCAL REGRESSION: PREDICTED Y(metric_X, metric_Y, include_zeros)**

[Row]{class="badge neutral"} Reciprocal regression: Y = a + b X ^ -1. Returns Y.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Reciprocal Regression: Slope reciprocal-regression-slope

**RECIPROCAL REGRESSION: SLOPE(metric_X, metric_Y, include_zeros)**

[Table]{class="badge neutral"} Reciprocal regression: Y = a + b X ^ -1. Returns b.

Argument
Description
metric_X
A metric that you would like to designate as the dependent data
metric_Y
A metric that you would like to designate as the independent data
include_zeros
Whether or not to include zero values in the calculations
## Sample Variance sample-variance

**SAMPLE VARIANCE(normalizing-container, success-metric)**

Calculates an estimate of the sample variance using the formula (sum(metric^2) / (N - 1)) - (sum(metric))^2/(N*(N-1)). where N is the count of the normalizing container.This is used as a part of *any-time valid* confidence calculations. Generally, this function is not useful alone, but can be used to check calculations or for performing confidence calculations *manually*.

Argument
Description
normalizing-container
The basis (People, Sessions, or Events) on which a test is run.
success-metric
The metric or metrics that a user is comparing variants with.
## Sine sine

**SINE(metric)**

[Row]{class="badge neutral"} Returns the sine of the given angle. If the angle is in degrees, multiply the angle by PI()/180.

Argument
Description
metric
The angle in radians for which you want the sine
## T-Score t-score

**T-SCORE(metric, include_zeros)**

The deviation from the [MEAN](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-functions#mean), divided by the standard deviation. Alias for [Z-Score](#z-score).

Argument
Description
metric
The metric for which you would like the T Score
include_zeros
Whether or not to include zero values in the calculations
## T-Test t-test

**T-TEST(metric, degrees, tails)**

Performs an m-tailed t-test with t-score of x and n degrees of freedom.

Argument
Description
metric
The metric on which you would like to perform a T Test
degrees
The degrees of freedom
tails
The length of the tail to be used to perform the T Test
### Details

The signature is T-TEST(metric, degrees, tails). Underneath, it simply calls *m* **CDF-T(-ABSOLUTE VALUE(tails), degrees)**. This function is similar to the **Z-TEST** function, which runs *m* **CDF-Z(-ABSOLUTE VALUE(tails))**.

- *m* is the number of tails.
- *n* is the degrees of freedom, and should be a constant number for the whole report, that is, not changing on a row by row basis.
- *x* is the T-test statistic, and would often be a formula (for example, **Z-SCORE**) based on a metric and is evaluated on every row.

The return value is the probability of seeing the test statistic x given the degrees of freedom and number of tails.

### Examples

- Use the function to find outliers: code language-none T-TEST(Z-SCORE(bouncerate), ROW COUNT - 1, 2)
- Combine the function with IF to ignore very high or low bounce rates, and count sessions on everything else: code language-none IF(T-TEST(Z-SCORE(bouncerate), ROW COUNT - 1, 2) < 0.01, 0, sessions )

## Tangent tangent

**TANGENT(metric)**

Returns the tangent of the given angle. If the angle is in degrees, multiply the angle by PI()/180.

Argument
Description
metric
The angle in radians for which you want the tangent
## Z-Score z-score

**Z-SCORE(metric, include_zeros)**

[Row]{class="badge neutral"} The deviation from the mean divided by the standard deviation.

Argument
Description
metric
The metric for which you would like the Z Score
include_zeros
Whether or not to include zero values in the calculations
A Z-score of 0 (zero) implies the score is the same as the mean. A Z-score can be positive or negative, indicating whether it is above or below the mean and by how many standard deviations.

The equation for Z-score is:

Where *x* is the raw score, *μ* is the mean of the population, and *σ* is the standard deviation of the population.

NOTE
μ
(mu) and
σ
(sigma) are automatically calculated from the metric.
## Z-Test z-test

**Z-TEST(metric_tails)**

Performs an n-tailed z-test with a z-score of x.

Argument
Description
metric
The metric on which you would like to perform a Z Test
tails
The length of the tail to be used to perform the Z Test
NOTE
Assumes that the values are normally distributed.
recommendation-more-help
