
---
# FILE: adobe-experience-platform-agent-orchestrator-a589b105.md
---

---
title: "Adobe Experience Platform Agent Orchestrator"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-orchestrator"
created_at: "2026-09-01T13:43:20.732294+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Adobe Experience Platform Agent Orchestrator

Last update: July 21, 2026
CREATED FOR:

- User
- Admin
- Leader
- Developer

Adobe Experience Platform Agent Orchestrator is the new agentic layer in Adobe Experience Platform. Designed to leverage Experience Platform’s rich data and customer knowledge, Experience Platform Agent Orchestrator powers the intelligence and reasoning behind purpose-built expert Adobe Experience Platform Agents, enabling them to execute complex decision-making and problem-solving tasks at speed and scale — all with human oversight. When you ask questions or request help via natural language in a conversational interface like AI Assistant, Agent Orchestrator automatically calls upon specialized agents to get you the right answers. Agent Orchestrator remembers your conversation history, enabling you to build on previous questions naturally without repeating context, and combines insights from multiple agents to present you with clear, unified responses.

You can complete complex end-to-end workflows through an intuitive conversational interface without needing to know which agents are working behind the scenes. The system understands your goals, creates step-by-step plans, and adjusts its approach as needed based on your feedback. Within your conversation in AI Assistant, you can explore the Agent Orchestrator reasoning panel to see the step-by-step thinking process and better understand how your requests are being handled.

agent-orchestrator-overview
Read this document to learn about Agent Orchestrator.

## Components of Agent Orchestrator components

Agent Orchestrator is made up of several key components, including the AI Assistant conversational interface, a reasoning engine for decision-making and planning, specialized Adobe Experience Platform agents, and a knowledge base that provides access to relevant information.

### AI Assistant conversational interface ai-assistant

AI Assistant is an intelligent, natural language conversational experience that lets practitioners using enabled CX Enterprise applications to leverage GenAI and Agentic AI capabilities, the breadth of which depends on the CX Enterprise applications licensed by customers. To unlock access, read [the guide on accessing AI Assistant](/en/docs/experience-platform/ai-assistant/access).

For more information, read the [AI Assistant UI guide](/en/docs/cx-enterprise-ai/experience-cloud-ai/ai-assistant/ai-assistant-ui).

### Reasoning engine reasoning-engine

Reasoning engine interprets your goals based on your natural language prompts, checks any limits or requirements, and creates step-by-step plans to help you reach your objectives. Unlike simple question-and-answer systems, it can adjust its plans as things change, and can go back and try different approaches if needed. The plans it creates are shown to you in the AI Assistant conversational interface, so you can see and follow the process, as well as intervene if needed.

### Adobe Experience Platform Agents agents

Adobe Experience Platform Agents are purpose-built grouping of AI agents skilled in delivering common jobs across customer experience domains. Below is the list of Adobe Experience Platform Agents that are currently available in CX Enterprise applications:

Agent
Details
Supported applications
Audience Agent
Audience Agent lets you view insights about audiences, including detecting significant audience size changes, detecting duplicate audiences, explore your audience inventory, and retrieve your audiences’ size.
- Real-Time CDP
- Adobe Journey Optimizer

Data Insights Agent
Data Insights Agent, accessible from the AI Assistant in Customer Journey Analytics, is a generative AI conversation agent that quickly and efficiently answers questions about your data. It builds relevant visualizations in Analysis Workspace using components from your data view and using your actual data.
Customer Journey Analytics
Experimentation Agent
Experimentation Agent helps teams learn faster by analyzing experiment results, predicting impact, and proposing new experiments. It centralizes past and active experiments so you can build on what you’ve already learned, spot gaps, and prioritize what to test next.
Adobe Journey Optimizer Experimentation Accelerator
Journey Agent
Journey Agent allows Adobe Journey Optimizer users to create, analyze, and optimize journeys using a natural language interface. With Journey Agent, you can quickly build journeys, detect and resolve schedule or audience conflicts, analyze performance and drop-off points, and identify top-performing journeys to replicate for future campaigns. It helps you make data-driven decisions, improve customer engagement, and streamline journey orchestration.
Adobe Journey Optimizer
Product Support Agent
Product Support Agent is a self-serve debugging and troubleshooting capability that helps you troubleshoot Adobe Experience Platform features and applications without leaving your workflows. Support administrators can create customer support tickets with context from your AI Assistant interactions and you can check ticket updates through AI Assistant.
- Adobe Experience Platform
- Real-Time CDP
- Adobe Journey Optimizer
- Adobe Journey Optimizer B2B Edition
- Customer Journey Analytics
- Adobe Experience Manager

For further information around availability of Agents in CX Enterprise applications, please review the [Agentic AI in CX Enterprise documentation](/en/docs/cx-enterprise-ai/experience-cloud-ai/overview/agentic-ai).

### Knowledge base knowledge-base

The knowledge base provides agents with secure access to customer business intelligence through structured and unstructured data sources, including Adobe product documentation, customer metadata about business objects, and analytics data.

## Ecosystem ecosystem

The Agent Orchestrator ecosystem includes the following agents:

Agent
Details
Adobe Marketing Agent for Microsoft 365 Copilot
Use the Adobe Marketing Agent for Microsoft 365 Copilot to retrieve marketing insights from Experience Platform in Microsoft 365 apps like Teams, Word, Powerpoint, and Excel. With this agent, you can:

- Make faster, data-driven marketing decisions.
- Reduce time spent switching between tools.
- Simplify access to audience and journey insights across teams.

## Access access

All users get access to AI Assistant and associated Experience Platform agents.

- Adobe Experience Manager : Your administrator must grant you the permission to access AI Assistant through the Adobe Admin Console .
- Customer Journey Analytics : Your administrator must grant you the permission to access AI Assistant through Customer Journey Analytics Access Control . This allows you to ask product knowledge and data insights questions.

NOTE
Operational insights questions are not available for Customer Journey Analytics; therefore, no additional permissions apply.
recommendation-more-help


---
# FILE: adobe-marketing-agent-for-microsoft-365-copilot-28add5c2.md
---

---
title: "Adobe Marketing Agent for Microsoft 365 Copilot"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ama-ms"
created_at: "2026-09-01T13:43:27.639616+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Adobe Marketing Agent for Microsoft 365 Copilot

Last update: July 21, 2026
CREATED FOR:

- Admin
- User
- Developer
- Leader

The Adobe Marketing Agent for Microsoft 365 Copilot is an AI-powered tool that connects Adobe Experience Platform directly to Microsoft 365 Copilot. With this agent, you can ask natural-language questions within Microsoft 365 applications such as Teams, Word, Powerpoint, and Excel to instantly retrieve marketing insights from Experience Platform without interrupting your workflow. The same agent is available across these apps, and your chat history with the Adobe Marketing Agent carries over—so you can start research in Copilot in Teams, for example, and continue the conversation in Word or Powerpoint while you draft a campaign brief or review a presentation.

With the Adobe Marketing Agent for Microsoft 365 Copilot, marketing managers, analytics and insights teams, and business stakeholders can:

- Make faster, data-driven marketing decisions.
- Reduce time spent switching between tools.
- Simplify access to audience and journey insights across teams.

## How the agent works

IMPORTANT
The Adobe Marketing Agent for Microsoft 365 Copilot currently supports Experience Platform Operational Insights, Customer Journey Analytics Data Insights, Audience Agent, and the Journey Agent.
The Adobe Marketing Agent for Microsoft 365 Copilot provides an integrated experience between Experience Platform and Microsoft 365 applications:

- Adobe Marketing Agent appears as an agent in Microsoft 365 Copilot, including in Teams, Word, Powerpoint, and Excel.
- Sign in with your Adobe account and select the data environment (sandbox, data view) that you would like to use.

### Data access and permissions

The answers you receive reflect the **data and access level** tied to your Adobe identity—what you can query and see is the same as what you are entitled to in Experience Platform and its associated solutions. The Adobe Marketing Agent **inherits** those permissions and does **not** require a separate permissions setup for the Microsoft 365 integration. For underlying Experience Platform AI Assistant capabilities and other Adobe AI agents, **permission requirements are unchanged** from using those features in Experience Platform.

The agent connects your Microsoft 365 instance to Experience Platform and its associated applications (Real-Time CDP, Adobe Journey Optimizer, and Customer Journey Analytics). With this integration, you can then use the Experience Platform AI Assistant and agents to retrieve relevant insights directly to your Microsoft 365 instance. The answers returned in your Microsoft 365 instance are presented as conversational and natural language texts, tables, and data visualizations. Additionally, support for follow-up questions and investigations is available within the same Copilot chat.

## Key use cases and example scenarios

Use case
Description
Retrieve operational insights for audiences and customer journeys
With the Adobe Marketing Agent, you can easily retrieve operational insights across your audiences and customer journeys. You can identify which audiences are the largest or most engaged, so you can prioritize where to focus your efforts. You can see which customer journeys are currently active and learn how they are performing, helping you pinpoint opportunities for optimization. The agent also lets you track how your different segments are growing or shrinking over time, empowering you to respond to changes in your audience dynamics as they happen.
Use data visualization to better analyze customer journeys and campaigns
You can review journey performance and drop‑offs, compare campaign performance over time, and understand which touchpoints drive conversions. Additionally, you can generate visual reports on campaign performance and compare these across channels, regions, or over different time periods. You can also explore trends without needing to manually build queries or dashboards.
Empower collaboration and decision-making
Use suggested prompts to explore audiences, campaigns, and web traffic. Take advantage of a natural‑language interface for easier learning of Experience Platform and Customer Journey Analytics concepts. Furthermore, you can share insights on Teams channels or chats during planning meetings. You can also use the Adobe Marketing Agent to answer ad-hoc questions in real-time while reviewing plans or decks, allowing you to keep stakeholders aligned on the same set of metrics and definitions.
## Prerequisites

Before you can use the Adobe Marketing Agent for Microsoft 365 Copilot, you must first ensure that you have the following:

- Microsoft 365 with Microsoft Teams or Microsoft Copilot Chat.
- Experience Platform and at least one of: Real-Time CDP, Adobe Journey Optimizer, and/or Customer Journey Analytics.
- Entitlement to the Experience Platform Agent Orchestrator and agents.
- Access to your organization’s Adobe CX Enterprise account (sign-in and product entitlements) for the solutions and data you use. If you do not have Adobe access, contact your Adobe administrator.

## Enable the agent for your organization enable-the-agent-for-your-organization

End users can use the Adobe Marketing Agent only after it is made available in your Microsoft 365 tenant. **Work with your Microsoft 365 Copilot administrator** (or equivalent admin for Copilot agents in your organization) to enable access and assign the agent as your organization requires.

Typical outcomes after admin setup include:

- You can open **Agent Store** in Teams, find **Adobe Marketing Agent** in your list of agents, and choose **Add** to attach it to your Copilot agents.
- Alternatively, your Copilot administrator can **publish** the agent to everyone in your organization or to specific groups so users do not need to add it individually.

For administrator steps and policy options in the Microsoft 365 admin center, see [Manage agents for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/manage) in the Microsoft documentation.

## Get started

