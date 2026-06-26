---
title: "Send a message to the subscribers of a list send-a-message-to-the-subscribers-of-a-list"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/message-to-subscribers-uc"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:05.524198+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Send a message to the subscribers of a list send-a-message-to-the-subscribers-of-a-list

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Use Cases](#)
- [Subscriptions](#)

CREATED FOR:

- Intermediate
- Experienced
- User
- Developer

The purpose of this use case is to create a journey to send a message to the subscribers of a list.

In this example, the **Consent and Preference Details** field group from Adobe Experience Platform is used. To find this field group, from the **Data Management** menu, choose **Schemas**. On the **Field groups** tab, enter the name of the field group in the search field.

To configure this journey, follow these steps:

- Create a journey that starts with a Read activity. Learn more in Create your first journey .
- Add an Email action activity to the journey. Learn how to Work with channel actions .
- In the Email parameters section of the Email activity settings, replace the default email address ( PersonalEmail.adress ) with the email address of the list subscribers: Click the Enable parameter override icon at the right of the Address field, then click the Edit icon. In the expression editor, enter the expression to retrieve the subscribers’ email addresses. Read more . This example shows an expression that includes references to map fields: code language-json #{ExperiencePlatform.Subscriptions.profile.consents.marketing.email.subscriptions.entry('daily-email').subscribers.firstEntryKey()} In this example, these functions are used: table 0-row-3 1-row-3 2-row-3 Function Description Example entry Refers to a map element according to the selected namespace Refer to a specific subscription list firstEntryKey Retrieves the first entry key of a map Retrieve the first email address of subscribers In this example, the subscription list is named daily-email . Email addresses are defined as keys in the subscribers map, which is linked to the subscription list map. Read more about references to fields in expressions. In the Add an expression dialog box, click Ok .

CAUTION
Email address override should only be used for specific use cases. Most of the time, you do not need to change the email address because the value defined as the primary address in the
Execution fields
is the one that should be used.
Learn more
recommendation-more-help
