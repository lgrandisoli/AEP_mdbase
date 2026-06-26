---
title: "Hosts endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/endpoints/hosts"
category: "reference"
topic: "experience-platform/tags"
created_at: "2026-05-29T17:09:53.363519+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Tags

# Hosts endpoint

Last update: May 23, 2026
- Topics:
- [Tags](#)

CREATED FOR:

- Developer

NOTE
This document covers how to manage hosts in the Reactor API. For more general information on hosts for tags, see the guide on
hosts overview
in the publishing documentation.
In the Reactor API, a host defines a destination where a [build](/en/docs/experience-platform/tags/api/endpoints/builds) can be delivered.

When a build is requested by a tags user in Adobe Experience Platform, the system checks the Library to determine which [environment](/en/docs/experience-platform/tags/api/endpoints/environments) the library should be built to. Each environment has a relationship with a host, indicating where to deliver the build.

A host belongs to exactly one [property](/en/docs/experience-platform/tags/api/endpoints/properties), while a property can have many hosts. A property must have at least one host before you can publish.

A host can be used by more than one environment within a property. It is common to have a single host on a property, and have all environments on that property use the same host.

## Getting started

The endpoint used in this guide is part of the [Reactor API](https://www.adobe.io/experience-platform-apis/references/reactor/). Before continuing, please review the [getting started guide](/en/docs/experience-platform/tags/api/getting-started) for important information regarding how to authenticate to the API.

## Retrieve a list of hosts list

You can retrieve a list of hosts for a property by including the property’s ID in the path of a GET request.

**API format**

```
GET /properties/{PROPERTY_ID}/hosts
```

Parameter
Description
PROPERTY_ID
The
id
of the property that owns the hosts.
NOTE
Using query parameters, listed hosts can be filtered based on the following attributes:
- created_at
- name
- type_of
- updated_at

filtering responses
**Request**

```
curl -X GET \
  https://reactor.adobe.io/properties/PRd428c2a25caa4b32af61495f5809b737/hosts \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H "Content-Type: application/vnd.api+json" \
  -H 'Accept: application/vnd.api+json;revision=1'
```

**Response**

A successful response returns a list of hosts for the specified property.

```
{
  "data": [
    {
      "id": "HT405b8d9306004eb38106e66c8a4afc09",
      "type": "hosts",
      "attributes": {
        "created_at": "2020-12-14T17:42:35.239Z",
        "server": null,
        "name": "Example Akamai Host",
        "path": null,
        "port": null,
        "status": "succeeded",
        "type_of": "akamai",
        "updated_at": "2020-12-14T17:42:35.239Z",
        "username": null
      },
      "relationships": {
        "property": {
          "links": {
            "related": "https://reactor.adobe.io/hosts/HT405b8d9306004eb38106e66c8a4afc09/property"
          },
          "data": {
            "id": "PRd428c2a25caa4b32af61495f5809b737",
            "type": "properties"
          }
        }
      },
      "links": {
        "property": "https://reactor.adobe.io/properties/PRd428c2a25caa4b32af61495f5809b737",
        "self": "https://reactor.adobe.io/hosts/HT405b8d9306004eb38106e66c8a4afc09"
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

## Look up a host lookup

You can look up a host by providing its ID in the path of a GET request.

**API format**

```
GET /hosts/{HOST_ID}
```

Parameter
Description
HOST_ID
The
id
of the host that you want to look up.
**Request**

```
curl -X GET \
  https://reactor.adobe.io/hosts/HT5d90148e72224224aac9bc0b01498b84 \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H "Content-Type: application/vnd.api+json" \
  -H 'Accept: application/vnd.api+json;revision=1'
```

**Response**

A successful response returns the details of the host.

```
{
  "data": {
    "id": "HT5d90148e72224224aac9bc0b01498b84",
    "type": "hosts",
    "attributes": {
      "created_at": "2020-12-14T17:42:25.353Z",
      "server": "https://server.example.com",
      "name": "Example Akamai Host",
      "path": "/akamai",
      "port": 8000,
      "status": "succeeded",
      "type_of": "akamai",
      "updated_at": "2020-12-14T17:42:25.353Z",
      "username": null
    },
    "relationships": {
      "property": {
        "links": {
          "related": "https://reactor.adobe.io/hosts/HT5d90148e72224224aac9bc0b01498b84/property"
        },
        "data": {
          "id": "PRd7cf174259f34057b5c435ef873a79bf",
          "type": "properties"
        }
      }
    },
    "links": {
      "property": "https://reactor.adobe.io/properties/PRd7cf174259f34057b5c435ef873a79bf",
      "self": "https://reactor.adobe.io/hosts/HT5d90148e72224224aac9bc0b01498b84"
    }
  }
}
```

## Create a host create

You can create a new host by making a POST request.

**API format**

```
POST /properties/{PROPERTY_ID}/hosts
```

Parameter
Description
PROPERTY_ID
The
id
of the
property
that you are defining the host under.
**Request**

The following request creates a new host for the specified property. The call also associates the host with an existing extension through the relationships property. See the guide on [relationships](/en/docs/experience-platform/tags/api/guides/relationships) for more information.

```
curl -X POST \
  https://reactor.adobe.io/properties/PRb25a704c0b7c4562835ccdf96d3afd31/hosts \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'Content-Type: application/json' \
  -d '{
        "data": {
          "attributes": {
            "name": "Example SFTP Host",
            "type_of": "sftp",
            "username": "John Doe",
            "encrypted_private_key": "{PRIVATE_KEY}",
            "server": "https://example.com",
            "skip_symlinks": true,
            "path": "assets",
            "port": 22
          },
          "type": "hosts"
        }
      }'
```

Property
Description
attributes.name
(Required)
A human-readable name for the host.
attributes.type_of
**(Required)** The type of host. Can be one of two options:

- akamai for [Adobe-managed hosts](/en/docs/experience-platform/tags/publish/hosts/managed-by-adobe-host)
- sftp for [SFTP hosts](/en/docs/experience-platform/tags/publish/hosts/sftp-host)

attributes.encrypted_private_key
An optional private key to be used for host authentication.
attributes.path
The path to append to the
server
URL.
attributes.port
An integer indicating the specific server port to be used.
attributes.server
The host URL for the server.
attributes.skip_symlinks
(For SFTP hosts only)
By default, all SFTP hosts use symbolic links (symlinks) to reference library builds that are saved to the server. However, not all servers support the use of symlinks. When this attribute is included and set to
true
, the host uses a copy operation to update the build assets directly instead of using symlinks.
attributes.username
An optional user name for authentication.
type
The type of resource being updated. For this endpoint, the value must be
hosts
.
**Response**

A successful response return the details of the newly created host.

```
{
  "data": {
    "id": "HT69bfe634dead4a9a8c659f5d4d94cecd",
    "type": "hosts",
    "attributes": {
      "created_at": "2020-12-14T17:42:07.033Z",
      "server": "//example.com",
      "name": "Example SFTP Host",
      "path": "assets",
      "port": 22,
      "status": "pending",
      "skip_symlinks": true,
      "type_of": "sftp",
      "updated_at": "2020-12-14T17:42:07.033Z",
      "username": "John Doe"
    },
    "relationships": {
      "property": {
        "links": {
          "related": "https://reactor.adobe.io/hosts/HT69bfe634dead4a9a8c659f5d4d94cecd/property"
        },
        "data": {
          "id": "PRb25a704c0b7c4562835ccdf96d3afd31",
          "type": "properties"
        }
      }
    },
    "links": {
      "property": "https://reactor.adobe.io/properties/PRb25a704c0b7c4562835ccdf96d3afd31",
      "self": "https://reactor.adobe.io/hosts/HT69bfe634dead4a9a8c659f5d4d94cecd"
    }
  }
}
```

## Update a host update

NOTE
Only SFTP hosts can be updated.
You can update a host by including its ID in the path of a PATCH request.

**API format**

```
PATCH /hosts/{HOST_ID}
```

Parameter
Description
HOST_ID
The
id
of the host that you want to update.
**Request**

The following request updates the name for an existing host.

```
curl -X PATCH \
  https://reactor.adobe.io/hosts/HT5d90148e72224224aac9bc0b01498b84 \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'Content-Type: application/json' \
  -d '{
        "data": {
          "attributes": {
            "name": "New host Name"
          },
          "id": "HT5d90148e72224224aac9bc0b01498b84",
          "type": "hosts"
        }
      }'
