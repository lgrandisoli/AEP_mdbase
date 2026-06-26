---
title: "Send a message with Campaign v7/v8 campaign-v7-v8-use-case"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/ajo-ac"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:11.209073+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Send a message with Campaign v7/v8 campaign-v7-v8-use-case

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Integrations](#)
- [Custom Actions](#)
- [Use Cases](#)

CREATED FOR:

- Intermediate
- Experienced
- Admin
- Developer
- User

This use case explains all the steps required to send an email using the integration with Adobe Campaign v7 and Adobe Campaign v8.

NOTE
In order to use this integration, you must have Campaign v7/v8 build 9125 or higher.
First, create a transactional email template in Campaign. Then, in Journey Optimizer, create the event, action, and design the journey.

To learn more about the Campaign integration, refer to these pages:

- [Creating a Campaign action](/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/acc-action)
- [Using the action in a journey](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/using-adobe-campaign-v7-v8).

**Adobe Campaign**

Your Campaign instance must be provisioned for this integration. The Transactional Messaging feature must be configured.

- Log in to your Campaign control instance.
- Under Administration > Platform > Enumerations , select the Event type (eventType) enumeration. Create a new event type (“journey-event”, in our example). Use the internal name of the event type when writing the JSON file later.
- Disconnect and reconnect to the instance for the creation to take effect.
- Under Message Center > Transactional message templates , create a new email template based on the event type previously created.
- Design your template. In this example, personalization is applied to the profile’s first name and the order number. The first name is in the Adobe Experience Platform data source, and the order number is a field from the Journey Optimizer event. Ensure you use the correct field names in Campaign.
- Publish your transactional template.
- Write the JSON payload corresponding to the template.

```
{
     "channel": "email",
     "eventType": "journey-event",
     "email": "Email address",
     "ctx": {
          "firstName": "First name", "purchaseOrderNumber": "Purchase order number"
     }
}
```

- For the channel, you need to type “email”.
- For the eventType, use the internal name of the event type created previously.
- The email address will be a variable, so you can type any label.
- Under ctx, the personalization fields are also variables.

**Journey Optimizer**

- Create an event. Include the “purchaseOrderNumber” field.
- Create an action in Journey Optimizer corresponding to your Campaign template. In the Action type drop-down, select Adobe Campaign Classic .
- Click the Payload field and paste the JSON created earlier.
- For the email address and the two personalization fields, change Constant to Variable .
- Now create a new journey and start with the event previously created.
- Add the action and map each field to the correct field in Journey Optimizer.
- Test your journey.
- You can now publish your journey.

recommendation-more-help
