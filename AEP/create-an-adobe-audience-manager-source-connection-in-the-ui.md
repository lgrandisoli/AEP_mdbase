---
title: "Create an Adobe Audience Manager source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/audience-manager"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T16:56:16.296164+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an Adobe Audience Manager source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial walks you through the steps to create a source connector for Adobe Audience Manager to bring in Consumer Experience Event data into Experience Platform using the user interface.

## Create a source connection with Adobe Audience Manager

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources that you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search bar.

Under Adobe Application, select **Adobe Audience Manager** and then select **Set up**.

### Select traits and segments

NOTE
You cannot ingest regional data from the Audience Manager source to Experience Platform. If you have Analytics use cases that require regional data, then please use the
Analytics source connector
.
The Select traits and segments step appears, providing you with an interactive interface to explore and select your traits, segments, and data.

- The left panel of the interface contains the Select traits and segments options, as well as a hierarchical directory of all segments available to you.
- The right half of the interface allows you to interact with selected segments and pick through specific data you want to use.

To navigate through available segments, select the folder you want to access from the All Segments panel. Selecting a folder allows you to traverse a folder’s hierarchy and provides you with a list of segments to filter through.

Once you have identified and selected the segments you want to use, a new panel appears on the right, displaying your list of selected items. You can continue to access different folders and select different segments for your connection. Selecting more segments updates the panel on the right.

Alternatively, you can select the **Select all segments** and **Select all traits** boxes. Selecting all segments will bring Audience Manager segments to Experience Platform, while selecting all traits enables all first party traits from Audience Manager.

WARNING
The ingestion of sizeable Audience Manager segment populations has a direct impact on your total profile count when you first send an Audience Manager segment to Experience Platform using the Audience Manager source. This means that selecting all segments can potentially lead to a Profile count in excess of your license usage entitlement. Please review your
license usage allowance
before proceeding.
Once you are finished, select **Next**

The Review step appears, allowing you to review your selected traits and segments before they are connected to Experience Platform. Details are grouped within the following categories:

- **Connection**: Shows the source platform and the status of the connection.
- **Selected data**: Shows the number of selected segments and enabled traits.

Once you have reviewed your dataflow, select **Finish** and allow some time for the dataflow to be created.

## Next steps

While an Audience Manager dataflow is active, incoming data is automatically ingested into Real-Time Customer Profiles. You can now utilize this incoming data and create audience segments using Experience Platform Segmentation Service. See the following documents for more details:

- [Real-Time Customer Profile overview](/en/docs/experience-platform/profile/home)
- [Segmentation Service overview](/en/docs/experience-platform/segmentation/home)

recommendation-more-help
