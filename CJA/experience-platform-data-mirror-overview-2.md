---
title: "Experience Platform Data Mirror overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-mirror/data-mirror"
category: "overview"
topic: "analytics-platform/using/cja-data-mirror/data-mirror"
created_at: "2026-06-23T20:41:53.352094+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Experience Platform Data Mirror overview

Last update: June 5, 2026
- Topics:
- [Data management](#)
- [Analysis Workspace](#)
- [Components](#)
- [Data governance](#)

CREATED FOR:

- Admin

Data Mirror is an Experience Platform capability that enables row-level change ingestion from external databases into the data lake using relational schemas. It preserves data relationships, enforces uniqueness, and supports versioning without requiring upstream extract, transform, and load (ETL) processes.

Use Experience Platform Data Mirror to synchronize inserts, updates, and deletes (mutable data) from external data warehouse native solutions (Snowflake, Azure Databricks, or Google BigQuery) directly with data in Experience Platform. Data Mirror helps you preserve your existing database model structure and data integrity as you bring data into Experience Platform.

## Capabilities and benefits

Data Mirror provides the following essential capabilities for database synchronization:

- **Primary key enforcement.** Ensures uniqueness within datasets and prevents duplicate records during ingestion.
- **Row-level change ingestion.** Supports granular data changes including upserts and deletes with precision control.
- **Schema relationships.** Enables foreign and primary key relationships between datasets through descriptors.
- **Out-of-order event handling.** Processes change events using version and timestamp descriptors, even when they arrive out of sequence.
- **Direct warehouse integration.** Connects with supported cloud data warehouses for real-time change synchronization.

Use Data Mirror to ingest changes directly from your source systems, enforce schema integrity, and make the data available for analytics, journey orchestration, and compliance workflows. Data Mirror eliminates complex upstream ETL processes and accelerates implementation by enabling direct mirroring of existing database models. This elimination can enhance data governance through precise control over deletions and data hygiene operations.

See also the [Experience Platform documentation on Data Mirror](/en/docs/experience-platform/xdm/data-mirror/overview#_blank).

## Data Mirror for Customer Journey Analytics

NOTE
Data Mirror is a feature that supports the synchronization of data from select data warehouses using change data capture (CDC) for analysis in Customer Journey Analytics.
Refer to the applicable Product Description to understand how the feature can impact annual ingestion limit consumption.
IMPORTANT
The change data capture datasets that you create in Experience Platform for the purpose of Data Mirror for Customer Journey Analytics should not be reused in other Experience Platform solutions like Real-Time Customer Data Platform or Journey Optimizer. If you want to use the same data for these solutions, consider to create alternative datasets with that same data.
Experience Platform Data Mirror for Customer Journey Analytics is available for selected data warehouse native solutions (Azure Databricks, Google BigQuery, and Snowflake). The Customer Journey Analytics version of Experience Platform Data Mirror requires proper configuration of the following applications or components:

- [Data warehouse native solutions](/en/docs/analytics-platform/using/cja-data-mirror/configure/datawarehouse)
- [Experience Platform](/en/docs/analytics-platform/using/cja-data-mirror/configure/aep)
- [Customer Journey Analytics](/en/docs/analytics-platform/using/cja-data-mirror/configure/cja)

Related Articles
Data Mirror quick start guide: Mirror and use relational data
Data Mirror (Experience Platform documentation)
Relational schemas (Experience Platform documentation)
recommendation-more-help
