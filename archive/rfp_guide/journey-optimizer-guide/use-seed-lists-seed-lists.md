---
title: "Use seed lists seed-lists"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/seed-lists"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:40.548716+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use seed lists seed-lists

Last update: May 8, 2026
- Topics:
- [Seed Lists](#)
- [Channel Configuration](#)

CREATED FOR:

- Intermediate
- User

Seed lists in Journey Optimizer enable you to automatically include specific seed addresses in your deliveries.

CAUTION
Currently this feature only applies to the email channel.
Seed addresses are used to target recipients who do not match the defined target criteria. This way, recipients who are out of the delivery scope can receive the delivery, as any other target recipient would.

Seed addresses are not real profiles nor test profiles as they do not include any profile details. They are only recipients belonging to internal stakeholders stored in the system. When selected in a specific campaign or journey, they are included at the delivery execution time, meaning they will receive a copy of the delivery for assurance purposes.

- By receiving deliveries at the same time and in the same conditions as your customers, seed lists allow you to monitor the email copies sent out to ensure that all display formats, images and links are correct, as well as keeping track of the actual messages sent out to your recipients. For example: accordion If you are a marketing manager: You want all your team members to receive copies of sent messages at the same time as your customers. This way your team can ensure that messages are sent out with the expected layout, active URLs, correct text and images - all as planned before execution. accordion If you are a product owner: You need to keep track of actual messages sent out to customers. Indeed, your team and leadership may be interested in some campaigns and need to be added on an ad hoc basis for receiving copies of message at the delivery time.
- Another reason for using seed lists is your mailing list protection. Inserting seed addresses into your mailing list lets you be noticed if it is being used by a third party, as the seed addresses it contains will receive the deliveries sent to your mailing list.

NOTE
Variants are supported, including multilingual and experimentation variants. Each seed address receives a single copy of every variant of the same message, e.g. different versions from a
content experiment
. Please note, separate seed emails are not sent for conditional content.
## Access the seed lists access-seed-lists

To access the seed lists already created, go to **Administration** > **Channels** > **Email settings**, and select **Seed list**.

CAUTION
To be able to view, edit and manage seed lists, you must have the
Manage Seedlist
permission.
You can search seed lists by name, and/or filter on the user who created the list or on the creation date. Once selected, you can clear the filter displayed on top of the list.

Use the **Delete** button to permanently remove an entry.

CAUTION
It is not possible to delete a seed list which is used in an active
campaign
or
journey
. You need to deactivate the campaign/journey, or edit it to use another configuration that has not the seed list selected.
Learn more about using a seed list
You can click a seed list name to edit it.Use the **Edit** button to edit a seed list.

## Create a seed list create-seed-list

To create a seed list, follow the steps below.

- Access the Administration > Channels > Email settings > Seed list menu.
- Select the Create seed list button.![](assets/seed-list-create-button.png)
- Fill in the details. Start by adding a name. note NOTE Names must begin with a letter (A-Z) and include only alpha-numeric characters or special characters ( _, ., -).
- Select the channel. Currently only the email channel is available.
- Select a test profile. Because seed addresses do not include profile details, this test profile will be only used to display the personalization data in the message sent to the seed addresses. note NOTE Only one test profile can be selected at a time.
- Add the seed addresses you want to send your deliveries to. You can either import a CSV file or manually enter email addresses. note NOTE You can combine both options, but the total number of addresses in a seed list cannot exceed 300.
- Click Create to confirm. The newly created seed list displays in the Seed list screen .

## Use a seed list in a campaign or journey use-seed-list

Now that your seed list is created, you can use it in any campaign or journey to include the corresponding seed addresses in your deliveries. To do so, follow the steps below.

CAUTION
Messages sent to seed addresses are not included in journey or campaign reports.
- Create a configuration and select the Email channel. Learn more
- Select the seed list of your choice in the corresponding section . note NOTE Only one seed list can be selected at a time.
- Submit the configuration.
- Create a campaign or a journey .
- Select the Email action and select the configuration including the seed list that is relevant to you.
- Activate your campaign or publish your journey .

Now each time an email message is sent out to your customers through that campaign or journey, the email addresses on the selected seed list will also receive it in the same conditions, at the same time and with the same content as the targeted recipients.

NOTE
Test mode
journeys do not send emails to the seed list. To check your email content, use the
preview and test
functionality before sending your message.
For recurring journeys, the email delivery is sent to the seed addresses at every journey execution, provided that at least one profile reaches the email node.
recommendation-more-help
