---
title: "Get Started with schemas schemas-gs"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/data-management/get-started-schemas"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:16.349826+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get Started with schemas schemas-gs

Last update: May 8, 2026
- Topics:
- [Data Model](#)
- [Datasets](#)
- [Data Management](#)

CREATED FOR:

- Experienced
- Developer
- Admin

Adobe Journey Optimizer relies on **Adobe Experience Platform schemas** to describe the structure of data in a consistent and reusable way. A schema provides an abstract definition of a real-world object (such as a person) and outlines what data should be included in each instance of that object (such as name, birthday, and so on). When data is ingested into Experience Platform, it is always structured according to an **XDM schema**.

## Standard & relational schemas

There are two types of schemas in Adobe Experience Platform:

- Standard schemas are hierarchical schemas that use classes and field groups to capture record or time-series data. A standard schema is composed of: A class (which defines the data behavior: record or time-series). One or more field groups (which add specific fields to the schema). In Journey Optimizer, standard schemas are typically used to represent individual people and their attributes , capture time-series interactions such as clicks, purchases, or logins, and power Real-Time Customer Profile for segmentation and personalization. ➡️ Learn how to create and configure a standard schema in this video (video)
- Relational schemas are flat, non-hierarchical schemas that do not use classes or field groups. They are used to capture record data for relational entities and are primarily used in Journey Optimizer Orchestrated campaigns . Examples of relational entities include: Bookings, contracts, or subscriptions Products or catalogs Stores, locations, or partners With relational schemas, you can send one message per entity (e.g., per booking, per subscription), create segments based on entity attributes (e.g., product category, store location), and improve addressability by reaching all contacts linked to an entity. How relational schemas work: Create schemas manually or import via DDL Link schemas to define relationships between entities and people (e.g., loyalty transactions linked to members, rewards linked to brands). Ingest data into your dataset from supported sources. ➡️ Learn how to manage relational schemas and datasets ➡️ Get started with Orchestrated campaigns

## How-to video video-schema

Learn how to create a standard schema, add field groups, create, and configure custom field groups.

https://video.tv.adobe.com/v/334461?quality=12&learn=on
Related Articles
- [Get started with data management in Journey Optimizer](/en/docs/journey-optimizer/using/data-management/gs-data)
- [Create a schema, a dataset and ingest data to add Test profiles in Journey Optimizer](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles)
- [XDM System overview](/en/docs/experience-platform/xdm/home#_blank)
- [Best practices for data modeling](/en/docs/experience-platform/xdm/schema/best-practices#_blank)
- [Create a schema using the Schema Registry API](/en/docs/experience-platform/xdm/tutorials/create-schema-api#_blank)
- [Define a relationship between two schemas using the Schema Editor](/en/docs/experience-platform/xdm/tutorials/relationship-ui#_blank)

recommendation-more-help
