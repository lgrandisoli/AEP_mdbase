---
title: "Leverage fragments in decision policies fragments"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/fragments-decision-policies"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:43.534985+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Leverage fragments in decision policies fragments

Last update: May 8, 2026
- Topics:
- [Decisioning](#)

CREATED FOR:

- Experienced
- User

If your decision policy contains decision items including fragments, you can leverage these fragments when authoring a message, within the decision policy. [Learn more on fragments](/en/docs/journey-optimizer/using/content-management/fragments/fragments)

AVAILABILITY
This feature is available for the
Code-based experience
and
Email
channels.
For example, let’s say you want to display different contents for several mobile device models. Add the specified fragments, each pertaining to a different phone model, to the decision item you are using in the decision policy. [Learn how](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/manage-decision-items/items#attributes).

{width="70%"}

Once done, you can use either one of the following methods:

Directly insert the code
Simply copy-paste the code block below into the decision policy code. Replace variable with the fragment ID and placement with the fragment reference key:

| code language-handlebars |
| --- |
| {% let variable = get(item._experience.decisioning.offeritem.contentReferencesMap, "placement").id %} {{fragment id = variable required=false}} |

Follow the detailed steps
- Navigate to the Helper functions and add the Let function {% let variable = expression %} {{variable}} to the code pane, where you can declare the variable for your fragment.
- Use the Map > Get function {%= get(map, string) %} to build your expression. The map is the fragment referenced in the decision item. The string can be the device model you entered in the decision item as the Fragment reference key .
- You can also use a contextual attribute which would contain this device model ID.
- Add the variable that you chose for your fragment as the fragment ID.

The fragment ID and reference key will be selected from the decision item’s **Fragments** section.

WARNING
If the fragment key is incorrect or if the fragment content is not valid, rendering may fail and cause an error in the Edge call.
To avoid failures when a fragment is temporarily unavailable, the
required=false
flag is used so the fragment is skipped instead.
Learn more
## Usage and guardrails fragments-guardrails

### Simulate content and expression fragments in emails simulate-content-expression-fragments

For the **Email** channel, expression fragments associated with a decision item display correctly when you **Send proof** or when the campaign is activated. However, **Simulate content** does not display the expression fragment from the decision item.

### Visual fragments and decision items in emails visual-fragments-decision-items

You cannot assign a **Visual fragment** to a decision item, only **expression fragments** are supported in this context.

### Decision item and context attributes decision-item-context-attributes

Decision item attributes and contextual attributes are not supported by default in Journey Optimizer fragments. However, you can use global variables instead, such as described below.

Let’s say you want to use the *sport* variable in your fragment.

- Reference this variable in the fragment, for example: code language-text Elevate your practice with new {{sport}} gear!
- Define the variable with the Let function within the decision policy block. In the example below, sport is defined with the decision item attribute: code language-handlebars {#each decisionPolicy.13e1d23d-b8a7-4f71-a32e-d833c51361e0.items as |item|}} {% let sport = item._cjmstage.value %} {{fragment id = get(item._experience.decisioning.offeritem.contentReferencesMap, "placement1").id }} {{/each}}

### Decision item fragment content validation fragment-content-validation

- Due to the dynamic nature of these fragments, when used in a campaign, message validation during campaign content creation is skipped for fragments referenced in decision items.
- The validation of the fragment content happens only during the fragment creation and publication.
- For JSON-type expression fragments, the content is syntactically validated upon saving the fragment. Validation errors are displayed as alerts.

At runtime, the campaign content (including fragment content from decision items) is validated. In case of a validation failure, the campaign will not get rendered.

### Temporarily unavailable fragments are skipped temporary-unavailable-fragments

When journeys or campaigns reference fragments attached to decision items, there can be short synchronization delays before updated fragments are available on Edge.

To avoid failures when a fragment is temporarily unavailable, fragments now have the required flag set to false by default so that they are skipped instead of causing the journey or campaign to fail.

This means that if the fragment is temporarily unavailable on Edge, it is simply ignored. If the fragment is available, it renders normally.

**Example**

If your decision policy qualifies for two offers and each has a fragment—for example, “20% off” and “30% off”—and the second fragment is temporarily unavailable, with required=false the system renders the available offer (20% off) and skips the other fragment (30% off) instead of failing the journey or campaign. This improves reliability when content is still synchronizing.

NOTE
You can still mark a fragment as mandatory by setting the
required
flag to
true
. However, if a fragment is temporarily missing, it may cause journey or campaign rendering to fail.
recommendation-more-help
