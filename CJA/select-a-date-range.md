---
title: "Select a date range"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-reportbuilder/select-date-range"
category: "other"
topic: "analytics-platform/using/cja-reportbuilder/select-date-range"
created_at: "2026-06-02T19:08:55.252370+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Select a date range

Last update: May 13, 2026
- Topics:
- [Report Builder](#)

CREATED FOR:

- User

To change the date range of an existing data block:

- Select **Edit a data block**, or
- Select the **Date range** link in **Quick edit**.

Use the following options to change a date range for a data block.

## Calendar

The **Calendar** option allows you to create static or rolling dates using the following options:

### Date range

The date range field displays the current date range for the data block request. You can enter dates directly or use to specify a date range.

{modal="regular"}

### Presets

Use the presets drop-down menu to select a preset. You can also enter text to search for presets.

{modal="regular"}

The preset drop-down menu includes a standard set of preset date ranges and date range components for a data view that you saved or a data view that was shared with you.

### Rolling dates

To define rolling dates:

{modal="regular"}

- Select Use rolling dates to define the logic for a rolling date definition. You can select the text in brackets (for example fixed start - rolling daily ) to extend the panel and specify details for Start and End .
- Select Start of , End of , or Fixed day . When you have selected Start of or End of , you can build a full expression. For example: End of current year plus 1 day . Pick the appropriate value for each individual part of the expression. Select a value for current. For example, current year . Select a value for an optional additional calculation. For example, plus . When you have specified an additional calculation, specify a value. For example, 1 . When you have specified an additional calculation, select the time period to use for the calculation. For example, day . When you have select Fixed Day , specify a fixed day or use the picker to select a day.
- Select hide to hide the details for rolling dates calculation.

### Custom expressions

The custom expression option allows you to change the date range by building a custom expression or you can enter an arithmetic formula.

{modal="regular"}

- Select Use rolling dates .
- Select Use custom expression . When you select Use custom expression , the standard rolling date range controls are disabled.
- Enter a custom expression .
- Use the Date preview to verify the resulting date range.

#### Create a custom expression

- Enter a date reference .
- Add an optional date operator to move the date to the past or future.

You can enter a custom expression that includes multiple operators, such as tm-11m-1d.

#### Date references

The following table lists date reference examples.

Date reference
Type
Description
1/1/10
Static Date
Entered in ISO Date format
td
Rolling Date
Start of current day
tw
Rolling Date
Start of current week
tm
Rolling Date
Start of current month
tq
Rolling Date
Start of current quarter
ty
Rolling Date
Start of current year
#### Date operators

The following table lists date operator examples.

Date operator
Unit
Description
+6d
Day
Add 6 days to the Date Reference
+1w
Week
Add one full week to the Date Reference
-2m
Month
Subtract 2 full months to the Date Reference
-4q
Quarter
Subtract 4 quarters to the Date Reference
-
1y
Year
Subtract one year to the Date Reference
#### Date expressions

The following table lists date expression examples.

Date Expression
Meaning
td
Today
td-1w
First day of last week
tm-1d
Last day of previous month
td-52w
Same day, 52 weeks ago
tm-11m-1d
Last day of the same month last year
"2020-09-06"
Specific date, Sept 9th, 2020
## Date range from cell

The date range can be specified in worksheet cells. Use the **Date range from cell** option to choose the data block start and end date from selected cells. When you select the **From cell** option, the panel displays **From** and **To** fields where you can enter a cell location or use to pick the current selected cell.

{modal="regular"}

## Exclude today

Select **Exclude today** to exclude today from a selected date range. The current day is excluded from all modes used to define a date range: calendar, rolling dates, or custom expressions.

## Valid date ranges

The following list describes valid date range formats.

- The start and end dates must be in the following format: YYYY-MM-DD
- The start date must be earlier to or equal to the end date. Both dates can be set to the future.
- When using rolling dates, the start date must be today or in the past. The start day must be in the past if Exclude today is selected.
- You can create a static date range set for the future. For example, you may need to set a future date for a marketing campaign launch next week. This option creates a workbook monitoring for a campaign ahead of time.

## Change the date range

You can edit the date range of an existing data block.

- Select a cell in your data block.

- Select **Edit data block** in the **Commands** panel, or
- Select the **Date range** link in the **Quick edit** panel.

- Modify the date range using any of the date selection options available.
- Select Apply .

Report Builder applies the new date range to all data blocks in the selection.

recommendation-more-help
