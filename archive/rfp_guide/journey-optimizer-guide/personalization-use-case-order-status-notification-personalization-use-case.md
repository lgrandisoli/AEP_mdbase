---
title: "Personalization use case: order status notification personalization-use-case"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/personalization-use-cases/personalization-use-case"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:06.878168+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Personalization use case: order status notification personalization-use-case

Last update: May 8, 2026
- Topics:
- [Personalization](#)
- [Use Cases](#)

CREATED FOR:

- Intermediate
- Developer

In this use case, you will see how to use multiple types of personalization in a single push notification message. Three types of personalization will be used:

- **Profile**: message personalization based on a profile field
- **Offer decision**: personalization based on decision management variables
- **Context**: personalization based on contextual data from the journey

The goal of this example is to push an event to Journey Optimizer every time a customer order is updated. A push notification is then sent to the customer with information on the order and a personalized offer.

For this use case, the following prerequisites are needed:

- configure an order event including the order number, status and item name. Refer to this [section](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).
- create a decision, refer to this [section](/en/docs/journey-optimizer/using/decisioning/offer-decisioning/create-manage-activities/create-offer-activities).

➡️ [Discover a similar use case in video](#video)

## Step 1 - Create the journey create-journey

- Click the Journeys menu and create a new journey.
- Add your entry event, and a Push action activity.
- Configure and design your push notification message. Refer to this section .

## Step 2 - Add personalization on profile add-perso

- In the Push activity, click Edit content .
- Click the Title field.
- Enter the subject and add profile personalization. Use the search bar to find the profile’s first name field. In the subject text, place the cursor where you want to insert the personalization field, and click the + icon. Click Save .

## Step 3 - Add personalization on contextual data add-perso-contextual-data

- In the Push activity, click Edit content and click the Title field.
- Select the Contextual attributes menu. Contextual attributes are only available if a journey has passed contextual data to the message. Click Journey Orchestration . The following contextual information appears: Events : this category regroups all fields from the event(s) placed before the channel action activity in the journey. Journey Properties : the technical fields related to the journey for a given profile, for example the journey ID or the specific errors encountered. Learn more in Journey Orchestration documentation .
- Expand the Events item, and look for the order number field related to your event. You can also use the search box. Click the + icon to insert the personalization field in the subject text. Click Save .
- Now click the Body field.
- Type the message and insert, from the Contextual attributes menu, the order item name and the order progress.
- From the left menu, select Offer decisions to insert a decisioning variable. Select the placement and click the + icon next to the decision to add it to the body.
- Click validate to make sure that there are no errors, and click Save .

## Step 4 - Test and publish the journey test-publish

- Click the Test button, then click Trigger an event .
- Enter the different values to pass in the test. Test mode only works with test profiles. The profile identifier needs to correspond to a test profile. Click Send . The push notification is sent and displayed on the test profile’s mobile phone.
- Verify that there is no error and publish the journey.

## How-to video video

The video below shows a similar use case leveraging contextual data from a journey to personalize an email.

https://video.tv.adobe.com/v/3425027?quality=12&learn=on
recommendation-more-help
