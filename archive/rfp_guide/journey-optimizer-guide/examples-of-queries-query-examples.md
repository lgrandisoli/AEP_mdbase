---
title: "Examples of queries query-examples"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/reporting/reports/query-examples"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:10.619243+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Examples of queries query-examples

Last update: May 8, 2026
- Topics:
- [Reporting](#)
- [Journeys](#)

CREATED FOR:

- Experienced
- Developer
- Admin

This section provides commonly used examples to query Journey Step Events in Data Lake. Before diving into specific use cases, it’s important to understand the key identifiers used in journey event data.

## Prerequisites prerequisites

Before running any query on this page, ensure the following:

- **Access to Adobe Experience Platform Query Service** — You must have access to [Query Service](/en/docs/experience-platform/query/home#_blank) in your Adobe Experience Platform sandbox.
- **Dataset available** — Queries target the journey_step_events dataset. Verify the dataset exists and contains data in your sandbox via **Experience Platform > Datasets**.
- **Correct journey version ID** — Most queries require a journeyVersionID. Find it in Journey Optimizer under **Journeys > [your journey] > Properties**, or use journeyVersionName to locate it in the dataset first.
- **Schema field values** — Make sure that the fields used in your queries have associated values in the corresponding schema. Empty fields return no results without errors.

TIP
New to Query Service?
Open
Adobe Experience Platform
, navigate to
Query Service > Queries
, paste any example below, replace the placeholder values (e.g.
<journeyVersionID>
,
<last x hours>
), and select
Run
.
## Find the right query find-query

I want to…
Go to
Count profiles that entered a journey
Basic use cases
Debug a specific profile’s journey path
Profile-based queries
Investigate Read Audience execution or errors
Read Audience queries
Troubleshoot message or action errors
Message & Action errors
Analyze Audience Qualification discards
Audience Qualification queries
Investigate business rules discards
Business rules queries
Debug external or business events
Event-based queries
Monitor custom action endpoint performance
Custom Action queries
Track Engageable Profiles and license usage
Engageable Profiles queries
Make sure that the fields used in your queries have associated values in the corresponding schema.

## Understanding key identifiers key-identifiers

What's the difference between id, instanceID and profileID
- id: unique for all the step event entries. Two different step events cannot have the same id.
- instanceID: instanceID is the same for all the step events associated to a profile within a journey execution. If a profile reenters the journey, a different instanceID will be used. This new instanceID will be same for all the step events of the reentered instance (from start to end).
- profileID: the profile’s identity corresponding to the journey namespace.

| note |
| --- |
| NOTE |
| For troubleshooting purposes, we recommend using journeyVersionID instead of journeyVersionName when querying journeys. Learn more about journey properties attributes [in this section](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/journey-properties#journey-properties-fields). |

## Basic use cases/common queries common-queries

How many profiles entered a journey in a certain time frame
This query gives the number of distinct profiles that entered the given journey in the given time frame.

*Data Lake query*

| code language-sql |
| --- |
| SELECT count(distinct _experience.journeyOrchestration.stepEvents.profileID) FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journeyVersionID>' AND _experience.journeyOrchestration.stepEvents.nodeType='start' AND _experience.journeyOrchestration.stepEvents.instanceType = 'unitary' AND DATE(timestamp) > (now() - interval '<last x hours>' hour); |

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

Which rule caused a profile to not enter into a given journey
This query returns the rejected ruleset and rule information when a profile is prevented from entering a journey due to capping or eligibility rules.

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.dispatcher.eventType, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.ID AS RULESET_ID, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.name AS RULESET_NAME, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.rejectedRules.ID AS RULE_ID, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.rejectedRules.name AS RULE_NAME FROM journey_step_events WHERE _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.stepEvents.journeyVersionID='3855072d-79c3-438a-a5c3-c77fd6843812' AND timestamp >= to_date('2025-05-16') |

Which rule caused a profile to not receive a journey action
This query returns the step event details for profiles that were discarded during a journey and did not receive a journey action. It helps identify why profiles were discarded due to business rules such as quiet hours constraints.

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.profileID, _experience.journeyOrchestration.stepEvents.instanceID, _experience.journeyOrchestration.stepEvents.journeyID, _experience.journeyOrchestration.stepEvents.journeyVersionID, _experience.journeyOrchestration.stepEvents.actionExecutionError, _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode, _experience.journeyOrchestration.serviceEvents.dispatcher.eventType, DATE(timestamp), timestamp FROM journey_step_events WHERE _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = '<eventType>' AND _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journeyVersionID>' AND _experience.journeyOrchestration.stepEvents.instanceID = '<instanceID>'; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.profileID, _experience.journeyOrchestration.stepEvents.instanceID, _experience.journeyOrchestration.stepEvents.journeyID, _experience.journeyOrchestration.stepEvents.journeyVersionID, _experience.journeyOrchestration.stepEvents.actionExecutionError, _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode, _experience.journeyOrchestration.serviceEvents.dispatcher.eventType, DATE(timestamp), timestamp FROM journey_step_events WHERE _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'quietHours' AND _experience.journeyOrchestration.stepEvents.journeyVersionID = '6f21a072-6235-4c39-9f6a-9d9f3f3b2c3a' AND _experience.journeyOrchestration.stepEvents.instanceID = 'unitary_089dc93a-1970-4875-9660-22433b18e500'; |

The query results display key fields that help identify the reason for profile discards:

- actionExecutionError - When set to businessRuleProfileDiscarded , this indicates the profile was discarded due to a business rule. The eventType field provides additional details on which specific business rule caused the discard.
- eventType - Specifies the type of business rule that caused the discard: quietHours : Profile was discarded due to quiet hours configuration forcedDiscardDueToQuietHours : Profile was forcibly discarded because guardrail limit was reached for profiles held in quiet hours

How many errors occurred on each node of a specific journey for a certain amount of time
This query counts the distinct profiles that experienced errors at each node of a journey, grouped by node name. It includes all types of action execution errors and fetch errors.

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.nodeName, count(distinct _experience.journeyOrchestration.stepEvents.profileID) FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID='<journeyVersionID>' AND DATE(timestamp) > (now() - interval '<last x hours>' hour) AND (_experience.journeyOrchestration.stepEvents.actionExecutionError is not NULL OR _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode is not NULL OR _experience.journeyOrchestration.stepEvents.actionExecutionOriginCode is not NULL OR _experience.journeyOrchestration.stepEvents.actionExecutionOriginError is not NULL OR _experience.journeyOrchestration.stepEvents.fetchError is not NULL OR _experience.journeyOrchestration.stepEvents.fetchErrorCode is not NULL ) GROUP BY _experience.journeyOrchestration.stepEvents.nodeName; |

How many events were discarded from a specific journey in a certain time frame
This query counts the total number of events that were discarded from a journey. It filters for various discard event codes including segment export job errors, dispatcher discards, and state machine discards.

*Data Lake query*

| code language-sql |
| --- |
| SELECT count(_id) AS NUMBER_OF_EVENTS_DISCARDED FROM journey_step_events WHERE ( _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode = 'error' OR _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' OR _experience.journeyOrchestration.serviceEvents.stateMachine.eventCode = 'discard' OR _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode is not null ) AND _experience.journeyOrchestration.stepEvents.journeyVersionID='<journeyVersionID>' AND DATE(timestamp) > (now() - interval '<last x hours>' hour); |

What happens to a specific profile in a specific journey in a specific time frame
This query returns all the step events and service events for the given profile and journey for the specified time in chronological order.

*Data Lake query*

| code language-sql |
| --- |
| SELECT timestamp, _experience.journeyOrchestration.stepEvents.journeyVersionID, _experience.journeyOrchestration.stepEvents.profileID, _experience.journeyOrchestration.stepEvents.nodeName, _experience.journeyOrchestration.stepEvents.journeyNodeProcessed, _experience.journeyOrchestration.serviceType, to_json(_experience.journeyOrchestration.profile), to_json(_experience.journeyOrchestration.serviceEvents) FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID='<journeyVersionID>' AND DATE(timestamp) > (now() - interval '<last x hours>' hour) AND ( _experience.journeyOrchestration.stepEvents.profileID='<profileID>' OR _experience.journeyOrchestration.profile.ID='<profileID>' ); ORDER BY timestamp; |

How much time elapsed between two nodes
These queries can be used, for example, to estimate the time spent in a wait activity. This allows you to make sure that the wait activity is correctly configured.

*Data Lake query*

| code language-sql |
| --- |
| WITH START_NODE_INFO AS ( SELECT timestamp AS TS_START, _experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, _experience.journeyOrchestration.stepEvents.instanceID AS INSTANCE_ID FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey version id>' AND _experience.journeyOrchestration.stepEvents.nodeName = '<name of node before wait activity>' AND _experience.journeyOrchestration.stepEvents.journeyNodeProcessed = true ), END_NODE_INFO AS ( SELECT timestamp AS TS_END, _experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, _experience.journeyOrchestration.stepEvents.instanceID AS INSTANCE_ID FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey version id>' AND _experience.journeyOrchestration.stepEvents.nodeName = '<name of wait activity node>' AND _experience.journeyOrchestration.stepEvents.journeyNodeProcessed = true ) SELECT T1.INSTANCE_ID AS INSTANCE_ID, T1.NODE_NAME AS START_NODE_NAME, T2.NODE_NAME AS END_NODE_NAME, DATEDIFF(millisecond,T1.TS_START,T2.TS_END) AS ELAPSED_TIME_MS FROM START_NODE_INFO AS T1, END_NODE_INFO AS T2 WHERE T1.INSTANCE_ID = T2.INSTANCE_ID |

*Data Lake query*

| code language-sql |
| --- |
| WITH START_NODE_INFO AS ( SELECT timestamp AS TS_START, _experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, _experience.journeyOrchestration.stepEvents.instanceID AS INSTANCE_ID FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey version id>' AND _experience.journeyOrchestration.stepEvents.nodeName = '<name of node before wait activity>' AND _experience.journeyOrchestration.stepEvents.journeyNodeProcessed = true ), END_NODE_INFO AS ( SELECT timestamp AS TS_END, _experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, _experience.journeyOrchestration.stepEvents.instanceID AS INSTANCE_ID FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey version id>' AND _experience.journeyOrchestration.stepEvents.nodeName = '<name of wait activity node>' AND _experience.journeyOrchestration.stepEvents.journeyNodeProcessed = true ) SELECT AVG(DATEDIFF(millisecond,T1.TS_START,T2.TS_END)) AS AVERAGE_ELAPSED_TIME, MIN(DATEDIFF(millisecond,T1.TS_START,T2.TS_END)) AS MIN_ELAPSED_TIME, MAX(DATEDIFF(millisecond,T1.TS_START,T2.TS_END)) AS MAX_ELAPSED_TIME FROM START_NODE_INFO AS T1, END_NODE_INFO AS T2 WHERE T1.INSTANCE_ID = T2.INSTANCE_ID |

How to check the details of a serviceEvent
The Journey Step Events dataset contains all the stepEvents and serviceEvents. stepEvents are used in reporting, as they relate to activities (event, actions, etc.) of profiles in a journey. serviceEvents are stored in the same dataset, and they indicate additional information for debugging purposes, for example the reason for an experience event discard.

Here is an example of query to check the detail of a serviceEvent:

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.profile.ID, _experience.journeyOrchestration.journey.versionID, to_json(_experience.journeyOrchestration.serviceEvents) FROM journey_step_event WHERE _experience.journeyOrchestration.serviceType is not null; |

## Message/Action Errors message-action-errors

List of each error encountered in journeys
This query allows you to list each error encountered in journeys while executing a message/action.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionExecutionError, count(distinct _id) AS ERROR_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.nodeName = '<message-name>' AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NOT NULL AND _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-version-id>' GROUP BY _experience.journeyOrchestration.stepEvents.actionExecutionError ORDER BY ERROR_COUNT DESC; |

*Sample output*

| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| actionExecutionError | ERROR_COUNT |
| TimedOut | 145 |
| ErrorConnecting | 87 |
| InvalidResponse | 23 |

This query returns all the different errors that occurred while executing an action in a journey along with the count of how many times each error occurred, ordered by frequency.

## Profile-based queries profile-based-queries

Find if a profile entered a specific Journey
This query checks whether a specific profile entered a journey by counting the events associated with that profile and journey combination.

| code language-sql |
| --- |
| SELECT count(distinct _id) AS EVENT_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-version-id>' AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID corresponding to the namespace used>'; |

*Sample output*

| table 0-row-1 1-row-1 |
| --- |
| EVENT_COUNT |
| 3 |

This query returns the exact number of times a profile has entered a journey. A result greater than 0 confirms that the profile entered the journey.

Find if a profile was sent a specific message
Method 1: if the name of your message is not unique in the journey (it is used at multiple places).

| code language-sql |
| --- |
| SELECT count(distinct _id) AS MESSAGE_SENT_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.nodeID = '<NodeId in the UI corresponding to the message>' AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-version-id>' AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID corresponding to the namespace used>'; |

*Sample output*

| table 0-row-1 1-row-1 |
| --- |
| MESSAGE_SENT_COUNT |
| 1 |

A result greater than 0 confirms the message action was successfully executed. This query only tells us whether the message action was successfully executed on the journey side.

Method 2: if the name of your message is unique in the journey.

| code language-sql |
| --- |
| SELECT count(distinct _id) AS MESSAGE_SENT_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.nodeName = '<NodeName in the UI corresponding to the message>' AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-version-id>' AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID corresponding to the namespace used>'; |

*Sample output*

| table 0-row-1 1-row-1 |
| --- |
| MESSAGE_SENT_COUNT |
| 1 |

The query returns the count of times the message was successfully invoked for the selected profile.

Find all the messages a profile has received in the last 30 days
This query retrieves all successfully executed message actions for a specific profile within the last 30 days, grouped by message name.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.nodeName AS MESSAGE_NAME, count(distinct _id) AS MESSAGE_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.nodeType = 'action' AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID corresponding to the namespace used>' AND timestamp > (now() - interval '30' day) GROUP BY _experience.journeyOrchestration.stepEvents.nodeName ORDER BY MESSAGE_COUNT DESC; |

*Sample output*

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 |  |
| --- | --- |
| MESSAGE_NAME | MESSAGE_COUNT |
| Welcome Email | 1 |
| Product Recommendation | 3 |
| Cart Abandonment Reminder | 2 |
| Weekly Newsletter | 4 |

The query returns the list of all messages along with their count invoked for the selected profile.

Find all the journeys a profile has entered in the last 30 days
This query returns all the journeys that a specific profile has entered within the last 30 days, along with the entry count for each journey.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.journeyVersionName AS JOURNEY_NAME, count(distinct _id) AS ENTRY_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.nodeType = 'start' AND _experience.journeyOrchestration.stepEvents.profileID = '<profileID corresponding to the namespace used>' AND timestamp > (now() - interval '30' day) GROUP BY _experience.journeyOrchestration.stepEvents.journeyVersionName ORDER BY ENTRY_COUNT DESC; |

*Sample output*

| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| JOURNEY_NAME | ENTRY_COUNT |
| Welcome Journey v2 | 1 |
| Product Recommendations | 5 |
| Re-engagement Campaign | 2 |

The query returns the list of all journey names along with the number of times the queried profile entered each journey.

Number of profiles that qualified for a journey daily
This query provides a daily breakdown of the number of distinct profiles that entered a journey over a specified time period.

| code language-sql |
| --- |
| SELECT DATE(timestamp) AS ENTRY_DATE, count(distinct _experience.journeyOrchestration.stepEvents.profileID) AS PROFILES_COUNT FROM journey_step_events WHERE DATE(timestamp) > (now() - interval '<last x days>' day) AND _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-version-id>' GROUP BY DATE(timestamp) ORDER BY DATE(timestamp) DESC; |

*Sample output*

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| ENTRY_DATE | PROFILES_COUNT |
| 2024-11-25 | 1,245 |
| 2024-11-24 | 1,189 |
| 2024-11-23 | 15,340 |
| 2024-11-22 | 1,205 |
| 2024-11-21 | 1,167 |

The query returns, for the defined period, the number of profiles that entered the journey each day. If a profile entered via multiple identities, it will be counted twice. If reentrance is enabled, profile count might be duplicated across different days if it reentered the journey on a different day.

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

## Queries related to the Read Audience read-segment-queries

Time taken to finish an audience export job
This query calculates the duration of an audience export job by finding the time difference between when the job was queued and when it finished.

| code language-sql |
| --- |
| select DATEDIFF (minute, (select timestamp where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.status = 'queued') , (select timestamp where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.status = 'finished')) AS export_job_runtime; |

The query returns the time difference, in minutes, between when time the audience export job was queued and when it finally ended.

Number of profiles that got discarded by the journey because they were duplicates
This query counts the number of distinct profiles that were discarded due to instance duplication errors during the Read Audience activity.

| code language-sql |
| --- |
| SELECT count(distinct _experience.journeyOrchestration.profile.ID) FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode = 'ERROR_INSTANCE_DUPLICATION' |

The query returns all the profile Ids that were discarded by the journey because they were duplicates.

Number of profiles that got discarded by the journey because of invalid namespace
This query returns the count of profiles that were discarded because they had an invalid namespace or missing identity for the required namespace.

| code language-sql |
| --- |
| SELECT count(*) FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode = 'ERROR_INSTANCE_BAD_NAMESPACE' |

The query returns all the profile Ids that were discarded by the journey because they had an invalid namespace or no identity for that namespace.

Number of profiles that got discarded by the journey because of no identity map
This query counts the profiles that were discarded because they were missing an identity map required for journey execution.

| code language-sql |
| --- |
| SELECT count(*) FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode = 'ERROR_INSTANCE_NO_IDENTITY_MAP' |

The query returns all the profile Ids that were discarded by the journey because the identity map was missing.

Number of profiles that got discarded by the journey because the journey was in test node and the profile was not a test profile
This query identifies profiles that were discarded when the journey was running in test mode but the profile did not have the testProfile attribute set to true.

| code language-sql |
| --- |
| SELECT count(distinct _experience.journeyOrchestration.profile.ID) FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode = 'ERROR_INSTANCE_NOT_A_TEST_PROFILE' |

The query returns all the profile Ids that were discarded by the journey because the export job was run in test mode but the profile did not have the testProfile attribute set to true.

Number of profiles that got discarded by the journey because of an internal error
This query returns the count of profiles that were discarded due to internal system errors during journey execution.

| code language-sql |
| --- |
| SELECT count(distinct _experience.journeyOrchestration.profile.ID) FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode = 'ERROR_INSTANCE_INTERNAL' |

The query returns all the profile Ids that were discarded by the journey due to some internal error.

Overview of the Read Audience for a given journey version
This query provides a comprehensive overview of the Read Audience activity, including segment export job details, event codes, statuses, and profile counts for all stages of the audience export process.

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode AS EVENT_CODE, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportSegmentID AS SEGMENT_ID, _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID AS EXPORTJOB_ID, _experience.journeyOrchestration.serviceEvents.segmentExportJob.status AS EXPORTJOB_STATUS, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountTotal AS TOTAL_EXPORTED_PROFILES_COUNT, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountRealized AS SUCCESS_EXPORTED_PROFILES_COUNT, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountFailed AS FAILED_EXPORTED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventType = 'segmenttrigger-orchestrator' |

It will return all service events related to the given journey version. We can follow the chain of operations:

- topic creation
- export job creation
- export job termination (with metrics on exported profiles)
- worker processing termination

We can also detect issues such as:

- errors in topic or export job creation (including timeouts on audience export API calls)
- export jobs which can be stuck (case when for a given journey version, we do not have any event regarding the export job termination)
- worker issues, if we have received export job termination event but no worker processing termination one

IMPORTANT: if there is no event returned by this query, it may be due to one of the following reasons:

- the journey version has not reached the schedule
- if the journey version is supposed to have trigger the export job by calling the orchestrator, something went wrong on the upstream flow: issue on journey deployment, business event or issue with scheduler.

Get Read Audience errors for a given journey version
This query filters for specific error event codes related to Read Audience failures, such as topic creation errors, API call errors, timeouts, and failed export jobs.

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode AS EVENT_CODE, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportSegmentID AS SEGMENT_ID, _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID AS EXPORTJOB_ID, _experience.journeyOrchestration.serviceEvents.segmentExportJob.status AS EXPORTJOB_STATUS, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountTotal AS TOTAL_EXPORTED_PROFILES_COUNT, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountRealized AS SUCCESS_EXPORTED_PROFILES_COUNT, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountFailed AS FAILED_EXPORTED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventType = 'segmenttrigger-orchestrator' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode IN ( 'ERROR_TOPIC_CREATION', 'ERROR_EXPORTJOB_APICALL', 'ERROR_EXPORTJOB_APICALL_TIMEOUT', 'ERROR_EXPORTJOB_FAILED' ) |

Get export job processing status
This query retrieves the processing status of audience export jobs, showing whether they succeeded or failed along with profile export metrics.

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode AS EVENT_CODE, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportSegmentID AS SEGMENT_ID, _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID AS EXPORTJOB_ID, _experience.journeyOrchestration.serviceEvents.segmentExportJob.status AS EXPORTJOB_STATUS, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountTotal AS TOTAL_EXPORTED_PROFILES_COUNT, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountRealized AS SUCCESS_EXPORTED_PROFILES_COUNT, _experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountFailed AS FAILED_EXPORTED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventType = 'segmenttrigger-orchestrator' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode IN ( 'INFO_EXPORTJOB_SUCCEEDED', 'ERROR_EXPORTJOB_FAILED' ) |

If no record is returned, that means that either:

- an error has occurred during topic or export job creation
- the export job is still running

Get metrics on exported profiles, including discards and export job metrics for each export jobs
This query combines discarded profile counts with export job metrics to provide a complete view of audience export performance for each individual export job.

*Data Lake query*

| code language-sql |
| --- |
| WITH DISCARDED_EXPORTED_PROFILES AS ( SELECT _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID AS EXPORTJOB_ID, count(distinct _experience.journeyOrchestration.profile.ID) AS DISCARDED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode IN ( 'ERROR_INSTANCE_DUPLICATION', 'ERROR_INSTANCE_BAD_NAMESPACE', 'ERROR_INSTANCE_NO_IDENTITY_MAP', 'ERROR_INSTANCE_NOT_A_TEST_PROFILE', 'ERROR_INSTANCE_INTERNAL' ) GROUP BY _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID ), SEGMENT_EXPORT_METRICS AS ( SELECT _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID AS EXPORTJOB_ID, sum(_experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountTotal) AS TOTAL_EXPORTED_PROFILES_COUNT, sum(_experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountRealized) AS SUCCESS_EXPORTED_PROFILES_COUNT, sum(_experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountFailed) AS FAILED_EXPORTED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventType = 'segmenttrigger-orchestrator' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode IN ( 'INFO_EXPORTJOB_SUCCEEDED', 'ERROR_EXPORTJOB_FAILED' ) GROUP BY _experience.journeyOrchestration.serviceEvents.segmentExportJob.ID ) SELECT sum(T2.TOTAL_EXPORTED_PROFILES_COUNT), sum(T2.SUCCESS_EXPORTED_PROFILES_COUNT), sum(T2.FAILED_EXPORTED_PROFILES_COUNT), sum(T1.DISCARDED_PROFILES_COUNT) FROM DISCARDED_EXPORTED_PROFILES AS T1, SEGMENT_EXPORT_METRICS AS T2 WHERE T1.EXPORTJOB_ID = T2.EXPORTJOB_ID |

Get aggregated metrics (audience export jobs and discards) on all export jobs
This query aggregates overall metrics across all export jobs for a given journey version, useful for recurring journeys or business event-triggered journeys with topic reuse.

*Data Lake query*

| code language-sql |
| --- |
| WITH DISCARDED_EXPORTED_PROFILES AS ( SELECT _experience.journeyOrchestration.journey.versionID AS JOURNEYVERSION_ID, count(distinct _experience.journeyOrchestration.profile.ID) AS DISCARDED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode IN ( 'ERROR_INSTANCE_DUPLICATION', 'ERROR_INSTANCE_BAD_NAMESPACE', 'ERROR_INSTANCE_NO_IDENTITY_MAP', 'ERROR_INSTANCE_NOT_A_TEST_PROFILE', 'ERROR_INSTANCE_INTERNAL' ) GROUP BY _experience.journeyOrchestration.journey.versionID ), SEGMENT_EXPORT_METRICS AS ( SELECT _experience.journeyOrchestration.journey.versionID AS JOURNEYVERSION_ID, sum(_experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountTotal) AS TOTAL_EXPORTED_PROFILES_COUNT, sum(_experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountRealized) AS SUCCESS_EXPORTED_PROFILES_COUNT, sum(_experience.journeyOrchestration.serviceEvents.segmentExportJob.exportCountFailed) AS FAILED_EXPORTED_PROFILES_COUNT FROM journey_step_events WHERE _experience.journeyOrchestration.journey.versionID = '<journey-version-id>' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventType = 'segmenttrigger-orchestrator' AND _experience.journeyOrchestration.serviceEvents.segmentExportJob.eventCode IN ( 'INFO_EXPORTJOB_SUCCEEDED', 'ERROR_EXPORTJOB_FAILED' ) GROUP BY _experience.journeyOrchestration.journey.versionID ) SELECT sum(T2.TOTAL_EXPORTED_PROFILES_COUNT), sum(T2.SUCCESS_EXPORTED_PROFILES_COUNT), sum(T2.FAILED_EXPORTED_PROFILES_COUNT), sum(T1.DISCARDED_PROFILES_COUNT) FROM DISCARDED_EXPORTED_PROFILES AS T1, SEGMENT_EXPORT_METRICS AS T2 WHERE T1.JOURNEYVERSION_ID = T2.JOURNEYVERSION_ID |

This query is different than the previous one.

It returns the overall metrics for a given journey version, regardless the jobs which can have run for it (in case of recurring journeys, business events triggered ones leveraging topic reuse).

## Queries related to Audience Qualification segment-qualification-queries

Profile discarded because of a different audience realization than the one configured
This query identifies profiles that were discarded because their audience realization status did not match the journey’s Audience Qualification configuration (e.g., configured for “enters” but profile “exited”).

*Data Lake query*

| code language-sql |
| --- |
| SELECT DATE(timestamp), _experience.journeyOrchestration.profile.ID FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = '<journey-version id>' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'ERROR_SEGMENT_REALISATION_CONDITION_MISMATCH' |

*Example*

| code language-sql |
| --- |
| SELECT DATE(timestamp), _experience.journeyOrchestration.profile.ID FROM journey_step_events where _experience.journeyOrchestration.journey.versionID = 'a868f3c9-4888-46ac-a274-94cdf1c4159d' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'ERROR_SEGMENT_REALISATION_CONDITION_MISMATCH' |

This query returns all the profile Ids that were discarded by the journey version due to wrong audience realization.

Audience Qualification events discarded by any other reason for a specific profile
This query retrieves all audience qualification or external events that were discarded for a specific profile due to internal service errors.

*Data Lake query*

| code language-sql |
| --- |
| SELECT DATE(timestamp), _experience.journeyOrchestration.profile.ID, _experience.journeyOrchestration.serviceEvents.dispatcher.projectionID FROM journey_step_events where _experience.journeyOrchestration.profile.ID = '<profile-id>' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'ERROR_SERVICE_INTERNAL'; |

*Example*

| code language-sql |
| --- |
| SELECT DATE(timestamp), _experience.journeyOrchestration.profile.ID, _experience.journeyOrchestration.serviceEvents.dispatcher.projectionID FROM journey_step_events where _experience.journeyOrchestration.profile.ID = 'mandee@adobe.com' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'ERROR_SERVICE_INTERNAL'; |

This query returns all events (external events / audience qualification events) that were discarded because of any other reason for a profile.

## Queries related to business rules business-rules-queries

Check all discards due to journey frequency capping exclusions on a specific journey after a specific date
This query returns the rejected ruleset and rule details for all profiles discarded due to frequency capping rules on a specific journey, starting from a given date.

*Data Lake query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.dispatcher.eventType, _experience.journeyOrchestration.serviceEvents.dispatcher.eventCodeReason, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.ID AS RULESET_ID, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.name AS RULESET_NAME, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.rejectedRules.ID AS RULE_ID, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.rejectedRules.name AS RULE_NAME FROM journey_step_events WHERE _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.stepEvents.journeyVersionID='<journeyVersionId>' AND _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.ID is not null AND timestamp >= to_date('<YYYY-MM-DD>') |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.dispatcher.eventType, _experience.journeyOrchestration.serviceEvents.dispatcher.eventCodeReason, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.ID AS RULESET_ID, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.name AS RULESET_NAME, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.rejectedRules.ID AS RULE_ID, _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.rejectedRules.name AS RULE_NAME FROM journey_step_events WHERE _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.stepEvents.journeyVersionID='3855072d-79c3-438a-a5c3-c77fd6843812' AND _experience.journeyOrchestration.serviceEvents.dispatcher.rejectedRuleset.ID is not null AND timestamp >= to_date('2025-05-16') |

This query returns all discards where a ruleset was matched (non-null rejectedRuleset.ID). The eventCodeReason field provides the sub-reason for the discard: LOWER_PRIORITY (profile discarded due to journey arbitration) or CAP_REACHED (profile discarded because the frequency cap was reached). The results show which specific frequency capping rulesets and rules caused profiles to be excluded from the journey after the specified date.

## Event-based queries event-based-queries

Check if a business event was received for a journey
This query counts the number of times a business event was received by a journey, grouped by date, within a specified time frame.

| code language-sql |
| --- |
| SELECT DATE(timestamp), count(distinct _id) FROM journey_step_events where _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journey-version-id>' AND _experience.journeyOrchestration.stepEvents.nodeName = '<node-name-corresponding-to-business-event>' AND _experience.journeyOrchestration.stepEvents.nodeType = 'start' AND WHERE DATE(timestamp) > (now() - interval '<last x hours>' hour) |

Check if an external event of a profile got discarded because no related journey was found
This query identifies when an external event for a specific profile was discarded because there was no active or matching journey configured to receive that event.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.profile.ID, DATE(timestamp) FROM journey_step_events where _experience.journeyOrchestration.serviceEvents.dispatcher.eventID = '<eventId>' AND _experience.journeyOrchestration.profile.ID = '<profileID>' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'EVENT_WITH_NO_JOURNEY' |

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

Check if an external event of a profile got discarded because of any other reason
This query retrieves external events that were discarded for a specific profile due to internal service errors, along with the event ID and error code.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.profile.ID, DATE(timestamp), _experience.journeyOrchestration.serviceEvents.dispatcher.eventID, _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode FROM journey_step_events where _experience.journeyOrchestration.profile.ID='<profileID>' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventID='<eventID>' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventCode = 'discard' AND _experience.journeyOrchestration.serviceEvents.dispatcher.eventType = 'ERROR_SERVICE_INTERNAL'; |

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

Check the count of all the events discarded by stateMachine by errorCode
This query aggregates all events discarded by the journey state machine, grouped by error code to help identify the most common reasons for discards.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.serviceEvents.stateMachine.eventCode, COUNT() FROM journey_step_events where _experience.journeyOrchestration.serviceEvents.stateMachine.eventType = 'discard' GROUP BY _experience.journeyOrchestration.serviceEvents.stateMachine.eventCode |

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

Check all discarded events because reentrance was not allowed
This query identifies all events that were discarded because a profile attempted to reenter a journey when reentrance was not permitted in the journey configuration.

| code language-sql |
| --- |
| SELECT DATE(timestamp), _experience.journeyOrchestration.profile.ID, _experience.journeyOrchestration.journey.versionID, _experience.journeyOrchestration.serviceEvents.stateMachine.eventCode FROM journey_step_events where _experience.journeyOrchestration.serviceEvents.stateMachine.eventType = 'discard' AND _experience.journeyOrchestration.serviceEvents.stateMachine.eventCode='reentranceNotAllowed' |

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

## Queries for engageable profiles engageable-profiles-queries

These queries help you monitor and analyze your Engageable Profiles count. An Engageable Profile is a unique profile that has been engaged through journeys or campaigns in the past 12 months. Learn more about [Engageable Profiles and license usage](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage#what-is-engageable-profile).

**Best practices for querying Engageable Profiles:**

- Ensure each non-aggregate field is included in the GROUP BY clause
- Avoid referencing datasets that don’t exist in your sandbox - confirm dataset names in the Platform UI
- Use distinct when counting unique profiles to avoid duplicates across identity namespaces
- When using LIMIT, place it at the end of the query after ORDER BY clauses

Count unique profiles engaged by a specific journey
This query returns the number of distinct profiles that have been engaged by a specific journey, which contributes to your Engageable Profiles count.

| code language-sql |
| --- |
| SELECT count(distinct _experience.journeyOrchestration.stepEvents.profileID) AS ENGAGED_PROFILES FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.journeyVersionID = '<journeyVersionID>' AND timestamp > (now() - interval '12' month); |

This query helps you understand how many unique profiles a specific journey has contributed to your [Engageable Profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage) count in the past 12 months.

Count profiles engaged per journey in the last 12 months
This query shows the number of unique profiles engaged by each journey in your organization over the past 12 months, helping you identify which journeys are contributing most to your [Engageable Profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage) count.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.journeyVersionID AS JOURNEY_VERSION_ID, _experience.journeyOrchestration.stepEvents.journeyVersionName AS JOURNEY_NAME, count(distinct _experience.journeyOrchestration.stepEvents.profileID) AS ENGAGED_PROFILES FROM journey_step_events WHERE timestamp > (now() - interval '12' month) GROUP BY _experience.journeyOrchestration.stepEvents.journeyVersionID, _experience.journeyOrchestration.stepEvents.journeyVersionName ORDER BY ENGAGED_PROFILES DESC; |

*Sample output*

| table 0-row-3 1-row-3 2-row-3 3-row-3 |  |  |
| --- | --- | --- |
| JOURNEY_VERSION_ID | JOURNEY_NAME | ENGAGED_PROFILES |
| 67b14482-143e-4f83-9cf5-cfec0fca3d26 | Welcome Campaign v2 | 125,450 |
| a3c21b89-456d-4e21-b8f3-9a8e7c6d5432 | Product Launch Journey | 98,230 |
| f9e8d7c6-b5a4-3210-9876-543210fedcba | Re-engagement Flow | 45,670 |

This output helps you identify which journeys are engaging the most profiles and contributing most significantly to your Engageable Profiles count.

| note |
| --- |
| NOTE |
| This query groups by both journeyVersionID and journeyVersionName. Both fields must be included in the GROUP BY clause since they are selected in the query. Omitting fields from the GROUP BY clause will cause the query to fail. |

Count profiles engaged by journeys daily over the past 30 days
This query provides a daily breakdown of newly engaged profiles, helping you identify spikes in [Engageable Profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage) count.

| code language-sql |
| --- |
| SELECT DATE(timestamp) AS ENGAGEMENT_DATE, count(distinct _experience.journeyOrchestration.stepEvents.profileID) AS ENGAGED_PROFILES FROM journey_step_events WHERE timestamp > (now() - interval '30' day) GROUP BY DATE(timestamp) ORDER BY ENGAGEMENT_DATE DESC; |

*Sample output*

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| ENGAGEMENT_DATE | ENGAGED_PROFILES |
| 2024-11-25 | 8,450 |
| 2024-11-24 | 7,820 |
| 2024-11-23 | 125,340 |
| 2024-11-22 | 9,230 |
| 2024-11-21 | 8,670 |

This output helps you monitor daily trends and identify when large numbers of profiles are being engaged. In this example, November 23 shows a significant spike (125,340 profiles) compared to typical daily engagement (~8,000 profiles), which would warrant investigation to understand what journey or campaign caused the increase in your [Engageable Profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage) count.

Identify journeys that recently engaged large audiences
This query helps identify which journeys have engaged large numbers of new profiles in recent time periods, which may explain sudden increases in [Engageable Profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage) count.

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.journeyVersionID AS JOURNEY_VERSION_ID, _experience.journeyOrchestration.stepEvents.journeyVersionName AS JOURNEY_NAME, DATE(timestamp) AS ENGAGEMENT_DATE, count(distinct _experience.journeyOrchestration.stepEvents.profileID) AS ENGAGED_PROFILES FROM journey_step_events WHERE timestamp > (now() - interval '7' day) AND _experience.journeyOrchestration.stepEvents.nodeType = 'start' GROUP BY _experience.journeyOrchestration.stepEvents.journeyVersionID, _experience.journeyOrchestration.stepEvents.journeyVersionName, DATE(timestamp) HAVING count(distinct _experience.journeyOrchestration.stepEvents.profileID) > 1000 ORDER BY ENGAGEMENT_DATE DESC, ENGAGED_PROFILES DESC; |

*Sample output*

| table 0-row-4 1-row-4 2-row-4 3-row-4 |  |  |  |
| --- | --- | --- | --- |
| JOURNEY_VERSION_ID | JOURNEY_NAME | ENGAGEMENT_DATE | ENGAGED_PROFILES |
| 67b14482-143e-4f83-9cf5-cfec0fca3d26 | Black Friday Campaign | 2024-11-23 | 125,340 |
| a3c21b89-456d-4e21-b8f3-9a8e7c6d5432 | Product Launch Journey | 2024-11-22 | 45,230 |
| f9e8d7c6-b5a4-3210-9876-543210fedcba | Holiday Newsletter | 2024-11-21 | 32,150 |

This query filters for journeys that engaged more than 1,000 profiles per day in the past 7 days. The output shows which specific journeys and dates are responsible for large profile engagements. Adjust the HAVING clause threshold based on your needs (e.g., change > 1000 to > 10000 for larger thresholds).

Total unique profiles engaged across all journeys in the last 12 months
This query provides a count of unique profiles engaged across all journeys in the past 12 months, giving you an overview of your journey-based engagement.

| code language-sql |
| --- |
| SELECT count(distinct _experience.journeyOrchestration.stepEvents.profileID) AS TOTAL_ENGAGED_PROFILES FROM journey_step_events WHERE timestamp > (now() - interval '12' month); |

*Sample output*

| table 0-row-1 1-row-1 |
| --- |
| TOTAL_ENGAGED_PROFILES |
| 2,547,890 |

This single number represents the total count of unique profiles that have been engaged by at least one journey in the past 12 months.

| note |
| --- |
| NOTE |
| This query counts distinct profile IDs in the journey step events dataset. The actual Engageable Profiles count shown in the [License Usage Dashboard](/en/docs/journey-optimizer/using/audiences-profiles-identities/license-usage) may differ slightly, as it also includes profiles engaged through campaigns and other Journey Optimizer capabilities beyond journeys. |

## Common journey-based queries journey-based-queries

Number of daily active journeys
This query returns a daily count of unique journey versions that had activity, helping you understand journey execution patterns over time.

| code language-sql |
| --- |
| SELECT DATE(timestamp) AS ACTIVITY_DATE, count(distinct _experience.journeyOrchestration.stepEvents.journeyVersionID) AS ACTIVE_JOURNEYS FROM journey_step_events WHERE DATE(timestamp) > (now() - interval '<last x days>' day) GROUP BY DATE(timestamp) ORDER BY DATE(timestamp) DESC; |

*Sample output*

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| ACTIVITY_DATE | ACTIVE_JOURNEYS |
| 2024-11-25 | 12 |
| 2024-11-24 | 15 |
| 2024-11-23 | 14 |
| 2024-11-22 | 11 |
| 2024-11-21 | 13 |

The query returns, for the defined period, the count of unique journeys that triggered each day. A single journey triggering on multiple days will be counted once per day.

## Queries on journey instances journey-instances-queries

Number of profiles in a specific state a specific time
This query uses Common Table Expressions (CTEs) to identify profiles that are currently waiting at a specific node in a journey by finding profiles that passed through the node but have not yet proceeded to the next nodes.

*Data Lake query*

| code language-sql |
| --- |
| WITH INSTANCES_PASSED_IN_ALL_NODES_WITH_DETAILS AS ( SELECT STEP_EVENTS.timestamp AS TS, STEP_EVENTS._experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, STEP_EVENTS._experience.journeyOrchestration.stepEvents.instanceID AS ID FROM journey_step_events AS STEP_EVENTS WHERE STEP_EVENTS._experience.journeyOrchestration.stepEvents.journeyVersionName = '<journey version name>' ), INSTANCES_PASSED_IN_NODE_WITH_DETAILS AS ( SELECT T1.TS AS TS, T1.ID AS ID FROM INSTANCES_PASSED_IN_ALL_NODES_WITH_DETAILS AS T1 WHERE T1.NODE_NAME = '<specific node name>' AND <filter on time for profile in specific node> ), INSTANCES_PASSED_IN_NEXT_NODES AS ( SELECT T1.TS AS TS, T1.ID AS ID FROM INSTANCES_PASSED_IN_ALL_NODES_WITH_DETAILS AS T1 WHERE T1.NODE_NAME in (<list of next node names from the specific node>) ), INSTANCES_PASSED_IN_NODE_NOT_PASSED_IN_NODES AS ( SELECT distinct T1.ID AS ID FROM INSTANCES_PASSED_IN_NODE_WITH_DETAILS AS T1 EXCEPT SELECT distinct T1.ID AS ID FROM INSTANCES_PASSED_IN_NEXT_NODES AS T1 ) SELECT DATE_FORMAT(T1.TS,'<date pattern>') AS DATETIME, count(T1.ID) AS INSTANCES_COUNT FROM INSTANCES_PASSED_IN_NODE_WITH_DETAILS AS T1, INSTANCES_PASSED_IN_NODE_NOT_PASSED_IN_NODES AS T2 WHERE T1.ID = T2.ID GROUP BY DATETIME ORDER BY DATETIME DESC |

*Example*

| code language-sql |
| --- |
| WITH INSTANCES_PASSED_IN_ALL_NODES_WITH_DETAILS AS ( SELECT STEP_EVENTS.timestamp AS TS, STEP_EVENTS._experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, STEP_EVENTS._experience.journeyOrchestration.stepEvents.instanceID AS ID FROM journey_step_events AS STEP_EVENTS WHERE STEP_EVENTS._experience.journeyOrchestration.stepEvents.journeyVersionName = 'Journey20009' ), INSTANCES_PASSED_IN_NODE_WITH_DETAILS AS ( SELECT T1.TS AS TS, T1.ID AS ID FROM INSTANCES_PASSED_IN_ALL_NODES_WITH_DETAILS AS T1 WHERE T1.NODE_NAME = 'slack_bso_tests - test1' AND T1.TS > (now() - interval '18 hour') ), INSTANCES_PASSED_IN_NEXT_NODES AS ( SELECT T1.TS AS TS, T1.ID AS ID FROM INSTANCES_PASSED_IN_ALL_NODES_WITH_DETAILS AS T1 WHERE T1.NODE_NAME in ('slack_bso_tests - test2') ), INSTANCES_PASSED_IN_NODE_NOT_PASSED_IN_NODES AS ( SELECT distinct T1.ID AS ID FROM INSTANCES_PASSED_IN_NODE_WITH_DETAILS AS T1 EXCEPT SELECT distinct T1.ID AS ID FROM INSTANCES_PASSED_IN_NEXT_NODES AS T1 ) SELECT DATE_FORMAT(T1.TS,'yyyy/MM/dd HH:mm') AS DATETIME, count(T1.ID) AS INSTANCES_COUNT FROM INSTANCES_PASSED_IN_NODE_WITH_DETAILS AS T1, INSTANCES_PASSED_IN_NODE_NOT_PASSED_IN_NODES AS T2 WHERE T1.ID = T2.ID GROUP BY DATETIME ORDER BY DATETIME DESC |

How many profiles exited the journey in the specific period of time
This query counts the journey instances that exited during a specified time period, including exits due to completion, errors, timeouts, or capping errors.

*Data Lake query*

| code language-sql |
| --- |
| SELECT DATE_FORMAT(STEP_EVENTS.timestamp,'yyyy/MM/dd HH:mm') AS DATETIME, count(STEP_EVENTS._experience.journeyOrchestration.stepEvents.instanceID) AS EXITED_INSTANCES_COUNT FROM journey_step_events AS STEP_EVENTS WHERE STEP_EVENTS._experience.journeyOrchestration.stepEvents.journeyVersionName = '<journey version name>' AND STEP_EVENTS._experience.journeyOrchestration.stepEvents.stepStatus in ('endStep', 'error', 'timedOut', 'cappingError') AND <timestamp filter> GROUP BY DATETIME ORDER BY DATETIME DESC |

*Example*

| code language-sql |
| --- |
| SELECT DATE_FORMAT(STEP_EVENTS.timestamp,'yyyy/MM/dd HH:mm') AS DATETIME, count(STEP_EVENTS._experience.journeyOrchestration.stepEvents.instanceID) AS EXITED_INSTANCES_COUNT FROM journey_step_events AS STEP_EVENTS WHERE STEP_EVENTS._experience.journeyOrchestration.stepEvents.journeyVersionName = 'Journey20009' AND STEP_EVENTS._experience.journeyOrchestration.stepEvents.stepStatus in ('endStep', 'error', 'timedOut', 'cappingError') AND STEP_EVENTS.timestamp > (now() - interval '22 hour') GROUP BY DATETIME ORDER BY DATETIME DESC |

How many profiles exited the journey in the specific period of time with node/status
This query provides a detailed breakdown of journey exits, showing the node name and exit status for each exited instance to help identify where and why profiles left the journey.

*Data Lake query*

| code language-sql |
| --- |
| SELECT DATE_FORMAT(STEP_EVENTS.timestamp,'yyyy/MM/dd HH:mm') AS DATETIME, STEP_EVENTS._experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, STEP_EVENTS._experience.journeyOrchestration.stepEvents.stepStatus AS EXIT_STATUS, count(STEP_EVENTS._experience.journeyOrchestration.stepEvents.instanceID) AS EXITED_INSTANCES_COUNT FROM journey_step_events AS STEP_EVENTS WHERE STEP_EVENTS._experience.journeyOrchestration.stepEvents.journeyVersionName = '<journey version name>' AND STEP_EVENTS._experience.journeyOrchestration.stepEvents.stepStatus in ('endStep', 'error', 'timedOut', 'cappingError') AND <timestamp filter> GROUP BY DATETIME, NODE_NAME, EXIT_STATUS ORDER BY DATETIME DESC |

*Example*

| code language-sql |
| --- |
| SELECT DATE_FORMAT(STEP_EVENTS.timestamp,'yyyy/MM/dd HH:mm') AS DATETIME, STEP_EVENTS._experience.journeyOrchestration.stepEvents.nodeName AS NODE_NAME, STEP_EVENTS._experience.journeyOrchestration.stepEvents.stepStatus AS EXIT_STATUS, count(STEP_EVENTS._experience.journeyOrchestration.stepEvents.instanceID) AS EXITED_INSTANCES_COUNT FROM journey_step_events AS STEP_EVENTS WHERE STEP_EVENTS._experience.journeyOrchestration.stepEvents.journeyVersionName = 'Journey20009' AND STEP_EVENTS._experience.journeyOrchestration.stepEvents.stepStatus in ('endStep', 'error', 'timedOut', 'cappingError') AND STEP_EVENTS.timestamp > (now() - interval '22 hour') GROUP BY DATETIME, NODE_NAME, EXIT_STATUS ORDER BY DATETIME DESC |

## Queries related to custom action performance metrics query-custom-action

Total number of successful calls, errors and requests per second of each endpoint over a specific time period
This query provides performance metrics for custom HTTP actions, including total calls, successful calls, error counts by type (4xx, 5xx, timeouts, capped), and throughput in requests per second for each endpoint.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS TOTAL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL THEN 1 END) AS SUCCESSFUL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '4%' THEN 1 END) AS "4xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '5%' THEN 1 END) AS "5xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'timedout' THEN 1 END) AS TIMEOUTS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' THEN 1 END) AS CAPPED_CALLS, ROUND(COUNT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime) / COUNT(DISTINCT DATE_TRUNC('second', _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime)), 0) AS THROUGHPUT_RPS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND (<actionExecutionOriginStartTime filter> OR (_experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' AND <timestamp filter>)) GROUP BY ENDPOINT ORDER BY ENDPOINT; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS TOTAL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL THEN 1 END) AS SUCCESSFUL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '4%' THEN 1 END) AS "4xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '5%' THEN 1 END) AS "5xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'timedout' THEN 1 END) AS TIMEOUTS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' THEN 1 END) AS CAPPED_CALLS, ROUND(COUNT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime) / COUNT(DISTINCT DATE_TRUNC('second', _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime)), 0) AS THROUGHPUT_RPS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND (_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) OR (_experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' AND timestamp > (now() - interval '1' day))) GROUP BY ENDPOINT ORDER BY ENDPOINT; |

