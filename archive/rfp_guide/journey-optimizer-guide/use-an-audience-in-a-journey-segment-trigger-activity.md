---
title: "Use an audience in a journey segment-trigger-activity"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:42.657635+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use an audience in a journey segment-trigger-activity

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)
- [Audiences](#)

CREATED FOR:

- Intermediate
- User

Use the Read Audience activity to start journeys with defined audiences. You choose the audience and when it runs; then use [conditions](#audience-targeting-in-journeys), timers, and actions to personalize each profile’s path.

## About the Read Audience activity about-segment-trigger-activity

The **Read Audience** activity is the journey entry-point activity that adds all profiles from a selected Adobe Experience Platform audience to a journey. You can run the entrance once or on a recurring schedule. In APIs and technical references this activity is also referred to as segment-trigger or audience-based journey entry.

**When to use Read Audience vs Audience Qualification**

Use
Read Audience
when
Use
Audience Qualification
when
You want to run a journey once or on a schedule (batch).
You need profiles to enter the journey in real time as they qualify.
Your audience is batch-evaluated (e.g. daily snapshot).
Your audience is streaming or event-based.
You are okay with a delay between audience evaluation and journey entry.
You need immediate entry when a profile qualifies.
TIP
Real-world examples
- **Weekly newsletter** → Read Audience. Your audience is a daily batch snapshot. You schedule the journey every Monday at 9 AM. All qualified profiles enter together.
- **Loyalty tier upgrade** → Audience Qualification. As soon as a profile reaches Gold status in a streaming audience, they enter the journey immediately to receive a congratulations email.
- **Re-engagement series** → Read Audience. You run a recurring journey every 30 days targeting profiles inactive for 90+ days.

**Key limits:** One Read Audience per journey (must be the first activity); one audience per activity; up to five concurrent Read Audience runs per organization; 20,000 profiles per second per sandbox; 12-hour job timeout. Full details in [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#read-segment-g).

**Prerequisites:** An Adobe Experience Platform audience that is built and evaluated (Realized status), a people-based identity namespace selected for the journey, and—for recurring runs—understanding of [scheduling and throughput limits](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#read-segment-g).

For example, the Luma app opening and checkout audience created in the [Build audiences](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences) use case can be used as the entry point. All qualified profiles enter the journey and progress through individualized paths using conditions, timers, events, and actions.

➡️ [Discover this feature in video](#video)

CAUTION
- Before using the Read audience activity, [read the Guardrails and Limitations](#must-read).

## Configure the activity configuring-segment-trigger-activity

You will set: **Audience** (mandatory), **Namespace** (mandatory), **Reading rate** (mandatory, default 5,000/s), and **Schedule** (when the journey runs). Optionally add a **Label** and **Supplemental identifier**. The steps below walk you through each setting.

### Add activity and select audience add-activity-and-select-audience

- Unfold the Orchestration category and drop a Read Audience activity into your canvas. The activity must be positioned as the first step of a journey.
- Add a Label to the activity (optional). An optional label helps you identify the activity in reporting and in test mode logs.
- In the Audience field, choose the Adobe Experience Platform audience that will enter the journey, then click Save . You can select any Adobe Experience Platform audience generated using segment definitions . note NOTE In addition, you can target Adobe Experience Platform audiences created using audience compositions . You can also target audiences uploaded from a CSV file . Learn more about how to generate and target audiences in Journey Optimizer . Note that you can customize the columns displayed in the list and sort them. Once the audience is added, the Copy button allows you to copy its name and ID: {"name":"Luma app opening and checkout","id":"8597c5dc-70e3-4b05-8fb9-7e938f5c07a3"} note NOTE Only the individuals with the Realized audience participation status will enter the journey. For more on how to evaluate an audience, refer to the Segmentation Service documentation .
- In the Namespace field, choose the namespace to use in order to identify the individuals. By default, the field is pre-filled with the last used namespace. Learn more about namespaces . note NOTE Individuals belonging to an audience that does not have the selected identity (namespace) among their different identities cannot enter the journey. You can only select a people-based identity namespace. If you have defined a namespace for a lookup table (for example: ProductID namespace for a Product lookup), it will not be available in the Namespace dropdown list.

### Supplemental identifier read-audience-supplemental-id

You can optionally enable **Use a supplemental identifier** to run the journey in the context of a secondary identifier (for example, an order ID or booking ID) in addition to the profile ID. This allows multiple entrances of the same profile when the supplemental identifier differs.

[Learn how to use supplemental identifiers in journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/supplemental-identifier). For Read audience journeys, the supplemental identifier must be a profile attribute; the reading rate is limited to 500 profiles per second when supplemental ID is used.

### Guardrails and recommendations must-read

All guardrails and limitations for the **Read Audience** activity (concurrency, throughput, one audience per activity, job timeout, retries, and more) are listed in [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#read-segment-g).

**Recommendations**

- As a best practice, use batch audiences in a **Read audience** activity for reliable and consistent counts. Read audience is designed for batch use cases. If your use case needs real-time data, use the [Audience qualification](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events) activity instead.
- Audiences [imported from a CSV file](/en/docs/experience-platform/segmentation/ui/overview#import-audience) or resulting from [composition workflows](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/get-started-audience-orchestration) can be selected in the **Read Audience** activity. These audiences are not available in the **Audience Qualification** activity.
- For information about audience snapshot timing, batch segmentation completion windows, and how to ensure your journey always runs on the freshest data, see [Timing and data propagation](#timing-and-data-propagation). For recurring journeys, consider enabling the **Trigger after batch audience evaluation** option to automatically delay execution until the latest audience snapshot is ready. [Learn more](#schedule).

CAUTION
Guardrails for Real-time Customer Profile data and segmentation
also apply to Adobe Journey Optimizer.
**Next:** Set the [reading rate](#profile-entry-and-reading-rate) and [schedule](#schedule), then [test and publish](#testing-publishing).

### Profile entry and reading rate profile-entry-and-reading-rate

Set the **Reading rate** (mandatory). This is the maximum number of profiles that can enter the journey per second. This rate applies only to this activity and no others in the journey. If you want to define a throttling rate on custom actions, for example, you need to use the throttling API. Refer to this [page](/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling).

This value is stored in the journey version payload. The default value is 5,000 profiles per second. You can modify this value from 500 to 20,000 profiles per second.

NOTE
The overall reading rate per sandbox is set to 20,000 profiles per second. Therefore, the reading rate of all the read audiences that run simultaneously in the same sandbox add up to at most 20,000 profiles per second. You cannot modify this cap. Learn more about journey processing rates and throughput in
this section
.
### Schedule the journey schedule

By default, journeys are configured to run once. To define a specific date/time and frequency at which the journey should run, follow the steps below.

NOTE
Journey status and the 91-day global timeout:
- **One-shot** Read audience journeys move to the **Finished** status 91 days ([journey global timeout](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#global_timeout)) after the journey execution.
- **Recurring** Read audience journeys with no end date **remain Live** as long as the journey is published. They move to **Finished** status 91 days after the execution of their **last occurrence**.
- The 91-day timeout applies to individual **profiles** flowing through the journey (maximum time a profile can remain active), not to the journey’s Live status.
- The 91-day **reporting window** is a separate concept: the UI shows performance data for approximately the last 91 days. Older data is not accessible in the UI but the journey continues to run. [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#global_timeout)

- In the Read audience activity properties, select Edit journey schedule .
- The journey’s properties display. In the Scheduler type drop-down list, select the frequency at which you want the journey to run.

For recurring journeys, specific options are available to help you manage the entry of profiles into the journey. Expand the sections below for more information on each option.

Incremental read
When a journey with a recurring **Read audience** executes for the first time, all the profiles in the audience enter the journey. This option allows you to target, after the first occurrence, only the individuals who entered the audience since the last execution of the journey.

When using this option, the system looks back **24 hours** from the time of the last audience evaluation job performed by Adobe Experience Platform’s segmentation service.

After segmentation completes, a profile snapshot export job begins which allows Journey Optimizer to detect and process new profiles. If the journey is scheduled between these two jobs, the incremental read will not pick up profiles that became members of the audience since the last execution of the journey.

To minimize the risk of missing profiles:

- Enable the **Trigger after batch audience evaluation** option to extend the look-back period to the time of the last successful journey execution, regardless of how long ago it occurred
- Schedule journeys to run well after daily batch segmentation jobs complete (typically 2-3 hours buffer)
- For time-critical use cases requiring immediate profile inclusion, consider using [Audience Qualification](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events) activities with streaming audiences instead

| note caution |
| --- |
| CAUTION |
| If you are targeting a [custom upload audience](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences#about-segments) in your journey, profiles are only retrieved on the first recurrence when this option is enabled in a recurring journey. These audiences are fixed. |

Force reentrance on recurrence
This option allows you to make all profiles still present in the journey automatically exit it on the next execution.

For example, if you have a 2-day wait in a daily recurring journey, activating this option moves profiles to the next journey execution. This happens the day after, whether they are in the next run audience or not.

If the lifespan of your profiles in this journey may be longer than the recurrence frequency, do not activate this option to make sure that profiles can finish their journey.

Trigger after batch audience evaluation
For journeys scheduled daily and targeting batch audiences, you can define a time window of up to 6 hours for the journey to wait for fresh audience data from batch segmentation jobs. If the segmentation job completes within the time window, the journey triggers. Otherwise, it skips the journey until its next occurrence. This option ensures journeys run with accurate and up-to-date audience data.

For example, if a journey is scheduled for 6 PM daily, you can specify a number of minutes or hours to wait before the journey runs. When the journey wakes up at 6 PM, it checks for a fresh audience, meaning an audience newer than the one used in the previous journey execution. During the specified time window, the journey will execute immediately upon detecting the fresh audience. If no fresh audience is detected, the journey execution will be skipped for that day.

## Test and publish the journey testing-publishing

The **Read Audience** activity allows you to test the journey on a unitary profile.

To do this, activate the test mode.

Configure and run the test mode as usual. [Learn how to test a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey).

Once the test is running, the **Show logs** button allows you to see the test results. For more on this, refer to [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey#viewing_logs)

Once the tests are successful, you can publish your journey (see [Publishing the journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey)). Individuals belonging to the audience will enter the journey on the date/time specified in the journey’s properties **Scheduler** section.

NOTE
For recurring audience-based journeys, the journey will automatically close once its last occurrence is executed. If no end date/time has been specified, you will have to close the journey to new entrances manually to end it.
## Audience targeting in journeys audience-targeting-in-journeys

Audience-based journeys always start with a **Read Audience** activity to retrieve individuals belonging to an Adobe Experience Platform audience. Those profiles are read once or on a recurring schedule.

After they enter the journey, you orchestrate them using **Condition** activities: segment by attributes or behavior, exclude part of the population, or merge branches back together (union). The sections below describe each pattern.

**Segmentation**

You can use conditions to perform segmentation using the **Condition** activity. For example, you can make VIP persons take a particular path and non-VIP flow in another path.

The segmentation can be based on:

- data source data
- the context of events part of the journey data, for example: did a person click on the message received an hour ago?
- a date, for example: are we in June when a person goes through the journey?
- a time, for example: is it morning in the person’s timezone?
- an algorithm splitting the audience flowing in the journey based on a percentage, for example: 90% - 10% to exclude a control group

NOTE
When using the “Daily” scheduler type with a
Read Audience
activity, you can define a time window for the journey to wait for fresh audience data. This ensures accurate targeting and prevents issues caused by delays in batch segmentation jobs.
Learn how to schedule a journey
**Exclusion**

The same **Condition** activity used for segmentation (see above) also allows you to exclude part of the population. For example, you can exclude VIP persons by making them flow into a branch with an end step right after.

This exclusion could happen right after audience retrieval, for population counting purposes or along a multistep journey.

**Union**

Journeys allow you to create N branches and join them together after a segmentation. As a result, you can make two audiences return to a common experience.

For example, after following a different experience during ten days in a journey, VIP and non-VIP customers can return to the same path. After a union, you can split the audience again by performing a segmentation or an exclusion.

## Troubleshooting audience-count-mismatch

This section helps you resolve **audience count mismatches** (fewer or more profiles entering than expected), **zero profiles processed** (Read Audience alert or no entries), and **delayed or missing entries** (timing and data propagation).

NOTE
When a Read Audience activity executes, the system generates internal events (called
segmentExportJob
events) to track the lifecycle of the audience export operation. These events are recorded at the activity level, not per individual profile, and can be queried for monitoring and troubleshooting purposes. Learn more about
querying Read Audience events
.
**Find your issue:**

Symptom
Go to
Fewer (or more) profiles entered than the audience size
Timing and data propagation
,
Data validation and monitoring
Read Audience processed zero profiles; alert fired
Zero profiles processed
Entries delayed or missing for batch audiences
Timing and data propagation
Need to verify segment job status or namespace
Data validation and monitoring
### Zero profiles processed zero-profiles-processed

If the **Read Audience** activity has not processed any profile (e.g. you see the [Read Audience alert](/en/docs/journey-optimizer/using/monitor/monitor-alerts-errors/alerts#alert-read-audiences)):

- **Check if the audience is empty** – In Adobe Experience Platform, verify the audience size and that profiles are in **Realized** status. An empty or not-yet-evaluated audience will result in zero entries.
- **Check namespace** – The namespace selected in the Read Audience activity must be present on the profiles in your audience. Profiles without that identity cannot enter the journey. [Learn more about namespaces](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-creating#select-the-namespace).
- **Review Alerts and retries** – Failures are reported in **Alerts**. The system retries export job creation every 10 minutes for up to 1 hour. [Learn more about retries and alerts](#read-audience-retry).

If the issue persists after these checks, see [Timing and data propagation](#timing-and-data-propagation) and [Data validation and monitoring](#data-validation-and-monitoring) for batch and configuration causes.

### Timing and data propagation timing-and-data-propagation

- Batch segmentation job completion : For batch audiences, ensure that the daily batch segmentation job has completed and snapshots are updated before the journey runs. Batch audiences become ready for use approximately 2 hours after segmentation job completion. Learn more about audience evaluation methods .
- Data ingestion timing : Verify that profile data ingestion has fully completed before the journey execution. If profiles were ingested shortly before the journey starts, they may not be reflected in the audience yet. Learn more about data ingestion in Adobe Experience Platform .
- Use “Trigger after batch audience evaluation” option : For daily scheduled journeys using batch audiences, consider enabling the Trigger after batch audience evaluation option. This ensures the journey waits for fresh audience data (up to 6 hours) before executing. Learn more about scheduling
- Add a Wait activity : For streaming audiences with recently ingested data, consider adding a Wait activity at the beginning of the journey to allow time for data propagation and profile qualification. Learn more about the Wait activity
- inAudience() condition timing: When using inAudience() in a condition node within a Read Audience journey, segment membership is read from the batch projection of the profile. Data in this projection is refreshed within 2 hours after ingestion. For full details on propagation timing scenarios, refer to the inAudience function documentation .

### Data validation data-validation-and-monitoring

- Check segmentation job status : Monitor batch segmentation job completion times in the Adobe Experience Platform monitoring dashboard . Use it to verify when audience data is ready.
- Verify merge policies : Ensure that the merge policy configured for your audience matches the expected behavior for combining profile data from different sources. Learn more about merge policies in Adobe Experience Platform .
- Review segment definitions : Confirm that segment definitions are configured correctly and include all expected qualification criteria. Learn more about building audiences . Pay special attention to: Time-based conditions that may exclude profiles based on event timestamps Attribute qualifications that depend on recently updated data Streaming vs. batch evaluation methods
- Validate namespace configuration : Ensure the namespace selected in the Read Audience activity matches the primary identity used by profiles in your audience. Profiles without the selected namespace will not enter the journey. Learn more about identity namespaces .

### Best practices

- Schedule journeys after segmentation : For batch audiences, schedule journey execution at least 2-3 hours after the typical batch segmentation job completion time. Learn more about journey scheduling
- Use streaming audiences for real-time use cases : If you need immediate profile qualification and journey entry, use Audience Qualification activities with streaming audiences instead of Read Audience with batch audiences.
- Test with smaller audiences first : Before launching large-scale journeys, test with a smaller subset to validate that counts match expectations. Learn how to test a journey
- Monitor regularly : Set up regular monitoring of audience sizes and journey entry metrics to detect discrepancies early. Learn more about journey processing rates and entry management .

### When to contact support

If count mismatches or zero-profile runs persist after following the steps above, contact Adobe support. Have ready: audience name/ID, journey name/ID, scheduled run time(s), sandbox, and a short description of the discrepancy (e.g. “Audience shows 10K realized, only 2K entered the journey on [date]”).

## Retries read-audience-retry

Retries are applied by default on audience-triggered journeys (starting with a **Read Audience** or a **Business Event**) while retrieving the export job. If an error occurs during the export job creation, retries will be made every 10mn, for 1 hour max. After that, we will consider it as a failure. Those types of journeys can therefore be executed up to 1 hour after the scheduled time.

Unsuccessful **Read Audience** triggers are captured and displayed in **Alerts**. The **Read Audience alert** warns you if a **Read Audience** activity has not processed any profile 10 minutes after the scheduled execution time. This failure can be caused by technical issues or an empty audience. If the failure is due to technical issues, retries can still occur depending on the issue type. For example, if export job creation fails, we retry every 10 minutes for up to 1 hour. [Learn more](/en/docs/journey-optimizer/using/monitor/monitor-alerts-errors/alerts#alert-read-audiences)

For the full list of Read Audience guardrails (including retry and throughput limits), see [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#read-segment-g).

## Related topics

- [Build audiences](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/about-audiences)
- [Audience Qualification activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/audience-qualification-events)
- [Use supplemental identifiers in journeys](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/supplemental-identifier)
- [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails#read-segment-g)
- [Journey processing rates and entry management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management)
- [Test a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)
- [Publish a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey)

## How-to video video

Understand the applicable use cases for a journey that is triggered by the read audience activity. Learn how to build batch-based journeys and which best practices to apply.

https://video.tv.adobe.com/v/3424997?quality=12&learn=on
recommendation-more-help
