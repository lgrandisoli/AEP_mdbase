---
title: "Metric deduplication component settings metric-deduplication-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/metric-deduplication"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-23T20:42:43.619594+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Metric deduplication component settings metric-deduplication-component-settings

Last update: June 5, 2026
- Topics:
- [Data management](#)

CREATED FOR:

- Admin

Metric deduplication lets you configure a metric to only count values non-repetitively.

Setting
Description
Metric deduplication
A checkbox that allows you to enable metric deduplication. Disabled by default.
Deduplication scope
Lets you determine how far back the unique check goes.
Global account
: Only the first metric occurrence in the reporting window is counted.
Account
: Only the first metric occurrence in the reporting window is counted.
Opportunity
: Only the first metric occurrence in the reporting window is counted.
Buying group
: Only the first metric occurrence in the reporting window is counted.
Person
: Only the first metric occurrence in the reporting window is counted.
Session
: Only the first metric occurrence of the session is counted.
Deduplication ID
Instead of applying deduplication on the metric itself, allows you to apply metric deduplication based on a dimension instead. Valuable for dimensions like Purchase ID to apply deduplication.
Value to keep
- **Keep first instance**: Use this in situations where the initial instance of the metric is the valid one. The most common one would probably be a purchase confirmation. Even if someone inadvertently reloads the page and we get another instance of a purchase confirmation, the initial event is the valid one.
- **Keep last instance**: Use this in situations where the last instance makes more sense to collect. Example: Someone makes an update to their online profile. We only want to count one of these updates per session. However, they may update their profile multiple times during the session. If we keep the first instance, there could be activities which would not tie to the event. In this case, it makes more sense to keep the last instance.

CAUTION
Deduplication at a
person
scope is evaluated by complete months in UTC time. A partial-month reporting window may not display all first or last instances, if some occurred within the full month but outside of the reporting dates.
recommendation-more-help
