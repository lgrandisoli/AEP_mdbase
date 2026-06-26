---
title: "Use custom actions use-custom-actions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-custom-actions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:06.234456+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use custom actions use-custom-actions

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Actions](#)
- [Custom Actions](#)

CREATED FOR:

- Intermediate
- User
- Developer

Use custom actions to enable connection to a third-party system to send messages or API calls. An action can be configured with any service from any provider that can be called through a REST API with a JSON-formatted payload.

Learn more about custom actions in [this section](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action).

Learn how to create and configure a custom action on [this page](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration).

Learn how to use API call responses from custom actions for personalization on [this page](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response).

## Consent and data governance privacy

In Journey Optimizer, you can apply data governance and consent policies to your custom actions to prevent specific fields from being exported to third-party systems or exclude customers who have not consented to receive email, push or SMS communication. For more information, refer to the following pages:

- [Data governance](/en/docs/journey-optimizer/using/privacy/action-privacy).
- [Consent](/en/docs/journey-optimizer/using/privacy/consent/consent).

## URL configuration

The configuration pane of the **Custom action** activity shows the URL configuration parameters and the authentication parameters that are configured for the custom action. You cannot set up the static part of the URL in the journey, but in the global configuration of the custom action. [Learn more](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration).

### Dynamic path

If the URL includes a dynamic path, specify the path in the **Path** field.

To concatenate fields and plain text strings, use the String functions or the Plus sign (+) in the advanced expression editor. Enclose plain text strings in single quotation marks (') or in double quotation marks ("). [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced).

This table shows an example of configuration:

Field
Value
URL
https://xxx.yyy.com:8080/somethingstatic/
Path
The _id + '/messages'
The concatenated URL has this form:

https://xxx.yyy.com:8080/somethingstatic/<ID>/messages

### Headers and query parameters headers

The **URL Configuration** section shows the dynamic header and query parameter fields, but not the constant fields. Dynamic header and query parameter fields are defined as variable in the action configuration screen. [Learn more](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration#url-configuration)

To specify the value of dynamic header and query parameter fields, click inside the field or on the pencil icon and select the desired field.

## Action parameters

In the **Action parameters** section, you’ll see the message parameters defined as *“Variable”*. For these parameters, you can define where to get this information (example: events, data sources), pass values manually or use the advanced expression editor for advanced use cases. Advanced uses cases can be data manipulation and other function usage. Refer to this [page](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced).

recommendation-more-help
