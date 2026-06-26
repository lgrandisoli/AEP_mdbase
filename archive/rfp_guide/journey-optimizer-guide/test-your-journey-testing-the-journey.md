---
title: "Test your journey testing_the_journey"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:59.953868+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Test your journey testing_the_journey

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Test Profiles](#)

CREATED FOR:

- Intermediate
- User

Once you have built your journey, you can test it before publishing. Adobe Journey Optimizer offers “Test mode” as a way to view test profiles as they move along the journey, detecting potential errors before activation. Running quick tests allows you to check that journeys operate correctly so that you can publish them with confidence.

Only test profiles can enter a journey in test mode. You can either create new test profiles or turn existing profiles into test profiles. Learn more about test profiles in [this section](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles).

Adobe Journeys Optimizer offers two ways to test and validate your journey:

- Simulation : Set the journey to Simulation and use simulated users (temporary profiles you create or generate on the fly without pre-created profiles in Adobe Experience Platform).
- Test mode : Persistent profiles explicitly flagged as test profiles in Adobe Experience Platform. They can be reused across multiple test sessions. This method is recommended for testing with consistent, predefined profile data. Learn how to create test profiles .

NOTE
Before testing your journey, you must resolve all errors if any. Learn how to check errors before testing in
this section
. If test profiles fail to progress in test mode, see
troubleshooting test mode transitions
.
## Important notes important_notes

Review these notes before running tests in your journey.

### General limitations

- **Test profiles only** - Only individuals flagged as “test profiles” in the Real-time Customer Profile Service can enter a journey in test mode. [Learn how to create test profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles).
- **Namespace requirement** - Test mode is available only for draft journeys that use a namespace. Test mode needs to check if a person entering the journey is a test profile or not and thus must be able to reach Adobe Experience Platform.
- **Profile limit** - A maximum of 100 test profiles can enter a journey during a single test session.
- **Event triggering** - Events can only be fired from the interface. Events cannot be fired from external systems using an API.
- **Custom upload audiences** - Journey test mode does not support [custom upload audience](/en/docs/journey-optimizer/using/audiences-profiles-identities/audiences/create/custom-upload) attribute enrichment.

### Behavior during and after testing

- **Disabling test mode** - When you disable test mode, all profiles currently in or previously entered in the journey are removed, and reporting is cleared.
- **Reactivation flexibility** - You can enable and disable test mode as many times as needed.
- **Automatic deactivation** - Journeys that remain inactive in test mode for **over a week** automatically revert to Draft status to optimize performance and prevent obsolete resource usage.
- **Editing and publishing** - While test mode is active, you cannot modify the journey. You can, however, directly publish the journey, no need to deactivate the test mode before.

### Execution

- **Split behavior** - When the journey reaches a split, the top branch is always selected. Reorder branches if you want a different path tested.
- **Event timing** - If the journey includes multiple events, trigger each event in sequence. Sending an event too early (before the first wait node finishes) or too late (after the configured timeout) will discard the event. The profile will then be sent to a timeout path. Always confirm any references to event payload fields remain valid by sending the payload within the defined window.
- **Active date window** - Make sure the journey’s configured [start and end dates/time](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#dates) window includes the current time when initiating test mode. Otherwise, triggered test events are silently discarded. Learn more about troubleshooting this issue [on this page](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution#troubleshooting-test-transitions).
- **Reaction events** - For reaction events with a timeout, the minimum and default wait time is 40 seconds.
- **Test datasets** - Events triggered in test mode are stored in dedicated datasets labeled as follows: JOtestmode - <schema of your event>
- **Shared infrastructure** - Test Mode runs on the same infrastructure as production. During high traffic periods, you may notice delays in email sends or event processing. In this case, check platform traffic dashboards or retry your tests during off-peak hours.

## Activate the test mode

Use the **Test mode** method when you want to test your journey with pre-existing test profiles that you have already created in Adobe Experience Platform.

- To activate the test mode, click the Simulate button, and select Test mode .
- If the journey has at least one Wait activity, set the Wait time parameter to define the time that each wait activity and event timeout will last in test mode. The default time is 10 seconds for waits and event timeouts. This will ensure that you get the test results quickly. note NOTE When a reaction event with a timeout is used in a journey, the wait time default and minimum value is 40 seconds. See this section .
- Use the Trigger an event button to configure and send events to the journey.
- Configure the different fields expected. In the Profile Identifier field, enter the value of the field used to identify the test profile. It can be the email address, for example. Make sure to send events related to test profiles. See this section .
- After the events are received, click the Show log button to view the test result and verify them. See this section .
- If there is any error, deactivate the test mode, modify your journey and test it again. Once tests are done, you can publish your journey. See this page .

## Worked example: validate a simple journey test-walkthrough

The following example walks through testing a journey that starts with a unitary event, sends an email, waits 10 minutes, then sends a push notification.

To validate the journey end to end:

- Activate test mode by clicking Test mode in the top-right corner. The canvas switches to test mode and a Trigger an event button appears.
- Set Wait time to 10 seconds so the wait node completes quickly during testing.
- Click Trigger an event , select your event, and enter a test profile identifier (for example, the email address of a profile flagged as a test profile in Adobe Experience Platform).
- Click Send . The visual flow appears on the canvas and turns green as the profile progresses through each step.
- Click Show log and confirm the following in the JSON output: currentstep matches the activity you expect the profile to be at. phase shows running while the profile is in a wait node, and finished when it reaches the end. No actionExecutionErrors entries are present.
- After 10 seconds, refresh the log. The profile should have advanced past the wait node and triggered the push action.
- When all steps show finished and no errors are logged, deactivate test mode and publish the journey.

TIP
If the profile does not appear in the log at all, check that:
- The profile identifier you entered is flagged as a test profile in Adobe Experience Platform.
- The journey’s configured start and end dates include the current time. Events triggered outside this window are silently discarded. [Learn more](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution#troubleshooting-test-transitions).

## Trigger your events firing_events

Use the **Trigger an event** button to configure an event that will make a person enter the journey.

### Prerequisites trigger-events-prerequisites

As a prerequisite, you must know which profiles are flagged as test profiles in Adobe Experience Platform. Indeed, the test mode only allows these profiles in the journey.

The event must contain an ID. The expected ID depends on the event configuration. It can be an ECID or an email address for example. The value of this key needs to be added in the **Profile Identifier** field.

If your journey fails to enable test mode with error ERR_MODEL_RULES_16, ensure the event used includes an [identity namespace](/en/docs/journey-optimizer/using/audiences-profiles-identities/get-started-identity) when using a channel action.

The identity namespace is used to uniquely identify the test profiles. For example, if email is used to identify the test profiles, the identity namespace **Email** should be selected. If the unique identifier is the phone number, then the identity namespace **Phone** should be selected.

NOTE
- When you trigger an event in test mode, a real event is generated, meaning it will also hit other journeys listening to this event.
- Ensure that each event in test mode is triggered in the correct order and within the configured waiting window. For example, if there is a 60-second wait, the second event must be triggered only after that 60-second wait has elapsed and before the timeout limit expires.

### Event configuration trigger-events-configuration

If your journey contains several events, use the drop-down list to select an event. Then, for each event, configure the fields passed and the execution of the event sending. The interface helps you pass the right information in the event payload and ensures the information type is correct. Test mode saves the last parameters used in a test session for later use.

The interface allows you to pass simple event parameters. If you want to pass collections or other advanced objects in the event, you can select **Code View** to see the entire code of the payload and modify it. For example, you can copy and paste event information prepared by a technical user.

A technical user can also use this interface to compose event payloads and trigger events without having to use a third-party tool.

When clicking the **Send** button, the test begins. The progression of the individual in the journey is represented by a visual flow. The path progressively turns green as the individual moves across the journey. If an error occurs, a warning symbol is displayed on the corresponding step. You can place the cursor on it to display more information about the error and access full details (when available).

When you select a different test profile in the event configuration screen and run the test again, the visual flow is cleared and shows the path of the new individual.

When opening a journey in test, the displayed path corresponds to the last test executed.

## Test mode for rule-based journeys test-rule-based

The test mode is also available for journeys that use a rule-based event. For more information on rule-based events, refer to [this page](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).

When triggering an event, the **Event configuration** screen allows you to define the event parameters to pass in the test. You can view the event ID condition by clicking the tooltip icon in the top right corner. A tooltip is also available next to each field that is part of the rule evaluation.

## Test mode for business events test-business

When using a [business event](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events), use the test mode to trigger a single test profile entrance in the journey, simulate the event and pass the right profile ID. You have to pass the event parameters and the identifier of the test profile that will enter the journey in test. In test mode, there is no “Code view” mode available for journeys based on business events.

Note that when you first trigger a business event, you cannot change the business event definition in the same test session. You can only make the same individual or a different individual enter the journey passing the same or another identifier. If you want to change business event parameters, you must stop and start again test mode.

## View logs viewing_logs

The **Show log** button allows you to view the test results. This page displays the journey’s current information in JSON format. A button allows you to copy entire nodes. You need to manually refresh the page to update the journey’s test results.

NOTE
In the test logs, in case of an error when calling a third-party system (data source or action), the error code and error response are displayed.
The number of individuals (technically called instances) currently inside the journey are displayed. The following information is displayed for each individual:

- *Id*: the individual’s internal ID in the journey. This can be used for debugging purposes.
- *currentstep*: the step where the individual is at in the journey. We recommend adding labels to your activities to identify them more easily.
- *currentstep* > phase: the status of the individual’s journey (running, finished, error or timed out). See below for more information.
- *currentstep* > *extraInfo*: description of the error and other contextual information.
- *currentstep* > *fetchErrors*: information on fetch data errors that occurred during this step.
- *externalKeys*: the value for the key formula defined in the event.
- *enrichedData*: the data that the journey has retrieved if the journey uses data sources.
- *transitionHistory*: the list of steps that the individual followed. For events, the payload is displayed.
- *actionExecutionErrors* : information on the errors that occurred.

Here are the different statuses of an individual’s journey:

- *Running*: the individual is currently in the journey.
- *Finished*: the individual is at the end of the journey.
- *Error*: the individual is stopped in the journey because of an error.
- *Timed out*: the individual is stopped in the journey because of a step which took too much time.

When an event is triggered using the test mode, a dataset is automatically generated with the name of the source.

The test mode automatically creates an Experience Event and sends it to Adobe Experience Platform. The name of the source for this experience Event is “Journey Orchestration Test Events”.

recommendation-more-help
