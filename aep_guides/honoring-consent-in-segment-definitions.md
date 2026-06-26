---
title: "Honoring consent in segment definitions"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/tutorials/consents"
category: "tutorials"
topic: "experience-platform/segmentation-service-guide"
created_at: "2026-06-26T17:26:55.551037+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Segmentation Service Guide

# Honoring consent in segment definitions

Last update: June 18, 2026
- Topics:
- [Segments](#)

CREATED FOR:

- User

NOTE
This guide explains how to honor consents within
segment definitions
.
Legal privacy regulations such as the California Consumer Privacy Act (CCPA) provide consumers the right to opt out of having their personal data collected or shared with third parties. Adobe Experience Platform provides standard Experience Data Model (XDM) components that are intended to capture these customer consent preferences in Real-Time Customer Profile data.

If a customer has withdrawn or withheld consent for having their personal data shared, it is important that your organization honors that preference when generating audiences for marketing activities. This document describes how to integrate customer consent values in your segment definitions using the Experience Platform user interface.

## Getting started

Honoring customer consent values requires an understanding of the various Adobe Experience Platform services involved. Before starting this tutorial, ensure that you are familiar with the following services:

- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, customer profile in real time based on aggregated data from multiple sources.
- [Adobe Experience Platform Segmentation Service](/en/docs/experience-platform/segmentation/home): Allows you to build audiences from Real-Time Customer Profile data.

## Consent schema fields

In order to honor customer consents and preferences, one of the schemas that is a part of your XDM Individual Profile union schema must contain the standard field group **Consents and Preferences**.

For details on the structure and intended use case of each of the attributes provided by the field group, see the [consents and preferences reference guide](/en/docs/experience-platform/xdm/field-groups/profile/consents). For step-by-step instructions on how to add a field group to a schema, refer to the [XDM UI guide](/en/docs/experience-platform/xdm/ui/resources/schemas#add-field-groups).

Once the field group has been added to a [Profile-enabled schema](/en/docs/experience-platform/xdm/ui/resources/schemas#profile) and its fields have been used to ingest consent data from your experience application, you can use the collected consent attributes in your segment rules.

## Handling consent in segmentation

In order to ensure that opted-out profiles are not included in segment definitions, special fields must be added to existing segment definitions and included when creating any new segment definitions.

The steps below demonstrate how to add the appropriate fields for two types of opt-out flags:

- Data Collection
- Share Data

NOTE
While this guide focuses on the two opt-out flags above, you can configure your segment definitions to incorporate additional consent signals as well. The
consents and preferences reference guide
provides more information on each of these options and their intended use cases.
When building a segment definition in the UI, under **Attributes**, navigate to **XDM Individual Profile**, then select **Consents and Preferences**, followed by **Id Specific**. From here, you can see the options for **Data Collection** and **Share Data**.

Start by selecting the **Data Collection** category, then drag **Choice Value** into the segment builder. When adding the attribute to the segment definition, you can specify the [consent values](/en/docs/experience-platform/xdm/field-groups/profile/consents#choice-values) that must be included or excluded.

One approach is to exclude any customers who have opted out of having their data collected. To do this, set the operator to **does not equal**, and choose the following values:

- **No (opt-out)**
- **Default of No (opt-out)**
- **Unknown** (if consent is assumed to be withheld if otherwise unknown)

Under **Attributes** in the left rail, navigate back to the **Consents and Preferences** section, then select **Share Data**. Drag its corresponding **Choice Value** into the canvas, and select the same values as those for the Data Collection choice value. Ensure that an **Or** relationship is established between the two attributes.

With both the **Data Collection** and **Share Data** consent values added to the segment definition, any customers that have opted out of having their data used will be excluded from the resulting audience. From here, you can continue customizing the segment definition before selecting **Save** to finish the process.

## Next steps

By following this tutorial, you should now have a better understanding of how to honor customer consents and preferences when building segment definitions in Experience Platform.

For more information on managing consent in Experience Platform, refer to the following documentation:

- [Consent processing using the Adobe standard](/en/docs/experience-platform/landing/governance-privacy-security/consent/adobe/overview)
- [Consent processing using the IAB TCF 2.0 standard](/en/docs/experience-platform/landing/governance-privacy-security/consent/iab/overview)

recommendation-more-help
