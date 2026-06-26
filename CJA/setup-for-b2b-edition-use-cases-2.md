---
title: "Setup for B2B Edition use cases"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/setup"
category: "other"
topic: "analytics-platform/using/cja-usecases/b2b"
created_at: "2026-06-23T20:44:59.126752+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

[B2B Edition]{class="badge informative"}

# Setup for B2B Edition use cases

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- User

This article covers a typical setup of the Customer Journey Analytics B2B Edition to support the following uses cases:

- [Optimize account marketing](/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/optimize-account-marketing)
- [Grow key accounts](/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/grow-key-accounts)
- [Build product value](/en/docs/analytics-platform/using/cja-usecases/b2b/b2b-edition/build-product-value)

NOTE
The demo data and screenshots that are used in these use cases are for illustration purposes only and do not reflect real world data.
## Solution design reference

Before you set up Customer Journey Analytics B2B Edition, ensure you have a proper solution design reference in place that documents each of the fields you collect.

An example solution design reference could look like:

Event dimensions
| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 8-row-1 9-row-1 10-row-1 11-row-1 12-row-1 13-row-1 14-row-1 15-row-1 16-row-1 17-row-1 18-row-1 19-row-1 20-row-1 21-row-1 22-row-1 23-row-1 24-row-1 25-row-1 26-row-1 27-row-1 28-row-1 29-row-1 30-row-1 31-row-1 32-row-1 33-row-1 |
| --- |
| Dimension name |
| Account ID |
| Account Name |
| Buying Group ID |
| Call Center |
| Call Center Representative ID |
| Call ID |
| Campaign Tracking Code |
| Content ID |
| Content Type |
| Data Source |
| Device Type |
| Event Details |
| Event Name |
| Funnel |
| Interaction Channel |
| Lead ID |
| Marketing Channel |
| Marketing Event ID |
| Marketing Event Type |
| Opportunity ID |
| Page |
| Page Details |
| Referring Domain |
| Sales Representative ID |
| Sales Stage Name |
| Sales Stage Number |
| Site Section |
| SKU |
| Subsidiary Account ID |
| Survey ID |
| Survey Satisfaction Score |
| Survey Type |
| User ID |

Event metrics
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 16-row-2 17-row-2 18-row-2 19-row-2 20-row-2 21-row-2 22-row-2 23-row-2 24-row-2 25-row-2 26-row-2 27-row-2 28-row-2 29-row-2 30-row-2 31-row-2 32-row-2 33-row-2 34-row-2 35-row-2 36-row-2 37-row-2 38-row-2 39-row-2 40-row-2 41-row-2 42-row-2 43-row-2 44-row-2 45-row-2 46-row-2 47-row-2 48-row-2 49-row-2 50-row-2 51-row-2 52-row-2 53-row-2 54-row-2 |  |
| --- | --- |
| Metric name | Event type |
| Account Creation: Complete | Counter |
| Account Creation: Start | Counter |
| Call Cost | Currency |
| Call Length | Counter |
| Call Satisfaction Score | Numeric |
| Call Surveys Completed | Counter |
| Calls | Counter |
| Closed-Lost | Counter |
| Closed-Won | Counter |
| Content Views | Counter |
| Deal Size Currency Display Click-throughs | Counter |
| Display Impressions | Counter |
| Email Bounced | Counter |
| Email Clicked | Counter |
| Email Delivered | Counter |
| Email Opened | Counter |
| Email Sent | Counter |
| Event Attendance | Counter |
| Event Registration: Complete | Counter |
| Event Registration: Step 1 | Counter |
| Event Registration: Step 2 | Counter |
| Event Registration: Step 3 | Counter |
| Global Satisfaction Score Numeric Inbound Call | Counter |
| Lead Form: Complete | Counter |
| Lead Form: Step 1 | Counter |
| Lead Form: Step 2 | Counter |
| Lead Generated | Counter |
| Lead Qualification | Counter |
| Meetings | Counter |
| MQL Disqualified | Counter |
| MQL Qualified | Counter |
| Needs Assessment | Counter |
| Negotiation | Counter |
| Objection Handling | Counter |
| Opportunities | Counter |
| Opportunity Creation | Counter |
| Orders | Counter |
| Outbound Call | Counter |
| Post-Sales Follow-Up | Counter |
| Proposal Submission | Counter |
| Revenue Closed-Lost | Currency |
| Revenue Closed-Won | Currency |
| Sales Contact Calls | Counter |
| Sales Stage Started | Counter |
| SMS Click-throughs | Counter |
| SMS Sent | Counter |
| Social Click-throughs | Counter |
| Social Impressions | Counter |
| Solution Presentation | Counter |
| SQL Disqualified | Counter |
| SQL Qualified | Counter |
| Units (do not expose) | Counter |
| VoC Survey Satisfaction Score | Numeric |
| VoC Surveys Completed | Counter |

