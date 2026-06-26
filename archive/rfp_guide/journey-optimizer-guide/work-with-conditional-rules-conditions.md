---
title: "Work with conditional rules conditions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/dynamic/create-conditions"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:04.243363+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with conditional rules conditions

Last update: May 8, 2026
- Topics:
- [Personalization](#)
- [Rules](#)

CREATED FOR:

- Intermediate
- Developer

Conditional rules are sets of rules that define which content should be displayed in your messages, depending on various criteria like profiles’ attributes, audience membership or contextual events.

Conditional rules are created using the personalization editor and can be stored if you want to reuse them across your contents. [Learn how to save a conditional rule to the library](#save)

NOTE
Individuals will need the
Manage Library Items
permission to save or delete conditional rules. Saved conditions are available for use by all users within an organization.
## Access the conditional rule builder access

Conditional rules are created from the **Conditions** menu within the personalization editor, which is accessible either:

- From the Email Designer, when enabling dynamic content for a component in the email body. Learn how to add dynamic content into emails
- In any field where you can add personalization using the personalization editor .

## Create a conditional rule create-condition

The steps to create a conditional rule are as follows:

- Access the Conditions menu from the personalization editor or the Email Designer, then click Create new .
- Build the conditional rule according to your needs. To do this, drag and drop and arrange the desired attributes from the left menu into the canvas. The steps to combine attributes into the canvas are similar to the segment building experience. For more information on how to work with the rule builder canvas, refer to this documentation . Attributes are organized into three tabs: Profile : Audiences lists all audience attributes (i.e. status, version etc.) for Adobe Experience Platform Segmentation service , XDM Individual profiles lists all the profile attributes associated to the Experience Data Model (XDM) schema defined in Adobe Experience Platform. Contextual : when your message is used in a journey, contextual journey fields are available through this tab. Audiences : lists all the audiences generated from segment definitions created in Adobe Experience Platform Segmentation service .
- Once your conditional rule is ready, you can add it to your message to create dynamic content. Learn how to add dynamic content You can also save the rule to allow further reuse. Learn how to save a condition

## Save a conditional rule save

If there are condition rules that you will frequently reuse, you can save them to the conditions library. All saved rules are shared and can be accessed and used by individuals within your organization.

NOTE
Conditional rules that leverage journeys contextual attributes cannot be saved to the library.
- In the condition edition screen, click the Save condition button.
- Give a name and a description (optional) to the rule, then click Add .
- The conditional rule is saved to the library. You can now use it to create dynamic content into your messages. Learn how to add dynamic content

CAUTION
When naming conditional content variants, use only alphanumeric characters (A-Z, a-z, 0-9). The use of special characters (such as
<
,
>
,
=
,
{
,
}
, etc.) in variant names can cause the template editor to break or hide components.
## Edit and delete saved conditional rules edit-delete

You can delete a conditional rule at any time using the ellipsis button.

Conditional rules saved to the library cannot be modified. However, you can still use them to create new rules. To do this, open the conditional rule, make the desired changes then save it to the library. [Learn how to save a condition to the library](#save)

recommendation-more-help
