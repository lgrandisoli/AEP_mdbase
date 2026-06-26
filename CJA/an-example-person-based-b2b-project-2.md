---
title: "An example person-based B2B project"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/b2b/example"
category: "other"
topic: "analytics-platform/using/cja-usecases/b2b"
created_at: "2026-06-23T20:42:34.195705+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# An example person-based B2B project

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- User

This article illustrates a use case where you want to properly report in Customer Journey Analytics on person data within the context of a typical person-based B2B setup. Such a configuration is facilitated by the [Real-Time CDP B2B edition](/en/docs/experience-platform/rtcdp/intro/rtcdpb2b-intro/b2b-overview). The use case explains how to set up, configure and report on profile (person) level based B2B data in Customer Journey Analytics.

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank) A separate section for account-based reporting use cases is published with the release of [Customer Journey Analytics B2B Edition](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition).

## Connection

Define your connection to include all relevant B2B datasets from Experience Platform. Datasets you can consider to add to your connection:

Dataset (optional)
Schema
Schema type
Base class
Description
B2B Activity Dataset
B2B Activity Schema
Event
XDM ExperienceEvent
An ExperienceEvent is a fact record of what occurred, including the point in time and identity of the individual involved. ExperienceEvents can be either explicit (directly observable human actions) or implicit (raised without a direct human action) and are recorded without aggregation or interpretation. Experience events are critical for time-domain analytics as they allow for observation and analysis of changes that occur in a given window of time and the comparison between multiple windows of time to track trends.
B2B Person Dataset
B2B Person Schema
Profile
XDM Individual Profile
An XDM Individual Profile forms a singular representation of the attributes and interests of both identified and partially identified individuals. Less-identified profiles may contain only anonymous behavioral signals, such as browser cookies, while highly identified profiles may contain detailed personal information such as name, date of birth, location, and email address. As a profile grows, it becomes a robust repository of personal information, identification information, contact details, and communication preferences for an individual.
B2B Account Dataset
B2B Account Schema
Lookup
XDM Business Account
An XDM Business Account is a standard Experience Data Model (XDM) class that captures the minimum required properties of a business account. This XDM class can only be included in the profile for customers with the B2B or B2P Edition.
B2B Opportunity Dataset
B2B Opportunity Schema
Lookup
XDM Business Opportunity
XDM Business Opportunity is a standard Experience Data Model (XDM) class that captures the minimum required properties of a business opportunity. This XDM class can only be included in the profile for customers with the B2B or B2P Edition.
B2B Campaign Dataset
B2B Campaign Schema
Lookup
XDM Business Campaign
XDM Business Campaign is a standard Experience Data Model (XDM) class that captures the minimum required properties of a business campaign. This XDM class can only be included in the profile for customers with the B2B or B2P Edition.
B2B Marketing List Dataset
B2B Marketing List Schema
Lookup
XDM Business Marketing List
XDM Business Marketing List is a standard Experience Data Model (XDM) class that captures the minimum required properties of a marketing list. Marketing lists allow you to prioritize on prospect clients who are most likely to buy your product. This XDM class can only be included in the profile for customers with the B2B or B2P Edition.
B2B Account Person Relation Dataset
B2B Account Person Relation Schema
Lookup
XDM Business Account Person Relation
XDM Business Account Person Relation is a standard Experience Data Model (XDM) class that captures the minimum required properties of a person that is associated with a business account.
B2B Opportunity Person Relation Dataset
B2B Opportunity Person Relation Schema
Lookup
XDM Business Opportunity Person Relation
XDM Business Opportunity Person Relation is a standard Experience Data Model (XDM) class that captures the minimum required properties of a person that is associated with a business opportunity.
B2B Marketing List Member Dataset
B2B Marketing List Member Schema
Lookup
XDM Marketing List Members
XDM Business Marketing List Members is a standard Experience Data Model (XDM) class that describes members, persons, or contacts associated with a marketing list.
B2B Campaign Member Dataset
B2B Campaign Member Schema
Lookup
XDM Business Campaign Members
XDM Business Campaign Members is a standard Experience Data Model (XDM) class that describes a contact or lead associated with a business campaign.
The relationship between the B2B lookup schemas, profile schema, and event schema is defined in the B2B setup within Experience Platform. See Schemas in [Real-Time Customer Data Platform B2B Edition](/en/docs/experience-platform/rtcdp/schemas/b2b) and [Define a many-to-one relationship between two schemas in Real-Time Customer Data Platform B2B Edition](/en/docs/experience-platform/xdm/tutorials/relationship-b2b).

To ensure a proper setup of a connection that supports person-based lookups of your B2B data, use the following illustration for an overview and follow these steps:

- Add datasets from the table above to your connection.
- For each lookup dataset that you add to your connection, you must explicitly define the relationship to an event dataset using the Key and the Matching key in the Edit dataset dialog.
- For each lookup dataset that you want to transform for person-based B2B lookups, enable Transform dataset to ensure that the data is transformed for person-based lookups. See Transform datasets for B2B lookups for additional information. The table below provides an example overview of the Person ID, Key, and Matching key example values for each of the datasets. note important IMPORTANT The values for Person ID , Key , and Matching Key in the table below are example values , and can be different in your specific environment. table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 6-row-4 7-row-4 8-row-4 9-row-4 10-row-4 Dataset (optional) Person ID Key Matching key (in event dataset) B2B Activity Dataset SourceKey personKey.sourceKey B2B Person Dataset SourceKey b2b.personKey.sourceKey B2B Account Dataset SourceKey accountKey.sourceKey ❶ SourceKey (B2B Person Dataset) b2b.accountKey.sourceKey ❶ B2B Opportunity Dataset Source Key opportunityKey.sourceKey ❷ SourceKey (B2B Opportunity Relation Dataset) opportunityKey.sourceKey ❷ B2B Campaign Dataset SourceKey campaignKey.sourceKey ❸ SourceKey (B2B Campaign Member Dataset) campaignKey.sourceKey ❸ B2B Marketing List Dataset SourceKey marketingListKey.sourceKey ❹ SourceKey (B2B Marketing List Member Dataset) marketingListKey.sourceKey ❹ B2B Account Person Relation Dataset SourceKey personKey.sourceKey ❺ Source Key (Event datasets) personKey.sourceKey ❺ B2B Opportunity Person Relation Dataset SourceKey personKey.sourceKe y❻ Source Key (Event datasets) personKey.sourceKey ❻ B2B Campaign Member Dataset SourceKey personKey.sourceKey ❼ Source Key (Event datasets) personKey.sourceKey ❼ B2B Marketing List Member Dataset SourceKey personKey.sourceKey ❽ Source Key (Event datasets) personKey.sourceKey ❽

See [Add and configure datasets](/en/docs/analytics-platform/using/cja-connections/create-connection) for more information on how to configure settings for a dataset.

## Data view

To have access to relevant B2B dimensions and metrics when building your Workspace project, you must define your data view accordingly.

You can, for example, add the following components to your data view to ensure you can report on person-based level on your B2B data. The component names are sometimes modified for clarity from their original schema names.

Metrics
| note important |
| --- |
| IMPORTANT |
| The metrics and their values (**Component name**, **Dataset**, **Dataset type**, and **Schema path)** in the table below are **examples**. Define relevant B2B metrics (Component name, Dataset, Data type, and Schema path) for your specific situation. |

| table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 6-row-4 7-row-4 |  |  |  |
| --- | --- | --- | --- |
| Component name | Dataset | Data type | Schema path |
| Annual Account Revenue | B2B Account Dataset | Double | accountOrganization.annualRevenue.amount |
| Number of Employees | B2B Account Dataset | Integer | accountOrganization.numberOfEmployees |
| Actual Campaign Cost | B2B Campaign Dataset | Double | actualCost.amount |
| Budgeted Campaign Cost | B2B Campaign Dataset | Double | budgetedCost.amount |
| Expected Opportunity Revenue | B2B Opportunity Dataset | Double | expectedRevenue.amount |
| Expected Campaign Revenue | B2B Campaign Dataset | Double | expectedRevenue.amount |
| Opportunity Amount | B2B Opportunity Dataset | Double | opportunityAmount.amount |

Dimensions
| note important |
| --- |
| IMPORTANT |
| The dimensions and their values (**Component name**, **Dataset**, **Dataset type**, and **Schema path)** in the table below are **examples**. Define relevant B2B dimensions (Component name, Dataset, Data type, and Schema path) for your specific situation. |

| table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 6-row-4 7-row-4 8-row-4 9-row-4 10-row-4 11-row-4 12-row-4 |  |  |  |
| --- | --- | --- | --- |
| Component name | Dataset | Data type | Schema path |
| Account Name | B2B Account Dataset | String | accountName |
| Campaign Name | B2B Campaign Dataset | String | campaignName |
| Channel Name | B2B Campaign Dataset | String | channelName |
| Country | B2B Account Dataset | String | accountBillingAddress.country |
| Forecast Category Name | B2B Opportunity Dataset | String | forecastCategoryName |
| Industry | B2B Account Dataset | String | accountOrganization.industry |
| Last name | B2B Person Dataset | String | person.name.lastName |
| Marketing List Name | B2B Marketing List Dataset | String | marketingListName |
| Opportunity Name | B2B Opportunity Dataset | String | opportunityName |
| Opportunity Stage | B2B Opportunity Dataset | String | opportunityStage |
| Opportunity Type | B2B Opportunity Type Dataset | String | opportunityType |
| Webinar Session Name | B2B Campaign Dataset | String | webinarSessionName |

## Workspace

With your components properly defined in the data view, you can now build specific B2B reports and visualizations in your Workspace project.

Below is a screenshot from an example project that relies on the connection and data view described above. The visualization descriptions explain which of the freeform table visualization relies on the transformed B2B lookup data.

recommendation-more-help
