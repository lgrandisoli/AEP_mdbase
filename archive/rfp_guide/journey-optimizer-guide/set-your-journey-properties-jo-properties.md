---
title: "Set your journey properties jo-properties"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:46.655905+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Set your journey properties jo-properties

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Get Started](#)

CREATED FOR:

- Intermediate
- User

Use journey properties to configure global settings for your journey, including its name, entrance rules, timezone, start and end dates, timeout duration, exit criteria, and conflict management. Properties are accessible from the right rail at any stage of journey authoring.

## Access the properties of a journey access-properties

The properties of a journey are centralized in the right rail. This section is displayed by default when creating a new journey. For existing journeys, click the pencil icon next to the journey’s name to open it.

From this section, define the name of the journey, add a description, and set your journey global properties.

You can:

- Assign Adobe Experience Platform Unified Tags to your journey, to easily classify them and improve search from the campaigns list. [Learn how to work with tags](/en/docs/journey-optimizer/using/get-started/work-efficiently/search-filter-categorize#tags)
- Select your journey metrics. [Learn how to configure and track your journey metrics](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/success-metrics)
- Manage [entrance and reentrance](#entrance). Profile entrance management depends on the type of journey. Details are available on [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management)
- Manage [access to data](#manage-access)
- Select the journey and profile [timezones](#timezone)
- Choose custom [start and end dates](#dates)
- Define a [timeout duration](#timeout) in journey activities (for Admin users only)
- Monitor the [current journey payload size](#journey-payload-size) to avoid publishing errors
- Monitor conflicts and prioritize your journeys using [conflict management tools](#conflict)

{width="80%" modal="regular"}

NOTE
For live journeys, this screen displays only the publication date and the name of the user who published the journey.
The **Copy technical details** option allows you to copy technical information about the journey which the support team can use to troubleshoot. The following information is copied:

**General**

- JourneyVersion UID – Unique identifier of this version of the journey
- OrgID – Your organization’s (IMS) identifier
- orgName – Your organization’s name
- sandboxName – Name of the sandbox where the journey runs
- lastDeployedBy – User who last published the journey
- lastDeployedAt – Date and time of the last publication

**Pause and resume** (included when the journey has been paused at least once)

- lastPausedAt – Date and time of the last time the journey was paused
- lastPausedBy – Display name of the user who performed the last pause
- lastPausedById – Internal identifier of the user who performed the last pause
- lastResumedAt – Date and time of the last time the journey was resumed
- lastResumedBy – Display name of the user who performed the last resume
- lastResumedById – Internal identifier of the user who performed the last resume

**Paused journey settings** (in pausedJourneySettings, when the journey is or has been paused)

- pauseBehavior – What happens to profiles in the journey when it is paused (for example, discard them or keep them in place)
- maxPauseDurationInMinutes – Maximum pause duration in minutes, after which the journey auto-resumes (for example, 20160 = 14 days)
- transitionStateForAutoResume – State applied when the journey auto-resumes at the end of the pause period (for example, stop or continue)
- pauseId – Unique identifier for the current pause instance

Learn more about technical fields related to a journey for a given profile, and how to use them [on this page](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/journey-properties).

## Entrance and reentrance entrance

The profile entry mode is defined at the journey level, in the right configuration pane. Settings are described below.

Profile entrance management depends on the type of journey. Learn more about profile entrance and reentrance management, on [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management). Learn more about journey processing rates and how profiles flow through journeys in [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management#journey-processing-rate).

### Allow reentrance allow-reentrance

By default, new journeys allow reentrance. You can uncheck the **Allow reentrance** option for “one shot” journeys, for example if you want to offer a one-time gift when a person enters a shop.

### Reentrance wait period reentrance-wait

When the **Allow reentrance** option is activated, the **Reentrance wait period** field is displayed. This field allows you to define the time to wait before allowing a profile to enter the journey again in unitary journeys (starting with an event or an audience qualification). This prevents journeys from being erroneously triggered multiple times for the same event. By default the field is set to 5 minutes. The maximum duration is 90 days.

## Manage access manage-access

You can limit access to a journey based on access labels.

To assign custom data usage labels to the journey, click the **Manage access labels** icon and select one or several labels.

[Learn more about Object Level Access Control (OLAC)](/en/docs/journey-optimizer/using/access-control/object-based-access)

## Journey payload size journey-payload-size

The **Current journey payload size** field in the journey properties panel displays the current size of your journey’s payload in relation to the configured limit — for example, *1.5 MB (out of 2 MB)*. This read-only indicator is visible at any stage of journey authoring.

{width="50%" modal="regular"}

Use this information to monitor the complexity of your journey before publishing. If the payload size approaches or exceeds the limit, journey publication fails. To reduce the size, consider simplifying the journey logic or reducing the number of activities.

The default limit is 4 MB. Contact Adobe Customer Care if you need to request a higher limit for your organization.

For full details on thresholds, warning and error messages, and troubleshooting steps, refer to [Journey payload size validation](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#journey-payload-size) and [General journey guardrails](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#journeys-guardrails-journeys).

## Journey and profile timezones timezone

The timezone is defined at journey level. You can enter a fixed time zone or use Adobe Experience Platform profiles to define the journey time zone. If a time zone is defined in Adobe Experience Platform profile, it can be retrieved in the journey.

[Learn more about timezone management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management)

## Start and end dates dates

By default, profiles can enter your journey as soon as it is published, and can stay until the [global journey timeout](#global_timeout) is reached. The only exception is recurring read audience journeys with **Force reentrance on recurrence** activated, which end at the start date of the next occurrence.

If needed, you can define custom **Start date** and **End date**. This allows profiles to enter your journey on a specific date, and exit automatically when the end date is reached.

## Timeout timeout

Timeout settings control how long a journey waits for activity execution and how long profiles can remain in a journey.

### Timeout in journey activities timeout_and_error

When editing an action or condition activity, you can define an alternative path in case of error or timeout. If the processing of the activity interrogating a third-party system exceeds the timeout duration defined in **Timeout or error** field of the journey’s properties, the second path will be chosen to perform a potential fallback action.

Recommended values are between 1 and 30 seconds.

We recommend that you define a very short **Timeout or error** value if your journey is time sensitive (example: reacting to the real-time location of a person) because you cannot delay your action for more than a few seconds. If your journey is less time sensitive, you can use a longer value to give more time to the system called to send a valid response.

Journeys also uses a global timeout as detailed below.

### Global journey timeout global_timeout

In addition to the [timeout](#timeout_and_error) used in journey activities, a global journey timeout is applied. It is not displayed in the interface and cannot be changed.

This global timeout stops the progress of individuals in the journey **91 days** after they enter. This means that an individual’s journey cannot last longer than 91 days. After this timeout period, the individual’s data is deleted. Individuals still flowing in the journey at the end of the timeout period will be stopped and they will not be taken into account in reporting. You could therefore see more people entering the journey than exiting.

NOTE
The exact definition of when a journey is considered “finished” varies by journey type.
See detailed criteria
.
Due to the 91-day journey timeout, when journey reentrance is not allowed, we cannot make sure the reentrance blocking will work more than 91 days. Indeed, as we remove all information about persons who entered the journey 91 days after they enter, we cannot know the person entered previously, more than 91 days ago.

An individual can enter a wait activity only if he or she has enough time left in the journey to complete the wait duration before the 91 days journey timeout. See [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity).

### Time-to-Live (TTL) and data retention FAQ timeout-faq

Starting Adobe Journey Optimizer June 2024 release, the journey global timeout has moved from 30 to 91 days. Impacts are listed in the FAQ below:

**For Unitary Journeys**

What happens to journey published after the TTL extension rolled out?
Profiles entering the new journey will automatically have a TTL of 91 days.
What happens to a profile entering a journey that was published before the TTL extension launch?
The profile will have a TTL of 30 days (7 days for HIPAA), consistent with the time the journey was originally published.
What happens to a profile which have already entered a journey when the TTL extension is launched?
The profile will retain a TTL of 30 days (7 days for HIPAA), as per the original publication time of the journey.
What happens to a profile in a previous journey version that is republished after the TTL extension launch?
The profile will maintain a TTL of 30 days (7 days for HIPAA), aligned with the original journey version's publication time.
What happens to a new profile entering a republished journey version after the TTL extension launch?
The profile will have a TTL of 91 days, matching the TTL of the newly republished journey version.
**For Segment Trigger Journeys**

What happens to new one-time journeys published after the TTL extension?
Profiles entering the new journey will have a TTL of 91 days automatically.
What happens to new recurring journeys without forced reentrance published after the TTL extension?
Profiles entering the new journey will have a TTL of 91 days automatically.
What happens to new recurring journeys with forced reentrance published after the TTL extension?
Profiles entering the new journey will have a TTL equal to the recurrence period. For example, if the journey runs daily, the TTL will be 1 day.
What happens to a profile entering a journey that was published before the TTL extension launch?
The profile will have a TTL of 30 days (7 days for HIPAA), consistent with the original publication time. For recurring journeys with forced reentrance, the TTL will match the recurrence period.
What happens to a profile running through a journey when the TTL extension is launched?
The profile will retain a TTL of 30 days (7 days for HIPAA), as per the original publication time of the journey. For recurring journeys with forced reentrance, the TTL will match the recurrence period.
What happens to a running profile in a previous journey version that is republished after the TTL extension launch?
The profile will maintain a TTL of 30 days (7 days for HIPAA), aligned with the original journey version's publication time. For recurring journeys with forced reentrance, the TTL will match the recurrence period.
What happens to a new profile entering a republished journey version after the TTL extension launch?
The profile will have a TTL of 91 days, matching the TTL of the newly republished journey version. For recurring journeys with forced reentrance, the TTL will match the recurrence period.
Will my always-on recurring Read Audience journey stop after 91 days?
No. A recurring Read Audience journey with no end date remains
Live
as long as it is published. It moves to
Finished
status only 91 days after the execution of its
last occurrence
. The 91-day global timeout applies to individual profiles flowing through the journey (maximum active duration per profile), not to the journey's Live status.
What is the difference between the 91-day journey timeout and the 91-day reporting window?
These are two separate concepts. The
journey global timeout
(91 days) is the maximum time an individual profile can remain active within a journey — after 91 days, the profile is exited and its data deleted. The
reporting window
(approximately 91 days) is a display limit in the UI: performance data older than ~91 days is no longer visible in reporting, but the journey itself continues to run and new profiles continue to enter.
## Merge policy merge-policies

Adobe Journey Optimizer uses merge policies while retrieving profile data from Adobe Experience Platform. Depending on the journey type, different merge policies are used:

- In **Read audience** or **Audience qualification** journeys: the merge policy from the audience is used
- In **Unitary event** journeys: the default merge policy is used
- In **Business event** journeys: the merge policy from the targeted audience in the following Read audience activity is used

Adobe Journey Optimizer applies the merge policy used throughout the entire journey. Therefore, if multiple audiences are used in a journey (for example using the in [inAudience functions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/functioninaudience)), this creates inconsistencies with the merge policy used by the journey, an error is raised and publication is blocked. However, if an inconsistent audience is used in message personalization, an alert is not raised, despite the inconsistency. For this reason, it is highly recommended to check the merge policy associated with your audience, when this audience is used in message personalization.

To learn more about merge policies, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/profile/merge-policies/overview#_blank).

NOTE
When an audience merge policy is updated, any active journey referencing that audience must be republished (or duplicated). Changing the merge policy effectively creates a ‘new’ audience that the ongoing journey cannot access, ensuring data consistency.
## Exit criteria exit-criteria

### Journey Exit criteria exit-criteria-desc

By adding exit criteria, you make the profiles exit the journey as soon as an event happens (e.g., Purchase) or they qualify for an audience. This will prevent the user from getting any further communications from the journey.

You may want to remove profiles from a journey when they do not meet the journey’s purpose anymore. This can be achieved by **global exit criteria**, which are closely associated with goal management.

TIP
Looking for practical guidance with real-world examples? See our
comprehensive guide to journey entry and exit criteria
, which includes complete use cases with both entry and exit configurations, best practices, and optimization strategies.
**Sample use case**

A marketer has a promotional journey that has a series of communications. Each of this communication is aimed at driving the customer to make a purchase. As soon as the purchase is made the customer should not receive rest of the messages in the series. By defining an exit criteria, any profiles who made a purchase is removed from the journey.

### Configuration and usage exit-criteria-config

Exit criteria are set at journey level. One journey can have multiple exit criteria. If you have set multiple exit criteria, the evaluation happens from top to bottom with an OR logic. Hence, if you have Exit Criteria A and Exit Criteria B, it is evaluated as A **OR** B. The criteria are evaluated at every step of the journey.

To **create** an exit criteria, follow these steps:

- Open your journey.
- Click the Show Exit Criteria icon located in the upper-right section of the journey canvas.
- Select Add exit criteria .
- Enter a Label and select if your exit criteria is based on an Event or an Audience . For Exit criteria based on an event, like for example downloading an app or adding a product to a cart, pick only unitary event. For Exit criteria based on an audience,like for example an audience that checks if a customer has purchased in the last 24 hours, select an audience. Note: Exit criteria using an audience can take up to 10 mins to be effective.

You can add multiple exit criteria. The exit criteria is now active and will be evaluated at each step of the journey.

{align="left" width="40%"}

### Profile Attribute-based exit criteria profile-exit-criteria

Profile Attribute–Based Exit Criteria gives you greater control over paused journeys by allowing you to define rules that automatically remove specific profiles before the journey resumes. You can set exit conditions based on profile attributes—such as location, status, or preferences—to ensure that only relevant profiles continue in the journey after it is resumed.

For example, you can [pause a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-pause), add an exit condition to remove all profiles located in France, and resume the journey knowing that those profiles will be excluded at the next action step. This logic applies both to profiles already in the journey and to any new profiles that qualify after the journey resumes.

This feature works alongside the Pause/Resume functionality, helping you manage journeys more safely and flexibly. It minimizes manual intervention, reduces the risk of sending irrelevant or non-compliant communications, and keeps your journey logic aligned with current business requirements.

Refer to this section to learn how to [use profile attribute exit criteria in paused journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-pause#journey-pause-sample).

### Guardrails and limitations exit-criteria-guardrails

The following guardrails and limitations apply to the [Journey Exit Criteria](#exit-criteria-desc) capability:

- Exit criteria are defined in draft state only
- Journey namespace coherence between events and event-based exit criteria

The following guardrails apply when using the [Profile Attribute–Based Exit Criteria](#profile-exit-criteria) capability:

- Exit criteria apply at the action level The “Profile Attribute” exit criteria are evaluated at action steps only. Unlike other exit criteria types, they do not apply globally across the journey. If you resume a journey and some profiles meet the exit condition, those profiles will be excluded at the next action node. New profiles entering the journey after resume will also be evaluated and excluded at their first action node, if they meet the condition.
- One profile-based exit rule per journey You can define only one “Profile Attribute” exit criteria per journey. This limitation helps maintain clarity and avoids conflicts in journey logic.
- Available in paused journeys only You can add or edit “Profile Attribute” exit criteria only when the journey is paused. In a draft journey , the Profile Attribute option appears disabled (read-only), while Event and Audience options remain active. In a paused journey , the Profile Attribute option becomes editable, and Event and Audience options become read-only.

### Related topics exit-criteria-related

- [Journey entry and exit criteria guide](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/entry-exit-criteria-guide) - Complete guide with real-world examples and best practices
- [Profile entrance management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management) - Configure how profiles enter journeys
- [How journeys end](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey) - Understand natural journey completion
- [Pause a journey with profile attribute exit criteria](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-pause#journey-exit-criteria) - Use exit criteria when pausing journeys

## Journey schedule schedule

The **Schedule** section is only available when a **Read Audience** activity has been dropped in the canvas. It allows you to define a specific date/time and frequency at which the journey should run. [Learn how to schedule a Read-audience journey](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience#schedule)

TIP
When scheduling the journey, you can also configure wave sending to deliver journey actions in batches over time.
Learn how to send using waves in journeys
## Conflict management conflict

The **Conflict management** section in the journey’s properties allows you to monitor conflicts and prioritize your journeys. You can:

- Apply a Rule Set to exclude this journey to part of your audience based on capping rules. Learn how to work with rule sets
- Assign a priority score to the journey, ranging from 0 to 100. A higher number indicates a higher priority. The priority value inserted here is inherited by any inbound actions (such as In-App) contained in this journey. learn how to work with priority scores For situations where this same inbound channel configuration is used in other campaigns or journeys, the inbound action with the highest priority score is shown to the recipient. If multiple journeys or campaigns have the same score, the element that was most recently modified is chosen.
- View conflicts with other journeys, campaigns, or channel configurations. If you wish to identify overlap on audience, start & end date, channel configuration, channel, or rule set you can view potential conflicts here. Learn how to identify potential conflicts in journey

## Related topics related-topics

- [Profile entrance management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management) - Configure how profiles enter and re-enter journeys
- [Journey entry and exit criteria guide](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/entry-exit-criteria-guide) - Complete guide with real-world examples and best practices
- [How journeys end](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey) - Understand natural journey completion and profile exit
- [Pause a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-pause) - Pause and resume journeys with profile attribute exit criteria
- [Timezone management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management) - Configure journey and profile timezones
- [Conflict management and prioritization](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts) - Identify and resolve conflicts across journeys and campaigns

recommendation-more-help
