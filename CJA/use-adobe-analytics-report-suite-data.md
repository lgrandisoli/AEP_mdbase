---
title: "Use Adobe Analytics report suite data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/aa-data-in-cja"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/cja-aa-comparison"
created_at: "2026-06-02T19:04:52.551545+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use Adobe Analytics report suite data

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User

Adobe Analytics customers can easily leverage their report suites in Experience Platform and Customer Journey Analytics using the [Analytics source connector](/en/docs/experience-platform/sources/connectors/adobe-applications/analytics). The following discussion explains how to do so.

IMPORTANT
You must have the
Select
package in order to perform data analysis across more than one report suite. Contact your administrator if you’re unsure what Customer Journey Analytics package you have.
## Preparation

As you get ready to start using Adobe Analytics report suites in Adobe Experience Platform and Customer Journey Analytics, there are several things you should consider doing to prepare your data for a seamless move to Customer Journey Analytics. Please review the following page for more information:

- [Adobe Analytics to Customer Journey Analytics evolution](/en/docs/analytics-platform/using/compare-aa-cja/aa-to-cja)

## Set up report suites for ingestion into the Adobe Experience Platform and Customer Journey Analytics

Once you have prepared your data you are ready to start configuring report suites for use in Adobe Experience Platform and Customer Journey Analytics.

- Create a dataflow for each report suite you wish to use in Adobe Experience Platform and Customer Journey Analytics. The Analytics source connector is the tool which allows you to create a connection (a.k.a dataflow) between Adobe Analytics and Adobe Experience Platform. You will use the source connector to create one dataflow for each report suite you want to use in Adobe Experience Platform. The dataflow creates a copy of your report suite data where the schema has been converted to XDM for consumption by Adobe Experience Platform applications including Customer Journey Analytics. Each report suite configured with a dataflow via the source connector is stored as a separate dataset in the Adobe Experience Platform Data Lake. 13 months of historical report suite data will automatically be included with each dataflow, and new data will flow into Adobe Experience Platform on an ongoing basis. (Note that beginning April 26, 2023, the backfill in non-production sandboxes is limited to 3 months.) With the Analytics source connector you don’t need to worry about creating the schema ahead of time. A standardized schema specific to Adobe Analytics is automatically created for you. However, Adobe Experience Platform Data Prep tool can be used to enhance this schema before the data is stored in Data Lake and made available to Customer Journey Analytics. Please note that certain types of data are segmented out by the source connector and will not be present in the dataset in Adobe Experience Platform Data Lake. Other rows may be segmented out between Data Lake and Customer Journey Analytics. See Compare your Adobe Analytics data to Customer Journey Analytics data for more details.
- Use Data Prep to help you combine report suites in Customer Journey Analytics. Data Prep can be used for many types of data transformation, and one common use for Adobe Analytics data is to resolve differences in prop and/or eVar mappings across multiple report suites so that report suites can easily be combined within Customer Journey Analytics. See combine report suites with different schemas for more details.
- Enable Stitching as necessary. When combining multiple datasets in Customer Journey Analytics, the stitching capabilities can help resolve different ID namespaces into a single stitched ID for a single view of the customer across devices and channels. See Stitching overview for more details.
- Create one or more Customer Journey Analytics connections. Once the datasets for your report suites are available in Adobe Experience Platform Data Lake, you can create one or more Customer Journey Analytics connections to bring those datasets into Customer Journey Analytics. Within a connection, report suite data can be combined with other types of data, allowing you to create a true cross-channel view of customer experiences.
- Create one or more Customer Journey Analytics data views. A data view is a container specific to Customer Journey Analytics that lets you determine how to interpret data from a Customer Journey Analytics connection. Data views have many powerful configuration options for customizing the data which is presented to your users within Analysis Workspace .

## Comparing Customer Journey Analytics and Adobe Analytics

Customer Journey Analytics and Adobe Analytics have a number of similarities. For example, both Customer Journey Analytics and Adobe Analytics offer the power of Analysis Workspace for freeform speed-of-thought analysis. However, since Customer Journey Analytics is an application within the Adobe Experience Platform and utilizes Adobe Experience Platform for data ingestion, Customer Journey Analytics and Adobe Analytics differ in a number of important ways. The following articles are helpful for understanding these differences:

- [Compare your Adobe Analytics data to Customer Journey Analytics data](/en/docs/analytics-platform/using/troubleshooting/compare)
- [Customer Journey Analytics feature support](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/cja-aa)
- [Compare terminology for Analytics data passed through the Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/terminology)
- [Compare data processing across Adobe Analytics and Customer Journey Analytics reporting features](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/data-processing-comparisons)
- [Virtual report suites, Data views, Adobe Experience Platform sandboxes and the Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/vrs-dataview-sandbox-adc)
- [Processing rules, VISTA and classifications versus Data Prep](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/pr-vista-dataprep)
- [AAID, ECID, AACUSTOMID and the Analytics source connector](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/aaid-ecid-adc)

recommendation-more-help
