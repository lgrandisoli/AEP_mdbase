---
title: "Set up channel configurations set-up-channel-surfaces"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/channel-surfaces"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:21.007402+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Set up channel configurations set-up-channel-surfaces

Last update: May 8, 2026
- Topics:
- [Channel Configuration](#)

CREATED FOR:

- Experienced
- Admin

With Journey Optimizer, you can set up channel configurations (i.e. message presets) that define all the technical parameters required for your messages: email type, sender email and name, reply and error routing, mobile apps, SMS configuration, and more.

CAUTION
- To create, edit and delete channel configurations, you must have the Manage messages presets permission.
- You must perform the Email configuration , Push configuration , SMS configuration , In-app configuration , Code-based configuration , Web configuration and Direct mail configuration steps before creating channel configurations.

Once channel configurations have been configured, you will be able to select them when creating messages from a journey or a campaign.

You can also use the guided channel setup to automate and validate channel setup in a unified experience, speeding up the process of getting started with Journey Optimizer. [Learn more](/en/docs/journey-optimizer/using/configuration/guided-setup/set-mobile-config)

## Create a channel configuration create-channel-surface

To create a channel configuration, follow these steps:

- Access the Channels > General settings > Channel configurations menu, then click Create channel configuration .
- Enter a name and a description (optional) for the configuration, then select the channel to configure. note NOTE Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore _ , dot . and hyphen - characters.
- To assign custom or core data usage labels to the configuration, you can select Manage access . Learn more about Object Level Access Control (OLAC) .
- Select your channel.
- Select Marketing action (s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. Learn more note NOTE Consent policies are currently only available for organizations that have purchased the Healthcare Shield and Privacy and Security Shield add-on offerings.
- Once all the parameters have been configured, click Submit to confirm. You can also save the channel configuration as draft and resume its configuration later on. note NOTE You cannot proceed with email configuration creation while the selected IP pool is under edition ( Processing status), and has never been associated with the selected subdomain. Learn more Save the configuration as draft and wait until the IP pool has the Success status to resume configuration creation.
- Once the channel configuration has been created, it displays in the list with the Processing status. During this step, several checks will be performed to verify that it has been configured properly. note NOTE When creating an email configuration for a subdomain, the processing time varies as detailed below: For new subdomains , the process for creating the first channel configuration can take 10 min to 10 days . For non production sandboxes , or if the selected subdomain is already used in another approved channel configuration, the process takes only up to 3 hours . These checks include configuration and technical tests that are performed by the Adobe team: SPF validation DKIM validation MX record validation Check IPs denylisting Helo host check IP pool verification A/PTR record, t/m/res subdomain verification FBL registration (this check will be performed only the first time an email configuration is created for a given subdomain) note NOTE If the checks are not successful, learn more on the possible failure reasons in this section .
- Once the checks are successful, the channel configuration gets the Active status. It is ready to be used to deliver messages.

## Monitor channel configurations monitor-channel-surfaces

All your channel configurations display in the **Channels** > **Channel configurations** menu. Filters are available to help you browse through the list (channel, user, status).

Once created, channel configurations can have the following statuses:

- **Draft**: The channel configuration has been saved as a draft and has not been submitted yet. Open it to resume the configuration.
- **Processing**: The channel configuration has been submitted and is going through several verifications steps.
- **Active**: The channel configuration has been verified and can be selected to create messages.
- **Failed**: One or several checks have failed during the channel configuration verification.
- **Deactivated**: The channel configuration is deactivated. It cannot be used to create new messages.

### Channel configuration failure reasons channel-config-failure

In case a channel configuration creation fails, the details on each possible failure reason are described below.

If one of these errors occurs, contact [Adobe Customer Care](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/support-for-experience-cloud.ug.html#_blank) to get assistance.

- SPF validation failed : SPF (Sender Policy Framework) is an email authentication protocol that allows to specify authorized IPs that can send emails from a given subdomain. SPF validation failure means that the IP addresses in the SPF record do not match the IP addresses used for sending emails to the mailbox providers.
- DKIM validation failed : DKIM (DomainKeys Identified Mail) allows the recipient server to verify that the received message was sent by the genuine sender of the associated domain and that the content of the original message was not altered on its way. DKIM validation failure means that the receiving mail servers are unable to verify the authenticity of the message content and its association with the sending domain.:
- MX record validation failed : MX (Mail eXchange) record validation failure means that the mail servers responsible for accepting inbound emails on behalf of a given subdomain are not correctly configured.
- Deliverability configurations failed : Deliverability configurations failure can happen due to any of the following reasons: Blocklisting of the allocated IPs Invalid helo name Emails being sent from IPs other than the ones specified in the IP pool of the corresponding configuration Unable to deliver emails to inboxes of major ISPs

## Edit a channel configuration edit-channel-surface

To edit a channel configuration, follow the steps below.

NOTE
You cannot edit the
Push notification settings
. If a channel configuration is only configured for the Push notification channel, it is not editable.
When editing an email configuration, you cannot add new
profile attributes
to header parameters. You must create a
new channel configuration
.
- From the list, click a channel configuration name to open it.
- Edit its properties as desired. note NOTE When the configuration has Active status, the Name , Select channel and Subdomain fields are read-only and cannot be modified. You can save your changes as a draft at any time and resume the update later. Edits limited to the Description , Email type and/or Email retry parameters fields take effect instantly, with no processing delay.
- Click Submit to confirm your changes.

Once the changes are submitted, the channel configuration will go through a validation cycle similar to the one in place when [creating a channel configuration](#create-channel-surface). The edition processing time can take up to **3 hours**.

### Update details update-details

For channel configurations that have the **Active** status, you can check the details of the update. To do so:

Click the **Recent update** icon that is displayed next to the active configuration name.

On the **Recent update** screen, you can see information such as the update status, and the list of requested changes.

### Update statuses update-statuses

A channel configuration update can have the following statuses:

- **Processing**: The channel configuration update has been submitted and is going through several verifications steps.
- **Success**: The updated channel configuration has been verified and can be selected to create messages.
- **Failed**: One or several checks have failed during the channel configuration update verification.

Each status is detailed below.

#### Processing surface-processing

Several deliverability checks will be performed to verify that the configuration has been updated properly.

NOTE
If you only edit the
Description
,
Email type
and/or
Email retry parameters
fields, the update is instantaneous.
The processing time can take up to **3 hours**. Learn more about the checks performed during the validation cycle in [this section](#create-channel-surface).

If you edit a configuration that was already active:

- Its status remains Active while the validation process is in progress.
- The Recent update icon displays next to the name of the configuration in the channel configurations list.
- During the validation process, the messages configured using this configuration are still using the older version of the configuration.

NOTE
You cannot modify a channel configuration while update is in progress. You can still click its name, but all the fields are greyed out. The changes will not be reflected until the update is successful.
#### Success success

Once the validation process is successful, the new version of the configuration is automatically used in all messages using this configuration. However, you may have to wait:

- a few minutes before it is consumed by the unitary messages,
- until the next batch for the configuration to be effective in batch messages.

#### Failed failed

If the validation process fails, the older version of the configuration will still be used.

Learn more about the possible failure reasons in [this section](#monitor-channel-surfaces).

Upon update failing, the configuration becomes editable again. You can click its name and update the settings that need to be fixed.

## Deactivate a channel configuration deactivate-a-surface

To make an **Active** channel configuration unavailable to create new messages, you can deactivate it.However, journeys' messages currently using this configuration will not be affected and will continue working.

You cannot deactivate a channel configuration in the following cases:

- If it is referenced by any live journey. Attempting to deactivate a configuration still in use by a live journey will result in an error. To deactivate a channel configuration, ensure that all live journeys using this configuration are closed or stopped. Learn how to end a journey
- While an update to the channel configuration is processing. You must wait until the update is successful or has failed. Learn more about editing channel configurations and about the update statuses .

To deactivate a channel configuration, follow the steps below.

- Access the channel configurations list.
- For the active configuration of your choice, click the More actions button.
- Select Deactivate .

NOTE
Deactivated channel configurations cannot be deleted to avoid any issue in journeys using these configurations to send messages.
You cannot directly edit a deactivated channel configuration. However, you can duplicate it and edit the copy to create a new version that you will use to create new messages. You can also activate it again, and wait until the update is successful to edit it.

## Add tags to a channel configuration channel-config-tags

- Access the channel configurations list.
- For the active configuration of your choice, click the More actions button.
- Click Edit Tags .
- Select Adobe Experience Platform tags from the list to categorize your channel configuration for improved search. Learn how to work with Unified Tags
- Once you assigned tags to your channel configurations, you can filter them on tags.

## How-to video video-presets

Learn what channel configurations are and how they are used in Adobe Journey Optimizer.

https://video.tv.adobe.com/v/3433124/?learn=on
recommendation-more-help
