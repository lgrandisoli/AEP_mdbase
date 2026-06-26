---
title: "Create a custom schema for the Analytics source connector create-custom-schema"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/historical-data-source-connector/cja-upgrade-source-connector-schema"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:55.358461+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create a custom schema for the Analytics source connector create-custom-schema

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

- Create a custom schema for the Analytics source connector, as described below.
- If you don’t already have an Analytics source connector, create the Analytics source connector and map fields to your custom schema . Or If you already have an Analytics source connector, map fields from the source connector to your XDM schema .
- Add the Analytics source connector dataset to the connection

## Create a custom schema for the Analytics source connector

You should have already [created a new custom schema](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create) for your Experience Platform Web SDK implementation to use with Customer Journey Analytics. This schema should contain any field groups for fields that you plan to collect data on.

You now need to use those same field groups from your Web SDK schema and add them to a new schema that you can use with the Analytics source connector.

This schema for the Analytics source connector needs to contain:

- All field groups (including any custom field groups that you created) that are included in your custom schema that you created for your Web SDK implementation. (Any custom fields that aren’t part of a default field group should have been added to your Web SDK schema as part of a custom field group.)
- The Adobe Analytics ExperienceEvent Template field group

To create the custom schema to use with the Analytics source connector:

- In Adobe Experience Platform, begin creating a new custom schema as described in Create a custom schema to use with your Customer Journey Analytics Web SDK implementation .
- Add all field groups (including any custom field groups) that are included in the schema that you created for your Web SDK implementation.
- After you finish adding these field groups, add the Adobe Analytics ExperienceEvent field group: In the Field groups section, select Add to add an additional field group.
- Search for and select the Adobe Analytics ExperienceEvent Template field group.
- Select Add field groups .
- Select Save to save your schema.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
