---
title: "Delete a dataflow using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/delete-dataflows"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:06:26.536050+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Delete a dataflow using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

You can delete batch and streaming dataflows that contain errors or have become obsolete using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

This tutorial covers the steps for deleting dataflows made with both batch and streaming sources using Flow Service.

## Getting started

This tutorial requires you to have a valid flow ID. If you do not have a valid flow ID, select your connector of choice from the [sources overview](/en/docs/experience-platform/sources/home) and follow the steps outlined before attempting this tutorial.

This tutorial also requires you to have a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Delete a dataflow

With an existing flow ID, you can delete a dataflow by performing a DELETE request to the Flow Service API.

**API format**

```
DELETE /flows/{FLOW_ID}
```

Parameter
Description
{FLOW_ID}
The unique
id
value for the dataflow you want to delete.
**Request**

```
curl -X DELETE \
    'https://platform.adobe.io/data/foundation/flowservice/flows/20c115bc-46e3-40f3-bfe9-fb25abe4ba76' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'x-api-key: {API_KEY}' \
    -H 'x-gw-ims-org-id: {ORG_ID}' \
    -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 204 (No Content) and a blank body. You can confirm the deletion by attempting a lookup (GET) request to the dataflow. The API will return an HTTP 404 (Not Found) error, indicating that the dataflow has been deleted.

## Next steps

By following this tutorial, you have successfully used the Flow Service API to to delete an existing dataflow.

For steps on how to perform these operations using the user interface, please refer to the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/delete)

recommendation-more-help
