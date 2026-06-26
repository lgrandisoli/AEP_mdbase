---
title: "Get started with the Optimize activity journey-path-optimization"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:04.232345+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with the Optimize activity journey-path-optimization

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Activities](#)

CREATED FOR:

- Intermediate
- User

IMPORTANT
The
Optimize
activity is the new vehicle for creating conditional paths in journeys. It replaces the former
Condition
activity, which has been removed from the UI. All conditional logic is retained and is now handled through the
Optimize
activity’s
conditions
.
If you have existing journeys that used
Condition
activities, you can continue to use them as before. They now appear with a new icon as
Optimize
activities using the
Condition
method, but the behavior is unchanged. Any custom label you had set on the node is preserved.
The **Optimize** activity lets you define how individuals progress through your journey by creating multiple **paths** based on specific criteria, including experimentation, targeting, and specific conditions - ensuring maximum engagement and success to create highly customized and effective journeys.

## What is a journey path? journey-path

A journey **path** can consist of any of the following: sequencing of communications, time in between them, number of communications, or any combination of these three variables.

For example, one path could contain one email, another could contain two SMS messages, and a third could contain an email, a Wait node of two hours, and then an SMS message.

## Three ways to optimize your journeys optimization-methods

Through the **Optimize** activity, you can perform the following actions on your journey paths:

- Run path experiments - Test different paths based on random splits to determine which performs best according to predefined success metrics (for example: conversion rate, revenue, engagement).
- Leverage targeting rules - Define specific rules that must be met for a customer to be eligible to enter one of the journey paths, based on audience segments, profile attributes, or contextual data. This ensures the right audience enters the specified path. note availability AVAILABILITY This capability is currently in Limited Availability. To request access, contact your Adobe representative.
- Apply conditions - Create conditional paths based on specific criteria such as data sources, time, date, percentage splits, or profile caps. This is the equivalent of the former Condition activity.

## How it works how-it-works

Once the journey is live, profiles are evaluated against the defined criteria, and based on matching criteria, they are sent down the appropriate path from the journey.

## Next steps next-steps

Select the optimization method that best fits your use case:

- Want to test and learn which path performs best? → Go to [Path experimentation](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/path-experimentation)
- Want to send different audiences down specific paths? → Go to [Path targeting](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/path-targeting)
- Want to create conditional logic (if/then scenarios)? → Go to [Conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions)

recommendation-more-help
