---
title: "Real-Time Customer Profile API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/profile/api/overview"
category: "reference"
topic: "experience-platform/real-time-customer-profile-guide"
created_at: "2026-06-26T17:26:56.579415+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Real-Time Customer Profile Guide

# Real-Time Customer Profile API guide

Last update: May 23, 2026
- Topics:
- [Profiles](#)

CREATED FOR:

- Developer

Real-Time Customer Profile enables you to see a holistic view of each of your individual customers within Adobe Experience Platform. Profile allows you to consolidate disparate customer data from multiple channels, such as online, offline, CRM, and third party data, into a unified view offering an actionable, timestamped account of every customer interaction.

The Real-Time Customer Profile API includes multiple endpoints, outlined below. Please visit the individual endpoint guides for details and refer to the [getting started guide](/en/docs/experience-platform/profile/api/getting-started) for important information on required headers, reading sample API calls, and more.

To view all available endpoints and CRUD operations, visit the [Real-Time Customer Profile API Reference swagger](https://www.adobe.com/go/profile-apis-en).

For a guide to working with Real-Time Customer Profile data in the Experience Platform UI, please refer to the [Profile user guide](/en/docs/experience-platform/profile/ui/user-guide).

## Computed attributes computed-attributes

Computed attributes are functions used to aggregate event-level data into profile-level attributes. These functions are automatically computed so that they can be used across segmentation, activation, and personalization.

Each computed attribute contains an expression, or “rule”, that evaluates incoming data and stores the resulting value in a profile attribute. These computations help you to easily answer questions related to things like lifetime purchase value, time between purchases, or number of application opens, without requiring you to manually perform complex calculations each time the information is needed. These computed attribute values can then be viewed in a profile, used to create an audience, or accessed through a number of different access patterns.

You can create, view, edit, and delete computed attributes using the ca/attributes/ endpoint. To learn how to use computed attributes, refer to the [computed attributes overview](/en/docs/experience-platform/profile/computed-attributes/overview). For API operations, visit the [computed attributes API endpoint guide](/en/docs/experience-platform/profile/computed-attributes/api).

## Entities (Profile access) entities

NOTE
You can only use these endpoints if you have Real-Time CDP Ultimate.
Through Adobe Experience Platform you can access Real-Time Customer Profile data using RESTful APIs or the user interface. To learn how to access entities, more commonly known as “profiles”, using the API, follow the steps outlined in the [entities endpoint guide](/en/docs/experience-platform/profile/api/entities). To access profiles using the Experience Platform UI, refer to the [Profile user guide](/en/docs/experience-platform/profile/ui/user-guide).

## Export jobs (Profile export) profile-export

Real-Time Customer Profile data can be exported to a dataset for further processing, such as exporting audiences for activation or profile attributes for reporting. Export jobs for audiences are part of the Adobe Experience Platform Segmentation Service API, please read the [segmentation export jobs endpoint guide](/en/docs/experience-platform/profile/api/export-jobs) to learn more. For step-by-step instructions on how to create and manage export jobs for profile attributes, please visit the [export jobs endpoint guide](/en/docs/experience-platform/profile/api/export-jobs).

## Merge policies merge-policies

When bringing data from multiple sources together in Experience Platform, merge policies are the rules that Experience Platform uses to determine how data will be prioritized and what data will be combined to create individual customer profiles. Using the Real-Time Customer Profile API, you can create new merge policies, manage existing policies, and set a default merge policy for your organization. To work with merge policies using the API, visit the [merge policies endpoint guide](/en/docs/experience-platform/profile/merge-policies/merge-policies).

To learn more about merge policies, and their role within Experience Platform, please begin by reading the [merge policies overview](/en/docs/experience-platform/profile/merge-policies/overview).

## Preview sample status (Profile preview) profile-preview

As data is ingested into Experience Platform, a sample job is run to update the profile count and other Real-Time Customer Profile data-related metrics. The results of this sample job can be viewed using the /previewsamplestatus endpoint, part of the Real-Time Customer Profile API. This endpoint can also be used to list profile distributions by both dataset and identity namespace, as well as to generate multiple reports in order to gain visibility into the composition of your organization’s Profile store. To get started using the /profilepreviewstatus endpoint, refer to the [preview sample status endpoint guide](/en/docs/experience-platform/profile/api/preview-sample-status).

## Profile system jobs profile-system-jobs

Profile-enabled data that is ingested into Experience Platform is stored in the Data Lake as well as the Real-Time Customer Profile data store. Occasionally it may be necessary to delete profile data associated with a dataset from the Profile store in order to remove data that is no longer needed or was added in error. This requires using the API to create a Profile System Job, also known as a “delete request”, which can be modified, monitored, or deleted if required. To learn how to work with delete requests using the /system/jobs endpoint in the Real-Time Customer Profile API, follow the steps outlined in the [profile system jobs endpoint guide](/en/docs/experience-platform/profile/api/profile-system-jobs).

## Update profiles attributes update-profile

Occasionally it may be necessary to update data in your organization’s Profile store. For example, you may need to correct records or change an attribute value. This can be done through batch ingestion and requires a Profile-enabled dataset configured with an upsert tag. For more information on how to configure a dataset for attribute updates, please refer to the tutorial for [enabling a dataset for Profile and upsert](/en/docs/experience-platform/catalog/datasets/enable-upsert).

## Next steps next-steps

To begin making calls using the Real-Time Customer Profile API, read the [getting started guide](/en/docs/experience-platform/profile/api/getting-started) then select one of the endpoint guides to learn how to use specific Profile-related endpoints. To work with Profile data using the Experience Platform UI, please refer to the [Real-Time Customer Profile user guide](/en/docs/experience-platform/profile/ui/user-guide).

recommendation-more-help
