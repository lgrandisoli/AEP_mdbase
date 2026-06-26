---
title: "Journey properties attributes journey-properties"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/journey-properties"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:00.501104+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Journey properties attributes journey-properties

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)

CREATED FOR:

- Experienced
- Developer

In the [simple expression editor](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions#about_condition), and in the [advanced expression editor](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced), below the **Event** and **Data source** categories, you can access the **Journey Properties** category. This category contains technical fields related to the journey for a given profile. This is the information retrieved by the system from live journeys, such as the journey ID, or the specific errors encountered.

It contains information, for example, about:

- journey version: journey uid, journey version uid, instance uid, etc.
- errors: data fetch, action execution, etc.
- current step, last current step, etc.
- discarded profiles The list of fields is available in this section .

You can use these fields to build expressions. During the journey execution, the values are retrieved directly from the journey.

Below are a few examples of use cases:

- Log discarded profiles : you can send all profiles excluded from a message by a capping rule to a third-party system for logging purposes. For this, you set up a path in case of timeout and error and add a condition to filter on a specific error type, for example: “discard people by capping rule”. You can then push the discarded profiles to a third-party system via a custom action.
- Send alerts in case of errors : you can send a notification to a third-party system every time an error occurs on a message. For this, you set up a path in case of error, add a condition and a custom action. You can send a notification on a Slack channel, for example, with the description of the error encountered.
- Refine errors in reporting : instead of having just one path for messages in error, you can define a condition per error type. This will allow you to refine the reporting and view all error types data.

## List of fields journey-properties-fields

Category
Field name
Label
Description
Journey Version
journeyUID
Journey Identifier
journeyVersionUID
Journey Version Identifier
journeyVersionName
Journey Version Name
journeyVersionDescription
Journey Version Description
journeyVersion
Journey Version
Journey Instance
instanceUID
Journey Instance Identifier
ID of the instance
externalKey
External Key
Individual identifier triggering the journey
organizationId
Organization identifier
Brand’s organization
sandboxName
Sandbox name
Name of the sandbox
Identity
profileId
Profile Identity Identifier
Identifier of the profile in the journey
namespace
Profile Identity Namespace
Namespace of the profile in the journey (example: ECID)
Current Node
currentNodeId
Current Node Identifier
Identifier of the current activity (node)
currentNodeName
Current Node Name
Name of the current activity (node)
Previous Node
previousNodeId
Previous Node Identifier
Identifier of the previous activity (node)
previousNodeName
Previous Node Name
Name of the previous activity (node)
Errors
lastNodeUIDInError
Last Node Identifier in Error
Identifier of the latest activity (node) in error
lastNodeNameInError
Last Node Name in Error
Name of the latest activity (node) in error
lastNodeTypeInError
Last Node Type in Error
Error type of the latest activity (node) in error. Possible types:

- Events: Events, Reactions, SQ (example: Audience Qualification)
- Flow control: End, Condition, Wait
- Actions: ACS actions, Jump, Custom Action

lastErrorCode
Last Error Code
Error code of the latest activity (node) in error. Possible errors:

- HTTP error codes
- capped
- timedOut
- error (example: default in case of an unexpected error. Should not/extremely rarely happen)

lastExecutedActionErrorCode
Last Executed Action Error Code
Error code of the latest action in error
lastDataFetchErrorCode
Last Data Fetch Error Code
Error code of the latest data fetch from data sources
Time
lastActionExecutionElapsedTime
Last action execution elapsed time
Time spent to execute the latest action
lastDataFetchElapsedTime
Last data fetch elapsed time
Time spent to execute the latest data fetch from data sources
recommendation-more-help