Time series of successful calls, errors and throughput of each endpoint over a specific time period
This query provides the same performance metrics as the previous query but organized as a time series, showing how endpoint performance varies over time with minute-by-minute granularity.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, DATE_FORMAT(COALESCE(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime, timestamp), 'yyyy/MM/dd HH:mm') AS SPAN, COUNT(1) AS TOTAL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL THEN 1 END) AS SUCCESSFUL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '4%' THEN 1 END) AS "4xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '5%' THEN 1 END) AS "5xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'timedout' THEN 1 END) AS TIMEOUTS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' THEN 1 END) AS CAPPED_CALLS, ROUND(COUNT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime) / COUNT(DISTINCT DATE_TRUNC('second', _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime)), 0) AS THROUGHPUT_RPS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND (<actionExecutionOriginStartTime filter> OR (_experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' AND <timestamp filter>)) GROUP BY ENDPOINT, SPAN ORDER BY ENDPOINT, SPAN; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, DATE_FORMAT(COALESCE(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime, timestamp), 'yyyy/MM/dd HH:mm') AS SPAN, COUNT(1) AS TOTAL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL THEN 1 END) AS SUCCESSFUL_CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '4%' THEN 1 END) AS "4xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'http' AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode LIKE '5%' THEN 1 END) AS "5xx_ERRORS", COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'timedout' THEN 1 END) AS TIMEOUTS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' THEN 1 END) AS CAPPED_CALLS, ROUND(COUNT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime) / COUNT(DISTINCT DATE_TRUNC('second', _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime)), 0) AS THROUGHPUT_RPS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND (_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) OR (_experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' AND timestamp > (now() - interval '1' day))) GROUP BY ENDPOINT, SPAN ORDER BY ENDPOINT, SPAN; |

