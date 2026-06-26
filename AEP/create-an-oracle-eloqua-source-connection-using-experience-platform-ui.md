---
title: "Create an Oracle Eloqua source connection using Experience Platform UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/marketing-automation/oracle-eloqua"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:07:59.062284+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Oracle Eloqua source connection using Experience Platform UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

WARNING
The Oracle Eloqua source will be deprecated in January 2026. A new source will be released later this year as an alternative. Once the new source is released, you must plan to migrate to the new source by creating new account connections and dataflows before the end of January 2026.
This tutorial provides steps for creating an Oracle Eloqua source connection using the Adobe Experience Platform user interface.

## Getting started

This guide requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

If you already have an authenticated Oracle Eloqua account on Experience Platform, then you may skip the remainder of this document and proceed to the tutorial on [creating a dataflow to bring marketing automation data to Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

### Gather required credentials

In order to connect Oracle Eloqua to Experience Platform, you must provide values for the following authentication properties:

Credential
Description
Endpoint
The endpoint of your Oracle Eloqua server. Oracle Eloqua supports multiple data centers. To find your endpoint, login to the
Oracle Eloqua interface
with your credentials and then copy the base URL portion from the redirect URL. The format for your URL pattern is
xxx.xx.eloqua.com
and should be entered without
http
or
https
.
Username
The username of your Oracle Eloqua server. The username must be formatted as
siteName + \\ + username
, where
siteName
is the company name you used to log in to Oracle Eloqua and
username
is your username. For example, your log in username can be:
Eloqua\Andy
.
Note
: You must use a single backslash (
\
)when using the UI because Experience Platform UI automatically adds an additional backslash (
\
) when entering a username.
Password
The password corresponding to your Oracle Eloqua username.
For more information on authentication credentials for Oracle Eloqua, see the [Oracle Eloqua guide on authentication](https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Authentication_Basic.html).

Once you have gathered your required credentials, you can follow the steps below to link your Oracle Eloqua account to Experience Platform.

## Connect your Oracle Eloqua account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Marketing automation category, select **Oracle Eloqua**, and then select **Add data**.

The **Connect Oracle Eloqua account** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To use an existing account, select the Oracle Eloqua account you want to create a new dataflow with, then select **Next** to proceed.

### New account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and the appropriate values for your Oracle Eloqua credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps

By following this tutorial, you have authenticated and created a source connection between your Oracle Eloqua account and Experience Platform. You can now continue on to the next tutorial and [create a dataflow to bring marketing automation data to Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

recommendation-more-help
