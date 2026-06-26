---
title: "Subscribe to alerts for sources dataflows in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/alerts"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:33:56.224024+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Subscribe to alerts for sources dataflows in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Adobe Experience Platform allows you to subscribe to event-based alerts regarding Adobe Experience Platform activities. Alerts reduce or eliminate the need to poll the [Observability Insights API](/en/docs/experience-platform/observability/api/overview) in order to check if a job has completed, if a certain milestone within a workflow has been reached, or if any errors have occurred.

You can subscribe to alerts when creating a dataflow to receive alert messages regarding the status, success, or failure of your flow run.

This document provides steps on how to subscribe receive alerts messages for your sources dataflows.

## Getting started

This document requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Observability](/en/docs/experience-platform/observability/home): Observability Insights allows you to monitor Experience Platform activities through the use of statistical metrics and event notifications. Alerts : When a certain set of conditions in your Experience Platform operations is reached (such as a potential problem when the system breaches a threshold), Experience Platform can deliver alert messages to any users in your organization who have subscribed to them.

## Subscribe to alerts in the UI subscribe-sources-alerts

IMPORTANT
You must enable instant notifications of emails for your Experience Platform account in order to receive email-based alert notifications for your dataflows.
You can enable alerts for your dataflows during the Dataflow detail step of the sources workflow in the sources workspace.

The available alerts for sources dataflows are:

NOTE
Streaming sources are currently not supported by alerts. You can only subscribe to alert notifications for batch sources.
Alerts
Description
Sources Flow Run Start
This alert sends you a message when your source dataflow has started.
Sources Flow Run Success
This alert sends you a message when data from your source is successfully ingested to Experience Platform.
Sources Flow Run Failure
This alert sends you a message if an error occurs in your dataflow.
Select the alerts you would like to subscribe to and then select **Next** to review and finish your dataflow.

See the following guides for detailed steps on creating a sources dataflow in the UI:

- [Advertising](/en/docs/experience-platform/sources/ui-tutorials/dataflow/advertising)
- [Cloud storage](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage)
- [CRM](/en/docs/experience-platform/sources/ui-tutorials/dataflow/crm)
- [Database](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases)
- [E-commerce](/en/docs/experience-platform/sources/ui-tutorials/dataflow/ecommerce)
- [Local files](/en/docs/experience-platform/sources/ui-tutorials/create/local-system/local-file-upload)
- [Marketing automation](/en/docs/experience-platform/sources/ui-tutorials/dataflow/marketing-automation)
- [Payments](/en/docs/experience-platform/sources/ui-tutorials/dataflow/payments)
- [Protocols](/en/docs/experience-platform/sources/ui-tutorials/dataflow/protocols)

## Receive alerts

Once your dataflow runs, you can receive alerts through the UI or by email.

### In the UI

Alerts are represented in the UI by a notification icon in the top header of the Experience Platform UI. Select the notification icon to see specific alert messages regarding your dataflows.

The notifications panel appears, displaying a list of status updates on the dataflow that you created.

You can hover on an alert message to mark them as read or you can select the clock icon to set future reminders on the status of your dataflow.

Select the alert message to see specific information on your dataflow.

The Dataflow run overview page appears. The upper half of the screen displays an overview on your dataflow, including information on its attributes, corresponding dataflow run ID, and high-level error summary.

The lower half of the page displays any Dataflow run errors that ocurred during the dataflow run stage. From here, you can preview error diagnostics or use the [Data Access API](https://www.adobe.io/experience-platform-apis/references/data-access/) to download error diagnostics or the file manifest that corresponds to your dataflow.

For more information on handling dataflow errors, see the guide on [monitoring sources dataflows in the UI](/en/docs/experience-platform/dataflows/ui/monitor-sources).

### By email

Alerts for your dataflows are also delivered to you by email. Select the dataflow name in the email body to see more information on your dataflow.

Similar to the UI alert, the Dataflow run overview page appears, providing you with an interface to investigate any errors associated with your dataflow.

## Subscribe and unsubscribe to alerts

You can subscribe to more alerts or unsubscribe from established alerts for an existing dataflow in the Dataflows page. Locate the dataflow you create from the list and then select the ellipses (...) to see a dropdown menu of options. Next, select **Subscribe alerts** to modify the alert settings of your dataflow.

A pop-up window appears, providing you with a list of sources alerts. Select any alerts you want to subscribe to or deselect alerts that you want to unsubscribe from. When finished, select **Save**.

## Next steps

This document provided a step-by-step guide on how to subscribe to in-context alerts for your sources dataflows. For more information, see the [alerts UI guide](/en/docs/experience-platform/observability/alerts/ui).

recommendation-more-help
