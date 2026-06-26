---
title: "Target reporting"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/integrations/at"
category: "other"
topic: "analytics-platform/using/integrations/at"
created_at: "2026-06-02T19:07:06.061841+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Target reporting

Last update: May 13, 2026
- Topics:
- [Experience Platform Integration](#)

CREATED FOR:

- User

Target Reporting in Customer Journey Analytics enables you to measure and report on Adobe Target activities directly in Customer Journey Analytics. This functionality is comparable to what is being performed in Adobe Analytics (AA) via Analytics for Target (A4T), but with the connectivity to Adobe Experience Platform (AEP).

By adding the Target Classification lookup dataset (that is available by default in Experience Platform) into a Customer Journey Analytics Connection, users now have proper exposure to Target reporting tools, Target order attribution, and other features. With only some minor preparation and adjustments made within the Customer Journey Analytics data view, these activities can be made immediately available for any user who wishes to send Target data directly into CJA.

## Primary benefits

- Marketers can dynamically apply Customer Journey Analytics success metrics to Target activity reports at any time. It is not required to specify everything before running the activity.
- Marketers can take advantage of Customer Journey Analytics features, such as the Experimentation Panel, to analyze their website personalization further.
- Marketers can have a single source of reporting for Adobe Journey Optimizer and Target. Both personalization products can be connected to Customer Journey Analytics for a more holistic view of your web personalization.

## Notes and Considerations

Your Target activity must [use Customer Journey Analytics as the reporting source](/en/docs/target/using/integrate/cja/target-reporting-in-cja).

Once the Target Classification Event Dataset has been added to a connection, there are a few minor adjustments to be made within the data view once these components have been added as dimensions, including:

- Setting persistence to be similar to how it is tracked in Target (check with a Target consultant or the customer to ensure proper settings).
- Setting persistence to ALL, which allows for multiple Target activities to be tracked simultaneously and not overwritten by future or previous activities.

## More detailed information

See [Target reporting in Adobe Customer Journey Analytics](/en/docs/target/using/integrate/cja/target-reporting-in-cja) in the Target documentation for more information.

See the [Experimentation panel](/en/docs/analytics-platform/using/cja-workspace/panels/experimentation) for more information on how analysts can compare different user experience, marketing, or messaging variations to determine which is best at driving a specific outcome. You can evaluate the lift and confidence of any A/B experiment from any experimentation platform - online, offline, from Adobe solutions like Target or Journey Optimizer, and even BYO (bring-your-own) data.

recommendation-more-help
