---
title: "Source connectors overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/home"
category: "overview"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T16:54:30.377771+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Source connectors overview

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Adobe Experience Platform allows data to be ingested from external sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services. You can ingest data from a variety of sources such as Adobe applications, cloud-based storages, databases, and many others.

Flow Service is used to collect and centralize customer data from various disparate sources within Experience Platform. The service provides a user interface and RESTful API that lets you set-up source connections to various data providers with ease. These source connections enable you to authenticate your third-party systems, set times for ingestion runs, and manage data ingestion throughput.

With Experience Platform, you can centralize data you collect from disparate sources and use the insights gained from it to do more.

recs-overview-body-1
recs-overview-body-2
recs-overview-body-3
recs-overview-body-4
recs-overview-body-5
recs-overview-body-6
## Adobe-built and partner-built sources adobe-and-partner-built-sources

Some of the connectors in the Experience Platform sources catalog are built and maintained by Adobe, while others are built and maintained by partner companies by using [Sources SDK](/en/docs/experience-platform/sources/sdk/overview). A note at the top of the documentation page for each partner-built connector calls out if a source is created and maintained by the partner. For example, the [Amazon S3 connector](/en/docs/experience-platform/sources/connectors/cloud-storage/s3) is created by Adobe, while the [RainFocus connector](/en/docs/experience-platform/sources/connectors/analytics/rainfocus) is created and maintained by the RainFocus team.

For partner-authored and maintained connectors, this means that issues with the connector might need to be resolved by the partner team (contact method provided in the note in the documentation page). For issues with Adobe-authored and maintained connectors, contact your Adobe representative or Customer Care.

style
shade-box
## Sources catalog

NOTE
Source ingestion dataflows that fail continuously for 30 days will automatically be disabled. Use
Monitoring Dashboard
to review your dataflow, identify why it failed (for example, credentials, permissions, or schema or mapping changes), apply the necessary updates, and re-enable the dataflow once resolved.
Read the following sections for a list of all sources available in the sources catalog.

### Adobe applications adobe-applications

Experience Platform allows data to be ingested from other Adobe applications, including Adobe Analytics, and Adobe Audience Manager. Read the following related documents for more information:

- Adobe Audience Manager Create an Adobe Audience Manager source connection in the UI
- Adobe Analytics Classifications Data Create an Adobe Analytics Classifications Data source connection in the UI
- Adobe Analytics Report Suite Data Create an Adobe Analytics source connection in the UI
- Adobe Campaign Managed Cloud Services Create an Adobe Campaign Managed Cloud Services source connection in the UI
- Adobe Commerce
- Adobe Data Collection Create a Customer Attributes source connection in the UI
- Marketo Engage Create a Marketo Engage source connection in the UI Create a Marketo Engage source connection and dataflow for custom activity data

### Advanced enterprise sources advanced-enterprise-sources

