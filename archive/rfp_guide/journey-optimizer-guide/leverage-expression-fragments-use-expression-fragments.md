---
title: "Leverage expression fragments use-expression-fragments"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/use-expression-fragments"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:03.713927+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Leverage expression fragments use-expression-fragments

Last update: May 8, 2026
- Topics:
- [Personalization](#)
- [Fragments](#)

CREATED FOR:

- Intermediate
- Developer

When using the **personalization editor**, you can leverage all the expression fragments that have been created or saved to the current sandbox.

A fragment is a reusable component that can be referenced across Journey Optimizer campaigns and journeys. This functionality allows to prebuild multiple custom content blocks that can be used by marketing users to quickly assemble contents in an improved design process. [Learn more on fragments](/en/docs/journey-optimizer/using/content-management/fragments/fragments)

➡️ [Learn how to manage, author and use fragments in this video](/en/docs/journey-optimizer/using/content-management/fragments/fragments#video-fragments)

## Use an expression fragment use-expression-fragment

To add expression fragments to your content, follow the steps below.

NOTE
You can add up to 30 fragments in a given delivery. Fragments can only be nested up to 1 level.
- Open the personalization editor and select the Fragments button on the left pane. The list displays all the expression fragments that have been created or saved as fragments on the current sandbox. Learn how to create fragments They are sorted by creation date: recently added expression fragments are shown first in the list. You can also refresh this list. note NOTE If some fragments were modified or added while you are editing your content, the list will be updated with the latest changes.
- Click the + icon next to an expression fragment to insert the corresponding fragment ID into the editor. note caution CAUTION You can add any Draft or Live fragment to your content. However, you won’t be able to activate your journey or campaign if a fragment with the Draft status is being used in it. At journey or campaign publication, draft fragments will show an error and you’ll need to approve them to be able to publish.
- Once the fragment ID has been added, if you open the corresponding expression fragment and edit it from the interface, the changes are synchronized. They are automatically propagated to all draft or live journeys/campaigns containing that fragment ID.
- Click the More actions button next to a fragment. From the contextual menu that opens, select View fragment to get more information about that fragment. The Fragment ID is also displayed and can be copied from here.
- You can open the expression fragment in another window to edit its content and properties - either using the Open fragment option in the contextual menu or from the Fragment info pane. Learn how to edit a fragment
- You can then customize and validate your content as usual using all the personalization and authoring capabilities of the personalization editor .
- In some cases, you only need to compute variables, so you may want to hide the content of the expression fragment. To do this, use the render attribute and set it to false . For example: code language-none Hi {{profile.person.name.firstName|fragment id='ajo:fragmentId/variantId' mode ='inline' render=false}}

NOTE
If you create an expression fragment that contains multiple line breaks and use it in
SMS
or
push
content, the line breaks are preserved. Thus make sure to test your
SMS
or
push
message before sending it.
## Use implicit variables implicit-variables

The implicit variables enhance the existing fragment functionality to improve efficiency for content reusability and scripting use cases. Fragments can use input variables and create output variables which can be used in campaign and journey content.

This capability can for example be used to initialize tracking parameters of your emails, based on the current campaign or journey, and use these parameters into the personalized links added to the email content.

The following use cases are possible:

- Use an input variables in a fragment. When a fragment is used in a campaign/journey action content, it has the ability to leverage variables that were declared outside of the fragment. Below is an example: We can see above the utm_content variable is declared in the campaign content. When the fragment Hero block is used, it will show a link to which the utm_content parameter value will be appended. The final result is: https://luma.enablementadobe.com?utm_campaign= Product_launch&utm_content= start_shopping .
- Use an output variables from a fragment. Variables calculated or defined inside a fragment are available for use in your contents. In the following example, a fragment F1 declares a set of variables: In an email content, you can have the following personalization: The fragment F1 initializes the following variables: utm_campaign and utm_content . Then the link in the message content will have these parameters appended. The final result is: https://luma.enablementadobe.com?utm_campaign= Product_launch&utm_content= start_shopping .

NOTE
At runtime, the system expands what is inside fragments and then interprets the personalization code from top to bottom. Keeping this in mind, more complex use cases can be achieved. For example, you can have a fragment F1 passing variables to another fragment F2 sitting below. You can also have a visual fragment F1 passing variables to a nested expression fragment F2.
## Use expression fragments inside loops fragments-in-loops

When using expression fragments within {{#each}} loops, it’s important to understand how variable scoping works. Expression fragments can access global variables defined in your message content, but they cannot receive loop-specific variables as parameters.

### Supported pattern: Use global variables global-variables-in-loops

Expression fragments can reference global variables that are defined outside of the fragment, even when the fragment is called from within a loop. This is the recommended approach when you need to use fragments in iterative contexts.

**Example: Using a fragment with global variables inside a loop**

In your message content, define a global variable and use a fragment that references it:

```
{% let globalDiscount = 15 %}

{{#each context.journey.actions.GetProducts.items as |product|}}
  <div class="product">
    <h3>{{product.name}}</h3>
    <p>Price: ${{product.price}}</p>
    {{fragment id='ajo:fragment123/variant456' mode='inline'}}
  </div>
{{/each}}
```

In the expression fragment (fragment123), you can reference the globalDiscount variable:

```
<p class="discount-info">Save {{globalDiscount}}% on all items!</p>
```

This pattern works because the global variable is accessible throughout the message, including within fragments, regardless of loop context.

### Not supported: Passing loop variables as fragment parameters loop-variables-limitations

You cannot pass the current iteration item (e.g., product in the example above) as a parameter to an expression fragment. The fragment cannot directly access loop-scoped variables from the surrounding {{#each}} block.

**Example: What does NOT work**

```
{{#each context.journey.actions.GetProducts.items as |product|}}
  <!-- This will NOT work as expected -->
  {{fragment id='ajo:fragment123/variant456' mode='inline' currentProduct=product}}
{{/each}}
```

The fragment cannot receive product as a parameter and use it internally because parameter passing for loop-specific variables is not supported in the current implementation.

### Recommended workarounds fragments-in-loops-workarounds

When you need to use expression fragments with data from a loop, consider these approaches:

- Include logic directly in the message : Instead of using a fragment for loop-specific logic, add the personalization code directly within your {{#each}} block. code language-handlebars {{#each context.journey.actions.GetProducts.items as |product|}} <div class="product"> <h3>{{product.name}}</h3> <p>Price: ${{product.price}}</p> {{#if product.price > 100}} <span class="premium-badge">Premium Product</span> {{/if}} </div> {{/each}}
- Use fragments outside of loops : If the fragment content is not loop-dependent, call the fragment before or after the iteration block. code language-handlebars {{fragment id='ajo:fragment123/variant456' mode='inline'}} {{#each context.journey.actions.GetProducts.items as |product|}} <div class="product"> <h3>{{product.name}}</h3> <p>Price: ${{product.price}}</p> </div> {{/each}}
- Set multiple global variables : If you need to pass different values to a fragment across iterations, set global variables before each fragment call (though this limits flexibility).

NOTE
For iterating over contextual data and working with loops, see the comprehensive guide on
iterating over contextual data
, which includes best practices, troubleshooting tips, and advanced patterns.
## Customize editable fields customize-fields

If certain portions of an expression fragment have been made editable using variables, you can override their default values using a specific syntax. [Learn how to make your fragments customizable](/en/docs/journey-optimizer/using/content-management/fragments/customizable-fragments)

To customize the fields, follow these steps:

- Insert the fragment into your code from the Fragments menu.
- Use the <fieldId>="<value>" code at the end of the syntax to override the default value of the variable. In the example below, we are overriding the value of a variable whose ID is “sports” with the “yoga” value. This will display “yoga” in your fragment content everywhere the “sport” variable is referenced.

An example showing how to add editable fields into an expression fragments and override their values when creating an email is available in [this section](/en/docs/journey-optimizer/using/content-management/fragments/customizable-fragments#example).

## Break inheritance break-inheritance

When adding a fragment ID to the personalization editor, the changes made to the original expression fragment are synchronized.

However, you can also paste the content of an expression fragment into the editor. From the contextual menu, select **Paste fragment** to insert that content.

In that case, the inheritance from the original fragment is broken. The content of the fragment is copied into the editor, and the changes are not synchronized anymore.

It becomes a standalone element that is no longer linked to the original fragment; you can edit it as any other element in your code.

recommendation-more-help
