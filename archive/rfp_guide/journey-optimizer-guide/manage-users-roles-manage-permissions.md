---
title: "Manage users & roles manage-permissions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/access-control/permissions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:20.577748+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Manage users & roles manage-permissions

Last update: May 8, 2026
- Topics:
- [Access Management](#)

CREATED FOR:

- Intermediate
- Admin

**Roles** refer to a collection of users who share the same permissions and sandboxes. These roles allow you to easily manage access and permissions for different groups of users within your organization.

With the Journey Optimizer product, you can choose from a range of pre-existing **Roles**, each with varying levels of permissions, to assign to your users. For more information on the available **Roles**, refer to this [page](/en/docs/journey-optimizer/using/access-control/ootb-product-profiles).

When a user belongs to a **Role**, they gain access to the Adobe apps and services contained within the product.

If the pre-existing roles do not meet your organization’s specific needs, you can also create custom **Roles** to fine-tune access to certain functionalities or objects in the interface. This way, you ensure that each user has access to only the resources and tools they require to perform their tasks efficiently.

IMPORTANT
Steps and procedures detailed below can only be carried out by a
Product
or
System
administrator.
## Assign a role assigning-role

You can assign an out-of-the-box or custom **Role** to your users.

The list of all out-of-the-box roles with assigned permissions is available in the [Built-in roles](/en/docs/journey-optimizer/using/access-control/ootb-product-profiles) section.

To assign a **Role**:

- To assign a role to a user in the Permissions product, navigate to the Roles tab and select the desired role.
- From the Users tab, click Add user .
- Type in your user’s name or email address or select the user from the list, and click Save . If the user was not previously created in the Admin Console, refer to the Add users documentation .

Your user receives an email redirecting them to your instance.

For more information on user management, refer to the [Access control documentation](/en/docs/experience-platform/access-control/home#_blank).

When accessing the instance, your user sees a specific view depending on the assigned permissions in the **Role**. If the user does not have the right access to a feature, the following message appears:

You do not have permission to access this feature. Permission needed: XX.

## Edit an existing role edit-product-profile

For built-in or custom **Roles**, you can decide at any time to add or delete permissions.

In the example below, we want to add **Permissions** related to the **Journeys** resource for users assigned to the Journey viewer **Role**. The users will then be able to publish journeys.

IMPORTANT
Changes made to a built-in or custom role will affect all users assigned to that role.
- To edit a role in the Permissions product, navigate to the Roles tab and select the desired role, here the Journey viewer Role .
- From your Role dashboard, click Edit .
- The Resources menu displays the list of resources that apply to the Experience Cloud - Platform powered applications product. Drag and drop resources to assign permissions. From the Journeys resource drop-down, we choose here the Publish journey Permission .
- If needed, under Included Permission Items , click the X icon to remove permissions or resources from your role.
- When finished, click Save .

If needed, you can also create a new role with specific permissions.

## Create a new role create-product-profile

Journey Optimizer allows you to create your own **Roles** and assign a set of permissions and sandboxes to your users. With **Roles**, you can authorize or deny access to certain functionalities or objects in the interface.

For more information on how to create and manage sandboxes, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/sandbox/ui/user-guide#_blank).

In this example, we create a role named **Journeys read-only**, where we grant read-only rights to the Journey feature. Users will only be able to access and view journeys and will not be able to access other features such as **Decision management** in Journey Optimizer.

To create our **Journeys read-only** **Role**:

- To assign a role to a user in the Permissions product, navigate to the Roles tab and click Create role .
- Add a Name and Description for your new Role . Then, click Confirm .
- From the Sandbox resource drop-down, choose which sandbox(es) to assign to your Role . Learn more about sandboxes .
- Select from the different resources such as Journeys , Segments , or Decision management available in Journey Optimizer listed in the left-hand menu. Here we select the Journeys resource.
- From the Journeys drop-down, select the permissions to assign to your Role . Here we select View journeys , View journeys report and View journeys event, data sources, actions .
- When finished, click Save .

Your **Role** is now created and configured. You now need to assign it to users.

For more information on role creation and management, refer to the [Adobe Admin Console documentation](/en/docs/experience-platform/access-control/abac/permissions-ui/roles#_blank).

recommendation-more-help
