---
title: "Get started with content optimization message-optimization"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/message-optimization/gs-message-optimization"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:32.219812+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with content optimization message-optimization

Last update: May 8, 2026
- Topics:
- [Experimentation](#)

CREATED FOR:

- Beginner
- User

Content optimization empowers you with the tools to deliver the right message to the right audience at the right time. By combining data-driven insights with powerful personalization capabilities, you can maximize engagement and conversions across your campaigns and journeys.

Content optimization is available in both [campaigns](/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign) and [journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs), enabling you to apply the same optimization strategies across all your customer touchpoints.

➡️ [Learn how to leverage content optimization within a campaign in this video](#video)

## Optimization capabilities capabilities

With content optimization in Journey Optimizer, you can:

- Use targeting to deliver personalized content to specific audience segments based on profile attributes, contextual data, or audience membership.
- Run experiments to test multiple content variations and identify which performs best based on your success metrics.
- Combine both approaches to create sophisticated optimization strategies where you test different variations for each targeted segment.

## Targeting vs experimentation targeting-vs-experimentation

Understanding the difference between targeting and experimentation helps you choose the right optimization approach for your goals.

**Targeting** uses deterministic rules to deliver personalized content to specific segments based on known profile attributes, context, or audience membership. It ensures the right message reaches the right audience.

**Experimentation** uses random assignment to test multiple content variations and discover which performs best. It helps you learn what resonates most with your audience through data-driven testing.

The table below summarizes the key differences:

Capability
Targeting
Experimentation
Assignment method
Deterministic - based on rules
Random - based on traffic allocation
Based on
Profile attributes, context, audiences
Random distribution
Use case
Deliver relevant content to known segments
Discover which content performs best
Example
Show different promotions by location
Test 2 subject lines to see which gets more opens
Best for
Personalization at scale
Optimization & learning
{width="110%" modal="regular"}

## Common use cases use-cases

Here are some typical scenarios where content optimization can help you achieve better results:

Targeting:

- Geo-targeting - Send location-specific offers based on where your customers are located. For example, promote winter coats in colder regions and swimwear in warmer climates.
- Device optimization - Deliver device-specific content, such as desktop-optimized layouts for desktop users and mobile-optimized layouts for smartphone users.

Experimentation:

- A/B testing - Test different email subject lines, call-to-action buttons, or promotional offers to discover which drives the most conversions.
- Lifecycle marketing - Test different onboarding messages for new customers versus retention offers for existing customers.

Combination:

- **Advanced segmentation** - Target customers by loyalty tier and test different reward messaging within each tier to maximize engagement across all segments.

## Get started get-started

To start optimizing your content:

- Create a campaign or journey : Set up your campaign or journey and add at least one action.
- Choose your optimization approach : Use targeting to personalize content for specific segments. Use experimentation to test multiple variations. Combine both for advanced optimization.
- Define your content : Create the different content variations for your optimization strategy.
- Activate and monitor : Launch your optimized campaign or journey and track performance in the reports .

## How it works how-it-works

Once your journey or campaign is live, profiles are evaluated against the criteria you’ve defined. Based on these evaluations, each profile receives the most appropriate content version:

- Profile evaluation - When a profile enters your campaign or journey, Journey Optimizer evaluates their attributes and context.
- Content assignment - Based on your optimization configuration: For targeting , profiles matching specific criteria receive the corresponding personalized content. For experimentation , profiles are randomly assigned to different content variations based on your traffic allocation settings. For combinations , profiles first match a targeting rule, then are randomly assigned to one of the experiment variations for that segment.
- Performance tracking - Journey Optimizer automatically tracks engagement metrics and conversion data to help you identify which content performs best.

## How-to video video

Learn how to leverage content optimization in action or API triggered campaigns. You’ll see how to target sub-audiences, create message variations by location, enable fallback content, and run multiple experiments within a single campaign. This tutorial also covers how to manage multi-channel campaigns while maintaining message consistency.

https://video.tv.adobe.com/v/3470368?quality=12&learn=on
**Related topics**

- [Create a campaign](/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign)
- [Create a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs)
- [Content experiment](/en/docs/journey-optimizer/using/content-management/content-experiment/get-started-experiment)

recommendation-more-help
