---
title: "Draft dataflows in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/draft"
category: "tutorials"
topic: "sources/ui-tutorials/draft"
created_at: "2026-05-29T17:06:01.966799+00:00"
---
Breadcrumbs: Documentation > Source Connectors Guide

# Draft dataflows in the UI

Last update: May 13, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Save your unfinished data ingestion workflow progress by setting your dataflow to a draft status. You can resume and complete your drafted dataflows at a later time.

This document provides steps on how to save your dataflows when using the sources workspace in the Adobe Experience Platform UI.

## Getting started

This document requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.

## Save a dataflow as a draft

You can pause your dataflow creation progress at any time after you select the data that you’ll be bringing into Experience Platform.

For example, if you want to save your progress during the dataflow detail step, select **Save as draft**.

Once you save your draft, you will be taken to your account’s page, where you can see a list of your existing dataflows, including your drafts.

TIP
Drafted dataflows will not be enabled and will have their status set to
draft
.
To continue on your draft, select the ellipses (...) beside your dataflow’s name and then select **Update dataflow**.

NOTE
If your draft includes scheduling information, then the dropdown window will also give you the option to
Edit schedule
.
### Access your drafts from the source catalog

You can also access your draft dataflows through the dataflows catalog. Select **Dataflows** from the top header to access the dataflows catalog. From here, find your draft from the list of existing dataflows in your organization, select the ellipses (...) beside its name, and then select **Update dataflow**.

## Publish your draft dataflow

You are returned to the Add data step of the sources workflow, where you can re-confirm the format of your data and continue progressing on your dataflow.

Once you confirm the formatting, delimiter, and compression type of your data, select **Next** to proceed.

Next, confirm your dataflow details. Use the dataflow details interface to update configurations surrounding your dataflow’s name, description, partial ingestion, error diagnostic settings, and alert preferences.

Once you have finished your configurations, select **Next** to proceed.

The Mapping step appears. During this step, you can reconfigure the mapping configurations of your dataflow. For a comprehensive guide on the data prep functions used for mapping, visit the [data prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once you have completed mapping reconfiguration, select **Next** to proceed.

Use the Scheduling step to establish an ingestion schedule for your dataflow. You can set your ingestion frequency to once, minute, hour, day, or week. When finished, select **Next** to proceed.

Finally, review the details of your dataflow and then select **Finish** to publish your draft.

After you save and publish a draft, the dataflow will be enabled, and you will no longer be able to reset it as a draft.

## Next steps

By following this tutorial, you have learned how to save your progress and set a dataflow as a draft. For more information on sources, visit the [sources overview](/en/docs/experience-platform/sources/home).

recommendation-more-help
