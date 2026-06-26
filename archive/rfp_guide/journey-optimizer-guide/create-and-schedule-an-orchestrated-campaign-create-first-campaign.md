---
title: "Create and schedule an Orchestrated campaign create-first-campaign"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/create-orchestrated-campaign"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:24.627924+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create and schedule an Orchestrated campaign create-first-campaign

Last update: May 8, 2026
- Applies to:
- Campaign Orchestration

Create an Orchestrated campaign in Adobe Journey Optimizer and configure its execution schedule to control when it starts and how often it runs. Choose to launch the campaign immediately, at a specific date and time, or on a recurring basis using flexible scheduling options such as daily, weekly, or monthly frequencies.

## Create the campaign create

To create an Orchestrated campaign, follow these steps:

- Browse to the Campaigns menu and select the Orchestration tab.
- Click the Create campaign button and select the Orchestration - Marketing and transactional campaign type. You will choose whether each message is marketing or transactional when you add a channel activity .
- Define the campaign properties. Enter a Name and Description for the campaign. Select a Merge policy for your campaign. In Adobe Experience Platform, each audience is tied to a specific merge policy, which defines how profile information are combined to form a merged profile. When you select a merge policy in the Read audience activity, only audiences based on that same merge policy are available. By default, the system uses the default merge policy, but you can change it if needed. For more information on merge policies, refer to the Adobe Experience Platform documentation . Use the Tags field to assign Adobe Experience Platform Unified Tags to your campaign. This allows you to easily classify them and improve search from the Orchestrated campaigns list. Learn how to work with tags . Click Save . You can access the campaign properties at any time using the button next to the campaign’s name.

## Schedule the campaign schedule

By default, Orchestrated campaigns start when activated manually and end once their associated activites have been executed. If you prefer to delay execution or run the campaign on a recurring basis, you can define a schedule for the campaign.

Consider the following best practices when scheduling Orchestrated campaigns to ensure optimal performance and expected behavior:

- Do not schedule an Orchestrated campaign to run more than every 15 minutes as it may impede overall system performance and create blocks in the database.
- If you want to send a one-shot message in your Orchestrated campaign, you can set it to run **Once**.
- If you want to send a recurring message in your Orchestrated campaign, you need to use a **Scheduling** options and set the execution frequency. The recurring delivery activity does not allow you to define a schedule.

NOTE
You can also start the campaign when it receives a signal from an external system or application instead of running on a schedule.
Learn how to trigger an Orchestrated campaign using a signal
.
To configure the campaign schedule, follow these steps:

- Open the campaign and click the As soon as possible button.
- Select an execution frequency for the campaign, then configure the available options. The settings vary depending on the selected frequency: accordion Once Run the campaign a single time at a specified date and time. Date : Select the date the campaign should be executed. Time : Select the specific time the campaign should be executed. accordion Daily Run the campaign every day or on selected days. Daily recurrence : Choose how often the campaign should run: Every day : Executes the campaign every day of the week, including weekends. On weekdays : Executes the campaign only from Monday to Friday. Through a specific period : Executes the campaign daily within a defined date range (e.g., from July 1 to July 15). The campaign will not run outside this range. On selected days of the week : Executes the campaign only on the specified days of the week (e.g., Monday, Wednesday, Friday). Start time : Define the time the campaign should execute each day. accordion Several times a day Run the campaign multiple times within the same day. You can choose specific times or set a periodic frequency. Selected hours : Select the specific times the campaign should run and configure its daily recurrence (execute every day of the week or on certains days). Periodic : Choose to run the campaign every n minutes or hours. You can also define the time range within the day when executions are allowed. accordion Weekly Run the campaign on a weekly basis, with options for specific days. Frequency : Choose how often the campaign should run (e.g., every week, every 2 weeks). Starting from date : Select the date the recurrence should begin. Daily recurrence : Choose specific days of the week for execution (e.g., every Monday and Thursday). Start time : Set the time the campaign should execute on selected days. accordion Monthly Run the campaign on a monthly basis, with options for specific days. Monthly recurrence : Select whether the campaign runs every month or only during specific months. Daily recurrence : Every day : Executes the campaign on every calendar day of the month, including weekends. Last day of the month : Executes the campaign only on the final calendar day of each month (e.g., Jan 31, Feb 28/29). Specific day of the month (e.g., 15th) : Executes the campaign on a specified day (e.g., the 15th of each month). First/last, or nth day of the week (e.g., first Monday): Executes the campaign on a specified weekday (e.g., the 15th of each week). Selected days of the week : Executes the campaign on a specified day. Start time : Set the time the campaign should execute.
- Use the Validity period setting to define a specific start and end date, restricting the campaign’s execution to a limited time window.
- For recurring schedules, click the Preview launch times button to preview the exact upcoming execution dates and times based on the current configuration. This helps validate the schedule before activation and ensures the campaign will run as expected.

NOTE
When scheduling campaigns in Adobe Journey Optimizer, ensure your start date/time aligns with the desired first delivery. For recurring campaigns, if the initial scheduled time has already passed, the campaigns will roll over to the next available time slot according to their recurrence rules.
In the following example, the activity is configured so that the Orchestrated campaign runs twice a day at 9 and 12 AM, every day of the week from October 1st, 2025 to January 1st, 2026.

{align="left" width="50%"}

## Next steps next

Once your campaign settings and schedule are configured, you are ready to start orchestrating the differents tasks it will perform. [Learn how to orchestrate campaign activities](/en/docs/journey-optimizer/using/campaigns/orchestrated-campaigns/launch/orchestrate-activities)

recommendation-more-help
