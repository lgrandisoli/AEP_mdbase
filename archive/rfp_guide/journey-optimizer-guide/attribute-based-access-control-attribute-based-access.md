---
title: "Attribute-based access control attribute-based-access"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/access-control/attribute-based-access"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:23.759916+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Attribute-based access control attribute-based-access

Last update: May 8, 2026
- Topics:
- [Access Management](#)

CREATED FOR:

- Intermediate
- Admin
- Leader

The attribute-based access control capability allows you to define authorizations to manage data access for specific teams or groups of users. Its purpose is to protect sensitive digital assets from unauthorized users, providing further protection of personal data.

Use the attribute-based access control in Adobe Journey Optimizer to protect data and grant specific access to specific field elements including Experience Data Model (XDM) schemas, Profile attributes, and audiences.

For a more detailed list of the terminology used with attribute-based access control, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/access-control/abac/overview#_blank).

In this example, a label is added to the **Nationality** schema field to restrict unauthorized users from using it. For this to work, perform the following steps:

- Create a new Role and assign it with the corresponding Label for users to be able to access and use the schema field.
- Assign a Label to the Nationality schema field in Adobe Experience Platform.
- Use the Schema field in Adobe Journey Optimizer.

Note that **Roles**, **Policies**, and **Products** can also be accessed with the attribute-based access control API. For more information, refer to this [documentation](/en/docs/experience-platform/access-control/abac/abac-api/overview#_blank).

## Create a role and assign labels assign-role

IMPORTANT
Before managing permissions for a role, create a policy. For more information, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/access-control/abac/permissions-ui/policies#_blank).

**Roles** are a set of users that share the same permissions, labels, and sandboxes within your organization. Each user belonging to a **Role** is entitled to the Adobe apps and services contained in the product. You can also create your own **Roles** to fine-tune users’ access to certain functionalities or objects in the interface.

To grant selected users access to the **Nationality** field labeled C2, create a new **Role** with a specific set of users and grant them the label C2, allowing them to use the **Nationality** details in a **Journey**.

- From the Permissions product, select Role from the left pane menu and click Create role . Note that you can also add Label to built-in roles.
- Add a Name and Description to your new Role , here: Restricted role demographic.
- From the drop-down, select your Sandbox .
- From the Resources menu, click Adobe Experience Platform to open the different capabilities. Here, we select Journeys .
- From the drop down, select the Permissions linked to the selected feature such as View journeys or Publish journeys .
- After saving your newly created Role , click Properties to further configure access to your role.
- From the Users tab, click Add users .
- From the Labels tab, select Add label .
- Select the Labels you want to add to your role and click Save . For this example, grant the label C2 for users to access the previously restricted schema’s field.

The users in the **Restricted role demographic** role now have access to the C2-labeled objects.

## Assign labels to an object in Adobe Experience Platform assign-label

WARNING
Incorrect label usage can break access for people and trigger policy violations.
**Labels** can be used to assign specific feature areas using attribute-based access control. In this example, access to the **Nationality** field is restricted. This field will only be accessible to users with the corresponding **Label** assigned to their **Role**.

Note that you can also add **Label** to **Schema**, **Datasets** and **Audiences**.

- Create your Schema . For more information, refer to this documentation .
- In the newly created Schema , we first add the Demographic details field group that contains the Nationality field.
- From the Labels tab, check the restricted field name, here Nationality . Then, from the right pane menu, select Edit governance labels .
- Select the corresponding Label , in this case, the C2 - Data cannot be exported to a third-party. For the detailed list of available labels, refer to this page .
- Further personalize your schema if needed, then enable it. For detailed steps on how to enable your schema, refer to this page .

Your schema’s field will now only be visible and usable by users who are part of a role set with the C2 label. By applying a **Label** to your **Field name**, the **Label** will automatically apply to the **Nationality** field in every created schema.

## Access labeled objects in Adobe Journey Optimizer attribute-access-ajo

After labeling the **Nationality** field name in a new schema and role, the impact of this restriction can be observed in Adobe Journey Optimizer. For this example:

- User X, with access to objects labeled C2, creates a journey with a condition targeting the restricted **Field name**.
- User Y, without access to objects labeled C2, attempts to publish the journey.

- From Adobe Journey Optimizer, configure the Data source with your new schema.
- Add a new Field group of your newly created Schema to the built-in Data source . You can also create a new external data source and associated Field groups .
- After selecting your previously created Schema , click Edit from the Fields category.
- Select the Field name you want to target. Here we select the restricted Nationality field.
- Create a journey that sends an email to users with a specific nationality. Add an Event and a Condition .
- Select the restricted Nationality field to start building your expression.
- Edit your Condition to target a specific population with the restricted Nationality field.
- Personalize your journey as needed, here we add an Email action.

If User Y, without access to label C2 objects, needs to access this journey with the restricted field:

- User Y will not be able to use the restricted field name since it will not be visible.
- User Y will not be able to edit the expression with the restricted field name in advanced mode. The following error will appear: The expression is invalid. Field is no longer available or you do not have enough permission to see it.
- User Y can delete the expression.
- User Y will not be able to test the journey.
- User Y will not be able to publish the journey.

recommendation-more-help
