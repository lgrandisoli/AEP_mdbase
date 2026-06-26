---
title: "App configurations endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/endpoints/app-configurations"
category: "reference"
topic: "tags/api/endpoints"
created_at: "2026-05-29T17:09:53.957177+00:00"
---
Breadcrumbs: Documentation > Tags

# App configurations endpoint

Last update: May 13, 2026
- Topics:
- [Tags](#)

CREATED FOR:

- Developer

WARNING
The implementation of the
/app_configurations
endpoint is in flux as features are added, removed, and reworked.
App configurations allow credentials to be stored and retrieved for later use. The /app_configurations endpoint in the Reactor API allows you to programmatically manage app configurations within your experience application.

## Getting started

The endpoint used in this guide is part of the [Reactor API](https://www.adobe.io/experience-platform-apis/references/reactor/). Before continuing, please review the [getting started guide](/en/docs/experience-platform/tags/api/getting-started) for important information regarding how to authenticate to the API.

## Retrieve a list of app configurations list

**API format**

```
GET /companies/{COMPANY_ID}/app_configurations
```

Parameter
Description
COMPANY_ID
The
id
of the
company
that owns the app configurations.
NOTE
Using query parameters, listed app configurations can be filtered based on the following attributes:
- app_id
- created_at
- key_type
- messaging_service
- name
- platform
- updated_at

filtering responses
**Request**

```
curl -X GET \
  https://reactor.adobe.io/companies/COdb0cd64ad4524440be94b8496416ec7d/app_configurations \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H "Content-Type: application/vnd.api+json" \
  -H 'Accept: application/vnd.api+json;revision=1'
```

**Response**

A successful response returns a list of app configurations.

```
{
  "data": [
    {
      "id": "AC40c339ab80d24c958b90d67b698602eb",
      "type": "app_configurations",
      "attributes": {
        "created_at": "2020-12-14T17:31:10.626Z",
        "updated_at": "2020-12-14T17:31:10.626Z",
        "app_id": "com.adobe.test_app",
        "name": "Kessel Apns App",
        "platform": "mobile",
        "messaging_service": "apns",
        "key_type": "p8_file"
      },
      "relationships": {
        "company": {
          "links": {
            "related": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb/company"
          },
          "data": {
            "id": "CO2bf094214ffd4785bb4bcf88c952a7c1",
            "type": "companies"
          }
        }
      },
      "links": {
        "company": "https://reactor.adobe.io/companies/CO2bf094214ffd4785bb4bcf88c952a7c1",
        "self": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb"
      }
    }
  ],
  "meta": {
    "pagination": {
      "current_page": 1,
      "next_page": null,
      "prev_page": null,
      "total_pages": 1,
      "total_count": 1
    }
  }
}
```

## Look up an app configuration lookup

You can look up an app configuration by providing its ID in the path of a GET request.

**API format**

```
GET /app_configurations/{APP_CONFIGURATION_ID}
```

Parameter
Description
APP_CONFIGURATION_ID
The
id
of the app configuration that you want to look up.
**Request**

```
curl -X GET \
  https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H "Content-Type: application/vnd.api+json" \
  -H 'Accept: application/vnd.api+json;revision=1'
```

**Response**

A successful response returns the details of the app configuration.

```
{
  "data": {
    "id": "AC40c339ab80d24c958b90d67b698602eb",
    "type": "app_configurations",
    "attributes": {
      "created_at": "2020-12-14T17:31:10.626Z",
      "updated_at": "2020-12-14T17:31:10.626Z",
      "app_id": "com.adobe.test_app",
      "name": "Kessel Apns App",
      "platform": "mobile",
      "messaging_service": "apns",
      "key_type": "p8_file"
    },
    "relationships": {
      "company": {
        "links": {
          "related": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb/company"
        },
        "data": {
          "id": "CO2bf094214ffd4785bb4bcf88c952a7c1",
          "type": "companies"
        }
      }
    },
    "links": {
      "company": "https://reactor.adobe.io/companies/CO2bf094214ffd4785bb4bcf88c952a7c1",
      "self": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb"
    }
  }
}
```

## Create an app configuration create

You can create a new app configuration by making a POST request.

**API format**

```
POST /companies/{COMPANY_ID}/app_configurations
```

Parameter
Description
COMPANY_ID
The
id
of the
company
that you are defining the app configuration under.
**Request**

```
curl -X POST \
  https://reactor.adobe.io/companies \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/vnd.api+json;revision=1' \
  -d '{
        "data": {
          "attributes": {
            "name": "Kessel Apns App",
            "app_id": "com.adobe.test_app",
            "platform": "mobile",
            "messaging_service": "apns",
            "key_type": "p8_file",
            "push_credential": {
              "bundleId": "com.adobe.test_app",
              "keyId": "{KEY_ID}",
              "p8": "{SECRET}",
              "teamId": "{TEAM_ID}"
            }
          },
          "type": "app_configurations"
        }
      }'
```

Property
Description
platform
The platform that the application runs on (web or mobile). This determines what messaging services are available.
messaging_service
The messaging service associated with the app, such as
Apple Push Notification service (APNs)
and
Firebase Cloud Messaging (FCM)
. This determines which key types can be used.
key_type
Represents the protocol that a push-service vendor supports and determines the format of the
push_credential
object. As protocols evolve for messaging services, new
key_type
values are created to support the updated protocols.
push_credential
The actual credential value, which is encrypted at rest. This field is not normally decrypted or included in API responses. Only certain Adobe services can get a response containing a decrypted push credential.
**Response**

A successful response return the details of the newly created app configuration.

```
{
  "data": {
    "id": "AC40c339ab80d24c958b90d67b698602eb",
    "type": "app_configurations",
    "attributes": {
      "created_at": "2020-12-14T17:31:10.626Z",
      "updated_at": "2020-12-14T17:31:10.626Z",
      "app_id": "com.adobe.test_app",
      "name": "Kessel Apns App",
      "platform": "mobile",
      "messaging_service": "apns",
      "key_type": "p8_file"
    },
    "relationships": {
      "company": {
        "links": {
          "related": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb/company"
        },
        "data": {
          "id": "CO2bf094214ffd4785bb4bcf88c952a7c1",
          "type": "companies"
        }
      }
    },
    "links": {
      "company": "https://reactor.adobe.io/companies/CO2bf094214ffd4785bb4bcf88c952a7c1",
      "self": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb"
    }
  }
}
```

## Update an app configuration

You can update an app configuration by including its ID in the path of a PATCH request.

**API format**

```
PATCH /app_configurations/{APP_CONFIGURATION_ID}
```

Parameter
Description
APP_CONFIGURATION_ID
The
id
of the app configuration that you want to update.
**Request**

The following request updates the app_id for an existing app configuration.

```
curl -X PATCH \
  https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/vnd.api+json;revision=1' \
  -d '{
        "data": {
          "attributes": {
            "app_id": "com.adobe.test_app_2"
          },
          "id": "AC40c339ab80d24c958b90d67b698602eb",
          "type": "app_configurations"
        }
      }'
```

Property
Description
attributes
An object whose properties represent the attributes to be updated for the app configuration. Each key represents the particular app configuration attribute to be updated, along with the corresponding value it should be updated to.The following attributes can be updated for app configurations:

- app_id
- key_type
- messaging_service
- name
- platform
- push_credential

id
The
id
of the app configuration you want to update. This should match the
{APP_CONFIGURATION_ID}
value provided in the request path.
type
The type of resource being updated. For this endpoint, the value must be
app_configurations
.
**Response**

A successful response returns the details of the updated app configuration.

```
{
  "data": {
    "id": "AC40c339ab80d24c958b90d67b698602eb",
    "type": "app_configurations",
    "attributes": {
      "created_at": "2020-12-14T17:31:10.626Z",
      "updated_at": "2020-12-14T17:31:21.787Z",
      "app_id": "com.adobe.test_app_2",
      "name": "Kessel Apns App",
      "platform": "mobile",
      "messaging_service": "apns",
      "key_type": "p8_file"
    },
    "relationships": {
      "company": {
        "links": {
          "related": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb/company"
        },
        "data": {
          "id": "CO2bf094214ffd4785bb4bcf88c952a7c1",
          "type": "companies"
        }
      }
    },
    "links": {
      "company": "https://reactor.adobe.io/companies/CO2bf094214ffd4785bb4bcf88c952a7c1",
      "self": "https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb"
    }
  }
}
```

## Delete an app configuration

You can delete an app configuration by including its ID in the path of a DELETE request.

**API format**

```
DELETE /app_configurations/{APP_CONFIGURATION_ID}
```

Parameter
Description
APP_CONFIGURATION_ID
The
id
of the app configuration that you want to delete.
**Request**

```
curl -X DELETE \
  https://reactor.adobe.io/app_configurations/AC40c339ab80d24c958b90d67b698602eb \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H "Content-Type: application/vnd.api+json" \
  -H 'Accept: application/vnd.api+json;revision=1'
```

**Response**

A successful response returns HTTP status 204 (No Content) with no response body, indicating that the app configuration has been deleted.

recommendation-more-help
