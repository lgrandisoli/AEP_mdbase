---
title: "Delete source connection accounts"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/delete-accounts"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:08:30.264754+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Delete source connection accounts

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

Source connectors in Adobe Experience Platform provide the ability to ingest externally sourced data on a scheduled basis. This tutorial provides steps for deleting accounts from the **Sources** workspace.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

## Delete accounts using the UI

TIP
Before deleting the source account, you must first delete any existing dataflows associated with the source account. To delete existing dataflows, refer to the tutorial on
deleting sources dataflows in the UI
.
Log in to [Adobe Experience Platform](https://platform.adobe.com) and then select **Sources** from the left navigation bar to access the **Sources** workspace. The **Catalog** screen displays a variety of sources for which you can create accounts and dataflows with. Each source shows the number of existing accounts and dataflows associated to them.

Select **Accounts** to access the **Accounts** page.

A list of existing accounts appears. On this page is a list of sortable information for existing accounts such as source, username, associated dataflows, and created date. Select the **funnel icon** on the top left to sort.

The sorting panel appears on the left side of the screen, containing a list of available sources. You can select more than one source using the sorting function.

Select the source you wish to access and locate the account you intend to delete from the list of accounts in the main interface. In the example, the source selected is **Azure Blob Storage** and the account name is **blobTestConnector**. When selecting multiple sources from the sorting panel, your most recently created accounts appear first because the list is sorted by created date.

Select the account you intend to delete.

The **Properties** panel appears on the right side of the screen, containing information regarding the selected account.

Select the ellipses (...) beside the name of the account you intend to delete. A pop-up panel appears, providing options to **Add data**, **Edit details**, and **Delete**. Select **Delete** to delete the account.

A final confirmation dialog box appears, select **Delete** to complete the process.

## Next steps

By following this tutorial, you have successfully used the **Sources** workspace to delete existing accounts.

For steps on how to perform these operations programmatically using the Flow Service API, please refer to the tutorial on [deleting connections using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/delete)

recommendation-more-help
