---
title: "Configure Customer Journey Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-mirror/configure/cja"
category: "other"
topic: "analytics-platform/using/cja-data-mirror/configure"
created_at: "2026-06-23T20:42:26.586146+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure Customer Journey Analytics

Last update: June 18, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- Admin

INFO
In the Customer Journey Analytics interface,
Relational
datasets might be labeled as
Model-based
.
To use the Experience Platform Data Mirror feature for Customer Journey Analytics, you have to create or update connections, data views and workspace projects to use relational data.

## Connections

In your connection, add the relational datasets that represent the data from the data warehouse native solutions. These datasets do have the Relational dataset type.

When you add a relational dataset that contains mirrored data from a data warehouse native solution, that data is usually event data. Ensure you select the correct settings for the dataset. For example, select the correct dataset type, field for identity, and field for timestamp.

## Data views

Define fields from the relational schema as components (metrics and dimensions) in your data view. The data mirrored fields are available in the **Adhoc & relational fields** subfolder of the **Event datasets** folder. Use functionalities, like [derived fields](/en/docs/analytics-platform/using/cja-dataviews/derived-fields) or [component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview), to modify the components that are based on relational fields.

## Workspace projects

Set up Workspace projects that use metrics and dimensions from your relational data. Components that are ultimately based on data in your data warehouse native solution. And are updated based on the data mirror functionality you have configured.

Related Articles
Data Mirror quick start guide: Mirror and use relationald data
recommendation-more-help