Response latency of each endpoint at 50th, 95th, 99th and 99.9th percentile over a specific time period
This query calculates response time percentiles for custom action endpoints, helping you understand latency distribution and identify performance outliers at different percentile thresholds.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS SUCCESSFUL_CALLS, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P50_LATENCY_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P95_LATENCY_MS, ROUND(PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P99_LATENCY_MS, ROUND(PERCENTILE_CONT(0.999) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P999_LATENCY_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime IS NOT NULL <actionExecutionOriginStartTime filter> GROUP BY ENDPOINT ORDER BY ENDPOINT; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS SUCCESSFUL_CALLS, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P50_LATENCY_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P95_LATENCY_MS, ROUND(PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P99_LATENCY_MS, ROUND(PERCENTILE_CONT(0.999) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P999_LATENCY_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) GROUP BY ENDPOINT ORDER BY ENDPOINT; |

Time series of response latency percentiles of each endpoint over a specific time period
This query provides latency percentiles organized as a time series, allowing you to track how endpoint response times change over time at different percentile levels.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS SUCCESSFUL_CALLS, DATE_FORMAT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime, 'yyyy/MM/dd HH:mm') AS SPAN, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P50_LATENCY_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P95_LATENCY_MS, ROUND(PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P99_LATENCY_MS, ROUND(PERCENTILE_CONT(0.999) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P999_LATENCY_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime IS NOT NULL <actionExecutionOriginStartTime filter> GROUP BY ENDPOINT, SPAN ORDER BY ENDPOINT, SPAN; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS SUCCESSFUL_CALLS, DATE_FORMAT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime, 'yyyy/MM/dd HH:mm') AS SPAN, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P50_LATENCY_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P95_LATENCY_MS, ROUND(PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P99_LATENCY_MS, ROUND(PERCENTILE_CONT(0.999) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime),0) AS P999_LATENCY_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginTime IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) GROUP BY ENDPOINT, SPAN ORDER BY ENDPOINT, SPAN; |

Waiting time in queue on throttled endpoints at 50th and 95th percentile over a specific time period
This query analyzes queue waiting times for throttled endpoints, showing the 50th and 95th percentile wait times to help you understand the impact of throttling on your custom actions.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS THROTTLED_CALLS, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P50_QUEUE_TIME_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P95_QUEUE_TIME_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionIsThrottled = 'true' AND _experience.journeyOrchestration.stepEvents.actionWaitTime IS NOT NULL AND <actionExecutionOriginStartTime filter> GROUP BY ENDPOINT ORDER BY ENDPOINT; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, COUNT(1) AS THROTTLED_CALLS, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P50_QUEUE_TIME_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P95_QUEUE_TIME_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionIsThrottled = 'true' AND _experience.journeyOrchestration.stepEvents.actionWaitTime IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) GROUP BY ENDPOINT ORDER BY ENDPOINT; |

Time series of queue waiting time percentiles for each throttled endpoint
This query provides queue waiting time percentiles as a time series, allowing you to monitor how throttling impacts wait times over time for each endpoint.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, DATE_FORMAT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime, 'yyyy/MM/dd HH:mm') AS SPAN, COUNT(1) AS THROTTLED_CALLS, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P50_QUEUE_TIME_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P95_QUEUE_TIME_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionIsThrottled = 'true' AND _experience.journeyOrchestration.stepEvents.actionWaitTime IS NOT NULL AND <actionExecutionOriginStartTime filter> GROUP BY ENDPOINT, SPAN ORDER BY ENDPOINT, SPAN; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionOriginEndpoint AS ENDPOINT, DATE_FORMAT(_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime, 'yyyy/MM/dd HH:mm') AS SPAN, COUNT(1) AS THROTTLED_CALLS, ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P50_QUEUE_TIME_MS, ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY _experience.journeyOrchestration.stepEvents.actionWaitTime),0) AS P95_QUEUE_TIME_MS FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionIsThrottled = 'true' AND _experience.journeyOrchestration.stepEvents.actionWaitTime IS NOT NULL AND _experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) GROUP BY ENDPOINT, SPAN ORDER BY ENDPOINT, SPAN; |

