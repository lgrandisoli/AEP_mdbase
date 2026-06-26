---
title: "Connect Snowflake to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/databases/snowflake"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:18.278708+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Ultimate]{class="badge positive"}

# Connect Snowflake to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
The Snowflake source is available in the sources catalog to users who have purchased Real-Time Customer Data Platform Ultimate.
Read this guide to learn how to connect your Snowflake account to Adobe Experience Platform using the user interface.

## Getting started

WARNING
Basic authentication (or account key authentication) for the Snowflake source will be deprecated on November 2025. You must move to key-pair based authentication in order to continue using the source and ingesting data from your database to Experience Platform. For more information on the deprecation, read the
Snowflake best practices guide on mitigating the risks of credential compromise
.
This tutorial requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

NOTE
You must set the
PREVENT_UNLOAD_TO_INLINE_URL
flag to
FALSE
to allow data unloading from your Snowflake database to Experience Platform.
## Navigate the sources catalog navigate

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Select **Snowflake** under the *Databases* category, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account exists, this option changes to
Add data
.
## Use an existing account existing

Next, you are taken to the authentication step of the sources workflow. Here, you can either use an existing account or create a new account.

To use an existing account, select the Snowflake account you want to connect with and then select **Next** to proceed.

## Create a new account create

If you do not have an existing account, then you must create a new account by providing the necessary authentication credentials that correspond with your source.

To create a new account, select **New account** and then provide a name and optionally add a description for your account.

### Connect to Experience Platform on Azure azure

You can connect your Snowflake account to Experience Platform on Azure with key-pair authentication.

To use key-pair authentication, select **KeyPair authentication**, provide values for your account, username, private key, private key passphrase, database, and warehouse, then select **Connect to source**.

With key-pair authentication, you must generate a 2048-bit RSA key pair and then provide the following values when creating an account for your Snowflake source.

Credential
Description
Account
An account name uniquely identifies an account within your organization. In this case, you must uniquely identify an account across different Snowflake organizations. To do this, you must prepend your organization name to the account name. For example:
orgname-account_name
. Read the guide on
retrieving your Snowflake account identifier
for additional guidance. For more information, refer to the
Snowflake documentation
.
Username
The username of your Snowflake account.
Private key
The Base64-encoded private key of your Snowflake account. You can generate either encrypted or unencrypted private keys. If you are using an encrypted private key, then you must also provide a private key passphrase when authenticating against Experience Platform. Read the guide on
retrieving your Snowflake private key
for more information.
Private key passphrase
The private key passphrase is an additional layer of security that you must use when authenticating with an encrypted private key. You are not required to provide the passphrase if you are using an unencrypted private key.
Database
The Snowflake database that contains the data you want to ingest to Experience Platform.
Warehouse
The Snowflake warehouse manages the query execution process for the application. Each Snowflake warehouse is independent from one another and must be accessed individually when bringing data over to Experience Platform.
For more information about these values, refer to [this Snowflake document](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).

### Connect to Experience Platform on AWS aws

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
To create a new Snowflake account and connect to Experience Platform on AWS, ensure that you are in a VA6 sandbox and then provide the necessary credentials for authentication.

Key-pair authentication
To connect using key-pairs, select **KeyPair Authentication**, provide your authentication credentials and then select **Connect to source**. For more information on these credentials, read the [Snowflake batch overview](/en/docs/experience-platform/sources/connectors/databases/snowflake#gather-required-credentials).

Basic authentication
| note warning |
| --- |
| WARNING |
| Basic authentication (or account key authentication) for the Snowflake source will be deprecated on November 2025. You must move to key-pair based authentication in order to continue using the source and ingesting data from your database to Experience Platform. For more information on the deprecation, read the [Snowflake best practices guide on mitigating the risks of credential compromise](https://www.snowflake.com/en/resources/white-paper/best-practices-to-mitigate-the-risk-of-credential-compromise/). |

To connect using a username and password combination, select **Basic authentication**, provide your authentication credentials and then select **Connect to source**. For more information on these credentials, read the [Snowflake batch overview](/en/docs/experience-platform/sources/connectors/databases/snowflake#gather-required-credentials).

### Skip preview of sample data skip-preview-of-sample-data

During the data selection step, you may encounter a timeout when ingesting large tables or files of data. You can skip data preview to circumvent the timeout and still view your schema, albeit without sample data. To skip data preview, enable the **Skip previewing sample data** toggle.

The rest of the workflow will remain the same. The only caveat is that skipping data preview may prevent calculated and required fields from being auto-validated during the mapping step, and you will then have to manually validate those fields during mapping.

## Next steps

By following this tutorial, you have established a connection to your Snowflake account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases).

recommendation-more-help
