---
title: "Relationships in the Reactor API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/guides/relationships"
category: "guides"
topic: "experience-platform/tags"
created_at: "2026-05-29T17:08:47.053283+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Tags

# Relationships in the Reactor API

Last update: May 23, 2026
- Topics:
- [Tags](#)

CREATED FOR:

- Developer

Resources in the Reactor API are often related to each other. This document provides an overview of how resource relationships are established in the API, and the relationship requirements of each resource type.

Depending on the type of resource in question, some relationships are required. A required relationship implies that the parent resource cannot exist without the relationship. All other relationships are optional.

Regardless of whether they are required or optional, relationships are either automatically established by the system when relevant resources are created, or they must be created manually. In the case of creating relationships manually, there are two possible methods depending on the resource in question:

- [Create by payload](#payload)
- [Create by URL](#url) (for libraries only)

Refer to the section on [relationship requirements](#requirements) for a list of the compatible relationships for each resource type, and the methods required to establish those relationships where applicable.

## Create a relationship by payload payload

Some relationships must be manually established when you initially create a resource. To accomplish this, you must provide a relationship object in the request payload when you first create the parent resource. Examples of these relationships include:

- [Creating a data element](/en/docs/experience-platform/tags/api/endpoints/data-elements#create) with the required extensions
- [Creating an environment](/en/docs/experience-platform/tags/api/endpoints/environments#create) with the required host relationship

**API format**

```
POST /properties/{PROPERTY_ID}/{RESOURCE_TYPE}
```

Parameter
Description
{PROPERTY_ID}
The ID of the property to which the resource belongs.
{RESOURCE_TYPE}
The type of resource to be created.
**Request**

The following request creates a new rule_component, establishing relationships with rules and an extension.

```
curl -X POST \
  https://reactor.adobe.io/properties/PRf606dbddfbdc44f580fc6f342b5ff9be/rule_components \
  -H 'Authorization: Bearer [TOKEN]' \
  -H 'x-api-key: [KEY]' \
  -H 'x-gw-ims-org-id: [ORG_ID]' \
  -H 'Accept: application/vnd.api+json;revision=1' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "data": {
          "attributes": {
            "delegate_descriptor_id": "kessel-test::events::click",
            "name": "My Example Click Event",
            "settings": "{\"elementSelector\":\".accordion\",\"bubbleFireIfChildFired\":true}"
          },
          "relationships": {
            "extension": {
              "data": {
                "id": "EXa2865f4d14204fa094f247406424371b",
                "type": "extensions"
              }
            },
            "rules": {
              "data": [
                {
                  "id": "RLd53598e3f1884e63bbc8e9c95e463dcf",
                  "type": "rules"
                }
              ]
            }
          },
          "type": "rule_components"
        }
      }'
```

Property
Description
relationships
An object that must be provided when creating relationships by payload. Each key in this object represents a specific relationship type. In the above example,
extension
and
rules
relationships are established, which are particular to
rule_components
. For more information on compatible relationship types for different resources, see the section on
relationship requirements by resource
.
data
Each relationship type provided under the
relationship
object must contain a
data
property, which references the
id
and
type
of the resource a relationship is being established with. You can create a relationship with multiple resources of the same type by formatting the
data
property as an array of objects, with each object containing the
id
and
type
of an applicable resource.
id
The unique ID of a resource. Each
id
must be accompanied with a sibling
type
property, indicating the type of resource in question.
type
The type of resource as referenced by a sibling
id
field. Accepted values include
data_elements
,
rules
,
extensions
, and
environments
.
## Create a relationship by URL url

Unlike other resources, libraries establish relationships through their own dedicated /relationship endpoints. Examples include:

- [Adding extensions, data elements, and rules to a library](/en/docs/experience-platform/tags/api/endpoints/libraries#add-resources)
- [Assigning a library to an environment](/en/docs/experience-platform/tags/api/endpoints/libraries#environment)

**API format**

```
POST /properties/{PROPERTY_ID}/libraries/{LIBRARY_ID}/relationships/{RESOURCE_TYPE}
```

Parameter
Description
{PROPERTY_ID}
The ID of the property to which the library belongs.
{LIBRARY_ID}
The ID of the library you want to create a relationship for.
{RESOURCE_TYPE}
The type of resource the relationship is targeting. Available values include
environment
,
data_elements
,
extensions
, and
rules
.
**Request**

The following request uses the /relationships/environment endpoint for a library to create a relationship with an environment.

```
curl -X POST \
  https://reactor.adobe.io/properties/PRf606dbddfbdc44f580fc6f342b5ff9be/libraries/LB10c1fd171cd347f19fcb8659a8d679ef/relationships/environment \
  -H 'Authorization: Bearer [TOKEN]' \
  -H 'x-api-key: [KEY]' \
  -H 'x-gw-ims-org-id: [ORG_ID]' \
  -H 'Accept: application/vnd.api+json;revision=1' \
  -H 'Content-Type: application/vnd.api+json' \
  -d '{
        "data": {
          "id": "ENf395a477d2b24ad696d65b901055b9dc",
          "type": "environments",
        }
      }'
```

Property
Description
data
An object which references the
id
and
type
of the target resource for the relationship. If you are creating a relationship with multiple resources of the same type (such as
extensions
and
rules
), the
data
property must be formatted as an array of objects, with each object containing the
id
and
type
of an applicable resource.
id
The unique ID of a resource. Each
id
must be accompanied with a sibling
type
property, indicating the type of resource in question.
type
The type of resource as referenced by a sibling
id
field. Accepted values include
data_elements
,
rules
,
extensions
, and
environments
.
## Relationship requirements by resource requirements

The following tables outline the available relationships for each resource type, whether or not those relationships are required, and the accepted method to manually create the relationship where applicable.

NOTE
If a relationship is not listed as being created by payload or URL, then it is automatically assigned by the system.
### Audit events

Relationship
Required
Create by payload
Create by URL
property
✓
entity
✓
### Builds

Relationship
Required
Create by payload
Create by URL
data_elements
extensions
rules
environment
✓
library
✓
property
✓
### Callbacks

Relationship
Required
Create by payload
Create by URL
property
✓
### Companies

Relationship
Required
Create by payload
Create by URL
properties
### Data elements

Relationship
Required
Create by payload
Create by URL
libraries
revisions
✓
notes
property
✓
origin
✓
extension
✓
✓
updated_with_extension
✓
updated_with_extension_package
✓
### Environments

Relationship
Required
Create by payload
Create by URL
library
builds
host
✓
✓
property
✓
### Extensions

Relationship
Required
Create by payload
Create by URL
libraries
revisions
✓
notes
property
✓
origin
✓
extension_package
✓
✓
updated_with_extension_package
✓
### Hosts

Relationship
Required
Create by payload
Create by URL
property
✓
### Libraries

Relationship
Required
Create by payload
Create by URL
builds
environment
✓
data_elements
✓
extensions
✓
rules
✓
notes
upstream_library
✓
property
✓
last_build
### Notes

Relationship
Required
Create by payload
Create by URL
resource
✓
### Properties

Relationship
Required
Create by payload
Create by URL
company
✓
callbacks
environments
libraries
data_elements
extensions
extensions
### Rule components

Relationship
Required
Create by payload
Create by URL
updated_with_extensions_package
✓
updated_with_extension
✓
extension
✓
✓
notes
origin
✓
property
✓
rules
✓
✓
revisions
✓
### Rules

Relationship
Required
Create by payload
Create by URL
libraries
revisions
✓
notes
property
✓
origin
✓
rule_components
### Secrets

Relationship
Required
Create by payload
Create by URL
property
✓
✓
environment
✓
✓
recommendation-more-help
