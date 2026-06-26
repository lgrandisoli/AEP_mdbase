---
title: "Format component settings format-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/format"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-23T20:42:42.917495+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Format component settings format-component-settings

Last update: June 5, 2026
- Topics:
- [Data management](#)

CREATED FOR:

- Admin

Format lets you determine how a given component is displayed when used in reports.

## Configure format settings for a component

You can determine how a given component is displayed by adjusting its format settings.

- In Customer Journey Analytics, select the Data views tab.
- Select the data view that contains the component whose format setting you want to configure.
- Select the Components tab.
- Select the component that you want to configure, then expand the Format section on the right side of the page.
- Specify the following information: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 layout-auto Setting Description Format Lets you specify the formatting of a component as Decimal, Time, Percent, or Currency. Decimal Not visible on Integer schema data types. Lets you specify the number of decimal places a component displays. Date Lets you determine how you want the date-time field displayed when used as a dimension in reporting. Learn more Date-Time Lets you determine how you want the date-time field displayed when used as a dimension in reporting. Learn more Currency Lets you determine which currency you want the component to display in. If you analyze global data where transactions occur in different currencies, see Use currency conversion . Show upward trend as Lets you specify if an upward trend on this component is good (green) or bad (red). True value and False value Only visible on Boolean schema data types. Lets you customize the dimension item label for true and false values.

## Use currency conversion use-currency-conversion

Currency conversion in Customer Journey Analytics can be extremely valuable for businesses that operate internationally. By removing the complexities of manual currency conversion, currency conversion in Customer Journey Analytics brings uniformity and clarity to financial data. Currency conversion keeps track of daily historical exchange rates and maintains those daily rates for a period of 4 years.

For example, if an e-commerce business operates in the US, UK, and EU, sales data can be automatically converted to USD, ensuring easy comparison and holistic understanding of performance.

NOTE
Before you begin configuring a metric for currency conversion, consider the following:
- The metric you select for currency conversion must have a numeric type (Double, Long, Integer, Short, Byte).
- Set up your Customer Journey Analytics connection to contain at least one event dataset that holds a currency code dimension for every event containing a currency metric. That currency code dimension uses an alphabetic currency code conforming to the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) standard for representing currencies. These values should be in full uppercase format, such as USD for $, EUR for €, GBP for £.

To determine how currencies are displayed and converted for a given metric:

- Begin configuring the metric for which you want to use currency as the format, as described above, in Configure format settings for a metric .
- With the metric selected, make the following selections in the Format section on the right side of the page: In the Format field, select Currency . In the Decimal places field, choose the number of decimal places the metric displays. This option is available only if the metric has a numeric type of ‘Double’. Select the Convert Currency option. In the Select currency code dimension field, select the dimension that represents the currency you are converting from (the currency that your data is based on). For example, select a dimension called Currency code . If you don’t have a dimension in your current data schema that contains a currency code field, you can create a new currency code field using Data Prep , Data Distiller , or Derived Fields . Data Prep is suitable only for new implementations because it is only on a go-forward basis. Depending on an organization’s setup, Data Distiller and Derived Fields can be used to access the currency code values historically. In the Convert and display currency in field, choose the currency in which you want data to be converted.
- Repeat these steps if you want to apply currency conversion to additional metrics.

### Frequently Asked Questions

How is currency conversion executed?
Upon report time, the value of the metric and original currency code are converted to USD and then converted to the currency configured for display. For this conversion, the daily currency exchange rates are used, applicable for the time of the event.
recommendation-more-help
