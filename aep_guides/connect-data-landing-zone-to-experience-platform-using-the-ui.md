---
title: "Connect Data Landing Zone to Experience Platform using the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/data-landing-zone"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:36:37.948192+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Connect Data Landing Zone to Experience Platform using the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
This page is specific to the Data Landing Zone
source
connector in Experience Platform. For information on connecting to the Data Landing Zone
destination
connector, refer to the
Data Landing Zone destination documentation page
.
Data Landing Zone is a secure, cloud-based file storage facility to bring files into Adobe Experience Platform. Data is automatically deleted from the Data Landing Zone after seven days.

This tutorial provides steps for creating a Data Landing Zone source connection using the Experience Platform user interface.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Bring your files from Data Landing Zone to Experience Platform

IMPORTANT
To connect to the source, you need the
View Sources
and
Manage Sources
access control permissions. Read the
access control overview
or contact your product administrator to obtain the required permissions.
In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. The Catalog screen displays a variety of sources that you can create an account with.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search bar.

Under the cloud storage category, select Data Landing Zone and then select **Add data**.

The Add data step appears, providing you with an interface to select and preview the data you want to bring to Experience Platform.

- The left part of the interface is a folder browser, providing you with a list of files from your container that you can then bring to Experience Platform.
- The right part of the interface lets you preview up to 100 rows of data from a compatible file.

Select the file that you want to bring to Experience Platform and allow for a few moments for the right interface to update into a preview screen.

TIP
Experience Platform auto-detects property information of the file you selected, including information on the file’s data format, designated column delimiter, and compression type.
The preview interface allows you to inspect the contents and structure of a file. By default, the preview interface displays the first file in the folder you selected.

To preview a different file, select the preview icon beside the name of the file you want to inspect.

When finished, select **Next**.

For a detailed, step-by-step guide on how to create a dataflow for a cloud storage source, see the tutorial on [creating a cloud storage dataflow to bring data to Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

## Retrieve your Data Landing Zone credentials

Data Landing Zone is a source that comes with your Adobe Experience Platform Sources license. Data Landing Zone uses an SAS URI and SAS Token-based authentication. You can retrieve your authentication credentials from the Sources catalog page.

To retrieve your credentials, select the **Data Landing Zone** card and then copy your credentials from the right rail that appears.

A popover appears, displaying your container name, SAS token, storage account name, SAS URI, and expiry date.

## Refresh your Data Landing Zone credentials

Your Data Landing Zone credentials are set to auto-expire after 90 days and you must use new credentials to re-connect to Data Landing Zone after expiration. Your dataflows in Experience Platform are not affected by expiring credentials and you can still continue working with new and existing dataflows with your new credentials.

There are two ways to refresh your Data Landing Zone credentials:

Use the source card
To refresh your credentials from the sources catalog page, select the ellipses (**...**) in the Data Landing Zone card and then select **Refresh credentials**.

A pop up window appears, prompting your confirmation before you can proceed. When you are ready, select **Refresh credentials**.

Use the right rail
To refresh your credentials using the right rail, select the **Data Landing Zone** source card and then select **More actions**. Next, select **Refresh Credentials** and then confirm using the pop up window that appears.

## Next steps

By following this tutorial, you have accessed your Data Landing Zone container and learned to retrieve and refresh your credentials. You can now proceed to the next tutorial on [creating a dataflow to bring data from a cloud storage to Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

recommendation-more-help
