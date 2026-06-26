---
title: "Content Analytics manual configuration"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/content-analytics/configuration/manual"
category: "other"
topic: "analytics-platform/using/content-analytics/configuration"
created_at: "2026-06-02T19:08:43.727554+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Content Analytics manual configuration

Last update: May 13, 2026
- Topics:
- [Content Analytics](#)

CREATED FOR:

- Admin

This article details the manual actions that are required to start or stop the data collection of a Content Analytics configuration, or to edit your Content Analytics implementation.

The following manual configuration actions are available:

## Start data collection

To start the data collection for an implemented Content Analytics configuration:

- Follow the publishing flow . Successfully publish the library for the Tags properties that contains your Content Analytics configuration.
- Based on the channels you have configured: For web : Install the embedded code in the <head> element of the pages on your development, staging or publishing environment, subject to Content Analytics. For mobile : Consult the solution specific Adobe Content Analytics extension guide in the Experience Platform Mobile SDK documentation on how to configure and instrument your mobile application for Content Analytics.

## Stop data collection

To stop the data collection for an implemented Content Analytics configuration, based on the channels you have configured:

- For web : Remove the embedded code in the <head> element of the pages on your development, staging or production environment, subject to Content Analytics. Delete the associated web Tags property for your Content Analytics configuration.
- For mobile : Remove the Content Analytics extension from your app. Delete the associated mobile Tags property for your Content Analytics configuration.

Follow the [publishing flow](/en/docs/experience-platform/tags/publish/overview#_blank) to apply the changes.

## Modify data collection

You can make some minor changes to an implemented configuration using the [guided configuration wizard](/en/docs/analytics-platform/using/content-analytics/configuration/guided). For example, change the data view, or enable or disable experiences.

### Web

You use the [Adobe Content Analytics web extension](/en/docs/experience-platform/tags/extensions/client/content-analytics/overview) in the Tags property associated with your Content Analytics configuration to make changes to the following artifacts:

- Sandbox and datastream . note caution CAUTION Verify that the sandbox and datastream you configure in the Adobe Content Analytics extension are already configured for Content Analytics using the guided configuration at an earlier stage. This configuration ensures that all required artifacts are available. Also verify that updates for sandbox or datastreams do not interfere with another Content Analytics configuration that is configured to use the same sandbox or datastreams.
- Experience capture and definition You can enable or disable experiences and edit the combinations of regular expression and query parameters to determine how content is rendered on your website.
- Event segmenting You can edit regular expressions to modify how you segment pages and assets.

After you make changes in the Adobe Content Analytics web extension, use the [publishing flow](/en/docs/experience-platform/tags/publish/overview#_blank) to start collecting data.

### Mobile

You use the [Adobe Content Analytics mobile extension](https://developer.adobe.com/client-sdks/solution/adobe-content-analytics/) in the Tags property associated with your Content Analytics configuration to make additional changes.

After you make changes in the Adobe Content Analytics web extension, use the [publishing flow](/en/docs/experience-platform/tags/publish/overview#_blank) to start collecting data.

## Versioning

NOTE
This section only applies to Content Analytics for the web channel.
If you want to collect Content Analytics experiences, you should consider implementing versioning to ensure new experiences (changes to your web page) are properly collected.

To implement versioning, you add a global adobe.getContentExperienceVersion function on the pages that you consider experiences that you want to analyze.

The adobe.getContentExperienceVersion function should return a string as value, which can be anything you choose, to identify the version. The version is appended to the [Experience ID URL](/en/docs/analytics-platform/using/content-analytics/report/components#experience-metadata).

If the function is not present or no value is returned from the function, the value NoVersion is used as a default.

### Example

```
window.adobe = window.adobe || {};
window.adobe.getContentExperienceVersion = () => {
  return "1.0";
};
```

Related Articles
Guided configuration
Data collection Tags publishing overview
recommendation-more-help
