---
title: "Iterate over contextual data personalization-contexts"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/iterate-contextual-data"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:46.788134+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Iterate over contextual data personalization-contexts

Last update: May 8, 2026
- Topics:
- [Personalization](#)

CREATED FOR:

- Intermediate
- Developer

Learn how to use Handlebars iteration syntax to display dynamic lists of data from various sources in your messages, including events, custom action responses, and other contextual data.

## Overview overview

Journey Optimizer provides access to contextual data from multiple sources during [message personalization](/en/docs/journey-optimizer/using/content-management/personalization/personalize). You can iterate over arrays from these sources using Handlebars syntax in native channels ([email](/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design), [push](/en/docs/journey-optimizer/using/channels/push/create-push), [SMS](/en/docs/journey-optimizer/using/channels/sms/create-sms)) to display dynamic content like product lists, recommendations, or other repeating elements.

**Available context sources:**

- **Events**: Data from journey events (business events, unitary events)
- **Custom action responses**: Data returned from external API calls via custom actions
- **Dataset lookup**: Enriched data retrieved from Adobe Experience Platform datasets
- **Technical properties**: Journey metadata such as journey ID and supplemental identifiers
- **Journey context**: Other journey-related data accessible during execution

This guide shows you how to iterate over arrays from each of these sources in your messages, and how to work with arrays when configuring journey activities. Start with [Handlebars iteration syntax](#syntax) to understand message personalization basics, or jump to [Work with arrays in Journey expressions](#arrays-in-journeys) to learn how to pass array data to custom actions and dataset lookups.

## Handlebars iteration syntax syntax

Handlebars provides the {{#each}} [helper](/en/docs/journey-optimizer/using/content-management/personalization/functions/helpers) to iterate over arrays. The basic syntax is:

```
{{#each arrayPath as |item|}}
  <!-- Access item properties here -->
  {{item.property}}
{{/each}}
```

**Key points:**

- Replace arrayPath with the path to your array data
- Replace item with any variable name you prefer (e.g., product, response, element)
- Access properties of each item using {{item.propertyName}}
- You can nest multiple {{#each}} blocks for multi-level arrays

## Iterate over event data event-data

Event data is available when your journey is triggered by an [event](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events). This is useful for displaying data that was captured at the moment the journey started, such as cart contents, order items, or form submissions.

TIP
You can combine event data with other sources. See
Combine multiple context sources
for examples.
### Context path for events

```
context.journey.events.<event_ID>.<fieldPath>
```

- <event_ID>: The unique ID of your event as configured in the journey
- <fieldPath>: The path to the field or array within your event schema

NOTE
Numeric event IDs require backticks.
If your event ID is a number (for example,
1697323153
), wrap it in backticks (
`
) in your expression path. Without backticks, the PQL parser raises a syntax error.`
| code language-handlebars |
| --- |
| context.journey.events.`1697323153`.fieldName |

For more details and a complete example including date formatting from event timestamps, see
Formatting a timestamp from a context event
.
### Example: Cart items from an event

If your [event schema](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/experience-event-schema) includes a productListItems array (standard [XDM format](/en/docs/experience-platform/xdm/data-types/product-list-item#_blank)), you can display cart contents as detailed in the sample below.

View example code
| code language-handlebars |
| --- |
| {{#each context.journey.events.event_ID.productListItems as |product|}} <div class="product"> <h3>{{product.name}}</h3> <p>Quantity: {{product.quantity}}</p> <p>Price: ${{product.priceTotal}}</p> </div> {{/each}} |

### Example: Nested arrays in events

For nested structures, use nested {{#each}} blocks.

View example code
| code language-handlebars |
| --- |
| {{#each context.journey.events.event_ID.categories as |category|}} <h2>{{category.name}}</h2> <ul> {{#each category.items as |item|}} <li>{{item.title}}</li> {{/each}} </ul> {{/each}} |

Learn more about nesting in [Best practices](#best-practices).

## Iterate over custom action responses custom-action-responses

[Custom action](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration) responses contain data returned from external API calls. This is useful for displaying real-time information from your systems, such as loyalty points, product recommendations, inventory status, or personalized offers.

NOTE
Custom actions must be configured with a response payload to use this feature. Learn more in
this section
. You can also combine custom action responses with event data or dataset lookups - see
Combine multiple context sources
for examples.
### Context path for custom actions

```
context.journey.actions.<actionName>.<fieldPath>
```

- <actionName>: The name of your [custom action](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration) as configured in the journey
- <fieldPath>: The path to the field or array within the response payload

### Example: Product recommendations from an API

To iterate over an array of product recommendations returned from a custom action and display them as individual cards in your message, see the example below.

View example code
**API Response:**

| code language-json |
| --- |
| { "recommendations": [ { "productId": "12345", "productName": "Summer Jacket", "price": 89.99, "imageUrl": "https://example.com/jacket.jpg" }, { "productId": "67890", "productName": "Running Shoes", "price": 129.99, "imageUrl": "https://example.com/shoes.jpg" } ] } |

**Message personalization:**

| code language-handlebars |
| --- |
| <h2>Recommended for You</h2> <div class="recommendations"> {{#each context.journey.actions.GetRecommendations.recommendations as |item|}} <div class="product-card"> <img src="{{item.imageUrl}}" alt="{{item.productName}}" /> <h3>{{item.productName}}</h3> <p class="price">${{item.price}}</p> </div> {{/each}} </div> |

### Example: Nested arrays from custom actions

To iterate over a custom action response containing nested arrays (an array of objects, where each object contains another array), see the example below. This demonstrates using nested {{#each}} loops to access multiple levels of data.

View example code
**API Response:**

| code language-json |
| --- |
| { "id": "84632848268632", "responses": [ { "productIDs": [1111, 2222, 3333] }, { "productIDs": [4444, 5555, 6666] }, { "productIDs": [7777, 8888, 9999] } ] } |

**Message personalization:**

| code language-handlebars |
| --- |
| <h2>Product Groups</h2> {{#each context.journey.actions.GetProducts.responses as |response|}} <div class="product-group"> <ul> {{#each response.productIDs as |productID|}} <li>Product ID: {{productID}}</li> {{/each}} </ul> </div> {{/each}} |

For more complex nesting patterns, see [Best practices](#best-practices).

### Example: Loyalty tier benefits

To display dynamic benefits based on loyalty status, see the below example.

View example code
**API Response:**

| code language-json |
| --- |
| { "loyaltyTier": "gold", "benefits": [ { "name": "Free shipping", "icon": "truck" }, { "name": "20% discount", "icon": "percent" }, { "name": "Priority support", "icon": "headset" } ] } |

**Message personalization:**

| code language-handlebars |
| --- |
| <h2>Your {{context.journey.actions.GetLoyaltyInfo.loyaltyTier}} Member Benefits</h2> <ul class="benefits"> {{#each context.journey.actions.GetLoyaltyInfo.benefits as |benefit|}} <li> <span class="icon-{{benefit.icon}}"></span> {{benefit.name}} </li> {{/each}} </ul> |

## Iterate over dataset lookup results dataset-lookup

The [Dataset Lookup activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup) allows you to retrieve data from [Adobe Experience Platform datasets](/en/docs/experience-platform/catalog/datasets/overview#_blank) during journey runtime. The enriched data is stored as an array and can be iterated over in your messages.

Learn more about configuring the Dataset Lookup activity in [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup). Dataset lookup is particularly powerful when combined with event data - see [Example: Event data enriched with dataset lookup](#combine-sources) for a practical use case.

### Context path for dataset lookups

```
context.journey.datasetLookup.<activityID>.entities
```

- <activityID>: The unique ID of your Dataset Lookup activity
- entities: The array of enriched data retrieved from the dataset

### Example: Product details from a dataset

If you’re using a Dataset Lookup activity to retrieve product information based on SKUs, see sample below.

View example code
**Dataset Lookup Configuration:**

- Lookup Keys: list(@event{purchase_event.products.sku})
- Fields to Return: ["SKU", "category", "price", "name"]

**Message personalization:**

| code language-handlebars |
| --- |
| <h2>Product Details</h2> <table> <thead> <tr> <th>Product Name</th> <th>Category</th> <th>Price</th> </tr> </thead> <tbody> {{#each context.journey.datasetLookup.3709000.entities as |product|}} <tr> <td>{{product.name}}</td> <td>{{product.category}}</td> <td>${{product.price}}</td> </tr> {{/each}} </tbody> </table> |

### Example: Filtered iteration with dataset data

To filter dataset lookup results during iteration and display only items matching specific criteria (e.g., products from a particular category), use conditional {{#if}} statements within your {{#each}} loop. See the example below.

View example code
| code language-handlebars |
| --- |
| <h2>Household Products</h2> {{#each context.journey.datasetLookup.3709000.entities as |product|}} {{#if product.category = "household"}} <div class="product"> <h3>{{product.name}}</h3> <p>Price: ${{product.price}}</p> </div> {{/if}} {{/each}} |

Learn more about conditional filtering in [Best practices](#best-practices).

### Example: Calculate totals from dataset lookup

To calculate and display totals while iterating over dataset lookup results, see the example below.

View example code
| code language-handlebars |
| --- |
| {% let householdTotal = 0 %} {{#each context.journey.datasetLookup.3709000.entities as |product|}} {%#if product.category = "household"%} {% let householdTotal = householdTotal + product.price %} {%/if%} {{/each}} <p>Your household products total: ${{householdTotal}}</p> |

## Use journey technical properties technical-properties

Journey technical properties provide access to metadata about the journey execution, such as the journey ID and supplemental identifiers. These can be useful when combined with iteration patterns, especially for filtering arrays based on specific journey instances.

### Available technical properties

```
context.journey.technicalProperties.journeyUID
context.journey.technicalProperties.supplementalId
```

### Example: Filter array items using supplemental identifier

When using supplemental identifiers in event-triggered journeys with arrays, you can filter to show only the relevant item for the current journey instance. Learn more about supplemental identifiers in [this guide](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/supplemental-identifier).

**Scenario**: A journey is triggered with multiple bookings, but you want to display information only for the specific booking (identified by supplemental ID) that triggered this journey instance.

View example code
| code language-handlebars |
| --- |
| {{#each context.journey.events.event_ID.bookingList as |booking|}} {%#if booking.bookingInfo.bookingNum = context.journey.technicalProperties.supplementalId%} <div class="booking-details"> <h3>Your Booking: {{booking.bookingInfo.bookingNum}}</h3> <p>Destination: {{booking.bookingInfo.bookingCountry}}</p> <p>Date: {{booking.bookingInfo.bookingDate}}</p> </div> {%/if%} {{/each}} |

### Example: Include journey ID for tracking

To include the journey ID in your message for tracking purposes, see the example below.

View example code
| code language-handlebars |
| --- |
| <footer> <p>Journey Reference: {{context.journey.technicalProperties.journeyUID}}</p> </footer> |

## Combine multiple context sources combine-sources

You can combine data from different sources in the same message to create rich, personalized experiences. This section shows practical examples of using multiple context sources together.

**Context sources you can combine:**

- [Event data](#event-data) + [Custom action responses](#custom-action-responses)
- [Event data](#event-data) + [Dataset lookup](#dataset-lookup)
- [Multiple sources](#combine-sources) + [Technical properties](#technical-properties)

### Example: Cart items with real-time inventory

To combine event data (cart contents) with custom action data (inventory status), view the sample below.

View example code
| code language-handlebars |
| --- |
| <h2>Your Cart</h2> {{#each context.journey.events.cartEvent.productListItems as |product|}} <div class="cart-item"> <h3>{{product.name}}</h3> <p>Quantity: {{product.quantity}}</p> <p>Price: ${{product.priceTotal}}</p> </div> {{/each}} <h2>We Also Recommend</h2> {{#each context.journey.actions.GetRecommendations.items as |recommendation|}} <div class="recommendation"> <h4>{{recommendation.name}}</h4> <p>${{recommendation.price}}</p> {{#if recommendation.inStock}} <span class="badge">In Stock</span> {{else}} <span class="badge out-of-stock">Out of Stock</span> {{/if}} </div> {{/each}} |

### Example: Event data enriched with dataset lookup

To combine [event SKUs](#event-data) with detailed product information from a [dataset lookup](#dataset-lookup), view the sample below.

View example code
| code language-handlebars |
| --- |
| <h2>Your Order Details</h2> {{#each context.journey.events.orderEvent.productListItems as |item|}} <div class="order-item"> <p><strong>SKU:</strong> {{item.SKU}}</p> <p><strong>Quantity:</strong> {{item.quantity}}</p> <!-- Enrich with dataset lookup data --> {{#each context.journey.datasetLookup.1234567.entities as |enrichedProduct|}} {{#if enrichedProduct.SKU = item.SKU}} <p><strong>Product Name:</strong> {{enrichedProduct.name}}</p> <p><strong>Category:</strong> {{enrichedProduct.category}}</p> <img src="{{enrichedProduct.imageUrl}}" alt="{{enrichedProduct.name}}" /> {{/if}} {{/each}} </div> {{/each}} |

### Example: Combine multiple sources with technical properties

To combine multiple context sources (profile data, event data, custom actions, and technical properties) in a single message, view the sample below.

View example code
| code language-handlebars |
| --- |
| <div class="personalized-content"> <!-- Profile data --> <h1>Hello {{profile.person.name.firstName}},</h1> <!-- Event data iteration --> <h2>Your Recent Purchases</h2> {{#each context.journey.events.purchaseEvent.items as |purchase|}} <div class="purchase"> <p>{{purchase.productName}} - ${{purchase.price}}</p> </div> {{/each}} <!-- Custom action response iteration --> <h2>Recommended for You</h2> {{#each context.journey.actions.GetPersonalizedRecs.recommendations as |rec|}} <div class="recommendation"> <h3>{{rec.title}}</h3> <p>{{rec.description}}</p> </div> {{/each}} <!-- Technical properties --> <footer> <p class="fine-print">Journey ID: {{context.journey.technicalProperties.journeyUID}}</p> </footer> </div> |

## Other context types other-contexts

While this guide focuses on iteration over arrays, other context types are available for personalization that typically don’t require iteration. These are accessed directly rather than looped over:

- **Profile attributes** (profile.*): Individual profile fields from Adobe Experience Platform
- **Audiences** (inAudience()): Audience membership checks
- **Offer decisions**: Decision management offers
- **Target attributes** (Orchestrated campaigns only): Attributes calculated in the campaign canvas
- **Token** (context.token): Session or authentication tokens

For complete personalization syntax and examples using these sources, refer to:

- [Add personalization](/en/docs/journey-optimizer/using/content-management/personalization/personalization-build-expressions)
- [Personalization syntax](/en/docs/journey-optimizer/using/content-management/personalization/personalization-syntax)

## Work with arrays in Journey expressions arrays-in-journeys

While the previous sections focus on iterating over arrays in message personalization using Handlebars, you also work with arrays when configuring journey activities. This section explains how to use array data from events in Journey expressions, particularly when passing data to custom actions or using arrays with dataset lookups.

IMPORTANT
Journey expressions use a different syntax than Handlebars personalization. In journey configuration (such as custom action parameters or conditions), you use the
Journey expression editor
with functions like
first
,
all
, and
serializeList
. In message content, you use Handlebars syntax with
{{#each}}
loops.
### Pass array values to custom action parameters arrays-to-custom-actions

When configuring [custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration), you often need to extract values from event arrays and pass them as parameters. This section covers common patterns.

Learn more about passing collections in [Pass collections into custom action parameters](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/collections#passing-collection).

#### Extract a single value from an array

**Use case**: Get a specific field from an event array to pass as a query parameter in a GET request.

View example code
**Example scenario**: Extract the first SKU with a price greater than 0 from a product list.

**Event schema example**:

| code language-json |
| --- |
| { "commerce": { "productListItems": [ { "SKU": "SKU-1", "priceTotal": 10.0 }, { "SKU": "SKU-2", "priceTotal": 0.0 }, { "SKU": "SKU-3", "priceTotal": 20.0 } ] } } |

**Custom action configuration**:

- In your custom action, configure a query parameter (e.g., sku) with type string
- Mark it as Variable to allow dynamic values

**Journey expression in action parameter**:

| code language-javascript |
| --- |
| @event{YourEventName.commerce.productListItems.first(currentEventField.priceTotal > 0).SKU} |

**Explanation**:

- @event{YourEventName}: References your journey event
- .first(currentEventField.condition): Returns the first array item matching the condition
- currentEventField: Represents each item in the event array as you loop through it
- .SKU: Extracts the SKU field from the matched item
- Result: "SKU-1" (a string suitable for the action parameter)

Learn more about the first function in [Collection management functions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/collection-management-functions).

#### Build a list of values from an array

**Use case**: Create a comma-separated list of IDs to pass as a query parameter (e.g., /products?ids=sku1,sku2,sku3).

View example code
**Custom action configuration**:

- Configure a query parameter (e.g., ids) with type string
- Mark it as Variable

**Journey expression**:

| code language-javascript |
| --- |
| serializeList( @event{YourEventName.commerce.productListItems.all(currentEventField.priceTotal > 0).SKU}, ",", true ) |

**Explanation**:

- .all(currentEventField.condition) : Returns all array items matching the condition (returns a list)
- currentEventField : Represents each item in the event array as you loop through it
- .SKU : Projects the list to only include SKU values
- serializeList(list, delimiter, addQuotes) : Joins the list into a string "," : Use comma as delimiter true : Add quotes around each string element
- Result: "SKU-1,SKU-3" (suitable for a query parameter)

Learn more about:

- [all function](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/collection-management-functions)
- [serializeList function](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/list-functions#serializeList)

Collection handling for custom actions is covered in [Pass collections into custom action parameters](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/collections#passing-collection).

#### Pass an array of objects to a custom action

**Use case**: Send a complete array of objects in a request body (for POST or GET with body).

View example code
**Request body example**:

| code language-json |
| --- |
| { "ctxt": { "products": [ { "id": "productA", "name": "Product A", "price": 20.1, "color": "blue" } ] } } |

**Custom action configuration**:

- In the request body, define products as type listObject
- Mark it as Variable
- Define the object fields: id, name, price, color (each becomes mappable)

**Journey canvas configuration**:

- In Advanced mode, set the collection expression: code language-javascript @event{YourEventName.commerce.productListItems.all(currentEventField.priceTotal > 0)}
- In the collection mapping UI: Map id → productListItems.SKU Map name → productListItems.name Map price → productListItems.priceTotal Map color → productListItems.color

Journey Optimizer constructs the array of objects matching your action payload structure.

| note |
| --- |
| NOTE |
| When working with event arrays, use currentEventField to reference each item. For data source collections (Adobe Experience Platform), use currentDataPackField. For custom action response collections, use currentActionField. |

Learn more in [Pass collections into custom action parameters](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/collections#passing-collection).

### Use arrays with dataset lookups arrays-with-dataset-lookup

When using the [Dataset Lookup activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup), you can pass an array of values as lookup keys to retrieve enriched data.

**Example**: Look up product details for all SKUs in an event array.

View example code
**Dataset Lookup configuration**:

In the lookup keys field, use list() to convert an array path to a list:

| code language-javascript |
| --- |
| list(@event{purchaseEvent.productListItems.SKU}) |

This creates a list of all SKU values to look up in the dataset. The results are available as an array at context.journey.datasetLookup.<activityID>.entities that you can iterate over in your message (see [Iterate over dataset lookup results](#dataset-lookup)).

### Limitations and patterns array-limitations

Be aware of these limitations when working with arrays in journeys:

#### No dynamic looping over arrays in journey flow

Journeys cannot create dynamic loops where one action node is executed multiple times for each item in an array. This is intentional to prevent runaway performance issues.

**What you cannot do**:

- Execute a custom action once per array item dynamically
- Create multiple journey branches based on array length

**Recommended patterns instead**:

- Send all items at once : Pass the entire array or a serialized list to a single custom action that processes all items. See Build a list of values from an array .
- Use external aggregation : Have your external API accept multiple IDs and return combined results in a single call.
- Pre-compute in AEP : Use computed attributes to pre-calculate values from arrays at the profile level.
- Single value extraction : If you only need one value, extract it using first or head . See Extract a single value from an array .

Learn more in [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails).

#### Array size considerations

Large arrays can impact journey performance:

- **Event arrays**: Keep event payloads under 50KB total
- **Custom action responses**: Response payloads should be under 100KB
- **Dataset lookup results**: Limit the number of lookup keys and returned entities

### Complete example: Event array to custom action complete-example

Here’s a complete workflow showing how to use an event array with a custom action.

**Scenario**: When a user abandons their cart, send cart data to an external recommendation API to get personalized suggestions, then display them in an email.

View example code
**Step 1: Configure the custom action**

Create a custom action “GetCartRecommendations”:

- **Method**: POST
- **URL**: https://api.example.com/recommendations
- **Request body**:

| code language-json |
| --- |
| { "cartItems": [ { "sku": "string", "price": 0, "quantity": 0 } ] } |

- Mark cartItems as type listObject and Variable
- Define fields: sku (string), price (number), quantity (integer)

Learn more in [Configure a custom action](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration).

**Step 2: Configure response payload**

In the custom action, configure the response:

| code language-json |
| --- |
| { "recommendations": [ { "productId": "string", "productName": "string", "price": 0, "imageUrl": "string" } ] } |

Learn more in [Use API call responses](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response).

**Step 3: Wire the action in the journey**

- After your cart abandonment event, add the custom action
- In Advanced mode for the cartItems collection: code language-javascript @event{cartAbandonment.commerce.productListItems.all(currentEventField.quantity > 0)}
- Map the collection fields: sku → productListItems.SKU price → productListItems.priceTotal quantity → productListItems.quantity

**Step 4: Use the response in your email**

In your email content, iterate over the recommendations:

| code language-handlebars |
| --- |
| <h2>We noticed you left these items in your cart</h2> {{#each context.journey.events.cartAbandonment.productListItems as |item|}} <div class="cart-item"> <p>{{item.name}} - Quantity: {{item.quantity}}</p> </div> {{/each}} <h2>You might also like</h2> {{#each context.journey.actions.GetCartRecommendations.recommendations as |rec|}} <div class="recommendation"> <img src="{{rec.imageUrl}}" alt="{{rec.productName}}" /> <h3>{{rec.productName}}</h3> <p>${{rec.price}}</p> </div> {{/each}} |

**Step 5: Test your configuration**

Before running a live journey, test the custom action using the “Send test request” feature in the action configuration to verify the built request and values.

- Use [journey test mode](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)
- Trigger with sample event data including a productListItems array
- Verify the custom action receives the correct array structure
- Check the [action test logs](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response#test-mode-logs)
- Preview the email to confirm both arrays display correctly

Learn more in [Troubleshoot your custom actions](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshoot-custom-action).

## Best practices best-practices

Follow these best practices when iterating over contextual data to create maintainable, performant personalization.

### Use descriptive variable names

Choose variable names that clearly indicate what you’re iterating over. This makes your code more readable and easier to maintain. Learn more about [personalization syntax](/en/docs/journey-optimizer/using/content-management/personalization/personalization-syntax):

View example code
| code language-handlebars |
| --- |
| <!-- Good --> {{#each products as |product|}} {{#each users as |user|}} {{#each recommendations as |recommendation|}} <!-- Less clear --> {{#each items as |item|}} {{#each array as |element|}} |

### Expression fragments in loops

When using [expression fragments](/en/docs/journey-optimizer/using/content-management/personalization/use-expression-fragments) within {{#each}} loops, be aware that you cannot pass loop-scoped variables as fragment parameters. However, fragments can access global variables that are defined in your message content outside of the fragment.

View example code
**Supported pattern - Use global variables:**

| code language-handlebars |
| --- |
| {% let globalDiscount = 15 %} {{#each context.journey.actions.GetProducts.items as |product|}} <div class="product"> <h3>{{product.name}}</h3> {{fragment id='ajo:fragment123/variant456' mode='inline'}} </div> {{/each}} |

The fragment can reference globalDiscount because it’s defined globally in the message.

**Not supported - Passing loop variables:**

| code language-handlebars |
| --- |
| {{#each products as |product|}} <!-- This will NOT work as expected --> {{fragment id='ajo:fragment123/variant456' currentProduct=product}} {{/each}} |

**Workaround**: Include the personalization logic directly in your loop instead of using a fragment, or call the fragment outside of the loop.

Learn more about [using expression fragments inside loops](/en/docs/journey-optimizer/using/content-management/personalization/use-expression-fragments#fragments-in-loops), including detailed examples and additional workarounds.

### Handle empty arrays

Use the {{else}} clause to provide fallback content when an array is empty. Learn more about [helper functions](/en/docs/journey-optimizer/using/content-management/personalization/functions/helpers):

View example code
| code language-handlebars |
| --- |
| {{#each context.journey.actions.GetRecommendations.items as |item|}} <div>{{item.name}}</div> {{else}} <p>No recommendations available at this time.</p> {{/each}} |

### Combine with conditional helpers

Use {{#if}} within loops for conditional content. Learn more about [conditional rules](/en/docs/journey-optimizer/using/content-management/dynamic/create-conditions) and see examples in [Custom action responses](#custom-action-responses) and [Dataset lookup](#dataset-lookup) sections.

View example code
| code language-handlebars |
| --- |
| {{#each context.journey.actions.GetProducts.items as |product|}} <div class="product"> <h3>{{product.name}}</h3> {{#if product.onSale}} <span class="badge">On Sale!</span> {{/if}} {{#if product.newArrival}} <span class="badge">New</span> {{/if}} </div> {{/each}} |

### Limit iteration for performance

For large arrays, consider limiting the number of iterations:

View example code
| code language-handlebars |
| --- |
| <!-- Display only first 5 items --> {{#each context.journey.actions.GetProducts.items as |product|}} {{#if @index < 5}} <div>{{product.name}}</div> {{/if}} {{/each}} |

### Access array metadata

Handlebars provides special variables within loops that help with advanced iteration patterns:

- @index: Current iteration index (0-based)
- @first: True for the first iteration
- @last: True for the last iteration

View example code
| code language-handlebars |
| --- |
| {{#each products as |product|}} <div class="product {{#if @first}}featured{{/if}}"> {{@index}}. {{product.name}} </div> {{/each}} |

NOTE
These Handlebars variables (
@index
,
@first
,
@last
) are only available within
{{#each}}
loops in message personalization. For working with arrays in Journey expressions (such as getting the first item from an array before passing to a custom action), use array functions like
head
,
first
, or
all
. See
Work with arrays in Journey expressions
for more details.
## Troubleshooting troubleshooting

Having issues with iteration? This section covers common problems and solutions.

### Array not displaying

**Issue**: Your array iteration isn’t showing any content.

View possible causes and solutions
**Possible causes and solutions**:

- Incorrect path : Verify the exact path to your array based on the context source: For events : context.journey.events.<event_ID>.<fieldPath> For custom actions : context.journey.actions.<actionName>.<fieldPath> For dataset lookups : context.journey.datasetLookup.<activityID>.entities
- Array is empty : Add an {{else}} clause to check if the array has no data. See Best practices for examples.
- Data not available yet : Ensure the custom action, event, or dataset lookup activity has been executed before the message activity in your journey flow.

### Syntax errors

**Issue**: Expression validation fails or message doesn’t render.

View common mistakes
**Common mistakes**:

- Missing closing tags: Every {{#each}} must have a {{/each}}. Review [Handlebars iteration syntax](#syntax) for proper structure.
- Incorrect variable name: Ensure consistent use of variable name throughout the block. See [Best practices](#best-practices) for naming conventions.
- Incorrect path separators: Use dots (.) not slashes or other characters

### Expression fragments not working in loops

**Issue**: An expression fragment doesn’t display expected content when used inside an {{#each}} loop, or shows empty/unexpected output.

View possible causes and solutions
**Possible causes and solutions**:

- Trying to pass loop variables as parameters : Expression fragments cannot receive loop-scoped variables (like the current iteration item) as parameters. This is a known limitation. Solution : Use one of these workarounds: Define global variables in your message that the fragment can access Include the personalization logic directly in your loop instead of using a fragment Call the fragment outside of the loop if it doesn’t need loop-specific data
- Fragment expects a parameter that isn’t available : If your fragment was designed to receive specific input parameters, it won’t work correctly when those parameters can’t be passed from within a loop. Solution : Restructure your approach to use global variables that the fragment can access. See Best practices - Expression fragments in loops for examples.
- Incorrect variable scope : The fragment might be trying to reference a variable that only exists within the loop scope. Solution : Define any variables the fragment needs at the message level (outside the loop) so they’re globally accessible.

Learn more about [using expression fragments inside loops](/en/docs/journey-optimizer/using/content-management/personalization/use-expression-fragments#fragments-in-loops), including detailed explanations, examples, and recommended patterns.

### Testing your iterations

Use [journey test mode](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) to verify your iterations. This is especially important when using [custom actions](#custom-action-responses) or [dataset lookups](#dataset-lookup):

View testing steps
- Start your journey in [test mode](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)
- Trigger the event or custom action with sample data
- Check the [message preview](/en/docs/journey-optimizer/using/test/preview-test/preview) to verify the iteration displays correctly
- Review test mode logs for any errors (see [Custom action test mode logs](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response#test-mode-logs))

## Related topics related-topics

**Personalization fundamentals:** [Get started with personalization](/en/docs/journey-optimizer/using/content-management/personalization/personalize) | [Add personalization](/en/docs/journey-optimizer/using/content-management/personalization/personalization-build-expressions) | [Personalization syntax](/en/docs/journey-optimizer/using/content-management/personalization/personalization-syntax) | [Helper functions](/en/docs/journey-optimizer/using/content-management/personalization/functions/helpers) | [Create conditional rules](/en/docs/journey-optimizer/using/content-management/dynamic/create-conditions)

**Journey configuration:** [About events](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events) | [Configure custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration) | [Pass collections into custom action parameters](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/collections#passing-collection) | [Use API call responses in custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response) | [Troubleshoot your custom actions](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshoot-custom-action) | [Use Adobe Experience Platform data in journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup) | [Use supplemental identifiers in journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/supplemental-identifier) | [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails) | [Test your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)

**Journey expression functions:** [Advanced expression editor](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced) | [Collection management functions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/collection-management-functions) (first, all, last) | [List functions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/list-functions) (serializeList, filter, sort) | [Array functions](/en/docs/journey-optimizer/using/content-management/personalization/functions/arrays-list) (head, tail)

**Personalization use cases:** [Cart abandonment email](/en/docs/journey-optimizer/using/content-management/personalization/personalization-use-cases/personalization-use-case-helper-functions) | [Order status notification](/en/docs/journey-optimizer/using/content-management/personalization/personalization-use-cases/personalization-use-case)

**Message design:** [Get started with email design](/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design) | [Create push notifications](/en/docs/journey-optimizer/using/channels/push/create-push) | [Create SMS messages](/en/docs/journey-optimizer/using/channels/sms/create-sms) | [Preview and test your content](/en/docs/journey-optimizer/using/test/preview-test/preview-test)

recommendation-more-help
