---
title: "Column settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/column-settings"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-02T19:07:53.616338+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Column settings

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

Column settings let you configure column formatting, some of which can be conditional.

markdownlint-disable MD034
markdownlint-enable MD034
markdownlint-disable MD034
markdownlint-enable MD034
See [Row and column settings in a Freeform table](/en/docs/analytics-learn/tutorials/analysis-workspace/building-freeform-tables/row-and-column-settings-in-freeform-tables#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
To access Column settings, select in the column heading.

You can edit settings for multiple columns at once. Select multiple columns and select in any one of the selected columns. Any change that you make applies to all columns with cells selected in them.

Option
Description
Show total
Show a client-side sum of the column. This total does
not
de-duplicate metrics like sessions or persons.
Show grand total
Show a server-side sum of the column. The grand total de-duplicates metrics like sessions or persons.
Show sparkline
Show a line chart at the column header.
Number
Determine if a cell shows/hides the numeric value for the metric. For example, if the metric is Page Views, the numeric value is the number of page views for the row item.
Percent
Determine if a cell shows/hides the percent value for the metric. For example, if the metric is Page Views, the percent value is the number of page views for the row item, divided by the total page views for the column. Note: Percentages greater than 100% are possible to ensure to be accurate. The upper bound cap can move to 1,000% to prevent columns width become too large.
Show anomalies
Determine if anomaly detection is run on the values in this column.
Show forecast
Determine if forecast values are shown in this column.
Wrap header text
Wrap the header text in Freeform tables to make headers more readable and tables more shareable. Wrapping is useful for PDF rendering and for metrics with long names. Enabled by default.
Interpret zero as no value
Determine, for cells with a 0 value, whether to show a 0 or a blank cell. This interpretation is useful when you look at data for each day of a month, and some days are in the future. Instead of showing 0’s for future dates, blank cells are shown instead. Charts respect this setting as well (that is, the charts do not show a line or bar with 0 values).
Background
Determine if a cell shows/hides all cell formatting, including the bar graph and conditional formatting.
Bar Graph
Show a horizontal bar graph representing the cell’s value relative to the total for the column.
Conditional Formatting
Use conditional formatting. See the
section
below.
Table Cell Preview
A preview of how each cell appears with the currently selected formatting options applied.
Use non-default attribution model
Use a non-default attribution model. See the
section
below.
## Conditional formatting conditional-formatting

Conditional formatting applies formatting to upper, midpoint, and lower limits that you can define. Applying conditional formatting within Freeform tables is also automatically enabled on breakdowns, unless Custom limits are selected.

Conditional formatting options
Description
Use percent limits
Change the limit range to be based on percentages rather than absolute values. The percentage limit range works for metrics that are solely percentage based (like Bounce Rate) and for metrics that have a count and a percentage (like Page Views).
Auto-generated
Automatically calculate upper/mid/lower limits based on the data. The upper limit is the largest value in this column. The lower limit is the lowest, and the midpoint is the average of the upper and lower limits.
Custom
Manually assign
Upper limit
,
Midpoint
and
Lower limit
. Limits provide the flexibility to determine when a column value becomes good, average, or poor.
Conditional formatting palette
Apply a preconfigured color set to cells. Depending on which of the four available color schemes you select, different colors are assigned to high values, midpoint values, and low values.
Replacing a dimension in the table resets the conditional formatting limits. Replacing a metric recalculates the limits for that column (where a metric is on the X axis and a dimension is on the Y axis).
## Use non-default attribution model use-non-default-attribution-model

You can override the default attribution model that is configured in [Data views](/en/docs/analytics-platform/using/cja-dataviews/component-settings/attribution).

NOTE
Consider the following when enabling a non-default attribution model on a metric:
- When using the metric in a report with a single dimension : The metric’s attribution overrides the allocation model set on the dimension. For example, a metric with a “first touch” attribution overrides a “most recent” dimension allocation.
- When using the metric in a report with multiple dimensions : The metric’s attribution is applied on top of the allocation model for each dimension. For example, a metric with a “first touch” attribution is applied on top of a “most recent” dimension allocation.

For more information about allocation, see
Persistence component settings
.
To use a non-default attribution model for a metric in an Analysis Workspace:

- Select Use non-default attribution model . When already selected, use Edit to edit the attribution model. Or unselect to return to the default attribution model.
- In Column attribution model , select a Model and a Lookback window . The lookback window determines the window of data attribution that is applied for each conversion.

### Attribution models

An attribution model determines which dimension items get credit for a metric when multiple values are seen within a metric’s lookback window. Attribution models only apply when there are multiple dimension items set within the lookback window. If only a single dimension item is set, that dimension item gets 100% credit regardless of attribution model used.

Icon
Attribution model
Definition
Last Touch
Gives 100% credit to the touch point occurring most recently before conversion. This attribution model is typically the default value for any metric where an attribution model is not otherwise specified. Organizations typically use this model where the time to conversion is relatively short, such as with analyzing internal search keywords.
First Touch
Gives 100% credit to the touch point first seen within the attribution lookback window. Organizations typically use this model to understand brand awareness or customer acquisition.
Linear
Gives equal credit to every touch point seen leading up to a conversion. It is useful where conversion cycles are longer or require more frequent customer engagement. Organizations typically use this attribution model measuring mobile app notification effectiveness or with subscription-based products.
Participation
Gives 100% credit to all unique touch points. Since every touch point receives 100% credit, metric data typically adds up to more than 100%. If a dimension item appears multiple separate times leading up to a conversion, values are deduplicated to 100%. This attribution model is ideal in situations where you want to understand which touch points customers are exposed to the most. Media organizations typically use this model to calculate content velocity. Retail organizations typically use this model to understand which parts of their site are critical to conversion.
Same Touch
Gives 100% credit to the same event where the conversion occurred. If a touch point does not happen on the same event as a conversion, It is bucketed under “None”. This attribution model is sometimes equated to having no attribution model at all. It is valuable in scenarios where you do not want values from other events affecting how a metric gives credit to dimension items. Product or design teams can use this model to assess the effectiveness of a page where conversion happens.
U Shaped
Gives 40% credit to the first interaction, 40% credit to the last interaction, and divides the remaining 20% to any touch points in between. For conversions with a single touch point, 100% credit is given. For conversions with two touch points, 50% credit is given to both. This attribution model is best used in scenarios where you value the first and last interactions the most, but don’t want to entirely dismiss additional interactions in between.
J Curve
Gives 60% credit to the last interaction, 20% credit to the first interaction, and divides the remaining 20% to any touch points in between. For conversions with a single touch point, 100% credit is given. For conversions with two touch points, 75% credit is given to the last interaction, and 25% credit is given to the first. Similar to U-Shaped, this attribution model favors the first and last interactions, but more heavily favors the last interaction.
Inverse J
Gives 60% credit to the first touch point, 20% credit to the last touch point, and divides the remaining 20% to any touch points in between. For conversions with a single touch point, 100% credit is given. For conversions with two touch points, 75% credit is given to the first interaction, and 25% credit is given to the last. Similar to J-Shaped, this attribution model favors the first and last interactions, but more heavily favors the first interaction.
Time Decay
Follows an exponential decay with a custom half-life parameter, where the default is 7 days. The weight of each channel depends on the amount of time that passed between the touch point initiation and the eventual conversion. The formula used to determine credit is
2^(-t/halflife)
, where
t
is the amount of time between a touch point and a conversion. All touch points are then normalized to 100%. Ideal for scenarios where you want to measure attribution against a specific and significant event. The longer a conversion happens after this event, the less credit is given.
Custom
Allows you to specify the weights that you want to give to first touch point, last touch point, and any touch points in between. Values specified are normalized to 100% even if the custom numbers entered do not add to 100. For conversions with a single touch point, 100% credit is given. For interactions with two touch points, the middle parameter is ignored. The first and last touch points are then normalized to 100%, and credit is assigned accordingly. This model is ideal for analysts who want full control over their attribution model and have specific needs that other attribution models do not fulfill.
Algorithmic
Uses statistical techniques to dynamically determine the optimal allocation of credit for the selected metric. The algorithm used for attribution is based on the Harsanyi Dividend from cooperative game theory. The Harsanyi dividend is a generalization of the Shapley value solution (named after Lloyd Shapley, a Nobel Laureate economist) to distributing credit among players in a game with unequal contributions to the outcome.
At a high level, attribution is calculated as a coalition of players to which a surplus must be equitably distributed. Each coalition’s surplus distribution is determined according to the surplus that was previously created by each subcoalition (or previously participating dimension items) recursively. For more details, see John Harsanyi’s and Lloyd Shapley’s original papers:
Shapley, Lloyd S. (1953). A value for n-person games.
Contributions to the Theory of Games, 2(28)
, 307-317.
Harsanyi, John C. (1963). A simplified bargaining model for the n-person cooperative game.
International Economic Review 4(2)
, 194-220.
### Container

An attribution container defines the desired scope for the attribution. Possible options are:

- **Session**: Looks back up to the beginning of the session where a conversion happened. Session lookback windows respect the modified [Session timeout](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#session-settings) in a data view. When **Session** is selected, the [Attribution lookback window](#atribution-lookback-window) is automatically set to **Reporting window** and cannot be changed.
- **Person**: Looks at conversions from the scope of the person container.
- **Global Account** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the global accounts container.
- **Accounts** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the person container .
- **Opportunity** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the opportunity container .
- **Buying group** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the buying group container.

### Lookback window

A attribution lookback window is the amount of time a conversion should look back to include touch points. If a dimension item is set outside of the lookback window, the value is not included in any attribution calculations.

- **Reporting window**: Looks back up to the start of the reporting window from when the conversion happened.
- **14 Days**: Looks back up to 14 days from when the conversion happened.
- **30 Days**: Looks back up to 30 days from when the conversion happened.
- **60 Days**: Looks back up to 60 days from when the conversion happened.
- **90 Days**: Looks back up to 90 days from when the conversion happened.
- **13 Months** [B2B Edition]{class="badge informative"}: Looks back up to 13 months from when the conversion happened.
- **Custom Time:** Allows you to set a custom lookback window from when a conversion happened. You can specify the number of minutes, hours, days, weeks, months, or quarters. For example, if a conversion happened on February 20, a lookback window of five days would evaluate all dimension touchpoints from February 15 to February 20 in the attribution model.

### Example

Consider the following example:

- On September 15, a person arrives to your site through a paid search advertisement, then leaves.
- On September 18, the person arrives to your site again through a social media link they got from a friend. They add several items to their cart, but do not purchase anything.
- On September 24, your marketing team sends them an email with a coupon for some of the items in their cart. They apply the coupon, but visit several other sites to see if any other coupons are available. They find another through a display ad, then ultimately make a purchase for $50.

Depending on your reporting window (for example September 10 - September 24), attribution model, container and channels receive different credit. See table below for examples:

Model
Container
Lookback window
Explanation
First touch
Session
Reporting window
Attribution looks at only the third visit. Between email and display, email was first, so email gets 100% credit for the $50 purchase.
First touch
Person
30 Days
Attribution looks at all three visits. Paid search was first, so it gets 100% credit for the $50 purchase.
Linear
Session
Reporting window
Credit is divided between email and display. Both of these channels each get $25 credit.
Linear
Person
30 Days
Credit is divided between paid search, social, email, and display. Each channel gets $12.50 credit for this purchase.
J-shaped
Person
30 Days
Credit is divided between paid search, social, email, and display.

- 60% credit is given to display, for $30.
- 20% credit is given to paid search, for $10.
- The remaining 20% is divided between social and email, giving $5 to each.

Time Decay
Person
30 Days
- Gap of zero days between display touch point and conversion. 2^(-0/7) = 1
- Gap of zero days between email touch point and conversion. 2^(-0/7) = 1
- Gap of six days between social touch point and conversion. 2^(-6/7) = 0.552
- Gap of nine days between paid search touch point and conversion. 2^(-9/7) = 0.41 Normalizing these values results in the following: Display: 33.8%, getting $16.88 Email: 33.8% getting $16.88 Social: 18.6%, getting $9.32 Paid Search: 13.8%, getting $6.92

Conversion events that typically have whole numbers are divided if credit belongs to more than one channel. For example, if two channels contribute to an order using a Linear attribution model, both channels get 0.5 of that order. These partial metrics are summed across all people then rounded to the nearest integer for reporting.

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank) Use specific B2B containers, like Accounts, or Opportunities, and more appropriate lookback windows (up to 13 months) to apply above attribution models in typical B2B scenarios.

Related Articles
- [Manage data sources](/en/docs/analytics-platform/using/cja-workspace/visualizations/t-sync-visualization)

recommendation-more-help
