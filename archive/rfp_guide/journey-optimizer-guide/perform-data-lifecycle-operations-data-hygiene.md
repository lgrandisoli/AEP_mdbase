---
title: "Perform data lifecycle operations data-hygiene"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/privacy/data-hygiene"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:34.373758+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Perform data lifecycle operations data-hygiene

Last update: May 8, 2026
- Topics:
- [Privacy](#)
- [Monitoring](#)

CREATED FOR:

- Intermediate
- User

AVAILABILITY
Data lifecycle capabilities are currently only available for organizations that have purchased the
Healthcare Shield
and
Privacy and Security Shield
add-on offerings.
As data is continuously ingested into Adobe Experience Platform, it becomes crucial to ensure your data is used as intended, updated when necessary, and deleted per organizational policies.

These tasks can be accomplished using the **Data Lifecycle** menu, which allows you to configure and schedule data lifecycle operations, ensuring that your records are properly maintained.

## Recommendations data-hygiene-recommendations

When performing data hygiene operations (such as deleting identities or datasets), be aware that historical delivery events associated with deleted identities will no longer appear in standard reporting or datalake queries. This can result in discrepancies between the number of emails reported as **Delivered** and the number of emails **Received** in recipient inboxes, especially for older journeys.

Before executing large-scale deletions, validate and export any required delivery or reporting data. If reconciliation is needed after data hygiene, coordinate with Adobe support to access archived logs or use Message Feedback Event Dataset queries for recent data.

## Learn more data-hygiene-learn-more

For more information on the Privacy Service and how to perform data lifecycle operations, refer to Adobe Experience Platform documentation:

- [Privacy Service overview](/en/docs/experience-platform/privacy/home)
- [Data Lifecycle in Adobe Experience Platform](/en/docs/experience-platform/data-lifecycle/home)

recommendation-more-help
