---
title: "B2B Edition quick start guide"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-quick-start-guide"
category: "overview"
topic: "analytics-platform/using/cja-overview/cja-b2b"
created_at: "2026-06-02T19:05:41.309821+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

[B2B Edition]{class="badge informative"}

# B2B Edition quick start guide

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User
- Admin

To implement Customer Journey Analytics B2B Edition, ensure you first do understand the B2B specific concepts and features. Also, you should be familiar with the traditional workflow to implement Customer Journey Analytics.

This document focuses on the workflow specific to the implementation of Customer Journey Analytics.

## Prerequisites

To implement Customer Journey Analytics B2B Edition, the following prerequisites do apply:

- You do have the necessary [access control and permissions](/en/docs/analytics-platform/using/technotes/access-control) to provide administration tasks in Customer Journey Analytics.
- You have puchased the Customer Journey Analytics B2B Edition add-on package.

## Workflow

Task
Details
Step 1: Get B2B data into Experience Platform
This step, performed in Experience Platform, involves several sub steps:

- **Step 1a: Prepare your data schema**: Use [Adobe Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home) to standardize B2B data and [define schemas](/en/docs/experience-platform/rtcdp/schemas/b2b) for your B2B data.
- **Step 1b: Create a dataset based on the schema**: Data in Platform consists of datasets, such as account data, opportunity data, buying group data, campaign data, marketing list data, email datasets, CRM datasets, POS datasets, and more. Each dataset consists of a schema and batches of data. You can [create a dataset in Experience Platform](/en/docs/platform-learn/getting-started-for-data-architects-and-data-engineers/create-datasets).
- **Step 1c: Ingest data into Experience Platform**: You have [several options](/en/docs/experience-platform/ingestion/home).

Step 2: Create connections between platform datasets and Customer Journey Analytics
A connection lets you integrate datasets from Adobe Experience Platform into Workspace. In order to report on Experience Platform datasets, you first have to establish a connection between datasets in Experience Platform and Workspace. You have additional options when you configure a connection with the B2B Edition.
See
Create or edit a connection
.
Step 3: Create data views
A data view is a
filtered
view of the data. You can create different data views for the same connection, with different settings for visit timeout, attribution, and more. You can create multiple data views for a single dataset. You have additional options when you configure a data view when you have the B2B Edition.
See
Create a data view
.
Step 4: Report on your cross-channel data in Workspace
After you have created connections and data views, analyze the B2B data you have brought in using the power and flexibility of Analysis Workspace.
See
Perform basic analysis
and
Perform advanced analysis
.
recommendation-more-help
