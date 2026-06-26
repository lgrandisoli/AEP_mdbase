---
title: "Use AI models to rank journeys journey-ai-models"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/journey-arbitration/journey-ai-models"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:37.931304+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

[Limited Availability]{class="badge informative"}

# Use AI models to rank journeys journey-ai-models

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Decisioning](#)

CREATED FOR:

- Intermediate
- User

AVAILABILITY
This feature is currently in Limited Availability. Contact your Adobe representative to gain access.
Adobe Journey Optimizer helps you control which journeys a profile can enter when they qualify for more than the system allows. To do so, you can use [rule sets](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets) to define caps on journey entry or concurrency. When a profile is eligible for more journeys than the cap allows, the priority assigned to each journey determines which journeys are selected.

Instead of using priority, you can also use **AI models** in your ranking formulas to dynamically rank journeys based on trained model scores.

## Create an AI model create-ai-model

To create an AI model for journey ranking, follow the steps below.

- Create a dataset where conversion events will be collected. Learn how
- Access the Orchestration ranking section, then select the AI models tab. The list of previously created AI models is displayed.
- Click Create AI model .
- Specify a unique name and, if needed, a description for the AI model. {width="85%"} note NOTE The ranking object is the entity that the ranking formula will apply to. By default, the ranking object is set to Journey .

- In the Optimization metric section, all metrics from your default Customer Journey Analytics data view display in the list. Select the metric that you want to optimize your model on. {width="70%"} Journey Optimizer ranks based on the conversion rate (Conversion rate = Total number of conversion events / Total number of impression events). The conversion rate is calculated using: Impression events (items that are displayed) Conversion events (items that result in clicks or conversions) These events are automatically captured using the Web SDK or the Mobile SDK. Learn more in the Adobe Experience Platform Web SDK overview.
- Select the dataset(s) where the conversion and impression events are collected. Learn how to create such datasets in this section . {width="85%"} note caution CAUTION Only the datasets created from schemas associated with the Experience Event - Proposition Interactions field group are displayed in the drop-down list. You can select up to 5 datasets.
- If you are creating a **Personalized optimization** AI model, Select the segment(s) to use to train the AI model. note NOTE You can select up to 50 audiences.
- Save and activate the AI model.

The AI model is now available for selection when you create a ranking formula.

## Reference the AI model in a formula to rank journeys reference-ai-model

You can now set the AI model as a reference to build a ranking formula, then assign the formula to a rule set and apply the rule set to your journeys. To do so, follow the steps below.

- Create a ranking formula. Learn how
- Use the Select AI model button to select the AI model you want to use in the formula. {width="80%"}
- In at least one of the Criterion sections, define a condition and select AI model score as the ranking method. For example, if the journey has a “Promo” tag, the ranking score is the AI model score. {width="60%"}
- Click Create to complete your ranking formula.
- Now create a rule set and select the formula that you created as the ranking method. Learn how
- Create the journey capping rules and save the rule set.
- Apply the rule set to the desired journeys and save them. Learn how note NOTE Only one rule set can be applied to a journey at a time.

All journeys that use this rule set will be ranked with the formula referencing the selected AI model when the cap is applied.

recommendation-more-help
