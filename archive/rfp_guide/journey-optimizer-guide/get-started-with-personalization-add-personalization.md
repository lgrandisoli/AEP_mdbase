---
title: "Get started with personalization add-personalization"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/personalize"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:39.301764+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with personalization add-personalization

Last update: May 8, 2026
- Topics:
- [Personalization](#)

CREATED FOR:

- Beginner
- Developer

Adobe Journey Optimizer personalization capabilities allow you to adapt your messages to each specific recipient by leveraging the data and information you have about them. It can be their first name, interests, where they live, what they bought, and more.

## How personalization works

Using the **personalization editor**, you can select, arrange, customize and validate all the data to create a customized personalization for your content, and leverage various tools such as helper functions or predefined expressions to tailor messages effectively.

Journey Optimizer employs an inline personalization syntax based on Handlebars which allows you to create expressions with contents enclosed by double curly braces **{{}}**.

When processing the message, Journey Optimizer replaces the expression with the data contained in the Experience Platform dataset. For example, Hello {{profile.person.name.firstName}} {{profile.person.name.lastName}} dynamically becomes Hello John Doe. Using this syntax, you can personalize messages across multiple fields, including email subject lines, message bodies, push notifications, or URLs.

## Data used for personalization

Personalization is based on the profile data that are managed by the **XDM Individual Profile** schema defined in Adobe Experience Platform. The **XDM Individual Profile** schema is the only schema you can use to personalize content in Journey Optimizer. Learn more in [Adobe Experience Platform Data Model (XDM) documentation](/en/docs/experience-platform/xdm/home#_blank).

You can also leverage **computed attributes** to personalize your content. Computed attributes allow you to summarize individual behavioral events into computed profile attributes available on Adobe Experience Platform. [Learn how to work with computed attributes](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/computed-attributes)

In addition, Journey Optimizer allows you to leverage data from Adobe Experience Platform in the personalization editor to personalize your content. To do this, datasets needed for lookup personalization must first be enabled through an API call. Once done, you can use their data to personalize your content into Journey Optimizer. This feature is currently available in beta. [Learn more](/en/docs/journey-optimizer/using/content-management/personalization/aep-data-perso)

## Learn and experiment with personalization playground

**Adobe Journey Optimizer** includes an interactive tool designed to help you learn and experiment with personalization capabilities.

This playground provides a simulated environment to write and test personalization code using sample data without requiring live datasets. You can leverage predefined code samples, edit dummy profile payloads, and preview the output of your personalization code in real-time.

➡️ [Access the personalization playground](/en/apps/journey-optimizer/ajo-personalization#_blank)

## AI assistant for personalization expressions ai-personalization-expressions

In the **Personalization Editor** or from the Email Designer toolbar (**Add expression**), **AI Assistant** helps you generate new expressions from natural language, explain what existing code does, and fix issues in a selection, then apply the output when it matches your intent.

➡️ [Learn how to work with AI Assistant for Personalization Expressions](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-personalization-expressions)

## Let’s dive deeper

Now that you have an understanding of personalization in **Journey Optimizer**, it’s time to dive deeper into these documentation sections to start working with the feature.

**Add personalization**

**Personalization syntax**

**Helper functions list**

**Personalization use cases**

## How-to videos video-perso

Learn how to use contextual event information from a journey to personalize a message.

https://video.tv.adobe.com/v/334165?quality=12&learn=on
Learn how to add profile-based personalization to a message and how to use audience membership as a pre-condition to a personalization block.

https://video.tv.adobe.com/v/334078?quality=12&learn=on
Learn how to leverage the personalization editor playground to write and test personalization code using sample data.

https://video.tv.adobe.com/v/3457868?quality=12&learn=on
Explore more video tutorials on personalization features and best practices in [Personalization tutorials](/en/docs/journey-optimizer-learn/tutorials/personalize-content/personalization-editor-overview#_blank)

recommendation-more-help
