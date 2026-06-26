---
title: "Configure Data warehouse native solutions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-mirror/configure/datawarehouse"
category: "other"
topic: "analytics-platform/using/cja-data-mirror/configure"
created_at: "2026-06-02T19:05:07.475191+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

[Beta]{class="badge informative"}

# Configure Data warehouse native solutions

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

AVAILABILITY
The functionality described in this article is in the Limited Testing phase of release and might not be available yet in your environment. This note will be removed when the functionality is generally available. For information about the Customer Journey Analytics release process, see
Customer Journey Analytics feature releases
.
To support Experience Platform Data Mirror for Customer Journey Analytics, the data you want to use from the three supported data warehouse native solutions ([Azure Databricks](#azure-databricks), [Google BigQuery](#google-bigquery), [Snowflake](#snowflake)) needs enablement for change data capture.

## Azure Databricks

Enable **change data feed** in your Azure Databricks tables to use change data capture in your source connection.

Use the following commands to enable change data feed on your tables:

**New table**

To apply change data feed to a new table, you must set the table property delta.enableChangeDataFeed to TRUE in the CREATE TABLE command.

```
CREATE TABLE student (id INT, name STRING, age INT) TBLPROPERTIES (delta.enableChangeDataFeed = true)
```

**Existing table**

To apply change data feed to an existing table, you must set the table property delta.enableChangeDataFeed to TRUE in the ALTER TABLE command.

```
ALTER TABLE myDeltaTable SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
```

**All new tables**

To apply change data feed to all new tables, you must set your default properties to TRUE.

```
set spark.databricks.delta.properties.defaults.enableChangeDataFeed = true;
```

For more information, read the [Azure Databricks guide on enabling change data feed](https://docs.databricks.com/aws/en/delta/delta-change-data-feed#enable-change-data-feed).

Read the following documentation for steps on how to enable change data capture for your Azure Databricks source connection:

- [Create a Azure Databricks base connection](/en/docs/experience-platform/sources/api-tutorials/create/databases/databricks).
- [Create a source connection for a database](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql#create-a-source-connection).

## Google BigQuery

To use change data capture in your Google BigQuery source connection, navigate to your Google BigQuery page in the Google Cloud console and set enable_change_history to TRUE. This property enables change history for your data table.

For more information, read the guide on [data definition language statements in GoogleSQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_option_list).

Read the following documentation for steps on how to enable change data capture for your Google BigQuery source connection:

- [Create a Google BigQuery base connection](/en/docs/experience-platform/sources/api-tutorials/create/databases/bigquery).
- [Create a source connection for a database](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql#create-a-source-connection).

## Snowflake

Enable **change tracking** in your Snowflake tables to use change data capture in your source connections.

In Snowflake, enable change tracking by using the ALTER TABLE and setting CHANGE_TRACKING to TRUE.

```
ALTER TABLE mytable SET CHANGE_TRACKING = TRUE
```

For more information, read the [Snowflake guide on using the changes clause](https://docs.snowflake.com/en/sql-reference/constructs/changes#usage-notes).

Read the following documentation for steps on how to enable change data capture for your Snowflake source connection:

- [Create a Snowflake base connection](/en/docs/experience-platform/sources/api-tutorials/create/databases/snowflake).
- [Create a source connection for a database](/en/docs/experience-platform/sources/api-tutorials/collect/database-nosql#create-a-source-connection).

Related Articles
Data Mirror quick start guide: Mirror and use relational data
recommendation-more-help
