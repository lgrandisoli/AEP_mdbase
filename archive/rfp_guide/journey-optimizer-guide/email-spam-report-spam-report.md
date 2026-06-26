---
title: "Email spam report spam-report"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/test/preview-test/spam-report"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:43.861520+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Email spam report spam-report

Last update: May 8, 2026
- Topics:
- [Preview](#)

CREATED FOR:

- Beginner
- User

You can check your email content spam scoring in a dedicated Spam report. Using [SpamAssassin](https://spamassassin.apache.org/#_blank), Adobe Journey Optimizer can test your email content and give it a score to indicate if ISPs or Mailbox providers will consider it as a spam or not.

When editing or previewing your email content, the **Spam report** button provides a scoring and advice to improve scores for each individual item that is listed.

This capability allows you to determine whether a message could be considered as spam by the anti-spam tools used upon receipt, and to take actions if this is the case. Many email inbox providers use tools as part of their spam filtering process. Sending emails with a bad score can severely impact your deliverability.

To access the **Spam report**, follow the steps below.

- From the Simulate screen, click the Spam report button.

- An anti-spam checking is automatically performed and the Spam report window displays the results. It shows how your content is doing in terms of body layout, structure, image size, spam trigger words if any, etc.
- Check the scores and descriptions for each item. The lower the score, the better. If the score is higher than 5, a warning is displayed: it indicates that some messages may be blocked or marked as spam when received. Best practice is to have a score lower than 2. note NOTE Spam score is derived via SpamAssassin , and rules are not owned by Adobe. For more details about these rules, refer to the SpamAssassin documentation.
- Based on that scoring, if you consider that some elements can be improved, edit your content in the Email Designer and make the necessary updates.
- Once your changes are done, browse back to the Spam report screen to ensure your score has improved.

recommendation-more-help
