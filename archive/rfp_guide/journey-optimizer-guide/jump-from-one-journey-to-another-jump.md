---
title: "Jump from one journey to another jump"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/jump"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:45.547928+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Jump from one journey to another jump

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

The **Jump** action activity allows you to push individuals from one journey to another. This feature allows you to:

- simplify the design of very complex journeys by splitting them into several ones
- build journeys based on common and reusable journey patterns

In the origin journey, add a **Jump** activity and select a target journey. When the individual enters the **Jump** step, an internal event is sent to the first event of the target journey. If the **Jump** action succeeds, the individual continues to progress in the journey. The behavior is similar to other actions.

In the target journey, the first event triggered internally by the **Jump** activity makes the individual flow in the journey.

## Lifecycle jump-lifecycle

Assume you have added a **Jump** activity in journey A to journey B. Journey A is the **origin journey**, and journey B is the **target journey**.

Here are the different steps of the execution process:

**Journey A** is triggered from an external event:

- Journey A receives an external event related to an individual.
- The individual reaches the **Jump** step.
- The individual is pushed to journey B and moves on to the next steps in journey A, after the **Jump** step.

In journey B, the first event is triggered internally via the **Jump** activity from journey A:

- Journey B receives an internal event from journey A.
- The individual starts flowing in journey B.

NOTE
Journey B can also be triggered via an external event.
### Profile behavior during a Jump jump-profile-behavior

When a profile reaches the **Jump** step, it continues progressing in the origin journey (Journey A) while simultaneously entering the target journey (Journey B). The profile is therefore active in both journeys at the same time.

This means:

- The profile completes any remaining steps in Journey A after the Jump activity (for example, a follow-up wait or closing action).
- The profile also starts flowing through Journey B from its first event, independently of Journey A.
- If the profile is **already active** in Journey B when the Jump is executed, it will **not** enter Journey B again. Journey A continues normally; no error is reported.

NOTE
The case above — profile already active in Journey B — results in a
silent skip
: no error is raised and Journey A continues normally. In other situations, the Jump can
fail
and Journey A applies its standard action-error handling. See
Runtime failures
for the full list of cases.
## Best practices and limitations jump-limitations

Use these guidelines to keep Jump activity behavior predictable and safe.

### Authoring jump-limitations-authoring

- The **Jump** activity is only available in journeys that use a namespace.
- You can only jump to a journey that uses the same namespace as the origin journey.
- You cannot jump to a journey that starts with an **Audience Qualification** event or **Read Audience**.
- You cannot have a **Jump** activity and an **Audience Qualification** event or **Read Audience** in the same journey.
- You can include as many **Jump** activities as needed in a journey. After a **Jump**, you can add any activity needed.
- You can have as many jump levels as needed. For example, journey A jumps to journey B, which jumps to journey C, and so on.
- The target journey can also include as many **Jump** activities as needed.
- Loop patterns are not supported. There is no way to link two or more journeys together, which would create an infinite loop. The **Jump** activity configuration screen prevents you from doing this.

### Execution jump-limitations-exec

- When the **Jump** activity is executed, the latest version of the target journey is triggered.
- A unique individual can only be present once in the same journey. As a result, if the individual pushed from the origin journey is already in the target journey, the individual will not enter the target journey. No error will be reported on the **Jump** activity because this is normal behavior.

## Design strategy: bite-sized sub-journeys jump-strategy

Complex customer journeys can quickly become difficult to build and maintain, especially as additional channels or touchpoints are introduced. Even a journey with a handful of milestones can expose 20 or more unique paths a customer can take, and that complexity grows exponentially with each addition.

A practical approach to managing this is to break large journeys into smaller, focused sub-journeys — one per business phase or milestone — and connect them using the **Jump** activity. This keeps each journey readable, testable, and independently maintainable.

**Step 1 — Visualize the end-to-end journey**

Map the full customer journey and identify its high-level phases. For example, a loyalty onboarding journey might include three distinct phases: download the mobile app, make a first transaction, make a second transaction.

**Step 2 — Annotate phases and define sub-journeys**

Mark the boundary of each phase and define its business objective. Each phase becomes a candidate sub-journey with a clear entry condition and goal.

**Step 3 — Build and connect sub-journeys**

Build each phase as a separate journey in Journey Optimizer, then use **Jump** activities to pass profiles from one sub-journey to the next. The result is a set of simpler, reusable journeys that combine to produce the full end-to-end experience — with less risk of introducing errors.

TIP
For a worked example using a multi-phase loyalty program, see
Multi-phase loyalty journey
.
## Configuring the Jump activity jump-configure

- Design your origin journey .
- At any step of the journey, add a Jump activity, from the ACTIONS category. Add a label and description.
- Click inside the Target journey field. The list displays all journey versions that are draft, live or in test mode. Journeys that use a different namespace or that start with an Audience Qualification event are not available. Target journeys that would create a loop pattern are also filtered out. note NOTE You can click the Open target journey icon, on the right side, to open the target journey in a new tab.
- Select the target journey that you want to jump to. The First event field is prefilled with the name of the target journey’s first event. If your target journey includes multiple events, the Jump is only allowed on the first event.
- The Action parameters section displays all the fields of the target event. Map each field with fields from the origin event or data source, as with other types of actions. This information will be passed to the target journey at runtime.
- Add the next activities to finish your origin journey. note NOTE The individual’s identity is automatically mapped. This information is not visible in the interface.

Your **Jump** activity is configured. As soon as your journey is live or in test mode, individuals reaching the **Jump** step will be pushed to the target journey.

When a **Jump** activity is configured in a journey, a **Jump** entry icon is automatically added at the beginning of the target journey. This helps you identify that the journey can be triggered externally but also internally from a **Jump** activity.

## Troubleshooting jump-troubleshoot

### Configuration errors

The following issues prevent the Jump from working correctly and appear as errors on the journey canvas:

- The target journey no longer exists.
- The target journey is draft, closed, or stopped.
- The first event of the target journey has changed and the mapping is broken.

### Runtime failures

In the following cases, the Jump step is treated as a **failed action** in Journey A. Journey A applies the standard action-error handling and continues:

- The existing target journey instance has been terminated and the target journey is non-reentrant.
- A reentrance period is configured on the target journey. Even when re-entry is allowed in principle, the profile cannot re-enter until the period elapses (the Jump fails with a “non-reentrant for the period” status).
- The target journey version cannot be located, has been deleted, is in a finished state, or has been stopped.

recommendation-more-help
