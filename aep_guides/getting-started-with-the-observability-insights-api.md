---
title: "Getting started with the Observability Insights API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/observability/api/getting-started"
category: "reference"
topic: "experience-platform/observability-insights-guide"
created_at: "2026-06-26T17:39:49.162933+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Observability Insights Guide

# Getting started with the Observability Insights API

Last update: May 23, 2026
- Topics:
- [Observability](#)

CREATED FOR:

- Developer

The Observability Insights API allows you to retrieve metric data for various Adobe Experience Platform features. This document provides an introduction to the core concepts you need to know before attempting to make calls to the Observability Insights API.

## Reading sample API calls

The Observability Insights API documentation provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on how to read example API calls in the [Experience Platform troubleshooting guide](/en/docs/experience-platform/landing/troubleshooting).

## Required headers

In order to make calls to Experience Platform APIs, you must first complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in. For more information on sandboxes in Experience Platform, see the [sandbox overview documentation](/en/docs/experience-platform/sandbox/home).

- x-sandbox-name: {SANDBOX_NAME}

## Next steps

To begin making calls using the Observability Insights API, proceed to the [metrics endpoint guide](/en/docs/experience-platform/observability/api/metrics).

recommendation-more-help