Number of errors by type and code for a specific endpoint over a specific time period
This query provides a detailed breakdown of errors for a specific endpoint, grouped by error type and error code, including information about retry attempts.

*Data Lake Query*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionExecutionError AS ERROR_TYPE, _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode AS ERROR_CODE, COUNT(1) AS CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionOriginError IS NOT NULL THEN 1 END) AS CALLS_WITH_RETRY FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint = '<endpoint URI>' AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NOT NULL AND (<actionExecutionOriginStartTime filter>) OR (_experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' AND <timestamp filter>)) GROUP BY ERROR_TYPE, ERROR_CODE ORDER BY ERROR_TYPE, ERROR_CODE; |

*Example*

| code language-sql |
| --- |
| SELECT _experience.journeyOrchestration.stepEvents.actionExecutionError AS ERROR_TYPE, _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode AS ERROR_CODE, COUNT(1) AS CALLS, COUNT(CASE WHEN _experience.journeyOrchestration.stepEvents.actionExecutionOriginError IS NOT NULL THEN 1 END) AS CALLS_WITH_RETRY FROM journey_step_events WHERE _experience.journeyOrchestration.stepEvents.actionType = 'customHttpAction' AND _experience.journeyOrchestration.stepEvents.actionOriginEndpoint = 'https://example.com/my/endpoint' AND _experience.journeyOrchestration.stepEvents.actionExecutionError IS NOT NULL AND (_experience.journeyOrchestration.stepEvents.actionExecutionOriginStartTime > (now() - interval '1' day) OR (_experience.journeyOrchestration.stepEvents.actionExecutionError = 'capped' AND timestamp > (now() - interval '1' day))) GROUP BY ERROR_TYPE, ERROR_CODE ORDER BY ERROR_TYPE, ERROR_CODE; |

recommendation-more-help
