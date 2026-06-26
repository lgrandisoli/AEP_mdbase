---
title: "Report on LLM and AI-generated traffic"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/derived-fields/ai-traffic"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-02T19:07:28.770190+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Report on LLM and AI-generated traffic

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- User

This use case article explores how to use the Customer Journey Analytics derived fields capability as a foundation to report on LLM (Large Language Model) and AI-generated traffic.

NOTE
The effectiveness of the
detection methods
,
detection signatures
and
implementation strategies
depends on your specific data collection method, Experience Platform dataset coverage, and Customer Journey Analytics implementation. Results may vary based on your technical environment, data governance policies, and implementation approach. When using Experience Edge, you’ll need to choose between recording the raw User Agent string or collecting device information.
## Detection methods

To detect LLM and AI-generated traffic, distinguish between:

- **LLM crawlers**: Collect data for training and retrieval augmented generation (RAG).
- **AI agents**: Function as interfaces that perform task on behalf of humans. AI agents prefer to interact via APIs, which bypasses web analytics tracking methods. Nonetheless, you can still analyze a significant portion of AI-generated traffic through websites.

Three common core detection methods to identify and monitor LLM and AI-generated traffic are:

- **User agent identification**: When a request is made to your server, the HTTP User-Agent header is extracted and analyzed against known AI crawler and agent patterns. This server-side method requires access to HTTP headers and is most effective when implemented at the data collection layer.
- **Referrer classification**: The HTTP Referrer header contains the URL of the previous webpage that linked to the current request. This header reveals when users click through to your site from web interfaces like ChatGPT or Perplexity.
- **Query parameter detection**: AI services can append URL parameters (particularly UTM parameters) to links. These parameters persist in the URL and can be detected through standard analytics implementations, making these URL parameters valuable indicators even in client-side tracking scenarios.

The following table illustrates how the detection methods can be used against different LLM and AI interaction scenarios.

Scenario
User agent identification
Referrer classification
Query parameter detection
Training of a model
Agent (
GPTBot
,
ClaudeBot
, and more) can be identified when server-side logging is implemented.
No classification is possible. AI crawlers don’t generate referrers during training.
Detection is impossible. AI crawlers do not add parameters during training.
Agent browsing
Agent (
ChatGPT-User
,
claude-web
) can be identified when server-side logging captures headers.
Classification is possible if the agent navigates from an AI interface with referrer preservation.
Detection is sometimes possible if the AI service adds tracking parameters.
Retrieval augmented generation (RAG) to answer query
Agent (
OAI-SearchBot
,
PerplexityBot
) can be identified with server-side logging.
No classification is typically possible as RAG operations often bypass referrer mechanisms.
Detection is rarely possible unless specifically implemented by the AI provider.
User clicks through
The agent cannot be identified. AI agent appears as a normal user agent.
Classification is possible when users click links from AI interfaces (
chatgpt.com
,
claude.ai
, and more).
Detection is possible when AI services add UTM parameters to outbound links.
Traffic visibility conditions
Require server-side logging integration with Customer Journey Analytics or server-side tagging for agent identification.
Classification depends on AI platform referrer policies and proper HTTP header transmission.
Detection requires parameter preservation through redirects and proper URL parameter collection.
### Challenges

LLM & AI agents demonstrate complex and evolving behaviors when interacting with digital properties. These technologies operate inconsistently across platforms and versions. This inconsistency creates unique challenges for data professionals. The behavioral patterns vary significantly and depend on the specific AI platform, version, and interaction mode used. This operational diversity complicates efforts to track and categorize LLM and AI-generated traffic within standard analytics frameworks. The complex nature of these interactions, combined with their rapid evolution, requires nuanced detection and classification methods to maintain data integrity:

- **Partial data collection**: Some newer AI agents execute limited JavaScript, resulting in incomplete analytics data for client-side implementations. As a result, some interactions are tracked while other interactions are missed.
- **Inconsistent session data**: AI agents might execute JavaScript differently across sessions or page types. This execution difference creates fragmented user journeys in Customer Journey Analytics for client-side implementations.
- **Detection challenges**: With partial tracking, detection becomes unreliable as certain touchpoints might be invisible to analytics.

## Detection signatures

As of August 2025, the following specific signals can be identified for each of the detection methods.

### User agent identification

