---
title: "Work with computed attributes computed-attributes"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/computed-attributes"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:02.633781+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with computed attributes computed-attributes

Last update: May 8, 2026
- Topics:
- [Audiences](#)
- [Profiles](#)

CREATED FOR:

- Intermediate
- User

Computed attributes summarize individual behavioral events into computed profile attributes available on Adobe Experience Platform. These attributes are based on Profile-enabled Experience Event datasets ingested into Adobe Experience Platform and serve as aggregated data points stored within customer profiles.

Each computed attribute is a profile attribute that you can leverage for segmentation, personalization, and activation in journeys and campaigns. This simplification enhances the ability to deliver timely and meaningful personalized experiences to your customers.

NOTE
To access computed attributes, ensure you have the appropriate permissions (
View Computed attributes
and
Manage Computed attributes
).
## Create computed attributes manage

To create computed attributes, browse to the **Computed attributes** tab in the **Profiles** menu located on the left hand-side.

From this screen, you can construct computed attributes by building rules that combine event attributes, aggregate functions, alongside a specified lookback period. For example, you can calculate the sum of purchases made in the last three months, identify the most recent item viewed by a profile who hasn’t made a purchase in the last week, or tally up the total reward points accumulated by each profile.

Once your rule is ready, publish the computed attribute to make it available in other downstream services, including Journey Optimizer.

Detailed information on creating and managing computed attributes is available in the [Computed attributes documentation](/en/docs/experience-platform/profile/computed-attributes/overview)

## Add computed attributes to the Adobe Experience Platform data source source

To leverage computed attributes in Journey Optimizer, add them to the Journey Optimizer **Experience Platform** data source.

The Adobe Experience Platform data source defines the connection to Adobe Real-time Customer Profile. This data source retrieves Profile data and Experience Events data from the Real-time Customer Profile Service.

To add computed attributes to the data source, follow these steps:

- Browse to the Configurations left menu, then click the Data sources card.
- Select the Experience Platform data source.
- Add the SystemComputedAttributes field group containing all the created computed attributes.

Computed attributes are now available for use in Journey Optimizer. [Learn how to use computed attributes in Journey Optimizer](#use)

Detailed information on adding field groups to the Adobe Experience Platform data source is available in [this section](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/adobe-experience-platform-data-source).

## Use computed attributes in Journey Optimizer use

NOTE
Before starting, ensure you have added your computed attributes to the Adobe Experience Platform data source.
Learn how in this section
.
Computed attributes provide versatile capabilities within Journey Optimizer. Use them for various purposes, such as personalizing message content, creating new audiences, or splitting journeys based on a specific computed attribute. For example, split a journey’s path based on a profile’s total purchases in the last three weeks by adding a single computed attribute in a Condition activity. You can also personalize an email by displaying the most recently viewed item for each profile.

Since computed attributes are profile attribute fields created on your profile union schema, access them from the personalization editor within the **SystemComputedAttributes** field group. From there, add computed attributes into your expressions, treating them like any other profile attribute to perform the desired operations.

recommendation-more-help
