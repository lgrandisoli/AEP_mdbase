---
title: "Work with rule sets rule-sets"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/rule-sets"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:36.683670+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with rule sets rule-sets

Last update: May 8, 2026
- Topics:
- [Rules](#)

CREATED FOR:

- Intermediate
- User

## Get started with rule sets gs

### What are rule sets? what

Rule sets allow you to **group together multiple rules into rule sets** and apply them to the journeys and campaigns of your choice. This provides improved granularity to limit how often and how many journeys a customer can enter within a certain time frame or control how often users will receive a message depending on the type of communication.

You can create two types of rule sets:

- Channel rule sets apply rules to communication channels. They allow you to set: Frequency capping rules - Do not send more than 1 Email, SMS, Push, Direct mail, or WhatsApp communication per day. Quiet hours rules - Do not send email messages outside of the 8AM - 9PM timeslot.
- Journey rule sets apply entry and concurrency capping rules to a journey. For example, do not enter profiles into more than one journey simultaneously.

➡️ [Discover this feature in video](#video)

### Permissions permissions-frequency-rules

To work with business rules, you need the following permissions:

- **View Frequency Rules**: Access and view business rules.
- **Manage Frequency Rules**: Create, edit or delete business rules.

Learn more about permissions in [this section](/en/docs/journey-optimizer/using/access-control/high-low-permissions).

### Global & custom rule sets global-custom

When accessing rule sets for the first time from the **Administration** > **Business rules** menu, a default rule set is pre-created and active: **Global Default Rule Set**.

This rule set contains global rules that you can apply to control how often users receive messages across one or multiple channels. All the rules defined in this rule set apply to all selected channels, whether communications are sent from a journey or a campaign.

In addition to this “Global Default Rule Set” rule set, you can create **rule sets** that you can apply to any journey or campaign to apply specific capping rules. [Learn how to create custom rule sets](#create)

## Create and activate rule sets Create

To create a rule set, follow the steps below.

NOTE
You can create up to 10 rule sets for the channel domain and 10 rule sets for the journey domain, for a total of 20 rule sets.
- Access the Rules sets list, then click Create rule set .
- Define a unique name for the rule set and add a description.
- Select the rule set’s domain and click Save . Channel domain: apply capping rules or quiet hours rules to communication channels. Journey domain: apply entry and concurrency capping rules to a journey.
- Define the rules you want to add to this rule set. To do so, access the rule set and click Add rule .
- Configure the rule parameters to suit your needs. The parameters available for the rule depend on the rule set domain selected at its creation. Detailed information on how to configure journey and channel rules is available in these sections: Journey capping Frequency capping by channel and communication type Quiet hours
- Click Save to confirm the rule creation. Your message is added to the rule set, with the Draft status.
- Repeat the steps above to add as many rules as needed to the rule set.
- When created, a rule has the Draft status and is not yet impacting any message. To enable it, click the More actions button next to the rule and select Activate .
- Activate the rule set to be able to apply it to your journeys and messages. note NOTE It can take up to 10 minutes for a rule or rule set to be fully activated. You do not need to modify messages or republish journeys for a rule to take effect.

- You can apply a rule set to a message or a journey, depending on the domain selected when creating the rule set. Detailed information on how to apply rule set is available in these sections: Apply a rule set to a journey Apply capping rules to journey and campaign actions Apply quiet hours rules to journey and campaign

## Access & manage rule sets access-rule-sets

All created rule sets display in the **Administration** > **Business rules** menu. They are sorted by last modification date.

Click a rule set name to view and edit its content. All rules included in that rule set are listed. The contextual menu on top right enables you to edit the name and description of the rule set, activate it, and delete it.

For each rule in the rule set, the **More actions** button enables you to edit the rule, activate it and delete it.

To deactivate a rule or a rule set, click the **More actions** button next to the desired item and select **Deactivate**.

Its status will change to **Inactive** and the rule will not apply to future message executions. Any messages currently in execution will not be affected.

NOTE
Deactivating a rule or rule set does not affect or reset any counts on individual profiles.
## How-to video video

https://video.tv.adobe.com/v/3435531?quality=12&learn=on
recommendation-more-help
