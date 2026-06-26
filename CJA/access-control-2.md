---
title: "Access Control"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/technotes/access-control"
category: "other"
topic: "analytics-platform/using/technotes/access-control"
created_at: "2026-06-23T20:42:23.106664+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Access Control

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

Three levels of access or three roles govern Customer Journey Analytics: Product administrator role, Product profile administrator role, and user-level access. This topic explains these roles in more detail.

In addition, this article discusses more granular ways to limit access, such as Workspace curation and row-level as well as value-level access control.

## Role-based access control

The following role-based access control levels are available.

### Product administrator role

Users who are assigned the Product administrator role are given the necessary permissions to perform most tasks within Customer Journey Analytics by default. However, some tasks require additional permissions.

To add a user as a Product administrator:

- Go to the Admin Console .
- Select Customer Journey Analytics > Admins tab > Add Admin . The users that you added are given the Product administrator default permissions . You can also grant them additional permissions if needed.

#### Product administrator default permissions

Product administrators have permissions to complete most tasks within Customer Journey Analytics.

Product administrators are granted the necessary permissions to perform the following tasks by default:

- Update and delete projects, segments, calculated metrics, audiences, annotations, or segments created by other users
- Share Workspace projects to all users
- Manage reporting activity in the [Reporting Activity Manager](/en/docs/analytics-platform/using/reporting-activity-manager/reporting-activity-overview)
- [Export full tables](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud) from Analysis Workspace

#### Product administrator additional permissions

