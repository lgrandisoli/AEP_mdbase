---
title: "Restricted labels in Report Builder"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-reportbuilder/restricted-labels"
category: "other"
topic: "analytics-platform/using/cja-reportbuilder/restricted-labels"
created_at: "2026-06-23T20:45:37.434109+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Restricted labels in Report Builder

Last update: May 13, 2026
- Topics:
- [Report Builder](#)

CREATED FOR:

- User

Generally data governance-related settings in Customer Journey Analytics are inherited from Experience Platform. The integration between Customer Journey Analytics and Experience Platform Data Governance allows for labeling of sensitive Customer Journey Analytics data and enforcement of privacy policies.

Privacy labels and policies that are created on datasets consumed by Experience Platform can be surfaced in the Customer Journey Analytics data views workflow. These labels stop or warn users who create metrics and dimensions from sensitive fields. For information about datasets, see [Datasets overview](/en/docs/experience-platform/catalog/datasets/overview)

In addition, when data is exported from Customer Journey Analytics (via reporting, export, API, etc.), warnings or labels are added to notify users that a report contains sensitive information that needs to be treated in a specific way.

This integration allows you to manage compliance. Data stewards in your organization can set policies to restrict usage. As a result, your Customer Journey Analytics users can more confidently use data, knowing that it complies with policies defined by data stewards.

For more information, see [Customer Journey Analytics and Data Governance](/en/docs/analytics-platform/using/cja-privacy/privacy-overview)

## View restricted data

Two Adobe-defined policies are surfaced in Customer Journey Analytics that affect reporting, downloading, and sharing:

- Enforce Analytics policy
- Enforce Download policy

Components subject to these policies are grayed out and do have an icon. When you hover over the info icon, a note is displayed to indicate the following: **Policies have been applied to this field prohibiting use of this data**.

For more information, see [Labels and policies](/en/docs/analytics-platform/using/cja-dataviews/data-governance).

{modal="regular"}

## Update reports that contain restricted data

In cases where a user created a Report Builder report with data elements that are later restricted, when the report is refreshed, an error message is displayed.

{width="100%" modal="regular"}

recommendation-more-help
