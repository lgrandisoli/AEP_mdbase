---
title: "Add the Analytics source connector dataset to the connection upgrade-source-connector-dataset"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/historical-data-source-connector/cja-upgrade-source-connector-dataset"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:51.588456+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Add the Analytics source connector dataset to the connection upgrade-source-connector-dataset

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

## Understand how the Analytics source connector can bring historical data into Customer Journey Analytics

You can use the Analytics source connector to bring Adobe Analytics report suite data into Adobe Experience Platform. This data can then be used as historical data in Customer Journey Analytics.

This process assumes that you want to [create an XDM schema when upgrading to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create), because you want a streamlined schema that is tailored to the needs of your organization and the specific Platform applications that you use.

To use the Analytics source connector to bring historical data into Customer Journey Analytics, you need to:

- Create an XDM schema for the Analytics source connector
- If you don’t already have an Analytics source connector, create the Analytics source connector and map fields to your XDM schema . Or If you already have an Analytics source connector, map fields from the source connector to your XDM schema .
- Add the Analytics source connector dataset to the connection, as described below.

## Add the Analytics source connector dataset to the connection

After you [create an Analytics source connector for historical data](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/historical-data-source-connector/cja-upgrade-source-connector), a dataset is automatically created for the Analytics data.

You need to add this automatically created dataset to the same connection that you created for your Web SDK implementation. Doing so brings the Analytics data into the same data view in Customer Journey Analytics as your Web SDK data.

To add the automatically created dataset to the same connection that you created for your Web SDK implementation:

- In Customer Journey Analytics, select Connections , optionally from Data management , in the top menu.
- Select the connection that you created for your Web SDK implementation .
- Select Edit .
- Select Add datasets in the upper-right.
- Scroll to or search for the dataset that was automatically created when you created the Analytics source connector. The name of this dataset is the name of your report suite, followed by midValues . For example: My report suite midValues
- Select the checkbox next to the dataset name, then select Next .
- Specify the following information: Copied from help/connections/create-connection.md. Should we single source? table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 layout-auto Setting Description Person ID Only available for event and profile datasets. Select a Person ID from the drop-down menu of available identities. These identities were defined in the dataset schema in the Experience Platform. See below for information on how to use Identity Map as a Person ID. If there are no Person IDs to choose from, that means one or more Person IDs have not been defined in the schema. See Define identity fields in the UI for more information. The value for the selected Person ID is considered to be case sensitive. For example, abc123 and ABC123 are two different values. Timestamp For event and summary datasets only, this setting is automatically set to the default timestamp field from event-based schemas in Experience Platform. Timezone Only available for summary data. Select the appropriate timezone for the time-series summary data. Data source type Select a type of data source. Types of data sources include: Web data Mobile App data POS data CRM data Survey data Call Center data Product data Accounts data Transaction data Customer Feedback data Other This field is used to survey the types of data sources in use.
- In the Import new data section, leave the Import all new data option disabled. Because you are using the Analytics source connector dataset for historical data, you don’t want to bring over future data that is collected into this dataset.
- In the Dataset backfill section, select Request backfill .
- Define the period that you want the connection backfill into Customer Journey Analytics to include by entering the start and end dates or by selecting the the calendar icon . Be explicit when specifying the dates you request for backfill. Depending on several factors, you might want to do any of the following: Choose an end date that is the same date as when you first started gathering data with your Web SDK implementation. Choose an end date that is shortly after the date when you first started gathering data with your Web SDK implementation, then use data view segments to segment out the overlapping data. Choose an end date that results in a greater overlap in data, then use data view segments to segment out the overlapping data. Note: This option would result in increased costs because there would be more rows in the connection. Include any of the following? Make sure you're explicit as to the dates you request backfill to. You want to request it to the date that you start gathering data with your Web SDK implementation. Also possibly include segments for any overlapping date. So you could request everything and then use a segment to exclude data that you don't want. That way if you need to move up the date, then you could change the date in the segment. Downside would be that you might pay for double rows. When they do that, they're going to see all schema fields from both their custom schema and their Analytics schema. So they'll need to be cognizant to select the right fields, and never select any Analytics fields, because they will be mapped as part of the source connector. Never select any Analytics field group fields because they'll be mapped.
- Select Queue backfill .
- Select Add datasets , then select Save to save the connection.
- (Conditional) If you are using lookup datasets, you must create the lookup dataset and add it to your connection. For more information, see Create lookup datasets to classify data in Customer Journey Analytics . This is required only if you did not already do it when configuring your Web SDK implementation.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
