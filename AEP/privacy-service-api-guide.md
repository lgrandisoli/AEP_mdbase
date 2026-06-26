---
title: "Privacy Service API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/privacy/api/overview"
category: "reference"
topic: "experience-platform/privacy-service-guide"
created_at: "2026-05-29T16:57:44.265669+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Privacy Service Guide

# Privacy Service API guide

Last update: May 23, 2026
- Topics:
- [Privacy](#)

CREATED FOR:

- Developer

The Privacy Service API provides several endpoints that allow you to programmatically manage privacy jobs for your organization. These endpoints are outlined below. Please visit the individual endpoint guides for details and refer to the [getting started guide](/en/docs/experience-platform/privacy/api/getting-started) for important information on required headers, reading sample API calls, and more.

NOTE
This guide covers how to use the Privacy Service API. For details on how to use the UI, see the
Privacy Service UI overview
.
To view all available endpoints and CRUD operations, visit the [Privacy Service API reference](https://www.adobe.io/experience-platform-apis/references/privacy-service/).

## Privacy jobs

When Privacy Service receives a request to access or delete the personal data of a subject, the system creates privacy jobs to fulfill that request. Each privacy job contains identity information related to the data subject, metadata about the Adobe Experience Cloud product that the job applies to, and the job’s processing status.

The /jobs endpoint allows you to create and retrieve privacy jobs for your organization. To learn how to use this endpoint, see the [privacy jobs endpoint guide](/en/docs/experience-platform/privacy/api/privacy-jobs).

## Consent

Certain regulations require explicit customer consent before their personal data can be collected. The /consent endpoint allows you to process customer consent requests and integrate them into your privacy workflow. See the [consent endpoint guide](/en/docs/experience-platform/privacy/api/consent) to learn more.

## Next steps

To begin making calls using the Privacy Service API, read the [getting started guide](/en/docs/experience-platform/privacy/api/getting-started) then select one of the endpoint guides to learn how to use specific endpoints.

recommendation-more-help
