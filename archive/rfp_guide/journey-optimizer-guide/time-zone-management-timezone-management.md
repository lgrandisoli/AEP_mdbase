---
title: "Time zone management timezone_management"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:09.280194+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Time zone management timezone_management

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Profiles](#)

CREATED FOR:

- Intermediate
- User

You can define a time zone in the [properties](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#timezone) of your journey.

To access journey properties, select the pencil icon in the top-right of the screen.

This time zone will be used for every activity of the journey containing a time element such as:

- [Time condition](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions#time_condition)
- [Date condition](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions#date_condition)
- [Custom wait](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity#custom)

You can select a [fixed time zone](#fixed-timezone) or choose to use the time zone [defined in the user profile](#timezone-from-profiles).

## Define a fixed time zone fixed-timezone

The time zone can be fixed. Clear the pre-defined time zone and pick one from the drop-down list. If you use a fixed time zone, it will be the same for all individuals entering the journey.

To do so, in the **Journey Properties** pane, select a time zone.

## Use profile time zone timezone-from-profiles

If the entry event of the journey has a namespace, meaning that the journey can reach the Real-time Customer Profile service of Adobe Experience Platform, you may want to use the time zone defined at the profile level. To do so, in **Properties**, check **Use Profile time zone in waits and conditions**. This option is not checked by default.

If a time zone has been defined for a profile, it is retrieved and used by the journey. If it hasn’t, the time zone used is the one defined in the time zone field.

NOTE
The profile time zone works with the
timeZone
field existing in the
Preference Details
field group.
## Use time zones in expressions timezone-in-expressions

The start and end dates of a journey cannot be linked to a specific time zone. They are automatically associated to the instance’s time zone.

recommendation-more-help
