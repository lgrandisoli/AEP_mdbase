---
title: "On-demand ingestion for sources dataflows in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/on-demand-ingestion"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:33:55.050309+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# On-demand ingestion for sources dataflows in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

You can use on-demand ingestion to trigger a flow run iteration of an existing dataflow using the sources workspace in the Adobe Experience Platform user interface.

This document provides you with steps on how to create dataflows on demand for sources, as well as how to retry flow runs that have been processed or have failed.

**What is a flow run?**

Flow runs represent an instance of dataflow execution. For example, if a dataflow is scheduled to run hourly at 9:00 AM, 10:00 AM, and 11:00 AM, then you would have three instances of a flow run. Flow runs are specific to your particular organization.

style
shade-box
## Getting started

NOTE
In order to create a flow run, you must first have the flow ID of a dataflow that is scheduled for one-time ingestion.
This document requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Dataflows](/en/docs/experience-platform/dataflows/home): A dataflow is a representation of data jobs that move data across Experience Platform. Dataflows are configured across different services, helping move data from source connectors to target datasets, to Identity Service and Real-Time Customer Profile, and to Destinations.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes that partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Create a dataflow on demand create-a-dataflow-on-demand

Navigate to the *Dataflows* tab of the sources workspace. From here, find the dataflow that you want to run on demand, and then select the ellipses (**...**) beside your dataflow name.

Next, select **Run on-demand** from the dropdown menu that appears.

Configure the schedule of your on-demand ingestion. Select the **Ingestion start time**, the **Date range start time**, and the **Date range end time**.

Scheduling configuration
Description
Ingestion start time
The scheduled time of when the on-demand flow run will begin.
Date range start time
The earliest date and time that data will be retrieved from.
Date range end time
The date and time that data will be retrieved up to.
Select **Schedule** and allow a few moments for your on-demand dataflow to trigger.

Select your dataflow name to view your dataflow activity. Here you will see a list of your dataflow runs that have been processed. You can re-run individual iterations of your dataflow runs regardless of whether they have failed or succeeded. For run iterations that have failed, you can use **Retry** to initiate the run again after diagnosing and addressing any errors that may have been encountered during the creation process.

TIP
Retrying a flow run will only process files with timestamps that fall within the range of the original run.
Select **Scheduled** to see a list of dataflow runs that are scheduled for future ingestion.

## Next steps

By reading this document, you have learned how to create flow runs on demand for existing sources dataflows. For more information on sources, read the [sources overview](/en/docs/experience-platform/sources/home)

recommendation-more-help
