---
title: "Create journey reports design-jo-reports"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/reporting/reports/sharing-overview"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:15.483014+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create journey reports design-jo-reports

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Reporting](#)

CREATED FOR:

- Experienced
- Developer
- Admin

In addition to [real-time reports](/en/docs/journey-optimizer/using/reporting/live-report/live-report) and built-in [reporting capabilities](/en/docs/journey-optimizer/using/reporting/channel-report/report-gs-cja), Journey Optimizer can automatically send journey performance data to Adobe Experience Platform so it can be combined with other data for analysis purposes.

NOTE
This feature is activated by default on all instances for journey steps events. You cannot modify or update the schemas and datasets that have been created during provisioning for step events. By default, these schemas and datasets are in read-only mode.
For example, you have set up a journey that sends multiple emails. This capability allows you to combine Journey Optimizer data with downstream event data like how many conversions occurred, how much engagement happened on the website, or how many transactions happened in the store. The journey information can be combined with data on Adobe Experience Platform, either from other digital properties or from offline properties to give a more comprehensive view of performance.

Journey Optimizer automatically creates the necessary schemas and streams into datasets to Adobe Experience Platform for each step an individual takes in a journey. A step event corresponds to an individual moving from one node to another in a journey. For example, in a journey that has an event, a condition and an action, three step events are sent to Adobe Experience Platform.

NOTE
In addition to profile-level step events, the system also generates internal events for
Read Audience
activities. These events, called
segmentExportJob
events, record the lifecycle of the Read Audience node (such as export job creation, queuing, completion, and errors) and are generated per Read Audience activity, not per individual profile. As a result, these events may not have an associated profile identifier (UPMID). These internal events are useful for monitoring and troubleshooting Read Audience performance and can be queried using the fields documented in the
serviceEvents section
. For query examples on how to work with segmentExportJob events, see
Queries related to the Read Audience
.
There are cases where multiple events can be created for the same node. For example, in the case of the Wait activity:

- One event is generated when the profile enters the wait (journeyNodeProcessed attribute is equal to false)
- One event is generated when the profile exits it (journeyNodeProcessed attribute is equal to true)

The list of XDM fields that are passed is comprehensive. Some contain system generated codes and others have human readable friendly names. Examples include the label of the journey activity or the step status: how many times an action timed out or ended in error.

CAUTION
Datasets cannot be turned on for real time profile service. Please make sure that the
Profile
toggle is turned off.
Journey Optimizer sends data as it occurs, in streaming. You can query this data using the Query Service. You can connect to Customer Journey Analytics or other BI tools to view data related to these steps.

The following schemas are created:

- Journey Step Event schema for Journey Orchestration – Journey step event that is tied to a Journey Metadata.
- Journey schema with Journey Fields for Journey Orchestration – Journey Metadata to describe Journeys.

The following datasets are passed:

- Journey Step Events
- Journeys

The lists of XDM fields passed to Adobe Experience Platform are detailed here:

- [Step event field list](/en/docs/journey-optimizer/using/reporting/reports/sharing-field-list)
- [Legacy step event fields](/en/docs/journey-optimizer/using/reporting/reports/legacy-step-event-fields/sharing-legacy-fields)

## Integration with Customer Journey Analytics integration-cja

Journey Optimizer step events can be linked to other datasets in [Adobe Customer Journey Analytics](/en/docs/analytics-platform/using/cja-overview/cja-overview#_blank).

The general workflow is:

- Customer Journey Analytics ingests the “Journey Step Event” dataset.
- The **profileID** field in the associated “Journey Step Event schema for Journey Orchestration” is defined as an Identity field. In Customer Journey Analytics, you can then link this dataset to any other dataset that has the same value as the person based identifier.
- To use this dataset in Customer Journey Analytics, for cross-channel journey analysis, refer to [Customer Journey Analytics documentation](/en/docs/analytics-platform/using/cja-usecases/cross-channel/cross-channel#_blank).

➡️ [Work with Customer Journey Analytics](/en/docs/journey-optimizer/using/reporting/channel-report/cja-ajo#_blank)

recommendation-more-help
