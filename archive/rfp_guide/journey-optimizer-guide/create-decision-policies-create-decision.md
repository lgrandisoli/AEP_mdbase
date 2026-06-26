---
title: "Create decision policies create-decision"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/create-decision-policy"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:41.507845+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create decision policies create-decision

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Decisioning](#)

CREATED FOR:

- Experienced
- User

To present the best dynamic offer and experience to your customers, add a decision policy to your content in a campaign or journey then configure the items to return and the selection strategy to use. To do so, follow the steps below:

- [Add a decision policy](#add)
- [Configure the decision policy](#configure) - Add a name and specify the number of items to return for the email channel.
- [Set up a strategy sequence](#strategy) - Select the items to return with the decision policy.
- [Select fallback offers](#fallback) (optional) - Select items to display if no items or selection strategies are qualified.
- [Review and save](#review) the selection strategy
- [Assign a placement](#placement) (Email channel only)

AVAILABILITY
Decision policies are available for the
Code-based Experience
,
Push notification
,
SMS
, and
Email
channels.
## Add a decision policy add

Open a journey or campaign, select a [channel action](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action) and edit the content of your message.

Edit the content of your message and browse the tabs below for more information on how to add the decision policy based on the selected channel.

Code-based Experience
For code-based experiences, you can add a new decision policy using either the **code editor**, or the **Decisioning** menu available in the properties pane.

| accordion |
| --- |
| Add a decision policy from the code editor |
| Open the code editor editor using the Edit code button. Navigate to the Decision policy menu then click the Add decision policy button. |

| accordion |
| --- |
| Add a decison policy from the Decisioning menu |
| Click the icon from the properties pane to access the Decisioning menu. Click the Add decision policy button. |

Email
- Toggle the Enable decisioning option. note important IMPORTANT Enabling decisioning clears existing email content. If you have already designed your email, be sure to save your content as a template beforehand.
- Add a new decision policy, using either the personalization editor or the Decisioning menu available in the Email designer. accordion Add a decision policy from the Personalization editor Open the personalization editor using the icon available in the subject line field or in any field in the email body where you can add personalization. Navigate to the Decision policies menu then click the Add decision policy button. accordion Add a decison policy from the Decisioning menu Open the Email Designer and select any component in the email structure. Click the icon from the properties pane to access the Decisioning menu. Click the Add new policy button. note NOTE The Reuse decision output option lets you reuse a decision policy that has already been created in this email. It is particularly helpful when you want to show the same offer in multiple locations (for example, header and footer). When the same offer can be selected by more than one decision policy in the email body, the engine deduplicates offers: each placement receives a different offer, so the same offer will not appear in both places. To display the same offer in multiple placements, use Reuse decision output to reuse the output of an existing decision policy in this email.

You can also add decision policies when using the **Code your own** mode in the Email Designer. To do so, navigate to **Decision policies** to insert the decision policy code. [Learn how to code your own email content](/en/docs/journey-optimizer/using/channels/email/design-email/start-creating-content/code-content).

| note |
| --- |
| NOTE |
| In **Code your own** mode, you can only return one decision item per policy, because the **Repeat Grid** component is not available. |

SMS
For SMS, you can add a new decision policy using either the **personalization editor**, or the **Decisioning** menu available in the properties pane.

| accordion |
| --- |
| Add a decision policy from the personalization editor |
| Open the personalization editor using the icon. Navigate to the Decision policies menu then click the Add decision policy button. |

| accordion |
| --- |
| Add a decison policy from the Decisioning menu |
| Click the icon from the properties pane to access the Decisioning menu. Click the Add decision policy button. |

Push notification
For Push notifications, you can add a new decision policy using either the **personalization editor**, or the **Decisioning** menu available in the properties pane.

| accordion |
| --- |
| Add a decision policy from the personalization editor |
| Open the personalization editor using the icon. Navigate to the Decision policies menu then click the Add decision policy button. |

| accordion |
| --- |
| Add a decison policy from the Decisioning menu |
| Click the icon from the properties pane to access the Decisioning menu. Click the Add decision policy button. note important IMPORTANT Experience Decisioning with push notifications requires a specific version of the Mobile SDK. Before implementing this feature, check the release notes to identify the required version and ensure you have upgraded accordingly. You can also view all available SDK versions for your platform in this section . | note important | IMPORTANT | Experience Decisioning with push notifications requires a specific version of the Mobile SDK. Before implementing this feature, check the [release notes](https://developer.adobe.com/client-sdks/home/release-notes#_blank) to identify the required version and ensure you have upgraded accordingly. You can also view all available SDK versions for your platform in [this section](https://developer.adobe.com/client-sdks/home/current-sdk-versions#_blank). |
| note important |
| IMPORTANT |
| Experience Decisioning with push notifications requires a specific version of the Mobile SDK. Before implementing this feature, check the [release notes](https://developer.adobe.com/client-sdks/home/release-notes#_blank) to identify the required version and ensure you have upgraded accordingly. You can also view all available SDK versions for your platform in [this section](https://developer.adobe.com/client-sdks/home/current-sdk-versions#_blank). |

## Configure the decision policy configure

After you have added a new decision policy into your content, the decision policy configuration screen opens. Follow these steps to configure the decision policy:

- Provide a name for the decision policy and select a catalog (currently limited to the default Offers catalog).
- The Number of items field allows you to define the number of decision items to return with decision policy. For example, if you select 2, the best 2 eligible offers will be presented for the current configuration. note NOTE This option is available for the Email and Code-based experience channels only. For all other channels, only 1 decision item can be returned per action. To return multiple items for the Email channel, you need to add the decision policy within a Repeat Grid component. Expand the section below for more details: accordion Return multiple decision items in emails Drag a Repeat Grid component in your email and configure it as desired using the Settings pane. Click the Decisioning icon in the canvas toolbar or open the Decisioning pane and select Add decision policy . Specify the number of items to return in the Number of items field then configure the decision policy as documented below. The maximum number of items you can select is limited by the number of tiles defined in the Repeat grid component.
- Click Next .

## Set up a strategy sequence strategy

The **Strategy sequence** section allows you to select the decision items and set up selection strategies to present with the decision policy.

- Click Add and choose the type of object to include in the policy: Selection strategy - Decision strategies leverage collections associated with eligibility constraints and ranking methods to determine the items to be shown. You can select one or multiple existing selection strategy, or create a new one using the Create selection strategy button. Learn how to create selection strategies Decision item - Select single decision items without having to run through a selection strategy. You can only select one decision item at a time. Any eligibility constraints set for the item will apply. note NOTE A decision policy supports up to 10 selection strategies and decision items combined. Learn more about Decisioning guardrails & limitations
- When adding several decision items and/or strategies, they will be evaluated in a specific order. The first object that was added to the sequence will be evaluated first, and so on. To change the default sequence, drag and drop the objects and/or the groups to reorder them as wanted. Expand the section below for more details. accordion Manage evaluation order in a decision policy Once you have added decision items and selection strategies to your policy, you can arrange their order to determine their evaluation order and combine together selection strategies to evaluate them together. The sequential order in which items and strategies will be evaluated is indicated with numbers at the left of each object or group of objects. To move the position of a selection strategy (or a group of strategies) within the sequence, drag and drop it to another position. note NOTE Only selection strategies can be dragged and drop within a sequence. To change the position of a decision item, you need to remove it and add it back using the Add button after adding the other items you want to evaluate before. You can also combine multiple selection strategies into groups so they are evaluated together and not separately. To do this, click the + button under a selection strategy to combine it with another one. You can also drag and drop a selection strategy on another one to group the two strategies into a group. note NOTE Decision items cannot be grouped together with other items or selection strategies. Multiple strategies and their grouping determine the priority of the strategies and ranking of eligible offers. The first strategy has the highest priority and the strategies combined within the same group have the same priority. For example, you have two collections, one in strategy A and one in strategy B. The request is for two decision items to be sent back. Let’s say there are two eligible offers from strategy A and three eligible offers from strategy B. If the two strategy are not combined or in sequential order (1 and 2), the top two eligible offers from the first strategy will be returned in the first row. If there are not two eligible offers for the first strategy, the decision engine will move on to the next strategy in sequence to find as many offers are still needed, and ultimately will return a fallback if needed. If the two collections are evaluated at the same time , as there are two eligible offers from strategy A and three eligible offers from strategy B, the five offers will all be stack ranged together based on the value determined by the respective ranking methods. Two offers are requested, therefore the top two eligible offers from these five offers will be returned. Example with multiple strategies Now let’s consider an example where you have multiple strategies divided into different groups. You defined three strategies. Strategy 1 and Strategy 2 are combined together in Group 1 and Strategy 3 is independent (Group 2). The eligible offers for each strategy and their priority (used in the ranking function evaluation) are as follows: Group 1: Strategy 1 - (Offer 1, Offer 2, Offer 3) - Priority 1 Strategy 2 - (Offer 3, Offer 4, Offer 5) - Priority 1 Group 2: Strategy 3 - (Offer 5, Offer 6) - Priority 0 The highest priority strategy offers is evaluated first and added to the ranked offers list. Iteration 1: Strategy 1 and Strategy 2 offers are evaluated together (Offer 1, Offer 2, Offer 3, Offer 4, Offer 5). Let’s say the result is: Offer 1 - 10 Offer 2 - 20 Offer 3 - 30 from Strategy 1, 45 from Strategy 2. The highest of both will be considered, so 45 is taken into account. Offer 4 - 40 Offer 5 - 50 The ranked offers are now as follows: Offer 5, Offer 3, Offer 4, Offer 2, Offer 1. Iteration 2: Strategy 3 offers are evaluated (Offer 5, Offer 6). Let’s say the result is: Offer 5 - Will not be evaluated since it already exists in the result above. Offer 6 - 60 The ranked offers are now as follows: Offer 5 , Offer 3, Offer 4, Offer 2, Offer 1, Offer 6.
- When your selection strategy is ready, click Next .

## Add fallback offers fallback

Once you have selected decision items and/or selection strategies, you can add fallback offers to display if none of the above items or selection strategies are qualified.

You can select any item from the list, which displays all the decision items created on the current sandbox. If no selection strategy is qualified, the fallback is displayed to the user no matter the dates and eligibility constraint applied to the selected itemnor frequency capping when available - TO CLARIFY.

NOTE
Fallbacks are optional. Up to the number of requested items can be selected. If none are eligible and no fallback is set, nothing will be displayed.
## Review & save the decision policy review

After configuring a selection strategy and adding fallback offers, click **Next** to review and save your decision policy then click **Create** to confirm the policy creation.

IMPORTANT
Once a decision policy is created, any changes made to it can take up to 15 minutes to propagate across all data regions, and up to 30 minutes for Canada. This includes changes such as adding a new decision item to a collection, changing a rule in an item, changing item content, or updating a formula.
You can edit or delete a decision policy at any time using the ellipsis button in the personalization editor, or in the **Decisioning** menu within the component properties pane.

Edit or delete a policy from the personalization editor
Edit or delete a policy from the Decisioning menu
## Assign a placement (Email) placement

For emails, you need to define a placement for the component associated to the decision policy. To do so, click the **Decisioning** button in the component properties pane and select **Assign placement**. [Learn how to work with placements](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/placements)

## Next steps next-steps

Now that you understand how to create a decision policy, you’re ready to use it into Journey Optimizer channels to deliver offers.

➡️ [Learn how to use decision policies in messages](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/use-decision-policy)

recommendation-more-help
