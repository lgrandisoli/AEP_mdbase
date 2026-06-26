---
title: "Create & manage approval policies approval-policies"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/test/approve/approval-policies"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:48.113233+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create & manage approval policies approval-policies

Last update: May 8, 2026
- Topics:
- [Approval](#)

CREATED FOR:

- Beginner
- User

NOTE
To create approval policies, you must have system or product administrator privileges in Adobe Experience Platform.
Learn more
Approval policies allow administrators to establish a validation process for journeys and campaigns. This system outlines specific conditions that determine whether a journey or campaign requires approval. These policies can vary in complexity. They can simply require all campaigns to be reviewed by a particular user or team, or establish criteria based on who created the campaign.

You can target approval policies using flexible criteria such as tags, campaign/journey names, channel types, or requestor information. For example, you can require approval for all objects tagged with “high-risk”, or for any campaign matching a specific naming pattern.

## Create approval policies create-policies

To create an approval policy, follow these steps:

- From the Administration menu in Journey Optimizer, access Permissions then Policies .
- Click Create in the Approval Policy tab, choose Approval Policy , and click Confirm .
- Enter a Name and Description for the policy.
- Select whether the policy will apply to Journeys or Campaigns .
- Enable the Block self-approval to prevent Journey/Campaign creators from approving their own objects.

You can now refine the conditions to specify who can initiate the approval request and who can validate it.

## Set conditions for approval policies conditions

Approval policies offer flexible targeting options to match your governance needs. You can create approval policies based on various criteria, including:

- **Campaign/Journey names**: Target specific objects by name
- **Tags**: Apply policies to all campaigns or journeys with a specific tag
- **Channel types**: Require approval for specific actions (email, SMS, push, etc.)
- **Campaign types**: Set different rules for [Action vs. API-triggered campaigns](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns#campaign-types)
- **Requestors**: Define policies based on who creates the campaign or journey

To define the conditions associated with an approval policy, follow these steps:

- Access your Approval policy .
- Under the If menu, click Add condition to define which object or user will trigger an approval request.
- Choose the appropriate Category , Matching Rule , and Options . For example, “if Action matches any Direct Mail” or “If Requestor Username matches John Doe.” accordion Learn more about available categories and options table 0-row-2 1-row-2 2-row-1 3-row-1 4-row-2 5-row-1 6-row-1 7-row-1 8-row-1 9-row-1 10-row-1 11-row-1 12-row-2 13-row-2 14-row-2 15-row-2 4-rowspan-3 11-rowspan-8 html-authored Category Option Campaign type Scheduled (Marketing) API-triggered (Marketing) API-triggered (Transactional) Action In-app Push notification SMS Email Direct mail Web Code-based Content card Tags Name of the tag used to organize your audiences. Object name Name of your object. Requestor username Name and email address of designated requestor Requestor user group Name of the user group of designated requestors
- To add more criteria, click Add condition to define additional rules and select either And or Or to specify how the conditions are connected.
- Under the Then, send approval request to menu, click Add condition to define which user can accept the approval request.
- From the Category drop-down, select whether you want to choose a User Group or an individual User.
- Then, from the Option drop-down, select the specific user group or user. The selected user or user group will be responsible for validating the approval request.
- To add more criteria, click Add condition to define additional rules and select either And or Or to specify how the conditions are connected.
- Once your policy is fully configured, click Save .

You can now activate your approval policy to apply it.

## Activate and manage approval policies activate-policies

To apply your approval policy, you must activate it. To perform this, follow these steps:

- Access your Approval policy .
- Then, click Activate to apply the configured conditions to your environment. note NOTE Once activated, policies cannot be edited. To modify conditions, deactivate the policy first.
- From the Policy menu, open the advanced options to Edit , Deactivate , or Duplicate the policy as needed.

recommendation-more-help
