---
title: "Send proofs using test profiles data send-proofs"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/test/preview-test/proofs"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:47.585056+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Send proofs using test profiles data send-proofs

Last update: May 8, 2026
- Topics:
- [Preview](#)
- [Proofs](#)

CREATED FOR:

- Beginner
- User

A proof is a specific message that allows you to test a message before sending it to the main audience. Recipients of the proof are in charge of approving the message: rendering, content, personalization settings, configuration.

NOTE
Journey Optimizer also allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV / JSON file, or added manually.
Learn how to simulate content variations
## Must-read must-read

**Frequency capping rules** - All existing frequency capping rules apply to proofs. If you have set [frequency capping rules](/en/docs/journey-optimizer/using/conflict-prioritization/capping-rules/channel-capping) (e.g., maximum sends per profile), these limits also apply when sending proofs. If a test profile has already reached the frequency cap limit, proofs will show as finished but no email will be delivered. For repeated testing, consider using unique test profiles or adjusting frequency caps for proofing scenarios as needed.

**Mirror page** - In the proof sent, the link to the mirror page is not active. It is only activated in the final messages.

**Assets** - Assets and images have specific accessibility rules:

- Assets/Images are accessible in delivered content or proof content for up to 2 years (730 days) since their first publication in any fragment/inline message.
- Re-publishing is required after this expiry period (any time after 730 days) to keep them accessible for another 2 years.
- Any re-publication done within 730 days of the first publication will not extend the expiry of assets/images to the next 730 days.

## Send proofs send-proofs-steps

To send email proofs using test profiles data, you must first select [test profiles](/en/docs/journey-optimizer/using/test/preview-test/test-profiles). Then, follow these steps:

- In the Simulate screen, click the Send proof button.
- From the Send proof window, type in your recipient’s email and click Add to send the proof to yourself or members of your organization. Note that you can add up to ten recipients for your proof delivery.
- Select the Test profiles to use to personalize the message content. Each recipient of the proof receives as many messages as the number of selected test profiles. For example, if you added five recipient emails and selected ten test profiles, you will send fifty proof messages. Each recipient will receive ten of them.
- You can add a prefix to the subject line of the proof if needed. Only alphanumeric characters and special characters such as . - _ ( ) [ ] are allowed as prefix to the subject line.
- Click Send proof .
- Back in the Simulate screen, click the View proofs button to check status.

It is recommended to send proofs after each modification to the message content.

recommendation-more-help
