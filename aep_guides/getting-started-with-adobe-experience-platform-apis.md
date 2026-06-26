---
title: "Getting started with Adobe Experience Platform APIs"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-guide"
category: "guides"
topic: "experience-platform/experience-platform-overview"
created_at: "2026-06-26T17:24:27.750456+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform overview

# Getting started with Adobe Experience Platform APIs

Last update: June 18, 2026
- Topics:
- [API](#)

CREATED FOR:

- Developer

Adobe Experience Platform is developed under an “API first” philosophy. Using Experience Platform APIs, you can programmatically perform basic CRUD (Create, Read, Update, Delete) operations against data, such as configuring computed attributes, accessing data/entities, exporting data, deleting unneeded data or batches, and more.

The APIs for each Experience Platform service all share the same set of authentication headers and use similar syntaxes for their CRUD operations. The following guide outlines the necessary steps for getting started with Experience Platform APIs.

## Authentication and headers

In order to successfully make calls to Experience Platform endpoints, you are required to complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

### Sandbox header

All resources in Experience Platform are isolated to specific virtual sandboxes. Requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

For more information on sandboxes in Experience Platform, see the [sandbox overview documentation](/en/docs/experience-platform/sandbox/home).

### Content-type header

All requests with a payload in the request body (such as POST, PUT, and PATCH calls) must include a Content-Type header. Accepted values are specific to each API endpoint. If a specific Content-Type value is needed for an endpoint, its value will be shown in the example API requests provided by the [API guides for individual Experience Platform services](#api-guides).

## Experience Platform API fundamentals

Adobe Experience Platform APIs employ several underlying technologies and syntaxes that are important to understand in order to effectively manage Experience Platform resources.

To learn more about the underlying API technologies Experience Platform utilizes, including example JSON schema objects, visit the [Experience Platform API fundamentals](/en/docs/experience-platform/landing/platform-apis/api-fundamentals) guide.

## Postman collections for Experience Platform APIs

Postman is a collaboration platform for API development that allows you to set up environments with preset variables, share API collections, streamline CRUD requests, and more. Most Experience Platform API services have Postman collections which can be used to assist with making API calls.

To learn more about Postman including how to set up an environment, a list of available collections, and how to import collections, visit the [Experience Platform Postman documentation](/en/docs/experience-platform/landing/platform-apis/postman).

## Reading sample API calls sample-api

Request formats vary depending on the Experience Platform API being used. The best way to learn how to structure your API calls is by following along with the examples provided in the documentation for the particular Experience Platform service you are using.

The documentation for Experience Platform shows example API calls in two different ways. First, the call is presented in its **API format**, a template representation showing only the operation (GET, POST, PUT, PATCH, DELETE) and the endpoint being used (for example, /global/classes). Some templates also show the location of variables to help illustrate how a call should be formulated, such as GET /{VARIABLE}/classes/{ANOTHER_VARIABLE}.

The calls are then shown as cURL commands in a **Request**, which includes the necessary headers and full “base path” needed to successfully interact with the API. The base path should be pre-pended to all endpoints. For example, the aforementioned /global/classes endpoint becomes https://platform.adobe.io/data/foundation/schemaregistry/global/classes. You will see the API format / request pattern throughout the documentation, and are expected to use the complete path shown in the example request when making your own calls to Experience Platform APIs.

### Example API request

The following is an example API request that demonstrates the format you will encounter in the documentation.

**API format**

The API format shows the operation (GET) and the endpoint being used. Variables are indicated by curly braces (in this case, {CONTAINER_ID}).

```
GET /{CONTAINER_ID}/classes
```

**Request**

In this example request, the variables from the API format are given actual values in the request path. Additionally, all required headers are shown as either sample header values or variables where sensitive information (such as security tokens and access IDs) should be included.

```
curl -X GET \
  https://platform.adobe.io/data/foundation/schemaregistry/global/classes \
  -H 'Accept: application/vnd.adobe.xed-id+json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'x-sandbox-name: {SANDBOX_NAME}'
```

**Response**

The response illustrates what you would expect to receive following a successful call to the API, based on the request that was sent. Occasionally the response is truncated for space, meaning that you may see more information or additional information to that which is displayed in the sample.

```
{
    "results": [
        {
            "title": "XDM ExperienceEvent",
            "$id": "https://ns.adobe.com/xdm/context/experienceevent",
            "meta:altId": "_xdm.context.experienceevent",
            "version": "1"
        },
        {
            "title": "XDM Individual Profile",
            "$id": "https://ns.adobe.com/xdm/context/profile",
            "meta:altId": "_xdm.context.profile",
            "version": "1"
        }
    ],
    "_links": {}
}
```

## Error messages

The [Experience Platform troubleshooting guide](/en/docs/experience-platform/landing/troubleshooting#errors-and-troubleshooting) provides a list of errors that you may encounter when using any Experience Platform service.

For troubleshooting guides on individual Experience Platform services, see the [service troubleshooting directory](/en/docs/experience-platform/landing/troubleshooting#service-troubleshooting-directory).

For more information on specific endpoints in Experience Platform APIs, including required headers and request bodies, please see the [Experience Platform API guides](#api-guides).

## Experience Platform API guides api-guides

API guide
Description
Access Control API guide
The Access Control API endpoint can retrieve current policies in effect for a user on given resources within a specified sandbox. All other access control capabilities are provided through the
Adobe Admin Console
.
Batch ingestion API guide
The Adobe Experience Platform Data Ingestion API allows you to ingest data into Experience Platform as batch files. Data being ingested can be the profile data from a flat file in a CRM system (such as a Parquet file), or data that conforms to a known schema in the Schema Registry (XDM).
Catalog Service API guide
The Catalog Service API allows developers to manage dataset metadata in Adobe Experience Platform. This includes data locations, processing stages, errors that occurred during processing, and data reports.
Data Access API guide
The Data Access API allows developers to retrieve information on ingested datasets within Experience Platform. This includes accessing and downloading dataset files, retrieving header information, listing failed and succeeded batches, and downloading preview CSV / Parquet files.
Dataset Service API guide
The Dataset Service API allows you to apply and edit usage labels for datasets. It is part of Adobe Experience Platform’s data catalog capabilities, but is separate from the Catalog Service API which manages dataset metadata.
Data Hygiene API guide
The Data Hygiene API allows you to programmatically correct or delete your customers’ stored personal data in Adobe Experience Platform, as well as schedule expiration dates for datasets.
Edge Network API guide
The Edge Network API can be used for a variety of data collection, personalization, advertising and marketing use cases. The Edge Network API can be used on servers, IoT devices, set-top boxes, and a variety of other devices.
Identity Service API guide
The Identity Service API allows developers to manage the cross-device, cross-channel, and near real-time identification of your customers using identity graphs in Adobe Experience Platform.
MTLS Service API guide
The MTLS Service API allows you to securely retrieve public certificates issued by Adobe for your organization.
Observability Insights API guide
Observability Insights is a RESTful API that allows developers to expose key observability metrics in Adobe Experience Platform. These metrics provide insights into Experience Platform usage statistics, health-checks for Experience Platform services, historical trends, and performance indicators for various Experience Platform functionalities.
Policy Service API guide
(Data Governance)
The Policy Service API allows you to create and manage data usage labels and policies to determine what marketing actions can be taken against data that contains certain data usage labels. To apply labels to datasets and fields, refer to the
Dataset Service API
guide
Privacy Service API guide
The Privacy Service API allows developers to create and manage customer requests to access or delete their personal data across Experience Cloud applications, in compliance with legal privacy regulations.
Query Service API guide
The Query Service API allows developers to query their Adobe Experience Platform data using standard SQL.
Real-Time Customer Profile API guide
The Real-Time Customer Profile API allows developers to explore and work with Profile data, including viewing profiles, creating and updating merge policies, exporting or sampling Profile data, and deleting Profile data that is no longer required or was added in error.
Sandbox API guide
The Sandbox API allows developers to programmatically manage isolated virtual sandbox environments in Adobe Experience Platform.
Schema Registry API guide
(XDM)
The Schema Registry API allows developers to programmatically manage all schemas and related Experience Data Model (XDM) resources within Adobe Experience Platform.
Segmentation Service API guide
The Segmentation Service API allows developers to programmatically manage segmentation operations in Adobe Experience Platform. This includes building segments and generating audiences from your Real-Time Customer Profile data.
Adobe AI Machine Learning API guide
(Data Science Workspace)
The Adobe AI Machine Learning API provides a mechanism for data scientists to organize and manage machine learning (ML) services from algorithm onboarding, experimentation, and to service deployment.
For more information on specific endpoints and operations available for each service, please see the [API reference documentation](https://www.adobe.com/go/platform-api-reference-en) on Adobe I/O.

## Next steps

This document introduced the required headers, available guides, and provided an example API call. Now that you have the required header values needed to make API calls on Adobe Experience Platform, select an API endpoint you wish to explore from the [Experience Platform API guides table](#api-guides).

For answers to frequently asked questions, refer to the [Experience Platform troubleshooting guide](/en/docs/experience-platform/landing/troubleshooting).

To set up a Postman environment and explore the available Postman collections, refer to the [Experience Platform Postman guide](/en/docs/experience-platform/landing/platform-apis/postman).

recommendation-more-help
