---
title: "List functions list-functions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/list-functions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:02.018601+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# List functions list-functions

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)

CREATED FOR:

- Experienced
- Developer

List functions enable you to manipulate and work with collections of values within your journey expressions. These functions are essential for filtering, sorting, transforming, and analyzing arrays and lists in your customer journeys.

Use list functions when you need to:

- Filter and extract specific items from collections based on criteria ([filter](#filter), [getListItem](#getListItem))
- Sort and organize list elements in ascending or descending order ([sort](#sort))
- Remove duplicates and get unique values from lists ([distinct](#distinct), [distinctWithNull](#distinctWithNull))
- Check if values exist within collections ([in](#in))
- Limit the number of items returned from a list ([limit](#limit))
- Get the size of a list ([listSize](#listSize)) or transform lists into different formats ([serializeList](#serializeList))
- Perform set operations like finding common elements between lists ([intersect](#intersect))

List functions provide powerful tools for working with complex data structures, enabling sophisticated data manipulation and conditional logic based on collection contents.

## distinct distinct

Returns the distinct values or objects of a given list. Null entries are ignored.

Syntax
distinct(<parameters>)
Parameters
| table 0-row-3 1-row-3 2-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. |
| keyAttributeName | string | This parameter is optional and only for listObject. If the parameter is not provided, an object is considered as duplicated if all the attributes have the same values. Otherwise, an object is considered as duplicated if the given attribute has the same value. |

Signatures and returned types
distinct(<listInteger>)

Returns a list of integers.

distinct(<listDecimal>)

Returns a list of decimals.

distinct(<listString>)

Returns a list of strings.

distinct(<listDateTimeOnly>)

Returns a list of datetimes without considering time zone.

distinct(<listDateTime>)

Returns a list of datetimes.

distinct(<listDateOnly>)

Returns a list of dates.

distinct(<listBoolean>)

Returns a list of booleans.

distinct(<listDuration>)

Returns a list of durations.

distinct(<listObject>)

distinct(<listObject>,<string>)

Returns a list of objects.

Examples
distinct([10,2,10,null])

Returns [10, 2].

## distinctWithNull distinctWithNull

Returns the distinct values or objects of a given list. If the list has at least one null entry, a null entry will be present in the returned list.

Syntax
distinctWithNull(<parameters>)
Parameters
| table 0-row-3 1-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly | List to process. |

Signatures and returned types
distinctWithNull(<listInteger>)

Returns a list of integers.

distinctWithNull(<listDecimal>)

Returns a list of decimals.

distinctWithNull(<listString>)

Returns a list of strings.

distinctWithNull(<listDateTimeOnly>)

Returns a list of datetimes without considering time zone.

distinctWithNull(<listDateTime>)

Returns a list of datetimes.

distinctWithNull(<listDateOnly>)

Returns a list of dates.

distinctWithNull(<listBoolean>)

Returns a list of booleans.

distinctWithNull(<listDuration>)

Returns a list of durations.

Examples
distinctWithNull([10,2,10,null])

Returns [10, 2, null]

**Note:** The parameter <listObject> is not supported in this function.

## filter filter

Returns a listObject with objects having the key attribute matching one of the given key values.

Syntax
filter(<parameters>)
Parameters
| table 0-row-3 1-row-3 2-row-3 3-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToFilter | listObject | list of objects, to be filtered. It must be a field reference. |
| keyAttributeName | string | attribute name in the objects of the given list, used as key for filtering |
| keyValueList | list | array of key values for filtering |

Signatures and returned types
filter(listObject, string, listString)

filter(listObject, string, listInteger)

filter(listObject, string, listDecimal)

filter(listObject, string, listDateTime)

filter(listObject, string, listDateTimeOnly)

filter(listObject, string, listDateOnly)

filter(listObject, string, listDuration)

filter(listObject, string, listBoolean)

Returns a listObject.

Examples
Here is an example of a payload passed in an incoming event “myevent”:

| code language-json |
| --- |
| "productListItems": [{ "id": "product1", "name": "the product 1", "price": 20 },{ "id": "product2", "name": "the product 2", "price": 30 },{ "id": "product3", "name": "the product 3", "price": 50 }] |

You can use the following expression:

| code language-json |
| --- |
| filter( @event{myevent.productListItems}, "id", ["product2", "product3", "product4"] ) |

Returns a listObject containing the two objects with “product2” and “product3” as id.

## getListItem getListItem

Returns the item of the list at the given index.

Syntax
getListItem(<parameters>)
Parameters
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 |  |
| --- | --- |
| Parameter | Type |
| list | listString |
| list | listBoolean |
| list | listInteger |
| list | listDecimal |
| list | listDuration |
| list | listDateTime |
| list | listDateTimeOnly |
| list | listDateOnly |
| index | integer |

Signatures and returned type
getListItem(<listInteger>,<index>)

Returns an integer.

getListItem(<listDecimal>,<index>)

Returns a decimal.

getListItem(<listString>,<index>)

Returns a string.

getListItem(<listDateTimeOnly>,<index>)

Returns a datetime without considering time zone.

getListItem(<listDateTime>,<index>)

Returns a datetime.

getListItem(<listDateOnly>,<index>)

Returns a list of dates.

getListItem(<listBoolean>,<index>)

Returns a boolean.

getListItem(<listDuration>,<index>)

Returns a duration.

Examples
getListItem([10, 2, 3], 1)

Returns “2”

getListItem(["A", "B", "C"], 2)

Returns “C”

Examples with an event field ‘event.appVersion’ with value: “20.45.2.3434”

split(@event{event.appVersion}, "\\.")

Returns ["20", "45", "2", "3434"]

getListItem(split(@event{event.appVersion}, "\\."), 0)

Returns “20”

## in in

Checks if the first argument value is in the list. The check is performed through an Equal on each argument value. It returns true if the argument value is found, false otherwise.

The type of the <expression> must match with items of the list. Types of items of the list, as a reminder, must match with each other.

Syntax
in(<parameters>)
Parameters
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 |  |
| --- | --- |
| Parameter | Type |
| String | String |
| Boolean | Boolean |
| Integer | Integer |
| Decimal | Decimal |
| Duration | Duration |
| DateTime | DateTime |
| DateTimeOnly | DateTimeOnly |
| List | listString |
| List | listBoolean |
| List | listInteger |
| List | listDecimal |
| List | listDuration |
| List | listDateTime |
| List | listDateTimeOnly |
| List | listDateOnly |

Signature and returned type
in(<integer>,<listInteger>)

in(<decimal>,<listDecimal>)

in(<string>,<listString>)

in(<boolean>,<listBoolean>)

in(<dateTimeOnly>,<listDateTimeOnly>)

in(<dateTime>,<listDateTime>)

in(<dateOnly>,<listDateOnly>)

in(<duration>,<listDuration>)

Return a boolean.

Examples
in(4,[4,5,3,4])

Returns true.

in(8,[4,5,3,4])

Returns false.

in(#{ExperiencePlatform.ProfileFieldGroup.profile.person.gender}, ["male"])

## intersect intersect

Returns the common values in the two input lists. If one of the two lists is null, returns an empty list.

Syntax
intersect(<parameters>)
Parameters
| table 0-row-2 1-row-2 2-row-2 |  |
| --- | --- |
| Parameter | Type |
| list 1 | list |
| list 2 | list |

Signatures and returned types
intersect(listString,listString): listString

intersect(listDecimal,listDecimal): listDecimal

intersect(listInteger,listInteger): listInteger

intersect(listDateTime,listDateTime): listDateTime

intersect(listDateTimeOnly,listDateTimeOnly): listDateTimeOnly

intersect(listDateOnly,listDateOnly): listDateOnly

intersect(listDuration,listDuration): listDuration

intersect(listBoolean,listBoolean): listBoolean

Returns a list.

Examples
| code language-json |
| --- |
| intersect( ["sports", "news", "documentary"], ["sports", "movies", "documentary"] ) |

Returns [“sports”, “news”]

| code language-json |
| --- |
| intersect( #{ExperienceDataPlatform.profile.interests}, ["sports", "documentary"] ) |

Returns common items between profile attributes and given list of categories.

| code language-json |
| --- |
| intersect( #{ExperienceDataPlatform.profile.interests}, @event{myEvent.sport_interests} ) |

Returns common items between profile attributes and given event field.

## limit limit

Returns the first or last N elements of a list.

Syntax
limit(<parameters>)
Parameters
| table 0-row-3 1-row-3 2-row-3 3-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to consider. For listObject, it must be a field reference. |
| numberOfItems | integer | Number of items to be returned from the given list. |
| firstOrLastItems | boolean | This parameter is optional (true by default). true returns the first items. false returns the last items. |

Signature and returned type
limit(<listString>,<integer>)

limit(<listString>,<integer>,<boolean>)

Returns a list of strings.

limit(<listInteger>,<integer>)

limit(<listInteger>,<integer>,<boolean>)

Returns a list of integers.

limit(<listDecimal>,<integer>)

limit(<listDecimal>,<integer>,<boolean>)

Returns a list of decimals.

limit(<listBoolean>,<integer>)

limit(<listBoolean>,<integer>,<boolean>)

Returns a list of booleans.

limit(<listDateOnly>,<integer>)

limit(<listDateOnly>,<integer>,<boolean>)

Returns a list of dates.

limit(<listDateTimeOnly>,<integer>)

limit(<listDateTimeOnly>,<integer>,<boolean>)

Returns a list of datetimes without considering time zone.

limit(<listDateTime>,integer>)

limit(<listDateTime>,<integer>,<boolean>)

Returns a list of datetimes.

limit(<listDuration>,<integer>)

limit(<listDuration>,<integer>,<boolean>)

Returns a list of durations.

limit(<listObject>,<integer>)

limit(<listObject>,<integer>,<boolean>)

Returns a list of objects.

Examples
limit(["A", "B", "C", "D", "E"], 3)

Returns ["A","B","C"].

limit(["A", "B", "C", "D", "E"], 3, false)

Returns ["C","D","E"].

## listSize listSize

Counts the number of elements in the list.

Syntax
listSize(<parameters>)
Parameters
| table 0-row-3 1-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to process. For listObject, it must be a field reference. A listObject cannot contain null object. |

Signatures and returned type
listSize(<listInteger>)

listSize(<listDecimal>)

listSize(<listString>)

listSize(<listBoolean>)

listSize(<listDateTimeOnly>)

listSize(<listDateTime>)

listSize(<listDateOnly>)

listSize(<listDuration>)

Return an integer.

listSize(<listObject>)

Examples
listSize([10,2,3])

Returns 3.

listSize(@event{my_event.productListItems})

Returns the number of objects in the given array of objects (listObject type).

## serializeList serializeList

Converts a given list (any type except listObject) into a string.

Syntax
serializeList(<parameters>)
Parameters
| table 0-row-3 1-row-3 2-row-3 3-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToProcess | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly | List to convert into a string. |
| separator | string | Separator between each list element in the output string. |
| addQuotes | boolean | This parameter indicates if each element in the output string should include quotes (true) or not (false). |

Signature and returned type
serializeList(<listInteger>,<string>,<boolean>)

serializeList(<listDecimal>,<string>,<boolean>)

serializeList(<listString>,<string>,<boolean>)

serializeList(<listBoolean>,<string>,<boolean>)

serializeList(<listDateTimeOnly>,<string>,<boolean>)

serializeList(<listDateTime>,<string>,<boolean>)

serializeList(<listDateOnly>,<string>,<boolean>)

serializeList(<listDuration>,<string>,<boolean>)

Return a string.

Examples
serializeList(["Hello","World"], " ", false)

Returns “Hello World”.

serializeList(["Hello", "World"], ",", true)

Returns ““Hello”,“World””.

## sort sort

Sorts a list of values or objects in the natural order.

Syntax
sort(<parameters>)
Parameters
| table 0-row-3 1-row-3 2-row-3 3-row-3 |  |  |
| --- | --- | --- |
| Parameter | Type | Description |
| listToSort | listString, listBoolean, listInteger, listDecimal, listDuration, listDateTime, listDateTimeOnly, listDateOnly, or listObject | List to sort out. For listObject, it must be a field reference. |
| keyAttributeName | string | This parameter is only for listObject. The attribute name in the objects of the given list is used as key for sorting. |
| sortingOrder | boolean | Ascending (true) or descending (false) |

Signature and returned type
sort(<listInteger>,<boolean>)

Returns a list of integers.

sort(<listDecimal>,<boolean>)

Returns a list of decimals.

sort(<listString>,<boolean>)

Returns a list of strings.

sort(<listDateTimeOnly>,<boolean>)

Returns a list of datetimes without considering time zone.

sort(<listDateTime>,<boolean>)

Returns a list of datetimes.

sort(<listDateOnly>,<boolean>)

Returns a list of dates.

sort(<listBoolean>,<boolean>)

Returns a list of booleans.

sort(<listObject>,<string>,<boolean>)

Returns a list of objects.

Examples
sort(["A", "C", "B"], true)

Returns ["A","B","C"].

sort([1, 3, 2], false)

Returns [3, 2, 1].

sort(@event{my_event.productListItems}, "SKU", true)

Returns the listObject ordered by SKU attribute (ascending order)

recommendation-more-help
