---
title: "List available identity namespaces"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/identity/api/list-namespaces"
category: "reference"
topic: "experience-platform/experience-platform-identity-service-guide"
created_at: "2026-06-26T17:38:43.977716+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform Identity Service Guide

# List available identity namespaces

Last update: June 18, 2026
- Topics:
- [Identities](#)

CREATED FOR:

- Developer

**API format**

```
GET /idnamespace/identities
```

**Request**

```
curl -X GET \
  'https://platform-va7.adobe.io/data/core/idnamespace/identities' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

The response includes an array of objects, with each object representing an available namespace. Namespaces with a “custom” value of “false” are standard namespaces, while those with a “custom” value of “true” are namespaces that your organization has created.

NOTE
This response has been truncated for space.
```
[
  {
        "updateTime": 1441122419000,
        "code": "CORE",
        "status": "ACTIVE",
        "description": "CORE Namespace",
        "id": 0,
        "createTime": 1441122419000,
        "idType": "COOKIE",
        "name": "CORE",
        "custom": false
    },
    {
        "updateTime": 1495153678000,
        "code": "ECID",
        "status": "ACTIVE",
        "description": "ECID Namespace",
        "id": 4,
        "createTime": 1495153678000,
        "idType": "COOKIE",
        "name": "ECID",
        "custom": false
    },
    {
        "updateTime": 1522783145000,
        "code": "AdCloud",
        "status": "ACTIVE",
        "description": "Adobe AdCloud - ID Syncing Partner",
        "id": 411,
        "createTime": 1522783145000,
        "idType": "COOKIE",
        "name": "AdCloud",
        "custom": false
    }
]
```

## Next steps

Proceed to the next tutorial to [create a custom namespace](/en/docs/experience-platform/identity/api/create-custom-namespace)

recommendation-more-help
