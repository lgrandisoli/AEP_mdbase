---
title: "Get the native ID for an identity"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/identity/api/list-native-id"
category: "reference"
topic: "experience-platform/experience-platform-identity-service-guide"
created_at: "2026-05-29T17:05:58.957796+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform Identity Service Guide

# Get the native ID for an identity

Last update: May 13, 2026
- Topics:
- [Identities](#)

CREATED FOR:

- Developer

Identity data is typically provided as an ID string value and identity namespace in XDM data ingested, and when supplying an identity for use in an API call. When identities are persisted in Identity Service, an ID is generated and assigned to that identity, called the native XID. Experience Platform APIs requiring identity data support using this more compact form for the aggregated ID and namespace. XID is a base64 encoded string.

NOTE
This format is mainly for internal Adobe use. Native XID as a singular value is more space efficient and is what is used internally within Experience Platform solutions for storage and serialization. However it is not human readable, it is opaque, and requires a separate call to obtain it to use.
Acquire the XID for a given ID value and namespace using the service described in this section.

**API format**

```
GET https://platform-{REGION}.adobe.io/data/core/identity/identity?namespace={NAMESPACE}&id={ID_VALUE}
```

**Request**

```
curl -X GET \
  'https://platform-va7.adobe.io/data/core/identity/identity?namespace=email&id=test@adobetest.com' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

```
{
    "xid":"BVrqzwVuzbXrLfmnaG3rXrLf3KJg"
}
```

recommendation-more-help
