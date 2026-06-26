---
title: "Personalization use case: cart abandonment email personalization-use-case-helper-functions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/personalization-use-cases/personalization-use-case-helper-functions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:06.297010+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Personalization use case: cart abandonment email personalization-use-case-helper-functions

Last update: May 8, 2026
- Topics:
- [Personalization](#)
- [Use Cases](#)

CREATED FOR:

- Intermediate
- Developer

In this example, you will personalize the body of an email message. This message targets customers who have left items in their shopping cart, but have not completed their purchase.

You will use these types of helper functions:

- The upperCase string function, to insert the customer’s first name in capital letters. [Learn more](/en/docs/journey-optimizer/using/content-management/personalization/functions/string#upper).
- The each helper, to list the items that are in the cart. [Learn more](/en/docs/journey-optimizer/using/content-management/personalization/functions/helpers#each).
- The if helper, to insert a product-specific note if the related product is in the cart. [Learn more](/en/docs/journey-optimizer/using/content-management/personalization/functions/helpers#if-function).

➡️ [Learn how to use helper functions in this video](#video)

Before you start, ensure you know how to configure these elements:

- A unitary event. [Learn more](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).
- A journey that starts with an event. [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer).
- An email message in your journey. [Learn more](/en/docs/journey-optimizer/using/channels/email/create-email)
- The body of an email. [Learn more](/en/docs/journey-optimizer/using/channels/email/design-email/start-creating-content/content-from-scratch).

Follow these steps:

- [Create the initial event and the journey](#create-context).
- [Create an email message](#configure-email).
- [Insert the customer’s first name in capital letters](#uppercase-function).
- [Add the cart content to the email](#each-helper).
- [Insert a product-specific note](#if-helper).
- [Test and publish the journey](#test-and-publish).

## Step 1: Create the initial event and the related journey create-context

The cart content is contextual information from the journey. Therefore, you must add an initial event and the email to a journey before you can add cart-specific information to the email.

- Create an event whose schema includes the productListItems array.
- Define all the fields from this array as payload fields for this event. Learn more about the product list item data type in Adobe Experience Platform documentation .
- Create a journey that starts with this event.
- Add an Email activity to the journey.

## Step 2: Create the email configure-email

- In the Email activity, click Edit content , then click Email Designer .
- From the left palette of the Email Designer home page, drag and drop three structure components onto the body of the message.
- Drag and drop an HTML content component onto each new structure component.

## Step 3: Insert the customer’s first name in capital letters uppercase-function

- On the Email Designer home page, click on the HTML component where you want to add the customer’s first name.
- On the contextual toolbar, click Show the source code .
- In the Edit HTML window, add the upperCase string function: In the left menu, select Helper functions . Use the search field to find “upper case”. From the search results, add the upperCase function. To do this, click the Plus (+) sign next to {%= upperCase(string) %}: string . The Expression editor shows this expression: code language-handlebars {%= upperCase(string) %}
- Remove the “string” placeholder from the expression.
- Add the first name token: In the left menu, select Profile attributes . Select Person > Full name . Add the First name token to the expression. The Expression editor shows this expression: code language-handlebars {%= upperCase(profile.person.name.firstName) %} Learn more about the person name data type in Adobe Experience Platform documentation .
- Click Validate , then click Save .
- Save the message.

## Step 4: Insert the list of items from the cart each-helper

This step demonstrates iterating over event data. For comprehensive examples of iterating over different data sources (events, custom action responses, and other contextual data), see [Iterate over contextual data with Handlebars](/en/docs/journey-optimizer/using/content-management/personalization/iterate-contextual-data).

- Reopen the message content.
- On the Email Designer home page, click on the HTML component where you want to list the cart content.
- On the contextual toolbar, click Show the source code .
- In the Edit HTML window, add the each helper: In the left menu, select Helper functions . Use the search field to find “each”. From the search results, add the each helper. The Expression editor shows this expression: code language-handlebars {{#each someArray as |variable|}} {{/each}}
- Add the productListItems array to the expression: Remove the “someArray” placeholder from the expression. In the left menu, select Contextual attributes . Contextual attributes are available only after the journey context has been passed to the message. Select Journey Optimizer > Events > event_name , then expand the productListItems node. In this example, event_name represents the name of your event. Add the Product token to the expression. The Expression editor shows this expression: code language-handlebars {{#each context.journey.events.event_ID.productListItems.product as |variable|}} {{/each}} In this example, event_ID represents the ID of your event. Modify the expression: Remove the “.product” string. Replace the “variable” placeholder with “product”. This example shows the modified expression: code language-handlebars {{#each context.journey.events.event_ID.productListItems as |product|}}
- Paste this code between the opening {{#each}} tag and the closing {{/each}} tag: code language-html <table> <tbody> <tr> <td><b>#name</b></td> <td><b>#quantity</b></td> <td><b>$#priceTotal</b></td> </tr> </tbody> </table>
- Add the personalization tokens for the item name, the quantity, and the price: Remove the placeholder “#name” from the HTML table. From the previous search results, add the Name token to the expression. Repeat these steps twice: Replace the placeholder “#quantity” with the Quantity token. Replace the placeholder “#priceTotal” with the Total price token. This example shows the modified expression: code language-handlebars {{#each context.journey.events.event_ID.productListItems as |product|}} <table> <tbody> <tr> <td><b>{{product.name}}</b></td> <td><b>{{product.quantity}}</b></td> <td><b>${{product.priceTotal}}</b></td> </tr> </tbody> </table> {{/each}}
- Click Validate , then click Save .

## Step 5: Insert a product-specific note if-helper

- On the Email Designer home page, click on the HTML component where you want to insert the note.
- On the contextual toolbar, click Show the source code .
- In the Edit HTML window, add the if helper: In the left menu, select Helper functions . Use the search field to find “if”. From the search results, add the if helper. The Expression editor shows this expression: code language-handlebars {%#if condition1%} render_1 {%else if condition2%} render_2 {%else%} default_render {%/if%}
- Remove this condition from the expression: code language-handlebars {%else if condition2%} render_2 This example shows the modified expression: code language-handlebars {%#if condition1%} render_1 {%else%} default_render {%/if%}
- Add the product name token to the condition: Remove the “condition1” placeholder from the expression. In the left menu, select Contextual attributes . Select Journey Orchestration > Events > event_name , then expand the productListItems node. In this example, event_name represents the name of your event. Add the Name token to the expression. The Expression editor shows this expression: code language-handlebars {%#if context.journey.events.`event_ID`.productListItems.name%} render_1 {%else%} default_render {%/if%}
- Modify the expression: In the Expression editor, specify the product name after the name token. Use this syntax, where product_name represents the name of your product: code language-javascript = "product_name" In this example, the product name is “Juno Jacket”: code language-handlebars {%#if context.journey.events.`event_ID`.productListItems.name = "Juno Jacket" %} render_1 {%else%} default_render {%/if%} Replace the “render_1” placeholder with the text of the note. Example: code language-handlebars {%#if context.journey.events.`event_ID`.productListItems.name = "Juno Jacket" %} Due to longer than usual lead times on the Juno Jacket, please expect item to ship two weeks after purchase. {%else%} default_render {%/if%} Remove the “default_render” placeholder from the expression.
- Click Validate , then click Save .
- Save the message.

## Step 6: Test and publish the journey test-and-publish

- Turn on the Test toggle, then click Trigger an event .
- In the Event configuration window, enter the input values, then click Send . The test mode works only with test profiles. The email is sent to the address of the test profile. In this example, the email contains the note about the Juno Jacket because this product is in the cart:
- Verify that there is no error, then publish the journey.

## Related topics related-topics

### Handlebars functions handlebars

- Helpers
- String functions

### Use cases use-case

- Personalization with profile information, context, and offer
- Personalization with decision-based offer

## How-to video video

Learn how to use helper functions.

https://video.tv.adobe.com/v/334244?quality=12&learn=on
recommendation-more-help
