---
title: "Create a SMS/MMS/RCS message create-sms"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/sms/create-sms"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:32.644355+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create a SMS/MMS/RCS message create-sms

Last update: May 8, 2026
- Topics:
- [SMS](#)

CREATED FOR:

- Beginner
- User

AVAILABILITY
RCS is not a HIPAA-Ready Service and must not be used to collect, store, or process any sensitive personal data, including permitted health data, e.g. personal health information, that your organization may otherwise be permitted to process in Journey Optimizer.
You can design and send text (SMS), rich communication (RCS) and multimedia (MMS) messages with Adobe Journey Optimizer. You first need to add an SMS action in a journey or a campaign, and then define the content of the text message, as detailed below. Adobe Journey Optimizer also offers capabilities to test your text messages before sending, so that you can check the rendering, personalization attributes, and all other settings.

In accordance with the industry standards and regulations, all SMS/MMS marketing messages must contain a way for the recipients to easily unsubscribe. To do this, SMS recipients can reply with opt-in and opt-out keywords. [Learn how to manage opt-out](/en/docs/journey-optimizer/using/privacy/consent/opt-out#opt-out-decision-management)

## Add a text message create-sms-journey-campaign

Browse the tabs below to learn how to add a text message (SMS/MMS/RCS) in a campaign or a journey.

Add a text message to a Journey
- Open your journey then drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select SMS as the action type.
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the SMS configuration to use. Learn more
- Additionally, you can apply capping rules to your SMS action by selecting a rule set in the Business rules drop-down list. Learn more
- Select the Edit content button and create your content as desired. Learn more
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

Add a text message to a Campaign
- Access the Campaigns menu, then click Create campaign .
- Select the type of campaign that you want to execute Scheduled - Marketing : execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface. API-triggered - Marketing/Transactional : execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing or transactional messages, i.e., messages sent out following an action performed by an individual: password reset, cart purchase, etc.
- From the Properties section, edit your Campaign’s Title and Description .
- Click the Select audience button to define the audience to target from the list of available Adobe Experience Platform audiences. Learn more .
- In the Identity namespace field, choose the namespace to use in order to identify the individuals from the selected audience. Learn more .
- In the Actions section, choose the SMS and select or create a new configuration. Learn more about SMS configuration on this page .
- Click Create experiment to start configuring your content experiment and create treatments to measure their performance and identify the best option for your target audience. Learn more
- In the Actions tracking section, specify if you want to track clicks on links in your SMS message.
- Campaigns are designed to be executed on a specific date or on a recurring frequency. Learn how to configure the Schedule of your campaign in this section .
- From the Action triggers menu, choose the Frequency of your SMS message: Once Daily Weekly Month

You can now start designing the content of your text message from the **Edit content** button, as detailed below.

For more information on how to create, configure and activate a campaign, refer to [this page](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns).

## Define your SMS/RCS content sms-content

To configure your message content, follow the steps below. Settings for MMS are detailed in [this section](#mms-content).

- From the journey or campaign configuration screen, click the Edit content button to configure the text message content.
- Click the Message field to open the personalization editor. For RCS messaging with Infobip, Twilio, or other third-party providers, paste the required JSON payload into your custom SMS configuration .
- Generate engaging text messages tailored to your audience using AI Assistant for text generation .
- Use the personalization editor to define content, add personalization and dynamic content. You can use any attribute, such as the profile name or city for example. You can also define conditional rules. Browse to the following pages to learn more about personalization and dynamic content in the personalization editor.
- After defining your content, you can add tracked URLs to your message. To do this, access the Helper functions menu and select Helpers . To use the URL shortening function, you must first configure a subdomain that will then be linked to your configuration. Learn more note NOTE To access and edit SMS subdomains, you must have the Manage SMS Subdomains permission on the production sandbox. Learn more about permissions in this section .
- Within the Helper functions menu, click URL function and then select Add URL . The URL shortening function cannot be used within a fragment. TBC
- In the originalUrl field, paste the URL that you want to shorten and click Save . note caution CAUTION The lifespan of short URLs is set to 30 days. After this period, these short URLs will no longer be accessible and will display the message: 404 short-code not found .
- Use the Character count to monitor SMS length as you compose the message. It updates in real time and indicates when the content will be delivered in multiple segments.
- Click Save and check your message in the preview. You can now test and check your message content as detailed in this section .

## Personalize with Decisioning decisioning-sms

You can personalize and optimize the content of your SMS messages with **Decisioning**. This capability allows you to use Priority Scores, Formulas, or AI Models to dynamically select and display the best content to your customers.

For more information on how to create and use decision policies in SMS messages, refer to [this section](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decision-policies/create-decision).

## Define your MMS content mms-content

You can enhance your communication by sending Multimedia Message Service (MMS) messages, enabling the sharing of media such as videos, pictures, audio clips and GIFs, and more. Additionally, MMS allows for up to 1600 characters of text in your message.

NOTE
MMS channel comes with a few limitations listed on
this page
.
To create MMS content, follow these steps:

- Create a SMS as described in this section .
- Edit your SMS content as detailed in this section .
- Enable the MMS option to add media to your SMS content.
- Add a Title to your media.
- Enter the URL of your media in the Media field.
- Click Save and check your message in the preview. You can now test and check your message content as detailed below.

## Test and send your messages sms-mms-test

Use the **Simulate content** button to preview your text message content, shortened URLs, and personalized content.

Once you have performed your tests and validated the content, you can send your text message to your audience. These steps are detailed on [this page](/en/docs/journey-optimizer/using/channels/sms/send-sms)

Once sent, you can measure the impact of your SMS within the Campaign or Journey reports. For more on reporting, refer to [this section](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-sms).

**Related topics**

- [Preview, test and send your text message](/en/docs/journey-optimizer/using/channels/sms/send-sms)
- [Configure SMS channel](/en/docs/journey-optimizer/using/channels/sms/configure-sms/sms-configuration)
- [SMS/MMS reports](/en/docs/journey-optimizer/using/reporting/channel-report/journey-reporting/journey-global-report-cja-sms)
- [Add a message in a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-action)
- [Add a message in a campaign](/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign)

recommendation-more-help
