---
title: "Content Analytics JavaScript library"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/content-analytics/configuration/tags-agnostic"
category: "other"
topic: "analytics-platform/using/content-analytics/configuration"
created_at: "2026-06-02T19:07:37.341969+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Content Analytics JavaScript library

Last update: May 13, 2026
- Topics:
- [Content Analytics](#)

CREATED FOR:

- Admin

The Adobe Content Analytics JavaScript library enables tracking of content-related events on websites by sending content data to Adobe Experience Platform via the Experience Platform Edge Network. Use this library when you want to implement Content Analytics without Adobe Experience Platform Tags.

NOTE
This article applies to Content Analytics for the web channel.
PREREQUISITES
- Adobe Experience Platform Web SDK (Alloy) must be initialized on the page before calling initializeContentLibrary.
- Complete the Content Analytics guided configuration wizard to guide you through all steps required to set up the prerequisites for a configuration of Content Analytics.
- After the guided configuration is finished, the JavaScript settings are available to use.

## Installation

You can install the library in two ways:

### npm package

Use npm to install the library.

- On the command line, use: code language-bash npm install @adobe/content-analytics
- Import the library: code language-javascript import initializeContentLibrary from "@adobe/content-analytics";

### Script tag (CDN)

Load the library directly from the CDN.

- Initialze the Web SDK JavaScript library and load the Content Analytics bundle: code language-html <!-- 1. Load and configure Alloy first --> <script src="https://cdn1.adoberesources.net/alloy/2.x.x/alloy.min.js"></script> <script> alloy("configure", { datastreamId: "YOUR_DATASTREAM_ID", orgId: "YOUR_ORG_ID@AdobeOrg", }); </script> <!-- 2. Load Content Analytics --> <script src="https://cdn1.adoberesources.net/content-analytics/1.x.x/content-analytics.min.js"></script> <script> window.contentAnalytics({ datastreamId: "YOUR_DATASTREAM_ID", }); </script> where alloy/2.x.x refers to the version you want to use of the Web SDK JavaScript library . content-analytics/1.x.x refers to the version you want to use of the Content Analytics SDK library.
- The standalone build exposes window.contentAnalytics as the initialization function.

## Datastream configuration

The datastreamId option is required and must reference a datastream that has the Experience Platform service configured with an enabled Content Analytics experience event dataset. Ensure the sandbox associated with the datastream is not already associated with another Content Analytics setup.

You can supply separate datastream IDs per environment:

```
initializeContentLibrary({
  datastreamId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",          // production
  stagingDatastreamId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",   // optional
  developmentDatastreamId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // optional
});
```

## Experience capture and definition

Enable experience tracking and control how experiences are identified on your website. Experiences are defined by combining a **domain regular expression** with optional **query parameters** that distinguish one experience from another within matching pages.

Option
Type
Default
Description
includeExperiences
boolean
false
Enable page/experience view tracking
experienceConfigurations
array
-
Define experiences by domain regex and query parameters
Each entry in experienceConfigurations accepts:

Property
Type
Description
regEx
string
Domain regular expression matched against the page URL (e.g.
^(?!.*\b(store|help|admin)\b)
)
queryParameters
array
Query parameter names whose values distinguish experiences on matching pages (e.g.
["outdoors", "patio", "kitchen"]
)
### Example

See below for an example of how to enable experience tracking with domain regex and query parameters.

```
initializeContentLibrary({
  datastreamId: "YOUR_DATASTREAM_ID",
  includeExperiences: true,
  experienceConfigurations: [
    {
      regEx: "^https://www\\.example\\.com/products",
      queryParameters: ["category", "collection"],
    },
    {
      regEx: "^https://www\\.example\\.com/blog",
      queryParameters: [],
    },
  ],
});
```

## Event filtering

Control which page URLs and asset URLs are included in data collection using regular expressions. Use the pattern examples below as a starting point and validate the patterns with a regex tester before deployment.

Option
Type
Default
Description
pageUrlQualifier
string (regex)
-
Only track pages whose URL matches this pattern
assetUrlQualifier
string (regex)
-
Only track assets whose URL matches this pattern
excludeURLsFromTracking
array
[]
List of URL strings to exclude from tracking
### Example

See below for an example of how to exclude documentation pages from Content Analytics and to consider only product images for Content Analytics.

```
initializeContentLibrary({
  datastreamId: "YOUR_DATASTREAM_ID",
  pageUrlQualifier: "^(?!.*\\/documentation).*",
  assetUrlQualifier: ".*\\/products\\/.*\\.(?:jpg|png|webp)",
  excludeURLsFromTracking: [
    "https://www.example.com/internal",
    "https://www.example.com/staging",
  ],
});
```

recommendation-more-help