Person records
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 16-row-2 17-row-2 18-row-2 19-row-2 20-row-2 21-row-2 22-row-2 23-row-2 24-row-2 25-row-2 26-row-2 27-row-2 28-row-2 29-row-2 30-row-2 31-row-2 32-row-2 33-row-2 34-row-2 35-row-2 36-row-2 37-row-2 38-row-2 39-row-2 40-row-2 41-row-2 42-row-2 |  |
| --- | --- |
| Data view field name | Field type |
| Age | Metric |
| Age Group | Dimension |
| Category 1 Affinity Level | Dimension |
| Category 1 Affinity Score | Metric |
| Category 2 Affinity Level | Dimension |
| Category 2 Affinity Score | Metric |
| Category 3 Affinity Level | Dimension |
| Category 3 Affinity Score | Metric |
| Category 4 Affinity Level | Dimension |
| Category 4 Affinity Score | Metric |
| Category 5 Affinity Level | Dimension |
| Category 5 Affinity Score | Metric |
| Consent Advertising | Dimension |
| Consent All Communications | Dimension |
| Consent Direct Mail | Dimension |
| Consent Email | Dimension |
| Consent Mobile Phone | Dimension |
| Consent Personalization | Dimension |
| Consent Share Data | Dimension |
| Consent SMS | Dimension |
| Email | Dimension |
| First Name | Dimension |
| Gender | Dimension |
| Individual City | Dimension |
| Individual CLTV Level | Dimension |
| Individual CLTV Score | Metric |
| Individual Country | Dimension |
| Individual Phone | Dimension |
| Individual Postal Code | Dimension |
| Individual Propensity to Buy Level | Dimension |
| Individual Propensity to Buy Score | Metric |
| Individual Propensity to Churn Level | Dimension |
| Individual Propensity to Churn Score | Metric |
| Individual Propensity to Upgrade Level | Dimension |
| Individual Propensity to Upgrade Score | Metric |
| Individual State | Dimension |
| Individual Street Address | Dimension |
| Job Title | Dimension |
| Last Name | Dimension |
| Net Promoter Score | Metric |
| Net Promoter Status | Dimension |
| Role Type | Dimension |

Account records
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 16-row-2 17-row-2 18-row-2 19-row-2 20-row-2 21-row-2 22-row-2 23-row-2 24-row-2 25-row-2 |  |
| --- | --- |
| Data view field name | Field type |
| Annual Revenue | Metric |
| Company City | Dimension |
| Company CLTV Level | Dimension |
| Company CLTV Score | Metric |
| Company Country | Dimension |
| Company Name | Dimension |
| Company Phone | Dimension |
| Company Postal Code | Dimension |
| Company Propensity to Buy Level | Dimension |
| Company Propensity to Buy Score | Metric |
| Company Propensity to Churn Level | Dimension |
| Company Propensity to Churn Score | Metric |
| Company Propensity to Upgrade Level | Dimension |
| Company Propensity to Upgrade Score | Metric |
| Company Size | Dimension |
| Company State | Dimension |
| Company Street Address | Dimension |
| Industry | Dimension |
| Number of Employees | Metric |
| Partner Audience - Hardware Shoppers | Dimension |
| Partner Audience - Rapid Growth | Dimension |
| Partner Audience - Services Needed | Dimension |
| Partner Audience - Software Shoppers | Dimension |
| Revenue Range | Dimension |
| Website | Dimension |

SKU records
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| --- | --- |
| Data view field name | Field type |
| Hardware Product Category | Dimension |
| Hardware Product Name | Dimension |
| Service Category | Dimension |
| Service Name | Dimension |
| Software Product Category | Dimension |
| Software Product Name | Dimension |

## Schemas and datasets

The data that supports the solution design reference is structured using the following schemas and datasets.

### Event data

The event dimensions and metrics are supported through a time-series (event) based schema and one or more datasets that contain event data.

### Person data

The person records are supported through a record (profile) based schema and one or more datasets that contain person data. See below for an example of person data (based on the example solution design reference) typically available in such a dataset.

### Account data

