---
title: "Metric type and Attribution"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/cm-workflow/m-metric-type-alloc"
category: "other"
topic: "analytics-platform/using/cja-components/cja-calcmetrics"
created_at: "2026-06-23T20:44:50.195151+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Metric type and Attribution

Last update: May 13, 2026
- Topics:
- [Calculated Metrics](#)

CREATED FOR:

- User
- Admin

You can configure the metric type and [attribution model](#attribution-models) for a metric in a calculated metric definition.

- Select in the metric component.
- In the popup dialog: Specify the Metric type : table 0-row-2 1-row-2 2-row-2 Metric Type Definition Standard If a formula consists of a single standard metric, it displays identical data to its non-calculated-metric counterpart. Standard metrics are useful to create calculated metrics specific to each individual line item. For example, Orders Sessions takes the orders for that specific line item and divides it by the number of sessions for that specific line item. Grand total Use Grand total for the reporting period in every line item. If a formula consists of a single Grand total metric, the calculated metric displays the same Grand total number on every line item. Grand total metrics are useful when you want to create calculated metrics that compare against total data. For example, Orders Total Sessions shows the proportion of orders against all sessions, not just the sessions to the specific line item. In this example, you specify Grand Total for the Sessions metric in your calculated metric, which will automatically turn it into Total Sessions . Specify Attribution . You can either: Disable Use non-default attribution model to use the default column attribution model, which is Last Touch, with a lookback window of 30 days. Enable Use non-default attribution model . In the Column attribution model dialog, Select a Model from the attribution models . Select a Container from the container options. Select a Lookback window from the lookback window options. If you select Custom Time , you can define the time period in Minute(s) up to Quarter(s) . Select Apply to apply the non-default attribution model. Select Cancel to cancel. If you already have defined a non-default attribution model, select Edit to modify the selection.

See [Example](#example) for an example of using an attribution model, container, and lookback window.

## Attribution models attribution-models

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
## Container container

An attribution container defines the desired scope for the attribution. Possible options are:

- **Session**: Looks back up to the beginning of the session where a conversion happened. Session lookback windows respect the modified [Session timeout](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#session-settings) in a data view. When **Session** is selected, the [Attribution lookback window](#atribution-lookback-window) is automatically set to **Reporting window** and cannot be changed.
- **Person**: Looks at conversions from the scope of the person container.
- **Global Account** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the global accounts container.
- **Accounts** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the person container .
- **Opportunity** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the opportunity container .
- **Buying group** [B2B Edition]{class="badge informative"}: Looks at conversions from the scope of the buying group container.

## Lookback window lookback-winwow

A attribution lookback window is the amount of time a conversion should look back to include touch points. If a dimension item is set outside of the lookback window, the value is not included in any attribution calculations.

- **Reporting window**: Looks back up to the start of the reporting window from when the conversion happened.
- **14 Days**: Looks back up to 14 days from when the conversion happened.
- **30 Days**: Looks back up to 30 days from when the conversion happened.
- **60 Days**: Looks back up to 60 days from when the conversion happened.
- **90 Days**: Looks back up to 90 days from when the conversion happened.
- **13 Months** [B2B Edition]{class="badge informative"}: Looks back up to 13 months from when the conversion happened.
- **Custom Time:** Allows you to set a custom lookback window from when a conversion happened. You can specify the number of minutes, hours, days, weeks, months, or quarters. For example, if a conversion happened on February 20, a lookback window of five days would evaluate all dimension touchpoints from February 15 to February 20 in the attribution model.

## Example

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
Attribution component settings
Participation metric
recommendation-more-help
