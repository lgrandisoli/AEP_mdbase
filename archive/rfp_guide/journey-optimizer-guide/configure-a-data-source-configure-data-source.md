---
title: "Configure a data source configure-data-source"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/configure-data-sources"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:03.242376+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Configure a data source configure-data-source

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Data Sources](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

NOTE
The data source configuration is always performed by a
technical user
.
To configure a data source, follow the steps below:

- In the ADMINISTRATION menu section, select Configurations . In the Data Sources section, click Manage . The list of data sources is displayed. See this page for more information on the interface.
- Then you can either add field groups to the built-in data source (see this page ) or create a new external data source (see this page ) and associated field groups (see this page ).
- Click Save . The data source is now configured and ready to be used in your journeys.

## Define field groups define-field-groups

Field groups are sets of fields that you can retrieve from a data source and use in a journey.

For each data source, you can define several field groups.

For example, you can create a field group with the telephone number, the email, the first name and the address of the profile. You will then be able to use this data in your journey to create conditions. For example, you can decide to send a push notification only if the customer has installed the mobile application. If it is empty, you can send an email.

Even though a default name is automatically added, we recommend that you give a name to your field group. Indeed, the field group name will be visible to other users in Journey Optimizer. Giving a relevant name to field groups is a best practice.

When a data source field is used in a journey, the system will retrieve all the fields defined for that field group. Therefore, selecting only the fields that you need for your journeys is a best practice. This will reduce the request latency in your journeys thus increasing performance. Note that you can easily add more fields in field groups later.

The number of journeys that use a field group is displayed in the **Used in** field. You can click the **View journeys** button to display the list of journeys using this field group.

NOTE
Note that if a field group has no field, it is not displayed in the expression editor.
## Field group lifecycle field-group-lifecycle

You can add or remove fields from a field group that is not used in any draft or live journey.

If the field group is used in one or more draft or live journeys, you can incrementally add new fields from the selected schema, but cannot deselect/remove/modify fields that have already been selected. Updates to a field group are not permitted if exiting fields of schema already in use by draft or live journeys are modified — for example, changing the data type of an field. This will avoid breaking journeys

To delete a field from a field group used in one or more journeys, follow these steps. Let’s use an example of a field group named “Field Group A”.

- In the list of field groups, place the cursor on “Field Group A” and click on the **Duplicate** icon located on the right. Name the duplicated field group “Field Group B”, for example.
- In “Field Group B”, remove the fields you no longer want.
- In “Field Group A”, check where this field group is used. This information is displayed in the **Used in** field.
- Open all the journeys which use “Field Group A”.
- Create new versions of each of these journeys. Edit all activities using “Field Group A” and select “Field Group B”.
- Stop old versions of journeys that use “Field Group A”. You should then have no journey using “Field Group A”.
- Remove “Field Group A” as is it not used anymore.

recommendation-more-help
