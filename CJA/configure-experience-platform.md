---
title: "Configure Experience Platform"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-mirror/configure/aep"
category: "other"
topic: "analytics-platform/using/cja-data-mirror/configure"
created_at: "2026-06-02T19:05:06.297629+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

[Beta]{class="badge informative"}

# Configure Experience Platform

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

AVAILABILITY
The functionality described in this article is in the Limited Testing phase of release and might not be available yet in your environment. This note will be removed when the functionality is generally available. For information about the Customer Journey Analytics release process, see
Customer Journey Analytics feature releases
.
Experience Platform Data Mirror for Customer Journey Analytics requires the proper configuration of several Experience Platform components:

- schema
- dataset
- source connector

Find below details that you should consider when configuring each of these components.

## Schema

You need to create a [relational schema](/en/docs/experience-platform/xdm/schema/relational#_blank) that s the data warehouse native table you want to mirror. When you construct the relational schema, ensure that the following requirements are met:

- When prompted for the type of relational schema, ensure you select the manual option.
- Select the appropriate schema for the type of data. Note that Experience Platform Data Mirror is mostly used for time series data (for example, event data) but can also be used for record-based (lookup and profile) data.
- Define the fields in your schema and their attributes
- Configure the required attributes for fields in a relational schema: Primary key . Version descriptor , which must be configured as a sequential number (Integer field type) or as a DateTime field type. When you use a DateTime field type, the version descriptor defines the timestamp of a modification of the data, for example to contain a last modified timestamp. Timestamp descriptor (for time series data), which defines the immutable timestamp at the moment that an event is captured. The timestamp descriptor is not required for a record-based relational schema.

## Dataset

You can set up a dataset for your schema in advance, or create a dataset when you set up your source connector.When you create a dataset in advance or select a dataset, ensure you the data uses a relational [schema](#schema) you created earlier.

## Source connector

To set up the source connector to the supported data warehouse native solutions, you use the Sources workflow that guide you through the setup. That workflow consists of the following steps:

### Authentication

For authentication against the supported data warehouse native solution, see the relevant Experience Platform documentation:

- [Azure Databricks](/en/docs/experience-platform/sources/connectors/databases/databricks)
- [Google BigQuery](/en/docs/experience-platform/sources/connectors/databases/bigquery)
- [Snowflake](/en/docs/experience-platform/sources/connectors/databases/snowflake)

### Select data

Once successfully connected to your data warehouse native solution, select the table from the data warehouse native solution you want to use for data mirror. Once selected, a preview of the contents of the data is shown.

### Dataflow detail

Ensure you enable change data capture. You see an information panel, explaining the requirements for change data capture.

Specify a new or existing dataset that is based on the relational schema you created earlier. Specify and select other options in the Dataflow detail interface.

### Mapping

Map the fields of the table in the data warehouse native solution to the fields that you have specified for the relational schema.

### Scheduling

Define a schedule to mirror the data from the table in the data warehouse native solution to the dataset in Experience Platform.

### Review

Review the settings for the source connector to the data warehouse native solution that supports data mirror and change data capture.

Once you finished the setup of the source connector, a dataflow is created. From that moment on data changes (inserts, updates, deletions) in the data warehouse native solution are mirrored to the specified dataset.

Related Articles
Data Mirror quick start guide: Mirror and use relational data
Data Mirror (Experience Platform documentation)
Relational schemas (Experience Platform documentation)
recommendation-more-help
