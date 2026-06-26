---
title: "Create code-based experiences create-code-based"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/code-based-experience/create-code-based-experiences/create-code-based"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:57.094269+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create code-based experiences create-code-based

Last update: May 8, 2026
- Topics:
- [Code-based Experiences](#)

CREATED FOR:

- Experienced
- User

In Journey Optimizer, you can create code-based experiences in a journey or a campaign.

## Add a code-based experience through a journey or a campaign create-code-based-experience

To start building your code-based experience through a journey or a campaign, follow the steps below.

Add a code-based experience to a journey
To add a **code-based experience** activity to a journey, follow these steps:

- Create a journey .
- Start your journey with an Event or a Read Audience activity.
- Drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select Code-based experience as the action type. note NOTE As Code-based experience is an inbound experience activity, it comes with a 3-days Wait activity. Learn more
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the code-based experience configuration to use. Learn more note NOTE When you have multiple code-based experience actions using the same channel configuration, the journey’s Priority score determines what is delivered to the end-user if they qualify for more than one action. Learn more on priority scores
- Select the Edit content button and edit your content as desired using the personalization editor. Learn more You can also use an existing content template as a basis for your code content. Note that the templates available to choose are scoped to either HTML or JSON based on the channel configuration that has been chosen beforehand. Learn how to use content templates
- You can add one or more inbound actions to your code-based experience by clicking the Add action button. Learn more
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

Create a code-based experience campaign
To start building your **code-based experience** through a campaign, follow the steps below.

- Create a campaign. Learn more
- Select the Scheduled - Marketing campaign type.
- Complete the steps to create a campaign, such as the campaign properties, audience , and schedule . For more information on how to configure a campaign, refer to this page .
- Select the Code-based experience action.
- Select or create the code-based experience configuration to use. Learn more note NOTE When you have multiple code-based experience actions using the same channel configuration, the campaign’s Priority score determines what is delivered to the end-user if they qualify for more than one action. Learn more on priority scores
- Edit your content as desired using the personalization editor. Learn more You can also use an existing content template as a basis for your code content. Note that the templates available to choose are scoped to either HTML or JSON based on the channel configuration that has been chosen beforehand. Learn how to use content templates![](assets/code-based-campaign-edit-content.png)

For more information on how to create, configure and activate a campaign, refer to [this page](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns).

➡️ [Learn how to create a code-based experience campaign in this video](#video)

## Edit the code content edit-code

To edit the content of your code-based experience, follow the steps below.

- From the journey activity or the campaign edition screen, select Edit code . note NOTE If you are using a code-based experience content template with predefined editable form fields, you can manage the content of these fields without opening the personalization editor. Learn more
- The personalization editor opens. It is a non-visual experience creation interface which allows you to author your code.
- You can switch the authoring mode from HTML to JSON, and vice versa. note caution CAUTION Changing the authoring mode will result in losing all of your current code, so make sure to switch modes before you start authoring.
- Enter your code as needed. You can leverage the Journey Optimizer personalization editor with all its personalization and authoring capabilities. Learn more
- You can add HTML or JSON expression fragments if needed. Learn how You can also save part of your code content as fragment. Learn how
- With code-based experiences, you can use the Decisioning feature. Select the Decision policy icon from the left bar and click Add decision policy . Learn more ![](../experience-decisioning/assets/decision-code-based-create.png) From the journey or campaign edition screen, you can also directly add a decision policy without opening the personalization editor. Use the dedicated icon on the right rail to display the Decisioning section.![](assets/code-based-campaign-show-decisioning.png) The detailed steps to create a decision policy are presented in this section .
- Click Save and close to confirm your changes.

Now as soon as your developer makes an API or SDK call to fetch content for the surface defined in your channel configuration, the changes will be applied to your web page or app.

## How-to video video

The video below shows how to create a code-based experience campaign, configure its properties, test, and publish it.

https://video.tv.adobe.com/v/3428868/?quality=12&learn=on
recommendation-more-help
