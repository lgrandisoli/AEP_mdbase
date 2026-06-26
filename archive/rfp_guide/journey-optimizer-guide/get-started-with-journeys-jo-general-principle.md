---
title: "Get started with journeys jo-general-principle"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:42.275952+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with journeys jo-general-principle

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Get Started](#)
- [Overview](#)

CREATED FOR:

- Beginner
- Intermediate
- User

Adobe Journey Optimizer empowers you to create personalized, multistep customer journeys that adapt in real-time to your audience’s behavior and needs. Using an intuitive drag-and-drop canvas, you can orchestrate messages and actions across multiple channels, leveraging contextual data and audience targeting for maximum impact.

This guide provides a clear roadmap to help you understand journey fundamentals, choose the right journey type for your use case, and confidently design journeys that deliver meaningful, timely customer experiences.

## What are journeys?

**Journeys** are automated, multistep customer experiences that orchestrate personalized interactions across channels in response to customer behavior, business events, or scheduled campaigns.

Use Journey Optimizer to:

- Build **real-time orchestration** use cases using contextual data stored in events or data sources
- Design **multistep advanced scenarios** that respond dynamically to customer behavior and business events
- Deliver **1:1 personalized experiences** at scale across email, push, SMS, in-app, web, and more

➡️ **Ready to start building?** [Create your first journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs) in 5 minutes.

### Journeys vs campaigns: when to use each journeys-vs-campaigns-intro

Adobe Journey Optimizer offers three approaches to reach customers: **Journeys** (1:1 real-time orchestration), **Campaigns** (simple batch or API-triggered delivery), and **Orchestrated campaigns** (batch canvas workflows with multi-entity data).

**Quick decision:**

- Use **Journeys** for multi-step, behavior-driven experiences where each customer progresses at their own pace
- Use **Action and API-triggered campaigns** for simple, scheduled or triggered message delivery to audiences
- Use **Orchestrated campaigns** for complex batch workflows requiring multi-entity segmentation and exact pre-send counts

## Choose your journey type journey-types

Adobe Journey Optimizer supports four journey types, each designed for different entry mechanisms and business scenarios:

- **Unitary journeys**: Real-time, event-triggered experiences (order confirmations, welcome emails)
- **Read Audience journeys**: Scheduled batch communications to audience segments (newsletters, promotional campaigns)
- **Audience Qualification journeys**: Real-time responses to audience membership changes (VIP upgrades, re-engagement)
- **Business event journeys**: Business conditions affecting multiple customers (inventory alerts, flash sales)

## Build with the journey designer journey-designer

The **journey designer** is your visual canvas for creating customer experiences. With an intuitive drag-and-drop interface, you can orchestrate every step of your journey without writing code.

### What you can do in the designer:

**Define entry points**

Choose how customers enter: through an event, audience segment, or audience qualification.

[Learn about entry management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management)

**Send messages**

Use built-in channel actions for email, push, SMS/MMS, in-app, web, and more—all designed in Journey Optimizer.

[Send messages in journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action)

**Add logic & conditions**

Branch your journey based on profile attributes, audience membership, or real-time events.

[Use conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions)

**Leverage data**

Use contextual data from events, Adobe Experience Platform, or third-party API services.

[Work with data sources](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources)

**Connect external systems**

Create custom actions to integrate third-party systems for sending messages or triggering workflows.

[Configure custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration)

**Add orchestration activities**

Use wait times, jumps, profile updates, and audience management to create sophisticated flows.

[Explore all activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/about-journey-activities)

➡️ **Hands-on learning:** [Watch the journey designer video](#video) or [explore end-to-end use cases](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/jo-use-cases)

## Your journey creation workflow workflow

Building successful journeys follows a clear, repeatable process. Here’s your step-by-step workflow:

**1. Plan** → **2. Design** → **3. Test** → **4. Publish** → **5. Monitor** → **6. Optimize**

### 1. Plan your journey plan

Before opening the designer, clarify your objectives:

- **What’s the goal?** (e.g., onboard new customers, re-engage inactive users)
- **Who’s the audience?** (specific segment, event-driven individuals)
- **Which journey type fits?** (See [journey types](#journey-types) above)
- **What channels will you use?** (email, push, SMS, etc.)

### 2. Design in the canvas design

Use the journey designer to build your flow:

- **Set entry conditions** - Define how profiles enter (event, audience, qualification)
- **Add orchestration logic** - Include wait times, conditions, and decision points
- **Configure messages** - Design your communications or leverage existing templates
- **Set up actions** - Configure built-in or custom actions to execute
- **Define exit criteria** - Specify when and how profiles complete the journey

[Learn to use the journey designer →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer)

### 3. Test before going live test

Always test your journey to catch issues before customers experience them:

- Use **test mode** to simulate the journey with test profiles
- Use **dry run** to preview journey execution without affecting real data or sending messages
- Verify all conditions, messages, and actions work as expected
- Check timing, data flows, and personalization

[Test your journey →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) | [Learn about dry run →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run)

### 4. Publish your journey publish

Once testing is complete, publish to make your journey live:

- Review final settings and properties
- Publish to activate for real customers
- Note: Live journeys can be stopped but not edited (you must create a new version)

[Publish your journey →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey)

### 5. Monitor performance monitor

Track how your journey performs in the real world:

- View journey reports and analytics
- Monitor entry, completion, and error rates
- Set up alerts for critical issues

[Monitor and report →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/report-journey) | [Set up alerts →](/en/docs/journey-optimizer/using/monitor/monitor-alerts-errors/alerts)

### 6. Optimize and iterate optimize

Use insights to improve:

- Analyze engagement metrics and conversion rates
- Test send-time optimization
- Create new journey versions with improvements
- Use AI-powered recommendations

[Optimize your journeys →](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize) | [Send-time optimization →](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/send-time-optimization)

➡️ **Ready to start?** [Create your first journey now →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs)

## Real-world use cases use-cases

Learn from practical examples that demonstrate how to apply journey concepts to solve common marketing challenges:

**Welcome new subscribers**

When a customer subscribes to your service, trigger a welcome journey that encourages them to complete onboarding steps.

[View use case →](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/message-to-subscribers-uc)

**Send-time optimization**

Use AI to deliver emails when each customer is most likely to engage, maximizing open and click rates.

[View use case →](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/send-time-optimization)

**Ramp up deliveries**

Gradually increase message volume to warm up your sending reputation and avoid deliverability issues.

[View use case →](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/ramp-up-deliveries-uc)

**Target by weekday**

Send different content based on the day of the week customers enter your journey for better relevance.

[View use case →](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/weekday-email-uc)

**Multi-channel campaigns**

Orchestrate seamless experiences across email, push, SMS, and web channels in a single journey.

[View use case →](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/journeys-uc)

**All use cases**

Explore the complete library of journey use cases with step-by-step implementations.

[Browse all →](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/jo-use-cases) | [Use case library →](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/journey-use-cases-landing-page)

## Explore journey capabilities capabilities

As you get more comfortable with journey building, explore these powerful capabilities to create sophisticated customer experiences:

**Advanced Expressions**

Build dynamic conditions and personalization using the expression editor for data manipulation and complex logic.

[Learn about expressions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/building-advanced-conditions-journeys-landing-page)

**Time zone management**

Handle global audiences with automatic time zone adjustments and optimal send times.

[Manage time zones](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management)

**Test mode & dry run**

Validate journeys with test profiles before going live, and preview execution without affecting real data.

[Use dry run](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run)

**Copy to sandbox**

Duplicate journeys across sandboxes to streamline testing and deployment workflows.

[Copy journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/copy-to-sandbox)

**Tags & organization**

Use tags to categorize and filter journeys for better management at scale.

[Organize with tags](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/tags)

**Throughput control**

Limit message throughput to manage sending reputation and avoid overwhelming systems.

[Control throughput](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/limit-throughput)

[View all journey capabilities →](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/manage-journey-landing-page)

## Learn by watching video

Get a visual introduction to journey components and learn the basics of building journeys in the canvas:

https://video.tv.adobe.com/v/3424996?quality=12&learn=on
➡️ **Want more videos?** [Explore journey video tutorials](/en/docs/journey-optimizer-learn/tutorials/journeys/journey-designer-overview#_blank)

## Common questions common-questions

What is the difference between a journey and a campaign?
Adobe Journey Optimizer offers three approaches:

- Journeys : 1:1 real-time orchestration where each profile travels through steps at their own pace. Best for behavior-driven, multi-step experiences with conditional logic (e.g., onboarding, cart abandonment).
- Campaigns (Action & API-triggered) : Simple message delivery to audiences, executing simultaneously to all profiles either on schedule or via API trigger. Best for promotional campaigns, newsletters, transactional messages.
- Orchestrated campaigns : Multi-step batch workflows with complex segmentation using relational data (profiles + products/stores/bookings). All profiles processed together with exact pre-send counts. Best for seasonal promotions, product launches, campaigns requiring multi-entity data.

**Key difference**: Journeys maintain individual customer state for real-time actions; Action and API-triggered campaigns deliver simple messages in batch; Orchestrated campaigns provide batch workflow canvas with multi-entity segmentation capabilities.

[Learn about Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/gs-orchestrated-campaigns)

Can I edit a live journey?
You can edit limited elements (name, message content), but structural changes require creating a new version.
Learn about journey versions
➡️ **More questions?** [View complete Journey FAQ](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-faq) with 40+ detailed answers

## Need help? help

Use these links to find guidance, troubleshooting, and resources.

### Quick links for common tasks

- **Create your first journey** - Step-by-step guide for beginners
- **Journey FAQ** - Common questions answered
- **Troubleshooting** - Diagnose and fix issues
- **Error codes reference** - Understand error messages
- **Guardrails & limitations** - Technical boundaries and best practices

### Get notified about issues

Set up **journey alerts** to receive real-time notifications when journeys encounter errors or unusual patterns.

### Additional resources

- **Journey management hub** - Tools for filtering, optimization, and profile management
- **Journey activities reference** - Complete guide to all activity types
- **Troubleshooting execution issues** - Debug journey execution problems
- **Troubleshooting inbound activities** - Fix entry and qualification issues

**Ready to build your first journey?** [Get started now →](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs)

recommendation-more-help
