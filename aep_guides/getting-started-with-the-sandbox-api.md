---
title: "Getting started with the Sandbox API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sandbox/api/getting-started"
category: "reference"
topic: "experience-platform/sandboxes-guide"
created_at: "2026-06-26T17:23:24.157795+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Sandboxes Guide

# Getting started with the Sandbox API

Last update: June 18, 2026
- Topics:
- [Sandboxes](#)

CREATED FOR:

- Developer

Sandboxes in Adobe Experience Platform provide isolated development environments that allow you to test features, run experiments, and make custom configurations without impacting your production environment.

This developer guide provides steps to help you use the Sandbox API to manage sandboxes in Experience Platform, and includes sample API calls for performing various operations.

## Prerequisites

In order to manage sandboxes for your organization, you must have Sandbox Administration permissions. Users without access permissions can only use the [available sandboxes endpoint](/en/docs/experience-platform/sandbox/api/available) to list active sandboxes for the current user. See the [access control overview](/en/docs/experience-platform/access-control/home) for more information on how to assign sandbox permissions for Experience Platform.

### Reading sample API calls

This guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in the documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

### Gather values for required headers

This guide requires you to have completed the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en) in order to successfully make calls to Experience Platform APIs. Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

In addition to the authentication headers, all requests require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

All requests that contain a payload (POST, PUT, and PATCH) require an additional header:

- Content-Type: application/json

## Next steps

Now that you have gathered the required credentials, you can now continue to read the rest of the developer guide. Each section provides important information regarding their endpoints and demonstrate example API calls for performing CRUD operations. Each call includes the general API format, a sample request showing required headers and properly formatted payloads, and a sample response for a successful call.

recommendation-more-help
