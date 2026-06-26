---
title: "Preview & test your content preview-test"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/test/preview-test/preview-test"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:45.044666+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Preview & test your content preview-test

Last update: May 8, 2026
- Topics:
- [Preview](#)
- [Proofs](#)

CREATED FOR:

- Beginner
- User

Once your content has been defined, you can preview its content before sending the message. This is a crucial step to ensure that it is accurate but also free of errors both in content and personalization settings.

You can also send test deliveries of your email messages to specific recipients or subscribers for testing and validation, and check their rendering in popular desktop, mobile and web-based clients. Additionally, you can evaluate general content quality aspects such as readability and effectiveness. [Learn more about content quality validation](/en/docs/journey-optimizer/using/content-management/ai-assistant/brands/brands-score#validate-quality)

All these actions can be performed using the **Simulate Content** button, which is accessible from the edit content screen of your message, or from the email and web designers for the email and web channels.

IMPORTANT
If you use
Simulate Content
from an
Orchestrated campaign
channel activity, see
Check and test your content
for more information and important notes.
## Testing using test profiles data or sample input data methods

Journey Optimizer provides two experiences to test your content:

- Testing content using test profiles data You can use test profiles to preview your content, send email proofs and check email rendering. If you have added personalized fields, you can check how they are displayed using test profile data. For more information, refer to these sections: ➡️ Select test profiles ➡️ Preview using test profiles ➡️ Send email proofs ➡️ Check email rendering ➡️ Preview & proof your email (video)
- Testing content variations using sample input data Journey optimizer allows you to preview and send proofs for different variations of your content using sample input data uploaded from a CSV / JSON file, or added manually. All the profiles attributes used in your content for personalization are automatically detected by the system and can be used for your tests to create multiple variants. ➡️ Simulate content variations

## Must-read

- Required permissions - You need to have the Manage Simulate Content permission included in the Content Library Manager product profile. Learn more . To send proofs, you must have Approve and publish permissions for the specific resource (campaign or journey) associated with the email. In addition, to send proofs in a journey, the Publish journey permission is also required. Learn more about permissions .
- Personalization with context data - When previewing a message or sending proofs, only profile personalization data is displayed. Personalization based on context data, such as event information, can only be tested in the context of a journey. Learn how in this use case .
- Preview content with multiple conditional variants - When simulating or rendering proofs for emails containing multiple conditional variants, Journey Optimizer may require more processing time. If you experience timeouts or error messages, consider reducing the total number of variants or simplifying conditional rules. Learn more about conditional content on this page .

## How-to video video-preview

Learn how to use test profiles to test email rendering across inboxes, preview your personalized emails against test profiles, and send proofs.

https://video.tv.adobe.com/v/3425026?quality=12&learn=on
recommendation-more-help
