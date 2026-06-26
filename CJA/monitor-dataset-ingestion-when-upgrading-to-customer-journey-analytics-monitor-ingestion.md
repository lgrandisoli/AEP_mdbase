---
title: "Monitor dataset ingestion when upgrading to Customer Journey Analytics monitor-ingestion"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-datasets/cja-upgrade-dataset-ingestion"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:46.775101+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Monitor dataset ingestion when upgrading to Customer Journey Analytics monitor-ingestion

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

After you configure your Web SDK or API implementation, you need to check the statuses of individual batches to verify that data is being ingested into the dataset.

- In the Experience Platform UI, select Monitoring in the left-navigation. The Monitoring dashboard displays. This dashboard lets you view the statuses of inbound data from either batch or streaming ingestion. insert screenshot
- Select Batch end-to-end to view a list of batches. If no batches are displayed, check your implementation to ensure that it is correctly sending data to Adobe. insert screenshot
- Select the batch ID for a given dataset, then validate that Success is shown in the Status field. If Failed is shown in the Status field, check your implementation to ensure that it is correctly sending data to Adobe. Repeat this step to verify the status of each batch.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
