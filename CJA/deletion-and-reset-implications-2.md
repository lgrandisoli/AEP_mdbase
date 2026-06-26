---
title: "Deletion and reset implications"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/technotes/deletion"
category: "other"
topic: "analytics-platform/using/technotes/deletion"
created_at: "2026-06-23T20:42:35.969941+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Deletion and reset implications

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)
- [Integrations](#)

CREATED FOR:

- Admin

The deletion or reset of Customer Journey Analytics or Experience Platform objects do have implications. These implications are outlined in this article.

## Customer Journey Analytics

Consider the following implications before you delete connections, data views or datasets in Customer Journey Analytics:

Action
Implications
Delete a connection in Customer Journey Analytics
An error message indicates that:

- Any data views created for the deleted connection no longer works.
- Similarly, any Workspace projects that depend on data views in the deleted connection cease working.

Note that you cannot delete Customer Journey Analytics connections that:

- Are tied to Adobe Experience Platform sandboxes for which you do not have permissions. Even if you have permissions to the data views built on those connections, you cannot delete the connections until you are granted permissions to the underlying Adobe Experience Platform sandboxes.
- Have the following compatibility option selected for a data view that is associated with the connection: Set as default data view in Adobe Journey Optimizer For more information about this configuration option, see Compatibility in Create or edit a data view .
- Are used in a configuration for any of the following services: Audience analysis : Provides audience data to Customer Journey Analytics for in-depth analysis Adobe Content Analytics : Provides data on content consumption and impact to Customer Journey Analytics Before you can delete the connection, you must first delete or edit the configuration that uses this connection.

Delete a dataset in Customer Journey Analytics
When you delete a dataset from a connection in Customer Journey Analytics, any data views and projects that relies on that dataset no longer works.
Delete a data view in Customer Journey Analytics
When you delete a data view in Customer Journey Analytics, any panel in a Workspace project that relies on the data view no longer works properly.

Note that you cannot delete Customer Journey Analytics data views that are used in a configuration for any of the following services:

- [Audience analysis](/en/docs/analytics-platform/using/cja-connections/audience-analysis/audience-analysis-overview): Provides audience data to Customer Journey Analytics for in-depth analysis
- [Adobe Content Analytics](/en/docs/analytics-platform/using/content-analytics/content-analytics): Provides data on content consumption and impact to Customer Journey Analytics

Before you can delete the data view, you must first delete or edit the configuration that uses this data view.

## Experience Platform

Consider the following implications before you delete datasets or batches, or when you reset or delete sandboxes in Experience Platform:

Action
Implications
Delete one or more records from a dataset in Experience Platform
The records are deleted from the Customer Journey Analytics connections that have the dataset defined as part of the connection configuration.
Delete a dataset in Experience Platform
The data flow from that dataset in Experience Platform stops to any connections that include that dataset. Any data from that dataset is automatically deleted from the associated Customer Journey Analytics connections.
Delete a batch from a dataset in Experience Platform
If a batch is deleted from an Adobe Experience Platform dataset, the same batch is removed from any Customer Journey Analytics connections that contain that specific batch. Customer Journey Analytics is notified of batches that were deleted in Adobe Experience Platform.
Delete a batch from Experience Platform
while it is being ingested
into Customer Journey Analytics
If there is only one batch in the dataset, no data or partial data from that batch appears in Customer Journey Analytics. The ingestion is rolled back. If, for example, there are 5 batches in the dataset and 3 of them have already been ingested when the fourth batch was deleted, data from those 3 batches appears in Customer Journey Analytics.
Delete lookup datasets in Experience Platform
While deleting datasets is possible for other source connectors, deletion of
Analytics Classifications Source Connector
datasets is not supported. If you do delete such a dataset by mistake, please contact Customer Care.
Delete or reset a sandbox in Experience Platform
When you [delete an Experience Platform sandbox](/en/docs/experience-platform/sandbox/ui/user-guide#delete-a-sandbox), all schemas, datasets, batches, policies, and more in that sandbox are deleted as well. The sandbox no longer exists, as well as the sandbox identifier and sandbox name.When you [reset an Experience Platform sandbox](/en/docs/experience-platform/sandbox/ui/user-guide#reset-a-sandbox), all schemas, datasets, batches, policies, and more in that sandbox are deleted. While the sandbox name and permissions remain untouched, the sandbox identifier is changed after the reset is complete.Customer Journey Analytics uses the sandbox identifier and sandbox name to associate a connection with a sandbox. As a result:

- Connections associated with the deleted or reset sandbox are deleted.
- Data views (and all component definitions, such as derived fields, within the data view) that are based on the deleted connections are deleted.
- Components relying on the deleted data views are deleted. Such as segments, calculated metrics, annotations, alerts, published audiences, and exports.
- Panels in Workspace projects that reference the deleted data views become unusable. These panels show **Unknown data view** errors. Remove these panels, or, if possible, associate these panels with an existing data view.
- You should no longer query (historical) data from the deleted connection that is already available within Customer Journey Analytics using Query Service or tools that rely on the BI extension. Eventually Adobe support or engineering deletes this data from Customer Journey Analytics.

As the implications of a reset or deletion of a sandbox in Experience Platform are substantial, consider the following before you reset or delete a sandbox:

- List your connections to understand which connections belong to which sandboxes.
- List data views to understand which data views are associated with which connections.
- Identify important Workspace projects and understand which data views these projects reference in their panels.
- Identify integrations with tools that use the BI extension and understand which data views these integrations rely on.

recommendation-more-help
