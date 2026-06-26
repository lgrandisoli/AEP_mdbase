---
title: "Attribute-based access control end-to-end guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/access-control/abac/end-to-end-guide"
category: "guides"
topic: "experience-platform/access-control-guide"
created_at: "2026-06-26T17:21:36.871893+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Access Control Guide

# Attribute-based access control end-to-end guide

Last update: May 13, 2026
- Topics:
- [Access Control](#)

CREATED FOR:

- Developer

Use Attribute-based access control on Adobe Experience Platform to give yourself and other multi-brand privacy-conscious customers greater flexibility to manage user access. Access to individual objects, such as schema fields and audiences, can be granted with policies based on the object’s attributes and role. This feature lets you grant or revoke access to individual objects for specific Experience Platform users in your organization.

This functionality allows you to categorize schema fields, audiences, and so on with labels that define organizational or data usage scopes. You can apply these same labels to journeys, Offers, and other objects in Adobe Journey Optimizer. In parallel, administrators can define access policies surrounding Experience Data Model (XDM) schema fields and better manage which users or groups (internal, external, or third-party users) can access those fields.

NOTE
This document focuses on the use case of access control policies. If you are trying to set up policies to govern the
use
of data rather than which Experience Platform users have access to it, see the end-to-end guide on
data governance
instead.
## Getting started

This tutorial requires a working understanding of the following Experience Platform components:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Adobe Experience Platform Segmentation Service : The segmentation engine within Experience Platform used to create audience segments from your customer profiles based on customer behaviors and attributes.

### Use case overview

You will go through an example attribute-based access control workflow where you will create and assign roles, labels, and policies to configure whether your users can or cannot access specific resources in your organization. This guide uses an example of restricting access to sensitive data to demonstrate the workflow. This use case is outlined below:

You are a healthcare provider and want to configure access to resources in your organization.

- Your internal marketing team should be able to access **PHI/ Regulated Health Data** data.
- Your external agency should not be able to access **PHI/ Regulated Health Data** data.

In order to do this, you must configure roles, resources, and policies.

You will:

- [Label the roles for your users](#label-roles): Use the example of a healthcare provider (ACME Business Group) whose marketing group works with external agencies.
- [Label your resources (schema fields and audiences)](#label-resources): Assign the **PHI/ Regulated Health Data** label to schema resources and audiences.
- [Activate the policy that will link them together](#policy): Enable the default policy to prevent access to schema fields and audiences by connecting the labels on your resources to the labels in your role. Users with matching labels will then be given access to the schema field and segment across all sandboxes.

## Permissions

Permissions is the area of Experience Cloud where administrators can define user roles and policies to manage permissions for features and objects within a product application.

Through Permissions, you can create and manage roles and assign the desired resource permissions for these roles. Permissions also allow you to manage the labels, sandboxes, and users associated with a specific role.

Contact your system administrator to gain access if you do not have admin privileges.

Once you have admin privileges, go to [Adobe Experience Cloud](https://experience.adobe.com/) and sign in using your Adobe credentials. Once logged in, the **Overview** page appears for your organization you have admin privileges for. This page shows the products your organization is subscribed to, along with other controls to add users and admins to the organization. Select **Permissions** to open the workspace for your Experience Platform integration.

The Permissions workspace for the Experience Platform UI appears, opening on the **Overview** page.

## Apply labels to a role label-roles

Roles are ways to categorize the types of users interacting with your Experience Platform instance and are building blocks of access control policies. A role has a given set of permissions, and members of your organization can be assigned to one or more roles, depending on the scope of access they need.

To get started, select **Roles** from the left navigation and then select **ACME Business Group**.

Next, select **Labels** and then select **Add Labels**.

A list of all labels in your organization appears. Select **RHD** to add the label for **PHI/Regulated Health Data** and then select **Save**.

NOTE
When adding an organization group to a role, all users in that group will be added to the role. Any changes to the organization group (users removed or added) will be automatically updated within the role.
## Apply labels to schema fields label-resources

Now that you have configured a user role with the RHD label, the next step is to add that same label to the resources that you want to control for that role.

From the top navigation, select the **application switcher**, represented by the icon and then select **Experience Platform**.

Select **Schemas** from the left navigation and then select **ACME Healthcare** from the list of schemas that appear.

Next, select **Labels** to see a list that displays the fields associated with your schema. From here, you can assign labels to one or multiple fields at once. Select the **BloodGlucose** and **InsulinLevel** fields, and then select **Apply access and data governance labels**.

The **Edit labels** dialog appears, allowing you to choose the labels that you want to apply to the schema fields. For this use case, select the **PHI/ Regulated Health Data** label, then select **Save**.

NOTE
When a label is added to a field, that label is applied to the parent resource of that field (either a class or a field group). If the parent class or field group is employed by other schemas, those schemas will inherit the same label.
## Apply labels to audiences

NOTE
Any audience that utilizes a labeled attribute must likewise be labeled if you want the same access restrictions to apply to it.
Once you have completed labeling your schema fields, you can now begin labeling your audiences.

Select **Audiences** from the left navigation under the **Customers** section. A list of audiences available in your organization is displayed. In this example, the following two audiences are to be labeled as they contain sensitive health data:

- Blood Glucose >100
- Insulin <50

Select **Blood Glucose >100** (by the audience name, not the checkbox) to start labeling the audience.

The segment **Details** screen appears. Select **Manage Access**.

The **Apply access and data governance labels** dialog appears, allowing you to choose the labels that you want to apply to the audience. For this use case, select the **PHI/ Regulated Health Data** label, then select **Save**.

Repeat the above steps with **Insulin <50**.

NOTE
Assign labels created in the Permissions workspace (such as the segment labels above) to various objects in Adobe Journey Optimizer using
Object Level Access Control
."
## Activate the access control policy policy

The default access control policy will leverage labels to define which user roles have access to specific Experience Platform resources. In this example, access to schema fields and audiences will be denied in all sandboxes for users who aren’t in a role that has the corresponding labels in the schema field.

To activate the access control policy, select Permissions from the left navigation and then select **Policies**.

Next, select the ellipsis (...) next to the **Default-Field-Level-Access-Control-Policy**, and a dropdown displays controls to edit, activate, delete, or duplicate the role. Select **Activate** from the dropdown.

The activate policy dialog appears which prompts you to confirm activation. Select **Confirm**.

Confirmation of policy activation is received and you are returned to the Policies page.

## Next steps

You have completed the application of labels to a role, schema fields, and audiences. The external agency assigned to these roles are restricted from viewing these labels and their values in the schema, dataset, and profile view. These fields are also restricted from being used in the segment definition when using the Segment Builder.

For more information on attribute-based access control, see the [attribute-based access control overview](/en/docs/experience-platform/access-control/abac/overview).

The following video is intended to support your understanding of attribute-based access control, and outlines how to configure roles, resources, and policies.

https://video.tv.adobe.com/v/345641?learn=on
https://video.tv.adobe.com/vc/345641/eng.json
recommendation-more-help
