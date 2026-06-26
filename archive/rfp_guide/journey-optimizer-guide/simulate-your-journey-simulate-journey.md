---
title: "Simulate your journey simulate-journey"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/simulate-journey"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:28.433058+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

[Limited Availability]{class="badge informative"}

# Simulate your journey simulate-journey

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Test Profiles](#)

CREATED FOR:

- Intermediate
- User

IMPORTANT
This capability is available to all customers as a Limited Availability with essential capabilities.
You can set the journey to **Simulation** in addition to **Draft**, **Test mode**, and **Live**. In Simulation, you test with **simulated users**: temporary profile-like entities you add, without using persistent test profiles in Adobe Experience Platform.

Adobe Journey Optimizer offers two ways to test and validate your journey:

- Simulation : Use the Simulation journey feature and simulated users for quick runs without pre-created profiles in Adobe Experience Platform.
- Test mode : Use persistent profiles flagged as test profiles in Adobe Experience Platform, reusable across sessions. Choose this approach when you need consistent, predefined data. Learn how to create test profiles .

Note that Journey Simulation is in **Limited availability**. To share feedback and help us improve the experience, open **Feedback** from the top bar.

## Create and manage simulated users test-users

IMPORTANT
You need the
Simulate journeys
permission to access the
Simulation
feature.
Learn more
Simulated users are temporary profile-like entities you define in **Simulation settings**. This section covers how to create them, from the UI or a JSON file, save them for reuse, adjust or remove them from the list, and send them into the journey.

### Create simulated users

The following steps show you how to create simulated users from the UI or by importing a JSON file.

- From your Journey, open Simulate and choose Simulation .
- Click Create Simulated Users to create new users and select whether to create users from the UI or import them from JSON. To reuse simulated users instead, click Select simulated users and choose entries you saved earlier.
- If you create simulated users from JSON, update the corresponding fields with your simulated user data.
- If you create simulated users from UI, enter a Display name and Description to identify this simulated user. Then, select the attributes from the Union schema that you want to populate for this user.
- Click add Audience membership to simulate segment memberships.
- Click Add profile to create multiple simulated users in a single session.
- For each simulated user you added in this session, you can use the following actions: Duplicate : Adds a new simulated user that replicates the completed configuration of an existing entry, you can then edit the duplicate as needed. Apply to all : Propagates the attribute values or settings from one simulated user to every other simulated user in the list. Delete : Removes the selected simulated user from the list.
- Click Save to store one or more simulated users for future use.
- After you save, the simulated users you created appear in the Test users list. For each entry, open the options menu and select one of the following: : Update the simulated user’s details. : Run the simulation for this simulated user only. : Remove the user from this list. The simulated user is not deleted and remains available in the Simulated Users selection.
- If your journey includes a Wait activity, open the Test settings tab to fine-tune how long that wait lasts during the simulation.
- Click Send all to send every simulated users in the list into the journey. A Simulated users have been sent successfully. confirmation message appears when the simulated users successfully enter the journey.
- Access the Results tab to open the execution log and review how each step ran. For more information, see View Results .

After you validate the journey in **Simulation**, review the **Results** log. If errors appear, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again until the run looks correct. You can then publish the journey. See [Publish your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey).

### Select simulated users

Simulated users that you create manually are stored and can be selected from this list when Simulation is enabled on other journeys.

- Set the journey to Simulation . Open the Simulate entry point and choose Simulation so the journey uses the Simulation feature, for example alongside Test mode or Live, depending on your workspace.
- In the Simulation settings panel, you can either select previously created simulated users clicking Select simulated users .
- Select from the list of simulated users that were previously created and saved.
- Once you have selected your simulated users, they are now available in the Test users list. From the options menu, choose between the following option: to edit users and change its details. to send your simulation to only one simulated user. to clear your simulated users from the list. Note that clearing it does not delete it, it can still be selectable from the Simulated users list.
- Click Send all to send every simulated users in the list into the journey. A Simulated users entered the journey successfully. confirmation message appears when the simulated users successfully enter the journey.
- Access the Results tab to open the execution log and review how each step ran. For more information, see View Results .

After you validate the journey in **Simulation**, review the **Results** log. If errors appear, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again until the run looks correct. You can then publish the journey. See [Publish your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey).

## Trigger your events firing_events

If your journey includes one or more events, you can trigger them while Simulation is active.

- In Select event type , select the event to fire for this simulation.
- Click Configure events to open the editor and adjust the event as needed. To change the payload for a specific simulated user only, click beside that user.
- In the Trigger event view, specify which simulated users to include in the execution. Event configuration applies to a single event at a time. Modifying the selected event or the set of included users resets previously entered field values. Complete the current configuration before changing either selection.
- Click Done .
- Then, in Test events , either select Send all to send every simulated user listed under Test users into the journey, or select for a single user to execute the simulation for that user only.
- Access the Results tab to open the execution log and review how each step ran. For more information, see View Results .

## View results viewing-results

The **Results** tab allows you to view the test results. In the **Test user** drop-down, select the simulated user whose execution you want to inspect.

For each activity, the log can show whether the simulated user entered or exited the step, and errors that occurred during the simulation.

For **Wait** activities, the log includes two duration-related values:

- **Defined duration**: The duration specified on the **Wait** activity for the published journey and applied once the journey is live. The log records whether Simulation applies an override from the test settings, for example 10 seconds, rather than relying solely on the value defined on the journey.
- **Actual duration**: The elapsed time the simulated user remained on the **Wait** activity. This value is set from the **Test settings** tab.

When errors appear in the log, leave **Simulation**, apply the required changes to the journey, and run **Simulation** again. After validation succeeds, publish the journey. See [Publish your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey).

## Limitations limitations

In this release, **Simulation** may not support every activity, channel, or integration that **Test mode** or a live journey supports, and behavior may change as the capability matures. Use the procedures in this article for supported workflows.

Refer to the drop-downs below to learn more on Simulation limitations.

Node-level restrictions
If a journey contains any of the following nodes, it cannot be started in **Simulation**. The journey must be modified, or the relevant node removed, before simulation can run.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 |  |
| --- | --- |
| Restricted node | Notes |
| Business Events | Journeys that start with a business event cannot be run in **Simulation**. |
| Supplemental ID (multiple re-entrance) | Concurrent re-entrance (several active instances for the same simulated user) prevents **Simulation** from starting. |
| Content Decision node | This activity must be removed or changed before you can simulate the journey. |
| Dataset Lookup | Customer dataset lookups by key are not supported; journeys that include this activity cannot be run in **Simulation**. |
| Path Experimentation (Optimize — Experiment variant) | Not supported in **Simulation**. You can still use **Optimize** for flows that used to live under **Condition** (for example, data source conditions). |
| Path Targeting (Optimize, Targeting Rule variant) | Not supported in **Simulation**. |
| External audience attribute enrichment | Journeys that use personalized attributes from external audience sources will not start in **Simulation** when this validation is active. |

Functional limitations
The following capabilities are not supported in **Simulation**.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 |  |
| --- | --- |
| Capability | Notes |
| Exit criteria | Exit criteria are not applied when you run **Simulation**. |
| Adobe Journey Optimizer decisioning inside an action (for example, email content with Adobe Journey Optimizer decisioning) | Action proofs for content that uses Adobe Journey Optimizer decisioning are not generated. |
| Mock custom action response | Custom actions perform a real outbound call by default. Mocking the response so no external call runs is not supported. |
| Consent policy evaluation | Consent cannot be mocked at the simulated-user level. |
| Journey capping and arbitration | Not supported in **Simulation**. |
| Frequency capping (by channel or communication type) | Not supported in **Simulation**. |
| Opt-out management, suppression, and allow lists | Follows messaging routing configuration where it applies. |
| Dynamic subdomain and dynamic attributes in channel configurations | Follows messaging routing configuration where it applies. |
| Send Time Optimization (STO) | Not supported in **Simulation**. |
| Sandbox tooling (copy simulated users across sandboxes) | Not supported. |
| Wave sending in journeys | Not supported. |
| Quiet hours | Not supported. |
| Opt-out management, suppression, and allow lists | Not supported. |
| Dynamic subdomain and dynamic attributes in channel configurations | Not supported. |
| Privacy service | Simulated users are not GDPR-compliant persistent profiles. Do not include real customer data in simulated users. |

Quantitative guardrails
These guardrails apply to **Simulation**. Numeric caps are enforced in the journey interface and at runtime. Limits may change in a later release; if you run near a ceiling, verify behavior in your sandbox.

| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 |  |  |
| --- | --- | --- |
| Guardrail | Limit | Notes |
| Maximum simulated users that can be selected and triggered in one batch (batch journeys, event-triggered flows, and audience-qualification flows) | 20 | Counted for each **Send all** or **Trigger selected events**; not a cumulative cap for the whole journey. |
| Maximum unique simulated users tested in a single simulation run | 100 | Reaching **100** unique users in one run blocks **Select simulated users** for new simulated users. If you are at **90**, you can add at most **10** more before the same block. |
| Maximum journeys that can run in **Simulation** at the same time in one sandbox | 20 | Cap is shared by every **Simulation** journey in that sandbox at once. |
| Maximum active simulated users in one sandbox | 2,000 | Maximum simulated users that can exist in the sandbox at one time. Adobe may adjust this limit based on customer feedback. |
| Event Pre-fill (Browser Only) | — | You can pre-fill event payload fields only in the browser-based simulation UI. Pre-filled values stay in that browser and are not synced to other browsers, devices, or sessions, so you may see different pre-fill data in each place you test. |

recommendation-more-help
