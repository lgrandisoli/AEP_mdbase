---
title: "Identity Service troubleshooting guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/identity/troubleshooting-guide"
category: "guides"
topic: "experience-platform/experience-platform-identity-service-guide"
created_at: "2026-06-26T17:26:10.843566+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform Identity Service Guide

# Identity Service troubleshooting guide

Last update: June 18, 2026
- Topics:
- [Identities](#)

CREATED FOR:

- Admin
- Developer

This document provides answers to frequently asked questions about Adobe Experience Platform Identity Service, as well as a troubleshooting guide for common errors. For questions and troubleshooting regarding Experience Platform APIs in general, see the [Adobe Experience Platform API troubleshooting guide](/en/docs/experience-platform/landing/troubleshooting).

Data that identifies a single customer is often fragmented across the various devices and systems that they use to engage with your brand. Identity Service gathers these fragmented identities together, facilitating a complete understanding of customer behavior so you can deliver impactful digital experiences in real time. For more information, see the [Identity Service overview](/en/docs/experience-platform/identity/home).

## FAQ

The following is a list of answers to frequently asked questions about Identity Service.

## What is identity data?

Identity data is any data that can be used to identify an individual person. Depending on the context of how the data is used within your organization, identity data can include usernames, email addresses, and IDs from CRM systems. Identity data is not limited to registered users of your website or service, as anonymous users can also be identified by their device or cookie ID.

## What is the benefit of labeling data fields as identities?

Labeling certain data fields as identities in your record and time series data allows you to map identity relationships within the natural structure of your data and reconcile duplicate data cross channels. See the [Identity Service overview](/en/docs/experience-platform/identity/home) for more information.

## What are known and anonymous identities?

A known identity refers to an identity value that can be used on its own or with other information to identify, contact, or locate an individual person. Examples of known identities may include email addresses, phone numbers, and CRMIDs.

An anonymous identity refers to an identity value that cannot be used on its own or with other information to identify, contact, or locate an individual person (such as a cookie ID).

## What is a Private Identity Graph?

A Private Identity Graph is a private map of relationships between stitched and linked identities, visible only to your organization.

When more than one identity is included in any data ingested from a streaming endpoint or sent to a dataset enabled for Identity Service, those identities are linked in the Private Identity Graph. Identity Service leverages this graph to glean identities for a given consumer or entity, allowing for identity stitching and profile merging.

## How do I create multiple identity fields within an XDM schema?

[Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home) schemas support multiple identity fields. Any data field of type string within a schema that implements the XDM Individual Profile or XDM ExperienceEvent class can be labeled as an identity field. Once labeled, any data contained in these fields is added to the profile’s identity map.

For steps on how to label an XDM field as an identity field using the user interface, see the [Identity section](/en/docs/experience-platform/xdm/tutorials/create-schema-ui) in the Schema Editor tutorial. If you are using the API, see the [Identity descriptor section](/en/docs/experience-platform/xdm/tutorials/create-schema-api) in the Schema Registry API tutorial.

## Are there contexts where some fields should not be labeled as identities?

Identity fields should be reserved for values that are unique to each individual. For example, consider a dataset for a customer loyalty program. The “loyalty level” field (gold, silver, bronze) would not be a useful identity field, whereas the loyalty ID—a unique value—would be.

Fields like ZIP codes and IP addresses should not be labeled as identities for individuals, as these values can apply to more than one individual person. These types of fields should only be labeled as identities for household-level marketing strategies.

## Why are my identity fields not linking the way I expect?

Using the [/cluster/members endpoint](/en/docs/experience-platform/identity/api/list-cluster-identites) in the Identity Service API, you can view the associated identities for one or more identity fields. If the response does not return the linked identities you expect, ensure that you are providing the appropriate identity information in your XDM data. See the section on [providing XDM data to Identity Service](/en/docs/experience-platform/identity/home) in the Identity Service overview for more information.

## What is an identity namespace?

An identity namespace gives context for how identity fields relate to a customer’s identity. For example, identity fields under the “Email” namespace should conform to a standard email format (name@emailprovider.com) whereas fields using the “Phone” namespace should conform to a standard phone number (such as 987-555-1234 in North America).

Namespaces distinguish similar identity values between different CRM systems. For example, consider a profile that contains a numerical Loyalty ID associated with your company’s rewards program. A namespace of “Loyalty” would separate this value from a similar numeric ID for your eCommerce system that also appears in the same profile.

See the [identity namespace overview](/en/docs/experience-platform/identity/home) for more information.

## How do I associate an identity with an identity namespace?

Identity fields must be associated with an existing identity namespace when they are created. Any new namespaces must be [created using the API](#how-do-i-create-a-custom-namespace-for-my-organization) before associating them with identity fields.

For step-by-step instructions for defining a namespace when creating an identity descriptor using the API, please see the section on [creating a descriptor](/en/docs/experience-platform/xdm/tutorials/create-schema-ui) in the Schema Registry developer guide. For marking a schema field as an identity in the UI, follow the steps in the [Schema Editor tutorial](/en/docs/experience-platform/xdm/tutorials/create-schema-api).

## What are the standard identity namespaces provided by Experience Platform? standard-namespaces

Standard identity namespaces are namespaces available to all organizations. See the [Identity namespaces overview](/en/docs/experience-platform/identity/features/namespaces) for a full list of available standard namespaces.

## Where can I find the list of identity namespaces available for my organization?

Using the [Identity Service API](https://www.adobe.io/experience-platform-apis/references/identity-service), you can list all available identity namespaces for your organization by making a GET request to the /idnamespace/identities endpoint. See the section on [listing available namespaces](/en/docs/experience-platform/identity/api/list-namespaces) in the Identity Service API overview for more information.

## How do I create a custom namespace for my organization?

Using the [Identity Service API](https://www.adobe.io/experience-platform-apis/references/identity-service), you can create a custom identity namespace for your organization by making a POST request to the /idnamespace/identities endpoint. See the section on [creating a custom namespace](/en/docs/experience-platform/identity/api/create-custom-namespace) in the Identity Service API overview for more information.

## What are composite identities and XIDs?

Identities are referenced in API calls either by their composite identity or XID. A composite identity is a representation of an identity that contains an ID value and a namespace. An XID is a single-value identifier that represents the same construct as a composite identity (an ID and a namespace), and is automatically assigned to new identities when persisted by Identity Service. See the [Identity Service API overview](/en/docs/experience-platform/identity/home) for more information.

## How does Identity Service handle personally identifiable information (PII)?

Identity Service has standard namespaces to support the ingestion of hashed identity values for phone numbers and emails. However, you are responsible for the hashing of values. To learn more about hashing data that is ingested into Experience Platform, see the [Data Prep mapping functions guide](/en/docs/experience-platform/data-prep/functions#hashing).

## Are there any considerations when hashing PII-based identities?

If you are sending hashed PII values to Identity Service, you must use the same encryption method across your datasets. This ensures that the same identity value across datasets generates the same hashed values and are able to be properly matched and linked in the identity graph.

## Why can’t I access the identity graph page or APIs?

Your Experience Platform administrator must provision you with the view-identity-graph permission in order for you to view identity graph data. Without this permission, you will receive a permission denied message on the identity graph viewer page and when calling Experience Platform APIs. See the [access control overvew](/en/docs/experience-platform/access-control/home) for more information on permissions.

## Troubleshooting

The following section provides troubleshooting suggestions for specific error codes and unexpected behavior you may encounter while working with the Identity Service API.

## Identity Service error messages

The following is a list of error messages you may encounter when using the Identity Service API.

### Missing required query parameter

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "Missing required query parameter - namespace"
}
```

This error displays when a required query parameter was not included in the request path. The detail of the error message provides the name of the missing parameter. Variations of this error message include:

- Missing required query parameter – nsId
- Missing required query parameter – id
- Missing required query parameter – xid or (nsid,id)
- Missing required query parameter – targetNs
- Missing required query parameter – xids or compositeXids

Check that you are properly including the indicated parameter in the request path before trying again.

### Timestamp should be within last 180 days

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "Timestamp should be within last 180 days"
}
```

Identity Service purges data older than 180 days. This error message displays when you attempt to access data older than this.

### There is a limit of 1000 XIDs in a single call

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "There is a limit of 1000 XIDs in a single call"
}
```

This error message displays when you attempt to retrieve identity information for more than the maximum number of [XIDs](#what-are-composite-identities-and-xids) permitted in a single API call. Reduce the number of XIDs in your request to below the displayed limit to resolve this issue.

### There is a limit for 1000 compositeXids in a single call

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "There is a limit for 1000 compositeXids in a single call"
}
```

This error message displays when you attempt to retrieve identity information for more than the maximum number of [composite identities](#what-are-composite-identities-and-xids) permitted in a single API call. Reduce the number of composite identities in your request to below the displayed limit to resolve this issue.

### The graph-type specified is invalid

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "The graph-type abc specified is invalid. Please provide a valid graph-type"
}
```

This error message displays when a graph-type query parameter is given an invalid value in the request path. See the section on [identity graphs](/en/docs/experience-platform/identity/home) in the Identity Service overview to learn which graph-types are supported.

### Service token does not have valid scope

```
{
    "title": "UnauthorizedAccess",
    "status": 401,
    "detail": "Service token does not have valid scope. Either acp.core.identity or acp.foundation is required"
}
```

This error message displays when your organization has not been provisioned with the proper permissions for Identity Service. Contact your system administrator to resolve this issue.

### Gateway service token is not valid

```
{
    "title": "UnauthorizedAccess",
    "status": 401,
    "detail": "Gateway service token is not valid"
}
```

In the case of this error, your access token is invalid. Access tokens expire every 24 hours and must be regenerated to continue using Experience Platform APIs. See the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) for instructions on generating new access tokens.

### Authorization service token is not valid

```
{
    "title": "UnauthorizedAccess",
    "status": 401,
    "detail": "Authorization service token is not valid"
}
```

In the case of this error, your access token is invalid. Access tokens expire every 24 hours and must be regenerated to continue using Experience Platform APIs. See the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) for instructions on generating new access tokens.

### User token does not have valid product context

```
{
    "title": "UnauthorizedAccess",
    "status": 401,
    "detail": "User token does not have valid product context"
}
```

This error message displays when your access token has not been generated from an Experience Platform integration. See the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) for instructions on generating new access tokens for an Experience Platform integration.

### Internal error when getting native XID from identity and namespace code

```
{
    "title": "UnauthorizedAccess",
    "status": 401,
    "detail": "Invalid IMS Token/IMS Org | Internal error - when tried to get native XID from identity and namespace code"
}
```

When Identity Service persists an identity, the identity’s ID and associated namespace ID are assigned a unique identifier called an XID. This message displays when an error occurs during the process of finding the XID for a given ID value and namespace.

### The IMS Org is not provisioned for Identity Service usage

```
{
    "title": "AccountNotProvisioned",
    "status": 403,
    "detail": "The IMS Org. {IMS_ORG_NAME} is not provisioned for Identity Service usage"
}
```

This error message displays when your organization has not been provisioned with the proper permissions for Identity Service. Contact your system administrator to resolve this issue.

### Internal Server Error

```
{
    "title": "InternalError",
    "status": 500,
    "detail": "Internal Server Error. There was a problem processing your request"
}
```

This error displays when an unexpected exception occurs in the execution of an Experience Platform service call. Best practice is to program your automated calls to retry their requests a few times at a timed interval when receiving this error. If the problem persists, contact your system administrator.

## Batch Ingestion error codes

Identity Service ingests identity data from record and time series data that is uploaded to Experience Platform using Batch Ingestion. As batch ingestion is an asynchronous process, you must view the details for a batch to view errors. Errors will accumulate as the batch progresses until the batch is complete.

The following is a list of error messages related to Identity Service you may encounter when using the [Batch Ingestion API](https://developer.adobe.com/experience-platform-apis/references/batch-ingestion/).

### Unknown XDM schema

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "Unknown XDM schema"
}
```

Identity Service only consumes identities for record or time series data that conforms to the Profile or ExperienceEvent classes, respectively. Attempting to ingest data for Identity Service that does not adhere to either class will trigger this error.

### There were 0 valid identities in the first 100 rows of the processed batch

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "There were 0 valid identities in the first 100 rows of the processed batch"
}
```

This error displays when the first 100 rows of a batch presented no identities. This error does not indicate conclusively that no identities were found in subsequent records, however.

### Skipped records as they had only 1 identity per XDM record

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "Skipped {NUMBER_OF_RECORDS} records as they had only 1 identity per XDM record"
}
```

Identity Service only links identities when single records present two or more identity values. This error message occurs once for each ingested batch, and displays the number of records where only one identity could be found and resulted in no change to the identity graph.

### Namespace Code is not registered for this IMS Org

```
{
    "title": "InvalidInput",
    "status": 400,
    "detail": "Namespace Code {ERRONEOUS_CODE} is not registered for this IMS Org"
}
```

This error displays when an ingested record presents an identity whose associated namespace does not exist or is inaccessible by your organization.

### Skipping batch ingestion as IMS Org is not provisioned for Private Identity Graph

```
{
    "title": "AccountNotProvisioned",
    "status": 403,
    "detail": "Skipping batch ingestion as IMS Org is not provisioned for Private Identity Graph"
}
```

When ingesting batch data, this error message displays when your organization has not been provisioned with the proper permissions for Identity Service. Contact your system administrator to resolve this issue.

### Internal Error

```
{
    "title": "InternalError",
    "status": 500,
    "detail": "Internal Error. There was a problem during the ingestion"
}
```

This error displays when an unexpected exception occurs during a batch ingestion. Best practice is to program your automated calls to retry their requests a few times at a timed interval when receiving this error. If the problem persists, contact your system administrator.

recommendation-more-help
