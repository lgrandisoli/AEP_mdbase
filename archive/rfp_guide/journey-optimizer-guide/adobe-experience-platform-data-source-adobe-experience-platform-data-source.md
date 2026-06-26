---
title: "Adobe Experience Platform data source adobe-experience-platform-data-source"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/adobe-experience-platform-data-source"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:01.999265+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Adobe Experience Platform data source adobe-experience-platform-data-source

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Data Sources](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

Adobe Experience Platform data source defines the connection to Adobe Real-time Customer Profile. This data source is built-in and pre-configured, and cannot be deleted. This data source is designed to retrieve and use data from the Real-time Customer Profile Service (for example, check if the person who entered a journey is a female). For more information about Adobe Real-time Customer Profile, refer to [Adobe Experience Platform documentation](/en/docs/experience-platform/profile/home#_blank).

To allow the connection to the Real-time Customer Profile Service, we must use a key to identify a person, and a namespace that contextualizes the key. As a result, you can only use this data source if your journeys start with an event containing a key and a namespace. [Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/journey).

You can edit the pre-configured field group named “ProfileFieldGroup”, add new ones and remove the ones that are not used in any draft or live journeys. [Learn more](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/configure-data-sources#define-field-groups).

CAUTION
Using experience events in journey expressions/conditions is not supported. If your use case requires the use of experience events, consider alternative methods.
Learn more
Main steps to add field groups to the built-in data source are detailed below:

- From the list of data sources, select the built-in Adobe Experience Platform data source. This opens the data source configuration pane on the right-hand side of the screen.
- Select Add a New Field Group to define a new series of fields to retrieve .
- Select a schema from the Schema drop-down. Schema creation is performed in Adobe Experience Platform, not performed in Adobe Journey Optimizer. note NOTE Only XDM Individual Profile-based schemas are supported in the Journey Optimizer Data Source configuration. For more information, see XDM Individual Profile class .
- Select the fields to use, and save your changes.

TIP
Hover over the name of a field group to reveal two icons on the right. Use these to
Duplicate
or
Delete
the field group. Note that the
Delete
icon is only available if the field group is not used in any
Live
,
Draft
or
Finished
journey. Refer to the
Used in
field to check if this is the case.
recommendation-more-help
