---
title: "Arrays and list functions arrays"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/functions/arrays-list"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:04.832993+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Arrays and list functions arrays

Last update: May 8, 2026
- Topics:
- [Personalization](#)

CREATED FOR:

- Experienced
- Developer

Use these functions to make interaction with arrays, lists, and strings easier.

## Count only null count-only-null

The countOnlyNull function is used to count the number of null values in a list.

**Syntax**

```
{%= countOnlyNull(array) %}
```

**Example**

```
{%= countOnlyNull([4,0,1,6,0,0]) %}
```

Returns 3.

## Count With Null count-with-null

The countWithNull function is used to count all the elements of a list including null values.

**Syntax**

```
{%= countWithNull(array) %}
```

**Example**

```
{%= countOnlyNull([4,0,1,6,0,0]) %}
```

Returns 6.

## Distinct distinct

The distinct function is used to get values from an array or list with duplicate values removed.

**Syntax**

```
{%= distinct(array) %}
```

**Example**

The following operation specifies people who have placed orders in more than one store.

```
{%= distinct(person.orders.storeId).count() > 1 %}
```

## Distinct count with null distinct-count-with-null

The distinctCountWithNull function is used to count the number of different values in a list including the null values.

**Syntax**

```
{%= distinctCountWithNull(array) %}
```

**Example**

```
{%= distinctCountWithNull([10,2,10,null]) %}
```

Returns 3.

## First item head

The head function is used to return the first item in an array or list.

**Syntax**

```
{%= head(array) %}
```

**Example**

The following operation returns the first of the top five orders with the highest price. More information about the topN function can be found in the [first n in array](#first-n) section.

```
{%= head(topN(orders,price, 5)) %}
```

## Sort and get first N in array first-n

The topN function sorts an array in descending order based on the given numerical expression and returns the first N items. If the array size is less than N, it returns the entire sorted array.

This function**Syntax**

```
{%= topN(array, value, amount) %}
```

Argument
Description
{ARRAY}
The array or list that is to be sorted.
{VALUE}
The property in which to sort the array or list.
{AMOUNT}
The number of items to be returned.
**Example**

The following operation returns the first five orders with the lowest price.

```
{%= topN(orders,price, 5) %}
```

## In in

The in function is used to determine if an item is a member of an array or list.

**Syntax**

```
{%= in(value, array) %}
```

**Example**

The following operation defines people with birthdays in March, June, or September.

```
{%= in (person.birthMonth, [3, 6, 9]) %}
```

## Includes includes

The includes function is used to determine if an array or list contains a given item.

**Syntax**

```
{%= includes(array,item) %}
```

**Example**

The following operation defines people whose favorite color includes red.

```
{%= includes(person.favoriteColors,"red") %}
```

## Intersects intersects

The intersects function is used to determine if two arrays or lists have at least one common member.

**Syntax**

```
{%= intersects(array1, array2) %}
```

**Example**

The following operation defines people whose favorite colors include at least one of red, blue, or green.

```
{%= intersects(person.favoriteColors,["red", "blue", "green"]) %}
```

## Sort and get last N in array last-n

The bottomN function sorts an array in ascending order based on the given numerical expression and returns the first N items. If the array size is less than N, it returns the entire sorted array.

**Syntax**

```
{%= bottomN(array, value, amount) %}
```

Argument
Description
{ARRAY}
The array or list that is to be sorted.
{VALUE}
The property in which to sort the array or list.
{AMOUNT}
The number of items to be returned.
**Example**

The following operation returns the last five orders with the highest price.

```
{%= bottomN(orders,price, 5) %}
```

## Not in notin

The notIn function is used to determine if an item is not a member of an array or list.

NOTE
The
notIn
function
also
ensures that neither value is equal to null. Therefore, the results are not an exact negation of the
in
function.
**Syntax**

```
{%= notIn(value, array) %}
```

**Example**

The following operation defines people with birthdays that are not in March, June, or September.

```
{%= notIn(person.birthMonth ,[3, 6, 9]) %}
```

## Subset of subset

The subsetOf function is used to determine if a specific array (array A) is a subset of another array (array B). In other words, that all elements in array A are elements of array B.

**Syntax**

```
{%= subsetOf(array1, array2) %}
```

**Example**

The following operation defines people who have visited all of their favorite cities.

```
{%= subsetOf(person.favoriteCities,person.visitedCities) %}
```

## Superset of superset

The supersetOf function is used to determine if a specific array (array A) is a superset of another array (array B). In other words, that array A contains all elements in array B.

**Syntax**

```
{%= supersetOf(array1, array2) %}
```

**Example**

The following operation defines people who have eaten sushi and pizza at least once.

```
{%= supersetOf(person.eatenFoods,["sushi", "pizza"]) %}
```

recommendation-more-help
