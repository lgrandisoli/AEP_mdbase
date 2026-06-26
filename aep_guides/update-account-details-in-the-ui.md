---
title: "Update account details in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/update"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:30:17.982155+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Update account details in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

In some circumstances, it may be required to update the details of an existing sources account. The Sources workspace provides you with the ability to add, edit, and delete details of an existing batch or streaming connection, including its name, description, and credentials.

This tutorial provides steps for updating the details and credentials of an existing account from the Sources workspace.

## Getting started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Update accounts

Log in to the [Experience Platform UI](https://platform.adobe.com) and then select **Sources** from the left navigation to access the Sources workspace. Select **Accounts** from the top header to view existing accounts.

The **Accounts** page appears. On this page is a list of viewable accounts, including information about their source, username, number of dataflows, and date of creation.

Select the filter icon on the top left to launch the sort panel.

The sort panel provides a list of all sources. You can select more than one source from the list to access a filtered selection of accounts associated with different sources.

Select the source you wish to work with to see a list of its existing accounts. Once you have identified the account you want to update, select the ellipses (...) beside the account name.

A dropdown menu appears, providing you with options to **Add data**, **Edit details**, and **Delete**. Select **Edit details** from the menu to update your account.

The **Edit account details** dialog box allows you to update an account’s name, description, and authentication credentials. Once you have updated the desired information, select **Save**.

After a few moments, a confirmation box appears on the bottom of the screen to confirm a successful update.

## Next steps

By following this tutorial, you have successfully used the Sources workspace to update the information of an existing source account.

For steps on how to perform these operations programmatically using the Flow Service API, please refer to the tutorial on [updating connection information using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/update).

recommendation-more-help
