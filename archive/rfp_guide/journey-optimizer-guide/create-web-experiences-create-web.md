---
title: "Create web experiences create-web"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/web/create-web"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:54.931819+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create web experiences create-web

Last update: May 8, 2026
- Topics:
- [Web Channel](#)

CREATED FOR:

- Beginner
- User

Journey Optimizer allows you to personalize the web experience you deliver to your customers through inbound journeys or campaigns.

## Define a web experience through a journey or a campaign create-web-experience

To start building your web experience through a campaign or a journey, follow the steps below.

NOTE
If this is your first time creating a web experience, make sure you follow the prerequisites described in
this section
.
Add a web experience to a journey
To add a **Web** activity to a journey, follow these steps:

- Create a journey .
- Start your journey with an Event or a Read Audience activity.
- Drag and drop an Action activity from the Actions section of the palette. Learn more about the Action activity . note important IMPORTANT Legacy native channel activities (Email, Push, SMS, In-app, Web, Code-based experience, and Content Card) are deprecated as of the March 2026 release. Existing journeys using these activities continue to work without any changes—no migration is required.
- Select Web as the action type. note NOTE As Web is an inbound experience activity, it comes with a 3-days Wait activity. Learn more
- Enter a Label to identify your action in the journey canvas.
- Click the Configure action button.
- You are directed to the Actions tab. From there, select or create the Web configuration to use.
- You can add one or more inbound actions to your web experience by clicking the Add action button. Learn more
- Go back to the journey canvas. If necessary, complete your journey flow by dragging and dropping additional actions or events. Learn more
- Select the Edit content button and edit your content as desired. Learn more

For more information on how to create, configure and publish a journey, refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-gs).

Create a web campaign
To start building your web experience through a campaign, follow the steps below.

- Create a campaign. Learn more
- Select the type of campaign that you want to execute Scheduled - Marketing : execute the campaign immediately or on a specified date. Scheduled campaigns are aimed at sending marketing messages. They are configured and executed from the user interface. API-triggered - Marketing/Transactional : execute the campaign using an API call. API-triggered campaigns are aimed at sending either marketing, or transactional messages, i.e. messages sent out following an action performed by an individual: password reset, cart purchase etc. Learn how to trigger a campaign using APIs
- Complete the steps to create a web campaign, such as the campaign properties, audience , and schedule .
- Select the Web action.
- Select or create the web configuration. Learn more about web configuration
- Click the Edit content button to edit your content as desired. Learn more![](assets/web-campaign-edit-content.png)

For more information on how to configure a campaign, refer to [this page](/en/docs/journey-optimizer/using/campaigns/get-started-with-campaigns).

