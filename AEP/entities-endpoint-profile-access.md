---
title: "Entities endpoint (Profile access)"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/profile/api/entities"
category: "reference"
topic: "experience-platform/real-time-customer-profile-guide"
created_at: "2026-05-29T16:56:01.562438+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Real-Time Customer Profile Guide

# Entities endpoint (Profile access)

Last update: May 23, 2026
- Topics:
- [Profiles](#)

CREATED FOR:

- Developer

IMPORTANT
You can
only
use these endpoints if you have Real-Time CDP Ultimate.
If you have Real-Time CDP Prime, you can continue to ingest and use experience events for personalization use cases as well as view events within the Experience Platform UI, but you will
not
be able to programatically look up experience events using the API.
If you have Real-Time CDP Ultimate and do
not
currently programatically look up events, please contact Adobe Customer Care to enable this feature.
Adobe Experience Platform enables you to access Real-Time Customer Profile data using RESTful APIs or the user interface. This guide outlines how to access entities, more commonly known as “profiles”, using the API. For more information on accessing profiles using the Experience Platform UI, please refer to the [Profile user guide](/en/docs/experience-platform/profile/ui/user-guide).

## Getting started

The API endpoint used in this guide is part of the [Real-Time Customer Profile API](https://www.adobe.com/go/profile-apis-en). Before continuing, please review the [getting started guide](/en/docs/experience-platform/profile/api/getting-started) for links to related documentation, a guide to reading the sample API calls in this document, and important information regarding required headers that are needed to successfully make calls to any Experience Platform API.

## Entity resolution

As part of the architecture upgrade, Adobe is introducing entity resolution for Accounts and Opportunities, using deterministic ID matching based on the latest data. Entity resolution job runs daily during batch segmentation, prior to evaluating multi-entity audiences with B2B attributes.

This enhancement enables Experience Platform to identify and unify multiple records that represent the same entity, improving data consistency and enabling more accurate audience segmentation.

Previously, Accounts and Opportunities relied on identity graph-based resolution that connected identities, including all historical ingestions. In the new entity-resolution approach, identities are linked based on the latest data only.

- Account and Opportunity are entity resolved with a time-precedence based merging: Account: identities using the b2b_account namespace. Opportunity: identities using the b2b_opportunity namespace.
- All other entities are simply unified and only primary identity overlaps are merged with time-precedence based merging.

NOTE
Entity resolution only supports
b2b_account
and
b2b_opportunity
. Identities from other namespaces are not used in entity resolution. If you are using custom namespaces, then you will not be able to find accounts and opportunities.
### How does entity resolution work?

- **Before**: If a Data Universal Numbering System (DUNS) number was used as an additional identity and account’s DUNS number was updated in a source system like CRM, the account ID is linked to both old and new DUNS numbers.
- **After**: If the DUNS number was used as an additional identity and the account’s DUNS number was updated in a source system like a CRM, the account ID is only linked to the new DUNS number, thereby reflecting the current state of account more accurately.

As a result of this update, the Profile Access API now reflects the latest merge profile view after an entity resolution job cycle completes. Additionally, the consistent data provides use cases such as segmentation, activation, and analytics with improved data accuracy and consistency.

## Retrieve an entity retrieve-entity

IMPORTANT
The following B2B entities are no longer supported for lookup requests via the API:
Account-Person Relation, Opportunity-Person Relation, Campaign, Campaign Member, Marketing List, and Marketing List Member
.
Support for these entities has been deprecated. If you have existing integrations or workflows that rely on accessing these entities, please update them to use supported entity types to ensure continued functionality.
You can retrieve a Profile entity by making a GET request to the /access/entities endpoint along with the required query parameters.

Profile entity
**API format**

| code language-http |
| --- |
| GET /access/entities?{QUERY_PARAMETERS} |

Query parameters provided in the request path specify which data to access. You can include multiple parameters, separated by ampersands (&).

To access a Profile entity, you **must** provide the following query parameters:

- schema.name: The name of the entity’s XDM schema. In this use case, the schema.name=_xdm.context.profile.
- entityId: The ID of the entity you’re trying to retrieve.
- entityIdNS: The namespace of the entity you’re trying to retrieve. This value must be provided if the entityId is **not** an XID.

Additionally, usage of the following query parameter is *highly* recommended:

- mergePolicyId: The ID of the merge policy you want to filter the data with. If no merge policy is specified, your organization’s default merge policy will be used.

A complete list of valid parameters is provided in the [query parameters](#query-parameters) section of the appendix.

**Request**

The following request retrieves a customer’s email and name using an identity.

| accordion |
| --- |
| A sample request to retrieve an entity using an identity |
| code language-shell curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.profile&entityId=janedoe@example.com&entityIdNS=email&fields=identities,person.name,workEmail' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' | code language-shell | curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.profile&entityId=janedoe@example.com&entityIdNS=email&fields=identities,person.name,workEmail' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |
| code language-shell |
| curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.profile&entityId=janedoe@example.com&entityIdNS=email&fields=identities,person.name,workEmail' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

**Response**

A successful response returns HTTP status 200 with the requested entity.

| accordion |
| --- |
| A sample response that contains the requested entity |
| code language-json { "BVrqzwVv7o2p3naHvnsWpqZXv3KJgA": { "entityId": "BVrqzwVv7o2p3naHvnsWpqZXv3KJgA", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316601", "namespace": { "code": "ecid" } }, { "id": "janedoe@example.com", "namespace": { "code": "email" } }, { "id": "johnsmith@example.com", "namespace": { "code": "email" } }, { "id": "89149270342662559642753730269986316604", "namespace": { "code": "ecid" } }, { "id": "58832431024964181144308914570411162539", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-28T20:57:24Z" } } | code language-json | { "BVrqzwVv7o2p3naHvnsWpqZXv3KJgA": { "entityId": "BVrqzwVv7o2p3naHvnsWpqZXv3KJgA", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316601", "namespace": { "code": "ecid" } }, { "id": "janedoe@example.com", "namespace": { "code": "email" } }, { "id": "johnsmith@example.com", "namespace": { "code": "email" } }, { "id": "89149270342662559642753730269986316604", "namespace": { "code": "ecid" } }, { "id": "58832431024964181144308914570411162539", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-28T20:57:24Z" } } |
| code language-json |
| { "BVrqzwVv7o2p3naHvnsWpqZXv3KJgA": { "entityId": "BVrqzwVv7o2p3naHvnsWpqZXv3KJgA", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316601", "namespace": { "code": "ecid" } }, { "id": "janedoe@example.com", "namespace": { "code": "email" } }, { "id": "johnsmith@example.com", "namespace": { "code": "email" } }, { "id": "89149270342662559642753730269986316604", "namespace": { "code": "ecid" } }, { "id": "58832431024964181144308914570411162539", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-28T20:57:24Z" } } |

| note |
| --- |
| NOTE |
| If a related graph links more than 50 identities, this service will return HTTP status 422 and the message “Too many related identities”. If you receive this error, consider adding more query parameters to narrow your search. |

B2B Account
**API format**

| code language-http |
| --- |
| GET /access/entities?{QUERY_PARAMETERS} |

Query parameters provided in the request path specify which data to access. You can include multiple parameters, separated by ampersands (&).

To access the B2B Account data, you **must** provide the following query parameters:

- schema.name: The name of the entity’s XDM schema. In this use case, this value is schema.name=_xdm.context.account.
- entityId: The ID of the entity you’re trying to retrieve.
- entityIdNS: The namespace of the entity you’re trying to retrieve. This value must be provided if the entityId is **not** an XID.

Additionally, usage of the following query parameter is *highly* recommended:

- mergePolicyId: The ID of the merge policy you want to filter the data with. If no merge policy is specified, your organization’s default merge policy will be used.

A complete list of valid parameters is provided in the [query parameters](#query-parameters) section of the appendix.

**Request**

| accordion |
| --- |
| A sample request to retrieve a B2B Account |
| code language-shell curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.account&entityIdNs=b2b_account&entityId=2334262' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' | code language-shell | curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.account&entityIdNs=b2b_account&entityId=2334262' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |
| code language-shell |
| curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.account&entityIdNs=b2b_account&entityId=2334262' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

**Response**

A successful response returns HTTP status 200 with the requested entity.

| accordion |
| --- |
| A sample response that contains the requested entity |
| code language-json { "GuQ-AUFjgjaeIw": { "entityId": "GuQ-AUFjgjaeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "{SOURCE_ID}", "sourceKey": "{SOURCE_KEY}", "sourceInstanceID": "{SOURCE_INSTANCE_ID}", "sourceType": "{SOURCE_TYPE}" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "{SOURCE_ID}" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } } } | code language-json | { "GuQ-AUFjgjaeIw": { "entityId": "GuQ-AUFjgjaeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "{SOURCE_ID}", "sourceKey": "{SOURCE_KEY}", "sourceInstanceID": "{SOURCE_INSTANCE_ID}", "sourceType": "{SOURCE_TYPE}" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "{SOURCE_ID}" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } } } |
| code language-json |
| { "GuQ-AUFjgjaeIw": { "entityId": "GuQ-AUFjgjaeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "{SOURCE_ID}", "sourceKey": "{SOURCE_KEY}", "sourceInstanceID": "{SOURCE_INSTANCE_ID}", "sourceType": "{SOURCE_TYPE}" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "{SOURCE_ID}" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } } } |

B2B Opportunity
**API format**

| code language-http |
| --- |
| GET /access/entities?{QUERY_PARAMETERS} |

Query parameters provided in the request path specify which data to access. You can include multiple parameters, separated by ampersands (&).

To access a B2B Opportunity entity, you **must** provide the following query parameters:

- schema.name: The name of the entity’s XDM schema. In this use case, the schema.name=_xdm.context.opportunity.
- entityId: The ID of the entity you’re trying to retrieve.
- entityIdNS: The namespace of the entity you’re trying to retrieve. This value must be provided if the entityId is **not** an XID.

Additionally, usage of the following query parameter is *highly* recommended:

- mergePolicyId: The ID of the merge policy you want to filter the data with. If no merge policy is specified, your organization’s default merge policy will be used.

A complete list of valid parameters is provided in the [query parameters](#query-parameters) section of the appendix.

**Request**

| accordion |
| --- |
| A sample request to retrieve a B2B Opportunity entity |
| code language-shell curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.opportunity&entityIdNs=b2b_opportunity&entityId=2334262' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' | code language-shell | curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.opportunity&entityIdNs=b2b_opportunity&entityId=2334262' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |
| code language-shell |
| curl -X GET 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.opportunity&entityIdNs=b2b_opportunity&entityId=2334262' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

**Response**

A successful response returns HTTP status 200 with the requested entity.

| accordion |
| --- |
| A sample response that contains the requested entity |
| code language-json { "Ggw_AUFjgjaeIw": { "entityId": "Ggw_AUFjgjaeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } } } | code language-json | { "Ggw_AUFjgjaeIw": { "entityId": "Ggw_AUFjgjaeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } } } |
| code language-json |
| { "Ggw_AUFjgjaeIw": { "entityId": "Ggw_AUFjgjaeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } } } |

## Retrieve multiple entities retrieve-entities

You can retrieve multiple Profile entities by making a POST request to the /access/entities endpoint and providing the identities in the payload.

Profile entities
**API format**

| code language-http |
| --- |
| POST /access/entities |

**Request**

The following request retrieves the names and email addresses of several customers by a list of identities.

| accordion |
| --- |
| A sample request to retrieve multiple entities |
| code language-shell curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.profile" }, "fields":[ "identities", "person.name", "workEmail" ], "identities":[ { "entityId":"89149270342662559642753730269986316601", "entityIdNS":{ "code":"ECID" } }, { "entityId":"89149270342662559642753730269986316900", "entityIdNS":{ "code":"ECID" } }, { "entityId":"89149270342662559642753730269986316602", "entityIdNS":{ "code":"ECID" } } ], "timeFilter": { "startTime": 1539838505, "endTime": 1539838510 }, "limit": 10, "orderby": "-timestamp" }' table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 Property Type Description schema.name String (Required) The name of the XDM schema the entity belongs to. fields Array The XDM fields to be returned, as an array of strings. By default, all fields will be returned. identities Array (Required) An array containing a list of identities for the entities you want to access. identities.entityId String The ID of an entity you wish to access. identities.entityIdNS.code String The namespace of an entity ID you wish to access. timeFilter.startTime Integer Specifies the start time to filter Profile entities (in milliseconds). By default, this value is set as the beginning of available time. timeFilter.endTime Integer Specifies the end time to filter Profile entities (in milliseconds). By default, this value is set as the end of available time. limit Integer The maximum number of records to return. By default, this value is set to 1000. orderby String The sort order of retrieved experience events by timestamp, written as (+/-)timestamp with the default being +timestamp . | code language-shell | curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.profile" }, "fields":[ "identities", "person.name", "workEmail" ], "identities":[ { "entityId":"89149270342662559642753730269986316601", "entityIdNS":{ "code":"ECID" } }, { "entityId":"89149270342662559642753730269986316900", "entityIdNS":{ "code":"ECID" } }, { "entityId":"89149270342662559642753730269986316602", "entityIdNS":{ "code":"ECID" } } ], "timeFilter": { "startTime": 1539838505, "endTime": 1539838510 }, "limit": 10, "orderby": "-timestamp" }' | table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 |  |  | Property | Type | Description | schema.name | String | **(Required)** The name of the XDM schema the entity belongs to. | fields | Array | The XDM fields to be returned, as an array of strings. By default, all fields will be returned. | identities | Array | **(Required)** An array containing a list of identities for the entities you want to access. | identities.entityId | String | The ID of an entity you wish to access. | identities.entityIdNS.code | String | The namespace of an entity ID you wish to access. | timeFilter.startTime | Integer | Specifies the start time to filter Profile entities (in milliseconds). By default, this value is set as the beginning of available time. | timeFilter.endTime | Integer | Specifies the end time to filter Profile entities (in milliseconds). By default, this value is set as the end of available time. | limit | Integer | The maximum number of records to return. By default, this value is set to 1000. | orderby | String | The sort order of retrieved experience events by timestamp, written as (+/-)timestamp with the default being +timestamp. |
| code language-shell |
| curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.profile" }, "fields":[ "identities", "person.name", "workEmail" ], "identities":[ { "entityId":"89149270342662559642753730269986316601", "entityIdNS":{ "code":"ECID" } }, { "entityId":"89149270342662559642753730269986316900", "entityIdNS":{ "code":"ECID" } }, { "entityId":"89149270342662559642753730269986316602", "entityIdNS":{ "code":"ECID" } } ], "timeFilter": { "startTime": 1539838505, "endTime": 1539838510 }, "limit": 10, "orderby": "-timestamp" }' |
| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 |  |  |
| Property | Type | Description |
| schema.name | String | **(Required)** The name of the XDM schema the entity belongs to. |
| fields | Array | The XDM fields to be returned, as an array of strings. By default, all fields will be returned. |
| identities | Array | **(Required)** An array containing a list of identities for the entities you want to access. |
| identities.entityId | String | The ID of an entity you wish to access. |
| identities.entityIdNS.code | String | The namespace of an entity ID you wish to access. |
| timeFilter.startTime | Integer | Specifies the start time to filter Profile entities (in milliseconds). By default, this value is set as the beginning of available time. |
| timeFilter.endTime | Integer | Specifies the end time to filter Profile entities (in milliseconds). By default, this value is set as the end of available time. |
| limit | Integer | The maximum number of records to return. By default, this value is set to 1000. |
| orderby | String | The sort order of retrieved experience events by timestamp, written as (+/-)timestamp with the default being +timestamp. |

**Response**

A successful response returns HTTP status 200 with the requested fields of entities specified in the request body.

| accordion |
| --- |
| A sample response that contains the requested entities |
| code language-json { "A29cgveD5y64ezlhxjUXNzcm": { "entityId": "A29cgveD5y64ezlhxjUXNzcm", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316601", "namespace": { "code": "ecid" } }, { "id": "janedoe@example.com", "namespace": { "code": "email" } }, { "id": "05DD23564EC4607F0A490D44", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316603", "namespace": { "code": "ecid" } }, { "id": "janesmith@example.com", "namespace": { "code": "email" } }, { "id": "89149270342662559642753730269986316604", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316700", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316701", "namespace": { "code": "ecid" } }, { "id": "58832431024964181144308914570411162539", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-28T20:57:24Z" }, "A29cgveD5y64e2RixjUXNzcm": { "entityId": "A29cgveD5y64e2RixjUXNzcm", "sources": [ "" ], "entity": {}, "lastModifiedAt": "1970-01-01T00:00:00Z" }, "A29cgveD5y64ezphxjUXNzcm": { "entityId": "A29cgveD5y64ezphxjUXNzcm", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true }, { "id": "janedoe@example.com", "namespace": { "code": "email" } } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-27T23:25:52Z" } } | code language-json | { "A29cgveD5y64ezlhxjUXNzcm": { "entityId": "A29cgveD5y64ezlhxjUXNzcm", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316601", "namespace": { "code": "ecid" } }, { "id": "janedoe@example.com", "namespace": { "code": "email" } }, { "id": "05DD23564EC4607F0A490D44", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316603", "namespace": { "code": "ecid" } }, { "id": "janesmith@example.com", "namespace": { "code": "email" } }, { "id": "89149270342662559642753730269986316604", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316700", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316701", "namespace": { "code": "ecid" } }, { "id": "58832431024964181144308914570411162539", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-28T20:57:24Z" }, "A29cgveD5y64e2RixjUXNzcm": { "entityId": "A29cgveD5y64e2RixjUXNzcm", "sources": [ "" ], "entity": {}, "lastModifiedAt": "1970-01-01T00:00:00Z" }, "A29cgveD5y64ezphxjUXNzcm": { "entityId": "A29cgveD5y64ezphxjUXNzcm", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true }, { "id": "janedoe@example.com", "namespace": { "code": "email" } } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-27T23:25:52Z" } } |
| code language-json |
| { "A29cgveD5y64ezlhxjUXNzcm": { "entityId": "A29cgveD5y64ezlhxjUXNzcm", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316601", "namespace": { "code": "ecid" } }, { "id": "janedoe@example.com", "namespace": { "code": "email" } }, { "id": "05DD23564EC4607F0A490D44", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316603", "namespace": { "code": "ecid" } }, { "id": "janesmith@example.com", "namespace": { "code": "email" } }, { "id": "89149270342662559642753730269986316604", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316700", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316701", "namespace": { "code": "ecid" } }, { "id": "58832431024964181144308914570411162539", "namespace": { "code": "ecid" } }, { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-28T20:57:24Z" }, "A29cgveD5y64e2RixjUXNzcm": { "entityId": "A29cgveD5y64e2RixjUXNzcm", "sources": [ "" ], "entity": {}, "lastModifiedAt": "1970-01-01T00:00:00Z" }, "A29cgveD5y64ezphxjUXNzcm": { "entityId": "A29cgveD5y64ezphxjUXNzcm", "sources": [ "1000000000" ], "entity": { "identities": [ { "id": "89149270342662559642753730269986316602", "namespace": { "code": "ecid" }, "primary": true }, { "id": "janedoe@example.com", "namespace": { "code": "email" } } ], "person": { "name": { "firstName": "Jane", "middleName": "F", "lastName": "Doe" } }, "workEmail": { "primary": true, "address": "janedoe@example.com", "label": "Jane Doe", "type": "work", "status": "active" } }, "lastModifiedAt": "2018-08-27T23:25:52Z" } } |

B2B Account
**API format**

| code language-http |
| --- |
| POST /access/entities |

**Request**

The following request retrieves the requested B2B Accounts.

| accordion |
| --- |
| A sample request to retrieve multiple entities |
| code language-shell curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.account" }, "identities": [ { "entityId": "2334262", "entityIdNS": { "code":"b2b_account" } }, { "entityId": "2334263", "entityIdNS": { "code":"b2b_account" } }, { "entityId": "2334264", "entityIdNS": { "code":"b2b_account" } } ] }' table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 Property Type Description schema.name String (Required) The name of the XDM schema the entity belongs to. identities Array (Required) An array containing a list of identities for the entities you want to access. identities.entityId String The ID of an entity you wish to access. identities.entityIdNS.code String The namespace of an entity ID you wish to access. | code language-shell | curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.account" }, "identities": [ { "entityId": "2334262", "entityIdNS": { "code":"b2b_account" } }, { "entityId": "2334263", "entityIdNS": { "code":"b2b_account" } }, { "entityId": "2334264", "entityIdNS": { "code":"b2b_account" } } ] }' | table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 |  |  | Property | Type | Description | schema.name | String | **(Required)** The name of the XDM schema the entity belongs to. | identities | Array | **(Required)** An array containing a list of identities for the entities you want to access. | identities.entityId | String | The ID of an entity you wish to access. | identities.entityIdNS.code | String | The namespace of an entity ID you wish to access. |
| code language-shell |
| curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.account" }, "identities": [ { "entityId": "2334262", "entityIdNS": { "code":"b2b_account" } }, { "entityId": "2334263", "entityIdNS": { "code":"b2b_account" } }, { "entityId": "2334264", "entityIdNS": { "code":"b2b_account" } } ] }' |
| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 |  |  |
| Property | Type | Description |
| schema.name | String | **(Required)** The name of the XDM schema the entity belongs to. |
| identities | Array | **(Required)** An array containing a list of identities for the entities you want to access. |
| identities.entityId | String | The ID of an entity you wish to access. |
| identities.entityIdNS.code | String | The namespace of an entity ID you wish to access. |

**Response**

A successful response returns HTTP status 200 with the requested entities.

| accordion |
| --- |
| A sample response that contains the requested entities |
| code language-json { "GuQ-AUFjgjeeIw": { "requestedIdentity": { "entityId": "2334263", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjeeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "GuQ-AUFjgjaeIw": { "requestedIdentity": { "entityId": "2334262", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjaeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "GuQ-AUFjgjmeIw": { "requestedIdentity": { "entityId": "2334265", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjmeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334265", "identityMap": { "b2b_account": [ { "id": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334265" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334265", "sourceKey": "2334265", "sourceInstanceID": "2334265", "sourceType": "Random" } } } | code language-json | { "GuQ-AUFjgjeeIw": { "requestedIdentity": { "entityId": "2334263", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjeeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "GuQ-AUFjgjaeIw": { "requestedIdentity": { "entityId": "2334262", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjaeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "GuQ-AUFjgjmeIw": { "requestedIdentity": { "entityId": "2334265", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjmeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334265", "identityMap": { "b2b_account": [ { "id": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334265" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334265", "sourceKey": "2334265", "sourceInstanceID": "2334265", "sourceType": "Random" } } } |
| code language-json |
| { "GuQ-AUFjgjeeIw": { "requestedIdentity": { "entityId": "2334263", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjeeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "GuQ-AUFjgjaeIw": { "requestedIdentity": { "entityId": "2334262", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjaeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_account": [ { "id": "2334263" }, { "id": "2334262" }, { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "GuQ-AUFjgjmeIw": { "requestedIdentity": { "entityId": "2334265", "entityIdNS": { "code": "b2b_account" } }, "entityId": "GuQ-AUFjgjmeIw", "mergePolicy": { "id": "a6150f47-a94f-4c9d-bfa0-958a370020ee" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334265", "identityMap": { "b2b_account": [ { "id": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334265" } ] }, "isDeleted": false, "accountKey": { "sourceID": "2334265", "sourceKey": "2334265", "sourceInstanceID": "2334265", "sourceType": "Random" } } } |

B2B Opportunity
**API format**

| code language-http |
| --- |
| POST /access/entities |

**Request**

The following request retrieves the requested B2B opportunities.

| accordion |
| --- |
| A sample request to retrieve multiple entities |
| code language-shell curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.opportunity" }, "identities": [ { "entityId": "2334262", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334263", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334264", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334265", "entityIdNS": { "code":"b2b_opportunity" } } ] }' table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 Property Type Description schema.name String (Required) The name of the XDM schema the entity belongs to. identities Array (Required) An array containing a list of identities for the entities you want to access. identities.entityId String The ID of an entity you wish to access. identities.entityIdNS.code String The namespace of an entity ID you wish to access. | code language-shell | curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.opportunity" }, "identities": [ { "entityId": "2334262", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334263", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334264", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334265", "entityIdNS": { "code":"b2b_opportunity" } } ] }' | table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 |  |  | Property | Type | Description | schema.name | String | **(Required)** The name of the XDM schema the entity belongs to. | identities | Array | **(Required)** An array containing a list of identities for the entities you want to access. | identities.entityId | String | The ID of an entity you wish to access. | identities.entityIdNS.code | String | The namespace of an entity ID you wish to access. |
| code language-shell |
| curl -X POST https://platform.adobe.io/data/core/ups/access/entities \ -H 'Content-Type: application/json' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "schema":{ "name":"_xdm.context.opportunity" }, "identities": [ { "entityId": "2334262", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334263", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334264", "entityIdNS": { "code":"b2b_opportunity" } }, { "entityId": "2334265", "entityIdNS": { "code":"b2b_opportunity" } } ] }' |
| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 |  |  |
| Property | Type | Description |
| schema.name | String | **(Required)** The name of the XDM schema the entity belongs to. |
| identities | Array | **(Required)** An array containing a list of identities for the entities you want to access. |
| identities.entityId | String | The ID of an entity you wish to access. |
| identities.entityIdNS.code | String | The namespace of an entity ID you wish to access. |

**Response**

A successful response returns HTTP status 200 with the requested entities.

| accordion |
| --- |
| A sample response that contains the requested entities |
| code language-json { "Ggw_AUFjgjaeIw": { "requestedIdentity": { "entityId": "2334262", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjaeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "Ggw_AUFjgjieIw": { "requestedIdentity": { "entityId": "2334264", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjieIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0041c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334264", "identityMap": { "b2b_opportunity": [ { "id": "2334264" }, { "id": "0041c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334264", "sourceKey": "2334264", "sourceInstanceID": "2334264", "sourceType": "Salesforce" } } }, "Ggw_AUFjgjeeIw": { "requestedIdentity": { "entityId": "2334263", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjeeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "Ggw_AUFjgjmeIw": { "requestedIdentity": { "entityId": "2334265", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjmeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334265", "identityMap": { "b2b_opportunity": [ { "id": "2334265" }, { "id": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334265", "sourceKey": "2334265", "sourceInstanceID": "2334265", "sourceType": "Random" } } } } | code language-json | { "Ggw_AUFjgjaeIw": { "requestedIdentity": { "entityId": "2334262", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjaeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "Ggw_AUFjgjieIw": { "requestedIdentity": { "entityId": "2334264", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjieIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0041c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334264", "identityMap": { "b2b_opportunity": [ { "id": "2334264" }, { "id": "0041c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334264", "sourceKey": "2334264", "sourceInstanceID": "2334264", "sourceType": "Salesforce" } } }, "Ggw_AUFjgjeeIw": { "requestedIdentity": { "entityId": "2334263", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjeeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "Ggw_AUFjgjmeIw": { "requestedIdentity": { "entityId": "2334265", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjmeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334265", "identityMap": { "b2b_opportunity": [ { "id": "2334265" }, { "id": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334265", "sourceKey": "2334265", "sourceInstanceID": "2334265", "sourceType": "Random" } } } } |
| code language-json |
| { "Ggw_AUFjgjaeIw": { "requestedIdentity": { "entityId": "2334262", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjaeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "Ggw_AUFjgjieIw": { "requestedIdentity": { "entityId": "2334264", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjieIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0041c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334264", "identityMap": { "b2b_opportunity": [ { "id": "2334264" }, { "id": "0041c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334264", "sourceKey": "2334264", "sourceInstanceID": "2334264", "sourceType": "Salesforce" } } }, "Ggw_AUFjgjeeIw": { "requestedIdentity": { "entityId": "2334263", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjeeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334262", "identityMap": { "b2b_opportunity": [ { "id": "0043c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" }, { "id": "2334263" }, { "id": "2334262" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" } } }, "Ggw_AUFjgjmeIw": { "requestedIdentity": { "entityId": "2334265", "entityIdNS": { "code": "b2b_opportunity" } }, "entityId": "Ggw_AUFjgjmeIw", "mergePolicy": { "id": "162824be-07f5-4cd0-aa85-2ff3c8f6c775" }, "sources": [ "er_m_attr" ], "entity": { "_id": "id1", "extSourceSystemAudit": { "lastReferencedDate": "2024-03-09 12:21:43.0", "lastActivityDate": "2024-03-09 12:21:43.0", "lastUpdatedDate": "2024-03-09 12:21:43.0", "lastUpdatedBy": "{USER_ID}", "externalKey": { "sourceID": "00394S0001xpG6xABE", "sourceKey": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce", "sourceInstanceID": "00DC0000000Q35nMAC", "sourceType": "Salesforce" }, "lastViewedDate": "2024-03-09 12:21:43.0", "createdDate": "2024-03-09 12:21:43.0" }, "accountID": "2334265", "identityMap": { "b2b_opportunity": [ { "id": "2334265" }, { "id": "0054c329201xpG6xAAE@00DC0000000Q35nWIN.Salesforce" } ] }, "isDeleted": false, "opportunityKey": { "sourceID": "2334262", "sourceKey": "2334262", "sourceInstanceID": "2334262", "sourceType": "Random" }, "accountKey": { "sourceID": "2334265", "sourceKey": "2334265", "sourceInstanceID": "2334265", "sourceType": "Random" } } } } |

### Access a subsequent page of results

Results are paginated when retrieving time series events. If there are subsequent pages of results, the _page.next property will contain an ID. Additionally, the _links.next.href property provides a request URI for retrieving the next page. To retrieve the results, make another GET request to the /access/entities endpoint and replace /entities with the value of the provided URI.

NOTE
Ensure you do not accidentally repeat
/entities/
in the request path. It should only appear once like,
/access/entities?start=...
**API format**

```
GET /access/{NEXT_URI}
```

Parameter
Description
{NEXT_URI}
The URI value taken from
_links.next.href
.
**Request**

The following request retrieves the next page of results by using the _links.next.href URI as the request path.

A sample request to access the next page of results
| code language-shell |
| --- |
| curl -X GET \ 'https://platform.adobe.io/data/core/ups/access/entities?start=c8d11988-6b56-4571-a123-b6ce74236037&orderby=timestamp&schema.name=_xdm.context.experienceevent&relatedSchema.name=_xdm.context.profile&relatedEntityId=89149270342662559642753730269986316900&relatedEntityIdNS=ECID&fields=endUserIDs,web,channel&startTime=1531260476000&endTime=1531260480000&limit=1' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

**Response**

A successful response returns the next page of results. This response does not have subsequent pages of results, as indicated by the empty string values of _page.next and _links.next.href.

A sample response that contains the next page of entities
| code language-json |
| --- |
| { "_page": { "orderby": "timestamp", "start": "c8d11988-6b56-4571-a123-b6ce74236037", "count": 1, "next": "" }, "children": [ { "relatedEntityId": "A29cgveD5y64e2RixjUXNzcm", "entityId": "c8d11988-6b56-4571-a123-b6ce74236037", "timestamp": 1531260477000, "entity": { "endUserIDs": { "_experience": { "ecid": { "id": "89149270342662559642753730269986316900", "namespace": { "code": "ecid" } } } }, "channel": { "_type": "web" }, "web": { "webPageDetails": { "name": "Fernie Snow", "pageViews": { "value": 1 } } } }, "lastModifiedAt": "2018-08-21T06:50:01Z" } ], "_links": { "next": { "href": "" } } } |

## Delete an entity delete-entity

IMPORTANT
The delete entity endpoint will be deprecated by the end of October 2025. If you want to perform record delete operations, you can use the
Data Lifecycle record delete API workflow
or the
Data Lifecycle record delete UI workflow
instead.
Additionally, delete requests for the following B2B entities have already been deprecated:
- Account
- Account-Person Relation
- Opportunity
- Opportunity-Person Relation
- Campaign
- Campaign Member
- Marketing List
- Marketing List Members

You can delete an entity from the Profile Store by making a DELETE request to the/access/entities endpoint along with the required query parameters.

**API format**

```
DELETE /access/entities?{QUERY_PARAMETERS}
```

Query parameters provided in the request path specify which data to access. You can include multiple parameters, separated by ampersands (&).

To delete an entity, you **must** provide the following query parameters:

- schema.name: The name of the entity’s XDM schema. In this use case, you can **only** use schema.name=_xdm.context.profile.
- entityId: The ID of the entity you’re trying to retrieve.
- entityIdNS: The namespace of the entity you’re trying to retrieve. This value must be provided if the entityId is **not** an XID.
- mergePolicyId: The merge policy ID of the entity. The merge policy contains information about identity stitching and key-value XDM object merging. If this value is not provided, the default merge policy will be used.

**Request**

The following request deletes the specified entity.

A sample request to delete an entity
| code language-shell |
| --- |
| curl -X DELETE 'https://platform.adobe.io/data/core/ups/access/entities?schema.name=_xdm.context.profile&entityId=janedoe@example.com&entityIdNS=email' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

**Response**

A successful response returns HTTP status 202 with an empty response body.

## Next steps

By following this guide you have successfully accessed Real-Time Customer Profile data fields, profiles, and time series data. To learn how to access other data resources stored in Experience Platform, see the [Data Access overview](/en/docs/experience-platform/data-access/home).

## Appendix appendix

The following section provides supplemental information regarding accessing Profile data using the API.

### Query parameters query-parameters

The following parameters are used in the path for GET requests to the /access/entities endpoint. They serve to identify the profile entity you wish to access and filter the data returned in the response. Required parameters are labeled, while the rest are optional.

Parameter
Description
Example
schema.name
(Required)
The name of the entity’s XDM schema.
schema.name=_xdm.context.profile
relatedSchema.name
If
schema.name
is
_xdm.context.experienceevent
, this value
must
specify the schema for the profile entity that the time series events are related to.
relatedSchema.name=_xdm.context.profile
entityId
(Required)
The ID of the entity. If the value of this parameter is not an XID, an identity namespace parameter (
entityIdNS
) must also be provided.
entityId=janedoe@example.com
entityIdNS
If
entityId
is not provided as an XID, this field
must
specify the identity namespace.
entityIdNS=email
relatedEntityId
If
schema.name
is
_xdm.context.experienceevent
, this value
must
specify the related profile entity’s ID. This value follows the same rules as
entityId
.
relatedEntityId=69935279872410346619186588147492736556
relatedEntityIdNS
If
schema.name
is “_xdm.context.experienceevent”, this value must specify the identity namespace for the entity specified in
relatedEntityId
.
relatedEntityIdNS=CRMID
fields
Filters the data returned in the response. Use this to specify which schema field values to include in data retrieved. For multiple fields, separate values by a comma with no spaces between.
fields=personalEmail,person.name,person.gender
mergePolicyId
Recommended
Identifies the merge policy by which to govern the data returned. If one is not specified in the call, your organization’s default for that schema will be used. If no default merge policy has been defined for the schema you are requesting, the API will return an HTTP 422 error status code.
mergePolicyId=5aa6885fcf70a301dabdfa4a
orderBy
The sort order of retrieved entities by timestamp. This is written as
(+/-)timestamp
, with the default being
+timestamp
.
orderby=-timestamp
startTime
Specifies the start time to filter the entities (in milliseconds).
startTime=1539838505
endTime
Specifies the end time to filter entities (in milliseconds).
endTime=1539838510
limit
Specifies the maximum number of entities to return. By default, this value is set to 1000.
limit=100
property
Filters by the property value. This query parameter supports the following evaluators: =, !=, <, <=, >, >=. This can only be used with experience events, with a maximum of three properties being supported.
property=webPageDetails.isHomepage=true&property=localTime<="2020-07-20"
recommendation-more-help
