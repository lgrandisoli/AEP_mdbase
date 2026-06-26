---
title: "Work with the advanced expression editor about-the-advanced-expression-editor"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:59.286911+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with the advanced expression editor about-the-advanced-expression-editor

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)

CREATED FOR:

- Experienced
- Developer

Use the Journey advanced expression editor to build advanced expressions in various screens of the interface. For example, you can build expressions when configuring and using journeys, and when defining a data source condition.

It is also available every time you need to define action parameters that require specific data manipulations. You can leverage data coming from the events or additional information retrieved from the data source. In a journey, the displayed list of event fields is contextual and varies according to the event(s) added in the journey.

The advanced expression editor offers a set of built-in functions and operators to let you manipulate values and define an expression that fits specifically your needs. The advanced expression editor also allows you to define the values of the external data source parameter, manipulate map fields and collections.

NOTE
The functions and capabilities available in the Journey advanced expression editor differ from the ones available in the
personalization editor
.
## Access the advanced expression editor accessing-the-advanced-expression-editor

The advanced expression editor can be used to:

- create [advanced conditions](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions#data_source_condition) on data sources and event information
- define custom [wait activities](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity#custom)
- define action parameters mapping

When possible, you can switch between the two modes using the **Advanced mode** / **Simple mode** button. The simple mode is described [here](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/conditions#about_condition).

NOTE
- Conditions can be defined in the simple or advanced expression editor. They always return a boolean type.
- Actions parameters can be defined by selecting fields or via the advanced expression editor. They return a specific data type according to their expression.

You can access the advanced expression editor in different ways:

- When you create a data source condition, you can access the advanced editor by clicking on Advanced mode .
- When you create a custom timer, the advanced editor will be directly displayed.
- When you map action parameter, click on Advanced mode .

## Discover the interface discovering-the-interface

This screen allows you to manually write your expression.

On the left part of the screen are displayed available fields and functions:

- Events : choose one of the fields received from the inbound event. The displayed list of event fields is contextual and varies according to the event(s) added in the journey. Read more note caution CAUTION Creating expressions using experience events is not supported. Alternative approaches and best practices for creating expressions/logic with experience events are referenced here
- Audiences : if you have dropped an Audience qualification event, choose the audience you want to use in your expression. Read more
- Data Sources : choose from the list of fields available from your data sources’ field groups. Read more
- Journey properties : this section regroups the technical fields related to the journey for a given profile. Read more
- Functions : choose from the a list of built-in functions that allow to carry out complex filtering. Functions are organized by categories. Read more

An autocompletion mechanism displays contextual suggestions.

A syntax validation mechanism checks the integrity of your code. Errors are displayed on top of the editor.

TIP
When creating conditions in the advanced expression editor, ensure that your expressions do not contain hidden or non-printable characters. Additionally, use single-line expressions to avoid parsing errors.
**Need for parameters when building conditions with the advanced expression editor**

If you select a field from an external data source requiring a parameter to be called (see [this page](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/external-data-sources)), a new tab appears on the right to let you specify this parameter. The parameter value can come from the events positioned in the journey or the Experience Platform data source (and not from other external data sources). For example, in a weather-related data source, a frequently used parameter will be “city”. As a result, you must select where you want to get this city parameter. Functions can also be applied to parameters to perform format changes or concatenations.

For more complex use cases, if you want to include the parameters of the data source in the main expression, you can define their values using the “params” keyword. See [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/syntax/field-references).

recommendation-more-help
