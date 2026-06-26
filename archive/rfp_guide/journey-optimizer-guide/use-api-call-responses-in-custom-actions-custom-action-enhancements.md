---
title: "Use API call responses in custom actions custom-action-enhancements"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:54.409242+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use API call responses in custom actions custom-action-enhancements

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Actions](#)
- [Custom Actions](#)

CREATED FOR:

- Experienced
- Developer
- Admin

You can leverage API call responses in custom actions and orchestrate your journeys based on these responses.

## Important notes custom-action-enhancements-notes

- Scalar arrays are supported in response payload: code language-none "dummyScalarArray": [ "val1", "val2" ]
- Heterogeneous arrays are not supported in response payload: code language-none "dummyRandomArray": [ 20, "aafw", false ]

## Configure the custom action config-response

- Create the custom action. Refer to this page .
- Click inside the Response (success response) field. {align="left" width="80%"}
- Paste an example of the payload returned by the call. Verify that the field types are correct (string, integer, etc.). Here is an example of response payload captured during the call. Our local endpoint sends the number of loyalty points and the status of a profile. code language-none { "customerID" : "xY12hye", "status":"gold", "points": 1290 } {align="left" width="80%"} Each time the API is called, the system will retrieve all the fields included in the payload example.
- (Optional) Enable an error response payload to capture the format returned when the call fails, then paste an example payload. To do this, select Define a failure response payload in the custom action configuration. Learn more about configuring the payload fields in Configure a custom action . code language-none { "errorResponse" : "customer not found" } The error response payload is only available if you enable it in the custom action configuration.
- Let’s also add the customerID as a query parameter. {align="left" width="80%"}
- Click Save .

## Leverage the response in a journey response-in-journey

Simply add the custom action to a journey. You can then leverage the response payload fields in conditions, other actions and message personalization.

If you have defined an error response payload, it is exposed under **Contextual attributes** > **Journey Orchestration** > **Actions** > <action name> > **errorResponse**. You can use it in the timeout and error branch to drive fallback logic and error handling.

For example, you can add a condition to check the number of loyalty points. When the person enters the restaurant, your local endpoint sends a call with the profile’s loyalty information. You can send a push if the profile is a gold customer. And if an error is detected in the call, send a custom action to notify your system administrator.

- Add your event and the Loyalty custom action created earlier.
- In the Loyalty custom action, map the customer ID query parameter with the profile ID. Check the option Add an alternative path in case of a timeout or error .
- In the first branch, add a condition and use the advanced editor to leverage the action response fields, under the Context node.
- Then add your push, and personalize your message using the response fields. In our example, we personalize the content using the number of loyalty points and the customer status. The action response fields are available under Contextual attributes > Journey Orchestration > Actions . note NOTE Each profile entering the custom action will trigger a call. Even if the response is always the same, Journey will still perform one call per profile.
- In the timeout and error branch, add a condition and leverage the built-in jo_status_code field. In our example, we’re using the http_400 error type. See this section . code language-none @action{ActionLoyalty.jo_status_code} == "http_400" If an error response payload has been defined, you can also target its fields, for example: code language-none @action{ActionLoyalty.errorResponse.errorResponse} == "customer not found"
- Add a custom action that will be sent to your organization.

## Test mode logs test-mode-logs

You can access, through test mode, status logs related to custom action responses. If you have defined custom actions with responses in your journey, you will see an **actionsHistory** section on those logs displaying the payload returned by the external endpoint (as a response from that custom action). When an error response payload is defined, it is included for failed calls. This can be very useful in terms of debugging.

## Error status error-status

The **jo_status_code** field is always available even when no response payload is defined.

Here are the possible values for this field:

- http status code: http_<HTTP API call returned code>, for instance http_200 or http_400
- timeout error: **timedout**
- capping error: **capped**
- internal error: **internalError**

An action call is considered in error when the returned http code is greater than 2xx or if an error occurs. The journey flows to the dedicated timeout or error branch in such cases.

If an error response payload has been configured for the custom action, its fields are exposed under the **errorResponse** node for failed calls. If no error response payload is configured, that node is not available.

WARNING
Only newly created custom actions include the
jo_status_code
field out-of-the-box. If you want to use it with an existing custom action, you need to update the action. For example, you can update the description and save.
## Expression syntax exp-syntax

Here is the syntax:

```
#@action{myAction.myField}
```

Here are a few examples:

```
 // action response field
 @action{<action name>.<path to the field>}
 @action{ActionLoyalty.status}
```

```
 // action response field
 @action{<action name>.<path to the field>, defaultValue: <default value expression>}
 @action{ActionLoyalty.points, defaultValue: 0}
 @action{ActionLoyalty.points, defaultValue: @event{myEvent.newPoints}}
```

While manipulating collections in a custom action response, you can rely on currentActionField to access the current item:

```
count(
@action{MyAction.MyCollection.all(
currentActionField.description == "abc"
)}
)
```

### Using custom action responses in native channels response-in-channels

Response payload fields from custom actions can be used in native channels (email, push, SMS) for message personalization. This includes the ability to iterate over arrays and nested data structures returned by external APIs.

For detailed examples and syntax for iterating over custom action response data in messages, refer to [Iterate over contextual data with Handlebars](/en/docs/journey-optimizer/using/content-management/personalization/iterate-contextual-data#custom-action-responses).

## Additional resources

For more information, refer to these pages:

- [Field references](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/field-references).
- [Collection management functions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/collection-management-functions)

recommendation-more-help
