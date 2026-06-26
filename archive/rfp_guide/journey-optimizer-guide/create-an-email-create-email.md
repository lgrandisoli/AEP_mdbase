---
title: "Create an email create-email"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/create-email"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:52.941786+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create an email create-email

Last update: May 8, 2026
- Topics:
- [Email](#)

CREATED FOR:

- Beginner
- User

## Add an email action email-action

To create an email in Journey Optimizer, add an **Email** action to a journey or a campaign. Then follow the steps below, according to your case.

Add an email to a journey
- Open your journey, then drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select Email as the action type.
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the email configuration to use. Learn more
- Additionnally: You can apply capping rules to your email action by selecting a rule set in the Business rules drop-down list. Learn more You can use the Send time optimization option to predict the best time to send the message to maximize engagement based on historical open and click rates. Learn how
- Select the Edit content button and create your content as desired using the Email Designer. Learn more
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

Add an email to a campaign
- Create a campaign , and select Email as your action.
- Complete the steps to create an email campaign, such as the campaign properties, audience , and schedule .
- Select the Email action.
- Select or create the email configuration. Learn more

From the **Action** section, specify if you want to track how your recipients react to your delivery: you can track email opens, and/or clicks on links and buttons in your email.
              
                              ![](assets/email_campaign_tracking.png)
For more information on how to create, configure and activate a campaign, refer to [this page](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns).

## Define your email content define-email-content

After adding the email action to your journey or campaign, you need to define the email content including the subject line, sender information, and email body using the Email Designer. Follow these steps:

- From the journey or campaign configuration screen, click the Edit content button to configure the email content. Learn more
- Toggle Enable decisioning if you want to add decision policies in your email. Decision policies are containers for your offers that leverage the Decisioning engine to dynamically return the best content to deliver for each audience member. Learn how to add a decision policy in an email note availability AVAILABILITY For now, decision policy creation in emails is available in Limited Availability. Contact your Adobe representative to gain access.
- In the Header section, check the From name , From email and BCC fields. They are configured in the email configuration that you selected. Learn more
- Add a subject line for your message. To configure and personalize the subject line with the personalization editor, click the Open personalization dialog icon. Learn more note NOTE The subject line is mandatory. It must not include line breaks.
- Click the Edit email body button to access the Email Designer and start building your content. Learn more
- If you are in a campaign, you can also click the Code Editor button to code your own content in plain HTML using the pop-up window that displays. note NOTE If you already created or imported content through the Email Designer, this content will display in HTML.

## Check alerts check-email-alerts

As you are designing your messages, alerts are displayed in the interface (on top right of the screen) when key settings are missing.

NOTE
If you do not see this button, no alert has been detected.
The settings and elements checked by the system are listed below. You will also find information on how to adapt your configuration to resolve the corresponding issues.

Two types of alerts can happen:

- Warnings refer to recommendations and best practices, such as: The opt-out link is not present in the email body : adding an unsubscription link into your email body is a best practice. Learn how to configure it in this section . note NOTE Marketing-type email messages must include an opt-out link, which is not required for transactional messages. The message category ( Marketing or Transactional ) is defined at the channel configuration level and when creating the message from a journey or a campaign. Text version of HTML is empty : do not forget to define a text version of your email body, as it will be used when HTML content cannot be displayed. Learn how to create the text version in this section . Empty link is present in email body : check that all the links in your email are correct. Learn how to manage content and links in this section . Email size has exceeded the limit of 100KB : for optimal delivery, make sure the size of your email does not exceed 100KB. Learn how to edit email content in this section .
- Errors prevent you from testing or activating the journey/campaign as long as they are not resolved, such as: The subject line is missing : email subject line is mandatory. Learn how to define and personalize it in this section . The email version of the message is empty : this error is displayed when the email content has not been configured. Learn how to design email content in this section . configuration doesn’t exist : you cannot use your message if the configuration you have selected is deleted after the message creation. If this error occurs, select another configuration in the message Properties . Learn more about channel configurations in this section .

CAUTION
To be able to test or activate the journey/campaign using the email, you must resolve all
error
alerts.
## Check and send your email

Once your message content has been defined, you can use test profiles to preview it, send proofs and control its rendering in popular desktop, mobile and web-based clients. If you inserted personalized content, you can check how this content is displayed in the message, using test profile data.

You can also validate your content quality to assess readability, effectiveness, and content cohesiveness. [Learn more about content quality validation](/en/docs/journey-optimizer/using/content-management/ai-assistant/brands/brands-score#validate-quality)

NOTE
In addition to test profiles, Journey optimizer also allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV / JSON file, or added manually.
Learn how to simulate content variations
To do this, click **Simulate content** then add a test profile to check your message using the test profile data.

Detailed information on how to select test profiles and preview your content is available in the [Content Management](/en/docs/journey-optimizer/using/test/preview-test/preview-test) section.

When your email is ready, complete the configuration of your [journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs) or [campaign](/en/docs/journey-optimizer/using/campaigns/action-campaigns/create-campaign), and activate it to send the message.

NOTE
To track the behavior of your recipients through email openings and/or interactions, make sure that the dedicated options in the
Tracking
section are enabled in the journey’s
email activity
or in the email
campaign
.
to move?
recommendation-more-help
