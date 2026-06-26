---
title: "Delete a destination dataflow using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/destinations/api/delete-destination-dataflow"
category: "reference"
topic: "experience-platform/destinations-guide"
created_at: "2026-05-29T17:10:15.596925+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Destinations Guide

# Delete a destination dataflow using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Destinations](#)

CREATED FOR:

- Admin
- User

You can delete dataflows that contain errors or have become obsolete using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

This tutorial covers the steps for deleting dataflows to both batch and streaming destinations using Flow Service.

## Getting started get-started

This tutorial requires you to have a valid flow ID. If you do not have a valid flow ID, select your destination of choice from the [destinations catalog](/en/docs/experience-platform/destinations/catalog/overview) and follow the steps outlined to [connect to the destination](/en/docs/experience-platform/destinations/ui/connect-destination) and [activate data](/en/docs/experience-platform/destinations/ui/activate/activation-overview) before attempting this tutorial.

This tutorial also requires you to have a working understanding of the following components of Adobe Experience Platform:

- [Destinations](/en/docs/experience-platform/destinations/home): Destinations are pre-built integrations with destination platforms that allow for the seamless activation of data from Adobe Experience Platform. You can use destinations to activate your known and unknown data for cross-channel marketing campaigns, email campaigns, targeted advertising, and many other use cases.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know to successfully delete a dataflow using the Flow Service API.

### Reading sample API calls reading-sample-api-calls

This tutorial provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

### Gather values for required headers gather-values-for-required-headers

To make calls to Experience Platform APIs, you must first complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform, including those belonging to Flow Service, are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

NOTE
If the
x-sandbox-name
header is not specified, requests are resolved under the
prod
sandbox.
All requests that contain a payload (POST, PUT, PATCH) require an additional media type header:

- Content-Type: application/json

## Delete a destination dataflow delete-destination-dataflow

With an existing flow ID, you can delete a destination dataflow by performing a DELETE request to the Flow Service API.

**API format**

```
DELETE /flows/{FLOW_ID}
```

Parameter
Description
{FLOW_ID}
The unique
id
value for the destination dataflow you want to delete.
**Request**

```
curl -X DELETE \
    'https://platform.adobe.io/data/foundation/flowservice/flows/455fa81b-f290-4222-94b6-540a73e3fbc2' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 202 (No Content) and a blank body. You can confirm the deletion by attempting a lookup (GET) request to the dataflow. The API will return an HTTP 404 (Not Found) error, indicating that the dataflow has been deleted.

## API error handling api-error-handling

The API endpoints in this tutorial follow the general Experience Platform API error message principles. See [API status codes](/en/docs/experience-platform/landing/troubleshooting#api-status-codes) and [request header errors](/en/docs/experience-platform/landing/troubleshooting#request-header-errors) in the Experience Platform troubleshooting guide for more information on interpreting error responses.

## Next steps next-steps

You have successfully used the Flow Service API to delete an existing dataflow to a destination.

For steps on how to perform these operations using the user interface, refer to the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/destinations/ui/delete-destinations).

You can now go on and [delete destination accounts](/en/docs/experience-platform/destinations/api/delete-destination-account) using the Flow Service API.

recommendation-more-help
