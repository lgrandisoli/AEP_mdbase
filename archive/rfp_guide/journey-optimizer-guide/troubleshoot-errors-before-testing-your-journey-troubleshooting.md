---
title: "Troubleshoot errors before testing your journey troubleshooting"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:53.497887+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Troubleshoot errors before testing your journey troubleshooting

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Monitoring](#)

CREATED FOR:

- Intermediate
- User

In this section, learn how to troubleshoot journeys before testing or publishing. All the checks listed below can be performed when the journey is in test mode or when the journey is live. The recommendation is to make all the checks below in test mode and then proceed to publication. Learn more about the test mode on [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey).

Learn how to troubleshoot journey events, check if profiles entered your journey, how they navigate through it, and if messages are sent [on this page](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution). If no profiles enter your event-based journey despite events being ingested, ensure the [event condition data types match the event schema](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution#verify-event-identity-and-rule-data-types).

If you are using inbound actions, learn how to troubleshoot them [on this page](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-inbound).

## Errors in activities activity-errors

Before testing and publishing your journey, verify that all the activities are properly configured. You cannot perform tests or publications if errors are still detected by the system.

Errors appear with a warning symbol displayed on the activities themselves on the canvas. Place your cursor on the exclamation mark to display the error message. If you select the activity, you should see the line in error with a warning. For example:

- if a mandatory field is empty, an error will be displayed
- in the canvas, when two activities are disconnected, a warning is displayed

## Errors in the journey canvas-errors

Errors are also visible from the **Alerts** button, above the canvas. This button lets you see errors detected by the system and which prevent test mode activation or journey publication.

The system detects two kinds of issues: **errors** and **warnings**. Errors block publication and test activation. Warnings indicate potential issues that are not blocking test activation or publication. You will see a description of the issue and an issue log ID of the type ERR_XXX_XXX. This can help identify the issue.

Errors and warnings that are global to the journey appear first in the list. Error and warnings related to specific activities are listed after, by activity order or appearance in the journey from left to right. At the bottom of the list of alerts, the **Copy details** button lets you copy technical information about the journey which are useful to troubleshoot the issues. For the list of copied fields (including pause and resume information), see [Copy technical details](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#access-properties) in journey properties.

## Add an alternative path canvas-add-path

You can define a fallback action in case of an error for the following journey activities: **Optimize** and **Action**.

When an error occurs in an action or a condition, the journey of an individual stops. The only way to make it continue is to solve the issue. To avoid interrupting the journey, you can also check the option **Add an alternative path in case of a timeout or an error** in the activity’s properties. Learn more in [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/using-the-journey-designer#paths).

recommendation-more-help