```

Property
Description
attributes
An object whose properties represent the attributes to be updated for the host. The following attributes can be updated for a host:

- encrypted_private_key
- name
- path
- port
- server
- type_of
- username

id
The
id
of the host you want to update. This should match the
{HOST_ID}
value provided in the request path.
type
The type of resource being updated. For this endpoint, the value must be
hosts
.
**Response**

A successful response returns the details of the updated host.

```
{
  "data": {
    "id": "HTb14e136a6fe147459b298a4645d2a6f5",
    "type": "hosts",
    "attributes": {
      "created_at": "2020-12-14T17:42:45.087Z",
      "server": null,
      "name": "My SFTP host",
      "path": null,
      "port": null,
      "status": "succeeded",
      "skip_symlinks": true,
      "type_of": "sftp",
      "updated_at": "2020-12-14T17:42:45.696Z",
      "username": null
    },
    "relationships": {
      "property": {
        "links": {
          "related": "https://reactor.adobe.io/hosts/HTb14e136a6fe147459b298a4645d2a6f5/property"
        },
        "data": {
          "id": "PR8f240526f7b54a4dbd46965e79519fde",
          "type": "properties"
        }
      }
    },
    "links": {
      "property": "https://reactor.adobe.io/properties/PR8f240526f7b54a4dbd46965e79519fde",
      "self": "https://reactor.adobe.io/hosts/HTb14e136a6fe147459b298a4645d2a6f5"
    }
  }
}
```

## Delete a host

You can delete a host by including its ID in the path of a DELETE request.

**API format**

```
DELETE /hosts/{HOST_ID}
```

Parameter
Description
HOST_ID
The
id
of the host that you want to delete.
**Request**

```
curl -X DELETE \
  https://reactor.adobe.io/hosts/HT5d90148e72224224aac9bc0b01498b84 \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}'
