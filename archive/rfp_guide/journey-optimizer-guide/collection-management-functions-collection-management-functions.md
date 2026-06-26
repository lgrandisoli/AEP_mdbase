---
title: "Collection management functions collection-management-functions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/collection-management-functions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:00.961557+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Collection management functions collection-management-functions

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)

CREATED FOR:

- Experienced
- Developer

## About query collection functions

The expression language also introduces a set of functions to query collections. These functions are explained below.

In the following examples, we use an event named “LobbyBeacon” containing a collection of push notification tokens. The examples on this page use the event payload structure shown below:

```
                {
   "_experience":{
      "campaign":{
         "message":{
            "profile":{
               "pushNotificationTokens":[
                  {
                     "token":"token_1",
                     "application":{
                        "_id":"APP1",
                        "name":"MarltonMobileApp",
                        "version":"1.0"
                     }
                  },
                  {
                     "token":"token_2",
                     "application":{
                        "_id":"APP2",
                        "name":"MarketplaceApp",
                        "version":"1.0"
                     }
                  },
                  {
                     "token":"token_3",
                     "application":{
                        "_id":"APP3",
                        "name":"VendorApp",
                        "version":"2.0"
                     }
                  }
               ]
            }
         }
      }
   },
   "timestamp":"1536160728"
}
```

NOTE
In the examples below, this payload is referenced using
@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens}
where “LobbyBeacon” is the event name and the rest of the path corresponds to the structure shown above.
## The all( <condition> ) function

The **all** function enables the definition of a filter on a given collection by using a boolean expression.

```
<listExpression>.all(<condition>)
```

**Conceptual example:** Among all the app users, you can get the ones using IOS 13 (boolean expression “app used == IOS 13”). The result of this function is the filtered list containing items matching the boolean expression (example: app user 1, app user 34, app user 432).

In a Data Source Condition activity you can check if the result of the **all** function is null or not. You can also combine this **all** function with other functions such as **count**. For more information, see [Data Source Condition activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions#data_source_condition).

**Code examples using the LobbyBeacon payload:**

The examples below use the event payload shown at the top of this page.

CAUTION
Using experience events in journey expressions/conditions is not supported. If your use case requires the use of experience events, consider alternative methods.
Learn more
### Example 1

We want to check if a user has installed a specific version of an application. For this we get all the push notification tokens associated with mobile applications for which the version is 1.0. Then, we perform a condition with the **count** function to check that the returned list of tokens contains at least one element.

```
count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all(currentEventField.application.version == "1.0").token}) > 0
```

The result is true.

### Example 2

Here we use the **count** function to check if there are push notification tokens in the collection.

```
count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.all().token}) > 0
```

The result is true.

```
count(@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.token})
```

The result of the expression is **3**.

NOTE
- When the filtering condition in the all() function is empty, the filter will return all the elements in the list. However, in order to count the number of elements of a collection, the all function is not required.
- currentEventField is only available when manipulating event collections, currentDataPackField when manipulating data source collections and currentActionField when manipulating custom action response collections.

When processing collections with
all
,
first
and
last
, we loop on each element of the collection one by one.
currentEventField
,
currentDataPackField
and
currentActionField
correspond to the element being looped.
## The first( <condition> ) and last( <condition> ) functions

The **first** and **last** functions also enable the definition of a filter on the collection while returning the first/last element of the list that meets the filter.

*<listExpression>.first(<condition>)*

*<listExpression>.last(<condition>)*

### Example 1

This expression returns the first push notification token associated with mobile applications for which the version is 1.0.

```
@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.first(currentEventField.application.version == "1.0").token}
```

The result is token_1.

### Example 2

This expression returns the last push notification token associated with mobile applications for which the version is 1.0.

```
@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.last(currentEventField.application.version == "1.0").token}
```

The result is token_2.

## The at( <index> ) function

The **at** function allows you to reference a specific element in a collection according to an index.Index 0 is the first index of the collection.

*<listExpression> .at( <index> )*

### Example

This expression returns the second push notification token of the list.

```
@event{LobbyBeacon._experience.campaign.message.profile.pushNotificationTokens.at(1).token}
```

The result is token_2.

recommendation-more-help
