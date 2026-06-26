---
title: "Use case: ramp up your deliveries use-case-ramp-up-your-deliveries"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/ramp-up-deliveries-uc"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:06.004217+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Use case: ramp up your deliveries use-case-ramp-up-your-deliveries

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Use Cases](#)
- [IP Warmup Plans](#)

CREATED FOR:

- Intermediate
- Experienced
- User
- Developer

If you recently moved to another email service provider, IP address, or email domain or subdomain, you need to establish your reputation as a sender. Otherwise, your deliveries might be blocked or moved to the spam folder of the recipients’ mailbox. Learn how to increase your email reputation with IP warming in the [Deliverability Best Practice Guide](/en/docs/deliverability-learn/deliverability-best-practice-guide/additional-resources/generic-resources/increase-reputation-with-ip-warming#_blank).

To warm up your IP, you can gradually ramp up the number of your deliveries. Read more about [optimizing deliverability in Journey Optimizer](/en/docs/journey-optimizer/using/monitor/deliverability/deliverability).

The purpose of this use case is to create a journey to ramp up your email deliveries. To configure this journey, follow these steps:

- Create a journey. Read more .
- Add an Optimize activity to the journey. Read more .
- In the Condition activity settings, set the maximum number of recipients for your delivery: In the Optimize activity settings, select Conditions method and set the Type field to Profile cap . Read more . Set the Limit field to the maximum number of recipients for this delivery. You can gradually increase this limit up to the total number of your subscribers.
- Add an Email action activity to the nominal path after the Condition activity. When the journey runs, the message is sent the entering profiles, up to the maximum number of profiles that you have specified. When this limit is reached, the entering profiles take the alternate path.
- Complete the journey with the activities of your choice.

After your IP has warmed up, you can remove this condition.

recommendation-more-help
