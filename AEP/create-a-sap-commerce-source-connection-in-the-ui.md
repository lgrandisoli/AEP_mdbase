---
title: "Create a SAP Commerce source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/ecommerce/sap-commerce"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:21.208165+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a SAP Commerce source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

The following tutorial walks you through the steps to create a SAP Commerce source connection to bring [SAP Subscription Billing](https://www.sap.com/products/financial-management/subscription-billing.html) contacts and customer data using the Adobe Experience Platform user interface.

## Getting started getting-started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid SAP Commerce account, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/ecommerce).

### Gather required credentials gather-credentials

In order to connect SAP Commerce to Experience Platform, you must provide values for the following connection properties:

Credential
Description
Client ID
The value of
clientId
from the service key.
Client secret
The value of
clientSecret
from the service key.
Token endpoint
The value of
url
from the service key, it will be similar to
https://subscriptionbilling.authentication.eu10.hana.ondemand.com
.
Region
Your data center location. The region is present in the
url
and has a value similar to
eu10
or
us10
. For example if the
url
is
https://eu10.revenue.cloud.sap/api
you will need
eu10
.
For more information, please refer to the [SAP Commerce documentation](https://help.sap.com/docs/CLOUD_TO_CASH_OD/987aec876092428f88162e438acf80d6/c5fcaf96daff4c7a8520188e4d8a1843.html).

### Create an Experience Platform schema create-platform-schema

Before creating a SAP Commerce source connection, you must also ensure that you first create an Experience Platform schema to use for your source. See the tutorial on [creating an Experience Platform schema](/en/docs/experience-platform/xdm/schema/composition) for comprehensive steps on how to create a schema.

Expand the following section to view an example schema.

View schema example
| code language-none |
| --- |
| { "_extconndev": { "addresses": [ { "addressUUID": "{ADDRESS_UUID}", "city": "Burnaby", "country": "Canada", "email": "chandni@acme.com", "houseNumber": "27", "isDefault": false, "phone": "123-456-7890", "postalCode": "V3J 1X9", "state": "British Columbia", "street": "Beresford" } ], "changedAt": "1687204041", "changedBy": "vero@acme.com", "contactNumber": "123-456-7980", "corporateInfo": { "company": "acme" }, "createAt": "1687204041", "createdBy": "vero@acme.com", "customReferences": [ { "id": "Sample value", "typeCode": "Sample value" } ], "customerNumber": "Sample value", "customerType": "Sample value", "defaultAddress": { "addressUUID": "Sample value", "city": "North Vancouver", "country": "Canada", "email": "chandni@acme.come", "houseNumber": "34", "isDefault": false, "phone": "123-456-7890", "postalCode": "V7H 2P1", "state": "British Columbia", "street": "Maple" }, "externalObjectReferences": [ { "externalId": "{EXTERNAL_ID}", "externalIdTypeCode": "{EXTERNAL_ID_TYPE_CODE}", "externalSystemId": "{EXTERNAL_SYSTEM_ID}" } ], "markets": [ { "active": false, "country": "USA", "currency": "USD", "marketId": "Sample value", "priceinfo": { "incoterms": "{INCO_TERMS}", "incotermsLocation": "{INCO_TERMS_LOCATION}", "priceGroup": "{PRICE_GROUP}", "priceListType": "{PRICE_LIST_TYPE}" }, "salesArea": { "distributionChannel": "{DISTRIBUTION_CHANNEL}", "division": "{DIVISION}", "salesOrganization": "{SALES_ORGANIZATION}" } } ], "personalInfo": { "firstName": "Chandni", "lastName": "Kaur" } }, "_id": "/uri-reference", "_repo": { "createDate": "2004-10-23T12:00:00-06:00", "modifyDate": "2004-10-23T12:00:00-06:00" }, "createdByBatchID": "/uri-reference", "modifiedByBatchID": "/uri-reference", "personID": "{PERSON_ID}", "repositoryCreatedBy": "kevin@acme.com", "repositoryLastModifiedBy": "kevin@acme.com" } |

## Connect your SAP Commerce account connect-account

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *eCommerce* category, select **SAP Commerce**, and then select **Add data**.

The **Connect SAP Commerce account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account existing-account

To use an existing account, select the SAP Commerce account you want to create a new dataflow with, then select **Next** to proceed.

### New account new-account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

### Select data select-data

Finally, you must select the object type that you want to ingest to Experience Platform.

Object type
Description
Customers
The entities who have subscriptions.
Contacts
The contact details for customers.
Customers
To ingest customer data, select **Customers** as your object type and then select **Next**.

Contacts
To ingest contact data, select **Contacts** as your object type and then select **Next**.

## Next steps next-steps

By following this tutorial, you have established a connection to your SAP Commerce account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/ecommerce).

## Additional resources additional-resources

The sections below provide additional resources that you can refer to when using the SAP Commerce source.

### Mapping mapping

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Mapping configurations for your dataflow will differ depending on your schema and the object type that you select to ingest.

Customers
For customer data, SAP Commerce uses the [customers](https://api.sap.com/api/BusinessPartner_APIs/path/GET_customers) and the [customer-contacts relationships](https://api.sap.com/api/BusinessPartner_APIs/path/GET_relationships-customer-contacts) endpoints of the SAP Business Partners API to retrieve the data

The following is an example of mapping configurations for SAP Commerce dataflow for customer data:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 |  |
| --- | --- |
| Target Field | Description |
| customerNumber | The customer’s number. |
| corporateInfo | The customer’s number. |
| customerType | The customer type. |
| createdAt | A timestamp indicating when the customer was created. |
| changedAt | A timestamp indicating when the customer was last updated. |
| markets[*].country | The customers markets, retrieved as an array object. |
| addresses[*].email | Emails associated with the customer’s multiple addresses, retrieved as an array object. |
| addresses[*].city | Cities associated with the customer’s multiple addresses, retrieved as an array object. |
| addresses[*].addressUUID | ID’s associated with the customer’s multiple addresses, retrieved as an array object. |
| externalObjectReferences[*].externalSystemId | Additional data, retrieved as an array object. |
| externalObjectReferences[*].externalId | Additional data, retrieved as an array object. |
| customReferences[*].id | Additional data, retrieved as an array object. |
| customReferences[*].typeCode | Additional data, retrieved as an array object. |

Contacts
For contact data, SAP Commerce uses the [contacts](https://api.sap.com/api/BusinessPartner_APIs/path/GET_contacts) endpoint of the SAP Business Partners API to retrieve the data.

The following is an example of mapping configurations for SAP Commerce dataflow for contact data:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 |  |
| --- | --- |
| Target Field | Description |
| contactNumber | The contact’s number. |
| createdAt | A timestamp indicating when the contact was created. |
| changedAt | A timestamp indicating when the contact was last updated. |
| personalInfo.lastName | The contact’s Last Name. |
| personalInfo.firstName | The contact’s First Name. |
| externalObjectReferences[*].externalSystemId | Additional data, retrieved as an array object. |
| externalObjectReferences[*].externalId | Additional data, retrieved as an array object. |
| externalObjectReferences[*].externalIdTypeCode | Additional data, retrieved as an array object. |

recommendation-more-help
