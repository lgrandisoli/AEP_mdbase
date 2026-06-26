---
title: "Upgrade alternative: Use AppMeasurement data collection with the Experience Platform Web SDK and Customer Journey Analytics data-collection-appmeasurement"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-appmeasurement"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:42.059759+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Upgrade alternative: Use AppMeasurement data collection with the Experience Platform Web SDK and Customer Journey Analytics data-collection-appmeasurement

Last update: May 12, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Use the information on this page when answering questions in the Customer Journey Analytics Upgrade Guide.
To access the guide from Customer Journey Analytics, select the
Workspace
tab, then select
Upgrade to Customer Journey Analytics
in the left panel. Follow the on-screen instructions.
When upgrading to Customer Journey Analytics, Adobe [recommends a new implementation of the Experience Platform Web SDK](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-recommendations). However, depending on several factors, such as timeline and resource constraints, the recommended upgrade steps might not be practical for your organization.

You can use your AppMeasurement or Analytics extension data collection logic with the Web SDK in order to send data to Platform and Customer Journey Analytics, instead of collecting data with the XDM object. However, this alternative introduces additional complexity over time.

## Advantages and disadvantages

This method is mutually exclusive with [sending your entire data layer to Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-appmeasurement), because both methods accomplish the same task. (This method is preferable to sending your entire data layer to Adobe. It is more refined because props and evars all go through data.__adobe.analytics.*variable-name*.)

Consider the following advantages and disadvantages of using this upgrade alternative:

Advantages
Disadvantages
This is the preferred upgrade path if your Adobe Analytics implementation is already using the Web SDK.

- Provides all the advantages of hosting data in Experience Edge Network : These advantages include: Highly performant reporting and data availability because Adobe Experience Platform is built to power real-time personalization use cases Consolidate implementation for Adobe CX Enterprise data collection between other CX Enterprise products (AJO, RTCDP, and so forth) Not reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth)
- Uses your existing implementation : While this approach requires some implementation changes, it does not require a completely new implementation from scratch. You can use your existing data layer and code with minimal changes to implementation logic without impacting your existing Adobe Analytics reporting.
- Provides an option to use an XDM schema : You can choose to use your existing Adobe Analytics schema or create an XDM schema and map fields in the data object to your XDM schema. XDM schemas are a flexible schema to define any fields you need, and only those fields that are relevant. See “Using your own XDM schema” below for more information about the advantages of using your own XDM schema.
- Retains rules and data elements : While it does require new rule actions, you can reuse your existing data elements and rule conditions with minimal changes.
- Future-proof : If you choose to use your own XDM schema, then future implementation updates are easier.

- Requires mapping to send data to Platform : When your organization is ready to use Customer Journey Analytics, you must send data to a data set in Adobe Experience Platform. This action requires that every field in the data object be an entry in the datastream mapping tool that assigns it to an XDM schema field. Mapping only needs to be done once for this workflow, and it doesn’t involve making implementation changes. However, it is an extra step that is not required when sending data in an XDM object.
- Introduces additional complexity over time : Any field you add in the future must be mapped to XDM in the datastream. Any time a new field is added to your implementation, you can do either of the following: Option 1: Populate a new arbitrary evar or new prop in the data object, then map it to the desired XDM field. This process drives consistency for the client-side implementation, but it requires mapping. Option 2: Leave the data object as a legacy implementation and start populating only the XDM object for all new fields. This process doesn’t require mapping, but it means that some of your variables are located only in a data object, while other variables are located only in an XDM object. Any time you need to troubleshoot your implementation, you need to go to two places. Make sure your internal workflows accommodate for this.

## Basic steps

The basic steps for migrating an Adobe Analytics implementation (either AppMeasurement or the Analytics extension) to use the Web SDK to send data to Customer Journey Analytics are:

- Migrate your Adobe Analytics implementation to use the Adobe Experience Platform Web SDK and begin sending data to Edge Network. This step allows you to migrate your existing Adobe Analytics implementation to use the Web SDK. You can optionally send data to Adobe Analytics to validate that everything is working in Adobe Analytics prior to sending data to Customer Journey Analytics. After this is configured and the data in Adobe Analytics is satisfactory, you can send data from Edge Network to Customer Journey Analytics. This flexibility allows for a more methodical and thoughtful upgrade to Customer Journey Analytics. For information about how to do this, see the following articles in the Adobe Analytics documentation: Migrate to the Web SDK using tags Migrate to the Web SDK using JavaScript
- Begin sending data from Edge Network to Platform. Send all your variables in AppMeasurement format through the data object. For more information, see Data object variable mapping to Adobe Analytics . Choose your schema. You can choose whether to use your existing Adobe Analytics schema, or you can create an XDM schema to better align with the needs of your organization as you begin to use other Platform services. Adobe recommends creating an XDM schema. For more information, see Create a custom schema to use with your Customer Journey Analytics Web SDK implementation . accordion Use the Adobe Analytics schema table 0-row-2 1-row-2 Advantages Disadvantages Advantages of using the Adobe Analytics schema include: Ease of upgrade If you are already sending data to Adobe Analytics with the Adobe Experience Platform Web SDK, you can add an additional service to your datastream to send data to Adobe Experience Platform (which then can be used in your Customer Journey Analytics configuration). Disadvantages of using the Adobe Analytics schema include: While using the Adobe Analytics schema doesn’t limit you in terms of how it can be used with other Platform applications, it does result in a schema that is more complex than it otherwise could be. This is because the Adobe Analytics schema contains many objects that are specific to Adobe Analytics that are unlikely to be used by your organization. When changes to the schema are required, you have to sift through thousands of unused fields to find the field that requires updating. accordion Create an XDM schema table 0-row-2 1-row-2 Advantages Disadvantages Advantages of updating to your own XDM schema include: A streamlined schema that is tailored to the needs of your organization and the specific Platform applications that you use. When changes to the schema are required, you don’t have to sift through thousands of unused fields to find the field that requires updating. Disadvantages of updating to your own XDM schema include: Updating your schema is a time-consuming process that is required before you begin sending data to Platform. Use datastream mapping to map all of the fields in the data object to your XDM schema. For more information, see Mapping in Data Prep for Data Collection in the Experience Platform documentation.

{{upgrade-final-step}}.

recommendation-more-help
