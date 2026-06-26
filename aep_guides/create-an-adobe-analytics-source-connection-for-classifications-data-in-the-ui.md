---
title: "Create an Adobe Analytics source connection for classifications data in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/classifications"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:24:41.392921+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Adobe Analytics source connection for classifications data in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

TIP
By default, Adobe Analytics classifications data is updated weekly. Data ingestion for your classifications data will be processed seven days after the initial set up of your dataflow. The first load ingests the entire data and the ensuing weekly ingestion runs incremental data.
Read this tutorial for steps on how to ingest your Adobe Analytics classifications data into Adobe Experience Platform through the user interface.

## Get started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- [Experience Data Model (XDM) System](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

The Analytics classifications source connector requires your data to have been migrated to the new classifications infrastructure of Adobe Analytics prior to use. To confirm the migration status of your data, please contact your Adobe account team.

## Select your classifications

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Adobe applications* category, select **Adobe Analytics**, and then select **Set up**.

TIP
Sources in the sources catalog display the
Set up
option if there is no authenticated account. Once an account is authenticated, the option changes to
Add data
.
Next, select Classifications and then select the classifications datasets that you want to ingest to Experience Platform. Alternatively, you can use search to filter and select for specific classifications.

You can select up to 30 different classifications datasets to bring into Experience Platform. Any datasets that you select will appear in the right rail. When you are finished, select Next to proceed.

## Review your classifications

The **Review** step appears, allowing you to review your selected classifications datasets before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source platform and the status of the connection.
- **Data type**: Shows the number of selected classifications.
- **Scheduling**: Shows the frequency of synchronization for classifications data. **Note**: Classifications data is updated on a weekly basis.

Once you have reviewed your dataflow, click **Finish** and allow some time for the dataflow to be created.

## Next steps

By following this tutorial, you have created an Analytics classifications sata connector that brings classifications data into Experience Platform. See the following documents for more information on Analytics and classifications data:

- [Adobe Analytics source connector overview](/en/docs/experience-platform/sources/connectors/adobe-applications/analytics)
- [Create an Analytics source connection for report suite data in the UI](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics)
- [About classifications](/en/docs/analytics/components/classifications/c-classifications)

recommendation-more-help