➡️ [Learn how to create a web campaign in this video](#video)

## Edit web content edit-web-content

Once you [added a web action](#create-web-experience) to a journey or a campaign, you can edit the content of your site using either:

- the [web designer](/en/docs/journey-optimizer/using/channels/web/author-web-pages/web-visual-editor), to author your experience using a visual editor;
- or the [non-visual editor](/en/docs/journey-optimizer/using/channels/web/author-web-pages/web-non-visual-editor).

To start authoring your web experience, follow the steps below.

- From the Action tab of the campaign or the Web activity in the journey, select Edit content .
- The edition screen displays. You can either: Click the Edit web page button to start authoring your content using the web designer for a visual experience. Learn more Unselect the Visual editor option to use the non-visual edition mode instead, and click Add a modification to start editing your web content without loading the visual editor. Learn more

## Test the web experience test-web-experience

Once you [authored your web experience](/en/docs/journey-optimizer/using/channels/web/author-web-pages/web-visual-editor) using the web designer, you can use test profiles to preview your modified web pages. If you inserted personalized content, you can check how this content is displayed, using test profile data.

To do this, click **Simulate content** from either the journey or campaign edit content screen, then add a test profile to check your web page using the test profile data.

You can also open it in the default browser, or copy the test URL to paste it in any browser. This allows you to share the link with your team and stakeholders who will be able to preview the new web experience in any browser before the campaign goes live.

NOTE
When copying the test URL, the content displayed is the one personalized for the test profile used when the content simulation was generated in Journey Optimizer.
Detailed information on how to select test profiles and preview your content is available in the [Content Management](/en/docs/journey-optimizer/using/test/preview-test/preview-test) section.

## Redirect to URL web-redirect-to-url

When creating a web experience, you can redirect visitors to another existing URL rather than authoring a new variation in the web designer.

Using this capacity, you can run a [Content experiment](/en/docs/journey-optimizer/using/content-management/content-experiment/content-experiment) comparing two different experiences instead of just changing a few elements within a page.

For example, create a web campaign with two treatments:

- In Treatment A , author a web experience using the web designer for half of your targeted population.
- In Treatment B , select the Redirect to URL option for the other half of the targeted population. Enter the URL of a page with an alternate design that you authored outside of Journey Optimizer. note NOTE The website preview does not display anymore and the Visual editor toggle button is disabled.

Once your web campaign is live, you can track how the web experience you authored in Journey Optimizer is performing for the visitors of your page against those who were redirected to the external landing page. Learn how with the [experimentation campaign report](/en/docs/journey-optimizer/using/reporting/channel-report/campaign-reporting/campaign-global-report-cja-experimentation)

## Make your web experience live web-experience-live

IMPORTANT
If your campaign is subject to an approval policy, you will need to request approval in order to be able to activate your Web experiences.
Learn more
Once you defined your web experience and you edited your content as desired, you can activate your journey or campaign to make your changes visible to your audience.

You can also preview your web experience content before making it live. [Learn more](#test-web-experience)

NOTE
If you activate a web journey/campaign impacting the same pages as another journey or campaign which is already live, all the changes will be applied to your web pages.
If multiple journeys or campaigns update the same element(s) of your website, the highest priority journey/campaign takes precedence.
### Publish a web journey activate-web-journey

To make your web experience live from a journey, follow the steps below.

- Verify that your journey is valid and that there is no error. Learn more
- From the journey, select the Publish option, located in the top right drop-down menu. note NOTE Learn more about publishing journeys in this section .

Your web journey takes the **Live** status and is now read-only. Each recipient of your journey can see the modifications you added to your website.

NOTE
After you click
Publish
, it can take up to 15 minutes for the changes to be available live on your website.
### Activate a web campaign activate-web-campaign

Once you defined your web campaign settings and you edited your content as desired, you can review and activate your web campaign. Follow the steps below.

- From your web campaign, select Review to activate .
- Check and edit if needed the content, properties, configuration, audience and schedule.
- Select Activate . note NOTE Learn more about activating campaigns in this section .

Your web campaign takes the **Live** [status](/en/docs/journey-optimizer/using/campaigns/manage-campaigns#statuses) and is now visible to the selected audience. Each recipient of your campaign can see the modifications you added to your website.

NOTE
After you click
Activate
, it can take up to 15 minutes for web campaigns changes to be available live on your website.
If you defined a schedule for your web campaign, it has the
Scheduled
status
until the start date and time are reached.
Once your experience is live, you can monitor your web journeys and campaigns. [Learn more](/en/docs/journey-optimizer/using/channels/web/author-web-pages/monitor-web-experiences)

## Stop a web journey or campaign stop-web-experience

When a web journey or campaign is live, you can stop it to prevent your audience from seeing your modifications. Follow the steps below.

- Select a live journey or campaign from the respective list.
- Perform the relevant action according to your case: From the campaign top menu, select Stop campaign . From the journey top menu, click the More button and select Stop .
- The modifications you added are not be visible anymore to the audience you defined.

NOTE
Once a web journey or campaign is stopped, you cannot edit or activate it again. You can only duplicate it and activate the duplicated journey/campaign.
## How-to video video

The video below shows how to create a web campaign, configure its properties, review, and publish it.

https://video.tv.adobe.com/v/3418800/?quality=12&learn=on
recommendation-more-help
