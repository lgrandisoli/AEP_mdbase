---
title: "Query Service overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/query/home"
category: "overview"
topic: "experience-platform/query-service-guide"
created_at: "2026-05-29T16:54:32.167860+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Query Service Guide

# Query Service overview

Last update: May 23, 2026
- Topics:
- [Queries](#)

CREATED FOR:

- User
- Developer

Adobe Experience Platform ingests data from a wide variety of sources. A major challenge for marketers is to make sense of this data to gain insights about their customers. To query data in Experience Platform, you can use standard SQL and Adobe Experience Platform Query Service. You can use Query Service to join any dataset in the data lake and capture the query results as a new dataset for use in reporting, machine learning, or for ingestion into Real-Time Customer Profile. This document provides an overview of the role of Query Service within Experience Platform.

You can use Query Service to connect the online-to-offline customer journey and understand omni-channel attribution for your brand. The following video shows how an experience business can use Query Service to address key use cases and explains how Query Service works.

https://video.tv.adobe.com/v/29795?quality=12&learn=on
https://video.tv.adobe.com/vc/29795/eng.json
## Using Query Service usage

To analyze your data, create and execute SQL queries with either the Query Service user interface or the RESTful API.With the Query Service UI you can write, execute, and schedule queries, view previously executed queries, and access queries saved by users within your organization. You can also test out your queries before executing them on your wider dataset with the Query Editor. See the [Query Service UI guide] (ui/overview.md) for an overview of the UI functionality.

The RESTful API provides a similar experience. You can use the Query Service API to programmatically write and execute queries, create and save templates for queries that you wish to adapt, or schedule queries for automated execution. See the [Query Service developer guide](/en/docs/experience-platform/query/api/getting-started) for more information on using the Query Service API.

To quickly get started using Query Service features, you are recommended to read the following documents:

- [General guidance for query execution](/en/docs/experience-platform/query/best-practices/writing-queries)
- [SQL syntax in Query Service](/en/docs/experience-platform/query/sql/syntax)
- [Create derived datasets with SQL](/en/docs/experience-platform/query/data-distiller/derived-datasets/create-derived-datasets-with-sql)

## Query Service and Experience Platform services experience-platform-services

Query Service interacts and can be used with multiple Experience Platform services. To make the most out of Query Service’s capabilities, you should become familiar with these services and how they interact with Query Service. The [Experience Platform documentation landing page] (https://experienceleague.adobe.com/docs/experience-platform.html) provides summaries and links to the platform’s capabilities.

### Data Science Workspace data-science-workspace

Adobe Experience Platform Data Science Workspace uses machine learning and artificial intelligence to gain insights from data stored within Experience Platform. Data scientists can use the [IDNL Data Science Workspace] to build recipes based on record and time-series data about customers and their activities. These recipes facilitate predictions such as buying propensity and recommended offers that the individual is likely to appreciate and use. You can use SQL within Data Science Workspace by integrating Query Service into JupyterLab to explore, transform, and analyze Adobe Analytics data. Read the [Data Science Workspace overview](/en/docs/experience-platform/data-science-workspace/home) and the [Jupyter Notebook connection guide](/en/docs/experience-platform/query/clients/jupyter-notebook) for more information about how Data Science Workspace interacts with Query Service.

### Segmentation Service segmentation

Use the Adobe Experience Platform Segmentation Service to divide your customers into smaller groups that share similar traits. These audiences can then be evaluated to provide better analysis on your Real-Time Customer Profile data. You can use Query Service to run queries on this audience data within the data lake and provide the analysis. Read the [Segmentation Service overview](/en/docs/experience-platform/segmentation/home) and the [Profile Query Language (PQL) guide](/en/docs/experience-platform/segmentation/pql/overview) for more information on how to analyze audiences.

## Use cases use-cases

Query Service provides a flexible approach to your data processing that serves many purposes. Among others, it can ease the burden of segmentation from marketers, and help generate actionable audiences and meaningful business insights. The following use cases offer more in-depth examples of the power of Query Service.

### Adobe Analytics browse abandonment abandon-browse

This [browse abandonment example centers on using Adobe Analytics](/en/docs/experience-platform/query/use-cases/abandoned-browse) data to create a particular actionable audience. Query Service accommodates complex logic for segmentation to calculate various personalized attributes for use downstream, or to greatly simplify how you build out your audiences.

## Generate insights with custom dashboards custom-dashboards

With Adobe Experience Platform, you can ingest, store, structure, and pull all stored datasets—including behavioral, CRM, and point-of-sale data. Using Query Service, you can query these datasets and answer specific business questions, generating impactful insights. Learn how to build and manage custom dashboards where you can create, add, and edit bespoke widgets to visualize key metrics with [user-defined dashboards](/en/docs/experience-platform/dashboards/standard-dashboards). You can also [customize your own Real-Time CDP reports](/en/docs/experience-platform/dashboards/data-models/cdp-insights-data-model-b2c) for your marketing and KPI use cases by using SQL queries with Real-Time Customer Data Platform Insights Data Models.

## Next steps and additional resources

By reading this document, you have been introduced to Query Service and how it functions within the greater scope of Experience Platform. To continue learning about Query Service features, you are recommended to read the following documents:

- The [Query Service developer guide](/en/docs/experience-platform/query/api/getting-started): For more information on interacting with various endpoints within the Query Service API.
- The [Query Service user interface guide](/en/docs/experience-platform/query/ui/overview): For more information on using the Query Editor and UI.
- The [Query Service clients overview](/en/docs/experience-platform/query/clients/overview): For a comprehensive list of external clients to connect with Query Service.

To better prepare yourself to run queries, watch the following video. This video shares tips and best practices for running queries in the query editor interface, PSQL clients, business intelligence (BI) solutions, and the HTTP API.

https://video.tv.adobe.com/v/29811?quality=12&learn=on
https://video.tv.adobe.com/vc/29811/eng.json
recommendation-more-help
