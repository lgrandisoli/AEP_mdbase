---
title: "Integrate Customer AI data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/integrations/customer-ai"
category: "other"
topic: "analytics-platform/using/integrations/customer-ai"
created_at: "2026-06-23T20:44:07.982252+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Integrate Customer AI data

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Integrations](#)

CREATED FOR:

- Admin

AVAILABILITY
The functionality described in this article is in the Limited Testing phase of release and might not be available yet in your environment. This note will be removed when the functionality is generally available. For information about the Customer Journey Analytics release process, see
Customer Journey Analytics feature releases
.
[Customer AI](/en/docs/experience-platform/intelligent-services/customer-ai/overview), as part of Adobe Experience Platform Intelligent Services, provides marketers with the power to generate customer predictions at the individual level.

With the help of influential factors, Customer AI can tell you what a customer is likely to do and why. Additionally, marketers can benefit from Customer AI predictions and insights to personalize customer experiences by serving the most appropriate offers and messaging.

Customer AI relies on individual behavioral data and profile data for propensity scoring. Customer AI is flexible in that it can take in multiple data sources, including Adobe Analytics, Adobe Audience Manager, Consumer Experience Event data and Experience Event data. If you use the Experience Platform source connector to bring in Adobe Audience Manager and Adobe Analytics data, the model automatically picks up the standard event types to train and score the model. If you bring in your own Experience Event dataset without standard event types, any relevant fields will need to be mapped as custom events or profile attributes if you’d like to use it in the model. This can be done in the Customer AI configuration step in Experience Platform.

Customer AI can integrate with Customer Journey Analytics to the extent that Customer AI-enabled datasets can be leveraged in data views and reporting in Customer Journey Analytics. You can:

- Track propensity scores for a segment of users over time . Use case: Understand the likelihood of customers in a specific segment to convert. Example: A marketer at a hotel chain wants to understand the likelihood of a hotel customer to purchase a show ticket at the hotel’s concert venue.
- Analyze which success events or attributes are associated with propensity scores . Use case: Understand the attributes or success events associated with propensity scores. Example: A marketer at a hotel chain wants to understand how purchases of show tickets at a hotel’s concert venue are associated with propensity scores.
- Follow the entry flow for customer propensity over different scoring runs . Use case: Understand people who were initially low-propensity users and, over time, became high-propensity users. Example: A marketer at a hotel chain wants to understand which hotel customers initially were identified as customers with low propensity to purchase a show ticket, but over time became customers with high propensity to purchase a show ticket.
- Look at the distribution of propensity . Use case: Understand the distribution of propensity scores to be more precise in defining segments. Example: A retailer wants to run a specific promotion for $50 off a product. They may want to run only a very limited promotion due to budget, etc. They analyze the data and decide to target only the top 80%+ of their customers.
- Look at the propensity to accomplish an action for a particular cohort over time . Use case: Track a specific cohort over time. Example: A marketer at a hotel chain wants to track their bronze tier versus their silver tier, or silver tier versus their gold tier, over time. They can see each cohort’s propensity for booking the hotel over time.

To actually integrate Customer AI data with Customer Journey Analytics, follow these steps:

NOTE
Some of the steps are performed in Adobe Experience Platform prior to working with the output in Customer Journey Analytics.
## Step 1: Configure a Customer AI instance

Once you have prepared your data and have all your credentials and schemas in place, start by following the [Configure a Customer AI Instance](/en/docs/experience-platform/intelligent-services/customer-ai/user-guide/configure) guide in Adobe Experience Platform.

## Step 2: Set up a Customer Journey Analytics connection to Customer AI datasets

In Customer Journey Analytics, you can now [create one or more connections](/en/docs/analytics-platform/using/cja-connections/create-connection) to Experience Platform datasets that have been instrumented for Customer AI. Each prediction, such as “Likelihood to upgrade account”, equates to one dataset. These datasets appears with the “Customer AI Scores in EE Format – name_of_application” prefix.

IMPORTANT
Each Customer AI instance has two output datasets if the toggle is turned on to enable scores for Customer Journey Analytics during the configuration in Step 1. One output dataset appears in Profile XDM format and one in Experience Event XDM format.
Here is an example of an XDM schema that Customer Journey Analytics would bring in as part of an existing or new dataset:

(Note that the example is a profile dataset; the same set of schema object would be part of an Experience Event dataset that Customer Journey Analytics would grab. The Experience Event dataset would include timestamps as the score date.) Every customer scored in this model would have a score, a scoreDate, etc. associated with them.

## Step 3: Create data views based on these connections

In Customer Journey Analytics, you can now proceed to [create data views](/en/docs/analytics-platform/using/cja-dataviews/create-dataview) with the dimensions (such as score, score date, probability, and so on) and metrics that were brought in as part of the connection you established.

## Step 4: Report on CAI scores in Workspace

In Customer Journey Analytics Workspace, create a new project and pull in visualizations.

### Trend propensity scores

Here is an example of a Workspace project with CAI data that trends propensity scores for a segment of users over time, in ​a stacked bar chart:

### Table with reason codes

Here is a table that shows reason codes for why a segment has high or low propensity​:

### Entry flow for customer propensity

This flow diagram shows the entry flow for customer propensity over different scoring runs​:

### Distribution of propensity scores

This bar chart shows the distribution of propensity scores​:

### Propensity overlaps

This Venn diagram shows the propensity overlaps over different scoring runs:

recommendation-more-help
