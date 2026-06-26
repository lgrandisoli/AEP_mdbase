---
title: "Journey capping & arbitration journey-capping"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/journey-capping"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:35.462117+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Journey capping & arbitration journey-capping

Last update: May 8, 2026
CREATED FOR:

- Beginner
- User

Journey capping helps you limit the number of journeys a profile can be enrolled in, preventing communication overload. In Journey Optimizer, you can set two types of capping rules:

- **Entry capping** limits the number of journey entries over a given period for a profile.
- **Concurrency capping** limits how many journeys a profile can be enrolled in simultaneously.

Both types of journey capping leverage priority scores to arbitrate entries.

➡️ [Discover this feature in video](#video)

## Create a journey capping rule create-rule

To create a journey capping rule, follow these steps:

- Navigate to the Business rules menu to access the rule sets inventory.
- Select the rule set where you want to add the capping rule, or create a new rule set: To use an existing rule set, select it from the list. Journey capping rules can only be added to rule sets with the “journey” domain. You can check this information in the rule sets lists, in the Domain column. To create the capping rule inside a new rule set, click Create rule set , specify a unique name for the rule set and select “Journey” from the Rule Set Domain drop-down, then click Save .
- In the rule set screen, click the Add Rule button then provide a unique name for the rule.
- In the Rule Type drop-down list, specify the type of capping for the rule. Journey Entry Cap : Limits the number of entries into the journey over a given period for a profile. Journey Concurrency Cap : Limits how many journeys a profile can be enrolled in simultaneously.
- Expand the sections below to learn how to configure each type of capping: accordion Configure a journey entry capping rule In the Capping field, set the maximum number of journeys a profile can enter. In the Duration field, define the time period to consider. Please note, that the duration is based on the UTC time zone. For example, the Daily cap will reset at midnight UTC. In this example, we want to restrict profiles from entering more than “5” journeys in a month. note NOTE The system will take into consideration the priority of upcoming scheduled journeys that have this same rule applied to it. In this example, if the marketer has already entered 4 journeys and there is another upcoming scheduled journey this month with a higher priority, then the customers will be suppressed from entering into the lower priority journey. accordion Configure a journey concurrency capping rule In the Capping field, set the maximum number of journeys a profile can be enrolled in simultaneously. Use the Prioritization look ahead field to arbitrate journey entries based on priority scores over a chosen period (e.g., 1 day, 7 days, 30 days). This option scans the upcoming scheduled Read-Audience journeys for the remainder of the week to determine if the profile should be suppressed from entering the journey due to a higher-priority journey coming up. It helps prioritize entry into higher-value journeys if a profile is eligible to multiple journeys. In this example, we want to restrict profiles from entering the journey if they are already enrolled into another journey containing the same rule set. If another journey within the next 7 days has a higher priority score, the profile will not enter this journey. {width="50%"}
- Repeat the steps above to add as many rules as needed to the rule set.
- When the capping rule is ready to be applied to journeys, activate the rule and the rule set where it has been added. Learn how to activate rule sets

## Apply capping rules to journeys apply-capping

To apply a capping rule to a journey, access the journey and open its properties. In the **Capping rules** drop-down, select the relevant rule set. Once the journey is activated, the capping rules defined in the rule set will take effect.

NOTE
If a journey is activated immediately, it can take up to 10 minutes for the system to begin suppressing customers. As a result, a message displays if you try to publish a journey with a start time thatis less than 10 minutes.
## Monitor rule set exclusions monitor

Once a journey is live, you can check in the journey report if the rule set has led to any exclusion from the journey, in the **Journey Exclusions** table. The Journey Exclusions table includes detailed breakdowns of exclusions by rule set and rule name, providing insights into why profiles were discarded. [Learn how to work with journey reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja)

In addition, you can use the [Adobe Experience Platform Query Service](/en/docs/experience-platform/query/api/getting-started#_blank) to build queries to identify which rule caused a profile to not enter into a given journey. Query examples, including the discard sub-reason (CAP_REACHED or LOWER_PRIORITY), are available in [this section](/en/docs/journey-optimizer/using/reporting/reports/query-examples#business-rules-queries).

## How-to video video

https://video.tv.adobe.com/v/3435530?quality=12&learn=on
recommendation-more-help
