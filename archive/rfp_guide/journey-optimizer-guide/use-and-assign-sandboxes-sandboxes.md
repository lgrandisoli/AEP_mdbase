---
title: "Use and assign sandboxes sandboxes"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/sandbox/sandboxes"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:31.880102+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use and assign sandboxes sandboxes

Last update: May 8, 2026
- Topics:
- [Sandboxes](#)

CREATED FOR:

- Experienced
- Admin
- Developer

**Sandboxes** are virtual environments that partition your Adobe Journey Optimizer instance into separate, isolated workspaces—for development, testing, or production. You’ll find sandbox management under **Administration** > **Channels** > **Connect your systems and environments** (or via the sandbox switcher in the top-right of the interface). Sandboxes help you experiment safely, assign different access per role, and keep content organized. This page covers how to use and assign sandboxes, configure content access, and—in the [Export objects to another sandbox](/en/docs/journey-optimizer/using/connect-systems/sandbox/copy-objects-to-sandbox) article—how to copy journeys and templates between sandboxes.

## Use sandboxes using-sandbox

Journey Optimizer allows you to partition your instance into separate virtual environments called sandboxes. Sandboxes are assigned through roles in Permissions. [Learn how to assign sandboxes](/en/docs/journey-optimizer/using/access-control/permissions#create-product-profile).

Journey Optimizer reflects Adobe Experience Platform sandboxes created for a given organization. Adobe Experience Platform sandboxes can be created or reset from your Adobe Experience Platform instance. [Learn more in the Sandbox user guide](/en/docs/experience-platform/sandbox/ui/user-guide#_blank).

You can find the sandbox switcher control at the top-right of your screen, next to your organization’s name. To switch from one sandbox to another, click the currently active sandbox in the switcher and select another sandbox from the drop-down list.

➡️ [Learn more about sandboxes in this video](#video)

## Assign sandboxes assign-sandboxes

IMPORTANT
Sandbox management can only be carried out by a
Product
or
System
administrator.
You can choose to assign different sandboxes to out-of-the-box or custom **Roles**.

To assign sandboxes:

- In Permissions, from the Roles tab, select a Role .
- Click Edit .
- From the Sandboxes resource drop-down, select the sandbox which will be assigned to your role.
- If needed, click the X icon next to it to remove sandbox access from your Role .
- Click Save .

## Access to Content content-access

To configure content accessibility, assign a content shared folder to each of your sandboxes. You can create and configure shared folders in the **Storage** tab displayed in the Admin Console for administrators. If you have access to the Admin Console as a system administrator, you can create shared folders and add delegates with different access levels to your shared folders.

Note that for your content to sync with the correct sandbox, you must follow the same syntax as the sandbox. For example, if your sandbox is called “development,” your shared folder should have the same name.

[Learn how to manage shared folders](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/manage-adobe-storage.ug.html#_blank).

## How-to video video

Understand what sandboxes are and how to distinguish between development and production sandboxes. Learn how to create, reset, and delete sandboxes.

https://video.tv.adobe.com/v/334355?quality=12&learn=on
recommendation-more-help
