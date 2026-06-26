---
title: "Create a custom namespace in the Identity Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/identity/api/create-custom-namespace"
category: "reference"
topic: "experience-platform/experience-platform-identity-service-guide"
created_at: "2026-06-26T17:34:28.262235+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform Identity Service Guide

# Create a custom namespace in the Identity Service API

Last update: June 18, 2026
- Topics:
- [Identities](#)

CREATED FOR:

- Developer

Using the Identity Namespace API, you can create a custom identity namespace that will be available only to your organization.

For recommendations around creating custom namespaces, see [the Identity Service FAQ documentation](/en/docs/experience-platform/identity/troubleshooting-guide).

NOTE
Namespaces are a qualifier for identities. As such, once a namespace has been created, it cannot be deleted.
**API format**

```
POST /idnamespace/identities
```

**Request**

```
curl -X POST \
  https://platform-va7.adobe.io/data/core/idnamespace/identities \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -d '{
        "name": "Loyalty Member",
        "code": "Loyalty",
        "description": "Loyalty Program Member ID",
        "idType": "Cross_device"
      }'
```

**Response**

```
{
    "updateTime": 1576286879075,
    "code": "Loyalty",
    "status": "ACTIVE",
    "description": "Loyalty Program Member ID",
    "id": 10093197,
    "createTime": 1576286879075,
    "idType": "Cross_device",
    "name": "Loyalty Member",
    "custom": true
}
```

## Next steps

Proceed to the next tutorial to [list the native ID of an identity](/en/docs/experience-platform/identity/api/list-native-id)

recommendation-more-help
