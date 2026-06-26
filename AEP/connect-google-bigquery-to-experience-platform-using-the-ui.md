---
title: "Connect Google BigQuery to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/bigquery"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:02:19.905155+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Connect Google BigQuery to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Google BigQuery source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this tutorial to learn how to connect your Google BigQuery account to Adobe Experience Platform using the user interface.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Google BigQuery connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

### Gather required credentials

Read the [Google BigQuery authentication guide](/en/docs/experience-platform/sources/connectors/databases/bigquery#prerequisites) for detailed steps on gathering your required credentials.

## Navigate the sources catalog navigate

In the Experience Platform UI, select **Sources** from the left navigation to access the *Sources* workspace. You can select the appropriate category in the *Categories* panel Alternatively, you can use the search bar to navigate to the specific source that you want to use.

To use Google BigQuery, select the **Google BigQuery** source card under *Databases* and then select **Add data**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account is created, this option changes to
Add data
.
## Use an existing account existing

To use an existing account, select the Google BigQuery account you want to connect with, then select **Next** to proceed.

## Create a new account create

If you do not have an existing account, then you must create a new account by providing the necessary authentication credentials that correspond with your source.

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform on Azure azure

You can connect your Google BigQuery account to Experience Platform on Azure using either basic or service authentication.

Use basic authentication
To use basic authentication, select **Basic Authentication** and provide values for your [project, client ID, client secret, refresh token, and (optional) large results dataset ID](/en/docs/experience-platform/sources/connectors/databases/bigquery#generate-your-google-bigquery-credentials). When finished, select **Connect to source** and allow for a few moments for the connection to establish.

Use service authentication
To use service authentication, select **Service Authentication** and provide values for your [project ID, key file content, and (optional) large results dataset ID](/en/docs/experience-platform/sources/connectors/databases/bigquery#generate-your-google-bigquery-credentials). When finished, select **Connect to source** and allow for a few moments for the connection to establish.

### Connect to Experience Platform on Amazon Web Services (AWS) aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
To create a new Google BigQuery account and connect to Experience Platform on AWS, ensure that you are in a VA6 sandbox and then provide the necessary credentials for authentication.

- **Project ID**: The project ID that corresponds with your Google BigQuery account.
- **Key file content**: The key file that is used to authenticate the service account. You can retrieve this value from the [Google Cloud service accounts dashboard](https://console.cloud.google.com). The key file content is in JSON format. You must encode this in Base64 when authenticating to Experience Platform.
- **Dataset ID**: The Google BigQuery dataset ID. This ID represents where your data tables are located and must be pre-created to enable support for large result sets.

## Skip preview of sample data skip-preview-of-sample-data

During the data selection step, you may encounter a timeout when ingesting large tables or files of data. You can skip data preview to circumvent the timeout and still view your schema, albeit without sample data. To skip data preview, enable the **Skip previewing sample data** toggle.

The rest of the workflow will remain the same. The only caveat is that skipping data preview may prevent calculated and required fields from being auto-validated during the mapping step, and you will then have to manually validate those fields during mapping.

## Next steps

By following this tutorial, you have established a connection to your Google BigQuery account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
