---
title: "Get started with relational schemas and datasets gs-schemas"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/data-configuration/schemas-datasets/gs-schemas"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:47.624870+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with relational schemas and datasets gs-schemas

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

This guide walks you through the process of creating a relational schema, configuring a dataset for Orchestrated campaigns and ingesting data.

{modal="regular"}

## Key concepts

In the context of Orchestrated campaigns, a **dataset** is a storage and management construct for a collection of data, typically a table, that contains a schema (rows) and fields (columns). Data that is successfully ingested into Experience Platform is stored within the data lake as datasets.

A **schema** represents and validates the structure and format of data. It provides an abstract definition of a real-world object (such as a person) and outlines what data should be included in each instance of that object (such as name, birthday, and so on).

A **data model** is the conceptual blueprint of normalizing your data

It describes:

- The entities (e.g., Customer, Campaign, Segment)
- The attributes of those entities (e.g., Customer Name, Campaign Start Date)
- The relationships between entities (e.g., Customers belong to Segments, Campaigns target Segments)

A data model is logical and conceptual, not tied to a physical implementation in Orchestrated campaign

In a **relational data model**, data is organized into tables relating to other tables.

- Each table has rows(records) and columns(attributes)
- Every table has a primary key to uniquely identify rows
- Relationships between tables are expressed using foreign keys

A **relational schema** is the formal definition of the relational data model.

It specifies:

- The set of tables
- The columns in each table
- The constraints
- The relationships across tables

Organizing schemas or tables in a relational data model is about structuring your data into multiple tables. Ensure each table stores one type of entity/schemas

➡️ [Learn more about schemas in Adobe Experience Platform documentation](/en/docs/experience-platform/xdm/ui/resources/schemas#create-model-based-schema)

## Implementation steps implementation

To ingest data and create relational schema, follow these steps:

- Create relational schema manually or using a DDL file Define the structure of your data model, including tables, attributes, and relationships. Choose to build the schema manually in the user interface or upload a DDL file for faster setup. When creating the schema manually, dataset must also be created and enabled manually. When using a DDL file, dataset creation and enablement are automatic.
- Link schemas Establish relationships between your schemas to ensure data consistency and enable cross-entity queries. For example, link loyalty transactions to recipients or rewards to brands.
- Create Dataset After defining your schema, you need to create a dataset based on it. This dataset acts as the storage for your ingested data.
- Enable Orchestrated campaigns The dataset stores your ingested data and must be enabled for Orchestrated campaigns to ensure it is accessible in Adobe Journey Optimizer.
- Ingest Data Bring data into Adobe Experience Platform from supported sources such as SFTP, cloud storage, or databases.

recommendation-more-help
