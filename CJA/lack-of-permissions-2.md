---
title: "Lack of permissions"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/troubleshooting/lack-of-permissions"
category: "other"
topic: "analytics-platform/using/troubleshooting/lack-of-permissions"
created_at: "2026-06-23T20:42:47.575391+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Lack of permissions

Last update: June 5, 2026
- Topics:
- [Data governance](#)
- [Administration](#)

CREATED FOR:

- Admin

Customer Journey Analytics does not function properly when certain Adobe Experience Platform permissions are not in place.

As an example, after creating a [Connection](/en/docs/analytics-platform/using/cja-connections/overview) and [Data view](/en/docs/analytics-platform/using/cja-dataviews/data-views), you might be presented with the following error message in the [Components](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#components) section:

*Something went wrong retrieving DULE policies. Please verify account permissions, policies, or labels. Message: Forbidden.*

style
shade-box
- Ensure you have the right access control: You must have system or product administrator privileges for an organization that has an Experience Platform product. See Access control overview for more information. You must be a user in the AEP-Default-All-Users product profile. Ask your administrator if you don’t have the permissions to add yourself to this profile. See Access control hierarchy and workflow for more information.
- Navigate to the Adobe Experience Platfom UI.
- Select Permissions from the left rail.
- Select Roles .
- Navigate into the relevant role.
- Select Edit to edit the role.
- Ensure Manage Data Usage Policies and View Data Usage Policies are added to the Data Governance container.
- Select Save to save the changes.

recommendation-more-help