Crawler
User Agent String
Purpose/Behavior
GPTBot
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.1; +https://openai.com/gptbot
OpenAI's primary web crawler for training ChatGPT and language models
ChatGPT-User
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot
Used when ChatGPT browses websites on behalf of users (legacy)
ChatGPT-User v2
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/2.0; +https://openai.com/bot
ChatGPT's updated version for on-demand fetching and in-response lookups
OAI-SearchBot
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot
ChatGPT's search-focused crawler for discovering content
ClaudeBot
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ClaudeBot/1.0; +claudebot@anthropic.com
Anthropic's crawler for training and updating the Claude AI assistant
Claude-User
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com)
Supports Claude AI users when individuals ask questions to Claude, it may access websites using a Cl...
Claude-SearchBot
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-SearchBot/1.0; +Claude-SearchBot@anthropic.com)
Navigates the web to improve search result quality for Claude AI users by analyzing online content t...
PerplexityBot
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)
Perplexity.ai's crawler for real-time web data indexing
Perplexity-User
Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://www.perplexity.ai/useragent)
Loads pages when users click Perplexity citations (bypasses robots.txt)
Google-Extended
Mozilla/5.0 (compatible; Google-Extended/1.0; +http://www.google.com/bot.html)
Google's AI-focused crawler for Gemini separate from standard Googlebot
BingBot
Mozilla/5.0 (compatible; BingBot/1.0; +http://www.bing.com/bot.html)
Microsoft's crawler powering Bing Search and Bing Chat (Copilot)
DuckAssistBot
Mozilla/5.0 (compatible; DuckAssistBot/1.0; +http://www.duckduckgo.com/bot.html)
Scrapes content for DuckAssist, DuckDuckGo's private AI answer feature
YouBot
Mozilla/5.0 (compatible; YouBot (+http://www.you.com))
Crawler behind You.com's AI search and browser assistant
meta-externalagent
Mozilla/5.0 (compatible; meta-externalagent/1.1 (+https://developers.facebook.com/docs/sharing/webmasters/crawler))
Meta's bot for collecting data to train or fine-tune LLMs
Amazonbot
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot)
Amazon's crawler for search and AI applications
Applebot
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)
Apple's crawler for Spotlight, Siri, and Safari
Applebot-Extended
Mozilla/5.0 (compatible; Applebot-Extended/1.0; +http://www.apple.com/bot.html)
Apple's AI-focused crawler for future AI models (opt-in)
Bytespider
Mozilla/5.0 (compatible; Bytespider/1.0; +http://www.bytedance.com/bot.html)
ByteDance's AI data collector for TikTok and other services
MistralAI-User
Mozilla/5.0 (compatible; MistralAI-User/1.0; +https://mistral.ai/bot)
Mistral's real-time citation fetcher for "Le Chat" assistant
cohere-ai
Mozilla/5.0 (compatible; cohere-ai/1.0; +http://www.cohere.ai/bot.html)
Collects textual data for Cohere's language models
### Referrer classification

Source
Referrer
Traffic Type
ChatGPT
chatgpt.com
Direct traffic from ChatGPT interface
Claude
claude.ai
Traffic from Anthropic's Claude interface
Google Gemini
gemini.google.com
Traffic from Google's AI assistant
Microsoft Copilot
copilot.microsoft.com
Traffic from Microsoft's AI assistant
Microsoft Copilot
m365.cloud.microsoft
Traffic from Microsoft's AI assistant (Microsoft 365 cloud services)
Perplexity AI
perplexity.ai
Traffic from AI search with citations
Meta AI
meta.ai
Traffic from Meta's AI assistant
### Query parameter detection

LLM Service
Example URL
Query Parameter
Example Value
ChatGPT
https://www.yoursite.com/product?utm_source=chatgpt.com
utm_source
chatgpt.com
Perplexity
https://www.yoursite.com/article?utm_source=perplexity
utm_source
perplexity
## Implementation

You can report on LLM and AI-generated traffic within a typical Customer Journey Analytics setup ([connection](/en/docs/analytics-platform/using/cja-connections/overview), [data views](/en/docs/analytics-platform/using/cja-dataviews/data-views), and [workspace projects](/en/docs/analytics-platform/using/cja-workspace/home)) through the specific setup and configuration of [derived fields](#derived-fields), [segments](#segments), and [workspace projects](#workspace-project).

### Derived fields

To configure detection methods and detection signals use derived fields as the foundation. For example, define derived fields for [user agent identification](#user-agent-identification), [query parameter detection](#query-parameter-detection), and [referrer classification](#referrer-classification).

#### LLM/AI user agent identification

Use the [Case When](/en/docs/analytics-platform/using/cja-dataviews/derived-fields#case-when) derived field functions to define a derived field that identifies LLM/AI user agents.

{modal="regular"}

#### LLM/AI query parameter detection

Use the [URL Parse](/en/docs/analytics-platform/using/cja-dataviews/derived-fields#url-parse) and [Classify](/en/docs/analytics-platform/using/cja-dataviews/derived-fields#classify) derived field functions to define a derived field that detects query parameters.

{modal="regular"}

#### LLM/AI referrer classification

Use the [URL Parse](/en/docs/analytics-platform/using/cja-dataviews/derived-fields#url-parse) and [Classify](/en/docs/analytics-platform/using/cja-dataviews/derived-fields#classify) derived field functions to define a derived field that classifies referrers.

{modal="regular"}

### Segments

Set up dedicated segments that help you to identify events, sessions or people related to LLM and AI-generated traffic. For example, use the derived fields that you created earlier to define a segment that identifies LLM and AI-generated traffic.

{modal="regular"}

### Workspace project

Use the derived fields and segments to report and analyze on LLM and AI-generated traffic. For example, see the annotated project below.

{modal="regular"}

Related Articles
This use case article is based on the blog article
Tracking and Analyzing LLM and AI-Generated Traffic in Adobe Customer Journey Analytics
.
recommendation-more-help
