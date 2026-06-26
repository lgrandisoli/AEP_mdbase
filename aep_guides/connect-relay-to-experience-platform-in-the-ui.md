---
title: "Connect Relay to Experience Platform in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/marketing-automation/relay-connector"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:25:59.906533+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Relay to Experience Platform in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

NOTE
The Relay Connector source is in beta. Please read the
sources overview
for more information on using beta-labeled sources.
With Relay Connector, you can deliver personalized experiences to your customers at the most meaningful moments in their journey, helping you build stronger relationships and drive greater loyalty and value by creating an inbound connection to stream Events from your Relay Network integration into Adobe Experience Platform.

Read this guide to learn how to use the Relay Connector within the sources workspace of the Experience Platform UI.

IMPORTANT
This documentation page is maintained by the
Relay Network
team. For any inquiries or update requests, please contact them directly at
Relay Network
or email
info@relaynetwork.com
.
## Connect your Relay Connector source

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account. You can select the appropriate category from the catalog on the left-hand side of your screen or use the search option to find a specific source.

Under the *Marketing automation* category, select the Relay Connector source card and select **Add data**.

TIP
Sources in the sources catalog display the
Set up
option when no authenticated account exists. Once an account is authenticated, this option changes to
Add data
.
### Select data

The **Connect Relay Connector source** interface appears. Use the *Select data* interface to browse or specify the source data schema. Alternatively, you can upload a sample JSON file to define the source schema.

NOTE
Acceptable file size is up to 1GB.
After the data is uploaded, you can use the Preview sample data section to preview the data.

### Dataflow details

Next, use the *Dataflow details* interface to provide a **name** and an **optional description** for your dataflow. Additionally, select the **Target dataset** that you want to use. You can either create a new dataset or use an existing dataset.

### Mapping

You can map your source fields to XDM schema fields using the auto-map functionality, which matches fields based on their names, or create custom mappings for more precise control. If needed, you can also apply transformations such as concatenation, formatting, or renaming to ensure your data fits perfectly into the target schema. For more information on mapping, read the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

TIP
For details on the types of events and data values that Relay will send to your source, read the
Relay Network Push Events
documentation. This information will help you design your
Experience Events Schema
appropriately.
### Review

Finally, review all configurations including your **source, dataset, and mappings**. When finished, select **Finish** to create the dataflow.

### Retrieve your streaming endpoint URL

Once you have created the dataflow, you will find the *streaming endpoint URL* and other related details in the **Properties** section on the right side of the dataflow page.

Use these values to set up the webhook in the **Relay console**. For detailed instructions on configuring the push, see the Relay documentation: [Configuring the Push API](https://docs.relaynetwork.com/docs/configuring-the-push-api).

## Additional resources

- [Create a new connection specification using the Flow Service API](/en/docs/experience-platform/sources/sdk/streaming-sdk/create)
- [Connect to your source using the UI](/en/docs/experience-platform/sources/sdk/streaming-sdk/submit#test-your-source-using-the-ui)

recommendation-more-help
