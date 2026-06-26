---
title: "Getting started with the Real-Time Customer Profile API getting-started"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/profile/api/getting-started"
category: "reference"
topic: "experience-platform/real-time-customer-profile-guide"
created_at: "2026-05-29T17:00:19.215911+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Real-Time Customer Profile Guide

# Getting started with the Real-Time Customer Profile API getting-started

Last update: May 23, 2026
- Topics:
- [Profiles](#)

CREATED FOR:

- Developer

Using Real-Time Customer Profile API endpoints, you can perform basic CRUD operations against Profile data, such as configuring computed attributes, accessing entities, exporting Profile data, and deleting unneeded datasets or batches.

Using the developer guide requires a working understanding of the various Adobe Experience Platform services involved in working with Profile data. Before beginning to work with the Real-Time Customer Profile API, please review the documentation for the following services:

- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, customer profile in real time based on aggregated data from multiple sources.
- [Adobe Experience Platform Identity Service](/en/docs/experience-platform/identity/home): Gain a better view of your customer and their behavior by bridging identities across devices and systems.
- [Adobe Experience Platform Segmentation Service](/en/docs/experience-platform/segmentation/home): Allows you to build audiences from Real-Time Customer Profile data.
- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully make calls to Profile API endpoints.

## Reading sample API calls

The Real-Time Customer Profile API documentation provides example API calls to demonstrate how to properly format requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

## Required headers

The API documentation also requires you to have completed the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) in order to successfully make calls to Experience Platform endpoints. Completing the authentication tutorial provides the values for each of the required headers in Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform are isolated to specific virtual sandboxes. Requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

For more information on sandboxes in Experience Platform, see the [sandbox overview documentation](/en/docs/experience-platform/sandbox/home).

All requests with a payload in the request body (such as POST, PUT, and PATCH calls) must include a Content-Type header. Accepted values specific to each call are provided in the call parameters.

## Next steps

To begin making calls using the Real-Time Customer Profile API, select one of the available endpoint guides.

recommendation-more-help
