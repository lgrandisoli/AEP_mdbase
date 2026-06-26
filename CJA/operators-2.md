---
title: "Operators"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/segments/seg-operators"
category: "other"
topic: "analytics-platform/using/cja-components/segments"
created_at: "2026-06-23T20:45:19.446821+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Operators

Last update: May 13, 2026
- Topics:
- [Filters](#)
- [Segments](#)

CREATED FOR:

- User

The Segment builder lets you compare and constrain values for components using selected operators. There are three categories of operators: [Standard](#standard-operators), [Data Warehouse](#data-warehouse-operators), and [Distinct Count](#distinct-count-operators).

Depending on the operator you select:

- You can enter a value.
- You can enter part of a value and select from a drop-down menu (if available).
- Immediately select a value from the drop-down menu (if available).

When you type a value for an operator that validates available values, like **equals**, and the value doesn’t match the values available for the component, you see a icon. You can either select a value from the drop-down menu or press *Enter* to enter the value.

## Wildcards

The only supported wildcard character for operators that support wildcards is the asterisk: *. If you need to search for the specific * character, you can escape it with a backslash, like \*.

For example, you have a page name called *My cool product*.

- The segment rule **Page name** **matches** * product will match the above page name.
- However, the rule **Page name** **matches** My \* product matches only the page name *My * Product*.

## Standard operators

Operator
The selected dimension, segment, or metric event…
equals
Returns items that match exactly for a numeric or string value. Note: If using wildcard characters, use the
matches
operator.
does not equal
Returns all items that do not contain the exact match of the value entered. Note: If using wildcard characters, use the
does not match
operator.
equals any of
Returns items that match exactly for any value in the input field (up to 500 items). For example, entering
Search Results, Homepage
for the
Page Name
dimension with this operator would match
Search Results
and
Homepage
, and count as 2 items. The input field for this operator is comma-delimited.
does not equal any of
Identifies items that match exactly for any value in the input field (up to 500 items), and then only returns items without these values. For example, entering
Search Results, Homepage
with this operator for the
Page Name
dimension would identify
Search Results
and
Homepage
and then
exclude
them from the returned items. This example would count as 2 items. The input field for this operator is comma-delimited.
contains
Returns items that compare to the substrings of the values entered. For example, if the rule is
Page Name
contains
Search
, then this rule will match any page that has the substring
Search
in it, including
Search Results
,
Search
, and
Searching
. The “contains” clause is not case sensitive in Adobe Analytics, but it is case sensitive in Customer Journey Analytics.
does not contain
Returns the inverse of the
contains
rule. Specifically, all items that match the entered value will be excluded from the entered values. For example, if the rule is
Page Name
does not contain
Search
, then it will not match any page that has the substring
Search
in it, including
Search Results
,
Search
, and
Searching
. These values will be excluded from the results.
contains all of
Returns items compared to the substrings, including multiple values joined together. For example, entering
Search Results
with this operator for the
Page Name
dimension would match
Search Results
and
Results of Search
, but not
Search
or
Results
individually. The rule would match
Search
AND
Results
found together. The input field for this operator is space-delimited (100 words).
does not contain all of
Identifies items compared to substrings, including multiple values joined together, and then only return items without these values. For example, entering
Search Results
with this operator for the
Page Name
dimension would identify
Search Results
and
Results of Search
(but not
Search
or
Results
individually) and then exclude these items. The input field for this operator is space-delimited (100 words).
contains any of
Returns items compared to the substrings, including multiple values joined or independently identified. For example, entering
Search Results
with this operator would match
Search Results
,
Results of Search
,
Search
, and
Results
. It would match either
Search
OR
Results
found together or independently. The input field for this operator is space-delimited (100 words).
does not contain any of
Identifies items based on substrings and then returns values that do not contain these substrings. It can have multiple joined values or values independently identified. For example, entering
Search Results
for the
Page Name
dimension would match
Search Result
s,
Results of Search
,
Search
, and
Results
where either
Search
or
Result
are found together or independently. It would then exclude items that contain these substrings. The input field for this operator is space-delimited (100 words).
starts with
Returns items that start with the string value entered.
does not start with
Returns all items that do not start with the string value entered. This is the inverse of the
starts with
operator.
ends with
Returns items that end with string value entered.
does not end with
Returns all items that do not end with the string value entered. This is the inverse of the
ends with
operator.
matches
Returns items that match exactly based on a given numeric or string value. The **matches** clause is case sensitive in Adobe Analytics and in Customer Journey Analytics. **Note**: Use this operator when using [wildcard](#wildcards) (globbing) features. Examples of “globbing”:

- a*e would match ae, abcde, adobe, and a whole sentence
- adob* would match adobe, adobe analytics, and adobo recipe
- *dobe would match dobe, adobe, and cute little dobe

does not match
Returns all items that do not contain the exact match of the value entered. Note: Use this operator when using
wildcard
(globbing) features.
exists
Returns the number of items that exist. For example, if you evaluate the
Pages Not Found
dimension using the
exist
operator, the number of error pages that exist is returned.
does not exist
Returns all items that do not exist. For example, if you evaluate the
Pages Not Found
dimension using the
does not exist
operator, the number of pages where this error page did not exist is returned.
## Data Warehouse operators

Operator
The selected dimension, segment, or metric event…
is less than
Returns items whose numeric count is less than the value entered.
is less than or equal to
Returns items whose numeric count is less than or equal to the value entered.
is greater than
Returns items whose numeric count is greater than the value entered.
is greater than or equal to
Returns items whose numeric count is greater than or equal to the value entered.
## Distinct Count operators

You can segment on a distinct count of items within a dimension. Examples: *Visitors who viewed more than 5 distinct products*, or *Visits where more than 5 distinct pages were seen*.

Operator
The selected dimension, segment, or metric event…
equals
Returns dimension items whose unique count equals the value entered.
does not equal
Returns dimension items whose unique count does not equal the value entered.
is greater than
Returns dimension items whose unique count is greater than the value entered.
is less than
Returns dimension items whose unique count is less than the value entered.
is greater than or equal to
Returns dimension items whose unique count is greater than or equal to the value entered.
is less than or equal to
Returns dimension items whose unique count is less than or equal to the value entered.
See [Distinct dimension counts](/en/docs/analytics-learn/tutorials/components/calculated-metrics/approximate-count-distinct-function-in-calculated-metrics#_blank) for a demo video.

style
shade-box
recommendation-more-help
