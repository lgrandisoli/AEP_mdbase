---
title: "Build segment definitions build-segments"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/creating-a-segment-definition"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:21.392119+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Build segment definitions build-segments

Last update: May 8, 2026
- Topics:
- [Audiences](#)
- [Profiles](#)

CREATED FOR:

- Beginner
- User

## Create a segment definition create

In this example, you build an audience to target all customers living in Atlanta, San Francisco, or Seattle and born after 1980. All these customers must have made a purchase within the last 7 days.

➡️ [Learn how to create audiences in this video](#video-segment)

- From the Audiences menu, click the Create audience button and select Build rule . The segment definition screen allows you to configure all the required fields to define your audience. Learn how to configure audiences in the Segmentation Service documentation .
- In the Audience properties pane, provide a name and a description (optional) for the audience.
- Drag and drop the desired fields from the left pane into the center workspace, then configure them according to your needs. The basic building blocks of segment definitions are attributes and events . In addition, the attributes and events contained in existing audiences can be used as components for new definitions. Learn more in the Segmentation service documentation note NOTE Note that the fields available in the left pane vary depending on how the XDM Individual Profile and XDM ExperienceEvent schemas have been configured for your organization. Learn more in the Experience Data Model (XDM) documentation . In this example, we need to rely on Attributes and Events fields to build the audience: Attributes : profiles living in Atlanta, San Francisco or Seattle born after 1980. note NOTE The frequencyMap attribute is not supported for use in segment definitions and cannot be used as part of audience segmentation criteria. For frequency based targeting consider using frequency capping rules under business rules. Events : profiles who made a purchase within the last 7 days.
- As you are adding and configuring new fields in the workspace, the Audience Properties pane is automatically updated with information on the estimated profiles belonging to the audience.
- Once the audience is ready, click Save . It displays in the list of Adobe Experience Platform audiences. Note that a search bar is available to help you search a specific audience in the list.

The audience is now ready for use in your journeys. For more information, refer to [this section](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences).

## Audience evaluation methods evaluation-method-in-journey-optimizer

In Adobe Journey Optimizer, audiences are generated from segment definitions using one of three evaluation methods below.

Streaming segmentation
The profiles list for the audience is kept up-to-date in real-time as new data flows into the system.

Streaming segmentation is an ongoing data selection process that updates your audiences in response to user activity. Once a segment definition has been built and the resulting audience has been saved, the segment definition is applied against incoming data to Journey Optimizer. This means that individuals are added or removed from the audience as their profile data changes, ensuring that your target audience is always relevant. [Learn more in Adobe Experience Platform documentation](/en/docs/experience-platform/segmentation/ui/streaming-segmentation#_blank).

| note important |
| --- |
| IMPORTANT |
| As of November 1st, 2024, streaming segmentation no longer supports the use of **send** and **open** events from Journey Optimizer tracking and feedback datasets. |
| This change applies to all customer sandboxes and organizations. Only send and open events are affected: Clicks and other tracking events remain available for streaming segmentation. This change applies only to streaming segmentation. Send and open events can still be used in batch segments, but if included in a streaming segment, they are evaluated in a batch manner. Additionally, exclusion events and bounce/delay events resulting from send events are also impacted by this change. Tracking data collection is not affected. Send and open events will continue to be collected as usual. Reaction events in journeys are unaffected by this change. |

Batch segmentation
The profiles list for the audience is evaluated every 24 hours.

Batch segmentation processes all profile data at once through segment definitions, creating a snapshot of the audience that can be saved and exported for use. Unlike streaming segmentation, batch segmentation does not continuously update the audience list in real-time. New data that comes in after the batch process is not reflected in the audience until the next batch process. Attempts to force an immediate update do not override the daily cycle. For immediate incremental updates, consider using streaming or on-demand segmentation options.

For more details, refer to the [Adobe Experience Platform Segmentation Service documentation](/en/docs/experience-platform/segmentation/home#batch#_blank)

Edge segmentation
Edge segmentation is the ability to evaluate segments in Adobe Experience Platform instantaneously
on the edge
, enabling same-page and next-page personalization use cases. Currently only select query types can be evaluated with edge segmentation. For more details, refer to the
Adobe Experience Platform Segmentation Service documentation
If you know the evaluation method you want to use, select it using the drop-down list. You can also click the browse icon folder icon with a magnifying glass to see a list of the available segment definition evaluation methods. For more details, refer to the [Adobe Experience Platform Segmentation Service documentation](/en/docs/experience-platform/segmentation/ui/segment-builder#segment-properties#_blank).

After you have first defined an audience, profiles are added to the audience when they qualify. Backfilling the audience from prior data can take up to 24 hours. After the audience has been backfilled, the audience is continuously kept up-to-date and is always ready for targeting.

## Flexible audience evaluation flexible

Adobe Experience Platform Audience Portal allows you to run a segmentation job on demand for selected audiences, ensuring that you always have the most up-to-date audience data before targeting them in Journey Optimizer journeys and campaigns.

With flexible audience evaluation, you can:

- Create a fresh new segment based on your latest data.
- Evaluate the audience in real time to ensure accuracy. To do so, choose the audiences you want to have evaluated and select “Evaluate audiences”, provided they meet specific criteria (e.g., people-based, Segmentation Service origin).
- Use the evaluated audience in Adobe Journey Optimizer campaigns or journeys for precise targeting.

You can evaluate up to 20 audiences at a time, and ineligible audiences are automatically excluded. For more details, see the [Adobe Experience Platform Segmentation Service documentation](/en/docs/experience-platform/segmentation/ui/audience-portal#flexible-audience-evaluation).

## How-to video video-segment

Understand how Journey Optimizer uses rules to generate audiences, and learn how to use attributes, events, and existing audiences to create an audience.

https://video.tv.adobe.com/v/3425020?quality=12&learn=on
recommendation-more-help
