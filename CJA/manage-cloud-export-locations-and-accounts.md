---
title: "Manage cloud export locations and accounts"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/exports/manage-export-locations"
category: "other"
topic: "analytics-platform/using/cja-components/exports"
created_at: "2026-06-02T19:08:21.328068+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Manage cloud export locations and accounts

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User
- Admin

You can view, edit, and delete cloud export locations and accounts.

For information about how to create a new location, see [Configure cloud export locations](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-locations).

## Filter and search locations

To find information you need, you can either filter on the list of locations or search for a location.

### Filter the list of locations

- In Customer Journey Analytics, select Components > Exports .
- Select the Locations tab.
- Select the Filter icon. You can filter by the following criteria: table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto Filter Description Location type The account type that the location is associated with. The following account types can be available: AEP Data Landing Zone Amazon S3 Role ARN Azure SAS Azure RBAC Google Cloud Platform Snowflake Account The name of account that the location is associated with. Created by The email address of the user who created the location.

### Search for locations

- In Customer Journey Analytics, select Components > Exports .
- Select the Locations tab.
- (Conditional) If you are a system administrator, you can enable the View locations for all users option to view locations created by all users in your organization.
- In the search field, begin typing any information associated with the location you’re searching for. You can search for data from any column available in the table.

## Edit locations

A location can be edited only by the user who created it or by a system administrator.

To edit a location:

- In Customer Journey Analytics, select Components > Exports .
- Select the Locations tab.
- (Conditional) If you are a system administrator, you can enable the View locations for all users option to view locations created by all users in your organization.
- Select the location you want to edit.
- Select Edit at the bottom of the screen.
- Make any desired changes, then select Save .

## Delete locations

If you delete a location, any exports that use the location are also deleted. Check the confirmation dialog when deleting to ensure that no exports are associated with the location.

To delete a location:

- In Customer Journey Analytics, select Components > Exports .
- Select the Locations tab.
- (Conditional) If you are a system administrator, you can enable the View locations for all users option to view locations created by all users in your organization.
- Select one or more locations that you want to delete.
- Select Delete at the bottom of the screen. The Delete Location dialog box displays.
- In the Delete Location dialog box, ensure that the location is not associated with any exports prior to confirming the delete.
- Select Delete again to confirm.

## Edit accounts

An account can be edited only by the user who created it or by a system administrator.

To edit an account:

- In Customer Journey Analytics, select Components > Exports .
- Select the Location accounts tab.
- (Conditional) If you are a system administrator, you can enable the View accounts for all users option to view accounts created by all users in your organization.
- Select Edit details on the account that you want to edit.
- Make any desired changes, then select Save .

## View account keys

After you create an account, you can view any associated account keys for that account. You might need to view this information if you didn’t finish configuring the account with your cloud provider [when you originally configured the account](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-accounts).

To view keys associated with an export account:

- In Customer Journey Analytics, select Components > Exports .
- Select the Location accounts tab.
- (Conditional) If you are a system administrator, you can enable the View accounts for all users option to view accounts created by all users in your organization.
- Select the 3-dot icon on the account that you want to edit, then select Show keys .

## Delete accounts

- In Customer Journey Analytics, select Components > Exports .
- Select the Location accounts tab.
- (Conditional) If you are a system administrator, you can enable the View accounts for all users option to view accounts created by all users in your organization.
- Select the 3-dot icon on the account that you want to delete, then select Delete account .
- Select Delete again on the confirmation dialog.

## Configure company-wide settings (administrators only)

System administrators can restrict users from creating accounts and locations, or they can limit the types of accounts users can create and use.

### Configure whether users can create and edit accounts

By default, all users in the organization can create accounts and edit accounts they create in your Customer Journey Analytics environment, as described in [configure cloud export accounts](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-accounts).

You can restrict users from creating accounts. When you do, users can still use any accounts they have already created, but they can no longer edit them. You can delete accounts that users have created, as described in [Delete an account](#delete-accounts).

To restrict all users from creating and editing accounts:

- In Customer Journey Analytics, select Components > Exports , then select the Admin settings tab.
- In the Location accounts section, deselect the option, Allow users to create and manage location accounts .
- Select Save .
- (Optional) Delete any accounts that users have created that you no longer want them to use, as described in Delete an account .

### Configure whether users can create and edit locations

By default, all users in the organization can create locations and edit locations they create in your Customer Journey Analytics environment, as described in [configure cloud export locations](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-locations).

You can restrict users from creating locations. When you do, users can still use any locations they have already created, but they can no longer edit them. You can delete locations that users have created, as described in [Delete locations](#delete-locations).

To restrict all users from creating and editing locations:

- In Customer Journey Analytics, select Components > Exports , then select the Admin settings tab.
- In the Locations section, deselect the option, Allow users to create and manage locations .
- Select Save .
- (Optional) Delete any locations that users have created that you no longer want them to use, as described in Delete a location .

### Limit which account types users can create and use

You can limit the account types users see in the following circumstances:

- When [creating new accounts](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-accounts).
- When choosing which accounts to use when exporting files using [full table export](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud).

When you limit account types as described in this section, any accounts of the type that you limit are no longer visible to users. This means that new accounts of that type cannot be created, and existing accounts of that type cannot be used when exporting files using full table export.

However, existing accounts that are configured for scheduled exports must be deleted if you want to restrict them from being used.

#### Ensure that accounts are not used for scheduled exports

When you limit account types, existing accounts are hidden, not deleted.

If schedules are already configured to send data to an account that is of the type that you limit, the schedules will continue to run even after you limit the account type, and data will continue to be sent to the account. For example, if a full table export is scheduled to send data to an account type that you limit, the schedule will continue to run.

If you need to ensure that accounts of a certain type are not used in scheduled exports, you can delete the accounts before you [limit the account types](#limit-the-account-types-that-are-available-to-users).

To delete accounts:

- Locate the accounts of the account type you plan to limit, which are being used for scheduled exports.
- Delete the accounts, as described in Delete an account .
- Continue with the following section, Limit the account types that are available to users .

#### Limit the account types that are available to users

To limit the account types that are available to users when creating and using accounts:

- In Customer Journey Analytics, select Components > Exports , then select the Admin settings tab.
- Locate the Permitted account types section. The following account types are available to users by default. Deselect any of these account types that you want to restrict users from using. AEP Data Landing Zone Amazon S3 Role ARN Google Cloud Platform Azure SAS Azure RBAC Snowflake
- Select Save .

recommendation-more-help
