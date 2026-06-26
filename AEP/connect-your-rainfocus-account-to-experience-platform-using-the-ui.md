---
title: "Connect your RainFocus account to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/analytics/rainfocus"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:01:54.440182+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Connect your RainFocus account to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The RainFocus source is in beta. See the
sources overview
for more information on using beta-labeled sources.
This tutorial provides steps on how to connect your RainFocus account and stream event management and analytics data to Adobe Experience Platform.

IMPORTANT
This source connector and documentation page are created and maintained by the RainFocus team. For any inquiries or update requests, please contact them directly at clientcare@rainfocus.com or visit the
RainFocus Help Center
## Getting started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

### Prerequisites

Before you can connect your RainFocus account to Experience Platform, you must first complete the following prerequisite tasks:

- [Gather required credentials](/en/docs/experience-platform/sources/connectors/analytics/rainfocus#gather-required-credentials)
- [Create an XDM schema and define the identity field](/en/docs/experience-platform/sources/connectors/analytics/rainfocus#create-an-xdm-schema-and-define-the-identity-field)
- [Create an Integration Profile in RainFocus](/en/docs/experience-platform/sources/connectors/analytics/rainfocus#create-an-integration-profile-in-rainfocus)

Once you have completed the prerequisite setup, you can then proceed to the steps outlined below.

## Connect your RainFocus account to Experience Platform

In the Experience Platform UI, select **Sources** from the left navigation bar to access the sources workspace. The *Catalog* screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Analytics* category, select **RainFocus Experience**, and then select **Add data**.

## Select data

The Select data step appears, providing an interface for you to select the data that you bring to Experience Platform.

- The left part of the interface is a browser that allows you to view the available data streams within your account;
- The right part of the interface lets you preview up to 100 rows of data from a JSON file.

Select **Upload files** to upload a JSON file from your local system. Alternatively, you can drag and drop the JSON file you want to upload into the Drag and drop files panel.

Upload the Sample JSON Payload downloaded from **RainFocus**.

Once your file uploads, the preview interface updates to display a preview of the schema you uploaded. The preview interface allows you to inspect the contents and structure of a file. You can also use the Search field utility to access specific items from within your schema.

When finished, select **Next**.

## Dataflow detail

The **Dataflow detail** step appears, providing you with options to use an existing dataset or establish a new dataset for your dataflow, as well as an opportunity to provide a name and description for your dataflow. During this step, you can also configure settings for Profile ingestion, error diagnostics, partial ingestion, and alerts.

When finished, select **Next**.

## Mapping mapping

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once your source data is successfully mapped, select **Next**.

## Review

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source file, and the amount of columns within that source file.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Get your streaming endpoint URL get-your-streaming-endpoint-url

With your streaming dataflow created, you can now retrieve your streaming endpoint URL. This endpoint will be used to subscribe to your webhook, allowing your streaming source to communicate with Experience Platform.

To retrieve your streaming endpoint, go to the *Dataflow activity* page of the dataflow that you just created and copy the endpoint from the bottom of the *Properties* panel.

## Activate your Integration Profile in RainFocus

Once your dataflow is complete and you have retrieved your streaming endpoint URL, you can now activate the Integration Profile in RainFocus.

- Log into the [RainFocus platform](https://app.rainfocus.com). In the primary navigation, select **Libraries** and **Integration Profiles**
- Open the Integration Profile that you created earlier as part of the [prerequisites](/en/docs/experience-platform/sources/connectors/analytics/rainfocus#create-an-integration-profile-in-rainfocus).
- Paste the **Dataflow ID** and **Streaming Endpoint** copied from the Dataflow in Experience Platform and select **Save**

## Next steps

By following this tutorial, you have established a connection for your RainFocus source, allowing you to stream your event management and analytics data to Experience Platform.

## Additional resources

The following documents provide additional guidance on nuances surrounding the RainFocus source.

- [RainFocus Help Center](https://help.rainfocus.com/hc/en-us)
- [Create an Adobe Service Account (JWT) in the Adobe Developer Portal](https://developer.adobe.com/developer-console/docs/guides/authentication/ServiceAccountIntegration/)
- [Create a Schema in the API](/en/docs/experience-platform/xdm/tutorials/create-schema-api)
- [Create a Schema in the UI](/en/docs/experience-platform/xdm/tutorials/create-schema-ui)
- [Define Identity Fields in the UI](/en/docs/experience-platform/xdm/ui/fields/identity)

recommendation-more-help
