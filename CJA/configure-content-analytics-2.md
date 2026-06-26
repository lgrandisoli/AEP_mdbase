---
title: "Configure Content Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/content-analytics/configuration/configuration"
category: "other"
topic: "analytics-platform/using/content-analytics/configuration"
created_at: "2026-06-23T20:43:57.700351+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure Content Analytics

Last update: May 13, 2026
- Topics:
- [Content Analytics](#)

CREATED FOR:

- Admin

This article documents, on a high level, how to configure Content Analytics.

Before you configure Content Analytics, you must ensure the [prerequisites](#prerequisites) are met, you do have the required [access control](#access-control), and you are aware of the [limitations](#limitations).

The steps to configure Content Analytics are:

{modal="regular"}

- Use the Content Analytics guided configuration wizard to guide you through all steps required to set up the prerequisites for a configuration of Content Analytics. You can save your configurations at any time and return later.
- Once you are comfortable with the configuration values, you can implement the configuration. This implementation creates all the required artifacts, based on what you have configured in the wizard.
- Only when you manually publish the Tags property is your Content Analytics configuration effectively deployed and data collection started.
- You can only make some minor changes to an implemented configuration using the guided configuration wizard. For example, change the data view .
- You can make other changes to an implemented configuration using the Adobe Content Analytics extension in the associated Tags property for web or mobile .
- Configuration modifications are effectively deployed and data collection starts only when you manually re-publish the Tags property.

## Prerequisites

Before you configure Content Analytics, ensure that the following prerequisites are met:

### Web

- You have allow-listed the User Agent and IP address for the featurization service that is used in Content Analytics. The User Agent string to configure is: AdobeFeaturization/1.0 .
- If you have implemented the Web SDK using JavaScript for regular behavioral data collection, ensure you are using the default name alloy for the JavaScript library.
- You have a Customer Journey Analytics Product Administrator role, with the additional permissions to manage connections and to manage data views.
- If you decide to collect Content Analytics experiences, ensure you set up and update Content Analytics versioning based on changes to your web pages.
- You must have permissions for data collection : Experience Platform permissions. Experience Platform Data Collection permissions.
- You have carefully considered the following important configuration options: Your site is suited for experience reporting. Proper experience reporting is only possible when the following conditions are met: The pages on the site must be reproducible using the page URL. The text content seen by any given user can be reproduced using the page URL and does not depend on cookies or other personalization mechanisms. You have a clear understanding of which pages you want to capture for content engagement analysis and insights. You have a clear understanding for which (type of) assets you want to capture content engagement analysis and insights.

### Mobile

- Ensure the Experience Platform Edge Network and Experience Platform Identity for Edge Network extensions are enabled for the mobile app.
- You have a Customer Journey Analytics Product Administrator role, with the additional permissions to manage connections and to manage data views.
- You must have permissions for data collection : Experience Platform permissions. Experience Platform Data Collection permissions.

## Access control

IMPORTANT
There is no Content Analytics permission that you can configure to enable or disable Content Analytics access for individual users or groups of users.
To provide a user or group of users access to Content Analytics, you must provide the user or group of users access to one or more [data views that are configured for Content Analytics](/en/docs/analytics-platform/using/content-analytics/configuration/guided#data-view).

This access implies:

- The Content Analytics enabled data view is included as part of the Data View permissions for a specific Customer Journey Analytics product profile.
- That specific Customer Journey Analytics product profile is one of the product profiles assigned to the user or group of users.

## Limitations

The schema used for Content Analytics event data is system-owned. A system-owned schema cannot be modified, which implies:

- You cannot include field groups for the support of functionalities like geolocation, bot detection, or device lookup.
- You cannot add a specific identifier to support [field-based stitching](/en/docs/analytics-platform/using/stitching/fbs).

Related Articles
- [Guided configuration](/en/docs/analytics-platform/using/content-analytics/configuration/guided)
- [Manual configuration](/en/docs/analytics-platform/using/content-analytics/configuration/manual)
- [Access control](/en/docs/analytics-platform/using/technotes/access-control)

recommendation-more-help
