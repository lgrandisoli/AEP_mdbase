---
title: "Create a Oracle NetSuite Activities source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/marketing-automation/oracle-netsuite-activities"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:03:36.652591+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Oracle NetSuite Activities source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Read the following tutorial to learn how to bring events data from your Oracle NetSuite Activities account to Adobe Experience Platform in the UI.

## Getting started getting-started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

If you already have a valid Oracle NetSuite account, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

TIP
Read the
Oracle NetSuite overview
for information on how to retrieve your authentication credentials.
## Connect your Oracle NetSuite account connect-account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Marketing Automation* category, select **Oracle NetSuite Activities**, and then select **Add data**.

The **Connect Oracle NetSuite Activities account** page appears. On this page, you can either use new credentials or existing credentials.

IMPORTANT
The refresh token expires after seven days. Once your token expire, you must create account on Experience Platform with your updated token. If you do not create a new account with your updated token, you may see the following error message:
The request could not be processed. Error from flow provider: The request could not be processed. Rest call failed with client error, status code 401 Unauthorized, please check your activity settings.
### Existing account existing-account

To use an existing account, select the Oracle NetSuite Activities account you want to create a new dataflow with, then select **Next** to proceed.

### New account new-account

If you are creating a new account, select **New account**, and then provide a name, an optional description, and your credentials. When finished, select **Connect to source** and then allow some time for the new connection to establish.

## Next steps next-steps

By following this tutorial, you have established a connection to your Oracle NetSuite Activities account. You can now continue on to the next tutorial and [configure a dataflow to bring data into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation).

## Additional resources additional-resources

The sections below provide additional resources that you can refer to when using the Oracle NetSuite Activities source.

### Mapping mapping

Experience Platform provides intelligent recommendations for auto-mapped fields based on the target schema or dataset that you selected. You can manually adjust mapping rules to suit your use cases. Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapper interface and calculated fields, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

NOTE
The fields displayed are dependent on the subscriptions that your Oracle NetSuite account has access to. For example, if you do not have access to billing, then you will not see the billing related fields.
### Scheduling scheduling

When scheduling your Oracle NetSuite Activities dataflow for ingestion, you must select the following frequency and interval configuration:

Frequency
Interval
Once
1
While retrieving data, the Oracle NetSuite responds with the last modified or created date as a date format instead of a timestamp. Hence, the scheduling is limited to one day.

Once your have provided the values for your schedule, select **Next**.

recommendation-more-help
