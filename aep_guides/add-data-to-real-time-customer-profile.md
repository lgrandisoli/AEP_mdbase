---
title: "Add data to Real-Time Customer Profile"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/profile/tutorials/add-profile-data"
category: "tutorials"
topic: "experience-platform/real-time-customer-profile-guide"
created_at: "2026-06-26T17:26:51.359258+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Real-Time Customer Profile Guide

# Add data to Real-Time Customer Profile

Last update: May 23, 2026
- Topics:
- [Profiles](#)

CREATED FOR:

- User

This tutorial outlines the steps necessary to add data to Real-Time Customer Profile.

## Enable a schema for Real-Time Customer Profile

Data being ingested into Experience Platform for use by Real-Time Customer Profile must conform to an Experience Data Model (XDM) schema that is enabled for Profile. In order for a schema to be enabled for Profile, it must implement either the XDM Individual Profile or XDM ExperienceEvent class.

You can enable a schema for use in Real-Time Customer Profile using the Schema Registry API or the Schema Editor user interface. To get started, follow the tutorials for [creating a schema using APIs](/en/docs/experience-platform/xdm/tutorials/create-schema-api) or [creating a schema using the Schema Editor UI](/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

## Add data using batch ingestion

All data uploaded to Experience Platform using batch ingestion is uploaded to individual datasets. Before this data can be used by Real-Time Customer Profile, the dataset in question has to be specifically configured. For complete instructions, see the tutorial on [configuring a dataset for Profile and Identity Service](/en/docs/experience-platform/profile/tutorials/dataset-configuration).

Once the dataset has been configured, you can start ingesting data into it. See the [batch ingestion developer guide](/en/docs/experience-platform/ingestion/batch/api-overview) for detailed steps on how to upload files in different formats.

## Add data using streaming ingestion

Any stream-ingested data that is compliant with a Profile-enabled XDM schema will automatically add or overwrite the appropriate record in Real-Time Customer Profile. If more than one identity is supplied in the record, or time series data is consumed, those identities will be mapped in the identity graph without additional configuration. See the [streaming ingestion developer guide](/en/docs/experience-platform/ingestion/tutorials/streaming-record-data) to learn more.

## Confirm that the upload is successful

When uploading data to a new dataset for the first time, or as part of a process involving a new ETL or data source, it is recommended to carefully check the data to ensure it has been uploaded correctly.

Using the Real-Time Customer Profile Access API, you can retrieve batch data as it gets loaded into a dataset. If you are unable to retrieve any of the entities you expect, your dataset may not be enabled for Profile. After confirming that your dataset has been enabled, ensure that your source data format and identifiers support your expectations.

For detailed instructions on how to access entities using the Real-Time Customer Profile API, please refer to the [entities endpoint guide](/en/docs/experience-platform/profile/api/entities), also known as the “Profile Access API”.

## Update Profile store data

Occasionally it may be necessary to update data in your organization’s Profile store. For example, you may need to correct records or change an attribute value. This can be done through batch ingestion and requires a Profile-enabled dataset configured with an upsert tag. For more information on how to configure a dataset for attribute updates, please refer to the tutorial for [enabling a dataset for Profile and upsert](/en/docs/experience-platform/catalog/datasets/enable-upsert).

recommendation-more-help
