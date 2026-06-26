---
title: "Data Ingestion overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/home"
category: "overview"
topic: "experience-platform/data-ingestion-guide"
created_at: "2026-05-29T16:54:58.457129+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Ingestion Guide

# Data Ingestion overview

Last update: May 23, 2026
- Topics:
- [Data Ingestion](#)

CREATED FOR:

- Developer

In Adobe Experience Platform, data ingestion is the transportation of data from assorted sources to a storage medium where it can be accessed, used, and analyzed by an organization. Data ingestion in Experience Platform can be grouped into two main categories: **streaming ingestion** and **batch ingestion**.

Under streaming and batch ingestion are a number of different methods that you can use to ingest your data into Experience Platform. These methods include the use of a variety of **sources** and connecting to these sources to then bring data into Experience Platform.

Read this document for an overview of the many different ways that data can be ingested into Experience Platform.

## Streaming ingestion streaming

You can use streaming ingestion to send data from client and server-side devices to Experience Platform in real-time. Experience Platform supports the use of data inlets to stream incoming experience data, which is persisted in streaming-enabled datasets within the data lake. Data inlets can be configured to automatically authenticate the data they collect, ensuring that the data is coming from a trusted source.

For more information, read the [streaming ingestion overview](/en/docs/experience-platform/ingestion/streaming/overview).

## Batch ingestion batch

In Experience Platform, a batch is a set of data collected over a period of time and processed together as a single unit. Datasets are made up of batches. You can use batch ingestion to ingest data into Experience Platform as batch files. Once ingested, batches provide metadata that describes the number of records successfully ingested, as well as any failed records and associated error messages.

Manually uploaded datafiles such as flat CSV files (mapped to XDM schemas) and parquet files must be ingested using this method.

For more information, read the [batch ingestion overview](/en/docs/experience-platform/ingestion/batch/overview).

## Sources sources

You can also ingest data by connecting to Experience Platform Sources. Experience Platform maintains a catalog of a variety of different data sources that you can connect to and ingest data from. These sources can be native Adobe applications such as the Adobe Analytics source or the Marketo Engage source. You can also connect to third-party sources such as the Amazon S3 source and the Google Cloud Storage source.

Sources are grouped into different categories like cloud storages, databases, and CRM systems. A given source may support batch or streaming ingestion.

With sources, you can ingest data from a number of different data sources, and of varying different use case categories. Additionally, data ingestion via a source gives you the opportunity to authenticate against the external data source, configure an ingestion schedule, and manage ingestion throughput.

For more information, read the [sources overview](/en/docs/experience-platform/sources/home) for more information.

### ML-Assisted schema creation ml-assisted-schema-creation

To quickly integrate new data sources, you can now use machine learning algorithms to generate a schema from sample data. This automation simplifies the creation of accurate schemas, reduces errors, and speeds up the process from data collection to analysis and insights.

See the [ML-assisted schema creation guide](/en/docs/experience-platform/xdm/ui/ml-assisted-schema-creation) for more information on this workflow.

## Data Prep data-prep

While data prep is not a method of ingestion, it is an important part of the data ingestion process. Use data prep functions to map, transform, and validate data to and from Experience Data Model (XDM) before creating a dataflow to ingest your data to Experience Platform. Data prep appears as the “Mapping” step in the Experience Platform user interface during the data ingestion process.

For more information, read the [data prep overview](/en/docs/experience-platform/data-prep/home).

## Streaming ingestion methods streaming-ingestion-methods

The following table outlines the variety of methods that you can use to ingest streaming data to Experience Platform.

Streaming Sources
Method
Common Use Cases
Protocols
Considerations
Adobe Web/Mobile SDK
- Data collection from websites and mobile apps.
- Preferred method for client side collection.

Push, HTTP, JSON
- Implement multiple Adobe applications leveraging a single SDK.

HTTP API Connector
- Collection from streaming sources, transactions, relevant customer events and signals.

Push, REST API, JSON
- Raw or XDM data is streamed directly to the hub, with no real-time Edge segmentation or event forwarding.

Edge Network API
- Collection from streaming sources, transactions, relevant customer events and signals from the globally distributed Edge Network.

Push, REST API, JSON
- Data is streamed through the Edge Network. Support for real-time segmentation and event forwarding on the Edge.

Adobe Applications
- Data ingestion from applications like Adobe Analytics, Marketo Engage, Adobe Campaign Managed Services, Adobe Target, Adobe Audience Manager

Push, Source Connectors and API
- The recommended approach is to migrate to the Web/Mobile SDK instead of using traditional application SDKs.

Streaming Sources
- Ingestion of an enterprise event stream, typically used for sharing enterprise data to multiple downstream applications.

Push, REST API, JSON
- Data is streamed in JSON format and can be mapped to XDM schema.

[Streaming Sources SDK](/en/docs/experience-platform/sources/sdk/streaming-sdk/getting-started)

- Use the self-service capabilities of Self-Serve Sources Streaming SDK to integrate your own data source to the Experience Platform sources catalog.

Push, HTTP API, JSON
- Examples of partner-integrated streaming sources include: Braze, Pendo, and RainFocus.

## Batch ingestion methods batch-ingestion-methods

The following table outlines the variety of methods that you can use to ingest batch data to Experience Platform.

Batch Sources
Method
Common Use Cases
Protocols
Considerations
Batch Ingestion API
- Ingestion from an enterprise managed queue. Use batch ingestion if your data needs to be prepared and formatted prior to ingestion.

Push, JSON or Parquet
- Must manage batches and files for ingestion.

Batch Sources
- Common approach for ingestion of data from cloud storage, CRM, and marketing automation applications.
- Ideal for ingesting large amounts of historical data.

Pull, CSV, JSON, Parquet
- Source ingestion based on pre-configured scheduled intervals.

Data Landing Zone
- Adobe-provisioned cloud-based file storage. You have access to one Data Landing Zone container per sandbox.
- Push your files to the Data Landing Zone for later ingestion into Experience Platform.

Push, CSV, JSON, Parquet
- Experience Platform enforces a strict seven-day expiration time on all files and folders uploaded to a Data Landing Zone container. All files and folders are deleted after seven days.

Batch Sources SDK
- Use the self-service capabilities of Self-Serve Sources Batch SDK to integrate your own data source to the Experience Platform sources catalog.
- Ideal for partner connectors or for a tailored workflow experience for setting up an enterprise connector.

Pull, REST API, CSV or JSON
- Examples of partner-integrated batch sources include: Mailchimp, OneTrust, Zendesk

## Next steps and additional resources

This document provided a brief introduction to the different aspects of Data Ingestion in Experience Platform. Please continue to read the overview documentation for each ingestion method to familiarize yourself with their different capabilities, use cases, and best practices. You can also supplement your learning by watching the ingestion overview video below. For information on how Experience Platform tracks the metadata for ingested records, see the [Catalog Service overview](/en/docs/experience-platform/catalog/home).

WARNING
The term “Unified Profile” thats used in the following video is out-of-date. The terms “Profile” or “Real-Time Customer Profile” are the correct terms used in the Experience Platform documentation. Please refer to the documentation for the latest functionality.
https://video.tv.adobe.com/v/27106?quality=12&learn=on
https://video.tv.adobe.com/vc/27106/eng.json
recommendation-more-help
