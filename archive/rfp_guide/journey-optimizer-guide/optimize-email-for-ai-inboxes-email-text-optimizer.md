---
title: "Optimize email for AI inboxes email-text-optimizer"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/design-email/add-content/llm-email-optimizer"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:39.746104+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Optimize email for AI inboxes email-text-optimizer

Last update: May 8, 2026
- Topics:
- [Email Design](#)

CREATED FOR:

- Beginner
- Intermediate
- User

Adobe Journey Optimizer comes with an email-channel capability that helps you structure a specific version of your messages for improved AI-assisted inbox experiences—such as Apple Intelligence and Google Gemini in Gmail—so they can answer questions and summarize mail based on your content more accurately, with better results.

You can use this capability to generate and refine a dedicated version of your messages so AI-assisted inbox experiences are more likely to surface the offers, calls to action, and details you intend—rather than thin auto-generated text or unrelated context.

## How it works how-it-works

Typical questions recipients may ask in AI-assisted inbox experiences are *What is this email about?* or *What are these offers?*.

- The answers provided by these AI assistants may be a short summary (for example that the message is promotional, mentions VIP early access and a sale, and includes links to product categories). However, they still omit objectives the marketer cared about because the assistants are inferring from whatever text they effectively see—not necessarily the full story you intended.
- Also, the assistants may proactively search for discounts or coupons related to the brand and fold those into the answer, so the user is no longer looking at only what your message actually promised. That behavior is useful to end users, but dilutes control for marketers who need answers to track the real terms in the send.

To prevent these issues, Journey Optimizer creates an additional specific version of your messages so that coupons, discount ranges, call to actions, and other priorities appear up front in clear linear copy.This version is different from the HTML view and default or custom plain text version of your messages.

The goal is for inbox AI to ground summaries and Q&A in your defined offers and actions—instead of leaning on a thin default text part or on unrelated web results.

IMPORTANT
Exact AI-assistant behaviors depend on the inbox provider and model version. After your email is delivered, answers and summaries provided by external AI clients can be wrong, incomplete, or mixed with web results.
The Optimize email for AI inboxes capability only generates a dedicated version in Journey Optimizer; it does not guarantee how a third-party assistant will interpret or display the message. Read more about the
limitations and risks of third-party inbox AI
.
## Recommended use cases use-cases

- Dense or fragmented content — When the content of the email is hard to scan, optimization can produce a clearer linear narrative with explicit offers and links.
- Controlling inbox Q&A — When you expect recipients to ask assistants what the email is about or what the offers are , a strong optimized for AI version reduces partial summaries and avoids reliance on web-supplemented answers that are not tied to your approved copy.

## Optimize for AI inbox experiences optimize-with-ai

IMPORTANT
Before you use this capability, read the related
Risks and limitations
.
To access this feature, you must agree to a user agreement which displays the first time you use Generative AI in Journey Optimizer. For more information, read the
Adobe Experience Cloud Generative AI User Guidelines
.
To optimize the content of your email for AI inbox experiences with Journey Optimizer, follow the steps below.

- Open your email in the Email Designer (from a campaign, journey, or template, depending on your workflow).
- Click the Optimize for AI Inbox button to generate an improved version that highlights key information for AI-assisted reading and summarization. {width="80%" modal="regular"}
- If this is the first time you are using Generative AI in Journey Optimizer, you will be asked to agree to the user agreement. To learn more, check out the Adobe Generative AI User Guidelines . {width="50%"} Click Agree to continue.
- The generated version is displayed in the AI Inbox Optimizer window. {width="80%" modal="regular"} note NOTE The optimized version is different from the HTML and text views of your email. It does not change your design, layout, or images.
- To edit the content automatically generated, select the Enable edit toggle and make manual changes as needed.
- Once happy with your version, click the Optimize Email button to confirm. You can also use the Re-optimize button to generate a new version.
- You are redirect to the HTML view and your email is now successfully optimized for AI inboxes. To access again or edit the optimized version, click the Optimized for AI Inbox button. {width="80%" modal="regular"}
- The optimized version is displayed. You can Remove optimization , or click Re-optimize to generate a new version. {width="80%" modal="regular"} note NOTE If you make changes to the original HTML content, you need to re-optimize the generated version for AI inboxes so that it is consistent with the new content.

## Risks and limitations of third-party inbox AI inbox-ai-risks

The Optimize email for AI inboxes capability helps you prepare a version of your email for how mailbox providers may process your Journey Optimizer sends. It does not control those providers’ products. Once a message is delivered, any AI features in Gmail, Apple Mail, Outlook, or other clients operate under their terms, models, and policies—not Adobe’s.

- Unpredictable presentation — Summaries, notification blurbs, and conversational answers can omit offers, misstate prices or dates, merge content with unrelated web results, or paraphrase in ways that no longer match your approved copy. This behavior can change when vendors update models or UI without notice.
- No guarantee of parity with HTML — Recipients who rely on previews or assistant answers may never see your full HTML design, images, or legal footers. What they believe the message “says” may come only from a short AI-generated digest.
- Privacy, compliance, and data use — Inbox AI may process message content on provider infrastructure subject to that provider’s privacy policy, retention, and regional rules. Organizations in regulated industries should assess whether recipient use of such features affects their obligations, independent of how the email was authored in Journey Optimizer.
- Brand and legal exposure — Incorrect or incomplete AI summaries can still create customer confusion or disputes about promotions, terms, or opt-out language. Journey Optimizer does not ensure that a third party’s model will reproduce the optimized version of your email faithfully.
- Optimize for AI Inbox in Journey Optimizer — The authoring-time control in the Email Designer is separate from end-user inbox assistants. Always review generated content before send.

## Related topics related-topics

- [Get started with email design](/en/docs/journey-optimizer/using/channels/email/design-email/get-started-email-design)
- For Adobe generative features more broadly, see [Get started with AI Assistant to create content](/en/docs/journey-optimizer/using/content-management/ai-assistant/gs-generative).

recommendation-more-help
