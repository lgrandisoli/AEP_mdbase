---
title: "Manage data usage policies in the UI user-guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-governance/policies/user-guide"
category: "guides"
topic: "experience-platform/data-governance-guide"
created_at: "2026-06-26T17:24:00.491000+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Governance Guide

# Manage data usage policies in the UI user-guide

Last update: June 18, 2026
- Topics:
- [Data Governance](#)

CREATED FOR:

- User
- Developer
- Admin

This document covers how to use the **Policies** workspace in the Adobe Experience Platform UI to create and manage data usage policies.

NOTE
For information on how to manage access control policies in the UI, refer to the
attribute-based access control UI guide
instead.
IMPORTANT
All data usage policies (including core policies provided by Adobe) are disabled by default. In order for an individual policy to be considered for enforcement, you must manually enable that policy. See the section on
enabling policies
for steps on how to do this in the UI.
## Prerequisites

This guide requires a working understanding of the following Experience Platform concepts:

- [Data governance](/en/docs/experience-platform/data-governance/home)
- [Data usage policies](/en/docs/experience-platform/data-governance/policies/overview)

## View existing policies view-policies

In the Experience Platform UI, select **Policies** to open the **Policies** workspace. In the **Browse** tab, you can see a list of available policies, including their associated labels, marketing actions, and status.

If you have access to consent policies, select the **Consent policies** toggle to view them in the Browse tab.

Select a listed policy to view its description and type. If a custom policy is selected, additional controls are displayed to edit, delete, or [enable/disable the policy](#enable).

## Create a custom policy create-policy

To create a new custom data usage policy, select **Create policy** in the top-right corner of the **Browse** tab in the **Policies** workspace.

The Choose type of policy dialog appears. Select either a [consent policy](#consent-policy) or a [data governance policy](#create-governance-policy).

### Use data governance and consent policies together combine-policies

NOTE
Consent policies are currently only available for organizations that have purchased Adobe Healthcare Shield or Adobe Privacy & Security Shield.
Governance and consent policies can be used together to create robust rules for governing audiences mapped to a destination. Consent policies are inclusive in nature, meaning they dictate which profiles can be included in each marketing experience. Conversely, governance policies exclude the use of specific labelled attributes from being configured for activation.

By using this behavior, you can set up a combination of policies and consent rules that include the correct profiles, but prevents you from including data that goes against your set organizational rules. An example scenario would be, where you want to exclude sensitive data from being included but are still able to target consented users for marketing via social media. The necessary steps for this scenario are outlined in the infographic below.

### Create a data governance policy create-governance-policy

The **Create policy** workflow appears. Start by providing a name and a description for the new policy.

Next, select the data usage labels that the policy will be based on. When selecting multiple labels, you are given the option to choose whether the data should contain all the labels or just one of them in order for the policy to apply. Select **Next** when finished.

The **Select marketing actions** step appears. Choose the appropriate marketing actions from the provided list, then select **Next** to continue.

NOTE
When selecting multiple marketing actions, the policy interprets them as an “OR” rule. In other words, the policy applies if
any
of the selected marketing actions are performed.
The **Review** step appears, allowing you to review the details of the new policy before creating it. Once you are satisfied, select **Finish** to create the policy.

The **Browse** tab reappears, which now lists the newly created policy in “Draft” status. To enable the policy, see the next section.

### Create a consent policy consent-policy

IMPORTANT
Consent policies are only available for organizations that have purchased
Adobe Healthcare Shield
or
Adobe Privacy & Security Shield
.
If you chose to create a consent policy, a new screen appears that allows you to configure the new policy.

In order to make use of consent policies, you must have consent attributes present in your profile data. See the guide on [consent processing in Experience Platform](/en/docs/experience-platform/landing/governance-privacy-security/consent/adobe/overview) for detailed steps on how to include the required attributes in your union schema.

Consent policies are comprised of two logical components:

- **If**: The condition that will trigger the policy check. This can be based on a certain marketing action being performed, the presence of certain data usage labels, or a combination of the two.
- **Then**: The consent attributes that must be present for a profile to be included in the action that triggered the policy.

NOTE
Consent policies support advanced rule building with various field types and operators. For a complete reference of supported field types, operators, and rule-building examples, see the
Consent policy rules reference
.
#### Configure conditions consent-conditions

Under the **If** section, select the marketing actions and/or data usage labels that should trigger this policy. Select **View all** and **Select labels** to view the full lists of available marketing actions and labels, respectively.

Once you have added at least one condition, you can select **Add condition** to continue adding further conditions as necessary, choosing the appropriate condition type from the dropdown.

If you select more than one condition, you can use the icon that appears between them to switch the conditional relationship between “AND” and “OR”.

#### Select consent attributes consent-attributes

Under the **Then** section, select at least one consent attribute from the union schema. This is the attribute that must be present in order for profiles to be included in the action governed by this policy. You can choose one of the suggested options, or select **View all** to choose the attribute directly from the union schema.

NOTE
Consent policies support primitive field types (String, Number, Boolean, Date) and container types (Object, Map, Array). You can navigate into containers to select specific attributes and apply AND/OR logic to combine rules. For a full reference of supported field types, operators, and rule-building examples, see the
consent policy rule building reference
.
If you select **View all**, the **Select consent attribute** dialog appears. Select the consent attribute(s) that you want this policy to check for. Alternatively, from this dialog, you can select **Advanced Schema search** to choose a nested primitive field to be assessed as part of the policy. Select **Done** to confirm your settings.

### Advanced schema search advanced-schema-search

In the **Select consent attribute** dialog, select **Advanced Schema search** to open the **Select union schema field** dialog. From this view, select root-level or nested attributes of primitive field types such as string, number, boolean, and date, as well as container types such as object, map, and array.

#### Fixed-value fields for a policy condition fixed-value-fields

When you select a fixed-value field as a policy condition, the Selected attributes panel displays the predefined values defined in your data schema.

NOTE
If a field is configured with a fixed set of values (for example, as an enum or other controlled vocabulary), the policy builder enforces that constraint to ensure conditions are evaluated only against valid, standardized data.
To maintain data quality and consistency, the UI renders these values as selectable checkboxes rather than free-text fields. This approach reduces manual validation and helps your consent policy evaluate data reliably.

To define the condition, select the checkboxes for the values you want the policy to evaluate.

#### Map data type fields for a policy condition map-data-type-fields

When you select a primitive field contained in a Map data type, additional configuration options appear in the **Selected attributes** panel. Use these options to configure consent checks across multiple keys without needing a separate policy for each key. This configuration method simplifies policy management by reducing the number of policies you need to create.

##### Configure Map data type attributes configure-map-attributes

To configure a Map-type attribute, follow the steps below:

In the union schema diagram, select a primitive field (such as a string or number) contained within a Map data type. The **Selected attributes** panel updates to display additional configuration options for that field.

In the **Selected attributes** panel, configure how the policy evaluates map keys by selecting or clearing the **Find any matching item** checkbox.

Option
Action
Policy Behavior
Find any matching item
checkbox is
selected
The
within
text field is disabled.
The policy checks
every key
within the map. Any key where the nested field meets the value condition is considered a match for the policy. This is useful for enforcing global compliance across dynamically keyed attributes.
Find any matching item
checkbox is
unselected
You must enter a specific key name in the
within
text field.
The policy checks only the map key specified in the
within
field. Only profiles where the nested field for a specific key meets the defined value are matched. This is useful for policies targeting a specific program or frequency key (for example,
frequencyMap.m1
).
Enter the value for the selected primitive field that the policy should evaluate. For example, if the field type is Integer, enter a numeric value.

Select **Select** to confirm your configuration and return to the policy builder.

After you select at least one consent attribute, the **Policy properties** panel updates to show the estimated number of profiles included under this policy, along with the percentage of affected profiles in the Profile store. The estimated profile count updates automatically as you change the policy configuration.

To add additional consent attributes, select **Add result**. This creates another rule for including profiles based on those attributes.

NOTE
To edit an existing attribute, select the attribute name and then select the pencil icon (
). The
Select union schema field
dialog opens for you to make changes.
Continue adding or adjusting conditions and consent attributes until the policy matches your requirements. When finished, enter a name and (optional) description, then select **Save** to create the policy.

The consent policy is now created, and its status is set to Disabled by default. To enable the policy right away, select the **Status** toggle in the right rail.

#### Verify policy enforcement

After you have created and enabled a consent policy, you can preview how it affects your consented audiences when activating segments to destinations. See the section on [consent policy evaluation](/en/docs/experience-platform/data-governance/enforcement/auto-enforcement#consent-policy-evaluation) for more information.

## Enable or disable a policy enable

All data usage policies (including core policies provided by Adobe) are disabled by default. For an individual policy to be considered for enforcement, you must manually enable that policy through the API or UI.

You can enable or disable policies from the **Browse** tab in the **Policies** workspace. Select a custom policy from the list to display its details on the right. Under **Status**, select the toggle button to enable or disable the policy.

## View marketing actions view-marketing-actions

In the **Policies** workspace, select the **Marketing actions** tab to view a list of available marketing actions defined by Adobe and your own organization.

## Create a marketing action create-marketing-action

To create a new custom marketing action, select **Create marketing action** in the top-right corner of the **Marketing actions** tab in the **Policies** workspace.

The **Create marketing action** dialog appears. Enter a name and description for the marketing action, then select **Create**.

The newly created action appears in the **Marketing actions** tab. You can now use the marketing action when [creating new data usage policies](#create-policy).

## Edit or delete a marketing action edit-delete-marketing-action

NOTE
Only custom marketing actions defined by your organization can be edited. Marketing actions defined by Adobe cannot be changed or deleted.
In the **Policies** workspace, select the **Marketing actions** tab to view a list of available marketing actions defined by Adobe and your own organization. Select a custom marketing action from the list, then used the provided fields in the right-hand section to edit the marketing action’s details.

If the marketing action is not being used by any existing usage policies, you can delete it by selecting **Delete marketing action**.

NOTE
Attempting to delete a marketing action that is being used by an existing policy causes an error message to appear, indicating that the delete attempt failed.
## Next steps

This document provided an overview of how to manage data usage policies in Experience Platform UI. For steps on how to manage policies using the Policy Service API, see the [developer guide](/en/docs/experience-platform/data-governance/api/getting-started). For information on how to enforce data usage policies, see the [policy enforcement overview](/en/docs/experience-platform/data-governance/enforcement/overview).

The following video provides a demonstration of how to work with usage policies in the Experience Platform UI:

https://video.tv.adobe.com/v/32977?quality=12&learn=on
https://video.tv.adobe.com/vc/32977/eng.json
recommendation-more-help
