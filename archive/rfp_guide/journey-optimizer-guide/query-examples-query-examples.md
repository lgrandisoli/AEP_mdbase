---
title: "Query examples query-examples"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/data-management/datasets/datasets-query-examples"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:09.541194+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Query examples query-examples

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Reporting](#)
- [Use Cases](#)
- [Datasets](#)
- [Data Management](#)

CREATED FOR:

- Experienced
- Developer
- Admin

In this page, you will find the list of Adobe Journey Optimizer datasets and related use cases:

- [Email Tracking Experience Event Dataset](#email-tracking-experience-event-dataset)
- [Message Feedback Event Dataset](#message-feedback-event-dataset)
- [Push Tracking Experience Event Dataset](#push-tracking-experience-event-dataset)
- [Journey Step Event](#journey-step-event)
- [Decisioning Event Dataset](#ode-decisionevents)
- [Secondary recipient feedback event dataset (BCC)](#bcc-feedback-event-dataset)
- [Entity Dataset](#entity-dataset)

To view the complete list of fields and attributes for each schema, consult the [Journey Optimizer schema dictionary](/tools/ajo-schemas/schema-dictionary.html#_blank).

See also several commonly used [examples to query Journey Step Events](/en/docs/journey-optimizer/using/reporting/reports/query-examples).

## Email tracking Experience event dataset email-tracking-experience-event-dataset

*Name in the interface : AJO Email Tracking Experience Event Dataset*

System dataset for ingesting email tracking experience events from Journey Optimizer.

The related schema is AJO Email Tracking Experience Event Schema.

This query shows the counts of different email interactions (opens, clicks) for a given message:

```
select
    _experience.customerJourneyManagement.messageInteraction.interactionType AS interactionType,
    count(1) eventCount
from ajo_email_tracking_experience_event_dataset
where
     _experience.customerJourneyManagement.messageExecution.messageExecutionID IN ('UMA-30647505')
group by
    _experience.customerJourneyManagement.messageInteraction.interactionType
```

This query shows the breakdown of counts of different email interactions (opens, clicks) by message for a given journey:

```
select
    _experience.customerJourneyManagement.messageExecution.messageExecutionID AS messageExecutionID,
    _experience.customerJourneyManagement.messageInteraction.interactionType AS interactionType,
    count(1) eventCount
from ajo_email_tracking_experience_event_dataset
where
     _experience.customerJourneyManagement.messageExecution.journeyVersionID IN ('0e86ac62-c315-48cc-ab4f-3f8b741ae667')
group by
    _experience.customerJourneyManagement.messageExecution.messageExecutionID,
    _experience.customerJourneyManagement.messageInteraction.interactionType
order by
    _experience.customerJourneyManagement.messageExecution.messageExecutionID,
    _experience.customerJourneyManagement.messageInteraction.interactionType
limit 100;
```

## Message feedback event dataset message-feedback-event-dataset

*Name in the interface: AJO Message Feedback Event Dataset*

Dataset for ingesting email and push application feedback events from Journey Optimizer.

The related schema is AJO Message Feedback Event Schema.

This query shows the counts of different email feedback status (sent, bounce, etc) for a given message:

```
select
    _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus AS feedbackStatus,
    count(1) eventCount
from ajo_message_feedback_event_dataset
where
     _experience.customerJourneyManagement.messageExecution.messageExecutionID IN ('UMA-30647505')
group by
    _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus;
```

This query shows the breakdown of counts of different email feedback status (sent, bounce, etc) by message for a given journey:

```
select
    _experience.customerJourneyManagement.messageExecution.messageExecutionID AS messageExecutionID,
    _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus AS feedbackStatus,
    count(1) eventCount
from ajo_message_feedback_event_dataset
where
     _experience.customerJourneyManagement.messageExecution.journeyVersionID IN ('0e86ac62-c315-48cc-ab4f-3f8b741ae667')
group by
    _experience.customerJourneyManagement.messageExecution.messageExecutionID,
    _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus
order by
    _experience.customerJourneyManagement.messageExecution.messageExecutionID,
    _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus
limit 100;
```

At aggregate level, domain level report (sorted by top domains): Domain Name, Message Sent, Bounces

```
SELECT split_part(_experience.customerJourneyManagement.emailChannelContext.address, '@', 2) AS recipientDomain, SUM( CASE WHEN _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus = 'sent' THEN 1 ELSE 0 END)AS sentCount , SUM( CASE WHEN _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus = 'bounce' THEN 1 ELSE 0 END )AS bounceCount FROM ajo_message_feedback_event_dataset WHERE _experience.customerjourneymanagement.messageprofile.channel._id = 'https://ns.adobe.com/xdm/channels/email' GROUP BY recipientDomain ORDER BY sentCount DESC;
```

Email sends on daily basis:

```
SELECT date_trunc('day', TIMESTAMP) AS rolluptimestamp, SUM( CASE WHEN _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus = 'sent' THEN 1 ELSE 0 END) AS deliveredcount FROM ajo_message_feedback_event_dataset WHERE _experience.customerjourneymanagement.messageprofile.channel._id = 'https://ns.adobe.com/xdm/channels/email' GROUP BY date_trunc('day', TIMESTAMP) ORDER BY rolluptimestamp ASC;
```

Find if a particular email id received an email or not and if not, then what was the error, bounce category, code:

```
SELECT _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus AS status, _experience.customerjourneymanagement.messagedeliveryfeedback.messagefailure.reason AS failurereason, _experience.customerjourneymanagement.messagedeliveryfeedback.messagefailure.type AS bouncetype FROM ajo_message_feedback_event_dataset WHERE _experience.customerjourneymanagement.messageprofile.channel._id = 'https://ns.adobe.com/xdm/channels/email' AND _experience.customerjourneymanagement.emailchannelcontext.address = 'user@domain.com' AND TIMESTAMP >= now() - INTERVAL '7' DAY ORDER BY status ASC
```

Find the list of all individual email ids which had a particular error, bounce category or code in the last x hours/days or associated with a particular message delivery:

```
SELECT _experience.customerjourneymanagement.emailchannelcontext.address AS emailid, _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus AS status, _experience.customerjourneymanagement.messagedeliveryfeedback.messagefailure.reason AS failurereason, _experience.customerjourneymanagement.messagedeliveryfeedback.messagefailure.type AS bouncetype FROM ajo_message_feedback_event_dataset WHERE _experience.customerjourneymanagement.messageprofile.channel._id = 'https://ns.adobe.com/xdm/channels/email' AND _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus != 'sent' AND TIMESTAMP >= now() - INTERVAL '10' HOUR AND _experience.customerjourneymanagement.messageexecution.messageexecutionid = 'BMA-45237824' ORDER BY emailid
```

Hard Bounce Rate at aggregate level:

```
select hardBounceCount, case when sentCount > 0 then(hardBounceCount/sentCount)*100.0 else 0 end as hardBounceRate from ( select SUM( CASE WHEN _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus = 'bounce' AND _experience.customerJourneyManagement.messageDeliveryfeedback.messageFailure.type = 'Hard' THEN 1 ELSE 0 END)AS hardBounceCount , SUM( CASE WHEN _experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus = 'sent' THEN 1 ELSE 0 END )AS sentCount from ajo_message_feedback_event_dataset WHERE _experience.customerjourneymanagement.messageprofile.channel._id = 'https://ns.adobe.com/xdm/channels/email' )
```

Permanent errors grouped by bounce code:

```
SELECT _experience.customerjourneymanagement.messagedeliveryfeedback.messagefailure.reason AS failurereason, COUNT(*) AS hardbouncecount FROM ajo_message_feedback_event_dataset WHERE _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus = 'bounce' AND _experience.customerjourneymanagement.messagedeliveryfeedback.messagefailure.type = 'Hard' AND _experience.customerjourneymanagement.messageprofile.channel._id = 'https://ns.adobe.com/xdm/channels/email' GROUP BY failurereason
```

NOTE
In some journeys,
messageID
may not be unique for each individual delivery. If a journey re-sends the same action to the same profile, the same
messageID
can be reused. Therefore, to accurately track or attribute events at the individual send level, combine the
journeyVersionID
,
journeyActionID
, and
batchInstanceID
(for batch journeys) or
identityMap
fields for more precise uniqueness.
### Identify quarantined addresses after an ISP outage isp-outage-query

In case of an Internet Service Provider (ISP) outage, you need to idenfity email addresses wrongly maked as bounces (quarantined) for specific domains, during a timeframe. To get those adresses, use the following query:

```
SELECT
    _experience.customerJourneyManagement.emailChannelContext.address AS RecipientAddress,
    timestamp AS EventTime,
    _experience.customerJourneyManagement.messageDeliveryfeedback.messageFailure.reason AS "Invalid Recipient"
FROM ajo_message_feedback_event_dataset
WHERE
    eventtype = 'message.feedback' AND
    DATE(timestamp) BETWEEN '<start-date-time>' AND '<end-date-time>' AND
    _experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus = 'bounce' AND
    _experience.customerJourneyManagement.emailChannelContext.address ILIKE '%domain.com%'
ORDER BY timestamp DESC;
```

where the format of dates is: YYYY-MM-DD HH:MM:SS.

Once identified, remove those addresses from Journey Optimizer suppression list. [Learn more](/en/docs/journey-optimizer/using/configuration/monitor-reputation/manage-suppression-list#remove-from-suppression-list).

NOTE
When referencing the identityMap in the Message Feedback Event Dataset, please note that it only reflects the identity used at runtime. For push notifications, a ‘sent’ event would rely only on the ECID linked to the push token used to send this notification while an ‘exclusion’ event could rely on a custom identity. For instance, if a profile was excluded because no push token was found, the identity used at the journey or action campaign level will be selected to register this event. If you need additional namespaces (e.g., custom IDs), join these feedback records with a profile-related dataset (eg: profile_snapshot ones) to retrieve the full identity list.
## Push tracking Experience event dataset push-tracking-experience-event-dataset

*Name in the interface: AJO Push Tracking Experience Event Dataset*

Dataset for ingesting mobile tracking experience events for push from Journey Optimizer.

The related schema is AJO Push Tracking Experience Event Schema.

Query example:

```
select _experience.customerJourneyManagement.pushChannelContext.platform, sum(pushNotificationTracking.customAction.value)  from ajo_push_tracking_experience_event_dataset
group by _experience.customerJourneyManagement.pushChannelContext.platform

select  _experience.customerJourneyManagement.pushChannelContext.platform, SUM (_experience.customerJourneyManagement.messageInteraction.offers.offerCount) from ajo_email_tracking_experience_event_dataset
  group by _experience.customerJourneyManagement.pushChannelContext.platform
```

## Journey step event journey-step-event

*Internal name: Journey Step Events (system dataset)*

Dataset for ingesting step events in the journey.

The related schema is Journey Step Event schema for Journey Orchestration.

This query shows the breakdown of action success counts by action label for a given journey:

```
select
    _experience.journeyOrchestration.stepEvents.actionName AS actionLabel,
    count(1) actionSuccessCount
from journey_step_events
where
     _experience.journeyOrchestration.stepEvents.journeyVersionID IN ('0e86ac62-c315-48cc-ab4f-3f8b741ae667')
     AND _experience.journeyOrchestration.stepEvents.actionID IS NOT NULL
     AND _experience.journeyOrchestration.stepEvents.actionType IS NOT NULL
     AND _experience.journeyOrchestration.stepEvents.actionExecutionErrorCode IS NULL
group by
    _experience.journeyOrchestration.stepEvents.actionName;
```

This query shows the breakdown of step entered counts by nodeId & nodeLabel for a given journey. nodeId is included here as nodeLabel can be the same for different journey nodes.

```
select
    _experience.journeyOrchestration.stepEvents.nodeID AS nodeID,
    _experience.journeyOrchestration.stepEvents.nodeName AS nodeLabel,
    count(1) stepEnteredCount
from journey_step_events
where
     _experience.journeyOrchestration.stepEvents.journeyVersionID IN ('0e86ac62-c315-48cc-ab4f-3f8b741ae667')
     AND _experience.journeyOrchestration.stepEvents.journeyNodeProcessed = TRUE
     AND _experience.journeyOrchestration.stepEvents.eventID IS DISTINCT FROM 'createInstance'
group by
    _experience.journeyOrchestration.stepEvents.nodeID,
    _experience.journeyOrchestration.stepEvents.nodeName;
```

This query retrieves which nodes (by nodeID and nodeName) in the journey are associated with the delivery of a message to a profile, using its profile ID and the Message Feedback Event dataset:

```
select
    _experience.journeyorchestration.stepevents.nodeID, JSE._experience.journeyorchestration.stepevents.nodeName
from journey_step_events JSE
where
    _experience.journeyOrchestration.stepEvents.actionID
    in

    (
    select
        _experience.customerJourneyManagement.messageExecution.journeyActionID
    from  ajo_message_feedback_event_dataset
    where
        _experience.customerJourneyManagement.messageProfile.messageProfileID = '<PROFILE ID>'
    group by
        _experience.customerJourneyManagement.messageExecution.journeyActionID
    )

group by
    _experience.journeyorchestration.stepevents.nodeID, JSE._experience.journeyorchestration.stepevents.nodeName
```

See also several commonly used [examples to query Journey Step Events](/en/docs/journey-optimizer/using/reporting/reports/query-examples).

Learn how to [troubleshoot discarded event types in journey_step_events](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list#discarded-events).

## Decisioning event dataset ode-decisionevents

*Name in the interface: ODE DecisionEvents (system dataset)*

Dataset for ingesting offer propositions to the users.

The related schema is ODE DecisionEvents.

This query shows all the offers returned the previous day:

```
SELECT date_format(Decision.Timestamp, 'MM/dd/yyyy') as Date
,HOUR(Decision.timestamp) as Hour
,COUNT(*)  as Count
FROM ode_decisionevents_b699fa78_efec_41b1_99fa_78efecc1b1ef_decision AS Decision
WHERE date_format(Decision.timestamp, 'MM/dd/yyyy') = date_format(CURRENT_DATE, 'MM/dd/yyyy') and Decision._experience.decisioning.propositionDetails.activity[0].id = 'xcore:offer-activity:13ab41890a335ad6'
GROUP BY date_format(Decision.Timestamp, 'MM/dd/yyyy')
,HOUR(Decision.timestamp)
ORDER BY 1, 2 DESC;
```

This query shows the number of times offers were proposed over the last 30 days of a particular activity/decision and its associated offer priority.

```
select proposedOffers.id,proposedOffers.name, po._experience.decisioning.ranking.priority, count(proposedOffers.id) as ProposedCount from (
select explode(propositionexplode.selections) AS proposedOffers from
(select explode(_experience.decisioning.propositionDetails) AS propositionexplode,timestamp FROM ode_decisionevents_itca_decisioning_20230925_235340_379  where date_format(timestamp, 'MM/dd/yyyy') >= date_format(DATE_ADD(CURRENT_DATE, -30), 'MM/dd/yyyy') and _experience.decisioning.propositionDetails.activity[0].id = 'xcore:offer-activity:12ae6f35a055c6f0')) a, decision_object_repository_personalized_offers po where proposedOffers.id LIKE 'xcore:personalized-offer%' and po._id=proposedOffers.id
group by proposedOffers.id, proposedOffers.name, po._experience.decisioning.ranking.priority;
```

## Secondary recipient feedback event dataset (BCC) bcc-feedback-event-dataset

*Name in the interface: AJO Secondary Recipient Feedback Event Dataset (system dataset). In Query Service, the dataset table may still be named ajo_bcc_feedback_event_dataset .*

Dataset for email BCC (secondary recipient) messages when BCC archiving is enabled.

Query for all BCC messages within 2 days (for a particular campaign):

```
SELECT bcc.*
FROM ajo_bcc_feedback_event_dataset AS bcc
WHERE
    bcc._experience.customerJourneyManagement.messageExecution.messageExecutionID = '<message-execution-id>' AND
    bcc.timestamp >= now() - INTERVAL '2' day;
```

Query with feedback dataset to show users who did not receive (all bounces and suppressions) and who have BCC entry for a particular message:

```
SELECT
    distinct bcc._experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress AS OriginalRecipientAddress
FROM ajo_bcc_feedback_event_dataset  AS bcc
WHERE
    bcc.timestamp > now() - INTERVAL '2' DAY AND     bcc._experience.customerJourneyManagement.messageExecution.messageExecutionID  = '<message-execution-id>' AND      bcc._experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress != '' AND
    (
            bcc._experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress NOT IN (
        SELECT distinct mfe._experience.customerJourneyManagement.emailChannelContext.address
        FROM ajo_message_feedback_event_dataset AS mfe
        WHERE
            mfe.timestamp > now() - INTERVAL '2' DAY AND
            mfe._experience.customerJourneyManagement.messageExecution.messageExecutionID  = '<message-execution-id>' AND
            mfe._experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus = 'sent'
        )
    OR     bcc._experience.customerJourneyManagement.secondaryRecipientDetail.originalRecipientAddress IN (
        SELECT distinct mfe._experience.customerJourneyManagement.emailChannelContext.address
        FROM ajo_message_feedback_event_dataset AS mfe
        WHERE
        mfe.timestamp > now() - INTERVAL '2' DAY AND
            mfe._experience.customerJourneyManagement.messageExecution.messageExecutionID  = '<message-execution-id>' AND
            mfe._experience.customerJourneyManagement.messageDeliveryfeedback.messageFailure.category = 'async' AND
            mfe._experience.customerjourneymanagement.messagedeliveryfeedback.feedbackstatus
```

## Entity Dataset entity-dataset

*Name in the interface: ajo_entity_dataset (system dataset)*

Dataset to store entity metadata for messages sent to the end user.

The related schema is AJO Entity Schema.

This dataset gives you access to marketer defined metadata which allows you to get better reporting insights when Journey Optimizer datasets are exported out for reporting visualization in external tools. This is achieved using the messageID attribute which helps stitch various datasets such as Message Feedback Dataset and Experience Event Tracking Datasets to get details of a message delivery from sending to tracking at a profile level.

**Important notes**

- An entry for a message is created only after journey or campaign is published.
- You may see the entry 30 minutes after the publication of the campaign/journey.

NOTE
For the time being, there are two entries for each message publication in the entity dataset for future compatibility reasons. This does not impact your ability to use join queries as needed across datasets to fetch the desired information.
If you want to sort, in your reports, the emails sent by a specific journey according to the action that sent them. you can join the Message Feedback dataset with the Entity dataset. The fields to use are: _experience.decisioning.propositions.scopeDetails.correlationID and _id field in entity dataset.

The following query helps you get the associated message template for a given campaign:

```
SELECT
  AE._experience.customerJourneyManagement.entities.channelDetails.template
from
  ajo_entity_dataset AE
    WHERE AE._experience.customerJourneyManagement.entities.campaign.campaignVersionID = 'd7a01136-b113-4ef2-8f59-b6001f7eef6e'
```

The following query helps get the Journey Details and email subject associated with all feedback events:

```
SELECT
  AE._experience.customerJourneyManagement.entities.journey.journeyActionName,
  AE._experience.customerJourneyManagement.entities.journey.journeyActionID,
  AE._experience.customerJourneyManagement.entities.journey.journeyVersionID,
  AE._experience.customerJourneyManagement.entities.channelDetails.email.subject
from
  ajo_entity_dataset AE
  INNER JOIN ajo_message_feedback_event_dataset MF ON AE._experience.customerJourneyManagement.entities.channelDetails.messageID = MF._experience.customerJourneyManagement.messageExecution.messageID
WHERE
  AE._experience.customerJourneyManagement.entities.channelDetails.channel._id = 'https://ns.adobe.com/xdm/channels/email'
  AND MF._experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus = 'sent'
  AND AE._experience.customerJourneyManagement.entities.journey.journeyVersionID IS NOT NULL
```

You can stitch journey step events, Message Feedback and tracking datasets to get the stats for a particular profile:

```
SELECT
  AE._experience.customerJourneyManagement.entities.journey.journeyActionName,
  AE._experience.customerJourneyManagement.entities.journey.journeyActionID,
  AE._experience.customerJourneyManagement.entities.journey.journeyVersionID,
  AE._experience.customerJourneyManagement.entities.channelDetails.email.subject,
    JE._EXPERIENCE.JOURNEYORCHESTRATION.STEPEVENTS.PROFILEID,
    JE._EXPERIENCE.JOURNEYORCHESTRATION.STEPEVENTS.NODENAME
from
  ajo_entity_dataset AE
  INNER JOIN ajo_message_feedback_event_dataset MF
    ON AE._experience.customerJourneyManagement.entities.channelDetails.messageID = MF._experience.customerJourneyManagement.messageExecution.messageID
    INNER JOIN journey_step_events JE
    ON AE._experience.customerJourneyManagement.entities.journey.journeyActionID = JE._experience.journeyOrchestration.stepEvents.actionID
WHERE
  AE._experience.customerJourneyManagement.entities.channelDetails.channel._id = 'https://ns.adobe.com/xdm/channels/email'
  AND MF._experience.customerJourneyManagement.messageDeliveryfeedback.feedbackStatus = 'sent'
  AND AE._experience.customerJourneyManagement.entities.journey.journeyVersionID IS NOT NULL
```

recommendation-more-help