The account records are supported through a record (lookup) record based schema and one or more datasets that contain account data. See below for an example of account data (based on the example solution design reference) typically available in such a dataset.

### SKU data

The SKU records are supported through a record (lookup) based schema and one or more datasets that contain SKU data. See below for an example of SKU data (based on the example solution design reference) typically available in such a dataset.

## Connection

Define an account-based connection in Customer Journey Analytics to ingest and join records from the event, account, person and SKU datasets.

- Create a new connection in Customer Journey Analytics.
- Enter a descriptive name and description for the connection.
- Select Account as the Primary ID .
- Select all Optional containers .
- Select your preferred sandbox and estimate the average number of daily events.
- Select Add datasets and add the B2B datasets that contain the data for events, accounts, persons and SKUs.
- Select Next to configure the settings for each of the selected datasets.
- For the event dataset, ensure you select the appropriate fields that correspond to the identities for Account ID , Global Account ID , Opportunity ID , Buying Group ID and Person ID .
- Scroll down to configure the account records dataset. Ensure you select the correct identifier ( Account_ID ) to match the account by the Global Account container. Select the correct identifier ( Account_ID ) as the Global Account field .
- Scroll down to configure the person records dataset. Ensure you select the correct key ( Person_ID ) to match the person by the Person container. Select the appropriate identity ( Profile_Account_ID_Individual ) to match the Global Account field.
- Scroll down to configure the SKU records dataset. Ensure you select the correct key ( Sku ). Select Match by field because no container is configured or available for this data. Select the SKU field in the event dataset( SKU (event datasets) ) as the matching key.
- Select Add datasets to save the datasets and their configured settings.
- Select Save to save the connection.

## Data view

After data is ingested in Customer Journey Analytics, you want to create a data view that includes all the components you have defined in your solution design reference.

### Configure

- Create a new data view in Customer Journey Analytics.
- Select the connection you previously created (for example: B2B Demo Connection (ExL) ).
- Provide a name for the data view. For example: B2B Demo Data view (ExL) and optionally a description.
- Optionally, rename the containers. Or stick with the default container names.
- Select Save and continue .

### Components

By default, all [standard components](/en/docs/analytics-platform/using/cja-dataviews/component-reference) are already included in your data view. These standard components include the B2B specific metrics for Accounts, Buying Groups, Global Accounts, and Opportunities.

- Add all event dimensions that you have defined in the solution design reference , to the dimension components in your data view. For example, the field Event Name , which represents the Event Name dimension. Ensure you configure the dimension component through the available Component settings .
- Add all event metrics that you have defined in the solution design reference to the metrics components in your data view. For example, the field SQL Qualified , which represents the SQL Qualified metric. Ensure you configure the dimension component through the available Component settings .
- Add all account dimensions that you have defined in the solution design reference to the dimension components in your data view. For example, the field Industry , which represents the Industry dimension. Ensure you configure the dimension component through the available Component settings .
- Add all account metrics that you have defined in the solution design reference to the metrics components in your data view. For example, the field Number_of_Employees , which represents the Number_of_Employees metric. Ensure you configure the dimension component through the available Component settings .
- Add all person dimensions that you have defined in the solution design reference to the dimension components in your data view. For example, the field Category_1_Affinity_Level , which represents the Category_1_Affinity_Level dimension. Ensure you configure the dimension component through the available Component settings .
- Add all person metrics that you have defined in the solution design reference to the metrics components in your data view. For example, the field Category_1_Affinity_Score , which represents the Category_1_Affinity_Score metric. Ensure you configure the dimension component through the available Component settings .
- Add all SKU dimensions that you have defined in the solution design reference to the dimension components in your data view. For example, the field Service Category , which represents the Service Category dimension. Ensure you configure the dimension component through the available Component settings .
- Select Save and Continue .

### Settings

- You can optionally define specific settings for the data view: Add segments to the data view. Use a (calculated) metric to define session settings.
- Select Save and continue .

## Segments

You can prepare one or more B2B specific container-based segments that you can use in your Workspace project.

For example:

- Accounts with event registration segment.
- US accounts with Buying Groups and stage 5 opportunities segment.

## Other

You can optionally define other components for your use cases, like [calculated metrics](/en/docs/analytics-platform/using/cja-components/cja-calcmetrics/calc-metr-overview), [date ranges](/en/docs/analytics-platform/using/cja-components/cja-date-ranges/overview), or [alerts](/en/docs/analytics-platform/using/cja-components/alerts/intelligent-alerts).

recommendation-more-help