After your organization has enabled the agent (see [Enable the agent for your organization](#enable-the-agent-for-your-organization)), navigate to Microsoft 365 Copilot in the application of your choice and use the left-navigation to select **All Agents**.

Locate the card for Adobe Marketing Agent or use the search bar to manually look for the agent. Once you have the agent, select the card.

Use the pop-up window to learn more about the agent. When you are ready, select **Add**.

The Microsoft 365 Copilot dashboard updates with the Adobe Marketing Agent branding now on the main page.

### Sign in and set your context

Next, prompt the agent to sign in and follow the ensuing steps required to authenticate your account. During this step, you will need to copy a numerical code that the agent returns and then sign in to your Adobe organization. If you cannot complete sign-in or you lack access to Adobe solutions for your organization, contact your **Adobe administrator**.

When successful, use the context setter to establish the documentation source, sandbox, and data view that you will use for your queries.

### Use the agent to retrieve operational insights

Once you are signed in, you can use the prompts provided in the main page to get started. You can also take advantage of a starter prompt that can branch out to analyzing marketing audiences, reviewing campaign performance, and monitoring campaign journeys. For example, select **Review campaign performance** and then select **Analyze engagement - Show web visitors for top 10 products last week**.

Allow for a few moments for the agent to calculate and then the agent responds with a visualized representation of your data. You can use the bar chart presented or you can select **View data** to view the data in tables.

You can further investigate by selecting follow-up questions that the agent recommends. Alternatively, you can pivot and try different starter prompts, verify the information sources that the agent referenced, or provide feedback using the feedback mechanism.

For more information on the AI Assistant UI features, read the guide on [using the AI Assistant](/en/docs/cx-enterprise-ai/experience-cloud-ai/ai-assistant/ai-assistant-ui).

## Security, Privacy, and Responsible AI

**Data handling and governance**

The Adobe Marketing Agent relies on the same controls and governance that apply to Experience Platform and Microsoft 365. Your organization retains ownership and control of its data. Insights returned through the agent are scoped to each user’s Adobe permissions and data entitlements; no additional permission model is introduced for the Microsoft 365 surface beyond what already applies in Experience Platform and related Adobe AI agents.

**Responsible AI use**

The agent is intended to return read‑only insights and does not modify your customer data in Experience Platform. You should review any generated summaries and analyses before you use them to make business decisions.

**Supported languages and scope**

The initial release is available as an English‑language experience. Capabilities are limited to read‑only insights; the agent does not create or update marketing assets or configurations.

IMPORTANT
The Adobe Marketing Agent invokes different Adobe agents and jobs depending on the submitted prompts. This underlying Adobe agent that gets invoked utilizes AI credits as indicated in the
Adobe Experience Platform agent jobs and AI credits consumption
page.
## Appendix

Read the following for additional information on the Adobe Marketing Agent for Microsoft 365 Copilot.

### Adobe Marketing Agent Microsoft 365 Copilot admin steps

To set up agents from an external provider (third-party developers or the Microsoft Commercial Marketplace), you must first ensure your tenant settings allow external apps and then manage them through the Integrated Apps or Agents section of the admin center.

#### Enable external agents in tenant settings

Before you can deploy external agents, your organization’s policy must allow them.

- Log in to the [Microsoft 365 admin center](https://admin.microsoft.com/).
- Go to **Agents** > **Settings** > **User access**.
- Under **Allowed agent types,** ensure **Allow apps and agents built by external publishers** is selected.

IMPORTANT
If this setting is disabled, external agents will not appear in the
Agent Store
for your users.
#### Acquire and approve the agent

Typically, you can find external agents in the [Microsoft Commercial Marketplace](https://appsource.microsoft.com/).

- **From the Marketplace**: Find the agent you want and select **Get it now**. This will often redirect you back to your admin center’s **Integrated Apps** page.
- **Review Permissions**: In the [Integrated Apps](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide) list, select the external agent.
- Review the **Data & tools** and **Security & compliance** tabs to see what data the external provider will access.
- Select **Approve** or **Activate** to move it into your organization’s inventory.

#### Deploy to certain users

Once approved, you can control exactly who sees the agent in their Copilot sidebar.

- In the [Microsoft 365 admin center](https://admin.microsoft.com/), navigate to **Agents** > **All agents**.
- Select the external agent from the list.
- Select **Deploy** (or **Edit Assignment**).
- Choose **Specific users/groups** and search for the individuals or Entra ID groups who should have it.
- Select **Finish deployment**. This “pushes” the agent to those users so it appears automatically in their Copilot interface.

#### Manage updates

External providers frequently update their agents. In order to manage these updates, follow the best practices below:

- Check the [Agent Registry](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide) periodically.
- If an update requires new permissions, the agent may show a status of **Pending Update**.
- You must manually **Approve Updates** before the new version is rolled out to your assigned users.

recommendation-more-help


---
# FILE: ai-assistant-prompt-library-7ea238db.md
---

---
title: "AI Assistant Prompt Library"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/ai-assistant/prompt-library"
created_at: "2026-09-01T13:43:29.485257+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# AI Assistant Prompt Library

Last update: July 13, 2026
CREATED FOR:

- User
- Admin
- Leader
- Developer

Read this guide for different types of prompts that you can use on AI Assistant.

## Audience Agent

The following sections provide example prompts you can use with the Audience Agent to explore and analyze your audiences. These include ways to investigate audience characteristics, detect duplicate audiences, retrieve audience sizes, and monitor significant changes in audience size over time. Use these prompts to gain deeper insights and maintain the quality of your audience data.

### Conversation audience exploration

- “Show me fields for affluent buyers.”
- “Which audiences have not been activated or used in any campaign in the last 30 days?”
- “List all the audiences that have been mapped to new destinations in the last 3 months.”

### Detect duplicate audiences

- “Do I have any audiences with identical or similar descriptions?”
- “Identify audiences that have the same rules but have different names.”
- “Show me all the audiences that have the same rules but different activation destinations.”

### Retrieve audience size

- “What is the current size of my audience “Gold-star Members in California_f153e1”?”
- “What is my biggest audience?”

### Detect significant changes in audience size

- “Which audiences have increased in size by more than 20% in the last week?”
- “Which audiences have decreased in size by more than 15% in the last month?”
- “What is my fastest growing audience?”

## Data Insights Agent

The following example prompts can be used with the Data Insights Agent to analyze your data, identify trends, and uncover actionable insights.

### Data visualization

- “Show me profits in September.”
- “Trend orders in September.”
- “Show revenue by region in September.”
- “Share of revenue by product category.”
- “Orders by day of week, from January to May.”
- “Show orders by gender, from March to June.”
- “What is the profit across SKUs from February to May.”
- “Revenue by store name in September.”
- “What were my top 10 SKUs by profit in September?”
- “Proportion of purchases by month of year.”
- “Total profit in September.”

## Journey Agent

The following example prompts can be used with the Journey Agent to help you analyze journey lifecycles, manage journey resources, gain insights into audience and journey relationships, and detect conflicts between journeys. Use these prompts to optimize your journey orchestration and resolve issues efficiently.

### Journey Lifecycle Questions

- “When was {JOURNEY_NAME} published?”
- “When was {JOURNEY_NAME} stopped?”
- “List all journeys currently in test mode”

### Journey Resource Questions

- “How many live journeys do I have?”
- “Give me a list of all scheduled recurring journeys and their expected run times.”

### Audience and Journey Insights

- “Which audiences are used in more than X journeys?”
- “List all journeys using the {AUDIENCE_NAME} audience.”

### Conflict Analysis Prompts

Use these prompts to analyze potential conflicts between journeys, including scheduling and audience overlaps:

Select to view list
- “Can you do a comprehensive analysis of conflicts for our journey {JOURNEY_NAME} with conflict type (scheduling/audience) information with live/running journeys?”
- “Please do a scheduling conflict analysis for journey {JOURNEY_NAME} with conflict type information.”
- “Please do an audience overlap analysis for journey {JOURNEY_NAME} with conflict type information.”
- “Are there any scheduling conflicts for journey {JOURNEY_NAME}?”
- “Show me audience overlap conflicts for journey {JOURNEY_NAME}.”
- “Analyze all conflicts for journey {JOURNEY_NAME} with other live journeys.”
- “What are the current conflicts for journey {JOURNEY_NAME}?”
- “Check if journey {JOURNEY_NAME} has audience conflicts with other journeys.”
- “Check for scheduling conflicts involving journey {JOURNEY_NAME}.”
- “I want to know about all journey conflicts for {JOURNEY_NAME}.”
- “Do any live journeys conflict with {JOURNEY_NAME} by schedule or audience?”
- “Identify conflict types for journey {JOURNEY_NAME} compared to running journeys.”
- “Show overlapping audiences for journey {JOURNEY_NAME} and other journeys.”
- “Highlight scheduling overlaps between journey {JOURNEY_NAME} and live journeys.”
- “Is journey {JOURNEY_NAME} running in conflict with any other journey?”
- “Please detect and list conflicts for {JOURNEY_NAME}.”
- “Report all types of conflicts for journey {JOURNEY_NAME}.”
- “Give me a conflict breakdown (scheduling and audience) for {JOURNEY_NAME}.”
- “Does {JOURNEY_NAME} have any conflicts that may impact performance?”
- “Are there any active conflicts affecting {JOURNEY_NAME}?”
- “List journeys in conflict with {JOURNEY_NAME} by schedule or audience.”
- “Has journey {JOURNEY_NAME} triggered any conflict alerts?”
- “Find potential audience conflicts for journey {JOURNEY_NAME}.”
- “Analyze conflict risk for journey {JOURNEY_NAME}.”
- “Provide conflict diagnostics for {JOURNEY_NAME}.”

## Product Support Agent

The Product Support Agent helps you troubleshoot issues, create support cases, and track the status of your support tickets. Use the following example prompts to get assistance.

### Troubleshooting help

- “Why does my profile count differ on the License Usage Dashboard and the Experience Platform home page?”
- “What are the reasons for a journey not triggering?”
- “How does Adobe Experience Platform create real-time experiences?”
- “How do you configure and use alerts in Adobe Experience Platform?”
- “What is the limit for batch segmentation jobs in Adobe Experience Platform Activation?”
- “What is the average profile richness limit in Adobe Experience Platform Activation?”

### Support case creation

- “Create a support ticket.”
- “Can you help me create a support ticket?”

### Track case progress

- “What is the latest on my case E-12345?”
- “What’s the update on ticket E-67890?”

recommendation-more-help


---
# FILE: audience-agent-1970cf91.md
---

---
title: "Audience Agent"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/audience"
created_at: "2026-09-01T13:43:21.590012+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Audience Agent

Last update: July 21, 2026
CREATED FOR:

- User
- Admin
- Leader
- Developer

AVAILABILITY
The Audience Agent is available for all customers who have access to AI Assistant. However, you will need the following permissions in order to fully use the Audience Agent features.
View Segments
: This permission lets you use the Audience Agent to view insights into the audiences directly in AI Assistant.
Manage Segments
: To permission lets you use the Audience Agent to create new audiences directly in AI Assistant.
The Audience Agent lets you view insights about audiences, including detecting significant audience size changes, detecting duplicate audiences, exploring your audience inventory, and retrieving your audiences’ size.

audience-agent-overview
## Supported use cases

The Audience Agent within AI Assistant supports the following use cases:

- Conversationally explore your audience Find audience sizes of existing audiences Look for audiences based on full or partial attributes named Detect duplicate audiences Discover XDM fields you can use to define an audience
- Detect significant changes in audience size This lets you find audiences that have suddenly grown or shrunk, letting you better analyze potential market changes
- Audience creation This skill lets you create an audience based on the given attributes and events Additionally, this skill lets you estimate the potential size of an audience prior to creating the audience, letting you quickly iterate on the most effective audience before it’s ready to activate

The Audience Agent does not **currently** support the following feature:

- Goal-based audience exploration Goal-based audience exploration lets you discover relevant datasets and profiles aligned to a business goal by applying machine learning models such as propensity to buy or convert.

Additionally, when using Audience Agent, you should keep the following constraints in mind:

- Audience Agent needs at least 24 hours to process your data For example, you cannot have a query that looks for data within the last 24 hours. You’ll need to look within the last 48 hours, at a minimum.
- Audience Agent only supports the following audience types: People-based audiences that are evaluated using batch segmentation Account-based audiences for the following use cases: Conversational audience exploration Duplicate audience detection

## Sample prompts

The following examples demonstrate sample prompts and responses for the Audience Agent.

### Conversational audience exploration

Show me fields for affluent buyers.

Response
Which audiences have not been activated or used in any campaign in the last 30 days?

Response
List all the audiences that have been mapped to new destinations in the last 3 months.

Response
Which account audience has the largest audience size and what is that size?

Response
### Detect duplicate audiences

Do I have any audiences with identical or similar descriptions?

Response
Identify audiences that have the same rules but have different names.

Response
Show me all the audiences that have the same rules but different activation destinations.

Response
Identify account audiences that have the same rules but have different names.

Response
### Retrieve audience size

What is the current size of my audience “Gold-star Members in California_f153e1”?

Response
What is my biggest audience?

Response
### Detect significant changes in audience size

Which audiences have increased in size by more than 20% in the last week?

Response
Which audiences have decreased in size by more than 10% in the last month?

Response
What is my fastest growing audience?

Response
### Create an audience

AVAILABILITY
You can only use the create audience skill if you are part of the Agent Orchestrator Explorer program. For more information, contact Adobe Customer Care.
When you create an audience with Audience Agent, AI Assistant will guide you through a plan. For example, you can ask to “Create an audience made up of people who live in California”. AI Assistant then lists the plan that it will undertake to create the audience.

Response
This plan is made up of three steps:

- [Identify audience characteristics](#identify)
- [Estimate audience size](#estimate)
- [Create and persist a new audience](#create)

#### Identify audience characteristics identify

{align="center" width="80%"}

After accepting the plan, AI Assistant will grab the audience’s characteristics based off of your initial query.

Response
For this query, AI Assistant generates the relevant Profile Query Language (PQL) that would look for people who live in California. In this use case, the PQL query would look like the following:

| code language-sql |
| --- |
| homeAddress.state.equals("California", false) |

For more information on PQL, read the [PQL overview](/en/docs/experience-platform/segmentation/pql/overview).

If the AI Assistant’s audience definition is correct, you can approve and move on to the next step.

#### Estimate audience size estimate

{align="center" width="80%"}

After approving the identified audience characteristics, AI Assistant will estimate the size of the potential audience and the audience definition details.

Response
If the estimated size looks correct, you can approve and move on to the next step.

#### Create and persist new audience create

{align="center" width="80%"}

Finally, if the characteristics and the audience size look correct, you can approve or reject the audience’s creation.

Response
First, you can review the proposed audience through the provided data grid.

If the audience looks correct, you can accept the proposal by selecting **Create** to finish creating the audience.

The audience is now created.

{align="center" width="80%"}

## Next steps

After reading this guide, you should have a better understanding of Audience Agent and what features it supports. For more information on agents in Adobe Experience Platform, read the [Agent Orchestrator overview](/en/docs/cx-enterprise-ai/experience-cloud-ai/agents/agent-orchestrator).

recommendation-more-help


---
# FILE: experimentation-agent-9ecc71c8.md
---

---
title: "Experimentation Agent"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/agent-experiment"
created_at: "2026-09-01T13:43:23.710006+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Experimentation Agent

Last update: July 21, 2026
CREATED FOR:

- User
- Admin
- Leader
- Developer

AVAILABILITY
The Experimentation Agent is available to all customers who have purchased the paid license of Journey Optimizer Experimentation Accelerator and integrates seamlessly with either Adobe Target or Adobe Journey Optimizer.
Learn more on Journey Optimizer Experimentation Accelerator
## Overview

The **Experimentation Agent** is an AI-powered tool that modernizes how you can run and manage digital experiments across websites, emails, push messages, and applications. Built on Adobe Experience Platform AI platform and experimentation tools, the **Experimentation Agent** helps you run experiments more efficiently, organize business goals, and generate actionable insights, highlighting what worked, what did not, and where to experiment next.

The following permissions in order to fully use the Experimentation Agent features.

- View Experiments : This permission lets you use the Experimentation Agent to view insights into the experiment directly in AI Assistant.
- Manage Experiment Metada : This permission lets you use the Experimentation Agent to create new experiments directly in AI Assistant.

➡️ [Learn more in Journey Optimizer Experimentation Accelerator documentation](/en/docs/experimentation-accelerator/using/get-started/experiment-accelerator-access)

As part of Experimentation Accelerator feature, the Agent delivers:

- Performance : a clear view of what happened in the experiment
- Insights : an explanation of why the results occurred
- Opportunities : guidance on the next actions to take

## Use Cases

The Experimentation Agent enhances each phase of the experimentation workflow by analyzing results, interpreting content, and suggesting next steps.

Its capabilities can be grouped into five key functions:

- Experiment Summarization Provide a clear, non-technical overview of experiment results for stakeholders.
- Content Analysis Examine the messaging or creative elements of treatments to understand why certain ones outperformed others.
- Attribute Identification Categorize treatments by their key attributes, e.g., themes, tones, formats, and connect those attributes to conversion outcomes.
- Recommendation Generation Suggest new treatments or adjustments to test, based on insights from prior experiments.
- Opportunities Identify broader areas or new angles for experimentation to uncover untapped potential.

## In Scope and Out of Scope Features

### In Scope

The following capabilities are currently supported:

- Performance
- Insights
- Opportunities

### Out of Scope

The following functionalities are currently not supported:

- Creating or editing experiments
- Using multiple metrics for reporting use cases

## Sample Prompts

Here is a list of prompt samples to help you get started with the Experimentation Agent:

### General questions

Prompts
What experiments are running?
Which experiments are running for the
<campaign name>
?
What experiments started in the last month?
How many experiments ended in the past year?
Which experiments are currently paused/stopped/etc?
What common patterns are emerging from recent tests?
What is the average duration of experiments in the last quarter?
### Performance questions

Prompts
For my
<experiment name>
, what treatment is leading?
What is the lift of the
<experiment name>
?
Which experiments had statistically significant results?
Which experiments had the best conversion rate?
### Insights questions

Prompts
What is
<experiment name>
testing? ?
What did we learn from the
<experiment name>
?
Can you tell me why treatment A won?
What themes are trending in winning variants?
What common patterns are emerging from recent tests?
Did anything unexpected happen in
<experiment name>
?
### Opportunities questions

Prompts
What do you recommend I do next after this experiment?
Is the any way to improve
<experiment name>
?
What opportunities became clearer after
<experiment name>
?
What could I test next to prove the hypothesis from
<experiment name>
?
What additional use cases should I implement?
recommendation-more-help


---
# FILE: field-discovery-agent-af866654.md
---

---
title: "Field Discovery Agent"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/field-discovery-agent"
created_at: "2026-09-01T13:43:24.867649+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Field Discovery Agent

Last update: July 21, 2026
CREATED FOR:

- User
- Admin
- Developer

When building audiences or onboarding data in Adobe Experience Platform, identifying the correct XDM field for a business concept often requires manually browsing schemas or knowing in advance exactly how a field is named. Different fields may represent the same concept under different names—for example, state, region, and location—and choosing the wrong one introduces errors in downstream workflows.

Field Discovery Agent is an AI-powered agent in Adobe Experience Platform that helps you find, evaluate, and select XDM fields using natural language queries in AI Assistant. You describe what you are looking for in plain language — a business concept, a workflow goal, or a specific field name — and the agent returns ranked field suggestions with supporting context.

Field Discovery Agent is invoked automatically in the background within AI Assistant when other Experience Platform agents need to resolve field or entity references. In those cases, it operates in the background to improve the accuracy of the agent you are working with. When you need field discovery for your own work, write an explicit field-finding prompt in AI Assistant. Field Discovery Agent surfaces field information only. It does not modify schemas, datasets, or audiences, and it respects your existing access controls and sandbox context.

## When to use this when-to-use-this

Use Field Discovery Agent explicitly in AI Assistant when you need ranked field suggestions, sample values, and usage context for a mapping, segmentation, or query. It is used implicitly when another Experience Platform agent invokes it in the background to resolve field or entity references. In those cases, you remain in that agent’s workflow and do not issue a separate field-finding prompt.

## Prerequisites prerequisites

To use Field Discovery Agent, ensure you have the following:

- Access to Adobe Experience Platform and AI Assistant
- The correct organization and sandbox
- Access to the schemas and datasets you intend to query

Basic familiarity with XDM schemas and how fields are used in segmentation or data workflows can help you interpret results more effectively. For more information, see the [XDM overview](/en/docs/experience-platform/xdm/home) and [Schema Editor documentation](/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

For instructions on enabling AI Assistant access and granting the required permissions, see the [Agent Orchestrator access guide](/en/docs/cx-enterprise-ai/experience-cloud-ai/agents/agent-orchestrator#access).

## Field Discovery Agent functions field-discovery-agent-functions

Field Discovery Agent processes your query and returns one of three types of output depending on your intent. These functions reflect how the agent interprets your query; you do not select them. The agent determines the appropriate response type automatically based on what you describe.

Function
Description
Expected output
Identification
Identifies XDM fields that semantically match a business concept or attribute you describe in natural language.
A ranked list of candidate fields with relevance labels, field paths, and Usage Contexts links.
Recommendation
Recommends XDM fields based on a workflow goal or use case you describe, such as building an audience segment or modeling a behavioral attribute.
A prioritized list of fields relevant to the stated goal, with relevance context for each.
Enrichment
Returns detailed context for a specific field, including sample values, schema location, and where the field is used across datasets, audiences, and destinations.
Field details including sample values, schema path, associated datasets, and audience or destination usage.
## How Field Discovery Agent works how-field-discovery-agent-works

At a high level, the agent interprets your intent, searches your available data, and ranks results by relevance. How you phrase your query directly affects each stage, which in turn impacts the quality of results.

When you submit a query in AI Assistant, Field Discovery Agent processes your request in three stages:

Stage
Description
Intent interpretation
The agent reads your natural language input and identifies the underlying concept or goal. For example, a query about “people in California” is interpreted as a geographic attribute request, not a literal string match. The agent maps your phrasing to semantically equivalent concepts that may appear under different names across your schemas.
Search scope
The agent searches across the XDM schemas, datasets, and field metadata available in your current IMS organization and sandbox. It considers field names, display names, descriptions, and usage associations to find candidates that align with your intent.
Ranking
The agent ranks results by semantic relevance — how closely a field matches your stated intent — supplemented by signals such as metadata completeness and field usage across your data ecosystem. Fields with descriptive names, populated metadata, and confirmed usage in active datasets rank higher than fields that exist only in a schema definition. The agent does not expose the specific weights assigned to individual signals.
## Understand your results understand-your-results

Field Discovery Agent returns a structured result set for each query. Understanding the components of a result helps you evaluate candidate fields and act on them with confidence, without additional trial and error.

Treat a field as ready to use when its **Relevance** label is **Highly Relevant**, its sample values match the data you expect (when available), and its **Usage Contexts** aligns with how you plan to use it. If results are only **Moderately Relevant** or **Relevant**, sample values do not match your expectations, or usage context is limited, refine your query and review a new result set before proceeding.

### Relevance labels

Field Discovery Agent assigns a relevance label in the **Relevance** column of the **Fields Identified** panel for each field result, indicating how closely the field matches your query.

- **Highly Relevant** — The field strongly matches your stated concept based on its name, metadata, and usage signals. Confirm the field path and review its sample values to verify it holds the data you expect.
- **Moderately Relevant** — The field has partial semantic overlap with your query but may differ in scope, data type, or specificity. Review the sample values and usage context to determine whether it meets your needs before selecting it.
- **Relevant** — The field partially matches your query. It may share semantic overlap but differ in scope, specificity, or data type. Review the sample values and usage context before deciding whether to use it.

If all results are labeled **Moderately Relevant** or **Relevant** rather than **Highly Relevant**, your query may be too broad or use terminology that does not match your schema metadata. Refine your prompt with more specific language or domain terms that reflect how your fields are named.

### Sample values

Alongside each field suggestion, Field Discovery Agent surfaces sample values drawn from the field’s data in your sandbox. Sample values help you verify that a field contains the type of data you expect before selecting it.

IMPORTANT
Sample values may contain PII. Do not share them outside secure internal workflows.
Sample values are visible only for fields within your dataset access permissions. For information on data governance and usage restrictions in Experience Platform, see the [Data Governance overview](/en/docs/experience-platform/data-governance/home).

If no sample values appear for a field, the field may be empty in your current sandbox or your permissions may not include access to its underlying dataset. Fields with high cardinality (such as identifier or UUID fields) may also not return representative sample values. Sample values are aggregated and frequency-based and are not traceable to individual profiles.

### Usage context

Each field result includes usage context showing where the field appears across your data ecosystem:

**Audience → Dataset → Destination → Schema**

A field that is used in a published audience, appears in an active dataset, is mapped to a live destination, and is defined in a schema has demonstrated real usage in your environment. This distinguishes fields that are actively relied on from fields that exist only in a schema definition but have not been used in practice. Use this signal alongside relevance label and sample values to make a more informed field selection.

### Results in AI Assistant

Field Discovery Agent returns results in a **Fields Identified** panel within the AI Assistant response. The panel displays a table with three columns:

- **Field Name** — The XDM path of the candidate field.
- **Relevance** — The relevance label assigned to the field (**Highly Relevant**, **Moderately Relevant**, or **Relevant**)
- **Usage Contexts** — Links showing where the field appears across your data ecosystem. Select **audience**, **dataset**, **destination**, or **schema** to open a side panel showing where the field is used.

A **Results Explained** section appears below the **Fields Identified** table and provides additional field-level context, including explanations and supporting detail for each result. For guidance on navigating the AI Assistant interface, see the [AI Assistant UI guide](/en/docs/cx-enterprise-ai/experience-cloud-ai/ai-assistant/ai-assistant-ui).

## Use Field Discovery Agent use-field-discovery-agent

You interact with Field Discovery Agent through AI Assistant using natural language. The agent requires a clear statement of intent—a vague or overly brief query produces lower-quality results or may not invoke Field Discovery Agent at all.

For explicit field discovery, follow this workflow: identify the attribute or mapping problem, submit a field-finding query, review ranked results and usage context in the **Fields Identified** panel, select the **Field Name** path that fits your intent, and apply that XDM path in Segment Builder, Query Service, or another workflow.

To use Field Discovery Agent:

- Navigate to AI Assistant from any enabled Experience Platform application. The AI Assistant workspace displays.
- State your intent explicitly in the input field. Describe the concept, goal, or field characteristic you are looking for. For example: “Find fields related to customer email opt-out status.”
- Review the ranked results in the Fields Identified panel. Each row includes a relevance label and an XDM field path in the Field Name column.
- Select audience , dataset , destination , or schema in the Usage Contexts column to open a side panel showing where the field is used. For additional field-level context, see the Results Explained section below the results table.
- Use the Field Name path in downstream tools such as Segment Builder, Query Service, or data ingestion workflows, depending on your use case. Field Discovery Agent provides the field reference but does not insert it into other tools.

If needed, select the **Reasoning complete** dropdown above the response to confirm that Field Discovery Agent handled your request. The dropdown displays reasoning details that indicate which agent was called.

NOTE
If the reasoning panel does not indicate Field Discovery Agent, your query may not have contained a clear field discovery intent. Restate your query with explicit field-finding language and resubmit. See
Troubleshooting
for common invocation issues.
For guidance on the AI Assistant interface, see the [AI Assistant UI guide](/en/docs/cx-enterprise-ai/experience-cloud-ai/ai-assistant/ai-assistant-ui).

## Supported use cases supported-use-cases

The following sections describe each of Field Discovery Agent’s three functions with representative scenarios and example prompts. Results include relevance labels and usage context to help evaluate fields. For result interpretation, see [Understand your results](#understand-your-results). Field Discovery Agent returns field information only — it does not create audiences, execute queries, or push data into other tools. After identifying a field, read its XDM path from the **Field Name** column and use it in your downstream workflow.

### Identify fields for a business concept

When you describe a specific data concept or attribute, Field Discovery Agent returns a ranked list of fields that semantically match your description.

“Which fields represent a customer’s home state or province?”“Find fields related to purchase transaction date.”“What fields contain information about email marketing consent?”

The response lists candidate fields with their relevance label and XDM path in the **Fields Identified** panel. Fields labeled **Highly Relevant** most closely match your stated concept. If the top results are labeled **Moderately Relevant** or **Relevant** rather than **Highly Relevant**, refine your query using more specific terminology or field-level context.

### Get field recommendations for a use case

When you describe a workflow goal or use case — such as building a segment, onboarding a dataset, or preparing a query — Field Discovery Agent recommends fields aligned to that objective, prioritized by relevance.

“I want to build an audience of high-value customers. What fields should I use?”“Recommend fields for modeling purchase propensity.”“What fields should I include when onboarding a retail transaction dataset?”

The response returns a prioritized list of fields with relevance context. Review the usage context for each recommended field to confirm it is actively used in your environment.

### Enrich field context

When you ask about a specific field by name or path, Field Discovery Agent returns detailed context for that field, including sample values, schema location, and usage across datasets, audiences, and destinations.

“Tell me more about the field person.name.lastName.”“What sample values exist for homeAddress.stateProvince?”“Where is the field commerce.purchases.value used across my datasets and audiences?”

The response returns the field’s sample values, schema location, associated datasets, and any audiences or destinations where the field appears. Review this context to confirm the field holds the data you expect.

## In scope and out of scope in-scope-and-out-of-scope

This section summarizes what Field Discovery Agent can and cannot do. For detailed task guidance, see [Supported use cases](#supported-use-cases). For platform constraints, see [Guardrails and limitations](#guardrails-and-limitations).

### In scope

The following list describes tasks Field Discovery Agent can perform; use it to confirm whether the agent can meet your request before you rely on it in your workflow.

- Identifying XDM fields that match a business concept or natural language description.
- Recommending fields for a stated workflow goal or use case.
- Enriching a specific field with sample values, schema location, and usage context.
- Returning results ranked by semantic relevance, labeled Highly Relevant, Moderately Relevant, or Relevant.
- Surfacing sample values within your authorized dataset permissions.

### Out of scope

The following list describes actions Field Discovery Agent does not perform; use it to avoid relying on the agent for work outside its scope.

- Modify schemas, datasets, fields, or audiences.
- Create or publish audiences or segments.
- Execute queries or activate data to destinations.
- Access fields or datasets outside your authorized permissions.
- Expose internal embedding logic, vector database architecture, or entity linking implementation details.
- Guarantee a specific time window for knowledge base updates after schema or dataset changes.

## Guardrails and limitations guardrails-and-limitations

These guardrails matter because Field Discovery Agent operates within platform-level constraints that affect result availability and quality. Use them to interpret missing, delayed, or incomplete results and to troubleshoot unexpected gaps with realistic expectations.

### Knowledge base

Field Discovery Agent relies on a knowledge base that is periodically refreshed with schema and metadata from your Experience Platform environment. Results reflect the state of the knowledge base at the time of your query—not the real-time state of your schemas, and there may be a delay between data ingestion and when it is surfaced in the agent.

New schemas, fields, or datasets added to your environment may not appear in Field Discovery Agent results immediately. Results may take time to reflect recent changes.

NOTE
The refresh interval for the knowledge base is subject to change. If a recently added field does not appear in results, allow time for the knowledge base to update and then resubmit your query.
### Metadata quality and coverage

Result quality depends on the quality and completeness of field metadata in your Experience Platform environment. The agent uses field names, display names, descriptions, and usage associations to rank results. Fields with poor or missing metadata may not surface in results or may rank lower than expected.

If you have schema editing access, you can improve result quality by:

- Using clear, descriptive display names for fields in your schemas.
- Adding field descriptions where possible.
- Associating fields with active datasets rather than leaving them as schema-only definitions.

For guidance on editing field display names and descriptions in the Schema Editor, see [Create and edit schemas in the UI](/en/docs/experience-platform/xdm/ui/resources/schemas).

If you do not have schema editing access and results are consistently poor, contact your Experience Platform administrator or data engineering team to review field metadata for the schemas you work with.

### Access and PII constraints

Field Discovery Agent respects all existing Experience Platform access controls and operates within your current sandbox context. You only receive results for fields in schemas and datasets you are authorized to access.

Sample values are governed by the same dataset-level permissions. Fields in profile-enabled datasets with PII restrictions return sample values only if you have the required access. See [Sample values](#sample-values) for handling guidance. Field Discovery Agent does not bypass field-level security or profile-enabled access restrictions.

## Best practices best-practices

Use the following guidance to get accurate, actionable results from Field Discovery Agent.

- **Be specific about the concept, not just the field type.** A prompt like “find a state field” produces lower-quality results than “find the field that holds a customer’s US state for geographic segmentation.” Specificity gives the agent more signal to match against your metadata. See [How Field Discovery Agent works](#how-field-discovery-agent-works) for why this matters.
- **Use terminology that matches your schema metadata.** If your schemas use the term “transaction” rather than “purchase,” use “transaction” in your prompts. The agent matches against actual field names and descriptions, not just general concepts.
- **Verify fields before committing.** After finding candidate fields, ask about a specific field by name or path to review its sample values and usage context before using it in a segment or query. This reduces the risk of selecting the wrong field.
- **Iterate when results are Moderately Relevant or Relevant rather than Highly Relevant.** Rephrase your query with different terminology or add more context about your use case. A second, more specific query often surfaces better candidates.
- **Include scope context in your prompts.** For geo-based segmentation, include the target region. For time-based queries, include the time attribute. The more context you provide, the more targeted the result ranking.

## Example prompts example-prompts

Use this section as a quick-reference prompt library. If you are new to Field Discovery Agent, read [Best practices](#best-practices) and [Supported use cases](#supported-use-cases) first to understand when and why each function applies.

### Identification prompts

Use these prompts when you know the data concept you need but not which field holds it.

“Which field holds a customer’s state or region?”“Find fields related to email subscription status.”“What field contains the date of a customer’s first purchase?”“Identify fields that represent customer lifetime value.”“Which fields in my profile schema relate to loyalty program membership?”

### Recommendation prompts

Use these prompts when you are starting a workflow and need guidance on which fields to include for a specific goal.

“What fields should I use to build a re-engagement audience?”“Recommend fields for an audience targeting customers who have not purchased in 90 days.”“What fields are most useful for modeling churn risk?”“Suggest fields I should include when creating a geographic segmentation.”“I am building a propensity-to-buy model. Which fields should I start with?”

### Enrichment prompts

Use these prompts when you have a candidate field and want to verify it before using it in a segment, query, or mapping.

“Tell me more about homeAddress.stateProvince.”“Show me sample values for commerce.purchases.value.”“Where is person.name.lastName used across my datasets and audiences?”“What datasets contain the field web.webPageDetails.URL?”“Is segmentMembership mapped to any active destinations?”

## Troubleshooting troubleshooting

Use this section when results are missing, unexpected, or when you are unsure whether Field Discovery Agent handled your request.

- A recently added field does not appear in results. The knowledge base may not yet reflect the new schema or field. Allow time for the knowledge base to update after adding schemas or fields to your environment, then resubmit your query. See Knowledge base .
- All results are labeled Moderately Relevant or Relevant rather than Highly Relevant. Your query may be too broad, or the terminology you used may not match your field metadata. Refine your prompt with more specific language or terms that align with how your fields are named in your schemas. See Best practices .
- Field Discovery Agent was not invoked. You submitted a query in AI Assistant but the Reasoning complete panel does not indicate Field Discovery Agent. Your query may not have contained a clear field discovery intent. Restate your query explicitly — for example, “Find the field that holds customer email opt-out status” — and resubmit. See Use Field Discovery Agent .
- Sample values are not appearing for a field. The field may be empty in your current sandbox, your permissions may not include access to its underlying dataset, or the field may have high cardinality (such as an ID field) for which sample values are not shown. Confirm your dataset access permissions and verify the field is populated with data. See Access and PII constraints .
- Results include fields from schemas you did not expect. Field Discovery Agent searches all schemas and datasets in your current sandbox that are accessible under your permissions. If unexpected results appear, confirm your active sandbox context in AI Assistant and verify which schemas and datasets are accessible to your role.

To verify which agent handled your request, see step 6 in [Use Field Discovery Agent](#use-field-discovery-agent).

recommendation-more-help


---
# FILE: journey-agent-overview-and-user-guide-b7af047d.md
---

---
title: "Journey Agent: Overview and User Guide"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/ajo-agent"
created_at: "2026-09-01T13:43:25.921675+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Journey Agent: Overview and User Guide

Last update: July 21, 2026
- Topics:
- [Journey management](#)
- [Communication channels](#)
- [Configuration](#)
- [Journeys](#)
- [Use cases](#)
- [Email](#)

CREATED FOR:

- User
- Admin
- Leader
- Developer

AVAILABILITY
Journey Agent create skills and content generation skills are available to customers that are a part of the Agent Orchestrator Explorer program. For more information, contact Adobe Customer Care.
## Introduction to Journey Agent in Adobe Journey Optimizer

Journey Agent enables Journey Optimizer users to create, analyze, and optimize marketing journeys using a natural language interface. With Journey Agent, practitioners can quickly build journeys, detect and resolve schedule or audience conflicts, analyze performance and drop-off points, and identify top-performing journeys to replicate for future campaigns. It empowers practitioners to make data-driven decisions, improve customer engagement, and streamline journey orchestration.

Journey Agent consists of four main jobs to be done:

- **Journey Create**: Build and configure marketing journeys through natural language prompts
- **Channel Content Create**: Generate, edit, and manage channel-specific content (email, push, SMS) for journeys using AI-powered content generation
- **Journey Analyze**: Analyze journeys, detect issues, uncover insights, and optimize customer engagement

In addition, **Journey Simulation** is a Journey Optimizer feature that includes [Journey Simulate](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/simulate-journey/simulate-journey-gs), an in-product agentic skill, non conversational, with three capabilities:

- Generating simulated users
- Generating event values
- Quick simulation

## Journey Create: Use cases, Agentic skills and User guide

## Overview

Journey Create enables Journey Optimizer users to build and configure marketing journeys using a natural language interface. With Journey Create, practitioners can quickly create journeys by describing their requirements in conversational prompts. The agent streamlines journey creation, allowing marketers to focus on strategy rather than technical configuration.

AVAILABILITY
Journey Create is available to customers that are a part of the Agent Orchestrator Explorer program. You will also need the following permissions in order to fully use Journey Create features:
Manage Journeys
: This permission lets you create new journeys directly in AI Assistant.
View Journey Events, Data Sources and Actions
: This permission ensures that the AI Assistant can search through Journey Events and Custom Actions.
View Segments
: This permission ensures that AI Assistant can search for audience segments when creating a Journey.
Manage Segments
: This permission lets you create new audiences directly in AI Assistant.
## Use cases

### Key use cases for Journey Create

Journey Create offers capabilities that can be leveraged to accelerate marketing execution:

- Event-triggered journey creation Create journeys that activate based on specific customer events. Design automated responses to customer actions in real-time. Build personalized communication flows based on customer behavior.
- Audience-targeted journey creation Build journeys targeting specific audience segments. Design multi-step communication sequences with strategic timing.
- Business-event triggered journey creation Create journeys that activate based on a particular business event and target a specified audience (e.g. product back in stock or game score change) Build personalized communication flows based on customer behavior.
- Audience qualification journey creation Create journeys that activate as profiles enter or exit an audience segment definition. Build personalized communication flows based on customer behavior.
- Conditional journey flows Create decision branches based on customer attributes. Design split paths that adapt to customer preferences.

For each of these use cases, the agent translates natural language requirements into structured journey configurations.

## In scope and out of scope skills

### In scope

The following capabilities are supported by Journey Create:

- **Natural language journey creation**: Allows users to describe journey flow in conversational language.
- **Event-based and audience-based journeys**: Supports both trigger-based and scheduled journey types, also business event and audience qualification.
- **Conditional logic**: Handles decision splits and branching based on customer attributes.
- **Multi-channel messaging**: Supports push notifications, email, and SMS channels.
- **Journey scheduling**: Configures start dates and timing for scheduled journeys.

### Out of scope

The following functionalities are currently not supported:

- **Advanced journey analytics**
- **Real-time journey modifications**
- **Cross-journey orchestration**
- **A/B testing configuration**
- **Complex data transformations**

## Sample prompts

### Common prompts for journey creation

Here are examples of valuable prompts users can leverage to create journeys.

### Event-triggered journey prompts

**Store visit journey:**

“Create a journey that starts when a user enters my store location. Send a push notification to welcome users to the store. Wait 2 days and check to see if the user has a valid email address. If the user has a valid email address, send an email survey to ask about their store experience. If the user does not have a valid email address, send a push notification to prompt for registration.”

**Post-purchase journey:**

“Create a journey that starts when a customer makes a purchase online. Send a push notification to thank them for their purchase. Next, check to see if they are loyalty members. If the user is a loyalty rewards member, send a second push notification with a 10% discount code. If the user is not a loyalty rewards member, send a push inviting them to sign up for the loyalty program. Wait 2 days and send a follow-up push with a survey about their purchase experience.”

**Event-based promotion:**

“Create a journey triggered when the game score reaches 50. Send an SMS message to loyalty reward members saying that they are eligible for a free slice of pizza from the partner sponsor.”

### Audience-targeted journey prompts

**Seasonal campaign:**

“I want to create a journey targeting an audience of day hikers. I want to send an email alerting this audience to my upcoming holiday sale that includes a variety of hiking essentials. Wait 3 days after sending the first email and send a second email that has a 15% coupon with free shipping. Wait 1 week and then send a 3rd email message to show our new sleeping bag and tent collection. Schedule the journey to start on 12/20.”

**Loyalty appreciation:**

“Build a loyalty appreciation journey for SUV owners, including a thank you push notification with a free carwash offer and a follow-up push notification reminder if the first notification is not interacted with within 1 day.”

### Open-ended prompts

For users starting without a specific journey in mind:

- “I’d like to create a journey”
- “Help me create a journey”
- “Create me a journey”

The agent will provide guidance and examples to help you define your journey requirements.

## Best practices

### Prompting best practices

To maximize the effectiveness of Journey Create, follow these best practices:

- **Be Specific**: Provide clear details about your journey goals, target audience, and desired actions. Include information about channels, timing, and conditions.
- **Specify Timing**: Clearly indicate wait periods between actions and when the journey should start.
- **Define Conditions**: When using conditional logic, explain the criteria for each branch path.
- **Include Channels**: Specify which communication channels you want to use (push, email, SMS).
- **Mention Scheduling**: For scheduled journeys, provide the desired start date and time.
- **Custom Actions**: If you are using custom actions in your workflow you need to specify that you are using a custom action along with the exact name of the custom action. Example:When a user enters my store location send a welcome message using custom action ExternalPush. Wait 2 days and then send a follow up message using custom action ExternalEmail with a survey on their visit.
- **Validate Expressions**: Make sure to check and validate any expressions that Journey Agent creates to ensure that the correct fields and values are used.

### Setup best practices

- **Define Clear Objectives**: Before creating journeys, establish clear goals (improving retention, driving conversions, increasing engagement).
- **Prepare Audiences**: Ensure your target audiences are already created and properly segmented.
- **Plan Message Content**: Have your messaging strategy defined before journey creation.
- **Consider Customer Experience**: Design journey flows that respect customer preferences and avoid over-communication.

## Channel Content Create: Use Cases, Agentic Skills and User Guide

AVAILABILITY
This feature is available for all customers in Limited Availability. Contact your Adobe representative to gain access.
## Overview

Channel Content Create enables Journey Optimizer users to generate, edit, and manage channel-specific content for journeys using AI-powered content generation.

## Use cases

### Key use cases for Channel Content Create

- Channel-specific content generation : Generate content for email, push notifications, SMS, and other channels using natural language prompts.
- Template-based content creation : Browse and select from available templates with preview capabilities.
- Multi-channel content management : Generate and manage content for multiple channels within the same journey workflow.
- In-context content editing : Open generated content in Content Designer for editing and refinement.
- Content refinement and iteration : Regenerate content with different tones or styles using the Regenerate action.
- Journey canvas integration : Select journeys from inventory and view associated channels.

## In scope and out of scope skills

### In scope

The following capabilities are supported by Channel Content Create:

- **AI-powered content generation**: Generate content for email, push, SMS, and other channels using natural language prompts.
- **Template management**: Browse and select from available templates with preview capabilities.
- **In-context editing**: Open generated content in Content Designer for editing and refinement.
- **Content regeneration**: Regenerate content with different tones, styles, or messaging using the Regenerate action.
- **Multi-channel support**: Generate and manage content for multiple channels within the same journey workflow.
- **Journey inventory access**: Select journeys from inventory and view associated channels.

### Out of scope

The following functionalities are currently not supported:

- **Brand alignment and content quality checks**
- **Insert content nodes directly into journey canvas**
- **Template import**

## Sample prompts

### Content generation

“Generate email content for my welcome journey. Create a welcome email for new customers with a friendly tone and include a 10% discount offer.”

“Add content for channel email for my welcome journey.”

“Generate a push notification for my store visit journey. Create a welcome message that encourages customers to check in and receive a special offer.”

“Generate SMS content for my event-triggered journey. Create a short message notifying customers about a flash sale with a call-to-action.”

### Template selection

“Show me available email templates for my seasonal campaign journey.”

“Select a template for my email that has a modern, clean design.”

### Content editing and refinement

“Open the email content in Content Designer so I can customize the design.”

“Regenerate the push notification content with a more casual tone.”

“Update the email content to include a promotional code.”

## Best practices

### Prompting best practices

- **Be Specific**: Provide clear details about the content type, tone, target audience, and key messaging.
- **Specify Channel**: Clearly indicate which channel you are creating content for (email, push, SMS).
- **Define Tone**: Specify the desired tone (friendly, formal, casual, urgent).
- **Iterate and Refine**: Use the regenerate action to refine content until it meets your requirements.

## Journey Analyze: Use Cases, Agentic Skills and User Guide

## Overview

Journey Agent will enable Journey Optimizer users to analyze, and optimize journeys using a natural language interface. With Journey Agent, practitioners can quickly identify and resolve schedule and/or audience conflicts, detect points of user abandonment in a journey and provide insights or recommendations. It empowers practitionners to make data-driven decisions, improve customer engagement, and streamline journey orchestration.

Learn more and discover the agent at a glance in this [overview](/en/slides/journey-agent-overview).

AVAILABILITY
The Journey Agent is available for all customers who have access to AI Assistant. However, you will need the following permissions in order to fully use the Journey Agent features:
View Journeys
: This permission lets you view insights into the journey directly in AI Assistant.
Manage Journeys
: To permission lets you create new journeys directly in AI Assistant.
View Segments
: This permission lets you view insights into the audiences directly in AI Assistant.
Manage Segments
: To permission lets you create new audiences directly in AI Assistant.
## Use Cases

### Key Use Cases for Journey Analyze

Journey Analyze offers a range of functionalities that can be leveraged to optimize marketing efforts:

- Journey Fallout Analysis Identify where and why customers drop off during a journey. Detect patterns in customer behavior leading to disengagement. Use insights to refine journey design and improve retention.
- Journey Audience Overlap Analysis Analyze audience overlap across multiple journeys. Prevent audience fatigue caused by over-targeting. Optimize segmentation to ensure balanced engagement.
- Journey Schedule Overlap Analysis Detect timing conflicts between scheduled journeys targeting the same audience. Avoid over-communication and improve scheduling efficiency. Maximize audience impact by ensuring journeys run at optimal times.
- Operational insights Prompt-based Journey Insights – Surface operational insights about journeys , i.e. “show me all live journeys.”

For each of these analyses, the agent not only detects issues but also provides **actionable recommendations to resolve them**.

## In Scope and Out of Scope Skills

### In Scope

The following capabilities are supported by Journey Analyze:

- **Reactive Queries**: Allows users to ask specific questions about journey performance, audience usage, and scheduling conflicts.
- **Integration with Other Agents**: Collaborates with Audience Agent and Data Insights Agent for deeper analysis.
- **Agent response structuration**: reasoning (explain the logic), analysis summary (highlight key points), issue details (describe the problem), and recommendation (propose next steps).

### Out of Scope

The following functionalities are currently not supported:

- **Automated Journey Creation**
- **Real-Time Anomaly Detection**
- **Channels overlap**
- **Journey entry analysis**
- **Technical issue analysis**
- **Fatigue analysis**

## Sample Prompts / Example Prompts

### Common Prompts for Journey Analysis

Here are examples of valuable prompts users can leverage to explore, monitor, and troubleshoot their journeys.

### Journey Lifecycle Questions

- “When was [Journey Name] published?”
- “When was [Journey Name] stopped?”
- “List all journeys currently in test mode”

### Journey Resource Questions

- “How many live journeys do I have?”
- “Give me a list of all scheduled recurring journeys and their expected run times.”

### Audience and Journey Insights

- “Which audiences are used in more than X journeys?”
- “List all journeys using the [audience name] audience.”

### Fallout analysis

- “I want to analyze the fallout by node for journey Fourth of July Campaign.”
- “Perform a fallout analysis for journey Fourth of July Campaign.”
- “What is profile loss over the course of journey Fourth of July Campaign?”
- “Show where users are dropping off in journey Fourth of July Campaign.”

### Conflict Analysis Prompts

Use these prompts to analyze potential conflicts between journeys, including scheduling and audience overlaps:

- “Can you do a comprehensive analysis of conflicts for our journey [Journey Name] with conflict type (scheduling/audience) information with live/running journeys?”
- “Please do a scheduling conflict analysis for journey [Journey Name] with conflict type information.”
- “Please do an audience overlap analysis for journey [Journey Name] with conflict type information.”
- “Are there any scheduling conflicts for journey [Journey Name]?”
- “Show me audience overlap conflicts for journey [Journey Name].”
- “Analyze all conflicts for journey [Journey Name] with other live journeys.”
- “What are the current conflicts for journey [Journey Name]?”
- “Check if journey [Journey Name] has audience conflicts with other journeys.”
- “Check for scheduling conflicts involving journey [Journey Name].”
- “I want to know about all journey conflicts for [Journey Name].”
- “Do any live journeys conflict with [Journey Name] by schedule or audience?”
- “Identify conflict types for journey [Journey Name] compared to running journeys.”
- “Show overlapping audiences for journey [Journey Name] and other journeys.”
- “Highlight scheduling overlaps between journey [Journey Name] and live journeys.”
- “Is journey [Journey Name] running in conflict with any other journey?”
- “Please detect and list conflicts for [Journey Name].”
- “Report all types of conflicts for journey [Journey Name].”
- “Give me a conflict breakdown (scheduling and audience) for [Journey Name].”
- “Does [Journey Name] have any conflicts that may impact performance?”
- “Are there any active conflicts affecting [Journey Name]?”
- “List journeys in conflict with [Journey Name] by schedule or audience.”
- “Has journey [Journey Name] triggered any conflict alerts?”
- “Find potential audience conflicts for journey [Journey Name].”
- “Analyze conflict risk for journey [Journey Name].”
- “Provide conflict diagnostics for [Journey Name].”

## Best Practices

### Prompting Best Practices

To maximize the effectiveness of Journey Analyze, follow these best practices:

- **Be Specific**: Use clear and concise prompts to get targeted insights. For example, instead of asking “What are my journeys?”, specify “List all journeys created in the last month.”
- **Combine Insights**: Integrate insights from Audience Agent and Data Insights Agent for a holistic view of journey performance.
- **Iterative Refinement**: Use fallout and overlap analysis to iteratively refine journey design and scheduling.

### Setup Best Practices

- **Define Clear Objectives**: Before analyzing journeys, establish clear goals (e.g., improving retention, increasing conversions).
- **Monitor Regularly**: Schedule regular reviews of journey performance to identify trends and anomalies.
- **Optimize Segmentation**: Ensure audience segmentation is balanced to avoid fatigue and maximize engagement.

## Journey Simulate: Use Cases, Agentic Skills and User Guide

## Overview

Journey Simulation is available to all Journey Optimizer customers. Journey Simulate, the in-product agentic skill within Journey Simulation, is available to customers that are a part of the Agent Orchestrator Explorer program and requires at least one of the following permissions:

- Simulate journeys : Run simulation workflows from the journey canvas.
- Publish journeys : Publish journeys, including flows that use simulation before go-live.
- Approve and Publish journeys : Approve and publish journeys when your organization uses approval workflows.

To use AI in **Simulation** (**Quick simulation**, generating simulated users with AI, **Generate event values**), users require **Generate Content** permission from the **AI Assistant** capability.

[Learn more about permissions](/en/docs/journey-optimizer/using/administration/permissions).

style
shade-box
Journey Simulation is a Journey Optimizer feature that enables Journey Optimizer users to safely test and validate marketing journeys before activation. Within Journey Simulation, Journey Simulate is an in-product agentic skill, not a conversational one, that automates and assists the testing process directly from the journey canvas.

Journey Simulate includes three capabilities:

- Generating simulated users
- Generating event values
- Quick simulation.

Together, they bridge the gap between journey creation and activation, building confidence in journey logic and reducing the risk of post-launch errors.

## Use cases

### Key use cases for Journey Simulate

Journey Simulate offers three capabilities that can be leveraged to reduce testing time and improve journey quality before go-live:

**Generating simulated users**

- Generate simulated users automatically based on journey paths and required attributes.
- Create simulated users that cover all branches and conditions in a journey, including execution addresses (email, push, SMS).
- Update simulated user attributes on demand to refine test scenarios.
- Ensure all journey branches are covered by assigning the right simulated user to each path.

**Generating event values**

- Generate values for events used in a journey to drive test execution through specific paths.
- Define event attribute values that trigger the desired conditions and branches during simulation.

**Quick simulation**

- Start journey simulation and trigger test executions for all simulated users needed to test all paths of a journey, in a single interaction.
- Visualize how simulated users flow through a journey, step by step, including branching paths and conditional logic.
- Identify which simulated user flows through which path, and why, with detailed node-by-node traversal.
- Review simulation reporting at the end of a run in the Journey Optimizer UI to validate outcomes before activation.

## In scope skills and limitations

### In scope

The following capabilities are supported by the Journey Simulation feature:

- **Simulated user management**: View, edit, and update simulated user attributes, including execution addresses and personalization data.
- **Simulation control**: Start and stop journey simulation directly through the Journey Simulation in-product experience.
- **Test execution**: Trigger test executions for one or multiple simulated users.
- **Journey flow visualization**: View step-by-step traversal of simulated users through journey nodes, including branching, splits, and user status.
- **Simulation reporting**: View reporting at the end of a simulation run in the Journey Optimizer UI.
- **Multi-user testing**: Run and visualize tests for multiple simulated users simultaneously, covering all journey branches.

In addition to this, the following capabilities are supported by the Journey Simulate skill:

- **Simulated user generation**: Create simulated users based on journey paths, existing test profiles, or specified attributes.
- **Event value generation**: Generate and assign event attribute values to drive test execution through specific journey paths.
- **Quick simulation**: Run a full end-to-end simulation with minimal intervention. The skill automatically generates simulated users, event values, and pre-filled test settings, then executes the journey and surfaces results for review.

### Limitations

Simulation may not support every activity, channel, or integration that Test mode or a live journey supports, and behavior may change as the capability matures.

➡️ Learn more about [Simulation limitations](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/simulate-journey/simulate-journey-gs#limitations) in the Journey Optimizer documentation.

recommendation-more-help


---
# FILE: legal-disclaimer-personal-data-language-support-and-verifying-responses-5fc97ff7.md
---

---
title: "Legal Disclaimer: Personal Data, Language Support, and Verifying Responses"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/ai-assistant/legal-disclaimer"
created_at: "2026-09-01T13:43:30.329835+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Legal Disclaimer: Personal Data, Language Support, and Verifying Responses

Last update: August 11, 2026
CREATED FOR:

- User
- Admin
- Leader
- Developer

Read this document for information on legal disclaimers regarding personal data, language support, and verifying responses when using the Adobe Experience Platform AI Assistant.

## Personal Data personal-data

AI Assistant uses an automated chatbot. Your use of this automated chatbot constitutes consent that the information you provide in the chat session will be collected, used, disclosed, and retained by Adobe and service providers acting on Adobe’s behalf in accordance with the terms of the agreement between your organization and Adobe.

If you need to include personal data here, only add what’s necessary and only if you have the right to use it.

## Language Support language-support

AI Assistant is currently supported in English only. Non-English inputs may produce inconsistent or erroneous results. Issues arising from non-English responses won’t be addressed or improved at the present time.

## Verifying Responses verifying-responses

It is important to check your answers, as language models can make mistakes. Always verify the sources to ensure that SQL logic is correct and that the appropriate documentation was referenced for your use case. Review the reasoning steps and explanations provided by AI Assistant to understand how it arrived at its answer. If something does not look right, please submit feedback.

recommendation-more-help


---
# FILE: product-support-agent-2a9e6a4c.md
---

---
title: "Product Support Agent"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/product-support"
created_at: "2026-09-01T13:43:26.794620+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Product Support Agent

Last update: July 14, 2026
CREATED FOR:

- User
- Admin
- Leader
- Developer

Product Support Agent is a self-serve debugging and troubleshooting capability of AI Assistant that you can use for Adobe Experience Platform features and applications.

You can use Product Support Agent in AI Assistant to seamlessly troubleshoot without leaving your workflows. When needed, support administrators can now use Product Support Agent to create customer support tickets, complete with context and session details from your interactions with AI Assistant. Additionally, you can now check on the latest updates to your support tickets using AI Assistant.

Product Support Agent includes the following solution capabilities:

## Quick troubleshooting help quick-troubleshooting-help

Get instant responses to common support questions sourced from expert-curated documentation, such as:

- Knowledge articles curated by Adobe support teams. Example questions: “Why does my profile count differ on the License Usage Dashboard and the Experience Platform home page?” “What are the reasons for a journey not triggering?”
- Product tutorials for self-guided learning and skill building. Example questions: “How does Adobe Experience Platform create real-time experiences?” “How do you configure and use alerts in Adobe Experience Platform?”
- Product legal documentation that provides accurate and licensing-oriented information. Example questions: “What is the limit for batch segmentation jobs in Adobe Experience Platform Activation?” “What is the average profile richness limit in Adobe Experience Platform Activation?”

## Support case creation support-case-creation

Initiate support cases directly from Product Support Agent, which automatically captures contextual insights to accelerate case resolution.

- Example questions: “Create a support ticket.” “Can you help me create a support ticket?”

## Track case progress track-case-progress

Seamlessly track the status of support issues.

- Example questions and commands: “What is the latest on my case E-12345?” “What’s the update on ticket E-67890?”

## Access Product Support Agent

Follow the [access guide](/en/docs/cx-enterprise-ai/experience-cloud-ai/agents/agent-orchestrator#access) to learn how to enable permissions and access AI Assistant.

Once you complete these steps, any support admins in your onboarded organization will be able to create tickets using AI Assistant.

For more information, watch the following video to learn how you can use Product Support Agent to seamlessly troubleshoot without leaving your workflows.

https://video.tv.adobe.com/v/3443183?learn=on
recommendation-more-help


---
# FILE: real-time-cdp-mcp-beta-rtcdp-mcp-bf707ef3.md
---

---
title: "Real-Time CDP MCP (Beta) rtcdp-mcp"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/mcp/rtcdp-mcp"
created_at: "2026-09-01T13:43:28.641974+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

[Beta]{class="badge informative"}

# Real-Time CDP MCP (Beta) rtcdp-mcp

Last update: July 17, 2026
- Topics:
- [Integrations](#)

CREATED FOR:

- Beginner
- Intermediate
- User
- Developer

You can use the Adobe Real-Time CDP MCP integration to query audiences, destinations, and activation health using plain-language prompts — without writing API calls or navigating product screens. This integration serves both Adobe Real-Time CDP and Adobe Real-Time CDP B2B Edition customers, providing a conversational way to inspect supported Real-Time CDP data and workflows from MCP-compatible clients. Read this guide to learn how the integration works, what you can do with it, and how to get started.

AVAILABILITY
Real-Time CDP MCP is in Beta. The feature and documentation are subject to change. The Real-Time CDP MCP server is distributed as a
remote HTTP transport server
that users install and configure in supported MCP clients and app platforms (for example, Claude, ChatGPT, Claude Code, Codex, Cursor, or VS Code). Authentication is handled through a
browser-based login flow
— when your client first connects to the server, it opens your default browser so you can sign in with your Adobe credentials and authorize access. Please contact your Adobe representative to access this Beta program.
## Beta, security, and legal notices mcp-notices

**Beta documentation notice:** This documentation covers a Beta feature and does not constitute final documentation. The content described herein relates to a Beta release and is subject to change prior to general availability. Adobe makes no representations about the completeness or accuracy of this documentation.

By using the Adobe Real-Time CDP MCP Server (Beta) (“Beta”), You hereby acknowledge that the Beta is provided **“as is” without warranty of any kind**. Adobe shall have no obligation to maintain, correct, update, change, modify or otherwise support the Beta. You are advised to use caution and not to rely in any way on the correct functioning or performance of such Beta and/or accompanying materials. The Beta is considered Confidential Information of Adobe. Any “Feedback” (information regarding the Beta including but not limited to problems or defects you encounter while using the Beta, suggestions, improvements, and recommendations) provided by You to Adobe is hereby assigned to Adobe including all rights, title, and interest in and to such Feedback.

WARNING
The Model Context Protocol (MCP) is an emerging open-source standard and may present security or reliability risks. Adobe MCP server integrations and related documentation are provided “as is,” without warranties of any kind.
Connecting MCP clients or servers to Adobe products is a customer-elected configuration. Customers are responsible for evaluating the security and suitability of any MCP integration. Adobe is not responsible for issues arising from misconfiguration, misuse of the MCP, vulnerabilities in third-party implementations, or unintended actions performed through MCP-enabled workflows.
To reduce risk, Adobe encourages testing integrations in a sandbox environment prior to productive use, and carefully reviewing and validating all MCP-initiated actions and responses before confirming or relying on them.
## What is the model context protocol? mcp-overview

Marketing, data, and customer-experience teams increasingly rely on chat-based applications and developer tools — such as Anthropic Claude, OpenAI ChatGPT, Cursor, and Microsoft Copilot Studio — to streamline their day-to-day work. These applications support the **Model Context Protocol (MCP)**, an open standard that lets applications expose back-end tools to large language models (LLMs) in a uniform way.

Real-Time CDP now provides an MCP server that surfaces audience, destination, and activation operations directly inside any MCP-compatible application. With the Real-Time CDP MCP integration, different personas can collaborate around the same segmentation and activation data — without writing queries against the Adobe Experience Platform REST APIs or navigating multiple UI screens. Customers can describe their intent conversationally and let the LLM invoke the appropriate MCP tools.

## Key capabilities mcp-capabilities

The Real-Time CDP MCP server is a **read-only** monitoring and triage surface. It exposes retrieve APIs across audiences, destinations, sources, identity, and profile resolution as plain-language answers inside your AI assistant — without writing queries or navigating product screens. No data can be created, modified, or deleted through the MCP server.

IMPORTANT
All tools in the current Beta are
read-only
. Write operations — including creating, activating, updating, or deleting audiences, destinations, or dataflows — are not supported.
The Beta release includes the following 18 tools:

Tool
Description
search_audiences
List and look up audiences by name, entity type, lifecycle state, identity namespace, or origin.
preview_audience_membership
Estimate the size of a PQL or SDD segment expression before saving it as an audience.
inspect_audience_evaluation_jobs
Retrieve segment evaluation job records to diagnose why a batch audience isn’t refreshing or to confirm recent evaluation history.
inspect_audience_export_jobs
Retrieve audience export job records to confirm exports completed or to surface failure details.
search_destination_connectors
List the destination connector types available in the platform (e.g. Amazon S3, Google Ads, Salesforce CRM).
search_destination_accounts
List authenticated destination accounts — configured instances of a destination connector type.
search_destination_input_connections
Retrieve the Experience Platform-side input of a destination flow — the audience or dataset being exported.
search_destination_output_connections
Retrieve the external endpoint of a destination flow — target path, file format, and delivery configuration.
search_destination_flows
List and inspect configured destination activation flows including their state, mappings, and schedule.
inspect_flow_runs
Retrieve execution history for source and destination flows — status, timing, record counts, and failure details per run.
search_source_connectors
List the source connector types available in the platform.
search_source_accounts
List authenticated source accounts — configured instances of a source connector type.
search_source_input_connections
Retrieve the data selection layer of a source flow — what is being pulled from an account.
search_source_output_connections
Retrieve the Experience Platform dataset destination of a source flow — where ingested data lands.
search_source_flows
List and inspect configured source ingestion pipelines including their state, mappings, and schedule.
search_identity_namespaces
List identity namespace definitions in your sandbox — both Adobe-standard and custom namespaces.
search_merge_policies
List merge policy records that control how Real-Time Customer Profiles are assembled from profile fragments.
search_organizations
List the Adobe organizations accessible to the authenticated user.
## Use cases mcp-use-cases

The Real-Time CDP MCP server is designed for **monitoring and triage**. Because the server works with IDs rather than names, a typical workflow starts with a list — ask Claude to show you what’s available, pick the item you want, then ask follow-up questions using the ID it returns.

Goal
Example prompt
List your audiences
“List my audiences in the
prod
sandbox.”
Inspect a specific audience
“Show me the details and lifecycle state for audience ID
abc123
.”
Diagnose an evaluation failure
“Show me the most recent evaluation jobs and flag any failures.”
Check an export job
“List recent audience export jobs and show me the status of each.”
Estimate audience size
“Estimate the size of this PQL expression before I save it:
homeAddress.country = 'US'
.”
List destination connector types
“What destination connector types are available in my sandbox?”
List configured destination accounts
“List my destination accounts and their connection state.”
List destination flows
“List my destination activation flows and show which are enabled or disabled.”
Inspect a destination flow
“Show me the full configuration for destination flow ID
xyz789
.”
Check destination account health
“List my destination accounts and flag any that are in an error state.”
Monitor recent activation runs
“Show me flow runs from the last 24 hours and flag any failures.”
Investigate a failed run
“Show me the run history for flow ID
xyz789
and summarize any errors.”
List source flows
“List my source ingestion flows and show their current state.”
Inspect a source flow
“Show me the configuration for source flow ID
src456
— what is it ingesting and where does it land?”
Check ingestion run health
“Show me recent run history for source flow ID
src456
and flag failures.”
List identity namespaces
“What identity namespaces are configured in my sandbox?”
List merge policies
“List my merge policies and show which is the default.”
Find your Organization ID
“List the Adobe organizations I have access to.”
## Access and enablement mcp-access

AVAILABILITY
The Real-Time CDP MCP server is in Beta and is not open for self-service enrollment. Access is by invitation only and requires your Adobe organization to be explicitly allowlisted before you can connect.
To request access:

- Contact your Adobe account representative (Customer Success Manager, Technical Account Manager, or Account Executive) and express your interest in the Real-Time CDP MCP Beta program.
- Your Adobe representative will coordinate with the product team to evaluate eligibility and enable your Organization ID.
- Once enabled, your Adobe representative will confirm access and provide any additional onboarding materials.

NOTE
Only organizations that have been explicitly enabled can connect to the Real-Time CDP MCP server. Attempting to connect before enablement will result in an authentication error.
## Prerequisites mcp-prerequisites

Before connecting the Real-Time CDP MCP server to your MCP client, ensure the following:

- You have an active Real-Time CDP license.
- Your Adobe organization has been enabled for the Beta program by your Adobe representative (see [Access and enablement](#mcp-access)).
- You have access to a supported MCP client such as Claude, ChatGPT, Claude Code, Codex, Cursor, or VS Code.
- You have your Organization ID and the name of the sandbox you want to query.
- You have the necessary permissions in Adobe Experience Platform to view audiences, destinations, and flow service entities.

## Connect the Real-Time CDP MCP server mcp-connect

The Real-Time CDP MCP server endpoint is:

```
https://rtcdp-mcp.adobe.io/mcp
```

The server uses a **remote HTTP (Streamable HTTP) transport** with a **browser-based Adobe sign-in flow**. In every client, the setup pattern is the same:

- Add the server URL: https://rtcdp-mcp.adobe.io/mcp
- Save or enable the connection.
- Complete the **browser-based Adobe login** the first time the client invokes a tool.
- Provide imsOrgId and sandboxName at the start of each session.

### General JSON configuration mcp-connect-json

For clients that accept a JSON-based MCP server configuration — such as Claude Desktop (claude_desktop_config.json), VS Code, or any client that reads a mcp.json file — use one of the following formats depending on whether your client supports native remote HTTP or requires a local bridge:

**Via mcp-remote bridge (Claude Desktop and other clients that require a local bridge)**

```
{
  "mcpServers": {
    "rtcdp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://rtcdp-mcp.adobe.io/mcp"
      ]
    }
  }
}
```

**Native remote HTTP (clients that support it directly)**

```
{
  "mcpServers": {
    "rtcdp": {
      "url": "https://rtcdp-mcp.adobe.io/mcp",
      "transport": "http"
    }
  }
}
```

NOTE
No API keys, bearer tokens, or additional headers are required in the configuration. Authentication is handled entirely through the browser-based Adobe sign-in flow on first use.
### Install in UI-based clients mcp-connect-ui

#### Claude

For claude.ai and Claude Desktop, add the Real-Time CDP MCP server as a **custom connector** using the server URL https://rtcdp-mcp.adobe.io/mcp.

- **Individual plans** — In Claude, navigate to **Customize → Connectors**, select **Add connector**, and enter the server URL.
- **Team and Enterprise plans** — A workspace **Owner** or **Primary Owner** adds the connector under **Organization settings → Connectors**. Once added, each user enables it in their own Claude settings.

After the connector is added, enable it in a conversation and complete the Adobe browser sign-in on first use. Claude discovers the Adobe authorization server automatically — no Client ID or Client Secret is required.

#### ChatGPT

In ChatGPT, add the Real-Time CDP MCP server as a **custom connector**:

- Navigate to **Settings → Connectors** (or **Settings → Apps & Connectors**, depending on your plan).
- Select **Add connector** and enter https://rtcdp-mcp.adobe.io/mcp as the server URL.
- Save the connector. Depending on your ChatGPT plan, this step may require **Developer mode** or workspace admin approval.
- Once the connector is enabled, authenticate through the Adobe browser sign-in when prompted on first use.

#### Cursor

In Cursor, add the Real-Time CDP MCP server as a remote MCP server:

- Open **Settings → MCP**.
- Select **Add new server** and enter https://rtcdp-mcp.adobe.io/mcp as the server URL.
- Select **connect** to trigger the browser-based Adobe sign-in and authenticate.

Once connected, Real-Time CDP tools are available in Cursor’s Composer and Agent modes.

#### Other UI-based clients

For clients such as VS Code or other desktop and web applications with remote MCP support, add the Real-Time CDP MCP server as a **remote HTTP** server using https://rtcdp-mcp.adobe.io/mcp. If the client supports optional headers or bearer tokens, leave them empty — authentication is handled through the browser-based Adobe sign-in flow on first use.

### Install in technical clients mcp-connect-technical

#### Claude Code

Add the server from the terminal:

```
claude mcp add --transport http rtcdp https://rtcdp-mcp.adobe.io/mcp
```

Then start Claude Code and run:

```
/mcp
```

Select the rtcdp server and complete the Adobe login flow in your browser. If you already added the server in claude.ai, it may appear automatically in Claude Code when both are signed in to the same account.

#### Codex

Add the server from the terminal:

```
codex mcp add rtcdp --url https://rtcdp-mcp.adobe.io/mcp
```

Authenticate the server:

```
codex mcp login rtcdp
```

Verify the configuration:

```
codex mcp list
```

You can also add the server directly to ~/.codex/config.toml:

```
[mcp_servers.rtcdp]
url = "https://rtcdp-mcp.adobe.io/mcp"
```

### Required request parameters mcp-connect-params

Every tool call requires two parameters that scope the request to your Adobe Experience Platform tenant:

- imsOrgId — your Organization ID, mapped to the x-gw-ims-org-id header on downstream Experience Platform API calls.
- sandboxName — the Experience Platform sandbox name, mapped to the x-sandbox-name header.

Provide these at the start of each session. For example:

“Use org 1234ABCD@AdobeOrg and sandbox prod for this session.”

If you don’t know your Organization ID, ask your AI assistant to call search_organizations — it will return every org your Adobe credentials can access.

## Known limitations (Beta) mcp-limitations

The following limitations apply to the current Beta release of the Adobe Real-Time CDP MCP server:

Limitation
Description
Workaround
Read-only surface
The MCP server only exposes retrieve APIs. You cannot create, update, activate, or delete audiences, destinations, or dataflows.
Use the Real-Time CDP UI or the Experience Platform REST APIs for write operations.
No engagement or delivery metrics
The MCP server does not return downstream delivery stats, engagement, or conversion metrics from destination platforms.
Use the destination platform’s own reporting, Customer Journey Analytics MCP, or Adobe Analytics MCP for engagement and conversion data.
Segment query must be authored externally
Preview Audience Membership
requires a valid PQL or SDD expression as input; the MCP server does not compose the query for you.
Author the PQL/SDD expression in the Segment Builder UI or via the Segmentation Service API, then paste into the MCP prompt.
Pagination via continuation tokens
List tools return paginated results. Full enumeration across very large sandboxes requires chaining
continuationToken
calls.
Narrow queries using filters (name, state, connection spec, time range) rather than enumerating the full list.
Activation run filtering is time-based only
Inspect Activation Runs
supports filtering by status and completion timestamp (epoch ms UTC), but not by error type or destination platform directly.
Filter by
flowId
first (obtained from
List Configured Destinations
) to scope runs to a specific destination.
Organization ID required at session start
Every tool call (except
search_organizations
) requires
imsOrgId
and
sandboxName
as explicit parameters. If these are not provided, tool calls will fail.
At the start of each session, tell your AI assistant: “Use org
<YOUR_ORG_ID>
and sandbox
<SANDBOX_NAME>
for this session.” If you don’t know your Organization ID, call
search_organizations
first — it will return the orgs your credentials can access.
## Frequently asked questions mcp-faq

Which MCP clients are supported?
The Real-Time CDP MCP server works with any client that supports remote MCP servers or custom connectors — including Claude, ChatGPT, Claude Code, Codex, Cursor, and VS Code. The setup flow depends on the client: UI-based clients typically add the server from a settings or connectors panel, while technical clients such as Claude Code and Codex can add it from the command line or configuration files.
How do I get access?
Access is by invitation only during the Beta. Contact your Adobe account representative (Customer Success Manager, Technical Account Manager, or Account Executive) to request enrollment. Your Adobe representative will coordinate with the product team to enable your organization. See
Access and enablement
for details.
How does authentication work?
Authentication is handled through a
browser-based login
. When your MCP client first invokes a tool, it opens your default browser to an Adobe sign-in page. After you authenticate and authorize the client, the session is established and subsequent tool calls reuse it. No API keys or long-lived credentials need to be stored in your client configuration.
What Real-Time CDP objects can I access via MCP?
You can access audiences, destination types, configured destination accounts, destination dataflows, source and target connections, and activation run history. Operations are read-only (retrieve APIs); write operations are not supported in the current release.
Do I need developer access to use the Real-Time CDP MCP server?
No. The MCP server is designed for both marketing and technical personas. Marketers can interact with it using natural language prompts in any supported MCP client, while data engineers and developers can use it in developer tools that support MCP.
recommendation-more-help


---
# FILE: visualize-data-with-data-insights-agent-4b07cf3c.md
---

---
title: "Visualize data with Data Insights Agent"
url: "https://experienceleague.adobe.com/en/docs/experience-cloud-ai/experience-cloud-ai/agents/cja-data-insights-agent"
created_at: "2026-09-01T13:43:22.828547+00:00"
---
Breadcrumbs: Documentation > AI Documentation > AI in CX Enterprise

# Visualize data with Data Insights Agent

Last update: August 11, 2026
- Topics:
- [Analytics dashboards](#)
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- User
- Admin

AVAILABILITY
Data Insights Agent is available to eligible customers for a limited time. Access to Data Insights Agent is available through March 31, 2026. To continue using Data Insights Agent beyond this date without interruption, please contact your Adobe account representative to learn more about licensing Adobe Experience Platform Agent Orchestrator.
Data Insights Agent, accessible from the [AI Assistant](/en/docs/cx-enterprise-ai/experience-cloud-ai/ai-assistant/ai-assistant-ui), is a generative AI conversation agent that quickly and efficiently answers questions about your data. It builds relevant visualizations in Analysis Workspace using components from your data view and your actual data.

Using Data Insights Agent to answer data-centric questions in Analysis Workspace can save significant time that you might otherwise spend manually building visualizations in Analysis Workspace and familiarizing yourself with your data view components.

## In-scope vs. out-of-scope features

Feature
In scope
Out of scope
Visualization types
- Line
- Multi-line
- Freeform table
- Bar
- Donut
- Summary number

- Flow
- Fallout
- Cohort Table
- Area, Area Stacked
- Bar Stacked
- Bullet
- Combo
- Histogram
- Horizontal Bar, Horizontal Bar Stacked
- Key Metric Summary
- Scatter
- Summary Change
- Text
- Treemap
- Venn
- Guided analysis: Active growth, Conversion trends, Engagement, First use impact, Frequency, Funnel, Net growth, Release impact, Retention, Timeline, Trends

Workspace actions and agent capabilities
- Build and update visualizations Generates a freeform table and associated visualization (such as a line, bar, donut, and so forth). For example, What is the profit across SKUs from February to May?
- Ask follow-up questions Respond to a prompt in the context from any prior prompts. For example: Prompt 1: Trend events from March. Prompt 2: Show me the data from March to April instead
- Out-of-scope prompt detection If you submit a prompt that is out of scope, such as Export this project , Data Insights Agent responds by informing you that the question is out of scope.

- Share
- Export
- Download
- Manage user preferences
- Manage data view
- Analytics Dashboards app
- Attribution
- In-line summary or response Data Insights Agent cannot respond in-line in the chat rail with a summary answer of a user prompt. Examples of out-of-scope prompts are, Give me a summary of the insights from my last prompt and Summarize the highlights from the line visualization.

Clarifying questions
If you ask a question that does not have enough context for Data Insights Agent to answer, or is too generic, Data Insights Agent responds with a clarifying question or suggested options.

The following clarifying questions are examples of component-related questions:

- Metric: *Which “revenue” metric did you mean?*
- Dimension: *Which of the below “regions” do you want to focus on?*
- Segment: *Which “Account” segment did you want to apply?*
- Date Range: *By “last month,” did you mean the last full month or the last 30 days?*

The following clarifying question is an example of a question related to dimension items:

- Which “store name” did you mean? (For example, Store #5274, Store #2949, and so forth.)

Clarifying questions are limited to components and dimension items. Data Insights Agent cannot clarify things such as data views, visualizations, data granularity, comparison, and scope. When clarifying questions cannot be used, the agent defaults to what you are most likely asking for. If it returns an unexpected visualization or data granularity, you can ask a follow-up question or adjust the visualization and data.
Data verifiability and correctness
Data verifiability and correctness can be confirmed by viewing the generated freeform table and data visualization.

For example, if you ask Data Insights Agent to *Trend orders last month*, you can confirm that the correct metric (“orders”) and date range (“last month”) were selected in the newly generated panel, data visualization, and freeform table.

Data Insights Agent does not respond by informing you which components or visualizations were added.
Feedback mechanisms
- Thumbs up
- Thumbs down
- Flag

## Manage access to Data Insights Agent manage-access

The following parameters govern access to Data Insights Agent in Customer Journey Analytics:

- Solution access : Data Insights Agent is available for eligible customers for a limited time. Access to Data Insights Agent is available through February 28, 2026. It is not available in Adobe Analytics.
- Contractual access : If you are not able to use Data Insights Agent in the AI Assistant, please contact your organization’s administrator or Adobe account team. Before your organization can use Data Insights Agent, you must agree to certain legal terms related to generative AI.
- Permissions : Necessary permissions must be granted in the Adobe Admin Console before users can access Data Insights Agent. To grant permissions, a product profile administrator must complete the following steps in the Admin Console: In the Admin Console , select the Products tab to view the All products and services page. Select Customer Journey Analytics . On the Product Profiles tab, select the title of the product profile for which you want to provide access to AI Assistant: Product Knowledge. In the specific product profile, select the Permissions tab. In the Reporting Tools row in the provided table, select the edit icon . Scroll to or search for AI Assistant: Product Knowledge , then select the plus icon next to this permission. Scroll to or search for Data Insights Agent , then select the plus icon next to this permission. The AI Assistant: Product Knowledge permission and the Data Insights Agent permission are added to the Included permission items column. . Select Save to save the permissions. For additional information about access control, see Access control .
- Data view access : Data views must be enabled for Data Insights Agent. note important IMPORTANT Consider the following when enabling data views: You can enable a maximum of 50 data views per IMS organization. If you enable more than 50 data views across all product profiles for a given organization, the Data Insights Agent will use the 50 most-used data views. You can use the info on the Data Insights Agent column in Data views to view the number of data views that are enabled for Data Insights Agent in your IMS organization. The Data Insights Agent can reference the included data views sometime during the same day that you enable them. To enable data views for Data Insights Agent: In Customer Journey Analytics, select Data Management > Data views . Select one or more data views that you want to enable for Data Insights Agent, then select Enable for Data Insights Agent . For more information about enabling data views for Data Insights Agent, see the AI Settings for a data view . To view the number of data views that are enabled for Data Insights Agent in your IMS organization: In Customer Journey Analytics, select Data Management > Data views . Select the info icon at the top of the Data Insights Agent column.

## Access Data Insights Agent in the AI Assistant

- Go to experience.adobe.com and log in with your Adobe ID.
- Select Customer Journey Analytics from CX Enterprise Home.
- Select Blank project in the banner at the top of the projects page to open a new blank project.
- Ensure that the selected data view for the panel is a data view that was enabled for use with Data Insights Agent, as described in Manage access to Data Insights Agent in Customer Journey Analytics .
- Select the AI Assistant chat icon at the top-right area of the page. If you do not see the chat icon, contact your administrator so they can enable the following features in the Admin Console: Reporting Tools: AI Assistant: Product Knowledge Data View Tools: Data Insights Agent For additional details, see Manage access to Data Insights Agent in Customer Journey Analytics .
- In the Ask about Customer Journey Analytics dialog at the bottom of the page, ask a data visualization question using Data Insights Agent. For more information, see the following examples.

### Example 1

For example, let’s say you are interested in the orders your business received in July.

**Prompt:** Enter *“Trend orders in July.”*

**Response:** Data Insights Agent gathers insights by looking through the data in the data view, including the metrics and components. It translates the prompt into the right dimensions and metrics within the data range.

As you can see, it automatically generated a line graph and a freeform table to show orders for July.

### Example 2

Next, you want to see how your revenue compares by region.

**Prompt:** In the prompt window, enter *“Show revenue by region.”*

**Response:** Data Insights Agent intelligently understands that by “region,” you mean “customer region.” It produces a bar chart that best shows revenue by region:

### Example 3

Next, in addition to understanding revenue by region, you also want to see data for profit by region. Instead of repeating the previous prompt, you can ask Data Insights Agent to update the most recent visualization and freeform table.

**Prompt:** In the prompt window, type *“Add profit.”*

**Response:** The **Bar** chart still provides the most concise answer, but the profit metric has been added as a column in the freeform table:

### Example 4

Finally, let’s look at the revenue by product category.

**Prompt:** In the prompt window, enter *“Proportion of revenue by product category.”*

**Response:** Again, Data Insights Agent picks the most appropriate visualization, in this case the **Donut** visualization, to answer the question.

## Access Data Insights Agent across CX Enterprise applications

Adobe Experience Platform Agent Orchestrator allows you to access the functionality of Data Insights Agent in multiple Adobe CX Enterprise applications, such as Adobe Journey Optimizer and Real-Time CDP.

Agent Orchestrator interprets your request, determines which specialized agents are needed, and orchestrates them to deliver the right response. It keeps track of context across multi-turn interactions, so you can build on prior queries naturally.

For more information, see [Adobe Experience Platform Agent Orchestrator](https://business.adobe.com/products/experience-platform/agent-orchestrator.html).

## Example data visualization prompts

The following are some examples of common prompts and the visualizations used by Data Insights Agent to respond to those prompts.

Example prompt
Expected visualization
Show me profits in [Month]
Line

Asking for a trend or metric within a certain time range by default returns a line visualization.

Trend orders in [Month]
Line
Show revenue by region in [Month]
Bar
Share of revenue by product category
Donut
Orders by day of week, from January to May
Bar
Show orders by gender, from March to June
Bar
What is the profit across SKUs from February to May
Bar
Revenue by store name in [Month]
Bar
What were my top 10 SKUs by profit in [Month]?
Bar
Proportion of purchases by month of year
Donut
Total profit in [Month]
Summary Number

Asking for the “total” of a metric across a certain time range should return a Summary number visualization.

## Prompting best practices

Data Insights Agent processes the context provided by each user prompt and tries to respond intelligently with the most appropriate visualization and components in a freeform table.

Responses can vary based on the specific words and phrases used in the prompt, and slight changes in language can lead to different results.

To achieve the best results, consider the following guidelines:

- Be specific: Include exact terms to narrow down the response. The following is an example of a specific prompt: “Last month’s sales in California”
- Use clear metrics, dimensions, and segments: Adding specific metrics (such as “Revenue”), dimensions (such as “website name”), segments (such as “iPhone users”), and date ranges (such as “last three months”) helps Data Insights Agent focus on the right data.
- Ask direct questions: Phrasing questions directly makes it easier for Data Insights Agent to provide clear, relevant insights. The following is an example of asking a direct question in a prompt: “What is the average revenue by product category this year?”

Review the following table of example terms and phrases that you can use in prompts with Data Insights Agent, along with the types of responses you can expect.

These examples are designed to help you get familiar with how specific words or structures can influence the output of the Data Insights Agent, ensuring more precise and valuable insights. Data Insights Agent uses generative AI, so visualizations or selected data may vary slightly across similar prompts.

Desired outcome
Example terms and phrases
Summary number visualization
- Total

Compare components
- Compare
- VS
- Contrast
- Week-to-Week
- Month-over-Month
- Quarter-over-Quarter
- Year-over-Year

Donut visualization
- Proportion
- Share of
- Distribution
- Percentage
- Contribution
- Portion
- Parts

Line visualization
- Trend
- [Metric] in [Time range]

Bar visualization
- [Metric] by [Dimension]

## Configuration best practices

Below are best practices for your Customer Journey Analytics configuration (data view, calculated metrics, segments, and more) to ensure that the Data Insights Agent can locate the correct components and return cleaner answers without having to prompt you for additional information.

- **Balance what components you need**. Do not add all the fields of your datasets as metrics or dimension components to your data view, especially those you don’t expect to use in your analysis. On the other hand, do not strictly limit yourself only to the fields you anticipate you require for your analysis. A too limited data view restricts the flexibility in your analysis and the Data Insights Agent functionality.
- **Always use friendly display names**. Ensure that all fields you define in your data view, either as a metric or dimension component, have a friendly component name. The process of renaming fields with a friendly name is especially relevant for fields from Adobe Analytics source connector datasets. These fields often have non-friendly unidentifiable names, like eVar41 or prop25.
- **Use distinctive names**. Distinctive names are especially relevant when you use the same field as both a metric and a dimension component in your data view. Or when you use a field in multiple components of the same type (such as in two different metrics), each with different component settings.
- **Use a component naming convention**. You can use a component naming convention to group components. For example, **Orders | Product** and **Orders | Customer** can distinguish between different order metrics that might exist in your data.
- **Use the Data Dictionary**. Add descriptions and other relevant data for components in the Data Dictionary. The Data Insights Agent currently does not use description and tags from the Data Dictionary, but it might in the future.
- **Use approved calculated metrics**. Agree on a process to use only approved calculated metrics as components in your data view, and avoid using experimental calculated metrics.
- **Share required segments**. Ensure that you share segments and make segments visible that are required for Data Insights Agent prompts.
- **Standardize on component names across data views**. If you use the same fields as a component in multiple data views, ensure that you use a single friendly name and a single identifier for that component. A single name and identifier allows the Data Insights Agent to switch data views without losing context.

Related Articles
Component settings
Data Dictionary
Approve calculated metric
Share segments
recommendation-more-help

