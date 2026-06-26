---
title: "Manage the default execution fields change-primary-email"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/primary-email-addresses"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:25.479479+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Manage the default execution fields change-primary-email

Last update: May 8, 2026
- Topics:
- [Application Settings](#)

CREATED FOR:

- Intermediate
- Admin

When you target a profile, several email addresses or phone numbers may be available in the database (professional email address, personal phone number, etc.).

In that case, Journey Optimizer uses **Execution fields** to determine which email address or phone number to use from the profile service in priority.

To check the fields that are currently used by default, access the **Administration** > **Channels** > **General settings** > **Executions fields** menu.

{width="90%"}

NOTE
Execution fields are available for the Email, SMS and WhatsApp channels.
The current values are used for all deliveries at the sandbox level. You can update these fields if needed.

In most cases, you will change an execution field globally and define a value that should be used for all email, SMS or WhatsApp messages.

## Update the Administration settings admin-settings

To change the execution fields globally at the sandbox level, follow the steps below.

- Access the Channels > General settings > Executions fields menu.
- Click Edit to change the default values. {width="70%"}
- Click the current field of your choice or the edit icon to select a new field. {width="70%"}
- The list of available email-type XDM fields displays. Select the field to use. {width="90%"}
- Click Save to confirm your choice.

The execution field is updated and will now be used as the primary address.

## Override the default execution field in the journey parameters override-execution-address-journey

For specific use cases, you can override the execution field set globally and define a different value at the journey level.

Overriding this value may be useful for example to:

- Test your delivery. You can add your own email address or phone number: after you publish the journey, the email, SMS or WhatsApp message is sent to you.
- Send a message to the subscribers of a list. Learn more in [this use case](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/message-to-subscribers-uc).

When adding an **Email**, **SMS** or **WhatsApp** action to a [journey](/en/docs/journey-optimizer/using/channels/email/create-email#create-email), the primary email address or phone number is displayed under the journey advanced parameters.

Override this value using the **Enable parameter override** icon to the right of the field.

{width="85%"}

CAUTION
Email address or phone number override should only be used for specific use cases. Most of the time, you do not need to change it, because the value defined as the primary field in the
Execution fields
at the sandbox level is the one that should be used.
Learn more
## Override the default execution field in the channel configuration override-execution-address-channel-config

You can change the default execution address for a specific email, SMS or WhatsApp [channel configuration](/en/docs/journey-optimizer/using/configuration/channel-surfaces).

To do this, go to the **Execution dimension** section, and edit the dedicated field under **Execution Address**.

NOTE
For the
WhatsApp channel
, the
WhatsApp Execution Field
is under the
WhatsApp Settings
section.
{width="85%"}

Then select an item from the list of available email-type XDM fields.

The execution field is updated and is then used as the primary address for the campaigns or journeys using this channel configuration. It overrides the [general setting](#admin-settings) defined at the sandbox level.

recommendation-more-help
