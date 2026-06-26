---
title: "Wait activity wait-activity"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:57.759355+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Wait activity wait-activity

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

You can use a **Wait** activity to define a duration before executing the next activity. The maximum wait duration is **90 days**.

You can set two types of **Wait** activity:

- A wait based on a relative duration. [Learn more](#duration)
- A custom date, using functions to calculate it. [Learn more](#custom)

## Recommendations wait-recommendations

Use these recommendations to keep waits predictable and safe.

### Multiple Wait activities multiple-wait-activities

When using multiple **Wait** activities in a journey, be aware that the [global timeout](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#global_timeout) for journeys is 91 days, meaning that profiles are always drop out of the journey maximum 91 days after they entered it. Learn more on [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#global_timeout).

An individual can enter a **Wait** activity only if they have enough time left in the journey to complete the wait duration before the 91 days journey timeout.

### Wait and reentrance wait-reentrance

A best practice to not use **Wait** activities to block reentrance. Instead, use the **Allow reentrance** option at the journey properties level. Learn more on [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#entrance).

### Wait and test mode wait-test-mode

In test mode, the **Wait time in test** parameter allows you to define the time that each **Wait** activity will last. The default time is 10 seconds. This will ensure that you get the test results quickly. Learn more on [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey).

### Wait and mobile channels wait-mobile-channels

If you want to show an [in-app message](/en/docs/journey-optimizer/using/channels/in-app/create-in-app) shortly after sending a [push notification](/en/docs/journey-optimizer/using/channels/push/push-landing-page), use a **Wait** activity to allow the in-app message payload time to propagate. Typically a 5–15 minute wait is recommended, but exact times can vary depending on payload complexity and personalization needs.

## Configuration wait-configuration

Configure wait duration and timing here.

### Duration wait duration

Select the **Duration** type to set the relative duration of the wait before the execution of the next activity. The maximum duration is **90 days**.

### Custom wait custom

Select the **Custom** type to define a custom date, using an advanced expression based on a field coming from an event or a custom action response. You cannot define a relative duration directly, for example, 7 days, but you can use functions to calculate it if needed (eg: 2 days after purchase).

The expression in the editor should provide a dateTimeOnly format. Refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced). For more information on dateTimeOnly format, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/data-types).

Best practice is to use custom dates that are specific to your profiles, and avoid using the same date for all. For example, do not define toDateTimeOnly('2024-01-01T01:11:00Z') but rather toDateTimeOnly(@event{Event.productDeliveryDate}) which is specific to each profile. Be aware that using fixed dates can cause issues on your journey execution. Learn more about the impact of Wait activities on journey processing rate in [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/entry-management#wait-activities-impact).

CAUTION
When working with
dateTimeOnly
expressions, keep the following in mind:
- You can use a dateTimeOnly expression directly, or convert to it using a function — for example: toDateTimeOnly(@event{Event.offerOpened.activity.endTime}) where the field value is in the form 2023-08-12T09:46:06Z.
- The **time zone** is defined in the journey properties. As a result, it is not possible from the UI to point at a full ISO-8601 timestamp that mixes time and time zone offset, such as 2023-08-12T09:46:06.982-05. [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/timezone-management)
- When building a custom wait expression with toDateTimeOnly(), do **not** append Z or a time zone offset (e.g., -05:00). The expression must reference the journey’s configured time zone without explicit time zone designators — otherwise profiles may get stuck in the wait activity.

| table 0-row-2 1-row-2 2-row-2 |  |
| --- | --- |
|  | Example |
| **Correct** | toDateTimeOnly(concat(toString(toDateOnly(nowWithDelta(2, "days"))),"T10:00:00")) |
| **Incorrect** | toDateTimeOnly(concat(toString(toDateOnly(nowWithDelta(2, "days"))),"T10:00:00Z")) ❌ (contains Z) |

To validate that the wait activity works as expected, you can use step events. [Learn more](/en/docs/journey-optimizer/using/reporting/reports/query-examples#common-queries).

## Profile refresh after wait profile-refresh

When a profile is parked at a **Wait** activity in a journey starting with a **Read Audience** activity, the journey automatically refreshes the profile’s attributes from the Unified Profile Service (UPS) to fetch the latest available data.

- **At journey entry**: Profiles use attribute values from the audience snapshot that was evaluated when the journey started.
- **After a wait node**: The journey performs a lookup to retrieve the latest profile data from UPS, not the older snapshot data. This means profile attributes may have changed since the journey began.

This behavior ensures that downstream activities use current profile information after a wait period. However, it may produce unexpected results if you expect the journey to use only the original snapshot data throughout execution.

Example: If a profile qualifies for a “silver customer” audience at journey start, but upgrades to “gold customer” during a 3-day wait, activities after the wait will see the updated “gold customer” status.

## Automatic wait node auto-wait-node

Each inbound experience activity (In-app message, Code-based experience, or Card) comes with a 3-days **Wait** activity. As inbound messages automatically end when a profile reach out the end of the journey, we assume that you want your users to see it at least for 3 days. You can remove this **Wait** activity, or change its configuration if needed.

recommendation-more-help
