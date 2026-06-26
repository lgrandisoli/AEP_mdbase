---
title: "Get started with email design get-started-content-design"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:50.060179+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with email design get-started-content-design

Last update: May 8, 2026
- Topics:
- [Email Design](#)

CREATED FOR:

- Beginner
- Intermediate
- User

To access the Email Designer and start designing your email content, you must first [create an email](/en/docs/journey-optimizer/using/channels/email/create-email) in a journey or a campaign.

You can then use Journey Optimizer **email design capabilities** to import existing content or start building responsive emails from scratch. [Learn more](/en/docs/journey-optimizer/using/channels/email/design-email/start-creating-content/content-from-scratch)

The Email Designer also enables you to:

- Leverage Adobe Experience Manager Assets Essentials to enrich your emails, build and manage your own assets database. Learn more
- Find Adobe Stock photos to build your content and improve your email design. Learn more
- Enhance customers’ experience by creating personalized and dynamic messages based on their profile attributes. Learn more about personalization and dynamic content .

➡️ [Discover this feature in video](#video)

## Key steps to create email content key-steps

Once you have created an email, you can start designing your email content.

- From the journey or campaign configuration screen, go through the Edit content screen to access the Email Designer. Learn more
- On the Email Designer home page, choose how you want to design your email from the following options: Design your email from scratch through the Email Designer’s interface and leverage images from Adobe Experience Manager Assets . Learn how to design your email content in this section . Code or paste raw HTML directly in the Email Designer. Learn how to code your own content in this section . note NOTE In a campaign, you can also select the Code Editor button from the Edit content screen. Learn more Import existing HTML content from a file or a .zip folder. Learn how to import an email content in this section . Convert image designs to HTML templates using the AI-powered image to HTML converter. Learn how to transform static images into editable email templates in this section . Select an existing content from a list of built-in or custom templates. Learn how to work with email templates in this section .
- Once your email content has been defined and personalized, you can export your content for validation or for later use. Click Export HTML to save on your computer a zip file which will include your HTML and assets.
- You can also validate your content quality to identify potential issues with readability, content cohesiveness, and effectiveness. Learn more about content quality validation

## Email design best practices best-practices

When sending emails, it’s important to consider that recipients may forward them, which can sometimes cause issues with the email’s rendering. This is particularly true when using CSS classes that may not be supported by the email provider used for forwarding, for example, if you are using the “is-desktop-hidden” CSS class to hide an image on mobile devices.

To minimize these rendering issues, we recommend keeping your email design structure as simple as possible. Try to use a single design that works well for both desktop and mobile devices, and avoid using complex CSS classes or other design elements that may not be fully supported by all email clients. By following these best practices, you can help ensure that your emails are consistently rendered correctly, regardless of how they are viewed or forwarded by recipients.

Refer to the table below for best practices for email design:

Recommended
Use with Care
Not recommended
- **Static, table-based layouts** for structure
- **HTML tables and nested tables** for layout consistency
- **Template widths** between 600px and 800px
- **Simple, inline CSS** for styling
- **Web-safe fonts** for universal compatibility

- **Background images** may not appear on certain email platforms.
- **Custom web fonts** lack universal support.
- **Wide layouts** can display poorly on smaller screens.
- **Image maps** offer limited functionality.
- **Embedded CSS** is sometimes removed during email delivery.

- **JavaScript** is generally unsupported in email environments.
- **<iframe>** tags are blocked on most platforms.
- **Flash** is outdated and no longer supported.
- **Embedded audio** often fails to play.
- **Embedded video** is incompatible with many email platforms.
- **Forms** do not work within emails.
- <div> layering can lead to rendering issues.

NOTE
The
European accessibility act
states that all digital communications should be accessible. In addition to the email design best practices listed in this section, make sure you also follow the guidelines listed on
this page
specific to building accessible content with the Email Designer.
## How-to videos video

Learn how to create email content with the message editor.

https://video.tv.adobe.com/v/334150?quality=12&learn=on
Learn how to configure content experiments to A/B test and explore email content best drives your business objectives.

https://video.tv.adobe.com/v/3419893?learn=on
recommendation-more-help
