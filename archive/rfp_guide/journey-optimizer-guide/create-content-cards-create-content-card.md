---
title: "Create content cards create-content-card"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/content-card/create-content-card"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:56.432690+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create content cards create-content-card

Last update: May 8, 2026
- Topics:
- [Content Cards](#)

CREATED FOR:

- Beginner
- User

IMPORTANT
By default, the close button hides the card. To add more functionality, you can manually define dismissal or disqualification rules.
Add Content cards to a journey
To add a Content card to a journey, follow these steps:

- Open your journey , then drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select Card as the action type. note NOTE As Card is an inbound experience activity, it comes with a 3-days Wait activity. Learn more
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the content card configuration to use. Learn more
- You can now start designing your content with the Edit content button. Learn more
- Enable the Enable additional delivery rules option then select Edit rules to define when your message should be shown, dismissed, or permanently hidden. Click Add condition to select your event. accordion See available Events table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 Package Trigger Definition Send data to Platform Sent data to Platform Triggered when the mobile app issues an edge experience event to send data to Adobe Experience Platform. Usually the API call sendEvent from the AEP Edge extension. Core tracking Track action Triggered when the legacy functionality offered in mobile code API trackAction is called. Core tracking Track state Triggered when the legacy functionality offered in mobile code API trackState is called. Core tracking Collect PII Triggered when the legacy functionality offered in mobile code API collectPII is called. Application lifecycle Application launch Triggered at every run, including crashes and installs. Also triggered on a resume from the background when the lifecycle session timeout has been exceeded. Application lifecycle Application install Triggered at the first run after installation or re-installation. Application lifecycle Application update Triggered at the first run after an upgrade or when the version number changes. Application lifecycle Application close Triggered when the application is closed. Application lifecycle Application crash Triggered when the application is not backgrounded before being closed. The event is sent when the application is started after the crash. Adobe Mobile crash reporting does not implement a global uncaught exception handler. Choose the Or condition if you want to add more Triggers to further expand your rule. Choose the And condition if you want to add Traits and better fine-tune your rule. accordion See available Traits table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 12-row-3 13-row-3 14-row-3 Package Traits Definition Device info Carrier name Triggered when one of the Carrier name from the list is met. Device info Device name Triggered when one of the Device name is met. Device info Locale Triggered when one of the language from the list is met. Device info OS version Triggered when one of the specified OS version is met. Device info Previous OS version Triggered when one of the specified Previous OS version is met. Device info Run mode Triggered if Run mode is either application or extension. Application lifecycle App ID Triggered when the specified App ID is met. Application lifecycle Day of week Triggered when the specified day of week is met. Application lifecycle Day since first use Triggered when the specified number of day since first use is met. Application lifecycle Day since last use Triggered when the specified number of day since last use is met. Application lifecycle Day since upgrade Triggered when the specified number of day since last upgrade is met. Application lifecycle Install date Triggered when the specified Install date is met. Application lifecycle Launches Triggered when the specified number of Launches is met. Application lifecycle Time of day Triggered when the specified Time of day is met. Click Make group to group triggers together.
- You can add one or more inbound actions to your content card by clicking the Add action button. Learn more
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

Add Content cards to a campaign
To start building your content cards through a campaign, follow the steps below.

- Create a campaign. Learn more
- Select the type of campaign that you want to execute Scheduled - Marketing : execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface. API-triggered - Marketing/Transactional : execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing , or transactional messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc. Learn how to trigger a campaign using APIs
- In the Properties section, specify a name and a description for the campaign.
- In the Audience section, click the Select audience button to display the list of available Adobe Experience Platform audiences. Learn more about audiences
- In the Identity namespace field, choose the namespace to use in order to identify the individuals from the selected segment. Learn more about namespaces
- Select the Content card action.
- Select or create a new Content card configuration .
- Select an Inbox configuration that defines the inbox surface for this Content card .
- To test the content of your message, click Create experiment . This allows you to test multiple variables of a delivery on sample populations to determine which treatment has the greatest impact on the targeted audience. Learn more about content experiment .
- Enable the Enable additional delivery rules option then select Edit rules to define when your message should be shown, dismissed, or permanently hidden. Use rule builders to set specific conditions that trigger these actions. Click Add condition to select your event. accordion See available Events table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 Package Trigger Definition Send data to Platform Sent data to Platform Triggered when the mobile app issues an edge experience event to send data to Adobe Experience Platform. Usually the API call sendEvent from the AEP Edge extension. Core tracking Track action Triggered when the legacy functionality offered in mobile code API trackAction is called. Core tracking Track state Triggered when the legacy functionality offered in mobile code API trackState is called. Core tracking Collect PII Triggered when the legacy functionality offered in mobile code API collectPII is called. Application lifecycle Application launch Triggered at every run, including crashes and installs. Also triggered on a resume from the background when the lifecycle session timeout has been exceeded. Application lifecycle Application install Triggered at the first run after installation or re-installation. Application lifecycle Application update Triggered at the first run after an upgrade or when the version number changes. Application lifecycle Application close Triggered when the application is closed. Application lifecycle Application crash Triggered when the application is not backgrounded before being closed. The event is sent when the application is started after the crash. Adobe Mobile crash reporting does not implement a global uncaught exception handler. Choose the Or condition if you want to add more Triggers to further expand your rule. Choose the And condition if you want to add Traits and better fine-tune your rule. accordion See available Traits table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 8-row-3 9-row-3 10-row-3 11-row-3 12-row-3 13-row-3 14-row-3 Package Traits Definition Device info Carrier name Triggered when one of the Carrier name from the list is met. Device info Device name Triggered when one of the Device name is met. Device info Locale Triggered when one of the language from the list is met. Device info OS version Triggered when one of the specified OS version is met. Device info Previous OS version Triggered when one of the specified Previous OS version is met. Device info Run mode Triggered if Run mode is either application or extension. Application lifecycle App ID Triggered when the specified App ID is met. Application lifecycle Day of week Triggered when the specified day of week is met. Application lifecycle Day since first use Triggered when the specified number of day since first use is met. Application lifecycle Day since last use Triggered when the specified number of day since last use is met. Application lifecycle Day since upgrade Triggered when the specified number of day since last upgrade is met. Application lifecycle Install date Triggered when the specified Install date is met. Application lifecycle Launches Triggered when the specified number of Launches is met. Application lifecycle Time of day Triggered when the specified Time of day is met. Click Make group to group triggers together.
- You can schedule your campaign to a specific date or set to recur at regular intervals. Learn more
- You can now start designing your content with the Edit content . Learn more

recommendation-more-help
