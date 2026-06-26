---
title: "Use Adobe Experience Platform data in journeys datalookup"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:54.962691+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

[Limited Availability]{class="badge informative"}

# Use Adobe Experience Platform data in journeys datalookup

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

The **Dataset lookup** activity allows you to dynamically retrieve data from Adobe Experience Platform record datasets during runtime. By leveraging this capability, you can access data that may not reside in the profile or event payload, ensuring your customer interactions are both relevant and timely.

AVAILABILITY
This feature is currently available to all customers as a limited availability release.
Key Benefits:

- **Real-Time personalization**: Tailor customer experiences using enriched data.
- **Dynamic decision-making**: Use external data to drive journey logic and actions.
- **Enhanced data Access**: Retrieve product metadata, pricing tables, or relational data tied to specific keys.

## Must-read must-read

Review these requirements before you configure dataset lookups.

### Dataset enablement

The dataset must be enabled for lookup in Adobe Experience Platform. Detailed information is available in this section: [Use Adobe Experience Platform data](/en/docs/journey-optimizer/using/data-management/lookup-aep-data).

### Limits & restrictions

- Maximum of 10 Dataset Lookup activities per journey.
- Maximum of 20 selected fields.
- Maximum of 50 keys in the lookup keys array.
- Enriched data size is limited to 10KB.

### Additional performance considerations

The below recommendations are guidance to avoid delays in deliverability:

Consideration
Recommended limit
Description
Attributes per Lookup
Up to 20
Number of data fields retrieved per record in a single lookup activity.
Lookup Activities
Up to 5 per journey
Each journey can contain up to 5 separate lookup activities. Each lookup can target a different dataset.
## Configure the Dataset lookup activity configure

To configure the **Dataset lookup** activity, follow these steps:

- Unfold the Orchestration category and drop a Dataset lookup activity into your canvas.
- Add a label and description.
- In the Dataset field, select the dataset with the attributes you need. note NOTE If the dataset you are looking for does not display in the list, make sure you have enabled it for lookup. For more details, refer to the Must read section.
- Select the specific fields you want to fetch from the dataset. You can only select leaf nodes (fields at the lowest level of the schema). The field must be a primitive value (string, number, boolean, date, etc.). Lists (arrays) and maps (key–value objects) cannot be selected. accordion Example
- In the Lookup key(s) field, choose a joining key that exists in both the decision item attributes and the dataset. This key is used by the system to search in the selected dataset. Keys can be expressions derived from the journey context, such as SKUs, email IDs, or other identifiers. Example: @profile.email or list(@event{purchase_event.products.sku}) . Only strings or lists of strings are supported. note important IMPORTANT You must define the lookup key using advanced mode . If you use simple mode to set the key, the dataset lookup activity output will not be available as a context attribute in downstream activities, and the @datasetLookup{} syntax will fail with a “Dataset lookup not found” error in condition activities. accordion Example

## Use enriched data in the journey

The data retrieved by the **Dataset lookup** activity is stored in the Journey context as an array of objects. It is available in the journey expression editor and personalization editor, enabling conditional logic and personalized messaging based on enriched data.

- Journey Expression Editor : Access the Advanced mode editor and use the syntax: @datasetLookup{MyDatasetLookUpActivity1.entities} . Learn how to work with the advanced expression editor
- Personalization Editor : Use the syntax: {{context.journey.datasetLookup.1482319411.entities}} .

NOTE
Enriched data is transient and available only during the runtime of the journey, and in the personalization of outbound activities (Email, Push, SMS, etc.)
## Examples of use cases

Product Category-Based Filtering
**Scenario**:Send a coupon to users who spend more than $40 on household products.

**Journey flow**:

- Purchase Event : Capture SKUs from the user’s cart.
- Dataset lookup activity : Dataset: products-dataset (SKU as the primary key). Lookup Keys: list(@event{purchase_event.products.sku}) . Fields to Return: ["SKU", "category", "price"] .
- Condition activity : Filter SKUs where the category is “household”. code language-none @event{purchase_event.products.all( in(currentEventField.sku, @datasetlookup{MyDatasetLookupActivity1.entities.all(currentDatasetLookupField.category == 'household').sku} ) )} OR Aggregate the total spend on household products and compare it to the $40 threshold. code language-none sum(@event{purchase_event.products.all( in(currentEventField.sku, @datasetlookup{MyDatasetLookUpActivity1.entities.all(currentDatasetLookupField.category == 'household').sku} ) )}.price}, ',', true ) > 40
- Personalization Editor : Use the enriched data to personalize the email content: code language-none {% let householdTotal = 0 %} {{#each journey.datasetlookup.3709000.entities as |product|}} {%#if get(product, "category") = "household"%} {% let householdTotal = householdTotal + product.price %}{%/if%} {{/each}} "Hi, thanks for spending " + {%= householdTotal %} + " on household products. Here is your reward!"

Personalization using external loyalty data
**Scenario**: Identify which email account for a profile has a Loyalty Status of Platinum. In this scenario, loyalty account is associated to an email ID and loyalty data is not available in the standard profile lookup store.

**Journey flow**:

- Profile Event Trigger : Capture email IDs from the profile or event context.
- Dataset Lookup activity : Dataset: loyalty-member-dataset (email as the primary key). Lookup Keys: @profile.email . Fields to Return: ["email", "loyaltyTier"] .
- Condition activity : Branch the journey based on the loyalty tier: code language-none @datasetLookup{MyDatasetLookUpActivity1.entity.loyaltyMember.loyaltyTier} == 'Platinum'
- Personalization Editor : Use the enriched loyalty tier data to personalize outbound communication: code language-none {{context.journey.datasetLookup.1482319411.entity.loyaltyMember.loyaltyTier}}

## Troubleshooting troubleshooting

### “Dataset lookup not found” error in condition activity troubleshooting-not-found

**Symptom:** The @datasetLookup{} syntax in a condition activity’s advanced expression editor returns a “Dataset lookup not found” error, even though the dataset lookup activity is correctly configured in the journey.

**Cause:** The lookup key in the dataset lookup activity was set using simple mode. When the key is not defined in advanced mode, the activity output is not exposed as a context attribute in downstream activities.

**Fix:** Open the dataset lookup activity, locate the **Lookup key(s)** field, and switch to **advanced mode** to redefine the key expression. Save the activity and republish the journey.

recommendation-more-help
