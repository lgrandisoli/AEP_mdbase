---
title: "Work with MCP clients ajo-mcp"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/combine/ajo-mcp"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:36.925029+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

[Beta]{class="badge informative"}

# Work with MCP clients ajo-mcp

Last update: May 8, 2026
- Topics:
- [Integrations](#)

CREATED FOR:

- Beginner
- Intermediate
- User
- Developer

The Adobe Journey Optimizer MCP integration lets you query campaigns and offers using plain-language prompts — without writing API calls or navigating product screens. This page explains how the integration works, what you can do with it, and how to get started.

AVAILABILITY
The Adobe Journey Optimizer MCP server is currently available in
Claude Web
and
Claude Desktop
only. Support for additional MCP-compatible applications will be added in future releases.
## Beta, security, and legal notices mcp-notices

**Beta documentation notice:** This documentation covers a Beta feature and does not constitute final documentation. The content described herein relates to a Beta release and is subject to change prior to general availability. Adobe makes no representations about the completeness or accuracy of this documentation.

By using the Adobe Journey Optimizer MCP Server (Beta) (“Beta”), You hereby acknowledge that the Beta is provided **“as is” without warranty of any kind**. Adobe shall have no obligation to maintain, correct, update, change, modify or otherwise support the Beta. You are advised to use caution and not to rely in any way on the correct functioning or performance of such Beta and/or accompanying materials. The Beta is considered Confidential Information of Adobe. Any “Feedback” (information regarding the Beta including but not limited to problems or defects you encounter while using the Beta, suggestions, improvements, and recommendations) provided by You to Adobe is hereby assigned to Adobe including all rights, title, and interest in and to such Feedback.

WARNING
The Model Context Protocol (MCP) is an emerging open-source standard and may present security or reliability risks. Adobe MCP server integrations and related documentation are provided “as is,” without warranties of any kind.
Connecting MCP clients or servers to Adobe products is a customer-elected configuration. Customers are responsible for evaluating the security and suitability of any MCP integration. Adobe is not responsible for issues arising from misconfiguration, misuse of the MCP, vulnerabilities in third-party implementations, or unintended actions performed through MCP-enabled workflows.
To reduce risk, Adobe encourages testing integrations in a sandbox environment prior to productive use, and carefully reviewing and validating all MCP-initiated actions and responses before confirming or relying on them.
## What is the model context protocol? mcp-overview

Marketing and customer-experience teams increasingly rely on chat-based applications and developer tools — such as Anthropic Claude, OpenAI ChatGPT, Cursor, and Microsoft Copilot Studio — to streamline their day-to-day work. These applications support the **Model Context Protocol (MCP)**, an open standard that lets applications expose back-end tools to large language models (LLMs) in a uniform way.

Adobe Journey Optimizer now provides an MCP server that surfaces campaign and sandbox operations directly inside any MCP-compatible application. With the Adobe Journey Optimizer MCP integration, different personas can collaborate around the same orchestration data — without writing queries against the Adobe Journey Optimizer REST API or navigating multiple UI screens. Customers can describe their intent conversationally and let the LLM invoke the appropriate MCP tools.

## Key capabilities mcp-capabilities

The Adobe Journey Optimizer MCP server lets you inspect, summarize, and troubleshoot campaigns and offers directly from your AI assistant. All operations are **read-only** — the MCP server surfaces retrieve APIs as plain-language answers so you can:

- **Get instant campaign visibility** — Ask about campaign statuses and channel configurations in plain language and get answers instantly, without navigating menus or pulling reports manually.
- **Spot problems early** — Surface stopped campaigns, orphaned drafts, and channel configuration issues the moment you ask, so your team can act fast.
- **Collaborate around live data** — Marketers, campaign managers, and stakeholders can all query the same live Adobe Journey Optimizer data through their AI assistant, making it easier to align, decide, and move together.
- **Audit your orchestration portfolio** — Review the full status of campaigns without parsing JSON or jumping across product screens.

## Available tools mcp-tools

The following tools are exposed by the Adobe Journey Optimizer MCP server:

Tool
Description
List Campaigns
Browse your Adobe Journey Optimizer marketing campaigns. Supports filtering by status (DRAFT, LIVE, STOPPED, COMPLETED).
Get Campaign
Fetch full details and configuration for a specific campaign by ID, including audience targeting, schedule, channel, and content settings.
List Channel Configurations
View surface presets and branding settings for email, SMS, push, or WhatsApp channels.
NOTE
All tools are read-only. Write operations (creating, updating, or deleting objects) are not supported in the current Beta release.
## Use cases mcp-use-cases

The following examples show how to interact with the Adobe Journey Optimizer MCP server using natural language:

Goal
Example prompt
Campaign overview
Show me all my Journey Optimizer campaigns / How many campaigns are set up in Journey Optimizer?
Status audit
Which campaigns are currently live? / List any paused or stopped campaigns.
Campaign details
Get the full details of campaign [ID] / Walk me through everything set up in campaign [ID].
Audience & targeting
What audience is targeted in campaign [ID]? / What eligibility rules are set on campaign [ID]?
Schedule & timing
When is campaign [ID] scheduled to run? / Is campaign [ID] a one-time send or recurring?
Troubleshooting
Why might campaign [ID] not be sending? / Review the setup of campaign [ID] for any issues.
Channel configuration
What channel presets are available in my sandbox? / Show me all my email channel configurations.
Channel audit
Which channel configurations are missing or incomplete? / How many channel configurations do I have across all channels?
## Prerequisites mcp-prerequisites

Before connecting the Adobe Journey Optimizer MCP server to your MCP client, ensure the following:

- You have an active Adobe Journey Optimizer license.
- You have access to a supported MCP-compatible application (currently Claude Web or Claude Desktop).
- You have the necessary permissions in Adobe Journey Optimizer to view campaigns and offers.

## Connect the Adobe Journey Optimizer MCP server mcp-connect

NOTE
This integration is in Beta. Detailed setup steps will be published when it reaches general availability. Contact your Adobe representative to request early access and receive configuration instructions.
During the Beta phase, your Adobe representative will provide:

- The MCP server endpoint URL specific to your organization.
- Authentication credentials for connecting your AI assistant to Adobe Journey Optimizer.
- Guidance on configuring the MCP server in Claude Desktop or Claude Web.

## Known limitations mcp-limitations

The following limitations apply to the current Beta release of the Adobe Journey Optimizer MCP server:

Limitation
Description
Workaround
No engagement or performance metrics
The MCP server exposes no reporting data. Tools do not return impressions, click-through rates, conversions, or delivery stats.
Use Journey Optimizer Reporting UI, CJA MCP, or Adobe Analytics MCP for metrics. AEP Query Service can query raw event data using the campaign execution ID.
Campaign list pagination is limited
List Campaigns
always returns the first page of results (up to 50 campaigns, sorted alphabetically). Offset and limit values are not applied, making full enumeration impractical for large sandboxes.
Use
Get Campaign
directly if the campaign ID or name is known. Use the Journey Optimizer UI for browsing and filtering the full list.
No server-side filtering by date, channel, or schedule
List Campaigns
only supports filtering by status. Filtering by publish date, schedule date, channel, or campaign type is not available server-side.
Use the Journey Optimizer UI campaign list, which supports native date and channel filtering.
Message content retrieval unavailable
The message content tool returns HTTP 502 for all channel types (email, code-based, and others). Message HTML, subject lines, personalization tokens, and offer content cannot be retrieved via MCP.
View message content and personalization tokens directly in the Journey Optimizer UI under
Campaigns > [Campaign] > Content
.
## Frequently asked questions mcp-faq

Which MCP clients are supported?
The Adobe Journey Optimizer MCP server is currently available for
Claude Web
and
Claude Desktop
. Support for additional MCP-compatible applications may be added in future releases.
What Adobe Journey Optimizer objects can I access via MCP?
You can access campaigns, offers and sandbox information. Operations are read-only (retrieve APIs); write operations are not supported in the current release.
Do I need developer access to use the Adobe Journey Optimizer MCP server?
No. The MCP server is designed for both marketing and technical personas. Marketers can interact with it using natural language prompts in any supported MCP client, while developers can also use it in developer tools that support MCP.
Is my data sent to the MCP client provider?
When you submit a prompt, the MCP client may send relevant context (including Adobe Journey Optimizer data returned by the MCP server) to its model for processing. Review the privacy and data-handling policies of your MCP client provider before connecting to production data.
What permissions do I need in Adobe Journey Optimizer?
You need at minimum
View
permissions for the objects you want to query — campaigns or offers. No write permissions are required because the MCP server only performs read operations. Contact your Adobe Journey Optimizer administrator if you are unsure about your current access level.
Can I use the MCP server in sandbox environments?
Yes. The MCP server respects your Adobe Journey Optimizer sandbox configuration. You can query sandbox-specific data by specifying the sandbox in your prompt or by connecting with credentials scoped to a particular sandbox.
recommendation-more-help
