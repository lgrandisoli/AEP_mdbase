---
title: "Access control troubleshooting guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/access-control/troubleshooting-guide"
category: "guides"
topic: "experience-platform/access-control-guide"
created_at: "2026-06-26T17:29:13.273243+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Access Control Guide

# Access control troubleshooting guide

Last update: May 13, 2026
- Topics:
- [Access Control](#)

CREATED FOR:

- Admin

This document provides answers to frequently asked questions about access control in Adobe Experience Platform. For questions and troubleshooting related to other Experience Platform services, please refer to the [Experience Platform troubleshooting guide](/en/docs/experience-platform/landing/troubleshooting).

Experience Platform leverages product profiles in the [Adobe Admin Console](https://adminconsole.adobe.com) to provide role-based access control, linking users with permissions and sandboxes. See the [access control overview](/en/docs/experience-platform/access-control/home) for more information.

## Where can I find my current access permissions?

If you are a system administrator, product administrator, or product-profile administrator for your organization, you can view your assigned product profile and the permissions it provides within the Adobe Admin Console. See the [access control user guide](/en/docs/experience-platform/access-control/ui/overview) for instructions on how to navigate the Admin Console to view a product profile’s permissions.

If you are not an administrator, you can still view your current access permissions by sending a request to the /acl/effective-policies endpoint in the Access Control API. See the “View effective policies” section in [access control developer guide](/en/docs/experience-platform/access-control/api/effective-policies) for more information.

## Some features in the Experience Platform UI are not available. How is access to these features controlled by permissions?

If you do not have access permissions for a particular Experience Platform feature, that feature will be hidden or greyed-out in the Experience Platform UI. For example, in order to view the “Profiles” tab, you must have either the “View Profiles” or “Manage Profiles” permissions. Contact your administrator if you require additional permissions for Experience Platform capabilities.

## How are permissions grouped, and which group contains the permission I want to use?

Permissions are grouped and categorized by the Experience Platform capabilities they apply to (such as Data Management and Profile Management). For a full list of available permissions and the groups they belong to, see the [permissions section](/en/docs/experience-platform/access-control/home#permissions) in the access control overview.

See the [access control overview](/en/docs/experience-platform/access-control/home) for more information on providing role-based access control.

## What happens to permissions after migrating from Adobe IO to Business ID?

Access control uses user ID (an internal unique id assigned to a user) for granting permissions. When an organization is migrated from Adobe ID to Business ID, all permissions set for its users will be lost because the user ID changes and access control will use the newly generated user ID. If your organization is migrated to Business ID, please contact your Adobe representative to migrate your user ID from Adobe ID to Business ID.

recommendation-more-help
