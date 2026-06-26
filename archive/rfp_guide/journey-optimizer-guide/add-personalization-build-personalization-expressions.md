---
title: "Add personalization build-personalization-expressions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/personalization-build-expressions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:49.075724+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Add personalization build-personalization-expressions

Last update: May 8, 2026
- Topics:
- [Personalization](#)

CREATED FOR:

- Intermediate
- Developer

The personalization editor is the centerpiece of the personalization in Journey Optimizer. It is available in every context where you need to define personalization like emails, push and offers.

In the personalization editor interface, you can select, arrange, customize and validate all the data to create a customized personalization for your content.

## Where can I add personalization where

You can add personalization in **Journey Optimizer** in every fields with the icon. Expand the sections below for more details.

Messages
In messages, personalization can be added at different locations in your messages, such as the **Subject line** field.

It can also be added in other sections of your content. For example, for [push notifications](/en/docs/journey-optimizer/using/channels/push/push-config/push-gs), personalization can be added in **Title**, **Body**, **Custom sound**, **Badges** and **Custom data** fields.

Email Designer
When editing email content in the [Email Designer](/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design), you can add personalization in most of the text elements using the icon in the contextual tool bar.

URLs
Journey Optimizer also allows you to personalize **URLs** in your messages. Personalized URLs take recipients to specific pages of a website, or to a personalized microsite, depending on the profile attributes. [Learn more](/en/docs/journey-optimizer/using/channels/email/design-email/add-content/url-personalization)

{width="50%"}

| note |
| --- |
| NOTE |
| URL personalization is available for these types of links: **External link**, **Unsubscription link** and **Opt-Out**. |

Email configuration
When creating an email channel configuration, you can define personalized values for subdomains, headers and URL tracking parameters.
Learn more
Offers
You can add personalization when using text-type content in your
offers’ representations
.
Learn how to create personalized offers
## Personalization sources sources

The navigation pane lets you select the source for personalization. Available sources are:

- **Profile attributes** : lists all the references associated to the profile schema described in [Adobe Experience Platform Data Model (XDM) documentation](/en/docs/experience-platform/xdm/home#_blank).
- **Target attributes** : This folder is specific to Orchestrated campaigns. It contains attributes calculated directly within the campaign canvas. [Learn how to add personalization in Orchestrated campaigns](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/design-campaigns/channels#add-personalization)
- **Audiences** : lists all the audiences created in Adobe Experience Platform Segmentation service. Learn more in the [Adobe Experience Platform Segmentation documentation](/en/docs/experience-platform/segmentation/home#_blank).
- **Offer decisions** : lists all the offers associated to a specific placement. Select the placement then insert the offers in your content. For a complete documentation on how to manage offers, refer to [this section](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/get-started-decision/starting-offer-decisioning).
- **Contextual attributes** : when a channel action activity (Email, push, SMS) is used in a journey or campaign, contextual attributes related to events and properties are available for personalization. An example of personalization leveraging contextual attributes is presented in [this section](/en/docs/journey-optimizer/using/content-management/personalization/personalization-use-cases/personalization-use-case). Additionally, custom action responses can be used for personalization. [Learn how to use custom action responses in native channels](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action-response#response-in-channels).

NOTE
If you are targeting an audience with enrichment attributes generated using a composition workflow, you can leverage these enrichment attributes to personalize your message.
Learn how to use audiences enrichment attributes
## Add personalization add

The central workspace is where you build your personalization syntax. To use an attribute to personalize your message, locate it into the left navigation pane and click the + button to add it into the expression.

The ellipsis menu next to the + icon allows you to get more details for each attribute and to add your most frequently used attributes to favorites. Attributes added to favorites are accessible from the **Favorites** menu in the navigation pane.

NOTE
By default, the attributes pane shows only populated attributes. To display all attributes, select the
button located above the search field and toggle off the
Show only populated attributes
option.
Additionally, you can define default fallback text that will display if a string-type profile attribute is empty. To do this, click the ellipsis button next to the attribute and select **Insert with fallback text**. Write the text that should display by default if the attribute’s value is empty for a profile then click **Add**.

In the following example, the personalization editor lets you select the profiles that have their birthday today then complete the customization by inserting a specific offer corresponding to this day.

## Options for expression editing options

The central workspace provides various tools to help you write your personalization expression.

Available options are:

- Find / Find and replace : Search through your expression and automatically replace portions of code.
- Undo / Redo : Undo / Redo the last operation.
- Auto complete : Automatically suggests and completes code as you type. This feature is available only for HTML and Text formats and supports Profile and Context attributes. If disabled via the toggle, the editor will provide native HTML code auto-completion instead. {align="center" width="70%" modal="regular"}
- HTML / JSON / Text : Identify the format of your code. This allows the system to adapt the validation and auto complete feature based on the selected language.
- Validate : Check the syntax of your expression. Learn more in this section .
- Save as fragment : Save your expression as an expression fragment. Learn more in this section
- Font size : Adjusts the font size for the contents inside the editor for better readability.
- Word wrap : Enables or disables word wrapping, allowing long expressions to be displayed on a single line or wrapped within the editor. Options include: Off (Default) - No word wrapping. Long lines extend beyond the editor view and require horizontal scrolling. On - Wraps lines at the width of the editor. Word wrap column - Wraps lines when a line characters reach 80 characters. Bounded - Wraps lines at either the editor width or at 80 characters, whichever is smaller.
- Pills : Display attributes as compact “pills” to improve readability by hiding long attribute paths. Click on an attribute to display its full path. note NOTE This option is only available for profile attributes, contextual attributes, and dynamic media.

In the navigation pane, additional features are available to help you build your personalization expression.

- Helper functions - Helper functions allow you to perform operations on data, such as calculations, data formatting or conversions, conditions, and manipulate them in the context of personalization. Learn more about available helper functions
- Favorites - Attributes that you have added to favorites display in this list. This allows you to quickly access to your most frequency used items. To add an attribute to your favorites, click the ellipsis menu and choose Add to favorites .
- Conditions - Leverage conditional rules created in the library to add dynamic content into your messages. This allows you to create multiple variants of your message based on conditions. Learn how to create dynamic content
- Fragments - Leverage expression fragments that have been created or saved to the current sandbox. A fragment is a reusable component that can be referenced across Journey Optimizer campaigns and journeys. This functionality allows to prebuild multiple custom content blocks that can be used by marketing users to quickly assemble contents in an improved design process. Learn how to use expression fragments for personalization

Once your personalization expression is ready, you need to have it validated by the personalization editor. Learn more in [this section](/en/docs/journey-optimizer/using/content-management/personalization/personalization-build-expressions).

## Validation mechanisms validation-mechanisms

The validation of your expression is automatically executed when you click on the **Add** button to close the editor window. You can also use the **Validate** button to check your personalization syntax.

Expand the section below to see common errors that may occur when validating personalization.

Common errors
- **Path “XYZ” not found**

When trying to reference a field that is not defined in the schema.

In this case **firstName1** is not defined as attribute in the profile schema:

| code language-none |
| --- |
| {{profile.person.name.firstName1}} |

- **Type mismatch for variable “XYZ”. Expected array. Found string.**

When trying to iterate over a string instead of array.

In this case **product** is not an array:

| code language-none |
| --- |
| {{each profile.person.name.firstName as |product|}} {{product.productName}} {{/each}} |

- **Invalid handlebars syntax. Found '[XYZ}}'**

When invalid handlebars syntax is used.

Handlebars expressions are surrounded with **{{expression}}**

| code language-none |
| --- |
| {{[profile.person.name.firstName}} |

- **Invalid segment definition**

| code language-none |
| --- |
| No segment definition found for 988afe9f0-d4ae-42c8-a0be-8d90e66e151 |

For offers, specific errors may occur. Expand the section below for more details:

Specific errors related to offers
The errors related to offers integration in an Email or Push message have the following pattern :

| code language-none |
| --- |
| Offer.<offerType>.[PlacementID].[ActivityID].<offer-attribute> |

The validation is performed during personalization content validation in the personalization editor.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 |  |
| --- | --- |
| Error title | Validation / Resolution |
| Resource with id placementID and type OfferPlacement not foundResource with id activityID and type OfferActivity not found | Check if ActivityID and/or PlacementID are available |
| Resource could not be validated. | The componentType in the Placement should match the offerType offer |
| The public URL is not present in offer offerId. | The Image Offers (all Personalized and fallback associated with the decision and placement pair) should have public URL populated (deliveryURL should not be empty). |
| The decision contains non-profile attributes. | Offers Model usage should contain only the profile attributes. |
| An error occurred while fetching the decision usage. | This error could occur when the API is trying to fetch the offer model. |
| Offer Attribute offer-attribute is invalid. | Check if the offer-attribute referenced in offer drp is valid. Following are the valid attributes:Image: deliveryURL, linkURLText: contentHTML: content |

recommendation-more-help
