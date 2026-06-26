---
title: "Available sandboxes endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sandbox/api/available"
category: "reference"
topic: "experience-platform/sandboxes-guide"
created_at: "2026-05-29T17:00:18.600643+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Sandboxes Guide

# Available sandboxes endpoint

Last update: May 23, 2026
- Topics:
- [Sandboxes](#)

CREATED FOR:

- Developer

NOTE
Unlike other endpoints provided in the Sandbox API, this endpoint is available for all users, including those without Sandbox Administration access permissions.
You can list the sandboxes that are available for the current user by making a GET request to the available sandboxes endpoint.

**API format**

```
GET /{QUERY_PARAMS}
```

Parameter
Description
{QUERY_PARAMS}
Optional query parameters to filter results by. See the
appendix document
for a list of available parameters.
**Request**

```
curl -X GET \
  https://platform.adobe.io/data/foundation/sandbox-management/?limit=3&offset=1 \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}'
```

**Response**

A successful response returns a list of sandboxes that are available for the current user, including details such as name, title, state, and type.

```
{
    "sandboxes": [
        {
            "name": "prod",
            "title": "Production",
            "state": "active",
            "type": "production",
            "region": "VA7",
            "isDefault": true,
            "eTag": 2,
            "createdDate": "2019-09-04 04:57:24",
            "lastModifiedDate": "2019-09-04 04:57:24",
            "createdBy": "{USER_ID}",
            "modifiedBy": "{USER_ID}"
        },
        {
            "name": "dev",
            "title": "Development",
            "state": "active",
            "type": "development",
            "region": "VA7",
            "isDefault": false,
            "eTag": 1,
            "createdDate": "2019-09-03 22:27:48",
            "lastModifiedDate": "2019-09-03 22:27:48",
            "createdBy": "{USER_ID}",
            "modifiedBy": "{USER_ID}"
        },
        {
            "name": "stage",
            "title": "Staging",
            "state": "active",
            "type": "development",
            "region": "VA7",
            "isDefault": false,
            "eTag": 1,
            "createdDate": "2019-09-03 22:27:48",
            "lastModifiedDate": "2019-09-03 22:27:48",
            "createdBy": "{USER_ID}",
            "modifiedBy": "{USER_ID}"
        }
    ],
    "_page": {
        "limit": 3,
        "count": 1
    },
    "_links": {
        "page": {
            "href": "https://platform.adobe.io:443/data/foundation/sandbox-management/?limit={limit}&offset={offset}",
            "templated": true
        }
    }
}
```

Property
Description
name
The name of the sandbox. Used for lookup purposes in API calls.
title
The display name for the sandbox.
state
The current processing state of the sandbox. A sandbox’s state can be any of the following:

- creating: The sandbox has been created, but is still being provisioned by the system.
- active: The sandbox is created and active.
- failed: Due to an error, the sandbox was not able to be provisioned by the system and is disabled.
- deleted: The sandbox has been manually disabled.

type
The sandbox type, either “development” or “production”.
isDefault
A boolean property indicating whether this sandbox is the default production sandbox for the organization.
eTag
An identifier for a specific version of the sandbox. Used for version control and caching efficiency, this value is updated each time a change is made to the sandbox.
recommendation-more-help
