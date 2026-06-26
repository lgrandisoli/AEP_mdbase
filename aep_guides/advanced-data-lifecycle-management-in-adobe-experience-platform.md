---
title: "Advanced Data Lifecycle Management in Adobe Experience Platform"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-lifecycle/home"
category: "overview"
topic: "experience-platform/advanced-data-lifecycle-management-guide"
created_at: "2026-06-26T17:22:16.148723+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Advanced Data Lifecycle Management Guide

# Advanced Data Lifecycle Management in Adobe Experience Platform

Last update: June 18, 2026
- Topics:
- [Data Hygiene](#)

CREATED FOR:

- User
- Developer
- Admin

Adobe Experience Platform provides a robust set of tools to manage large, complicated data operations in order to orchestrate consumer experiences. As data is ingested into the system over time, it becomes increasingly important to manage your data stores so that data is used as expected, is updated when incorrect data needs correcting, and is deleted when organizational policies deem it necessary.

These activities can be performed using the [Data Lifecycle UI workspace](#ui) or the [Data Hygiene API](#api). When a data lifecycle job executes, the system provides transparency updates at each step of process. See the section on [timelines and transparency](#timelines-and-transparency) for more information on how each job type is represented in the system.

NOTE
Advanced Data Lifecycle Management supports dataset deletions through the
dataset expiration endpoint
and ID deletions (row-level data) using primary identities via the
workorder endpoint
. You can also manage
dataset expirations
and
record deletions
through the Experience Platform UI. See the linked documentation for more information. Note that Data Lifecycle does not support batch deletion.
## Data Lifecycle UI workspace ui

The Data Lifecycle workspace in the Experience Platform UI allows you to configure and schedule data lifecycle operations, helping to ensure that your records are being maintained as expected.

For detailed steps on managing data lifecycle tasks in the UI, see the [data lifecycle UI guide](/en/docs/experience-platform/data-lifecycle/ui/overview).

## Data Hygiene API api

The Data Lifecycle UI is built on top of the Data Hygiene API, whose endpoints are available for you to use directly if you prefer to automate your data lifecycle activities. See the [Data Hygiene API guide](/en/docs/experience-platform/data-lifecycle/api/overview) for more information.

## Timelines and transparency timelines-and-transparency

[Record delete](/en/docs/experience-platform/data-lifecycle/ui/record-delete) and dataset expiration requests each have their own processing timelines and provide transparency updates at key points in their respective workflows.

TIP
For additional reference information:
- To monitor your current usage against quota limits, see the [Quota reference guide](/en/docs/experience-platform/data-lifecycle/api/quota).
- For entitlement rules, monthly caps, SLA timelines, and exception handling policies, see the [Record delete quota guide (UI)](/en/docs/experience-platform/data-lifecycle/ui/record-delete#quotas) and [Work order quota guide (API)](/en/docs/experience-platform/data-lifecycle/api/workorder#quotas).

### Dataset expiration timelines dataset-expiration-timelines

The following takes place when a [dataset expiration request](/en/docs/experience-platform/data-lifecycle/ui/dataset-expiration) is created:

Stage
Time after scheduled expiration
Description
Request is submitted
0 hours
A data steward or privacy analyst submits a request for a dataset to expire at a given time. The request is visible in the Data Lifecycle UI after it has been submitted and remains in a pending status until the scheduled expiration time, after which the request will execute.
Dataset is dropped from data lake
1 hour
The dataset is dropped from the
dataset inventory page
in the UI. The data within the data lake is only soft deleted, and will remain so until the end of the process, after which it will be hard deleted.
Dataset is dropped from profile service
3 hours
From this point forward, operations including batch and streaming segmentation, preview or estimation, export, and entity access will no longer read data from this dataset. The data within the profile service is only soft deleted and will remain so until the end of the process, after which it will be hard deleted.
Profile count and audiences updated
48 hours
Once all affected profiles are updated, all related
audiences
are updated to reflect their new size. Depending on the dataset that was removed and the attributes that you are segmenting on, the size of each audience could increase or decrease because of the deletion. At this point any resulting changes in overall profile counts are reflected in
dashboard widgets
and other reports.
Journeys and destinations updated
50 hours
Journeys
,
campaigns
, and
destinations
are updated according to changes in related segments.
Hard deletion complete
15 days
All data related to the dataset is hard deleted from the data lake and profile service. The
status of the data lifecycle job
that deleted the dataset is updated to reflect this.
### Record delete timelines record-delete-transparency

Record delete requests are processed based on entitlement tier, with different SLA commitments for standard and Shield customers. For a full breakdown of processing stages and timelines, see [Data Lifecycle processing timelines](/en/docs/experience-platform/data-lifecycle/data-lifecycle-processing-timelines).

## Next steps next-steps

This document provides an overview of Experience Platform’s Data Lifecycle capabilities. To get started making data hygiene requests in the UI, see the [data lifecycle UI guide](/en/docs/experience-platform/data-lifecycle/ui/overview). To create Data Lifecycle jobs programmatically, see the [Data Hygiene API guide](/en/docs/experience-platform/data-lifecycle/api/overview).

recommendation-more-help
