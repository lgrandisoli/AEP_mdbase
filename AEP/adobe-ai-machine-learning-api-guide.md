---
title: "Adobe AI Machine Learning API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-science-workspace/api/getting-started"
category: "reference"
topic: "experience-platform/data-science-workspace-guide"
created_at: "2026-05-29T17:01:47.211285+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Science Workspace Guide

# Adobe AI Machine Learning API guide

Last update: May 13, 2026
- Topics:
- [Data Science Workspace](#)

CREATED FOR:

- Developer

NOTE
Data Science Workspace is no longer available for purchase.
This documentation is intended for existing customers with prior entitlements to Data Science Workspace.
The Adobe AI Machine Learning API provides a mechanism for data scientists to organize and manage machine learning services, from algorithm onboarding through experimentation and to service deployment.

This developer guide provides steps to help you start using the [Adobe AI Machine Learning API](https://developer.adobe.com/experience-platform-apis/references/sensei-machine-learning/), and demonstrates API calls for performing CRUD operations on various Data Science Workspace resources.

## Getting started

You are required to have completed the [authentication](https://www.adobe.com/go/platform-api-authentication-en) tutorial in order to have access to the following request headers to make calls to Adobe Experience Platform APIs:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

All resources in Experience Platform are isolated to specific virtual sandboxes. All requests to Experience Platform APIs require a header that specifies the name of the sandbox the operation will take place in:

- x-sandbox-name: {SANDBOX_NAME}

For more information on sandboxes in Experience Platform, see the [sandbox overview documentation](/en/docs/experience-platform/sandbox/home).

All requests that contain a payload (POST, PUT, PATCH) require an additional header:

- Content-Type: application/json

## Next steps

Once you have gathered the required authentication credentials, you can proceed to the subsequent sections of this developer guide for sample API calls to the following endpoint groups:

- [Engines](/en/docs/experience-platform/data-science-workspace/api/engines)
- [Experiments](/en/docs/experience-platform/data-science-workspace/api/experiments)
- [Insights](/en/docs/experience-platform/data-science-workspace/api/insights)
- [MLInstances (Recipes)](/en/docs/experience-platform/data-science-workspace/api/mlinstances)
- [MLServices](/en/docs/experience-platform/data-science-workspace/api/mlservices)
- [Models](/en/docs/experience-platform/data-science-workspace/api/models)
- [Appendix](/en/docs/experience-platform/data-science-workspace/api/appendix)

recommendation-more-help
