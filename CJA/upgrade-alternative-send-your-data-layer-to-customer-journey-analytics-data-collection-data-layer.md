---
title: "Upgrade alternative: Send your data layer to Customer Journey Analytics data-collection-data-layer"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-data-layer"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:42.408974+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Upgrade alternative: Send your data layer to Customer Journey Analytics data-collection-data-layer

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

You can send your entire data layer to Customer Journey Analytics instead of collecting data with the XDM object. However, this alternative introduces additional complexity over time.

## Advantages and disadvantages

This method is mutually exclusive with [using your AppMeasurement data collection logic with Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/alternative-upgrade-methods/cja-upgrade-alternative-appmeasurement), because both methods accomplish the same task.

Following are the advantages and disadvantages of using this upgrade alternative:

Advantages
Disadvantages
- Provides all the advantages of hosting data in Experience Edge Network : These advantages include: Highly performant reporting and data availability because Adobe Experience Platform is built to power real-time personalization use cases Consolidate implementation for Adobe CX Enterprise data collection between other CX Enterprise products (AJO, RTCDP, and so forth) Not reliant on Adobe Analytics nomenclature (prop, eVar, event, and so forth)
- Uses your current data layer logic : This method uses your current data layer logic in place of a conventional Web SDK implementation. While this approach requires some configuration, it does not require a completely new implementation from scratch and it requires no populating of data elements or tag rules. It allows you to map data from your data layer to XDM, rather than populating an XDM object from scratch.

- Requires mapping to send data to Platform : When your organization is ready to use Customer Journey Analytics, you must send data to a data set in Adobe Experience Platform. Because this option allows you to put your entire client-side data layer into the data object and send it to Adobe, this results in a significant amount of data that Adobe can’t readily interpret. To allow Adobe to interpret the data, you must use datastream mapping to map every individual field to the desired XDM field.
- Rigid implementation : The implementation is constrained to what the data layer provides at the time the hit is sent. This might be acceptible for organizations with basic data needs, but most organizations should avoid this type of rigid implementation in favor of a more flexible implementation that allows for the populating of data elements.
- Future changes are more difficult to implement : Any field you add to your data later in the future must be mapped to XDM in the datastream.

## Basic steps

The basic steps for sending your entire data layer to Customer Journey Analytics are:

- Configure your implementation to send data to Adobe at the desired time, and configure the JSON payload to be your data layer in its entirety.
- Map every data layer element to the desired XDM field. Any data layer elements that are not mapped to an XDM field are permanently dropped, since Adobe does not know where or how to store that data.

recommendation-more-help
