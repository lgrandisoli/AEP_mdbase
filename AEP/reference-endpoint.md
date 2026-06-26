---
title: "Reference endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/access-control/api/permissions-and-resource-types"
category: "reference"
topic: "experience-platform/access-control-guide"
created_at: "2026-05-29T17:07:44.911688+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Access Control Guide

# Reference endpoint

Last update: May 13, 2026
- Topics:
- [Access Control](#)

CREATED FOR:

- Developer

NOTE
If a user token is being passed, then the user of the token must have an “org admin” role for the requested org.
You can list the names of all permissions and resource types by making a GET request to the /acl/reference endpoint. These names can then be used in API calls to [view effective access control policies](/en/docs/experience-platform/access-control/api/effective-policies) for the current user.

A permission is a policy that is managed through the Adobe Admin Console, and maps to zero or more resource-type policies. A resource type is a policy that enables read, write, and/or delete capabilities for a specific type of Experience Platform resource (such as datasets or schemas).

**API format**

```
GET /acl/reference
```

**Request**

```
curl -X GET \
  https://platform.adobe.io/data/foundation/access-control/acl/reference \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}'
```

**Response**

A successful response returns a permissions object and a resource-types object, each containing a full list of names for access permissions or resource types, respectively.

```
{
  "permissions": {
    "export-audience-for-segment": {
      "segments": [
        "read"
      ]
    },
    "manage-datasets": {
      "connection": [
        "read",
        "write",
        "delete"
      ],
      "datasets": [
        "read",
        "write",
        "delete"
      ]
    }
    {"..."}
  },
  "resource-types": {
    "classes": [
      "read",
      "write",
      "delete"
    ],
    "connection": [
      "read",
      "write",
      "delete"
    ],
    "data-types": [
      "read",
      "write",
      "delete"
    ],
    "...": [
      "..."
    ]
  }
}
```

recommendation-more-help
