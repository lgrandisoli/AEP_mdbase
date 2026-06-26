---
title: "Create a source connection and dataflow for SAP Commerce using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/ecommerce/sap-commerce"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:37:49.472767+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Create a source connection and dataflow for SAP Commerce using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The SAP Commerce source is in beta. See the
sources overview
for more information on using beta-labeled sources.
The following tutorial walks you through the steps to create a SAP Commerce source connection and a dataflow to bring [SAP Subscription Billing](https://www.sap.com/products/financial-management/subscription-billing.html) contacts and customer data to Adobe Experience Platform using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully connect to SAP Commerce using the Flow Service API.

### Gather required credentials

In order to connect SAP Commerce to Experience Platform, you must provide values for the following connection properties:

Credential
Description
clientId
The value of
clientId
from the service key.
clientSecret
The value of
clientSecret
from the service key.
tokenEndpoint
The value of
url
from the service key, it will be similar to
https://subscriptionbilling.authentication.eu10.hana.ondemand.com
.
region
Your data center location. The region is present in the
url
and has a value similar to
eu10
or
us10
. For example if the
url
is
https://subscriptionbilling.authentication.eu10.hana.ondemand.com
, then you will need
eu10
.
For more information on these credentials, please refer to the [SAP Commerce documentation](https://help.sap.com/docs/CLOUD_TO_CASH_OD/987aec876092428f88162e438acf80d6/c5fcaf96daff4c7a8520188e4d8a1843.html).

## Connect SAP Commerce to Experience Platform using the Flow Service API

The following outlines the steps you need to make in order to authenticate your SAP Commerce source, create a source connection, and create a dataflow to bring your accounts and contacts data to Experience Platform.

### Create a base connection base-connection

A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

To create a base connection ID, make a POST request to the /connections endpoint while providing your SAP Commerce authentication credentials as part of the request body.

**API format**

```
POST /connections
```

**Request**

The following request creates a base connection for SAP Commerce:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/connections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "SAP Commerce base connection",
      "description": "Authenticated base connection for SAP Commerce",
      "connectionSpec": {
          "id": "d8ee38de-7ae9-4058-9610-c79ce75f8e92",
          "version": "1.0"
      },
      "auth": {
          "specName": "OAuth2 Client Credential",
          "params": {
              "region": "{REGION}",
              "clientId": "{CLIENT_ID}",
              "clientSecret": "{CLIENT_SECRET}"
              "tokenEndpoint": "{TOKEN_ENDPOINT}"
          }
      }
  }'
```

Property
Description
name
The name of your base connection. Ensure that the name of your base connection is descriptive as you can use this to look up information on your base connection.
description
An optional value that you can include to provide more information on your base connection.
connectionSpec.id
The connection specification ID of your source. This ID can be retrieved after your source is registered and approved through the Flow Service API.
auth.specName
The authentication type that you are using to authenticate your source to Experience Platform.
auth.params.region
Your data center location. The region is present in the
url
and has a value similar to
eu10
or
us10
. For example, if the
url
is
https://subscriptionbilling.authentication.eu10.hana.ondemand.com
you will need
eu10
.
auth.params.clientId
The value of
clientId
from the service key.
auth.params.clientSecret
The value of
clientSecret
from the service key.
auth.params.tokenEndpoint
The value of
url
from the service key, it will be similar to
https://subscriptionbilling.authentication.eu10.hana.ondemand.com
.
**Response**

A successful response returns the newly created base connection, including its unique connection identifier (id). This ID is required to explore your source’s file structure and contents in the next step.

```
{
     "id": "5f6d6022-3f64-400c-ba01-d4010de2d8ff",
     "etag": "\"f8018de1-0000-0200-0000-6482d7210000\""
}
```

### Explore your source explore

Once you have your base connection ID, you can now exploree the content and structure of your source data by performing a GET request to the /connections endpoint while providing your base connection ID as a query parameter.

**API format**

```
GET /connections/{BASE_CONNECTION_ID}/explore?objectType=rest&object={OBJECT}&fileType={FILE_TYPE}&preview={PREVIEW}&sourceParams={SOURCE_PARAMS}
```

When performing GET requests to explore your source’s file structure and contents, you must include the query parameters that are listed in the table below:

Parameter
Description
{BASE_CONNECTION_ID}
The base connection ID generated in the previous step.
objectType=rest
The type of object that you wish to explore. Currently, this value is always set to
rest
.
{OBJECT}
This parameter is required only when viewing a specific directory. Its value represents the path of the directory you wish to explore. For this source the value would be
json
.
fileType=json
The file type of the file you want to bring to Experience Platform. Currently,
json
is the only supported file type.
{PREVIEW}
A boolean value that defines whether the contents of the connection supports preview.
{SOURCE_PARAMS}
Defines parameters for the source file you want to bring to Experience Platform. To retrieve the accepted format-type for {SOURCE_PARAMS}, you must encode the entire string in base64.SAP Commerce supports multiple APIs. Depending on which object type you are leveraging, pass one of the below :

- customers
- contacts

The SAP Commerce source supports multiple APIs. Depending on which object type you are leveraging the request to be sent is as below:

NOTE
Some response records have been truncated to allow for a better presentation.
Customers
| accordion |
| --- |
| Request |
| For SAP Commerce Customers API the value for {SOURCE_PARAMS} is passed as {"object_type":"customers"} . When encoded in base64, it equates to eyJvYmplY3RfdHlwZSI6ImN1c3RvbWVycyJ9 as shown below. code language-shell curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/f5421911-6f6c-41c7-aafa-5d9d2ce51535/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJvYmplY3RfdHlwZSI6ImN1c3RvbWVycyJ9' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' | code language-shell | curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/f5421911-6f6c-41c7-aafa-5d9d2ce51535/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJvYmplY3RfdHlwZSI6ImN1c3RvbWVycyJ9' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |
| code language-shell |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/f5421911-6f6c-41c7-aafa-5d9d2ce51535/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJvYmplY3RfdHlwZSI6ImN1c3RvbWVycyJ9' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

| accordion |
| --- |
| Response |
| A successful response returns a JSON structure like the following: code language-json { "format": "hierarchical", "schema": { "type": "object", "properties": { "personalInfo": { "type": "object", "properties": { "firstName": { "type": "string" }, "lastName": { "type": "string" } } }, "addresses": { "type": "array", "items": { "type": "object", "properties": { "country": { "type": "string" }, "isDefault": { "type": "boolean" }, "phone": { "type": "string" }, "city": { "type": "string" }, "street": { "type": "string" }, "postalCode": { "type": "string" }, "addressUUID": { "type": "string" }, "houseNumber": { "type": "string" }, "additionalAddressInfo": { "type": "string" }, "state": { "type": "string" }, "email": { "type": "string" } } } }, "customerNumber": { "type": "string" }, "corporateInfo": { "type": "object", "properties": {} }, "customReferences": { "type": "array", "items": { "type": "object", "properties": {} } }, "externalObjectReferences": { "type": "array", "items": { "type": "object", "properties": { "externalSystemId": { "type": "string" }, "externalId": { "type": "string" }, "externalIdTypeCode": { "type": "string" } } } }, "createdAt": { "type": "string" }, "customerType": { "type": "string" }, "markets": { "type": "array", "items": { "type": "object", "properties": { "country": { "type": "string" }, "salesArea": { "type": "object", "properties": { "division": { "type": "string" }, "distributionChannel": { "type": "string" }, "salesOrganization": { "type": "string" } } }, "priceType": { "type": "string" }, "active": { "type": "boolean" }, "currency": { "type": "string" }, "marketId": { "type": "string" } } } }, "createdBy": { "type": "string" }, "changedBy": { "type": "string" }, "changedAt": { "type": "string" }, "defaultAddress": { "type": "object", "properties": { "country": { "type": "string" }, "isDefault": { "type": "boolean" }, "phone": { "type": "string" }, "city": { "type": "string" }, "street": { "type": "string" }, "postalCode": { "type": "string" }, "addressUUID": { "type": "string" }, "houseNumber": { "type": "string" }, "additionalAddressInfo": { "type": "string" }, "state": { "type": "string" }, "email": { "type": "string" } } } } }, "data": [ { "personalInfo": { "firstName": "Test 1", "lastName": "User 1" }, "addresses": [ { "email": "user1@test.com", "phone": "123456890", "houseNumber": "123", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "ff871221-ab48-435c-b1f5-903db1c3cea2", "isDefault": true } ], "customerNumber": "2863620303", "externalObjectReferences": [ { "externalSystemId": "t090000", "externalId": "1324566", "externalIdTypeCode": "201" } ], "createdAt": "2023-05-31T06:39:28.499Z", "customerType": "INDIVIDUAL", "markets": [ { "marketId": "US", "active": true, "currency": "USD", "country": "US", "salesArea": { "salesOrganization": "SE10", "distributionChannel": "00", "division": "00" }, "priceType": "Net" } ], "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedAt": "2023-05-31T06:39:28.499Z", "defaultAddress": { "email": "user1@test.com", "phone": "123456890", "houseNumber": "123", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "ff871221-ab48-435c-b1f5-903db1c3cea2", "isDefault": true } }, { "personalInfo": { "firstName": "Test 2", "lastName": "User 2" }, "addresses": [ { "email": "user2@test.com", "phone": "1234567899", "houseNumber": "876", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "1cd039aa-5b86-4e46-8e37-9ef263332c6b", "isDefault": true } ], "customerNumber": "6776445404", "externalObjectReferences": [ { "externalSystemId": "t089999", "externalId": "1324565", "externalIdTypeCode": "201" } ], "createdAt": "2023-05-31T06:39:28.142Z", "customerType": "INDIVIDUAL", "markets": [ { "marketId": "US", "active": true, "currency": "USD", "country": "US", "salesArea": { "salesOrganization": "SE10", "distributionChannel": "00", "division": "00" }, "priceType": "Net" } ], "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b12345", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b12345", "changedAt": "2023-05-31T06:39:28.142Z", "defaultAddress": { "email": "user2@test.com", "phone": "1234567899", "houseNumber": "876", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "1cd039aa-5b86-4e46-8e37-9ef263332c6b", "isDefault": true } } ] } | code language-json | { "format": "hierarchical", "schema": { "type": "object", "properties": { "personalInfo": { "type": "object", "properties": { "firstName": { "type": "string" }, "lastName": { "type": "string" } } }, "addresses": { "type": "array", "items": { "type": "object", "properties": { "country": { "type": "string" }, "isDefault": { "type": "boolean" }, "phone": { "type": "string" }, "city": { "type": "string" }, "street": { "type": "string" }, "postalCode": { "type": "string" }, "addressUUID": { "type": "string" }, "houseNumber": { "type": "string" }, "additionalAddressInfo": { "type": "string" }, "state": { "type": "string" }, "email": { "type": "string" } } } }, "customerNumber": { "type": "string" }, "corporateInfo": { "type": "object", "properties": {} }, "customReferences": { "type": "array", "items": { "type": "object", "properties": {} } }, "externalObjectReferences": { "type": "array", "items": { "type": "object", "properties": { "externalSystemId": { "type": "string" }, "externalId": { "type": "string" }, "externalIdTypeCode": { "type": "string" } } } }, "createdAt": { "type": "string" }, "customerType": { "type": "string" }, "markets": { "type": "array", "items": { "type": "object", "properties": { "country": { "type": "string" }, "salesArea": { "type": "object", "properties": { "division": { "type": "string" }, "distributionChannel": { "type": "string" }, "salesOrganization": { "type": "string" } } }, "priceType": { "type": "string" }, "active": { "type": "boolean" }, "currency": { "type": "string" }, "marketId": { "type": "string" } } } }, "createdBy": { "type": "string" }, "changedBy": { "type": "string" }, "changedAt": { "type": "string" }, "defaultAddress": { "type": "object", "properties": { "country": { "type": "string" }, "isDefault": { "type": "boolean" }, "phone": { "type": "string" }, "city": { "type": "string" }, "street": { "type": "string" }, "postalCode": { "type": "string" }, "addressUUID": { "type": "string" }, "houseNumber": { "type": "string" }, "additionalAddressInfo": { "type": "string" }, "state": { "type": "string" }, "email": { "type": "string" } } } } }, "data": [ { "personalInfo": { "firstName": "Test 1", "lastName": "User 1" }, "addresses": [ { "email": "user1@test.com", "phone": "123456890", "houseNumber": "123", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "ff871221-ab48-435c-b1f5-903db1c3cea2", "isDefault": true } ], "customerNumber": "2863620303", "externalObjectReferences": [ { "externalSystemId": "t090000", "externalId": "1324566", "externalIdTypeCode": "201" } ], "createdAt": "2023-05-31T06:39:28.499Z", "customerType": "INDIVIDUAL", "markets": [ { "marketId": "US", "active": true, "currency": "USD", "country": "US", "salesArea": { "salesOrganization": "SE10", "distributionChannel": "00", "division": "00" }, "priceType": "Net" } ], "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedAt": "2023-05-31T06:39:28.499Z", "defaultAddress": { "email": "user1@test.com", "phone": "123456890", "houseNumber": "123", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "ff871221-ab48-435c-b1f5-903db1c3cea2", "isDefault": true } }, { "personalInfo": { "firstName": "Test 2", "lastName": "User 2" }, "addresses": [ { "email": "user2@test.com", "phone": "1234567899", "houseNumber": "876", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "1cd039aa-5b86-4e46-8e37-9ef263332c6b", "isDefault": true } ], "customerNumber": "6776445404", "externalObjectReferences": [ { "externalSystemId": "t089999", "externalId": "1324565", "externalIdTypeCode": "201" } ], "createdAt": "2023-05-31T06:39:28.142Z", "customerType": "INDIVIDUAL", "markets": [ { "marketId": "US", "active": true, "currency": "USD", "country": "US", "salesArea": { "salesOrganization": "SE10", "distributionChannel": "00", "division": "00" }, "priceType": "Net" } ], "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b12345", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b12345", "changedAt": "2023-05-31T06:39:28.142Z", "defaultAddress": { "email": "user2@test.com", "phone": "1234567899", "houseNumber": "876", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "1cd039aa-5b86-4e46-8e37-9ef263332c6b", "isDefault": true } } ] } |
| code language-json |
| { "format": "hierarchical", "schema": { "type": "object", "properties": { "personalInfo": { "type": "object", "properties": { "firstName": { "type": "string" }, "lastName": { "type": "string" } } }, "addresses": { "type": "array", "items": { "type": "object", "properties": { "country": { "type": "string" }, "isDefault": { "type": "boolean" }, "phone": { "type": "string" }, "city": { "type": "string" }, "street": { "type": "string" }, "postalCode": { "type": "string" }, "addressUUID": { "type": "string" }, "houseNumber": { "type": "string" }, "additionalAddressInfo": { "type": "string" }, "state": { "type": "string" }, "email": { "type": "string" } } } }, "customerNumber": { "type": "string" }, "corporateInfo": { "type": "object", "properties": {} }, "customReferences": { "type": "array", "items": { "type": "object", "properties": {} } }, "externalObjectReferences": { "type": "array", "items": { "type": "object", "properties": { "externalSystemId": { "type": "string" }, "externalId": { "type": "string" }, "externalIdTypeCode": { "type": "string" } } } }, "createdAt": { "type": "string" }, "customerType": { "type": "string" }, "markets": { "type": "array", "items": { "type": "object", "properties": { "country": { "type": "string" }, "salesArea": { "type": "object", "properties": { "division": { "type": "string" }, "distributionChannel": { "type": "string" }, "salesOrganization": { "type": "string" } } }, "priceType": { "type": "string" }, "active": { "type": "boolean" }, "currency": { "type": "string" }, "marketId": { "type": "string" } } } }, "createdBy": { "type": "string" }, "changedBy": { "type": "string" }, "changedAt": { "type": "string" }, "defaultAddress": { "type": "object", "properties": { "country": { "type": "string" }, "isDefault": { "type": "boolean" }, "phone": { "type": "string" }, "city": { "type": "string" }, "street": { "type": "string" }, "postalCode": { "type": "string" }, "addressUUID": { "type": "string" }, "houseNumber": { "type": "string" }, "additionalAddressInfo": { "type": "string" }, "state": { "type": "string" }, "email": { "type": "string" } } } } }, "data": [ { "personalInfo": { "firstName": "Test 1", "lastName": "User 1" }, "addresses": [ { "email": "user1@test.com", "phone": "123456890", "houseNumber": "123", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "ff871221-ab48-435c-b1f5-903db1c3cea2", "isDefault": true } ], "customerNumber": "2863620303", "externalObjectReferences": [ { "externalSystemId": "t090000", "externalId": "1324566", "externalIdTypeCode": "201" } ], "createdAt": "2023-05-31T06:39:28.499Z", "customerType": "INDIVIDUAL", "markets": [ { "marketId": "US", "active": true, "currency": "USD", "country": "US", "salesArea": { "salesOrganization": "SE10", "distributionChannel": "00", "division": "00" }, "priceType": "Net" } ], "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedAt": "2023-05-31T06:39:28.499Z", "defaultAddress": { "email": "user1@test.com", "phone": "123456890", "houseNumber": "123", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "ff871221-ab48-435c-b1f5-903db1c3cea2", "isDefault": true } }, { "personalInfo": { "firstName": "Test 2", "lastName": "User 2" }, "addresses": [ { "email": "user2@test.com", "phone": "1234567899", "houseNumber": "876", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "1cd039aa-5b86-4e46-8e37-9ef263332c6b", "isDefault": true } ], "customerNumber": "6776445404", "externalObjectReferences": [ { "externalSystemId": "t089999", "externalId": "1324565", "externalIdTypeCode": "201" } ], "createdAt": "2023-05-31T06:39:28.142Z", "customerType": "INDIVIDUAL", "markets": [ { "marketId": "US", "active": true, "currency": "USD", "country": "US", "salesArea": { "salesOrganization": "SE10", "distributionChannel": "00", "division": "00" }, "priceType": "Net" } ], "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b12345", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b12345", "changedAt": "2023-05-31T06:39:28.142Z", "defaultAddress": { "email": "user2@test.com", "phone": "1234567899", "houseNumber": "876", "city": "New Orleans", "state": "LA", "postalCode": "700089", "country": "US", "addressUUID": "1cd039aa-5b86-4e46-8e37-9ef263332c6b", "isDefault": true } } ] } |

Contacts
| accordion |
| --- |
| Request |
| For SAP Commerce Contacts API the value for {SOURCE_PARAMS} is passed as {"object_type":"contacts"} . When encoded in base64, it equates to eyJvYmplY3RfdHlwZSI6ImNvbnRhY3RzIn0= as shown below. code language-shell curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/f5421911-6f6c-41c7-aafa-5d9d2ce51535/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJvYmplY3RfdHlwZSI6ImNvbnRhY3RzIn0=' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' | code language-shell | curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/f5421911-6f6c-41c7-aafa-5d9d2ce51535/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJvYmplY3RfdHlwZSI6ImNvbnRhY3RzIn0=' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |
| code language-shell |
| curl -X GET \ 'https://platform.adobe.io/data/foundation/flowservice/connections/f5421911-6f6c-41c7-aafa-5d9d2ce51535/explore?objectType=rest&object=json&fileType=json&preview=true&sourceParams=eyJvYmplY3RfdHlwZSI6ImNvbnRhY3RzIn0=' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

| accordion |
| --- |
| Response |
| A successful response returns a JSON structure like the following: code language-json { "format": "hierarchical", "schema": { "type": "object", "properties": { "externalObjectReferences": { "type": "array", "items": { "type": "object", "properties": {} } }, "personalInfo": { "type": "object", "properties": { "firstName": { "type": "string" }, "lastName": { "type": "string" } } }, "createdAt": { "type": "string" }, "createdBy": { "type": "string" }, "changedBy": { "type": "string" }, "contactNumber": { "type": "string" }, "changedAt": { "type": "string" } } }, "data": [ { "personalInfo": { "firstName": "Test 1", "lastName": "User 1" }, "createdAt": "2023-05-31T13:33:52.689Z", "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "contactNumber": "4365374130", "changedAt": "2023-05-31T13:33:52.689Z" }, { "personalInfo": { "firstName": "Test 2", "lastName": "User 2" }, "createdAt": "2023-05-31T13:33:52.37Z", "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "contactNumber": "4075431868", "changedAt": "2023-05-31T13:33:52.37Z" } ] } | code language-json | { "format": "hierarchical", "schema": { "type": "object", "properties": { "externalObjectReferences": { "type": "array", "items": { "type": "object", "properties": {} } }, "personalInfo": { "type": "object", "properties": { "firstName": { "type": "string" }, "lastName": { "type": "string" } } }, "createdAt": { "type": "string" }, "createdBy": { "type": "string" }, "changedBy": { "type": "string" }, "contactNumber": { "type": "string" }, "changedAt": { "type": "string" } } }, "data": [ { "personalInfo": { "firstName": "Test 1", "lastName": "User 1" }, "createdAt": "2023-05-31T13:33:52.689Z", "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "contactNumber": "4365374130", "changedAt": "2023-05-31T13:33:52.689Z" }, { "personalInfo": { "firstName": "Test 2", "lastName": "User 2" }, "createdAt": "2023-05-31T13:33:52.37Z", "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "contactNumber": "4075431868", "changedAt": "2023-05-31T13:33:52.37Z" } ] } |
| code language-json |
| { "format": "hierarchical", "schema": { "type": "object", "properties": { "externalObjectReferences": { "type": "array", "items": { "type": "object", "properties": {} } }, "personalInfo": { "type": "object", "properties": { "firstName": { "type": "string" }, "lastName": { "type": "string" } } }, "createdAt": { "type": "string" }, "createdBy": { "type": "string" }, "changedBy": { "type": "string" }, "contactNumber": { "type": "string" }, "changedAt": { "type": "string" } } }, "data": [ { "personalInfo": { "firstName": "Test 1", "lastName": "User 1" }, "createdAt": "2023-05-31T13:33:52.689Z", "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "contactNumber": "4365374130", "changedAt": "2023-05-31T13:33:52.689Z" }, { "personalInfo": { "firstName": "Test 2", "lastName": "User 2" }, "createdAt": "2023-05-31T13:33:52.37Z", "createdBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "changedBy": "sb-subscription-billing!b123456|revenue-cloud!b1234", "contactNumber": "4075431868", "changedAt": "2023-05-31T13:33:52.37Z" } ] } |

### Create a source connection source-connection

You can create a source connection by making a POST request to the /sourceConnections endpoint of the Flow Service API. A source connection consists of a connection ID, a path to the source data file, and a connection spec ID.

**API format**

```
POST /sourceConnections
```

Depending on which object type you are leveraging, select from the tabs below:

Customers
| accordion |
| --- |
| Request |
| The following request creates a source connection for SAP Commerce customers data: code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SAP Commerce Source Connection", "description": "SAP Commerce Source Connection", "baseConnectionId": "f5421911-6f6c-41c7-aafa-5d9d2ce51535", "connectionSpec": { "id": "63d2b27b-69a5-45c9-a7fe-78148a25de3c", "version": "1.0" }, "data": { "format": "json" }, "params": { "object_type": "customers" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Property Description name The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection. description An optional value that you can include to provide more information on your source connection. baseConnectionId The base connection ID of SAP Commerce. This ID was generated in an earlier step. connectionSpec.id The connection specification ID that corresponds to your source. data.format The format of the SAP Commerce data that you want to ingest. Currently, the only supported data format is json . object_type SAP Commerce supports multiple APIs. For customers API, the object_type parameter should be set to customers . path This will have the same value that you select for object_type . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SAP Commerce Source Connection", "description": "SAP Commerce Source Connection", "baseConnectionId": "f5421911-6f6c-41c7-aafa-5d9d2ce51535", "connectionSpec": { "id": "63d2b27b-69a5-45c9-a7fe-78148a25de3c", "version": "1.0" }, "data": { "format": "json" }, "params": { "object_type": "customers" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  | Property | Description | name | The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection. | description | An optional value that you can include to provide more information on your source connection. | baseConnectionId | The base connection ID of SAP Commerce. This ID was generated in an earlier step. | connectionSpec.id | The connection specification ID that corresponds to your source. | data.format | The format of the SAP Commerce data that you want to ingest. Currently, the only supported data format is json. | object_type | SAP Commerce supports multiple APIs. For customers API, the object_type parameter should be set to customers. | path | This will have the same value that you select for object_type. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SAP Commerce Source Connection", "description": "SAP Commerce Source Connection", "baseConnectionId": "f5421911-6f6c-41c7-aafa-5d9d2ce51535", "connectionSpec": { "id": "63d2b27b-69a5-45c9-a7fe-78148a25de3c", "version": "1.0" }, "data": { "format": "json" }, "params": { "object_type": "customers" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| Property | Description |
| name | The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection. |
| description | An optional value that you can include to provide more information on your source connection. |
| baseConnectionId | The base connection ID of SAP Commerce. This ID was generated in an earlier step. |
| connectionSpec.id | The connection specification ID that corresponds to your source. |
| data.format | The format of the SAP Commerce data that you want to ingest. Currently, the only supported data format is json. |
| object_type | SAP Commerce supports multiple APIs. For customers API, the object_type parameter should be set to customers. |
| path | This will have the same value that you select for object_type. |

| accordion |
| --- |
| Response |
| A successful response returns the unique identifier ( id ) of the newly created source connection. This ID is required in a later step to create a dataflow. code language-json { "id": "8f1fc72a-f562-4a1d-8597-85b5ca1b1cd3", "etag": "\"ed05f1e1-0000-0200-0000-6368b8710000\"" } | code language-json | { "id": "8f1fc72a-f562-4a1d-8597-85b5ca1b1cd3", "etag": "\"ed05f1e1-0000-0200-0000-6368b8710000\"" } |
| code language-json |
| { "id": "8f1fc72a-f562-4a1d-8597-85b5ca1b1cd3", "etag": "\"ed05f1e1-0000-0200-0000-6368b8710000\"" } |

Contacts
| accordion |
| --- |
| Request |
| The following request creates a source connection for SAP Commerce contacts data: code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SAP Commerce Source Connection", "description": "SAP Commerce Source Connection", "baseConnectionId": "f5421911-6f6c-41c7-aafa-5d9d2ce51535", "connectionSpec": { "id": "63d2b27b-69a5-45c9-a7fe-78148a25de3c", "version": "1.0" }, "data": { "format": "json" }, "params": { "object_type": "contacts" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 Property Description name The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection. description An optional value that you can include to provide more information on your source connection. baseConnectionId The base connection ID of SAP Commerce. This ID was generated in an earlier step. connectionSpec.id The connection specification ID that corresponds to your source. data.format The format of the SAP Commerce data that you want to ingest. Currently, the only supported data format is json . object_type SAP Commerce supports multiple APIs. For contacts API, the object_type parameter should be set to contacts . path This will have the same value which you select for object_type . | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SAP Commerce Source Connection", "description": "SAP Commerce Source Connection", "baseConnectionId": "f5421911-6f6c-41c7-aafa-5d9d2ce51535", "connectionSpec": { "id": "63d2b27b-69a5-45c9-a7fe-78148a25de3c", "version": "1.0" }, "data": { "format": "json" }, "params": { "object_type": "contacts" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  | Property | Description | name | The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection. | description | An optional value that you can include to provide more information on your source connection. | baseConnectionId | The base connection ID of SAP Commerce. This ID was generated in an earlier step. | connectionSpec.id | The connection specification ID that corresponds to your source. | data.format | The format of the SAP Commerce data that you want to ingest. Currently, the only supported data format is json. | object_type | SAP Commerce supports multiple APIs. For contacts API, the object_type parameter should be set to contacts. | path | This will have the same value which you select for *object_type*. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/sourceConnections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SAP Commerce Source Connection", "description": "SAP Commerce Source Connection", "baseConnectionId": "f5421911-6f6c-41c7-aafa-5d9d2ce51535", "connectionSpec": { "id": "63d2b27b-69a5-45c9-a7fe-78148a25de3c", "version": "1.0" }, "data": { "format": "json" }, "params": { "object_type": "contacts" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| Property | Description |
| name | The name of your source connection. Ensure that the name of your source connection is descriptive as you can use this to look up information on your source connection. |
| description | An optional value that you can include to provide more information on your source connection. |
| baseConnectionId | The base connection ID of SAP Commerce. This ID was generated in an earlier step. |
| connectionSpec.id | The connection specification ID that corresponds to your source. |
| data.format | The format of the SAP Commerce data that you want to ingest. Currently, the only supported data format is json. |
| object_type | SAP Commerce supports multiple APIs. For contacts API, the object_type parameter should be set to contacts. |
| path | This will have the same value which you select for *object_type*. |

| accordion |
| --- |
| Response |
| A successful response returns the unique identifier ( id ) of the newly created source connection. This ID is required in a later step to create a dataflow. code language-json { "id": "8f1fc72a-f562-4a1d-8597-85b5ca1b1cd3", "etag": "\"ed05f1e1-0000-0200-0000-6368b8710000\"" } | code language-json | { "id": "8f1fc72a-f562-4a1d-8597-85b5ca1b1cd3", "etag": "\"ed05f1e1-0000-0200-0000-6368b8710000\"" } |
| code language-json |
| { "id": "8f1fc72a-f562-4a1d-8597-85b5ca1b1cd3", "etag": "\"ed05f1e1-0000-0200-0000-6368b8710000\"" } |

### Create a target XDM schema target-schema

In order for the source data to be used in Experience Platform, a target schema must be created to structure the source data according to your needs. The target schema is then used to create an Experience Platform dataset in which the source data is contained.

A target XDM schema can be created by performing a POST request to the [Schema Registry API](https://developer.adobe.com/experience-platform-apis/references/schema-registry/).

For detailed steps on how to create a target XDM schema, see the tutorial on [creating a schema using the API](/en/docs/experience-platform/xdm/api/schemas#create-a-schema).

### Create a target dataset target-dataset

A target dataset can be created by performing a POST request to the [Catalog Service API](https://developer.adobe.com/experience-platform-apis/references/catalog/), providing the ID of the target schema within the payload.

For detailed steps on how to create a target dataset, see the tutorial on [creating a dataset using the API](/en/docs/experience-platform/catalog/api/create-dataset).

### Create a target connection target-connection

A target connection represents the connection to the destination where the ingested data is to be stored. To create a target connection, you must provide the fixed connection spec ID that corresponds to the data lake. This ID is: c604ff05-7f1a-43c0-8e18-33bf874cb11c.

You now have the unique identifiers a target schema a target dataset and the connection spec ID to the data lake. Using these identifiers, you can create a target connection using the Flow Service API to specify the dataset that will contain the inbound source data.

**API format**

```
POST /targetConnections
```

**Request**

The following request creates a target connection for SAP Commerce:

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/targetConnections' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "SAP Commerce Target Connection Generic Rest",
      "description": "SAP Commerce Target Connection Generic Rest",
      "connectionSpec": {
          "id": "c604ff05-7f1a-43c0-8e18-33bf874cb11c",
          "version": "1.0"
      },
      "data": {
          "format": "parquet_xdm",
          "schema": {
              "id": "https://ns.adobe.com/{TENANT_ID}/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473",
              "version": "1.2"
          }
      },
      "params": {
          "dataSetId": "645923cd7aeeea1c06c5e92e"
      }
  }'
```

Property
Description
name
The name of your target connection. Ensure that the name of your target connection is descriptive as you can use this to look up information on your target connection.
description
An optional value that you can include to provide more information on your target connection.
connectionSpec.id
The connection specification ID that corresponds to data lake. This fixed ID is:
6b137bf6-d2a0-48c8-914b-d50f4942eb85
.
data.format
The format of the SAP Commerce data that you want to ingest.
params.dataSetId
The target dataset ID retrieved in a previous step.
**Response**

A successful response returns the new target connection’s unique identifier (id). This ID is required in later steps.

```
{
    "id": "5b72a4b6-2fb8-4ca7-8ad8-4114a3063c5c",
    "etag": "\"db00c6dc-0000-0200-0000-6482d8280000\""
}
```

### Create a mapping mapping

In order for the source data to be ingested into a target dataset, it must first be mapped to the target schema that the target dataset adheres to. This is achieved by performing a POST request to [Data Prep API](https://www.adobe.io/experience-platform-apis/references/data-prep/) with data mappings defined within the request payload.

**API format**

```
POST /conversion/mappingSets
```

Customers
| accordion |
| --- |
| Request |
| The following request creates a mapping for SAP Commerce Customers API data code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/conversion/mappingSets' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/b156e6f818f923e048199173c45e55e20fd2487f5eb03d22", "contentType": "application/vnd.adobe.xed-full+json;version=1" } }, "mappings": [ { "sourceType": "ATTRIBUTE", "source": "customerNumber", "destination": "_extconndev.customerNumber" }, { "sourceType": "ATTRIBUTE", "source": "customerType", "destination": "_extconndev.customerType" }, { "sourceType": "ATTRIBUTE", "source": "changedAt", "destination": "_extconndev.changedAt" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].email", "destination": "_extconndev.addresses[*].email" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].city", "destination": "_extconndev.addresses[*].city" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].addressUUID", "destination": "_extconndev.addresses[*].addressUUID" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalSystemId", "destination": "_extconndev.externalObjectReferences[*].externalSystemId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalId", "destination": "_extconndev.externalObjectReferences[*].externalId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalIdTypeCode", "destination": "_extconndev.externalObjectReferences[*].externalIdTypeCode" }, { "sourceType": "ATTRIBUTE", "source": "customReferences[*].id", "destination": "_extconndev.customReferences[*].id" }, { "sourceType": "ATTRIBUTE", "source": "customReferences[*].typeCode", "destination": "_extconndev.customReferences[*].typeCode" } ], "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473", "contentType": "application/vnd.adobe.xed-full+json;version=1" } } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Property Description outputSchema.schemaRef.id The ID of the target XDM schema generated in an earlier step. mappings.sourceType The source attribute type that is being mapped. mappings.source The source attribute that needs to be mapped to a destination XDM path. mappings.destination The destination XDM path where the source attribute is being mapped to. | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/conversion/mappingSets' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/b156e6f818f923e048199173c45e55e20fd2487f5eb03d22", "contentType": "application/vnd.adobe.xed-full+json;version=1" } }, "mappings": [ { "sourceType": "ATTRIBUTE", "source": "customerNumber", "destination": "_extconndev.customerNumber" }, { "sourceType": "ATTRIBUTE", "source": "customerType", "destination": "_extconndev.customerType" }, { "sourceType": "ATTRIBUTE", "source": "changedAt", "destination": "_extconndev.changedAt" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].email", "destination": "_extconndev.addresses[*].email" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].city", "destination": "_extconndev.addresses[*].city" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].addressUUID", "destination": "_extconndev.addresses[*].addressUUID" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalSystemId", "destination": "_extconndev.externalObjectReferences[*].externalSystemId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalId", "destination": "_extconndev.externalObjectReferences[*].externalId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalIdTypeCode", "destination": "_extconndev.externalObjectReferences[*].externalIdTypeCode" }, { "sourceType": "ATTRIBUTE", "source": "customReferences[*].id", "destination": "_extconndev.customReferences[*].id" }, { "sourceType": "ATTRIBUTE", "source": "customReferences[*].typeCode", "destination": "_extconndev.customReferences[*].typeCode" } ], "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473", "contentType": "application/vnd.adobe.xed-full+json;version=1" } } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  | Property | Description | outputSchema.schemaRef.id | The ID of the [target XDM schema](#target-schema) generated in an earlier step. | mappings.sourceType | The source attribute type that is being mapped. | mappings.source | The source attribute that needs to be mapped to a destination XDM path. | mappings.destination | The destination XDM path where the source attribute is being mapped to. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/conversion/mappingSets' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/b156e6f818f923e048199173c45e55e20fd2487f5eb03d22", "contentType": "application/vnd.adobe.xed-full+json;version=1" } }, "mappings": [ { "sourceType": "ATTRIBUTE", "source": "customerNumber", "destination": "_extconndev.customerNumber" }, { "sourceType": "ATTRIBUTE", "source": "customerType", "destination": "_extconndev.customerType" }, { "sourceType": "ATTRIBUTE", "source": "changedAt", "destination": "_extconndev.changedAt" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].email", "destination": "_extconndev.addresses[*].email" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].city", "destination": "_extconndev.addresses[*].city" }, { "sourceType": "ATTRIBUTE", "source": "addresses[*].addressUUID", "destination": "_extconndev.addresses[*].addressUUID" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalSystemId", "destination": "_extconndev.externalObjectReferences[*].externalSystemId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalId", "destination": "_extconndev.externalObjectReferences[*].externalId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalIdTypeCode", "destination": "_extconndev.externalObjectReferences[*].externalIdTypeCode" }, { "sourceType": "ATTRIBUTE", "source": "customReferences[*].id", "destination": "_extconndev.customReferences[*].id" }, { "sourceType": "ATTRIBUTE", "source": "customReferences[*].typeCode", "destination": "_extconndev.customReferences[*].typeCode" } ], "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473", "contentType": "application/vnd.adobe.xed-full+json;version=1" } } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| Property | Description |
| outputSchema.schemaRef.id | The ID of the [target XDM schema](#target-schema) generated in an earlier step. |
| mappings.sourceType | The source attribute type that is being mapped. |
| mappings.source | The source attribute that needs to be mapped to a destination XDM path. |
| mappings.destination | The destination XDM path where the source attribute is being mapped to. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created mapping including its unique identifier ( id ). This value is required in a later step to create a dataflow. code language-json { "id": "ddf0592bcc9d4ac391803f15f2429f87", "version": 0, "createdDate": 1597784069368, "modifiedDate": 1597784069368, "createdBy": "{CREATED_BY}", "modifiedBy": "{MODIFIED_BY}" } | code language-json | { "id": "ddf0592bcc9d4ac391803f15f2429f87", "version": 0, "createdDate": 1597784069368, "modifiedDate": 1597784069368, "createdBy": "{CREATED_BY}", "modifiedBy": "{MODIFIED_BY}" } |
| code language-json |
| { "id": "ddf0592bcc9d4ac391803f15f2429f87", "version": 0, "createdDate": 1597784069368, "modifiedDate": 1597784069368, "createdBy": "{CREATED_BY}", "modifiedBy": "{MODIFIED_BY}" } |

Contacts
| accordion |
| --- |
| Request |
| The following request creates a mapping for SAP Commerce Contacts API data code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/conversion/mappingSets' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/b156e6f818f923e048199173c45e55e20fd2487f5eb03d22", "contentType": "application/vnd.adobe.xed-full+json;version=1" } }, "mappings": [ { "sourceType": "ATTRIBUTE", "source": "contactNumber", "destination": "_extconndev.contactNumber" }, { "sourceType": "ATTRIBUTE", "source": "createdAt", "destination": "_extconndev.createdAt" }, { "sourceType": "ATTRIBUTE", "source": "changedAt", "destination": "_extconndev.changedAt" }, { "sourceType": "ATTRIBUTE", "source": "personalInfo.lastName", "destination": "_extconndev.personalInfo.lastName" }, { "sourceType": "ATTRIBUTE", "source": "personalInfo.firstName", "destination": "_extconndev.personalInfo.firstName" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectRefereneces[*].externalSystemId", "destination": "_extconndev.externalObjectReferences[*].externalSystemId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalId", "destination": "_extconndev.externalObjectReferences[*].externalId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalIdTypeCode", "destination": "_extconndev.externalObjectReferences[*].externalIdTypeCode" } ], "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/extconndev/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473", "contentType": "application/vnd.adobe.xed-full+json;version=1" } } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 Property Description outputSchema.schemaRef.id The ID of the target XDM schema generated in an earlier step. mappings.sourceType The source attribute type that is being mapped. mappings.source The source attribute that needs to be mapped to a destination XDM path. mappings.destination The destination XDM path where the source attribute is being mapped to. | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/conversion/mappingSets' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/b156e6f818f923e048199173c45e55e20fd2487f5eb03d22", "contentType": "application/vnd.adobe.xed-full+json;version=1" } }, "mappings": [ { "sourceType": "ATTRIBUTE", "source": "contactNumber", "destination": "_extconndev.contactNumber" }, { "sourceType": "ATTRIBUTE", "source": "createdAt", "destination": "_extconndev.createdAt" }, { "sourceType": "ATTRIBUTE", "source": "changedAt", "destination": "_extconndev.changedAt" }, { "sourceType": "ATTRIBUTE", "source": "personalInfo.lastName", "destination": "_extconndev.personalInfo.lastName" }, { "sourceType": "ATTRIBUTE", "source": "personalInfo.firstName", "destination": "_extconndev.personalInfo.firstName" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectRefereneces[*].externalSystemId", "destination": "_extconndev.externalObjectReferences[*].externalSystemId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalId", "destination": "_extconndev.externalObjectReferences[*].externalId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalIdTypeCode", "destination": "_extconndev.externalObjectReferences[*].externalIdTypeCode" } ], "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/extconndev/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473", "contentType": "application/vnd.adobe.xed-full+json;version=1" } } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  | Property | Description | outputSchema.schemaRef.id | The ID of the [target XDM schema](#target-schema) generated in an earlier step. | mappings.sourceType | The source attribute type that is being mapped. | mappings.source | The source attribute that needs to be mapped to a destination XDM path. | mappings.destination | The destination XDM path where the source attribute is being mapped to. |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/conversion/mappingSets' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/{TENANT_ID}/schemas/b156e6f818f923e048199173c45e55e20fd2487f5eb03d22", "contentType": "application/vnd.adobe.xed-full+json;version=1" } }, "mappings": [ { "sourceType": "ATTRIBUTE", "source": "contactNumber", "destination": "_extconndev.contactNumber" }, { "sourceType": "ATTRIBUTE", "source": "createdAt", "destination": "_extconndev.createdAt" }, { "sourceType": "ATTRIBUTE", "source": "changedAt", "destination": "_extconndev.changedAt" }, { "sourceType": "ATTRIBUTE", "source": "personalInfo.lastName", "destination": "_extconndev.personalInfo.lastName" }, { "sourceType": "ATTRIBUTE", "source": "personalInfo.firstName", "destination": "_extconndev.personalInfo.firstName" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectRefereneces[*].externalSystemId", "destination": "_extconndev.externalObjectReferences[*].externalSystemId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalId", "destination": "_extconndev.externalObjectReferences[*].externalId" }, { "sourceType": "ATTRIBUTE", "source": "externalObjectReferences[*].externalIdTypeCode", "destination": "_extconndev.externalObjectReferences[*].externalIdTypeCode" } ], "outputSchema": { "schemaRef": { "id": "https://ns.adobe.com/extconndev/schemas/325fd5394ba421246b05c0a3c2cd5efeec2131058a63d473", "contentType": "application/vnd.adobe.xed-full+json;version=1" } } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| Property | Description |
| outputSchema.schemaRef.id | The ID of the [target XDM schema](#target-schema) generated in an earlier step. |
| mappings.sourceType | The source attribute type that is being mapped. |
| mappings.source | The source attribute that needs to be mapped to a destination XDM path. |
| mappings.destination | The destination XDM path where the source attribute is being mapped to. |

| accordion |
| --- |
| Response |
| A successful response returns details of the newly created mapping including its unique identifier ( id ). This value is required in a later step to create a dataflow. code language-json { "id": "ddf0592bcc9d4ac391803f15f2429f87", "version": 0, "createdDate": 1597784069368, "modifiedDate": 1597784069368, "createdBy": "{CREATED_BY}", "modifiedBy": "{MODIFIED_BY}" } | code language-json | { "id": "ddf0592bcc9d4ac391803f15f2429f87", "version": 0, "createdDate": 1597784069368, "modifiedDate": 1597784069368, "createdBy": "{CREATED_BY}", "modifiedBy": "{MODIFIED_BY}" } |
| code language-json |
| { "id": "ddf0592bcc9d4ac391803f15f2429f87", "version": 0, "createdDate": 1597784069368, "modifiedDate": 1597784069368, "createdBy": "{CREATED_BY}", "modifiedBy": "{MODIFIED_BY}" } |

### Create a flow flow

The last step towards bringing data from SAP Commerce to Experience Platform is to create a dataflow. By now, you have the following required values prepared:

- [Source connection ID](#source-connection)
- [Target connection ID](#target-connection)
- [Mapping ID](#mapping)

A dataflow is responsible for scheduling and collecting data from a source. You can create a dataflow by performing a POST request while providing the previously mentioned values within the payload.

**API format**

```
POST /flows
```

**Request**

```
curl -X POST \
  'https://platform.adobe.io/data/foundation/flowservice/flows' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}' \
  -H 'Content-Type: application/json' \
  -d '{
      "name": "SAP Commerce Connector Description Flow Generic Rest",
      "description": "SAP Commerce Connector Description Flow Generic Rest",
      "flowSpec": {
          "id": "6499120c-0b15-42dc-936e-847ea3c24d72",
          "version": "1.0"
      },
      "sourceConnectionIds": [
          "2ef2e831-f4f1-4363-a0f7-08b4ea347164"
      ],
      "targetConnectionIds": [
          "5b72a4b6-2fb8-4ca7-8ad8-4114a3063c5c"
      ],
      "transformations": [
          {
              "name": "Mapping",
              "params": {
                  "mappingId": "ddf0592bcc9d4ac391803f15f2429f87",
                  "mappingVersion": "0"
              }
          }
      ],
      "scheduleParams": {
          "startTime": "1625040887",
          "frequency": "once",
      }
  }'
```

Property
Description
name
The name of your dataflow. Ensure that the name of your dataflow is descriptive as you can use this to look up information on your dataflow.
description
An optional value that you can include to provide more information on your dataflow.
flowSpec.id
The flow specification ID required to create a dataflow. This fixed ID is:
6499120c-0b15-42dc-936e-847ea3c24d72
.
flowSpec.version
The corresponding version of the flow specification ID. This value defaults to
1.0
.
sourceConnectionIds
The
source connection ID
generated in an earlier step.
targetConnectionIds
The
target connection ID
generated in an earlier step.
transformations
This property contains the various transformations that are needed to be applied to your data. This property is required when bringing non-XDM-compliant data to Experience Platform.
transformations.name
The name assigned to the transformation.
transformations.params.mappingId
The
mapping ID
generated in an earlier step.
transformations.params.mappingVersion
The corresponding version of the mapping ID. This value defaults to
0
.
scheduleParams.startTime
This property contains information on the ingestion scheduling of the dataflow.
scheduleParams.frequency
The frequency at which the dataflow will collect data.
scheduleParams.interval
The interval designates the period between two consecutive flow runs. The interval’s value should be a non-zero integer.
**Response**

A successful response returns the ID (id) of the newly created dataflow. You can use this ID to monitor, update, or delete your dataflow.

```
{
     "id": "fcd16140-81b4-422a-8f9a-eaa92796c4f4",
     "etag": "\"9200a171-0000-0200-0000-6368c1da0000\""
}
```

## Appendix

The following section provides information on the steps you can to monitor, update, and delete your dataflow.

### Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to see information on flow runs, completion status, and errors. For complete API examples, read the guide on [monitoring your sources dataflows using the API](/en/docs/experience-platform/sources/api-tutorials/monitor).

### Update your dataflow

Update the details of your dataflow, such as its name and description, as well as its run schedule and associated mapping sets by making a PATCH request to the /flows endpoint of Flow Service API, while providing the ID of your dataflow. When making a PATCH request, you must provide your dataflow’s unique etag in the If-Match header. For complete API examples, read the guide on [updating sources dataflows using the API](/en/docs/experience-platform/sources/api-tutorials/update-dataflows).

### Update your account

Update the name, description, and credentials of your source account by performing a PATCH request to the Flow Service API while providing your base connection ID as a query parameter. When making a PATCH request, you must provide your source account’s unique etag in the If-Match header. For complete API examples, read the guide on [updating your source account using the API](/en/docs/experience-platform/sources/api-tutorials/update).

### Delete your dataflow

Delete your dataflow by performing a DELETE request to the Flow Service API while providing the ID of the dataflow you want to delete as part of the query parameter. For complete API examples, read the guide on [deleting your dataflows using the API](/en/docs/experience-platform/sources/api-tutorials/delete-dataflows).

### Delete your account

Delete your account by performing a DELETE request to the Flow Service API while providing the base connection ID of the account you want to delete. For complete API examples, read the guide on [deleting your source account using the API](/en/docs/experience-platform/sources/api-tutorials/delete).

recommendation-more-help
