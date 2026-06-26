---
title: "Access Control API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/access-control/api/getting-started"
category: "reference"
topic: "experience-platform/access-control-guide"
created_at: "2026-06-26T17:35:29.239037+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Access Control Guide

# Access Control API guide

Last update: May 13, 2026
- Topics:
- [Access Control](#)

CREATED FOR:

- Developer

Access control for Experience Platform is administered through the [Adobe Admin Console](https://adminconsole.adobe.com). This functionality leverages product profiles in Admin Console, which link users with permissions and sandboxes. See the [access control overview](/en/docs/experience-platform/access-control/home) for more information.

This developer guide provides information on how to format your requests to the [Access Control API](https://www.adobe.io/experience-platform-apis/references/access-control/), and covers the following operations:

- [List names of permissions and resource types](/en/docs/experience-platform/access-control/api/permissions-and-resource-types)
- [View effective access policies for the current user](/en/docs/experience-platform/access-control/api/effective-policies)

## Getting started

The following sections provide additional information that you will need to know in order to successfully make calls to the Access Control API.

### Reading sample API calls

This guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

### Gather values for required headers

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

## Next steps

Now that you have gathered the required credentials, you can now continue to read the rest of the developer guide. Each section provides important information regarding their endpoints and demonstrate example API calls for performing CRUD operations. Each call includes the general API format, a sample request showing required headers and properly formatted payloads, and a sample response for a successful call.

recommendation-more-help
