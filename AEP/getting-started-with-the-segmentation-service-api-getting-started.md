---
title: "Getting started with the Segmentation Service API getting-started"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/api/getting-started"
category: "reference"
topic: "experience-platform/segmentation-service-guide"
created_at: "2026-05-29T17:01:21.993777+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Segmentation Service Guide

# Getting started with the Segmentation Service API getting-started

Last update: May 23, 2026
- Topics:
- [Segments](#)

CREATED FOR:

- Developer

Adobe Experience Platform Segmentation Service allows you to create audiences through segment definitions or other sources in Adobe Experience Platform from your Real-Time Customer Profile data.

The developer guide requires a working understanding of the various Experience Platform services involved with using Segmentation Service.

- [Adobe Experience Platform Segmentation Service](/en/docs/experience-platform/segmentation/home): Allows you to build audiences from Real-Time Customer Profile data.
- [Experience Data Model (XDM) System](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. To best make use of Segmentation, please ensure your data is ingested as profiles and events according to the [best practices for data modeling](/en/docs/experience-platform/xdm/schema/best-practices).
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully work with the Segmentation API.

## Reading sample API calls

The Segmentation Service API documentation provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

## Required headers

The API documentation also requires you to have completed the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) in order to successfully make calls to Experience Platform endpoints. Completing the authentication tutorial provides the values for each of the required headers in Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox in which the operation will take place:

- x-sandbox-name: {SANDBOX_NAME}

NOTE
For more information on working with sandboxes in Experience Platform, see the
sandboxes overview documentation
.
## Next steps

To being making calls using the Segmentation Service API, select one of the available endpoint guides either using the left navigation or within the [developer guide overview](/en/docs/experience-platform/segmentation/api/overview)

recommendation-more-help
