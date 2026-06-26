---
title: "B2B Edition concepts and features"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-concepts-features"
category: "overview"
topic: "analytics-platform/using/cja-overview/cja-b2b"
created_at: "2026-06-02T19:05:15.574699+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

[B2B Edition]{class="badge informative"}

# B2B Edition concepts and features

Last update: May 19, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User
- Admin

This article explains concepts like connections, identifiers, containers, and datasets, commonly used in Customer Journey Analytics. And how the Customer Journey Analytics B2B Edition adds additional features to these concepts.

## Connections and identifiers

In Customer Journey Analytics, you pick a common identifier, known as Person ID, to connect your event data with other datasets like profile dataset and lookup datasets. This type of connection is known as a person-based connection which facilitates person-based reporting and analysis.

In Customer Journey Analytics B2B Edition, you can select between a person-based connection or an account-based connection. An account-based connection facilitates account-based reporting and analysis.

- For a person-based connection, you select Person as the primary identifier. You can then configure and set up your connection, data view and workspace projects for person-based reporting.
- For an account-based connection, you select Account as the primary identifier. You can then optionally add additional containers for Global Account, Buying Group and Opportunity. Based on whether you add a Global Account or not, your primary identifier is an account identifier or a global account identifier.

## Containers

In Customer Journey Analytics containers are generated as part of the configuration of a connection and data view, and provide data structure and scope. Containers store groups of identifiers to sequence all event timestamps by unique identifiers. That storage facilitates quick and performant execution of functionalities like segmentation, attribution, and visualizations.

### Standard containers

Customer Journey Analytics is built around the concept of three containers: Person, Session, and Event. During a configuration, these containers are implicitly generated.

You can redefine how these containers are named when you configure a data view but the hierarchy and relationships between the containers is predetermined. The Session container is generated based on how you define a session in the [Session settings](/en/docs/analytics-platform/using/cja-dataviews/session-settings) in your data view.

{modal="regular"}

### B2B containers

In Customer Journey Analytics B2B Edition, an Account container is added to the list of generated containers. And you have the option to configure the generation of additional containers, like Global Account, Buying Group, and Opportunity.

The hierarchy and relationships between the containers is predetermined. Opportunity, Buying Group and Person are all sibling containers of the Account container. In that hierarchy the Session container between the Person container and Event container is generated based on how you define a session in the [Session settings](/en/docs/analytics-platform/using/cja-dataviews/session-settings) in your data view. Additional session containers, for example between the Account container and Event container, are currently not generated and supported. See the table below for a description and basic usage of the B2B containers.

{modal="regular"}

B2B container
Description
Basic use case
Account
A company that is a customer or potential customer of your business. The company could be a subsidiary or division of a larger organization. Account represents the organization that you are selling to and want to track at that organization level.
Global Account (optional)
The top parent company of a group of related companies. A global account has no parent company, but may have subsidiaries or divisions belonging to the global account. When you have the Global Account container configured in your connection, an account that has no parent or subsidiaries should be listed in both the account field and global account field.
Opportunity (optional)
A collection of products and services that are sold together. An opportunity often involved various stages in the sales cycle up until the closure of the sale.
You would use data to measure the opportunity progression through the sales funnel. For example, a report that provides details on the top opportunities that moved from stage 3 to stage 4.
Buying group (optional)
A collection of people within an organization that is involved in the decision-making process to purchase a product or service.
You would use buying group data to track buying groups through campaign management. For example, build an audience segment of key buying groups.
You most likely want a lookup from the buying group to profile data, so you can report on the people in a buying group.
Person
An individual, often identified by a unique e-mail address that has interacted with the company.
You would use the profile data to identify people who work for an account. For example: target all the people at an account that have signed-up for a conference.
IMPORTANT
- If you have **enabled** the Global Account container in an account-based connection, every record in your event datasets should contain an Account ID and Global Account ID. If not, the record is skipped.
- If you have **not enabled** the Global Account container in an account-based connection, every record in your event datasets should contain an Account ID. If not, the record is skipped.

You can use the B2B containers for specific B2B functionality in Analysis Workspace:

- Segmentation : B2B segment containers allow you to build segments with a container scope beyond person, session or event. For example: an Accounts with event registration segment, or a US accounts with buying groups and stage 5 opportunities segment. note NOTE The B2B event data in an account based setup in Customer Journey Analytics B2B Edition may contain rows of data without a person or session. For example: a row that details opportunity stage progression. When you evaluate your segment, keep in mind that people and sessions may no longer be the right criteria.
- Attribution : You can use the new B2B containers in attribution panel , in attribution component settings , in calculated metrics , or in columns in a Freeform table . Account lookbacks are extended to 13 months.
- Visualizations : Fall out , Flow , Journey canvas , and Cohort table visualizations support the new B2B containers. For example: you can use the new containers to understand how buying groups consume content, or how opportunity cohorts move towards the close of a sale. You can also set the default container for these visualizations in the user preferences .

Segments, attribution, and visualizations together with the B2B containers support you in deep B2B analysis and insights.

## Datasets

The Customer Journey Analytics B2B distinguishes between the following data types and datasets.

Data type
Time series
Container records
Field records
Datasets
**Event datasets**For example:

- Digital analytics
- CRM events
- In-person events
- Call center data

**Profile datasets**For example:

- CRM records
- AJO B2B records
- CDP records

**Classications**For example:

- Campaign records
- Marketing list records
- Content metadata
- Product records

Requirements
**Time stamp**Every record needs:

- Account ID
- Global Account ID (optional)

**Account ID**Records need a container ID, like:

- Account
- Person
- Opportunity
- Buying Group

**Matching key**Records need an ID contained in a container or event dataset, like:

- Campaign ID
- Content ID
- Product ID

An example account-based connection in the Customer Journey Analytics B2B Edition:

Customer Journey Analytics B2B Edition offers the [Connection map](/en/docs/analytics-platform/using/cja-connections/create-connection#connection-map) interface to provide you with an overview of the relationships between datasets in your connection.

Similar to Customer Journey Analytics, event-based time series data is at the core of Customer Journey Analytics B2B Edition. The main difference for an account-based connection is that you need an account ID on every record in your event dataset instead of a person ID.

When you configure [datasets settings](/en/docs/analytics-platform/using/cja-connections/create-connection#dataset-settings) for your account-based connection in Customer Journey Analytics B2B Edition, the options available for some of the settings depend on the [dataset type](/en/docs/analytics-platform/using/cja-connections/create-connection#dataset-types). For example, you have to:

- Specify identifiers for each of the containers that you have configured for your event datasets.
- Define an account field or global account field for your profile datasets.
- Define keys and how to match these keys (by container of field) for lookup datasets.

## Match by container or field

You can define for each lookup dataset, whether you match the dataset by field or by container.

### Match by container

If a record dataset uses a match by container, the record dataset is treated as a profile dataset type and as a Profile dataset in the user interface. Use match by container on datasets that contain container records and that support your configured containers. For example, a Buying Group dataset.

### Match by field

If a record dataset uses a match by field, the record dataset is treated as a lookup dataset type and as a Lookup dataset in the user interface. Use match by field on datasets that contain additional classification details through lookup. For example, a Marketing List Member dataset, or a Product Details dataset.

## Report on person and account based data

If you want to report on person-based containers (and person identities) and account-based containers (and account identities), you should set up two separate connection within Customer Journey Analytics. One connections where you select Person as the Primary ID, and one connection where you select Account as the Primary ID. Customer Journey Analytics does not support person-based and account-based reporting from a single container hierarchy.

recommendation-more-help
