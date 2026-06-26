---
title: "Understand Adobe Analytics feature support when upgrading to Customer Journey Analytics feature-support-upgrade"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/additional-information/cja-upgrade-adobe-analytics-features"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-23T20:43:43.721824+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Understand Adobe Analytics feature support when upgrading to Customer Journey Analytics feature-support-upgrade

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)
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
The following list shows only those Adobe Analytics features that require consideration during the upgrade process to Customer Journey Analytics. For a comprehensive list that shows which Adobe Analytics features are fully supported, partially supported, or not supported in Customer Journey Analytics, see [Customer Journey Analytics feature support](/en/docs/analytics-platform/using/compare-aa-cja/cja-aa-comparison/cja-aa).

Consider which of the following Adobe Analytics features you want to continue using when you upgrade to Customer Journey Analytics:

Adobe Analytics feature
Corresponding feature in Customer Journey Analytics
Components and projects from Adobe Analytics
Migrate projects and their associated components to Customer Journey Analytics
.
Activity map overlay and link tracking
Not yet available
Classification data
Lookup datasets are the method for classifying data in Customer Journey Analytics.

[Create a lookup dataset for each dimension containing classification data.](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-datasets/cja-upgrade-dataset-lookup)

Marketing channels
Derived fields are created within a data view.

[Create a marketing channel derived field.](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/cja-upgrade-marketing-channel)

Data Feeds
Experience Platform and Customer Journey Analytics provide a number of functionalities that either independently or combined can solve the various export requirements. These functionalities include [Experience Platform Data Access API](/en/docs/experience-platform/data-access/api), [Experience Platform Destinations](/en/docs/experience-platform/destinations/ui/activate/export-datasets), [Customer Journey Analytics Full Table Export](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud), and [BI tool integration](/en/docs/analytics-platform/using/cja-dataviews/bi-extension).

For more information about export options, see [Data export use cases](/en/docs/analytics-platform/using/cja-usecases/data-export/overview).

Data Warehouse
Customer Journey Analytics Full Table Export
is the evolution of Data Warehouse reports in Adobe Analytics, with many new, often-requested features that are not available in Data Warehouse today.
Streaming Media data
Streaming media data are available using the Analytics source connector as part of the Media Concurrent Viewers panel and the Media Playback Time Spent panel in Workspace.
recommendation-more-help
