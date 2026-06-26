---
title: "Date time functions date-time"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/functions/dates"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:53.376623+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Date time functions date-time

Last update: May 8, 2026
- Topics:
- [Personalization](#)

CREATED FOR:

- Experienced
- Developer

Date and time functions are used to perform date and time operations on values within Journey Optimizer.

NOTE
The
now()
function is not available in the personalization editor. Use
getCurrentZonedDateTime()
or
currentTimeInMillis()
instead for current date/time values.
Learn more
## Add Days add-days

The addDays function adjusts a given date by a specified number of days, using positive values to increment and negative values to decrement.

**Syntax**

```
{%= addDays(date, number) %}
```

Example
- Input: {%= addDays(stringToDate("2024-11-01T17:19:51Z"),10) %}
- Output: 2024-11-11T17:19:51Z

## Add Hours add-hours

The addHours function adjusts a given date by a specified number of hours, using positive values to increment and negative values to decrement.

**Syntax**

```
{%= addHours(date, number) %}
```

Example
- Input: {%= addHours(stringToDate("2024-11-01T17:19:51Z"),1) %}
- Output: 2024-11-01T18:19:51Z

## Add Minutes add-minutes

The addMinutes function adjusts a given date by a specified number of minutes, using positive values to increment and negative values to decrement.

**Syntax**

```
{%= addMinutes(date, number) %}
```

Example
- Input: {%= addMinutes(stringToDate("2024-11-01T17:59:51Z"),10) %}
- Output: 2024-11-01T18:09:51Z

## Add Months add-months

The addMonths function adjusts a given date by a specified number of months, using positive values to increment and negative values to decrement.

**Syntax**

```
{%= addMonths(date, number) %}
```

Example
- Input: {%= addMonths(stringToDate("2024-11-01T17:19:51Z"),2) %}
- Output: 2025-01-01T17:19:51Z

## Add Seconds add-seconds

The addSeconds function adjusts a given date by a specified number of seconds, using positive values to increment and negative values to decrement.

**Syntax**

```
{%= addSeconds(date, number) %}
```

Example
- Input: {%= addSeconds(stringToDate("2024-11-01T17:19:51Z"),10) %}
- Output: 2024-11-01T17:20:01Z

## Add Years add-years

The addYears function adjusts a given date by a specified number of years, using positive values to increment and negative values to decrement.

**Syntax**

```
{%= addYears(date, number) %}
```

Example
- Input: {%= addYears(stringToDate("2024-11-01T17:19:51Z"),2) %}
- Output: 2026-11-01T17:19:51Z

## Age age

The age function is used to retrieve the age from a given date.

**Syntax**

```
 {%= age(datetime) %}
```

## Age In Days age-days

The ageInDays function calculates the age of a given date in days, i.e. the number of days elapsed between the given date and the current date, negative for future dates and positive for past dates.

**Syntax**

```
{%= ageInDays(date) %}
```

Example
currentDate = 2025-01-07T12:17:10.720122+05:30 (Asia/Kolkata)

- Input: {%= ageInDays(stringToDate("2025-01-01T17:19:51Z"))%}
- Output: 5

## Age In Months age-months

The ageInMonths function calculates the age of a given date in months, i.e. the number of months elapsed between the given date and the current date , negative for future dates and positive for past dates.

**Syntax**

```
{%= ageInMonths(date) %}
```

Example
currentDate = 2025-01-07T12:22:46.993748+05:30(Asia/Kolkata)

- Input: {%=ageInMonths(stringToDate("2024-01-01T00:00:00Z"))%}
- Output: 12

## Compare Dates compare-dates

The compareDates function compares the first input date with the other. Returns 0 if date1 is equal to date2, -1 if date1 comes before date2 and 1 if date1 comes after date2.

**Syntax**

```
{%= compareDates(date1, date2) %}
```

Example
- Input: {%=compareDates(stringToDate("2024-12-02T00:00:00Z"), stringToDate("2024-12-03T00:00:00Z"))%}
- Output: -1

## Convert ZonedDateTime convert-zoned-date-time

The convertZonedDateTime function converts a date-time to a given timezone.

**Syntax**

```
{%= convertZonedDateTime(dateTime, timezone) %}
```

Example
- Input: {%=convertZonedDateTime(stringToDate("2019-02-19T08:09:00Z"), "Asia/Tehran")%}
- Output: 2019-02-19T11:39+03:30[Asia/Tehran]

## Current time in milliseconds current-time

The currentTimeInMillis function is used to retrieve current time in epoch milliseconds.

**Syntax**

```
{%= currentTimeInMillis() %}
```

## Date difference date-diff

The dateDiff function is used to retrieve the difference between two dates in number of days.

**Syntax**

```
{%= dateDiff(datetime,datetime) %}
```

## Day of month day-month

The dayOfMonth returns the number representing the day of the month.

**Syntax**

```
{%= dayOfMonth(datetime) %}
```

Example
- Input: {%= dayOfMonth(stringToDate("2024-11-05T17:19:51Z")) %}
- Output: 5

## Day of week day-week

The dayOfWeek function is used to retrieve the day of week.

**Syntax**

```
{%= dayOfWeek(datetime) %}
```

## Day of year day-year

The dayOfYear function is used to retrieve the day of year.

**Syntax**

```
{%= dayOfYear(datetime) %}
```

## Diff In Seconds diff-seconds

The diffInSeconds function returns the difference between two dates in terms of seconds.

**Syntax**

```
{%= diffInSeconds(endDate, startDate) %}
```

Example
- Input: {%=diffInSeconds(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-11-01T17:19:01Z"))%}
- Output: 50

## Extract Hours extract-hours

The extractHours function extracts the hour component from a given timestamp.

**Syntax**

```
{%= extractHours(date) %}
```

Example
- Input: {%= extractHours(stringToDate("2024-11-01T17:19:51Z"))%}
- Output: 17

## Extract Minutes extract-minutes

The extractMinutes function extracts the minute component from a given timestamp.

**Syntax**

```
{%= extractMinutes(date) %}
```

Example
- Input: {%= extractMinutes(stringToDate("2024-11-01T17:19:51Z"))%}
- Output: 19

## Extract Months extract-months

The extractMonth function extracts the month component from a given timestamp.

**Syntax**

```
{%= extractMonths(date) %}
```

Example
- Input: {%=extractMonth(stringToDate("2024-11-01T17:19:51Z"))%}
- Output: 11

## Extract Seconds extract-seconds

The extractSeconds function extracts the second component from a given timestamp.

**Syntax**

```
{%= extractSeconds(date) %}
```

Example
- Input: {%=extractSeconds(stringToDate("2024-11-01T17:19:51Z"))%}
- Output: 51

## Format date format-date

The formatDate function is used to format a date time value. The format should be a valid Java DateTimeFormat pattern.

**Syntax**

```
{%= formatDate(datetime, format) %}
```

Where the first parameter is the date-time attribute and the second value is how you would like the date to be converted and displayed.

NOTE
The
formatDate
function requires a
date-time field type
as input, not a string. If your field is stored as a string type in your XDM schema, you must first convert it to date-time using a conversion function like
stringToDate()
or
toDateTime()
. See the examples below.
If a date pattern is invalid the date will fallback to ISO standard format.
You can use Java date formatting functions as summarized in
Oracle documentation
**Examples**

Formatting a date-time field
The following operation formats a date-time field to MM/DD/YY format.

| code language-sql |
| --- |
| {%= formatDate(profile.timeSeriesEvents._mobile.hotelBookingDetails.bookingDate, "MM/dd/YY") %} |

Converting a string to date first
If your field is stored as a string, you must first convert it to a date-time using stringToDate() before formatting it.

| code language-sql |
| --- |
| {%= formatDate(stringToDate(profile.person.birthDayAndMonth), "MM/DD/YY") %} |

Full date format with day name
The following operation returns a full date format with day name, month name, day and year.

| code language-sql |
| --- |
| {%= formatDate(profile.person.birthDateTime, "EEEE MMMM dd yyyy") %} |

Output: Wednesday January 01 2020

Dynamic date based on system time
You can format the current system time to generate dynamic dates. The following operation returns the current date in MM/dd/YYYY format.

| code language-sql |
| --- |
| {%= formatDate(getCurrentZonedDateTime(), "MM/dd/YYYY") %} |

Output (on Jan 30, 2026): 01/30/2026

Day of week format
You can extract the day of the week in short form.

| code language-sql |
| --- |
| {%= formatDate(getCurrentZonedDateTime(), "EEE") %} |

Output: Sun (for Sunday), Mon (for Monday), Tue (for Tuesday), etc.

For lowercase output, combine with the lowerCase function:

| code language-sql |
| --- |
| {%= lowerCase(formatDate(getCurrentZonedDateTime(), "EEE")) %} |

Output: sun, mon, tue, etc.

Formatting a timestamp from a context event
When using a timestamp from a journey event context attribute, two requirements apply:

- **Wrap the timestamp with toDateTime()** — context event timestamps are not automatically recognized as date-time values by formatDate().
- **Wrap numeric event IDs in backticks** — if your event ID is a number (for example, 1697323153), it must be escaped with backticks in the expression path, otherwise the editor raises a PQL syntax error.
- **Use {% let %} assignment syntax** — inline {%= %} syntax does not support this pattern. Assign the result to a variable first, then render it with {{varName}}.

| code language-handlebars |
| --- |
| {% let appointmentDate = formatDate(toDateTime(context.journey.events.`1697323153`.timestamp), "dd/MM/yyyy HH:mm") %} {{appointmentDate}} |

Output (example): 18/03/2026 14:30

CAUTION
Common error: “mismatched input ‘(’ expecting <EOF>”
This PQL syntax error occurs when using
formatDate()
with a context event timestamp inline (
{%= formatDate(...) %}
). The most common causes are a numeric event ID that is not wrapped in backticks (
`
), or a timestamp field passed directly to
formatDate()
without first wrapping it in
toDateTime()
. To fix both issues, use the
{% let %}
assignment pattern shown in the example above.`
### Pattern characters pattern-characters

Some pattern letters may look similar but represent different concepts.

Pattern
Meaning
Example (for
2023-12-31T10:15:30Z
)
y
Calendar year (standard year)
2023
Y
Week-based year (ISO 8601). May differ at year boundaries.
2024
(since Dec 31, 2023 falls in the first week of 2024)
M
Month-of-year (1–12 or text like
Jan
,
January
)
12
or
Dec
m
Minute-of-hour (0–59)
15
d
Day-of-month (1–31)
31
D
Day-of-year (1–366)
365
### Format date with locale support format-date-locale

The formatDate function can be used to format a date time value into its corresponding language sensitive representation, i.e in a desired locale. The format should be a valid Java DateTimeFormat pattern.

**Syntax**

```
{%= formatDate(datetime, format, locale) %}
```

Where the first string is the date attribute, second value is how you would like the date to be converted and displayed and the third value represents the locale in string format.

NOTE
If a date pattern is invalid the date will fallback to ISO standard format.
You can use Java date formatting functions as summarized in
Oracle documentation
.
You can use formatting and valid locales as summarized in
Oracle documentation
and
Supported locales
.
**Example**

The following operation will return the date in the following format: MM/dd/YY and locale FRANCE.

```
{%= formatDate(profile.timeSeriesEvents._mobile.hotelBookingDetails.bookingDate, "MM/dd/YY", "fr_FR") %}
```

## Get CurrentZonedDateTime get-current-zoned-date-time

The getCurrentZonedDateTime function returns the current date and time with time zone information.

**Syntax**

```
{%= getCurrentZonedDateTime() %}
```

Example
- Input: {%= getCurrentZonedDateTime() %}
- Output: 2024-12-06T17:22:02.281067+05:30[Asia/Kolkata]

## Hours Difference hours-difference

The diffInHours function returns the difference between two dates in terms of hours.

**Syntax**

```
{%= diffInHours(endDate, startDate) %}
```

Example
- Input: {%= diffInHours(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-11-01T07:19:51Z"))%}
- Output: 10

## Minutes Difference diff-minutes

The diffInMinutes function is used to return the difference between two dates in terms of minutes.

**Syntax**

```
{%= diffInMinutes(endDate, startDate) %}
```

Example
- Input: {%= diffInMinutes(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-11-01T16:19:51Z"))%}
- Output: 60

## Months Difference months-difference

The diffInMonths function returns the difference between two dates in terms of months.

**Syntax**

```
{%= diffInMonths(endDate, startDate) %}
```

Example
- Input: {%=diffInMonths(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2024-08-01T17:19:51Z"))%}
- Output: 3

## Set days set-days

The setDays function is used to set the day of the month for the given date-time.

**Syntax**

```
{%= setDays(datetime, day) %}
```

## Set hours set-hours

The setHours function is used to set the hour of the date-time.

**Syntax**

```
{%= setHours(datetime, hour) %}
```

## To date time to-date-time

The ToDateTime function converts string to date. It returns the epoch date as output for invalid input.

**Syntax**

```
{%= toDateTime(string, string) %}
```

Example
- Input: {%=toDateTime("2024-11-01T17:19:51Z")%}
- Output: 2024-11-01T17:19:51Z

## To UTC to-utc

The toUTC function is used to convert a datetime to UTC.

**Syntax**

```
{%= toUTC(datetime) %}
```

## Truncate to start of day truncate-day

The truncateToStartOfDay function is used to modify a given date-time by setting it to the start of the day with the time set to 00:00.

**Syntax**

```
{%= truncateToStartOfDay(date) %}
```

Example
- Input: {%= truncateToStartOfDay(stringToDate("2024-11-01T17:19:51Z")) %}
- Output: 2024-11-01T00:00Z

## truncateToStartOfQuarter truncate-quarter

The truncateToStartOfQuarter function is used to truncate a date-time to the first day of its quarter (e.g., Jan 1, Apr 1, Jul 1, Oct 1) at 00:00.

**Syntax**

```
{%= truncateToStartOfQuarter(dateTime) %}
```

Example
- Input: {%=truncateToStartOfQuarter(stringToDate("2024-11-01T17:19:51Z"))%}
- Output: 2024-10-01T00:00Z

## truncateToStartOfWeek truncate-week

The truncateToStartOfWeek function modifies a given date-time by setting it to the start of the week(Monday at 00:00).

**Syntax**

```
{%= truncateToStartOfWeek(dateTime) %}
```

Example
- Input: {%= truncateToStartOfWeek(stringToDate("2024-11-19T17:19:51Z"))%} // tuesday
- Output: 2024-11-18T00:00Z // monday

## truncateToStartOfYear truncate-year

The truncateToStartOfYear function is used to modify a given date-time by truncating it to the first day of the year (January 1st) at 00:00.

**Syntax**

```
{%= truncateToStartOfYear(dateTime) %}
```

Example
- Input: {%=truncateToStartOfYear(stringToDate("2024-11-01T17:19:51Z"))%}
- Output: 2024-01-01T00:00Z

## Week of year week-of-year

The weekOfYear function is used to retrieve the week of the year.

**Syntax**

```
{%= weekOfYear(datetime) %}
```

## Years Difference diff-years

The diffInYears function is used to return the difference between two dates in terms of years.

**Syntax**

```
{%= diffInYears(endDate, startDate) %}: int
```

Example
- Input: {%=diffInYears(stringToDate("2024-11-01T17:19:51Z"), stringToDate("2019-10-01T17:19:51Z"))%}
- Output: 5

recommendation-more-help
