---
title: "Create the Analytics source connector and map fields create-source-connector"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/historical-data-source-connector/cja-upgrade-source-connector"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:54.311864+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create the Analytics source connector and map fields create-source-connector

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Administration](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

## Understand how the Analytics source connector can bring historical data into Customer Journey Analytics

You can use the Analytics source connector to bring Adobe Analytics report suite data into Adobe Experience Platform. This data can then be used as historical data in Customer Journey Analytics.

This process assumes that you want to [create a custom schema to use with your Customer Journey Analytics Web SDK implementation](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create), because you want a streamlined schema that is tailored to the needs of your organization and the specific Platform applications that you use.

To use the Analytics source connector to bring historical data into Customer Journey Analytics, you need to:

- Create a custom schema for the Analytics source connector
- If you don’t already have an Analytics source connector, create the Analytics source connector and map fields to your custom Web SDK schema, as described below. Or If you already have an Analytics source connector, map fields from the source connector to your custom Web SDK schema .
- Add the Analytics source connector dataset to the connection

## Create the Analytics source connector and map fields

With your custom schema created, you need to create the Adobe Analytics source connector to use for historical data. (For more comprehensive, general guidelines on creating a source connector, see [Create an Adobe Analytics source connection in the UI](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics).)

To create an Adobe Analytics source connector to use for historical data:

- In the Platform UI, In the Connections section in the left rail, select Sources .
- Select Adobe applications from the list of CATEGORIES.
- Select Add data in the Adobe Analytics tile.
- Select Report suite , then from the list of report suites, select the report suite that contains the historical data that you want to use in Customer Journey Analytics.
- Select Next in the upper-right corner of the screen.
- Select Custom schema , then select the schema that you created in Create a custom schema that includes the Adobe Analytics field group . add screenshot
- Map each Adobe Analytics dimension to a custom schema dimension. In the Map standard fields section, select the Custom tab. Select Add new mapping . In the Source field , select an Adobe Analytics field from the Adobe Analytics ExperienceEvent Template field group. Then, in the Target field , select the custom field in the XDM schema that you want to map it to. Not all Adobe Analytics fields have a corresponding field in XDM due to the inherent architecture differences between AppMeasurement and XDM. Repeat this process for each field in the Adobe Analytics ExperienceEvent Template field group that you are using to collect data in Adobe Analytics.
- Select Next in the upper-right corner of the screen.
- Name the data flow and (optionally) provide a description.
- Select Next in the upper-right corner of the screen.
- Review the connection, then select Finish . After the connection is created, the dataflow is automatically created to populate a dataset with the Adobe Analytics data from your report suite. The dataflow ingests up to 13 months of historical data for production sandboxes. The backfill in non-production sandboxes is limited to three months. If you are using the Analytics source connector to bring historical data into your Customer Journey Analytics Web SDK implementation, then you need to add this automatically created dataset to the connection that you created for your Web SDK implementation.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