The following sources are only available to [Adobe Real-Time Customer Data Platform Ultimate](https://helpx.adobe.com/legal/product-descriptions/real-time-customer-data-platform-b2c-edition-prime-and-ultimate-packages.html) or customers who have licensed the standalone Advanced Enterprise Source Connectors SKU.

Source
Category
Ingestion type
Cloud
Amazon Kinesis
Cloud storage
Streaming
Azure, AWS
Amazon Redshift
Database
Batch
Azure, AWS
Azure Databricks
Database
Batch
Azure
Azure Event Hubs
Cloud Storage
Streaming
Azure, AWS
Azure Synapse Analytics
Database
Batch
Azure
Google BigQuery
Database
Batch
Azure, AWS
Google PubSub
Cloud Storage
Streaming
Azure
Snowflake
Database
Streaming
Azure, AWS
Snowflake
Database
Batch
Azure, AWS
### Advertising advertising

You can use the following sources to ingest advertising data to Experience Platform.

Source
Ingestion type
Cloud
Google Ads
Batch
Azure
### Analytics analytics

You can use the following sources to ingest analytics data to Experience Platform.

Source
Ingestion type
Cloud
Mixpanel
Batch
Azure
Pendo
Streaming
Azure
RainFocus
Streaming
Azure
### Cloud Storage cloud-storage

Cloud storage sources can bring your own data into Experience Platform without the need to download, format, or upload. Ingested data can be formatted as XDM JSON, XDM Parquet, or delimited. Every step of the process is integrated into the Sources workflow using the user interface. See the following related documents for more information:

You can use the following sources to ingest cloud storage data to Experience Platform.

Source
Ingestion type
Cloud
Azure Data Lake Storage Gen2
Batch
Azure
Azure Blob Storage
Batch
Azure
Amazon S3
Batch
Azure, AWS
Apache HDFS
Batch
Azure
Azure File Storage
Batch
Azure
Data Landing Zone
Batch
Azure, AWS
FTP
Batch
Azure
Google Cloud Storage
Batch
Azure
Oracle Object Storage
Batch
Azure
SFTP
Batch
Azure
### Consent and Preferences consent

You can use the following sources to ingest consent and preferences data to Experience Platform.

Source
Ingestion type
Cloud
Didomi
Streaming
Azure
OneTrust Integration
Batch
Azure
### Customer Relationship Management (CRM) customer-relationship-management

CRM systems provide data that can help build customer relationships, which in turn, create loyalty and drive customer retention. Experience Platform provides support for ingesting CRM data from Microsoft Dynamics 365 and Salesforce. See the following related documents for more information:

You can use the following sources to ingest CRM data to Experience Platform.

Source
Ingestion type
Cloud
Microsoft Dynamics
Batch
Azure
Salesforce
Batch
Azure, AWS
SugarCRM
Batch
Azure
Veeva CRM
Batch
Azure
### Customer Success customer-success

You can use the following sources to ingest customer success data to Experience Platform.

Source
Ingestion type
Cloud
Salesforce Service Cloud
Batch
Azure
ServiceNow
Batch
Azure
Zendesk
Batch
Azure
### Database database

Experience Platform provides support for ingesting data from a third-party database. See the following related documents for more information on specific source connectors:

You can use the following sources to ingest data from your database to Experience Platform.

Source
Ingestion type
Cloud
Apache Hive on Azure HDInsights
Batch
Azure
Apache Spark on Azure HDInsights
Batch
Azure
Azure Data Explorer
Batch
Azure
Azure Table Storage
Batch
Azure
GreenPlum
Batch
Azure
HP Vertica
Batch
Azure
IBM DB2
Batch
Azure
MariaDB
Batch
Azure
Microsoft SQL Server
Batch
Azure
MySQL
Batch
Azure, AWS
Oracle
Batch
Azure, AWS
PostgreSQL
Batch
Azure, AWS
Teradata Vantage
Batch
Azure
### Data & Identity Partners data-partner

You can use the following sources to ingest data and identity partner data to Experience Platform.

Source
Ingestion type
Cloud
Acxiom Data Ingestion
Batch
Azure
Acxiom Prospecting Data Import
Batch
Azure
Algolia User Profiles
Batch
Azure
Bombora Intent
Batch
Azure
Demandbase Intent
Batch
Azure
Merkury Enterprise Identity Resolution
Batch
Azure
### e-commerce ecommerce

You can use the following sources to ingest e-commerce data to Experience Platform.

Source
Ingestion type
Cloud
SAP Commerce
Batch
Azure
Shopify
Batch
Azure
Shopify
Streaming
Azure
### Local system local-system

You can use the following sources to ingest data from your local system to Experience Platform.

Source
Ingestion type
Cloud
Local file upload
Batch
Azure
### Loyalty loyalty

You can use the following sources to ingest loyalty data to Experience Platform.

Source
Ingestion type
Cloud
Capillary Streaming Events
Streaming
Azure
LAVA
Streaming
Azure
Talon.One
Batch, Streaming
Azure
### Marketing Automation marketing-automation

You can use the following sources to ingest marketing automation data to Experience Platform.

Source
Ingestion type
Cloud
Braze
Streaming
Azure
Chatlio
Streaming
Azure
Customer.io
Streaming
Azure
HubSpot
Batch
Azure
Mailchimp
Batch
Azure
Oracle Eloqua (V2)
Batch
Azure
Oracle NetSuite
Batch
Azure
PathFactory
Batch
Azure
Relay Connector
Streaming
Azure
Salesforce Marketing Cloud (V2)
Batch
Azure
### Payments payments

You can use the following sources to ingest payments data to Experience Platform.

Source
Ingestion type
Cloud
Square
Batch
Azure
Stripe
Batch
Azure
### Streaming streaming

You can use the following sources to stream data to Experience Platform.

Source
Ingestion type
Cloud support
HTTP API
Streaming
Azure, AWS
### Protocols protocols

You can use the following sources to ingest protocol data to Experience Platform.

Source
Ingestion type
Cloud support
Generic OData
Batch
Azure
Generic REST API
Batch
Azure
## Access control for sources in data ingestion

Permissions for sources in data ingestion can be managed within the Adobe Admin Console. You can access permissions through the **Permissions** tab in a particular product profile. From the **Edit Permissions** panel, you can access the permissions pertaining to sources through the **data ingestion** menu entry. The **View Sources** permission grants read-only access to available sources in the **Catalog** tab and authenticated sources in the **Browse** tab, while the **Manage Sources** permission grants full access to read, create, edit, and disable sources.

The following table outlines how the UI behaves based on different combinations of these permissions:

Permission level
Description
View Sources
On
Grant read-only access to sources in each source-type in the Catalog tab, as well as the Browse, Accounts, and Dataflow tabs.
Manage Sources
On
In addition to the functions included in
View Sources
, grants access to
Connect Source
option in
Catalog
and to
Select Data
option in
Browse
.
Manage Sources
also allows you to enable or disable
DataFlows
and edit their schedules.
View Sources
Off and
Manage Sources
Off
Revoke all access to sources.
For more information about the available permissions granted through Adobe Permissions, read the [access control overview](/en/docs/experience-platform/access-control/home).

### Attribute-based access control

Attribute-based access control in Adobe Experience Platform allows administrators to control access to specific objects and/or capabilities based on attributes.

With attribute-based access control, you can apply mapping configurations to fields that you have permissions to. Furthermore, you cannot ingest data to a dataset if you do not have access to all fields in the dataset.

#### Support for attribute-based access control in sources

TIP
Attribute-based access control works as follows:
roles
are created to categorize the types of users that interact with your Experience Platform instance.
Labels
are applied to
roles
to designate the access of that given role.
Labels
are also applied to resources like schema fields and segments. In order for a user to have access to certain schema fields and segments, they must be added to
a role with the same label that is assigned to the queried resource
. For more information, read the
attribute-based access control end-to-end guide
.
- Apply labels to schema fields to define access to specific schema fields in your organization. Once access to specific schema fields are established, users will only be able to create mappings for the fields that they have access to.
- Users without the appropriate roles will not be able to create or update dataflows with mappings that involve inaccessible schema fields. Furthermore, unauthorized users cannot update, delete, enable, or disable existing dataflows with inaccessible schema fields.
- Additionally, a dataflow must have the exact same schema ID and version in its mapping, target dataset, and target connection. This applies to both standard XDM schemas and relational schemas.

NOTE
Relational schemas have additional requirements including primary key and version identifier fields. For more information, see the
relational schema overview
.
For more information on attribute-based access control, read the [attribute-based access control overview](/en/docs/experience-platform/access-control/abac/overview).

## Terms and conditions terms-and-conditions

By using any of the Sources labeled as beta (“Beta”), You hereby acknowledge that the Beta is provided *“as is” without warranty of any kind*.

Adobe shall have no obligation to maintain, correct, update, change, modify, or otherwise support the Beta. You are advised to use Informative and not to rely in any way on the correct functioning or performance of such Beta and/or accompanying materials. The Beta is considered Confidential Information of Adobe.

Any “Feedback” (information regarding the Beta including but not limited to problems or defects you encounter while using the Beta, suggestions, improvements, and recommendations) provided by You to Adobe is hereby assigned to Adobe including all rights, title, and interest in and to such Feedback.

Submit Open Feedback or create a Support Ticket to share your suggestions or report a bug, seek a feature enhancement.

recommendation-more-help