```

**Response**

A successful response returns HTTP status 204 (No Content) with no response body, indicating that the host has been deleted.

## Retrieve related resources for a host related

The following calls demonstrate how to retrieve the related resources for a host. When [looking up a host](#lookup), these relationships are listed under the relationships property.

See the [relationships guide](/en/docs/experience-platform/tags/api/guides/relationships) for more information on relationships in the Reactor API.

### Look up the related property for a host property

You can look up the property that owns a host by appending /property to the path of a lookup request.

**API format**

```
GET /hosts/{HOST_ID}/property
```

Parameter
Description
{HOST_ID}
The
id
of the host whose property you want to look up.
**Request**

```
curl -X GET \
  https://reactor.adobe.io/hosts/HT5d90148e72224224aac9bc0b01498b84/property \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H "Content-Type: application/vnd.api+json" \
  -H 'Accept: application/vnd.api+json;revision=1'
```

**Response**

A successful response returns the details of the specified host’s property.

```
{
  "data": {
    "id": "PRbdfaffb7bf374b87be50e672f0cf9309",
    "type": "properties",
    "attributes": {
      "created_at": "2020-12-14T17:52:05.900Z",
      "enabled": true,
      "name": "Kessel Example Property",
      "updated_at": "2020-12-14T17:52:05.900Z",
      "platform": "web",
      "development": false,
      "token": "47d65c7c98db",
      "domains": [
        "example.com"
      ],
      "undefined_vars_return_empty": false,
      "rule_component_sequencing_enabled": false
    },
    "relationships": {
      "company": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/company"
        },
        "data": {
          "id": "CO2bf094214ffd4785bb4bcf88c952a7c1",
          "type": "companies"
        }
      },
      "callbacks": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/callbacks"
        }
      },
      "hosts": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/hosts"
        }
      },
      "environments": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/environments"
        }
      },
      "libraries": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/libraries"
        }
      },
      "data_elements": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/data_elements"
        }
      },
      "extensions": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/extensions"
        }
      },
      "rules": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/rules"
        }
      },
      "notes": {
        "links": {
          "related": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/notes"
        }
      }
    },
    "links": {
      "company": "https://reactor.adobe.io/companies/CO2bf094214ffd4785bb4bcf88c952a7c1",
      "data_elements": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/data_elements",
      "environments": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/environments",
      "extensions": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/extensions",
      "rules": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309/rules",
      "self": "https://reactor.adobe.io/properties/PRbdfaffb7bf374b87be50e672f0cf9309"
    },
    "meta": {
      "rights": [
        "approve",
        "develop",
        "manage_environments",
        "manage_extensions",
        "publish"
      ]
    }
  }
}
```

recommendation-more-help
