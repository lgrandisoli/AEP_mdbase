---
title: "Sandbox Types endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sandbox/api/types"
category: "reference"
topic: "experience-platform/sandboxes-guide"
created_at: "2026-05-29T17:05:52.156564+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Sandboxes Guide

# Sandbox Types endpoint

Last update: May 23, 2026
- Topics:
- [Sandboxes](#)

CREATED FOR:

- Developer

You can retrieve a list of supported sandbox types for your organization by making a GET request to the /sandboxTypes endpoint.

## Getting started

The API endpoint used in this guide is part of the [Sandbox API](https://www.adobe.io/experience-platform-apis/references/sandbox). Before continuing, please review the [getting started guide](/en/docs/experience-platform/sandbox/api/getting-started) for links to related documentation, a guide to reading the sample API calls in this document, and important information regarding required headers that are needed to successfully make calls to any Experience Platform API.

## Retrieve a list of supported sandbox types

You can retrieve a list of supported sandbox types for your organization by making a GET request to the /sandboxTypes endpoint.

**API format**

```
GET /sandboxTypes
```

**Request**

```
curl -X GET \
  https://platform.adobe.io/data/foundation/sandbox-management/sandboxTypes \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
```

**Response**

A successful response returns a list of sandbox types that are supported for your organization.

```
{
    "sandboxTypes": [
        "production",
        "development"
    ]
}
```

recommendation-more-help
