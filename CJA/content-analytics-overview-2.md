---
title: "Content Analytics overview"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/content-analytics/content-analytics"
category: "overview"
topic: "analytics-platform/using/content-analytics/content-analytics"
created_at: "2026-06-23T20:42:18.388665+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Content Analytics overview

Last update: May 13, 2026
- Topics:
- [Content Analytics](#)

CREATED FOR:

- Admin
- User

Content Analytics helps marketers to understand how content impacts the key performance indicators that a business has defined. In addition to the behavioral data, Content Analytics collects data on how content is consumed and how content drives impact. For example, do customers respond better to a specific tone of voice, a specific color palette, or specific themes? This information, together with specifically designed reporting workflows and templates, can help you to perform even better analysis and gain deeper insights on customer journey data in Customer Journey Analytics.

Content Analytics uses an AI and machine learning based **featurization service** to break content down into components and attributes. By creating a structured metadata profile on all your content, you can analyze what content and what attributes of that content drive business results.

In addition to the creation of this structured metadata profile, Content Analytics provides an **identity service** that identifies assets and experiences using a single identifier. The identity service can recognize when the exact same asset appears in more than one place. When that happens, the instances of this asset are treated as the same asset, allowing for a more holistic view of content usage and consumption.

## Value

Content Analytics does provide value at an increasing level:

- Content **usage**: With Content Analytics you get insights on which assets are receiving impressions and where assets are receiving impressions. These insights help you to see whether assets are underused or overused on your web and mobile properties.
- Content **engagements**: Content Analytics can provide engagement insights like the average click through rate for assets with certain attributes. These insights help you to determine whether specific types of experiences are still effective.
- Content journeys: Furthermore, when combined with all other data available in Experience Platform, you can gain additional insights on your content journeys; for example, whether specific content leads to conversions, in addition to engagement. For example, whether specific content leads to conversions, in addition to engagement. And with that knowledge you can determine the ROI on types of content.
- Content **personalization**: Ultimately Content Analytics allows you to act upon your insights and use these insights to determine how to spend money on content. For example, should I send specific types of content to specific audiences? What content provides me with high-personalization opportunities?

## Terminology

Content Analytics uses the following key terms:

- **Experience**: An experience is all text on a web page that is reproducible using the URL that the initial user used to visit the web page. Or the combination of text, assets and click to actions in a mobile app. Each experience gets a unique identifier.
- **Asset**: An asset is an individual and unique piece of content, like an image. Each asset also gets a unique identifier and a perceptual ID. A perceptual ID is an identifier that is shared with assets that are visually identical. Perceptual IDs help to deduplicate assets that may have a different asset URL and therefore a different asset ID, but are perceptually identical.
- **Attribute**: An attribute is a descriptive metadata element associated with an experience or asset. Examples of an attribute are: style of photography, readability, persuasion strategy, object color, background color.

## How it works

Content Analytics uses web and mobile image view data from Experience Platform event datasets to [collect content event data](/en/docs/analytics-platform/using/content-analytics/configuration/datacollection). These content experience events require the data to be collected with the Experience Platform Edge Network (Web SDK, Mobile SDK, Server API). Behavioral data can be collected with the Web SDK, Mobile SDK or the Analytics Source Connector.

- When a user visits a site or app, [configured for Content Analytics](/en/docs/analytics-platform/using/content-analytics/configuration/configuration), the Experience Platform Web or Mobile SDK records impressions and interactions with content.
- The identity and featurization service processes these interactions. That process consists of a retrieval service that revisits the public-facing versions of the configured URLs that define the interactions. For all of these retrieved URLs, the identity service uniquely identifies the experiences and assets. And the featurization service applies AI/ML services to discover experience and asset metadata and attributes.
- The results of these services ([components, attributes, and identities](/en/docs/analytics-platform/using/content-analytics/report/components)) are used to update the relevant specific Content Analytics datasets in Experience Platform.
- You can use the Content Analytics data, together with behavioral data and other lookup data, in a Customer Journey Analytics setup ([Connection](/en/docs/analytics-platform/using/cja-connections/overview), [Data view](/en/docs/analytics-platform/using/cja-dataviews/data-views) and [Workspace](/en/docs/analytics-platform/using/cja-workspace/home)). That setup provides the foundation for the unique macro-level insights on your content.You can quickly begin your Content Analytics reports and analysis using the [Content Analytics template](/en/docs/analytics-platform/using/content-analytics/report/report#template).

NOTE
Content Analytics leverages AI/ML services which may produce inaccurate or misleading results. As a result, please use your judgment to review and validate AI/ML generated outputs.
You can use the
Feedback
tab, available from
on the main interface, to provide feedback on the AI/ML generated outputs.
NOTE
If you have licensed the Privacy and Security Shield add-on, be aware that DULE labeling or Customer Managed Keys do not cover experiences and assets subject to Content Analytics. Also, Content Analytics is not a HIPAA-Ready service.
IMPORTANT
Content Analytics supports featurization in English only.
Related Articles
Content Analytics reporting
Configure Content Analytics
Calculating bounces and bounce rate in Customer Journey Analytics
recommendation-more-help
