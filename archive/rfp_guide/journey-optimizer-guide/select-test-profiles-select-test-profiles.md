---
title: "Select test profiles select-test-profiles"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/test/preview-test/test-profiles"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:41.260806+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Select test profiles select-test-profiles

Last update: May 8, 2026
- Topics:
- [Preview](#)
- [Proofs](#)

CREATED FOR:

- Beginner
- User

Test profiles are additional recipients who do not match the defined targeting criteria. [Learn how to create test profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles)

Before using test profiles to test your content, you first need to select them. To do this, follow these steps:

- From the edit content screen of your message or in the Email Designer, click the Simulate content button and select Simulate content .
- Click the Manage test profiles button then select the namespace to use to identify test profiles by clicking the Identity namespace selection icon. Learn more about Adobe Experience Platform identity namespaces . In the example below, we use the Email namespace.
- Use the search field to find the namespace, select it and click Select
- In the Identity value field, enter the value (here the email address) to identify the test profile and click Add profile .![](assets/preview-identity-value.png)
- If you added personalization to your message, add other profiles so that you can test different variants of the message depending on profile data. Once added, profiles are listed under the selected fields. Based on the message personalization elements, this list displays data for each test profile in the related columns.

NOTE
In addition to test profiles, Journey optimizer also allows you to test different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV / JSON file, or added manually.
Learn how to simulate content variations
recommendation-more-help
