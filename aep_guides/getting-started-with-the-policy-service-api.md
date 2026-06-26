---
title: "Getting started with the Policy Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-governance/api/getting-started"
category: "reference"
topic: "experience-platform/data-governance-guide"
created_at: "2026-06-26T17:27:13.225432+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Governance Guide

# Getting started with the Policy Service API

Last update: June 18, 2026
- Topics:
- [Data Governance](#)

CREATED FOR:

- Developer

The Policy Service API allows you to create and manage various resources related to Adobe Experience Platform Data Governance. This document provides an introduction to the core concepts you need to know before attempting to make calls to the Policy Service API.

## Prerequisites

Using the developer guide requires a working understanding of the various Experience Platform services involved in working with Data Governance capabilities. Before beginning to work with the Policy Service API, please review the documentation for the following services:

- [Data Governance](/en/docs/experience-platform/data-governance/home): The framework by which Experience Platform enforces data usage compliance.
- [Experience Data Model (XDM) System](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Reading sample API calls

The Policy Service API documentation provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

## Required headers

The API documentation also requires you to have completed the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) in order to successfully make calls to Experience Platform endpoints. Completing the authentication tutorial provides the values for each of the required headers in Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform, including those belonging to Data Governance, are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

NOTE
For more information on sandboxes in Experience Platform, see the
sandbox overview documentation
.
All requests that contain a payload (POST, PUT, PATCH) require an additional header:

- Content-Type: application/json

## Core vs custom resources

Within the Policy Service API, all policies and marketing actions are referred to as either core or custom resources.

core resources are those defined and maintained by Adobe, whereas custom resources are those created and maintained by your organization, and are therefore unique and visible solely to your organization. As such, listing and lookup operations (GET) are the only operations permitted on core resources, whereas listing, lookup and update operations (POST, PUT, PATCH, and DELETE) are available for custom resources.

## Next steps

To begin making calls using the Policy Service API, select one of the available endpoint guides.

recommendation-more-help
