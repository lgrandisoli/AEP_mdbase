---
title: "Processing rules, VISTA, and classifications versus Data Prep"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/pr-vista-dataprep"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/cja-aa-comparison"
created_at: "2026-06-23T20:43:33.329322+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Processing rules, VISTA, and classifications versus Data Prep

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- User

Adobe Analytics [processing rules and VISTA rules](/en/docs/analytics/technotes/processing-order) provide a means to transform and manipulate data which is passed into Adobe Analytics [data collection](/en/docs/discontinued/using/reports-and-analytics). These transformations occur as a part of Adobe’s data processing before the data is stored for reporting and analytics purposes in Adobe Analytics.

[Data Prep](/en/docs/experience-platform/data-prep/home) is a tool that lets you apply row-based mappings and transformations to data ingested into [Adobe Experience Platform](/en/docs/experience-platform). Subsequently, the data is made available to Experience Platform applications including Customer Journey Analytics and others. Data prep is integrated with many of the Platform [source connectors](/en/docs/experience-platform/sources/home), as well as with the [Analytics source connector](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics). This connector provides a way to ingest report suite data from Adobe Analytics into Platform.

## Further transformation using Data Prep data-prep

Data which is collected by and stored in Adobe Analytics can be transformed by either processing rules or VISTA rules or both. But report suites that are then forwarded to Platform via the Analytics source connector may be transformed yet another time using Data Prep. This can be desirable for a number of a number of purposes:

- **Resolving schema differences between report suites for use in Customer Journey Analytics and/or RTCDP**. For example, a report suite A defines eVar1 as “Search Term” and report suite B defines eVar2 as “Search Term”. You can use data prep to map the two different eVars into a common field which contains data from both eVars. This makes it possible to [combine report suites with different schemas](/en/docs/analytics-platform/using/cja-usecases/aa-data/combine-report-suites) in a [Customer Journey Analytics connection](/en/docs/analytics-platform/using/cja-connections/overview) or for use in [Real-time Customer Data Platform](/en/docs/platform-learn/tutorials/rtcdp/understanding-the-real-time-customer-data-platform).
- **Mapping eVars fields to semantically meaningful names**. eVars and props coming through the Analytics source connector are mapped to fields such as *_experience.analytics.customDimensions.eVars.eVar1*. Data prep can be used to map eVar and prop fields to new fields that have more meaningful names for your users, or that match names coming from other data sources. (This can also be accomplished via other means, such as renaming the fields in a [Customer Journey Analytics data view](/en/docs/analytics-platform/using/cja-dataviews/create-dataview).)
- **Generally transforming data**. Data prep has hundreds of mapping functions that can be used to compute and calculate new fields based on the data coming through the Analytics source connector. You can split delimited fields into separate fields. You can combine fields. You can manipulate strings. You can extract information from a field, based on regular expressions, and much more.

## Data Prep and classification classifications

Data Prep has crossover with [classifications](/en/docs/analytics/components/classifications/c-classifications) in some situations.

For example, in a delimited field you can use Data Prep to split that field into multiple individual fields without the use of classifications. Generally, classifications are a way to add metadata to a field by uploading a lookup file that is supplied outside the stream of incoming Analytics events.

For example, you can upload a classification file which groups SKUs into ‘size’, ‘brand’, ‘color’, etc. Another difference between classifications and Data Prep is that classifications apply to data *both historically and going forward*. Data Prep mappings, on the other hand, are applied *forward* to data from the time the mapping is created.

recommendation-more-help
