---
title: "Choose your schema for Customer Journey Analytics choose-schema"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-existing"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:57.334066+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Choose your schema for Customer Journey Analytics choose-schema

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Administration](#)

CREATED FOR:

- Admin

NOTE
Use the information on this page when answering questions in the Customer Journey Analytics Upgrade Guide.
To access the guide from Customer Journey Analytics, select the
Workspace
tab, then select
Upgrade to Customer Journey Analytics
in the left panel. Follow the on-screen instructions.
When upgrading to Customer Journey Analytics, Adobe recommends creating a custom Experience Data Model (XDM) schema to better align with the needs of your organization as you begin to use other Platform services. Alternatively, you can choose to use your existing Adobe Analytics schema.

Consider the advantages and disadvantage of each.

## Create a custom schema tailored to your organization (Recommended)

Adobe recommends creating a custom schema when upgrading to Customer Journey Analytics.

Advantages
Disadvantages
- Advantages of updating to your own custom schema include: A streamlined schema that is tailored to the needs of your organization and the specific Platform applications that you use. When changes to the schema are required, you don’t have to sift through thousands of unused fields to find the field that requires updating.

Disadvantages of updating to your own custom schema include:

- Updating your schema is a time-consuming process that is required before you begin sending data to Platform.

## Use your existing Adobe Analytics schema

The option to use your existing Adobe Analytics schema with Customer Journey Analytics is available only if your Adobe Analytics implementation is configured with the Adobe Experience Platform Web SDK. correct? Or can you do this with an AppMeasurement implementation?

Advantages
Disadvantages
Advantages of using the Adobe Analytics schema include:

- Ease of upgrade If you are already sending data to Adobe Analytics with the Adobe Experience Platform Web SDK, you can add an additional service to your datastream to send data to Adobe Experience Platform (which then can be used in your Customer Journey Analytics configuration).

Disadvantages of using the Adobe Analytics schema include:

- While using the Adobe Analytics schema doesn’t limit you in terms of how it can be used with other Platform applications, it does result in a schema that is more complex than it otherwise could be. This is because the Adobe Analytics schema contains many objects that are specific to Adobe Analytics that are unlikely to be used by your organization. When changes to the schema are required, you have to sift through thousands of unused fields to find the field that requires updating.

recommendation-more-help
