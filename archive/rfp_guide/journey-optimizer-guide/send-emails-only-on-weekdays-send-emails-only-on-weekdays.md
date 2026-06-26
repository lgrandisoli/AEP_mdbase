---
title: "Send emails only on weekdays send-emails-only-on-weekdays"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/weekday-email-uc"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:07.001057+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Send emails only on weekdays send-emails-only-on-weekdays

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Use Cases](#)
- [Email](#)

CREATED FOR:

- Intermediate
- User

This use case demonstrates how to configure a journey in Adobe Journey Optimizer that sends emails only on weekdays (Monday through Friday). For profiles that enter the journey on weekends (Saturday or Sunday), emails are automatically queued and sent on Monday at a specified time. This ensures optimal engagement by delivering messages during the workweek.

## Use case overview

**The Challenge**: Ensuring that emails are only sent on weekdays, even though profiles may enter the journey on weekends. For weekend entries, emails should be queued and sent on Monday at a specific time.

**The Solution**: Use a condition activity to identify the day of the week. For weekend entries, Wait activities with custom formulas delay the email until Monday. Weekday entries proceed directly to the email send step.

This approach shows you how to use a condition activity to check if the current day is Saturday or Sunday, implement Wait activities with custom formulas for weekend entries, queue weekend emails for Monday delivery at a specific hour, and send emails immediately for weekday entries (Monday-Friday).

This approach is ideal for business-to-business (B2B) email campaigns, professional newsletters and communications, business-related announcements, work-related product updates, and any marketing campaign where weekend delivery is not desired.

NOTE
To implement this use case, you need an active Adobe Journey Optimizer instance with a configured
email channel surface
, an
audience
or
event
to trigger the journey, and a basic understanding of
journey conditions
and
expressions
.
## Implementation steps

Use these steps to build the weekday-only email flow.

### Step 1: Create your journey

- Navigate to Journey Management > Journeys in Adobe Journey Optimizer.
- Click Create Journey to create a new journey .
- Configure the journey properties .
- Choose your journey entry point: Read Audience : For batch campaigns targeting a specific audience Event : For real-time triggered journeys based on customer behavior

### Step 2: add a condition activity to check the day of the week

Right after the journey start, add a **Condition** activity to check if the current day is Saturday or Sunday. This will branch the workflow accordingly.

- Drag and drop an Optimize activity onto the canvas after your entry point.
- Click on the Condition activity to open its configuration panel.
- Select Time condition as the condition type.
- Select Day of the week as the time filtering option.
- For the first path (Saturday) , select Saturday only. Label this path as “Saturday”.
- Click Add a path to create a second condition.
- For the second path (Sunday) , select Day of the week and choose Sunday only. Label this path as “Sunday”.
- Check Show path for other cases than the one(s) above to create a path for weekday entries (Monday-Friday).

NOTE
The time zone used for day of week evaluation is defined at the journey level in the journey properties, not at the condition level. The journey
timezone
used in the formula is the journey’s configured timezone, not the recipient’s.
### Step 3: configure wait activities for weekend entries

For profiles entering on Saturday or Sunday, use **Wait** activities with custom formulas to delay the email until Monday at your desired hour.

In the **Wait** activity, use the following formula:

```
toDateTimeOnly(setHours(nowWithDelta(X, "days"), H))
```

Where:

- X is the number of days to wait: Use 2 for Saturday (wait until Monday) Use 1 for Sunday (wait until Monday)
- H is the hour you want to send (e.g., 9 for 9 AM)

**Example for Saturday:**

```
toDateTimeOnly(setHours(nowWithDelta(2, "days"), 9))
```

**Example for Sunday:**

```
toDateTimeOnly(setHours(nowWithDelta(1, "days"), 9))
```

To implement this in your journey:

- On the Saturday path , add a Wait activity after the condition.
- Select Duration as the wait type.
- Click Advanced mode to enter the custom formula.
- Enter: toDateTimeOnly(setHours(nowWithDelta(2, "days"), 9))
- Repeat the same steps for the Sunday path , using: toDateTimeOnly(setHours(nowWithDelta(1, "days"), 9))

TIP
For more complex business hours (e.g., only send between 9 AM and 5 PM on weekdays), you can further enhance the formula and conditions.
### Step 4: Weekday branch

For profiles entering Monday to Friday, proceed to the email send step as usual.

- On the Weekday path (the “other cases” path), proceed directly to add an Email action activity. No Wait activity is needed for weekday entries.
- Configure your email message as needed.

### Step 5: Complete the journey flow

After the **Wait** activities on both the Saturday and Sunday paths, all three paths (Saturday, Sunday, and weekdays) should flow to the same **Email** action activity. Add an **End** activity after the email.

### Visual workflow overview

The complete journey workflow follows this logic:

- Start → Condition : Is it Saturday or Sunday? Yes (Saturday): Wait until Monday 9 AM → Send email Yes (Sunday): Wait until Monday 9 AM → Send email No (Monday-Friday): Send email immediately

This ensures that all emails are sent on weekdays only, with weekend entries automatically queued for Monday delivery.

### Step 6: Test your journey

Before publishing, thoroughly test your journey logic in Adobe Journey Optimizer’s Test Mode to confirm everything works as expected:

- Click the Test button in the top right corner.
- Enable test mode .
- Create test profiles with simulated entry times on different days of the week: Saturday entry : Verify the profile follows the Saturday path, waits, and receives email on Monday at the specified hour Sunday entry : Verify the profile follows the Sunday path, waits, and receives email on Monday at the specified hour Monday-Friday entries : Verify emails are sent immediately without any wait
- Review the journey visualization to ensure profiles follow the correct conditional paths (Saturday, Sunday, or weekday).
- Check for any errors or warnings in the journey.
- Verify that the Wait formulas calculate the correct duration for your desired Monday delivery time.

IMPORTANT
Always test your journey logic in test mode to ensure the Wait activities behave as expected. Use Test Mode to simulate different entry scenarios and validate that weekend entries are correctly queued for Monday delivery. See
journey testing best practices
for more details.
### Step 7: Publish your journey

Once testing is complete:

- Click Publish in the top right corner.
- Confirm the publication .
- Monitor the journey performance using Journey reporting and live reports .

## Related topics

- [Optimize activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize) - Learn how to create different paths in your journey
- [Use conditions in a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions) - Detailed guide on journey conditions
- [Wait activity](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity) - Configure wait durations and formulas
- [Date functions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/main-functions-journey/date-functions) - Complete reference for date and time functions
- [Expression editor](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced) - Build complex expressions
- [Journey best practices](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs#best-practices) - Recommended approaches for journey design

recommendation-more-help
