---
title: "Work with consent policies consent-management"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/privacy/consent/consent"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:25.033620+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with consent policies consent-management

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Actions](#)
- [Custom Actions](#)
- [Privacy](#)
- [Consent Management](#)

CREATED FOR:

- Experienced
- Developer
- Admin

Your data may be subject to usage restrictions defined by your organization or by legal regulations. It is therefore important to ensure that your data operations within Journey Optimizer are compliant with [data usage policies](/en/docs/experience-platform/data-governance/policies/overview#_blank). These policies are Adobe Experience Platform rules defining which marketing actions you are allowed to perform on data.

By default, if a profile has opted out from receiving communications from you, the corresponding profile is excluded from subsequent deliveries. You can create a **consent policy** that overrides this default logic. For example, you can create a consent policy in Experience Platform to exclude customers who have not consented to receive communication for a given channel. In the absence of a custom policy, the default policy applies.

IMPORTANT
Consent policies are currently only available for organizations that have purchased the Adobe
Healthcare Shield
or
Privacy and Security Shield
add-on offerings.
The main steps to apply consent policies are as follows:

- Create a consent policy in Adobe Experience Platform with an associated marketing action. Learn how to create a consent policy
- Apply consent policies in Adobe Journey Optimizer using channel configurations or journey custom actions. Create a channel configuration with an associated marketing action. When creating a communication using the channel configuration, it will inherit the marketing action that has been associated and apply the corresponding consent policies defined in Adobe Experience Platform. Learn how to leverage consent policies through channel configurations At journey level, you can either: Associate a channel and a marketing action to a custom action when configuring it. Learn how to leverage consent policies when configuring a custom action Define an additional marketing action when adding a custom action in a journey. Learn how to leverage consent policies when adding a custom action in a journey

## Leverage consent policies through channel configurations surface-marketing-actions

In Journey Optimizer, consent is handled by the Experience Platform [Consent schema](/en/docs/experience-platform/xdm/field-groups/profile/consents#_blank). By default, the value for the consent field is empty and treated as consent to receive your communications. You can modify this default value while onboarding to one of the possible values listed [here](/en/docs/experience-platform/xdm/data-types/consents#choice-values#_blank).

To modify the consent field value, you can create a custom consent policy in which you define a marketing action and the conditions under which that action is performed. [Learn more about marketing actions](/en/docs/experience-platform/data-governance/policies/overview#marketing-actions#_blank)

For example, if you want to create a consent policy to target only profiles who have consented to receive email communications, follow the steps below.

- Make sure your organization has purchased the Adobe Healthcare Shield or Privacy and Security Shield add-on offerings. Learn more
- In Adobe Experience Platform, create a custom policy (from the Privacy > Policies menu). Learn how![](assets/consent-policy-create.png)
- Choose the Consent policy type and configure a condition as follows. Learn how to configure consent policies Under the If section, select the Email Targeting default marketing action. note NOTE The core marketing actions provided out-of-the-box by Adobe are listed in this table . The steps to create a custom marketing action are listed in this section . Select what happens when the marketing action applies. In this example, select Email Marketing Consent .
- Save and enable this policy.
- In Journey Optimizer, create an email channel configuration. Learn how
- In the email configuration details, select the Email Targeting marketing action.

All consent policies associated with that marketing action are automatically leveraged in order to respect the preferences of your customers.

Therefore, in this example, any [email](/en/docs/journey-optimizer/using/channels/email/create-email) using that configuration in a campaign or a journey is only sent to the profiles who have consented to receive emails from you. Profiles who have not consented to receive email communications are excluded.

## Leverage consent policies through custom actions journey-custom-actions

### Important notes important-notes

In Journey Optimizer, consent can also be leveraged in custom actions. If you want to use it with the build-in message capabilities, you need to use a condition activity to filter customers in your journey.

With consent management, two journey activities are analyzed:

- Read audience: the retrieved audience is taken into account.
- Custom action: consent management takes into account the attributes used ([action parameters](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration#define-the-message-parameters)) as well as the marketing action(s) defined (required marketing action and additional marketing action).
- Attributes that are part of a field group using the out-of-the-box Union Schema are not supported. These attributes will be hidden from the interface. You need to create another field group using a different schema.
- Consent policies only apply when a marketing action (required or additional) is set at the custom action level.

All other activities used in a journey are not taken into account. If you start your journey with an Audience qualification, the audience is not taken into account.

In a journey, if a profile is excluded by a consent policy in a custom action, the message is not sent to him, but he continues the journey. The profile does not go to the timeout and error path when using a condition.

Before refreshing policies in a custom action positioned in a journey, make sure your journey has no error.

### Leverage consent policies when configuring a custom action consent-custom-action

When configuring a custom action, two fields can be used for consent management.

The **Channel** field allows you to select the channel related to this custom action. It prefills the **Required marketing action** field with the default marketing action for the selected channel. If you select **other**, no marketing action is defined by default.

The **Required marketing action** allows you to define the marketing action related to your custom action. For example, if you use that custom action to send emails, you can select **Email targeting**. When used in a journey, all consent policies associated with that marketing action are retrieved and leveraged. A default marketing action is selected, but you can click the down arrow to select any available marketing actions from the list.

For certain types of important communications, for example a transactional message sent to reset the client’s password, you may not want to apply a consent policy. You will then select **None** in the **Required marketing action** field.

The other steps for configuring a custom action are detailed in [this section](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/about-custom-action-configuration#consent-management).

### Leverage consent policies when adding a custom action in a journey consent-journey

When adding the custom action in a journey, several options allow you to manage consent. Click the **Show read-only fields** to display all parameters.

The **Channel** and **Required marketing action**, defined when configuring the custom action, are displayed at the top of the screen. You cannot modify these fields.

You can define an **Additional marketing action** to set the type of custom action. This allows you to define the purpose of the custom action in this journey. In addition to the required marketing action, which is usually specific to a channel, you can define an additional marketing action which is specific to the custom action in this particular journey. For example: a workout communication, a newsletter, a fitness communication, etc. Both the required marketing action and the additional marketing action apply.

Click the **Refresh policies** button, at the bottom of the screen, to update and check the list of policies taken into consideration for this custom action. This is for information purpose only, while building a journey. With live journeys, consent policies are retrieved and updated automatically every 6 hours.

The other steps for configuring a custom action in a journey are detailed in [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-custom-actions).

recommendation-more-help
