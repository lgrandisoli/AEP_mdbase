---
title: "Content decision activity content-decision"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/content-decision"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:07.013055+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Content decision activity content-decision

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

Journey Optimizer allows you to include offers in your journeys through the dedicated **Content decision** activity in the journey canvas. You can then add other activities (such as [custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration)) to your journeys to target your audiences with these personalized offers.

NOTE
The output of a content decision activity cannot be used in native channel activities.
To leverage this capability, create a journey where you add a [content decision activity](#add-content-decision-activity) to define the offers you want to present to the eligible profiles.

You can then use the output of the content decision activity in:

- an Optimize activity with a condition , to move profiles to specific paths based on the offers retrieved;
- a custom action , where you can send those offers to external systems.

## Configure a content decision activity add-content-decision-activity

Using the content decision activity, you can define a decision policy which allows you to pick the best items from Journey Optimizer Decisioning and deliver them to the right audience.

To configure the **Content decision** activity, follow the steps below.

- Unfold the Orchestration category and drop an Content decision activity into your canvas. {width="100%"}
- Optionally, add a label and description to the activity.
- Click Add decision policy . Learn more on decision policies note NOTE Decisioning permissions are needed to author a decision policy. Learn more
- Select the number of items you want to be returned back. For example, if you select 2, the best 2 eligible offers will be presented. Click Next .
- In the Strategy sequence section, select the decision items and/or selection strategies to present with the decision policy. Learn more
- Arrange the evaluation order as needed. When adding several decision items and/or strategies, they are evaluated in sequential order, indicated with numbers at the left of each object or group of objects. To change the default sequence, you can drag and drop the objects and/or the groups to reorder them as wanted. Learn more
- (optional) Add a fallback offer. Learn more
- Review and save your decision policy. {width="70%"}

You are now ready to leverage the output of this content decision activity in your journey.

## Guardrails & limitations guardrails

**Consent policies**

- Updates to consent policies take up to 48 hours to take effect. If a decision policy references an attribute tied to a recently updated consent policy, the changes will not be applied immediately.
- Similarly, if new profile attributes that are subject to a consent policy are added to a decision policy, they will be usable, but the consent policy associated with them will not be enforced until the delay has passed.
- Consent policies are only available to organizations with the Adobe Healthcare Shield or Privacy and Security Shield add-on.

## Use the output of the content decision activity use-content-decision-output

The output of a content decision can be used in multiple journey activities. For example, you can use an [Optimize activity with a condition](#add-condition-activity) to move profiles to specific branches of your journey, based on the number of offers retrieved for them.

You can also add a [custom action](#add-custom-action) to your journey in order to share the offers from the content decision activity to an external system.

### In an optimize activity (condition method) add-condition-activity

To leverage the output of a content decision activity, add an **Optimize** activity, choose the **Condition** method, and define expressions to move profiles to specific paths using data from those offers. Follow the steps below. For more condition types and options, see [Conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions).

- From the Orchestration category, drop an Optimize activity into your canvas. Learn more
- (optional) Rename Path1 , which corresponds to the first expression you define, to a more relevant label.
- For this first path, click inside the Expression field or use the Edit icon to add an expression. {width="80%"}
- In the pop-up window that opens, switch to Advanced mode to use the advanced expression editor . note caution CAUTION The output of a content decision node is only available in the Advanced mode .
- Unfold the Context node and navigate to your decision policy to display all the attributes available in the offers catalog schema . note NOTE Any restricted label defined on an attribute can result in a policy violation for DULE or consent. This applies to journey experience events used in a decision rule and to the offers schema . Learn more about data governance policies in this section .
- To check if any offer has been returned for the profiles who enter the journey, use the listSize function with the following syntax: listSize(@decision{ContentdecisionName.items})>0 note NOTE In this example, Name is the label of the content decision you added to your journey.
- Click Ok .
- Add more paths to define other conditions as needed. You can also create another path for profiles that do not meet the first condition by checking Show path for other cases than the one(s) above .
- Save the condition activity.

### In a custom action add-custom-action

To leverage the output of a content decision activity, you can add a custom action to your journey, in which you will share the offers you defined to an external system. Follow the steps below.

- Add a custom action to your journey. Learn more
- Enter a label for your action.
- In the Request parameters section, select the parameter you would like to map to attributes from the offers that have been retrieved. Click inside the editable text field and select any parameter you would like to map to attributes from the offers that have been retrieved.
- Switch to Advanced mode in the pop-up window that opens. In the advanced expression editor , unfold the Context node to display all the decision policy items. note caution CAUTION The output of a content decision node is only available in the Advanced mode .
- Browse through the offers catalog schema using the items array. For example, use the itemName of the first offer retrieved and the itemName of the second offer retrieved.
- Click Ok to save your expression.
- Save your custom action configuration.

### End-to-end example use-case

Below is the full example of a journey using a content decision activity combined to a condition activity and a custom action - such as described above.

Once the journey is [activated](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey):

- Every time a profile qualifies for that audience, it enters the journey.
- Through the content decision activity, Journey Optimizer retrieves the offers relevant to each profile.
- Only profiles for which at least one offer is retrieved continue the journey (through the ‘Eligible profiles’ path).
- If the condition is met, the corresponding offers are sent to an external system through the custom action.

## Decisioning data in step events decisioning-step-events

When a content decision activity is executed in a journey, decisioning data is made available in the journey step events. This data provides detailed information about the items retrieved and how the decisions were made.

For each content decision activity, the step event includes decisioning data at the top level (such as **exdRequestID** and **propositionEventType**), and an array of **propositions**. Each proposition has an **id**, **scopeDetails** (including decision provider, correlation ID, and decision policy), and an **items** array. Each item contains:

- id : the unique identifier of the item
- name : the name of the item
- score : the score assigned to the item
- itemSelection : data related to how the decision was made and how the item was retrieved, including: selectionDetail : information about the selection strategy used rankingDetail : information about the ranking process (strategy, algorithm, step, traffic type)

**Example of decisioning data in a step event:**

```
"decisioning": {
  "exdRequestID": "8079d2bb-a8b2-4ecf-b9e7-32923dd6ad4e",
  "propositions": [
    {
      "id": "f475cb21-0842-44da-b0eb-70766ba53464",
      "scopeDetails": {
        "decisionProvider": "EXD",
        "correlationID": "6940d1c46208f3c00dae2ab94f3cd31c601461b47bf6d29ff8af0d0806a9c204",
        "decisionPolicy": {
          "id": "b913f724-3747-447b-a51e-8a2f9178f0db"
        }
      },
      "items": [
        {
          "id": "dps:14c7468e7f6271ff8023748a1146d11f05f77b7fc1368081:1bebbf0b7e0f1374",
          "name": "My item name",
          "score": 0.93,
          "itemSelection": {
            "selectionDetail": {
              "strategyID": "dps:selection-strategy:1bebbfc9245cb35e",
              "strategyName": "My selection strategy",
              "selectionType": "selectionStrategy",
              "version": "latest"
            },
            "rankingDetail": {
              "strategyID": "4FyRZTmpjrbzuL7rX7gvmu",
              "algorithmID": "RANDOM",
              "step": "aiModel",
              "trafficType": "random"
            }
          }
        }
      ]
    }
  ],
  "propositionEventType": {
    "decision": 1
  }
}
```

recommendation-more-help
