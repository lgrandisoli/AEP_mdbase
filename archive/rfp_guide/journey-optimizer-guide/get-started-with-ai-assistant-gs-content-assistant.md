---
title: "Get started with AI Assistant gs-content-assistant"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/ai-assistant/gs-generative"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:48.451965+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with AI Assistant gs-content-assistant

Last update: May 8, 2026
- Topics:
- [Content Assistant](#)

CREATED FOR:

- Beginner
- User

INFO
Immerse yourself in a hands-on experience with
our live feature preview
, designed to let you explore its features firsthand and fully understand its capabilities.
The AI Assistant in Adobe Journey Optimizer, powered by Microsoft Azure OpenAI and Adobe Firefly, brings proactive content variation suggestions for text and images. This new capability provides a **prompt based text and image generation**. Image generation is managed with Adobe Firefly.

AI Assistant supports generation **in multiple languages** enabling you to reach and engage diverse global audiences. AI Assistant is available in the following languages:

- Chinese (Hong Kong)
- Chinese (Simplified)
- Chinese (Taiwan)
- Dutch

- French
- German
- Italian
- Japanese

- Norwegian
- Portuguese
- Spanish
- Swedish

Use AI Assistant in Adobe Journey Optimizer to optimize your message’s impact by experimenting with different main titles and images. Generate multiple variant and build an experiment to compare them. Leveraging **Journey Optimizer Content Experiment**, you can define multiple message treatments in order to measure which one performs best for your target audience. You can choose to vary the delivery content, or subject. The message audience is randomly allocated to each treatment to determine which one works best in terms of the specified metric. Learn more about Content Experiment in [this section](/en/docs/journey-optimizer/using/content-management/content-experiment/content-experiment).

IMPORTANT
- Before you start using this capability, read the related Guardrails and limitations .
- You must agree to a user agreement before you can use AI Assistant in Adobe Journey Optimizer. For more information, contact your Adobe representative.

## Access AI Assistant generative-access

To access AI Assistant in Adobe Journey Optimizer feature, users need to be granted the **Generate Content** permission. [Learn more](/en/docs/journey-optimizer/using/access-control/permissions)

Learn how to assign Content generation related permissions
- In the Permissions product, go to the Roles tab and select the desired Role .
- Click Edit to modify the permissions.
- Add the AI Assistant resource, then select Generate Content from the drop-down menu. {modal="regular"}
- Click Save to apply changes. Any users already assigned to this role will have their permissions automatically updated.
- To assign this role to new users, navigate to the Users tab within the Roles dashboard and click Add User .
- Enter the user’s name, email address, or choose from the list, then click Save .
- If the user was not previously created, refer to the this documentation .

The user will receive an email with instructions to access your instance.

## Guardrails and limitations generative-guardrails

General guidelines for using AI Assistant in Adobe Journey Optimizer for email generation are listed below:

### Supported channels

- Only available for the email, push, web and SMS channels.

### Content quality, prompts, and feedback

- The quality of the generated content is strongly impacted by the marketing objective / prompt you define. Use well defined prompt for the GenAI model to accurately interpret.
- GenAI content might not always be accurate: please share your feedback so that our engineers can refine the models.
- Make sure to report any problematic outputs using the thumb up, thumb down or flag icons when selecting variants.

### Brand assets

- Upload brand asset to have accurate, on brand content. Else, content is based on publicly available info. The uploaded content can be in the following formats: PDF, JPEG, PNG, or ZIP files (with supported file formats).
- The maximum size for uploaded brand asset is 50MB. Larger files or lots of images can work but the processing time is increased.
- You may upload multiple brand assets, but can leverage only one for a specific generation.

### Email templates and imagery

- Use brand specific or custom template to create your email content using AI Assistant in Adobe Journey Optimizer. Email templates with up to 8-10 images is recommended.

### Legal use and transparency

- Your use of AI Assistant is subject to the Adobe Experience Cloud Generative AI User Guidelines. [Learn more](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html)
- As part of Adobe’s commitment to promote transparency in the use of generative AI tools in media creation, Adobe will apply Content Credentials when content or a project that included a Firefly generated asset is downloaded or exported. [Learn more](https://helpx.adobe.com/firefly/using/content-credentials.html)

### AI assistant for personalization expressions ai-assistant-personalization-editor-guardrails

The following guardrails apply to [AI Assistant for personalization expressions](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-personalization-expressions) in the Personalization Editor and in the Email Designer.

- **Offer and Experience Decisioning** — Not supported.
- **Favorites** — Not supported.
- **Saved conditions** — Not supported.
- **Adobe Experience Manager Content Fragments** — Not supported.

## AI Assistant content generation capabilities generative-features

**Generate full content**

**Generate text**

**Generate images**

## Additional resources

- **Generative experimentation** - Understand how to combine AI-generated content with experimentation.
- **AI Assistant use cases** - Learn through use cases how to use AI Assistant
- **AI Assistant tutorials** - Explore step-by-step video tutorials on AI Assistant features and best practices.

recommendation-more-help
