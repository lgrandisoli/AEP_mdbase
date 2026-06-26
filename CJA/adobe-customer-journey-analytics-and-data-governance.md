---
title: "Adobe Customer Journey Analytics and Data Governance"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-privacy/privacy-overview"
category: "overview"
topic: "analytics-platform/using/cja-privacy/privacy-overview"
created_at: "2026-06-02T19:07:46.711690+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Adobe Customer Journey Analytics and Data Governance

Last update: May 13, 2026
- Topics:
- [Privacy](#)

CREATED FOR:

- Admin

Generally speaking, any data governance-related settings in Customer Journey Analytics are inherited from Adobe Experience Platform.

## Data Governance

The integration between Adobe Customer Journey Analytics and [Adobe Experience Platform Data Governance](/en/docs/experience-platform/data-governance/home) allows for labeling of sensitive Customer Journey Analytics data and enforcement of privacy policies.

Privacy labels and policies that were created on datasets consumed by Experience Platform can be surfaced in the Customer Journey Analytics data views workflow. These labels stop or warn users who create metrics and/or dimensions from sensitive fields.

In addition, when data is exported from Customer Journey Analytics (via reporting, export, API, etc.), warnings or labels are added to notify users that a report contains sensitive information that needs to be treated in a specific way.

This integration allows you to manage compliance more easily. Data stewards in your organization can set policies to restrict usage. As a result, your Customer Journey Analytics users can more confidently use data, knowing that it complies with policies defined by data stewards.

[Learn more](/en/docs/analytics-platform/using/cja-dataviews/data-governance)

## Privacy Requests

Adobe handles privacy requests in accordance with applicable local and international laws.

Because Customer Journey Analytics uses data that is available in Adobe Experience Platform, Adobe offers the [Adobe Experience Platform Privacy Service](/en/docs/experience-platform/privacy/home) to submit data access and deletion requests. The requests apply to both the original and rekeyed datasets.

## GDPR

Customer Journey Analytics will not subscribe to the General Data Protection Regulation (GDPR) Central Service directly and will instead inherit all dataset changes made in Experience Platform. Customer Journey Analytics depends on Platform Data Lake to enforce GDPR deletion requests and notify Customer Journey Analytics when requests are complete. All changes to affected batches in Customer Journey Analytics for event datasets are synchronized with Platform data. Profile and lookup datasets affected by GDPR deletion requests are fully re-ingested after each delete request. Deletion requests are typically finished within 7 days of a deletion event in Data Lake.

## CCPA

The California Consumer Privacy Act (CCPA) enhances privacy rights and consumer protection for residents of California, United States. This Act became effective on January 1, 2020.The CCPA provides new data privacy rights to California residents, such as the right to access and delete their personal data, to know whether their personal data is sold or disclosed (and to whom), and to refuse the sale of their personal data.In accordance with the CCPA, the Privacy Service supports requests to opt out from the selling of personal data.

Related Articles
- [Blog: How to Maintain Effective Governance In Adobe Customer Journey Analytics](https://experienceleaguecommunities.adobe.com/t5/adobe-analytics-blogs/bg-p/adobe-analytics-blogs/page/4)

recommendation-more-help
