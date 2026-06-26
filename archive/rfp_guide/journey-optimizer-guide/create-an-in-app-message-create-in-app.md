---
title: "Create an In-app message create-in-app"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/in-app/create-in-app"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:54.210039+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create an In-app message create-in-app

Last update: May 8, 2026
- Topics:
- [In App](#)

CREATED FOR:

- Beginner
- User

You can add an In-app message in a campaign or in a journey. Follow the steps detailed below to create an In-app message in both contexts.

Note that In-app messages are not impacted by the user’s choice to opt-in or opt-out of push notifications at the operating system.

Add an In-app message to a journey
To add an In-app message in a journey, follow these steps:

- Open your journey , then drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select In-app as the action type. note NOTE When a profile reaches the end of their journey, any in-app messages displayed to them will automatically expire. For that reason, a 3-days Wait activity is automatically added after your In-app action to ensure proper timing. Learn more
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the in-app configuration to use. Learn more
- Select the Edit content button and create your content as desired. Learn more
- Click Edit triggers to choose the event(s) and criteria that will trigger your message. Rule builders enable users to specify criteria and values that, when met, trigger a set of actions, such as sending an in-app message. Learn more Click the event drop-down to change your Trigger if needed. accordion See available Triggers table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 Package Trigger Definition Send data to Platform Sent data to Platform Triggered when the mobile app issues an edge experience event to send data to Adobe Experience Platform. Usually the API call sendEvent from the AEP Edge extension. Core tracking Track action Triggered when the legacy functionality offered in mobile code API trackAction is called. Core tracking Track state Triggered when the legacy functionality offered in mobile code API trackState is called. Core tracking Collect PII Triggered when the legacy functionality offered in mobile code API collectPII is called. Application lifecycle Application launch Triggered at every run, including crashes and installs. Also triggered on a resume from the background when the lifecycle session timeout has been exceeded. Application lifecycle Application install Triggered at the first run after installation or re-installation. Application lifecycle Application update Triggered at the first run after an upgrade or when the version number changes. Application lifecycle Application close Triggered when the application is closed. Application lifecycle Application crash Triggered when the application is not backgrounded before being closed. The event is sent when the application is started after the crash. Adobe Mobile crash reporting does not implement a global uncaught exception handler. Places Enter POI Triggered by the Places SDK when your customer enters the Point of Interest (POI) that you configured. Places Exit POI Triggered by the Places SDK when your customer exits the Point of Interest (POI) that you configured. Click Add condition if you want the trigger to consider multiple events or criteria. Choose the Or condition if you want to add more Triggers to further expand your rule. Choose the And condition if you want to add Traits and better fine-tune your rule. accordion See available Traits table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 12-row-3 13-row-3 14-row-3 15-row-3 16-row-3 17-row-3 Package Traits Definition Device info Carrier name Triggered when one of the Carrier name from the list is met. Device info Device name Triggered when one of the Device name is met. Device info Locale Triggered when one of the language from the list is met. Device info OS version Triggered when one of the specified OS version is met. Device info Previous OS version Triggered when one of the specified Previous OS version is met. Device info Run mode Triggered if Run mode is either application or extension. Application lifecycle App ID Triggered when the specified App ID is met. Application lifecycle Day of week Triggered when the specified day of week is met. Application lifecycle Day since first use Triggered when the specified number of day since first use is met. Application lifecycle Day since last use Triggered when the specified number of day since last use is met. Application lifecycle Day since upgrade Triggered when the specified number of day since last upgrade is met. Application lifecycle Install date Triggered when the specified Install date is met. Application lifecycle Launches Triggered when the specified number of Launches is met. Application lifecycle Time of day Triggered when the specified Time of day is met. Places Current POI Triggered by the Places SDK when your customer enters the specified Point of Interest (POI). Places Last entered POI Triggered by the Places SDK depending on your customer last entered Point of Interest (POI). Places Last exited POI Triggered by the Places SDK depending on your customer last exited Point of Interest (POI). Click Make group to group triggers together. Choose the frequency of your trigger when your In-app message is active: Show every time : Always show the message when the events selected in the Mobile app trigger drop-down occur. Show once : This message appears only once per user session and stays visible across all windows or activities until closed. To limit it to a certain screen or make it dismiss automatically, use custom logic with the messaging delegate. Show until click through : Show this message when the events selected in the Mobile app trigger drop-down occur until an interact event is sent by the SDK with an action of “clicked”.
- You can add one or more inbound actions to your in-app message by clicking the Add action button. Learn more
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

| note |
| --- |
| NOTE |
| If you want to show an in-app message shortly after sending a push notification, use a **Wait** activity to allow the in-app message payload time to propagate. Typically a 5–15 minute wait is recommended, but exact times can vary depending on payload complexity and personalization needs. |

Add an In-app message to a campaign
To add an In-app message in a campaign, follow these steps:

- Access the Campaigns menu, then click Create campaign .
- Select the type of campaign that you want to execute Scheduled - Marketing : execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface. API-triggered - Marketing/Transactional : execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing, or transactional messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc.
- From the Properties section, enter the Title and the Description description.
- To assign custom or core data usage labels to the In-app message, select Manage access . Learn more .
- Click the Select audience button to define the audience to target from the list of available Adobe Experience Platform audiences. Learn more .
- In the Identity namespace field, choose the namespace to use in order to identify the individuals from the selected audience. Learn more .
- In the Actions section, choose the In-app message and select or create a new configuration. Learn more about In-app configuration on this page .
- Click Create experiment to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. Learn more
- Click Edit triggers to choose the event(s) and criteria that will trigger your message. Rule builders enable users to specify criteria and values that, when met, trigger a set of actions, such as sending an in-app message. Click the event drop-down to change your Trigger if needed. accordion See available Triggers table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 Package Trigger Definition Send data to Platform Sent data to Platform Triggered when the mobile app issues an edge experience event to send data to Adobe Experience Platform. Usually the API call sendEvent from the AEP Edge extension. Core tracking Track action Triggered when the legacy functionality offered in mobile code API trackAction is called. Core tracking Track state Triggered when the legacy functionality offered in mobile code API trackState is called. Core tracking Collect PII Triggered when the legacy functionality offered in mobile code API collectPII is called. Application lifecycle Application launch Triggered at every run, including crashes and installs. Also triggered on a resume from the background when the lifecycle session timeout has been exceeded. Application lifecycle Application install Triggered at the first run after installation or re-installation. Application lifecycle Application update Triggered at the first run after an upgrade or when the version number changes. Application lifecycle Application close Triggered when the application is closed. Application lifecycle Application crash Triggered when the application is not backgrounded before being closed. The event is sent when the application is started after the crash. Adobe Mobile crash reporting does not implement a global uncaught exception handler. Places Enter POI Triggered by the Places SDK when your customer enters the Point of Interest (POI) that you configured. Places Exit POI Triggered by the Places SDK when your customer exits the Point of Interest (POI) that you configured. Click Add condition if you want the trigger to consider multiple events or criteria. Choose the Or condition if you want to add more Triggers to further expand your rule. Choose the And condition if you want to add Traits and better fine-tune your rule. accordion See available Traits table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 12-row-3 13-row-3 14-row-3 15-row-3 16-row-3 17-row-3 Package Traits Definition Device info Carrier name Triggered when one of the Carrier name from the list is met. Device info Device name Triggered when one of the Device name is met. Device info Locale Triggered when one of the language from the list is met. Device info OS version Triggered when one of the specified OS version is met. Device info Previous OS version Triggered when one of the specified Previous OS version is met. Device info Run mode Triggered if Run mode is either application or extension. Application lifecycle App ID Triggered when the specified App ID is met. Application lifecycle Day of week Triggered when the specified day of week is met. Application lifecycle Day since first use Triggered when the specified number of day since first use is met. Application lifecycle Day since last use Triggered when the specified number of day since last use is met. Application lifecycle Day since upgrade Triggered when the specified number of day since last upgrade is met. Application lifecycle Install date Triggered when the specified Install date is met. Application lifecycle Launches Triggered when the specified number of Launches is met. Application lifecycle Time of day Triggered when the specified Time of day is met. Places Current POI Triggered by the Places SDK when your customer enters the specified Point of Interest (POI). Places Last entered POI Triggered by the Places SDK depending on your customer last entered Point of Interest (POI). Places Last exited POI Triggered by the Places SDK depending on your customer last exited Point of Interest (POI). Click Make group to group triggers together.
- Choose the frequency of your trigger when your In-app message is active. The following options are available: Everytime : Always show the message when the events selected in the Mobile app trigger drop-down occur. Once : Only show this message the first time the events selected in the Mobile app trigger drop-down occur. Until click through : Show this message when the events selected in the Mobile app trigger drop-down occur until an interact event is sent by the SDK with an action of “clicked”. X number of times : Show this message X time.
- If needed, choose which Day of the week or Time of day the In-app message will be displayed.
- Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the Schedule of your campaign in this section .
- You can now start designing your content with the Edit content button. Learn more

For more information on how to create, configure and activate a campaign, refer to [this page](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns).

## How-to videos video

- The video below shows how to create, configure, and publish In-app messages in your campaigns. accordion See video embed https://video.tv.adobe.com/v/3410430?quality=12&learn=on
- The video below shows how to configure and analyze content experiments to A/B test In-app messages. accordion See video embed https://video.tv.adobe.com/v/3419898/?learn=on&autoplay=true
- The video below shows how to create an In-app message in a journey and how to test and publish your journey. accordion See video embed https://video.tv.adobe.com/v/3423077/?learn=on&autoplay=true

**Related topics:**

- [Design In-app message](/en/docs/journey-optimizer/using/channels/in-app/design-in-app)
- [Test and send your In-app message](/en/docs/journey-optimizer/using/channels/in-app/send-in-app)
- [In-app report](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-inapp)
- [In-app configuration](/en/docs/journey-optimizer/using/channels/in-app/inapp-configuration)

recommendation-more-help
