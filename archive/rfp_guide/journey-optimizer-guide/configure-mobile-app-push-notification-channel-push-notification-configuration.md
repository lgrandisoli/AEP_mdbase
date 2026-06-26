---
title: "Configure mobile app push notification channel push-notification-configuration"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:42.777831+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Configure mobile app push notification channel push-notification-configuration

Last update: May 8, 2026
- Topics:
- [Push](#)
- [Channel Configuration](#)

CREATED FOR:

- Intermediate
- Admin

Journey Optimizer allows you to create your journeys and send messages to targeted audience. Before beginning to send push notifications with Journey Optimizer, you need to ensure configurations and integrations are in place on the mobile app and for tags in Adobe Experience Platform. To understand the Push Notifications data flow in Adobe Journey Optimizer please refer to [this page](/en/docs/journey-optimizer/using/channels/push/push-config/push-gs).

AVAILABILITY
The new
Mobile onboarding quick start workflow
is now available. Use this new product feature to rapidly configure the Mobile SDK to start collecting and validating mobile event data, and to send mobile push notifications. This capability is accessible via the Data Collection home page as a public beta.
Learn more
## Before starting start-push

### Set up permissions setup-permissions

Before creating a mobile application, you first need to make sure that you have or assign the correct user permissions for tags in Adobe Experience Platform. Learn more in [Tags documentation](/en/docs/experience-platform/tags/admin/user-permissions#_blank).

CAUTION
Push configuration must be performed by an expert user. Depending on your implementation model and personas involved in this implementation, you might need to assign the full set of permissions to a single product profile or share permissions between the app developer and the
Adobe Journey Optimizer
administrator. Learn more about
Tags
permissions in
this documentation
.
To assign **Property** and **Company** rights, follow the steps below:

- Access the Admin Console .
- From the Products tab, select the Adobe Experience Platform Data Collection card.
- Select an existing Product Profile or create a new one with the New profile button. Learn how to create a new New profile in the Admin console documentation .
- From the Permissions tab, select Property rights .
- Click Add all . This will add the following right to your product profile: Approve Develop Manage Environments Manage Extensions Publish These permissions are required to install and publish the Adobe Journey Optimizer extension and publish the app property in Adobe Experience Platform Mobile SDK.
- Then, select Company rights in the left-hand menu.
- Add the following rights: Manage App Configurations Manage Properties These permissions are required for the mobile app developer to set up push credentials in Adobe Experience Platform Data Collection and define Push Notification channel configurations (i.e. message presets) in Adobe Journey Optimizer .
- Click Save .

To assign this **Product profile** to users, follow the steps below:

- Access the Admin Console .
- From the Products tab, select the Adobe Experience Platform Data Collection card.
- Select your previously configured Product profile .
- From the Users tab, click Add user .
- Type in your user’s name or email address and select the user. Then, click Save . note NOTE If the user was not previously created in the Admin console, refer to the Add users documentation .

### Check your datasets push-datasets

The following schemas and datasets are available with the push notification channel:

Schema
Dataset
Group of fields
Operation
CJM Push Profile Schema
CJM Push Profile Dataset
Push Notification Details
Adobe CJM ExperienceEvent - Message Profile Details
Adobe CJM ExperienceEvent - Message Execution Details
Application Details
Environment Details
Register Push Token
CJM Push Tracking Experience Event Schema
CJM Push Tracking Experience Event Dataset
Push Notification Tracking
Track interactions and provide data for the reporting UI
NOTE
When push tracking events are ingested into the CJM Push Tracking Experience Event dataset, some failures can happen, even though data is partly ingested successfully. This can occur if some fields in your mapping do not exist in incoming events: the system logs warnings but does not prevent ingestion of valid portions of the data. These warnings appear in batch status as ‘failed’ but reflect partial ingestion success.
To view the complete list of fields and attributes for each schema, consult the
Journey Optimizer schema dictionary
.
### Configure your app configure-app

The technical setup involves close collaboration between the app developer and business administrator. Before starting sending push notifications with Journey Optimizer, you need to create push credentials, a Push channel configuration in Adobe Journey Optimizer and and integrate your mobile app with Adobe Experience Platform Mobile SDKs.

Follow implementation steps detailed in the links below:

- For **Apple iOS**: Learn how to register your app with APNs in [Apple Documentation](https://developer.apple.com/documentation/usernotifications/registering_your_app_with_apns#_blank)
- For **Google Android**: Learn how to setup up a Firebase Cloud Messaging client app on Android in [Google Documentation](https://firebase.google.com/docs/cloud-messaging/android/client#_blank)

### Integrate your mobile app with Adobe Experience Platform SDK integrate-mobile-app

Adobe Experience Platform Mobile SDK provides client-side integration APIs for your mobiles via Android and iOS compatible SDKs. Follow [Adobe Experience Platform Mobile SDK documentation](https://developer.adobe.com/client-sdks/documentation/getting-started#_blank) to get setup with Adobe Experience Platform Mobile SDKs in your app.

By the end of this, you should have also created and configured a mobile property in Adobe Experience Platform Data Collection. You will typically create a mobile property for each mobile application you want to manage. Learn how to create and configure a mobile property in [Adobe Experience Platform Mobile SDK documentation](https://developer.adobe.com/client-sdks/documentation/getting-started/create-a-mobile-property#_blank).

## Step 1: Add your app push credentials in Journey Optimizer push-credentials-launch

After granting the correct user permissions, you now need to add your mobile application push credentials in Journey Optimizer.

The mobile app push credential registration is required to authorize Adobe to send push notifications on your behalf. Refer to the steps detailed below:

- Access the Channels > Push settings > Push credentials menu.
- Click Create push credential .
- From the Platform drop-down, select the Operational system: For iOS Enter the mobile app App ID . Enable the Apply to all sandboxes option to make these Push credentials available across all sandboxes. If a specific sandbox has its own credentials for the same Platform and App ID pair, those sandbox-specific credentials will take precedence. Switched on the Manually enter push Credentials button to add your credentials. Drag and drop your .p8 Apple Push Notification Authentication Key file. This key can be acquired from the Certificates , Identifiers and Profiles page. note NOTE Only .p8 Apple Push Notification keys are supported. Use another Apple Developer account if you have reached the .p8 key limit. For more information on Apple key limits, refer to Apple Developer Documentation . Provide the Key ID . This is a 10 character string assigned during the creation of p8 auth key. It can be found under Keys tab in Certificates , Identifiers and Profiles page. Provide the Team ID . This is a string value which can be found under the Membership tab. For Android Provide the App ID , usually the package name is the app id in your build.gradle file. Enable the Apply to all sandboxes option to make these Push credentials available across all sandboxes. If a specific sandbox has its own credentials for the same Platform and App ID pair, those sandbox-specific credentials will take precedence. Switched on the Manually enter push credentials button to add your credentials. Drag and drop the FCM push credentials. For more details on how to get the push credentials refer to Google Documentation .

- Click **Submit** to create your app configuration.

## Step 2: Create a channel configuration for push message-preset

Once creating your push credentials, you need to create a configuration to be able to send push notifications from **Journey Optimizer**.

- Access the Channels > General settings > Channel configurations menu, then click Create channel configuration .
- Enter a name and a description (optional) for the configuration. note NOTE Names must begin with a letter (A-Z). It can only contain alpha-numeric characters. You can also use underscore _ , dot . and hyphen - characters.
- To assign custom or core data usage labels to the configuration, you can select Manage access . Learn more about Object Level Access Control (OLAC) .
- Select Push channel.
- Select Marketing action (s) to associate consent policies to the messages using this configuration. All consent policies associated with the marketing action are leveraged in order to respect the preferences of your customers. Learn more
- Choose your Platform : Android and/or iOS .
- For App id , select the value that matches your push credential . Optionally, use personalization to drive many apps from one journey or campaign. Learn more
- Save your changes.

You can now select your configuration when creating your push notifications.

### Personalize the App id (optional) app-id-personalization

When you have many brands or tenants with separate apps, you can store each **App id** on the profile and use a single channel configuration to send push notifications to the correct app for each recipient.

To do so, click the Personalization icon next to the **App id** field, select a profile attribute mapped to the app id, and save. The field uses the corresponding [Handlebars expression](/en/docs/journey-optimizer/using/content-management/personalization/personalization-syntax) evaluated for each recipient at send time.

{width="70%"}

CAUTION
Journey Optimizer does not check that
push credentials
exist for every value the expression may return. Make sure you have push credentials for every possible app id, and test with representative profiles. If a recipient’s resolved app id has no matching push credentials, they will not be delivered as expected.
## Step 3: configure Adobe Journey Optimizer extension in your mobile property configure-journey-optimizer-extension

The **Adobe Journey Optimizer extension** for Adobe Experience Platform Mobile SDKs powers push notifications for your mobile apps and helps you collects user push tokens and manages interaction measurement with Adobe Experience Platform services.

Learn how to setup Journey Optimizer extension in [Adobe Experience Platform Mobile SDK documentation](https://developer.adobe.com/client-sdks/documentation/adobe-journey-optimizer#_blank).

## Step 4: Test your mobile app with an event mobile-app-test

After configuring your mobile app in both Adobe Experience Platform and in Adobe Experience Platform Data Collection, you can now test it before sending push notifications to your profiles. In this use case, we create a journey to target our mobile app and set an event which triggers the push notification.

For this journey to work, you need to create an XDM schema. For more information, refer to [XDM documentation](/en/docs/experience-platform/xdm/schema/composition#schemas-and-data-ingestion#_blank).

- In the DATA MANAGEMENT menu section, click Schemas .
- Click Create schema , in the top right, select Experience Event and click Next .
- Enter a name and description for your schema and click Finish .
- In the Field groups section, on the left, click Add and select Create a new field group .
- Enter a Display Name and a Description . Click Add field groups when done. For more information on how to create field groups, refer to XDM System documentation .
- On the left side, select the schema. In the right pane, enable this schema for Profile .
- On the left side, select the field group, then click the + icon to create a new field. In the Field groups properties , on the right side, type in a Field name , Display name and select String as Type .
- Check Required and click Apply .
- Click Save . Your schema is now created and can be used in an event.

You then need to set up an event.

- From the left menu of the home page, under ADMINISTRATION, select Configurations . The click Manage in the Events section to create your new event.
- Click Create Event , the event configuration pane opens on the right side of the screen.
- Enter the name of your event. You can also add a description.
- In the Event ID type field, select Rule Based .
- In the Parameters , select your previously created schema.
- In the list of fields, check that the field created in the schema field group is selected.
- Click Edit in the Event ID condition field. Drag and drop your previously added field to define the condition that will be used by the system to identify the events that trigger your journey.
- Type in the syntax that you will need to use to trigger your push notification in your test app, in this example order confirmation .
- Select ECID as your Namespace .
- Click Ok then Save .

Your event is now created and can now be used in a journey.

- In the left menu, click Journeys .
- Click Create Journey to create a new journey.
- Edit the journey’s properties in the configuration pane displayed on the right side. Learn more in this section .
- Start by drag and dropping the event created in the previous steps from the Events drop-down.
- From the Actions drop-down, drag and drop a Push activity to your journey.
- Configure the push notification. For more information on how to create push notifications, refer to this page .
- Click the Test toggle to start testing your push notifications and click Trigger an event .
- Enter your ECID in the Key field then type in order confirmation in the second field.
- Click Send .

Your event will be triggered and you will receive your push notification to your mobile app.

recommendation-more-help
