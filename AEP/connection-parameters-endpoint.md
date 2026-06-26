---
title: "Connection parameters endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/query/api/connection-parameters"
category: "reference"
topic: "experience-platform/query-service-guide"
created_at: "2026-05-29T17:04:18.337372+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Query Service Guide

# Connection parameters endpoint

Last update: May 23, 2026
- Topics:
- [Queries](#)

CREATED FOR:

- Developer

## Sample API call

The following section walks you through the API call you can make using the Query Service API. The call includes the general API format, a sample request showing required headers, and a sample response.

### Request connection parameters

You can retrieve your connection parameters by making a GET request to the /connection_parameters endpoint. For more information about clients that use connection parameters to connect via the interactive service, please read the documentation on [Query Service clients](/en/docs/experience-platform/query/clients/overview).

**API format**

```
GET /connection_parameters
```

**Request**

```
curl -X GET https://platform.adobe.io/data/foundation/query/connection_parameters
 -H 'Authorization: Bearer {ACCESS_TOKEN}' \
 -H 'x-gw-ims-org-id: {ORG_ID}' \
 -H 'x-api-key: {API_KEY}' \
 -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

A successful response returns HTTP status 200 with your connection parameters.

```
{
    "username": "{USERNAME}",
    "dbName": "prod:all",
    "host": "{HOSTNAME}",
    "version": 1,
    "port": 80,
    "token": "{TOKEN}",
    "compressedToken": "{COMPRESSED_TOKEN}",
    "websocketHost": "{WEBSOCKET_HOSTNAME}"
}
```

recommendation-more-help
