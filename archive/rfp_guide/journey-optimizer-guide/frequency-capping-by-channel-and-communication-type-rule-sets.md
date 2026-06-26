---
title: "Frequency capping by channel and communication type rule-sets"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/channel-capping"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:36.072437+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Frequency capping by channel and communication type rule-sets

Last update: May 8, 2026
- Topics:
- [Rules](#)

CREATED FOR:

- Intermediate
- User

**Channel** rule sets apply capping rules to communication channels. For example, do not send more than 1 email or SMS communication per day.

Leveraging channel rule sets allows you to set frequency capping by communication type to prevent overloading customers with similar messages. For example, you can create a rule set to limit the number of **promotional communications** sent to your customers and another rule set to limit the number of **newsletters** sent to them. Depending on the type of campaign that you are creating, you can then choose to apply either the promotional communication or the newsletters rule set.

IMPORTANT
To ensure channel level capping works correctly, make sure you choose the highest priority namespace while authoring a campaign or journey. Learn more about namespace priority in the
Platform Identity Service guide
## Create a channel capping rule

To create a channel rule set, follow these steps :

NOTE
You can create up to 10 active local rule sets for each channel domain and for the journey domain.
- Access the Rules sets list, then click Create rule set .
- Select the rule set where you want to add the capping rule, or create a new rule set: To use an existing rule set, select it from the list. Channel capping rules can only be added to rule sets with the “channel” domain. You can check this information in the rule sets lists, in the Domain column. To create the capping rule inside a new rule set, click Create rule set , specify a unique name for the rule set and select “Channel” from the Rule Set Domain drop-down, then click Save .
- In the rule set screen, click the Add Rule button and define a unique name for the rule.
- The Category field specifies the category of message the rule applies to. For now, this field is read-only as only the Marketing category is available.
- In the Capping count field, set the capping for your rule, meaning the maximum number of messages that can be sent to an individual user profile each month, week or day or hour - according to your selection in the following fields.
- From the Reset capping frequency drop-down list, select if you want the capping to be applied hourly, daily, weekly or monthly. Frequency cap is based on the selected calendar period. It is reset at the beginning of the corresponding time frame. The expiry of the counter for each period is as follows: Hourly - The frequency cap is valid for the selected number of hours. The counter automatically resets at the beginning of each time window. For a 1-hour frequency cap, it resets every hour, coinciding with the end of a UTC hour. Daily - The daily frequency cap is valid for the day until 23:59:59 UTC and resets to 0 at the start of the next day. Weekly - The frequency cap is valid until Saturday 23:59:59 UTC of that week. The expiry date applies regardless of when the rule was created. For example, if the rule is created on Thursday, this rule is valid until Saturday at 23:59:59. Monthly - The frequency cap is valid until the last day of the month at 23:59:59 UTC. For example, the monthly expiration for January is 01-31 23:59:59 UTC. note important IMPORTANT To ensure accuracy, make sure you choose the highest priority namespace while authoring a campaign or journey. Learn more about namespace priority in the Platform Identity Service guide The profile counter value updates once the communication is delivered. Please be cognizant of this when you are sending large volumes of communications as the throughput could result in the recipient getting the email minutes or even hours after the initiation of the communication (in the case that you are sending millions of communications simultaneously). This matters in the case that a recipient receives two communications close together. We suggest spacing communications apart by at least two hours where possible to give sufficient time for the recipient to receive the communication and the counter value to update accordingly.
- The Every field allows you to repeat the frequency capping rules over multiple hours, days, weeks, or months, depending on the specified duration. Example: apply the frequency capping rule for 2 weeks. Make sure you enter a value that matches the selected duration type: 1-23 for Hourly, 1-30 for Daily, 1-4 for Weekly, and 1-3 for Monthly. The counter automatically resets to 0 when a new time window begins. For a 2-day frequency cap, this reset occurs every two days at midnight UTC.
- Select the channel(s) you want to use for this rule: Email , SMS , Push notification , Direct mail or WhatsApp . Select several channels if you want to apply capping across all selected channels as a total count. For example, set capping to 5, and select both the Email and SMS channels. If a profile has already received 3 marketing emails and 2 marketing SMS messages for the selected period, this profile will be excluded from the very next delivery of any marketing email or SMS message.
- Click Save to confirm the rule creation. Your message is added to the rule set, with the Draft status.
- Repeat the steps above to add as many rules as needed to the rule set.
- When the capping rule is ready to be applied to messages, activate the rule set and the rule where it has been added. Learn how to activate rule sets

## Apply rule sets to a message apply-frequency-rule

To apply a rule set to a message, follow these steps:

- When creating a journey or campaign message, select one of the channels you defined for your rule set and edit the content of your message
- In the content edition screen, click the Add Business Rule button.
- Select the rule set you created. note NOTE Only activated rule sets display in the list.Messages where the category selected is **Transactional** will not be evaluated against business rules.
- Before activating your journey or campaign, make sure you schedule its execution at least 10 minutes into the future. This allows for sufficient time to populate the counter values on the profile for the business rule you selected. If you activate the campaign immediately, the rule set counter values will not populate on the profiles of the recipients, and the message will not be counted toward their frequency capping rules for the custom rule sets. In addition, the capping may not work correctly for journeys and campaigns activated immediately and API triggered campaigns.
- You can view the number of profiles excluded from delivery in the Customer Journey Analytics report , and in the Live report , where frequency rules will be listed as a possible reason for users excluded from delivery.

NOTE
Several rules can apply to the same channel, but once the lower cap is reached, the profile will be excluded from the next deliveries.
When testing frequency rules, it is recommended to use a newly created [test profile](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles), because once a profile’s frequency cap is reached, there is no way to reset the counter until the next period. Deactivating a rule will allow capped profiles to receive messages, but it will not remove or delete any counter increments.

CAUTION
Frequency capping rules also apply when sending
proofs
. If a test profile has already reached the frequency cap limit, proofs will show as finished but no email will be delivered.
## How-to video video

https://video.tv.adobe.com/v/3435531?quality=12&learn=on
recommendation-more-help
