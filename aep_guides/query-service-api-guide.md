---
title: "Query Service API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/query/api/getting-started"
category: "reference"
topic: "experience-platform/query-service-guide"
created_at: "2026-06-26T17:26:26.630252+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Query Service Guide

# Query Service API guide

Last update: May 23, 2026
- Topics:
- [Queries](#)

CREATED FOR:

- Developer

This developer guide provides steps for performing various operations in the Adobe Experience Platform Query Service API.

## Getting started

This guide requires a working understanding of the various Adobe Experience Platform services involved with using Query Service.

- [Query Service](/en/docs/experience-platform/query/home): Provides the ability to query datasets and capture the resulting queries as new datasets in Experience Platform.
- [Experience Data Model (XDM) System](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The following sections provide additional information that you will need to know in order to successfully use Query Service using the API.

### Reading sample API calls

This guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in this documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/troubleshooting#how-do-i-format-an-api-request) in the Experience Platform troubleshooting guide.

### Gather values for required headers

In order to make calls to Experience Platform APIs, you must first complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox in which the operation will take place:

- x-sandbox-name: {SANDBOX_NAME}

NOTE
For more information on working with sandboxes in Experience Platform, see the
sandboxes overview documentation
.
## Sample API calls

Now that you understand what headers to use, you are ready to begin making calls to the Query Service API. The following documents walk through the various API calls you can make using the Query Service API. Each example call includes the general API format, a sample request showing required headers, and a sample response.

- [Queries](/en/docs/experience-platform/query/api/queries)
- [Connection parameters](/en/docs/experience-platform/query/api/connection-parameters)
- [Scheduled queries](/en/docs/experience-platform/query/api/scheduled-queries)
- [Runs for scheduled queries](/en/docs/experience-platform/query/api/runs-scheduled-queries)
- [Query templates](/en/docs/experience-platform/query/api/query-templates)
- [Accelerated queries](/en/docs/experience-platform/query/api/accelerated-queries)
- [Alert subscriptions](/en/docs/experience-platform/query/api/alert-subscriptions)

## Next steps

Now that you have learned how to make calls using the Query Service API, you can create your own non-interactive queries. For more information on how to create queries, please read the [SQL reference guide](/en/docs/experience-platform/query/sql/overview).

recommendation-more-help
