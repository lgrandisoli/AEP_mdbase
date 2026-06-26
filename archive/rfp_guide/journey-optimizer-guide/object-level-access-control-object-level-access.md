---
title: "Object level access control object-level-access"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/access-control/object-based-access"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:24.936353+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Object level access control object-level-access

Last update: May 8, 2026
- Topics:
- [Access Management](#)

CREATED FOR:

- Experienced
- Admin
- Developer

You can limit the access to an object based on access labels. This approach protects sensitive digital assets from unauthorized users and ensures further protection of personal data.

The Object level access control (OLAC) capability allows you to define authorizations to manage data access for a selection of objects:

- Journey
- Campaign
- Template
- Fragment
- Landing page
- Offer
- Static offer collection
- Offer decision
- Channel configuration
- IP warmup plan

## Prerequisites prereq-labels

To be able to [create labels](#create-labels), you must belong to a role with the **Manage usage labels** permission.

To be able to [assign labels](#assign-labels), you must belong to a role with a **Manage** permission i.e., Manage journeys, Manage Campaigns, or Manage decisions. Without this permission, the **Manage access** button is greyed out.

Learn more about permissions in [this section](/en/docs/journey-optimizer/using/access-control/permissions).

## Create labels create-labels

**Labels** allow you to categorize datasets and fields according to usage policies that apply to that data. **Labels** can be applied at any time, providing flexibility in how you govern data.

Use labels to provide access to users, and enforce data governance and consent policies. These governance labels can affect downstream consumption.

You can create labels in the Permissions product. For more details, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/access-control/abac/permissions-ui/labels#_blank).

You can also create **Labels** directly in Journey Optimizer. To create a label, follow these steps:

- From an Adobe Journey Optimizer object, such as a newly created Campaign , click the Manage access button.
- From the Manage access window, click Create label .
- Configure your label. You must specify: Name Friendly name Description
- Click Create to save your Label .

Your newly created **Label** is now available in the list. If needed, you can modify it in the Permissions product.

## Assign labels assign-labels

To assign custom or core data usage labels to your Journey Optimizer objects:

- From an Adobe Journey Optimizer object, such as a newly created Campaign , click the Manage access button.
- From the Manage access window, select your custom or core data usage label(s) to manage access to this object. For more information on core data usage labels, refer to this page .
- Click Save to apply this label restriction.

To access this object, users must have the specific **Label** included in their **Roles**. For example, a user with the C1 label will only have access to C1-labeled or unlabeled objects.

For more details on how to assign a **Label** to a **Role**, refer to [this page](/en/docs/experience-platform/access-control/abac/permissions-ui/permissions#manage-labels-for-a-role#_blank).

recommendation-more-help
