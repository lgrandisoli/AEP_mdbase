---
title: "Catalog Service API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/catalog/api/getting-started"
category: "reference"
topic: "experience-platform/catalog-and-datasets-guide"
created_at: "2026-06-26T17:29:51.803905+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Catalog and Datasets Guide

# Catalog Service API guide

Last update: June 18, 2026
- Topics:
- [Catalog](#)

CREATED FOR:

- Developer

Catalog Service is the system of record for data location and lineage within Adobe Experience Platform. Catalog acts as a metadata store or “catalog” where you can find information about your data within Experience Platform, without needing to access the data itself. See the [Catalog overview](/en/docs/experience-platform/catalog/home) for more information.

This developer guide provides steps to help you start using the Catalog API. The guide then provides sample API calls for performing key operations using Catalog.

## Prerequisites

Catalog tracks metadata for several kinds of resources and operations within Experience Platform. This developer guide requires a working understanding of the various Experience Platform services involved with creating and managing these resources:

- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Batch ingestion](/en/docs/experience-platform/ingestion/batch/overview): How Experience Platform ingests and stores data from data files, such as CSV and Parquet.
- [Streaming ingestion](/en/docs/experience-platform/ingestion/streaming/overview): How Experience Platform ingests and stores data from client- and server-side devices in real time.

The following sections provide additional information that you will need to know or have on-hand in order to successfully make calls to the Catalog Service API.

## Reading sample API calls

This guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

## Gather values for required headers

In order to make calls to Experience Platform APIs, you must first complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

NOTE
For more information on sandboxes in Experience Platform, see the
sandbox overview documentation
.
All requests that contain a payload (POST, PUT, PATCH) require an additional header:

- Content-Type: application/json

## Best practices for Catalog API calls

When performing GET requests to the Catalog API, best practice is to include query parameters in your requests in order to return only the objects and properties that you need. Unfiltered requests can cause response payloads to reach past 3GB in size, which can slow overall performance.

You can view specific objects by including their ID in the request path or use query parameters such as properties and limit to filter responses. Filters can be passed as headers and as query parameters, with those passed as query parameters taking precedence. See the document on [filtering Catalog data](/en/docs/experience-platform/catalog/api/filter-data) for more information.

Since some queries can put a heavy load on the API, global limits have been implemented on Catalog queries to further support best practices.

## Next steps

This document covered the prerequisite knowledge required to make calls to the Catalog API. You can now proceed to the sample calls provided in this developer guide and follow along with their instructions.

Most of the examples in this guide use the /dataSets endpoint, but the principles can be applied to other endpoints within Catalog (such as /batches). See the [Catalog Service API reference](https://www.adobe.io/experience-platform-apis/references/catalog/) for a complete list of all calls and operations available for each endpoint.

For a step-by-step workflow that demonstrates how the Catalog API is involved with data ingestion, see the tutorial on [creating a dataset](/en/docs/experience-platform/catalog/datasets/create).

recommendation-more-help