In addition to being added as a Product administrator in the **Customer Journey Analytics Product Profile** in the [Admin Console](https://adminconsole.adobe.com/enterprise/), additional permissions are required to complete the following tasks within Customer Journey Analytics:

- Create, update, and delete data views .
- Create, update, and delete connections To perform this task, users must be part of an Experience Platform Product Profile that provides the following permissions: table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 Category Permission Description Sandboxes At least one Access to relevant sandboxes for connections. Data Modeling View Schemas Read-only access to schemas and related resources. Data Modeling Manage Schemas Access to read, create, edit, and delete schemas and related resources. Data Management View Datasets Read-only access for datasets and schemas. Identity Management View Identity Namespaces Read-only access for identity namespaces. For more information on Experience Platform permissions, see Manage permissions for a product profile .
- If Journey Optimizer is integrated with Customer Journey Analytics where Journey Optimizer Connections exist, then Journeys permissions must also be added to access Connections: table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 Category Permission Description Journeys View Journeys Events, Data Sources and Actions Read-only access to journey events, journey custom actions, and journey data sources. Journeys Manage Journeys Events, Data Sources and Actions Read, create, edit, and delete events, sources, or actions. Journeys View Journeys Read-only access to journeys. Journeys Manage Journeys Read, create, edit, and delete journeys.
- Export datasets to destinations To perform this task, users must be part of an Experience Platform Product Profile that provides the following permissions: table 0-row-3 1-row-3 2-row-3 Category Permission Description Destinations Manage Destinations Access to read, create, and delete destination connections and destination accounts. Destinations Activate Destinations Allow users to activate segments to existing destinations. Enables the mapping step in the activation workflow. This permission also requires the View Destinations permission to be granted to the user who wants to activate data to destinations. For more information on Experience Platform permissions, see Manage permissions for a product profile .
- Use the BI extension For users to use the BI extension, a Product administrator must ensure the Experience Platform permissions for the user include a role that has the Query Service resource with the Manage Queries and Manage Query Service Integration options. For more information on Experience Platform permissions, see Manage permissions for a product profile . table 0-row-3 1-row-3 2-row-3 Category Permission Description Query Service Manage Queries Access to read, create, edit, and delete structured SQL queries for Platform data. Query Service Manage Query Service Integration Access to create, update, and delete non-expiring credentials for Query Service access. must ensure the proper Customer Journey Analytics permissions for the user: permission to access to the relevant data views. See Data Views in User-level access . permission to access the Customer Journey Analytics BI extension. See Data View Tools in User-level access .

### Product profile administrator role

A product profile is a set of permissions. Product administrators create product profiles and can assign Product profile administrators to manage one or more product profiles. A Product profile administrator can then:

- Manage the assigned product profiles. Such as adding or removing users or user groups and modify the permissions for the product profiles.
- In Customer Journey Analytics, edit data views that are part of an assigned product profile. Product profile administrators cannot create new data views.

### User-level access

The table below outlines the main access permissions for different Customer Journey Analytics capabilities that you can configure for relevant users. You can manage different level of user access through product profiles. A product profile combines a number of permissions, which you then can assign to individual users or user groups.

The **Permissions** tab is part of each product profile in the [Admin Console](https://adminconsole.adobe.com/enterprise/).

Category
Permission
Description
Data Views
data view name
If you toggle
Auto-Include
to
On
, users that are part of this product profile can view all existing and newly created data views. If this setting is set to
Off
, you can select specific data views that users have access to.
Reporting Tools
Guided Analysis Access
Let users access
Guided Analysis
.
Reporting Tools
Calculated Metrics Creation
Let users create
calculated metrics
. Users can tag, share, delete, rename only the calculated metrics they create or the calculated metrics shared with them.
Reporting Tools
Segment Creation
Let users create
segments
. Users can tag, share, delete, rename only the segments they create or the segments shared with them.
Reporting Tools
Labs Access
Let users access the
Labs
tab in Customer Journey Analytics.
Reporting Tools
Annotation Creation
Let users create
annotations
. Users can tag, share, delete, and rename only the annotations they create or annotations shared with them.
Reporting Tools
Audience View
Let users view
audiences
.
Reporting Tools
Audience Creation
Let users create
audiences
. Requires
Manage Segments
in Adobe Experience Platform.
Reporting Tools
Data storytelling
Let users
generate slide presentations based on Workspace projects.
Reporting Tools
Audit Logs Access
Enforce the permission check on the
API
and the audit logs UI.
Reporting Tools
Share Project Links With Anyone
Let users
share projects with anyone.
Reporting Tools
Forecasting
Let users access the
Forecasting
feature in Analysis Workspace
Reporting Tools
AI Assistant: Product Knowledge
Let users access the
AI Assistant
for product knowledge.
Reporting Tools
Data Insights Agent
Let users access the
Data Insights Agent
for AI driven data insights.
Reporting Tools
Intelligent Captions
Let users access
Intelligent captions
.
Reporting Tools
MCP Access
Let users access the
Customer Journey Analytics MCP server
.
Data View Tools
Full Table Export
Let users
export full tables to the cloud
.
Data View Tools
CJA BI Extension
Let users use the
BI extension
.
## Workspace project curation

Another level of access control can be used at the Workspace reporting level. You can limit access to specific components for certain users. For more information on how to limit components (dimensions, metrics, segments, date ranges) at the Workspace project level, and how curation is tied to data views, see [Curate projects](/en/docs/analytics-platform/using/cja-workspace/curate-share/curate).

## Grant access to individual metrics or dimensions

You cannot grant or deny permissions for individual metrics or dimensions in Customer Journey Analytics like you can in traditional Adobe Analytics. Metrics and dimensions can be modified in [data views](/en/docs/analytics-platform/using/cja-dataviews/data-views) and are thus subject to change in Customer Journey Analytics. Changing them also retroactively changes reporting.

## Use cases

Here are a few use cases that illustrate how access control can be used in real-life scenarios.

### Third-party access

You can provide Product profile administration access to a team lead of a third party that your company works. This admin can add users on the company’s team to this product profile. This Product profile administrator can give access to specific data views and add other users within the third party to this product profile. The Product profile administrator can modify data views to fit the third party team’s requirements.

### Row-level access control

You want to give users access to data from one day only. Here is how you would limit access to those specific rows:

- Create a segment in Settings of a specific data view, where Day equals the date you want them to have data access to. See [Create data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#settings-filters) for more information.
- Save the data view, which applies the segment to the data part of the datasets in the underlying connection. Any rows that don’t fit the segment definition are automatically excluded from the data view and not available to Analysis Workspace when using this data view.
- Create a new [Product profile](#product-profile-admin-role) in the Admin Console, add users to the product profile, and include only this specific data view to the product profile.

### Value-level access control

Users who have access to a data view can only work with the metrics and dimensions that the administrator has included in this data view. Administrators can use the [Include/Exclude functionality](/en/docs/analytics-platform/using/cja-dataviews/component-settings/include-exclude-values) or [Value bucketing](/en/docs/analytics-platform/using/cja-dataviews/component-settings/value-bucketing) component settings in a data views to exclude or aggregate certain dimension values from a data view.

For example: You create a metric called *Hypertension* in a data view from a component that contains individual patient data from the dataset. You use value bucketing to provide only access to bucketed values, so users of the data do not see the individual patients data.

recommendation-more-help
