---
title: "AI & intelligent features ai-features"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/get-started/essentials/ai-features"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:29.581256+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# AI & intelligent features ai-features

Last update: May 8, 2026
- Topics:
- [Overview](#)

CREATED FOR:

- Beginner
- User

Adobe Journey Optimizer harnesses the power of artificial intelligence and machine learning to help you create, optimize, and deliver exceptional customer experiences. From generating personalized content to predicting optimal send times, AI capabilities streamline your workflow and maximize impact. Use Case Playbooks provide pre-built templates to quickly implement common marketing scenarios.

## AI Assistant ai-assistant

AI Assistant is your conversational guide to Adobe Journey Optimizer. Use it to get instant answers about product features, operational insights about your journeys, and help navigating the platform.

### Access AI Assistant

Click the AI Assistant icon in the top bar to open the assistant panel on the right side of your screen.

IMPORTANT
You must agree to the
Adobe Experience Cloud Generative AI User Guidelines
before using AI Assistant.
### What AI assistant can do

**Product Knowledge** - Ask questions about Adobe Journey Optimizer features and concepts:

- “How do I set up a campaign in Adobe Journey Optimizer?”
- “How do I create a custom action to use in journeys?”
- “How many live activities can I have in one sandbox?”

**Operational Insights (Beta)** - Get real-time information about your journeys:

- “How many live journeys do I have?”
- “Give me a list of all scheduled journeys”
- “How many journeys have been created in the last 7 days?”

NOTE
Operational insights are currently only available for
Journeys
and reflect data from your current sandbox.
### How to use AI assistant

- Enter your question in the text field at the bottom of the panel
- Press Enter to submit your query
- Review the AI-generated response
- Click **Show sources** to access related documentation
- Use thumbs up/down to rate the response quality

{align="left" width="40%"}

[Learn more about AI Assistant in Experience Platform](/en/docs/experience-platform/ai-assistant/home#_blank)

## Advanced AI agents for Journey optimization ai-agents

Building on AI Assistant’s conversational capabilities, Adobe Journey Optimizer offers specialized AI Agents that provide deep analysis and actionable recommendations for journey optimization and experimentation.

### Journey Agent journey-agent

Journey Agent includes two skills in AI Assistant: Analyze and Create. Use them to optimize existing journeys or build new ones from natural language prompts.

Permissions Required
- **View Journeys** - View insights into journeys directly in AI Assistant
- **Manage Journeys** - Create new journeys directly in AI Assistant
- **View Segments** - View insights into audiences and search existing audiences
- **Manage Segments** - Create new audiences directly in AI Assistant
- **View Journey Events, Data Sources and Actions** - Required for the Create skill to search journey events and custom actions

#### Journey analyze skill journey-analyze-skill

The [Journey Analyze Agent](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent#journey-create-agent-skill-overview-and-user-guide#_blank) helps you optimize journey performance through natural language analysis:

Key Capabilities
- **Journey Fallout Analysis** - Identify where and why customers drop off during journeys, detect disengagement patterns
- **Audience Overlap Detection** - Analyze audience overlap across multiple journeys to prevent fatigue from over-targeting
- **Schedule Conflict Detection** - Identify timing conflicts between scheduled journeys targeting the same audience
- **Operational Insights** - Get prompt-based insights like “show me all live journeys” or “which audiences are used in more than X journeys”

Sample Prompts
- “Perform a fallout analysis for journey [Journey Name]”
- “Are there any scheduling conflicts for journey [Journey Name]?”
- “Show me audience overlap conflicts for journey [Journey Name]”
- “Which audiences are used in more than 5 journeys?”

#### Journey create skill journey-create-skill

The [Journey Create Agent](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent#journey-analyze-agent-skill-overview-and-user-guide#_blank) helps you build journeys from natural language prompts, translating your goals into structured journey configurations:

Key Capabilities
- **Natural Language Journey Creation** - Describe your desired journey and have it created automatically
- **Event- and Audience-Based Starts** - Create event-triggered, audience-based, business-event, or audience qualification journeys
- **Conditional Logic** - Build split paths based on customer attributes or behavior
- **Multi-Channel Messaging** - Add email, push, and SMS actions
- **Scheduling** - Configure start dates and timing between steps

Sample Prompts
- “Create a journey that starts when a customer makes a purchase online and sends a thank you push notification.”
- “Build a journey targeting my day hikers audience with three emails over two weeks, starting 12/20.”
- “Create a journey that starts when a user enters my store location and follows up based on whether they have a valid email address.”

### Experimentation Agent experimentation-agent

The [Experimentation Agent](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-experiment#_blank) modernizes how you run and manage digital experiments across websites, emails, push messages, and applications:

Key Capabilities
- **Performance Analysis** - Clear view of what happened in experiments
- **Insights Generation** - Explanation of why results occurred
- **Opportunities Discovery** - Guidance on next actions to take
- **Content Analysis** - Examine messaging elements to understand why certain treatments outperformed others
- **Recommendation Generation** - Suggest new treatments or adjustments based on insights

Sample Prompts
- “What experiments are running for [Campaign Name]?”
- “For my [Experiment Name], what treatment is leading?”
- “What did we learn from [Experiment Name]?”
- “What do you recommend I do next after this experiment?”
- “What common patterns are emerging from recent tests?”

Permissions Required
- **View Experiments** - View insights into experiments in AI Assistant
- **Manage Experiment Metadata** - Create new experiments in AI Assistant

**Note:** Available with Journey Optimizer Experimentation Accelerator license.

### Additional AI Agents

**Audience Agent** - For conversational audience exploration and management across Adobe Experience Platform, including duplicate detection and size tracking. [Learn more about Audience Agent](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/audience#_blank)

**Agent Orchestrator** - Coordinates multiple specialized agents to solve complex, multi-step marketing challenges. The orchestrator automatically determines which agents to involve and sequences their work efficiently. [Learn more about Agent Orchestrator](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-orchestrator#_blank)

## AI-Powered content generation content-generation

Use generative AI to create and personalize content across multiple channels, accelerating your content creation process while maintaining brand consistency. AI Assistant for content generation is available for [email](/en/docs/journey-optimizer/using/channels/email/get-started-email), [push notifications](/en/docs/journey-optimizer/using/channels/push/get-started-push), [SMS](/en/docs/journey-optimizer/using/channels/sms/get-started-sms), and [web](/en/docs/journey-optimizer/using/channels/web/get-started-web) experiences - helping you generate subject lines, body text, images, and complete message variations.

### Key Features

- **Full Content Generation** - Generate complete content experiences (text and images) in one flow for email, web, landing pages, and push. [Generate full content with AI Assistant](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-full-content)
- **Text Generation** - Create compelling copy based on your brand voice and objectives. [Generate text with AI](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-text)
- **Image Generation** - Generate custom images using Adobe Firefly. [Generate images with AI](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-image)
- **Content Variations** - Produce multiple variations for A/B testing. [Content experiment with AI](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-experimentation)
- **Personalization** - Generate new expressions, explain existing code, or fix issues with AI Assistant from the Personalization Editor or from the Email Designer toolbar (**Add expression**). [AI Assistant for Personalization Expressions](/en/docs/journey-optimizer/using/content-management/ai-assistant/generative-personalization-expressions)
- **Brand Alignment** - Ensure generated content matches your brand guidelines. [Evaluate brand alignment](/en/docs/journey-optimizer/using/content-management/ai-assistant/brands/brands-score)
- **Template Support** - Leverage your existing email templates. [Work with content templates](/en/docs/journey-optimizer/using/content-management/content-templates/content-templates)

### Best Practices

- **Be specific** - Provide clear, detailed prompts for better results. [Learn prompt best practices](/en/docs/journey-optimizer/using/content-management/ai-assistant/ai-assistant-prompting-guide)
- **Upload brand assets** - Use PDFs, images, or ZIP files (max 50MB) to maintain brand consistency
- **Use custom templates** - Leverage brand-specific templates with up to 8-10 images
- **Provide feedback** - Rate outputs to help improve the AI models
- **Review all content** - Always review AI-generated content for accuracy before publishing

[Learn more about AI content generation](/en/docs/journey-optimizer/using/content-management/ai-assistant/gs-generative)

## Send-Time Optimization send-time-optimization

Use AI to predict the optimal time to send each message based on individual customer behavior patterns, maximizing engagement.

### How It Works

Send-Time Optimization analyzes historical engagement data (opens and clicks) to predict when each customer is most likely to engage with your messages. The system automatically schedules delivery within your specified time window.

### When to Use It

Best For
Not Recommended For
Marketing campaigns and newsletters
Time-sensitive operational messages (order confirmations, password resets)
Promotional messages
Urgent notifications (flight delays, emergency alerts)
Educational content
Event-based messages with specific timing requirements
Engagement campaigns
[Learn more about Send-Time Optimization](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/send-time-optimization)

## AI models for decisioning ai-decisioning

Create intelligent ranking models that automatically optimize which offers to show to each customer, maximizing business objectives.

### Model Types

**Auto-optimization** - Learns from customer interactions to automatically improve offer performance over time

**Personalized optimization** - Uses customer profile attributes and behavior to predict the best offer for each individual

### Requirements

- At least 2 offers with sufficient interaction data: 100+ display events 5+ click events Within the last 14 days
- Maximum 5 AI ranking models per organization

[Learn more about AI models for decisioning](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-rankings/experience-decisioning-ai-models/ai-models) | [Create AI ranking models](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-rankings/experience-decisioning-ai-models/create-ai-models)

## AI-powered rule and formula optimization decisioning-optimization

Adobe Journey Optimizer can automatically analyze [Decisioning rules](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/rules) and [ranking formulas](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-rankings/ranking-formulas) expressed in PQL syntax, and suggest simplifications that preserve the original logic. When a simplification is found, a red **Optimize** indicator appears next to the rule or formula, opening a side-by-side comparison of the original and AI-suggested expressions, with a downloadable analysis to validate that both behave identically.

### Key Capabilities

- **Logic-preserving simplifications** - The AI suggests a shorter expression that returns the same result on simulated profiles.
- **Validation report** - Download an analysis (TSV) showing how each simulated profile is evaluated against both versions before applying the change.
- **One-click apply** - Replace the original PQL with the optimized version directly from the **Optimize** window.

### Eligibility

Only rules and ranking formulas whose PQL expression is larger than **2 KB** (UTF-8 encoded) are targeted for analysis, smaller expressions are not analyzed.

### Permissions

This capability uses the same generative AI access controls as **AI Assistant**. Users must be granted the **Generate Content** permission on the **AI Assistant** resource. [Learn more about AI Assistant access](/en/docs/journey-optimizer/using/content-management/ai-assistant/gs-generative#generative-access)

[Optimize Decisioning rules](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/rules#optimize) | [Optimize ranking formulas](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-rankings/ranking-formulas#optimize)

## Content Experimentation with AI experimentation

**Experiment Accelerator** helps you run experiments faster with AI-driven insights and recommendations, identifying winning content variations more quickly.

Key capabilities:

- Generate multiple content variations automatically
- Receive AI recommendations for experiment design
- Get early indicators of performance trends
- Accelerate time to statistical significance

[Learn more about Experiment Accelerator](/en/docs/journey-optimizer/using/content-management/content-experiment/experiment-accelerator-gs)

## Use case playbooks playbooks

Use Case Playbooks are pre-built workflows that help you implement common marketing scenarios quickly. Each playbook includes ready-to-use journeys, messages, schemas, and segments.

### How playbooks work

- **Browse** the playbook library to find use cases matching your goals
- **Enable** a playbook to automatically generate all required resources
- **Customize** the generated assets to match your brand and requirements
- **Deploy** to production or test in a development sandbox

### Available Playbooks

Browse Journey Optimizer playbooks for common scenarios like:

- Abandoned cart recovery
- Welcome series for new customers
- Post-purchase engagement
- Birthday messages
- Re-engagement campaigns

Prerequisites
- Sandbox with appropriate permissions
- Channel configurations for email, push, and/or SMS
- User permissions to create journeys and messages

[View all available playbooks](/en/docs/experience-platform/use-case-playbooks/playbooks/playbooks-list#_blank) | [Learn more in Experience Platform documentation](/en/docs/experience-platform/use-case-playbooks/playbooks/overview#_blank)

## Additional AI Capabilities additional-capabilities

### Image to HTML Converter

Transform static image designs (JPEG, PNG) into editable HTML email templates using AI-powered conversion technology.

[Learn more about Image to HTML](/en/docs/journey-optimizer/using/content-management/content-templates/image-to-html)

### GenStudio for performance marketing

Integrate with Adobe GenStudio for Performance Marketing to create AI-powered email content and import templates into Journey Optimizer for orchestration. Export Journey Optimizer templates to GenStudio, generate variations with AI, and bring them back for deployment. (Limited availability, email channel only.)

[Learn more about GenStudio](/en/docs/journey-optimizer/using/content-management/combine/genstudio)

### Brand alignment scoring

Evaluate how well your content aligns with your brand guidelines using AI-powered scoring that measures tone, voice, and messaging consistency.

[Learn more about Brand Alignment](/en/docs/journey-optimizer/using/content-management/ai-assistant/brands/brands-score)

## Frequently asked questions faq

What permissions do I need for AI features?
- **AI Assistant for content generation** - Requires the “Generate Content” permission
- **AI Assistant** product knowledge - Requires agreement to Adobe Generative AI User Guidelines
- **Journey Analyze Agent** - Requires View/Manage Journeys and View/Manage Segments permissions
- **Journey Create Agent** - Requires Manage Journeys, View Journey Events/Data Sources/Actions, View Segments, and Manage Segments permissions
- **Experimentation Agent** - Requires View Experiments and Manage Experiment Metadata permissions

All AI Agents require access to AI Assistant and agreement to Adobe Experience Cloud Generative AI User Guidelines.

[Learn more about permissions](/en/docs/journey-optimizer/using/access-control/ootb-permissions)

Is AI-generated content always accurate?
No. Always review
AI-generated content
for accuracy and brand appropriateness. Use the feedback tools (thumbs up/down) to help improve the models.
What are the main limitations?
- **Send-Time Optimization** - Only available for email and push in journeys; requires 30-day training period
- **AI Content Generation** - Not available for Direct Mail, Content Cards, LINE, or WhatsApp
- **AI Ranking Models** - Maximum 5 models per organization; requires minimum interaction data

How do I get access to these features?
Most AI features are included with Adobe Journey Optimizer. Some capabilities like
Send-Time Optimization
or
AI Agents
may require enablement by Adobe. Contact your Adobe representative for details about your specific license and available features.
Related Articles
- [What is Journey Optimizer?](/en/docs/journey-optimizer/using/get-started/essentials/get-started)
- [Understanding how it works](/en/docs/journey-optimizer/using/get-started/essentials/understanding-ajo)
- [AI content generation](/en/docs/journey-optimizer/using/content-management/ai-assistant/gs-generative)
- [Send-Time Optimization](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/send-time-optimization)
- [AI models for decisioning](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-rankings/experience-decisioning-ai-models/ai-models)

recommendation-more-help
