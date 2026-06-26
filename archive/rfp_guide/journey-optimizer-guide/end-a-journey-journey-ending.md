---
title: "End a journey journey-ending"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/end-journey"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:52.423241+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# End a journey journey-ending

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)

CREATED FOR:

- Intermediate
- User

TIP
Looking for practical guidance on when and how profiles should exit journeys? See our
comprehensive guide to journey entry and exit criteria
, which includes real-world exit scenarios, best practices, and configuration guidance.
## How a live journey ends

Journeys are closed when the global journey timeout is reached, or after the last occurrence of a recurring audience-based journey. [Learn how journeys are closed](#close-journey).

If you need to terminate a live journey, we recommend that [you close it](#close-to-new-entrances) manually. The arrival of new customers in the journey is then blocked. Profiles who already entered in the journey are able to experience it to the end.

You can also [stop a journey](#stop-journey), only in case of an emergency and if all journey processing must to be ended immediately. People who already entered a journey are all stopped in their progress.

IMPORTANT
- You cannot restart or delete a closed or stopped journey. You can create a new version of it or duplicate it .
- Only finished journeys can be deleted.

## How profiles end a journey

A journey ends for an individual in two specific contexts:

- The individual reaches at the last activity of a path, then moves to the [End tag](#end-tag).
- The individual reaches at a **Condition** activity (or a **Wait** activity with a condition) and does not match any of the conditions.

The individual can then reenter the journey if reentrance is allowed. [Learn more about entrance/reentrance management](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#entrance)

## Journey End tag end-tag

While authoring a journey, an End tag is displayed at the end of each path. This node cannot be added by a user, cannot be removed and only its label can be changed. It marks the end of each path of the journey.

If the journey has several paths, we recommend that you add a label to each end to make reports easier to read. Learn more about [journey reports](/en/docs/journey-optimizer/using/reporting/live-report/live-report).

## Close a journey close-journey

A journey can close because of the following reasons:

- A one-shot segment based journey that has finished executing, and reached the global timeout of 91 days.
- After the last occurrence of a recurring audience-based journey.
- The journey is closed manually via the **Close to new entrances** button.

After the **91-day journey global timeout**, a Read audience journey switches to the **Finished** status. This behavior is set for 91 days only as all information about profiles who entered the journey is removed 91 days after they entered. Persons still in the journey automatically are impacted. They exit the journey after the 91-day timeout. Learn more about [the journey global timeout](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#global_timeout).

TIP
A one-shot segment-based journey keeps the
Live
status even after running once. Profiles cannot re-enter once completed, but the journey remains in
Live
status until the default global timeout expires. You can manually close it sooner using the
Close to new entrances
option.
### When is a journey considered “finished”? journey-finished-definition

The definition of “finished” varies depending on the journey type:

Journey Type
Recurring?
Has end date?
Definition of “finished”
Read audience
No
n/a
91 days after execution start
Read audience
Yes
No
91 days after execution start
Read audience
Yes
Yes
When end date is reached
Event-triggered journey
n/a
Yes
When end date is reached
Event-triggered journey
n/a
No
When closed in UI or via API
### Close to new entrances close-to-new-entrances

Closing a journey manually ensures that customers who already entered the journey can finish their path but new users are not able to enter the journey. When a journey is closed (for any of the reasons above), it will have the status **Closed**. The journey stops letting new individuals enter the journey. Profiles already in the journey can finish the journey normally. After the default global timeout of 91 days, the journey will switch to the **Finished** status.

To close a journey from the list of journeys, click the **Ellipsis** button that is located to the right of the journey name and select **Close to new entrances**.

You can also:

- In the Journeys list, click the journey you want to close.
- On the top-right, click the down arrow. {align="left" width="50%" modal="regular"}
- Click Close to new entrances , and confirm in the dialog box.

## Stop a journey stop-journey

In case you need to stop the progress of all individuals in the journey, you can stop it. Stopping the journey timeout all individuals in the journey. However, stopping a journey involves that people who already entered a journey are all stopped in their progress. The journey is basically switched off. If you want to end to a journey, best practice is [to close it](#close-journey).

You can stop a journey, for example, if a marketer realizes that the journey targets the wrong audience or a custom action supposed to deliver messages is not working correctly. To stop a journey from the list of journeys, click the **Ellipsis** button that is located to the right of the journey name and select **Stop**.

You can also:

- In the Journeys list, click the journey you want to stop.
- On the top-right, click the down arrow. {align="left" width="50%" modal="regular"}
- Click Stop , and confirm in the dialog box.

When stopped, the journey status is set to **Stopped**.

CAUTION
Stopping a journey requires the
Manage journeys
permission. If the journey includes inline campaigns or messaging nodes, users also need
Campaigns > Publish Campaigns
permissions. If the journey uses assets (for example, in emails), users must have access to those asset folders. Learn more about managing Journey Optimizer users’ access rights in
this section
.
## Related topics

- [Journey entry and exit criteria guide](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/entry-exit-criteria-guide) - Complete guide with real-world examples and best practices
- [Profile entrance management](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management) - Configure how profiles enter journeys
- [Configure exit criteria](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#exit-criteria) - Set up automatic profile removal from journeys
- [Pause a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-pause) - Temporarily halt journey execution

recommendation-more-help
