---
title: "Create an SFTP source connection in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/cloud-storage/sftp"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:34:38.438878+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an SFTP source connection in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

This tutorial provides steps to create an SFTP source connection using the Adobe Experience Platform UI.

## Get started

This tutorial requires a working understanding of the following components of Experience Platform:

- Experience Data Model (XDM) System : The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn about the basic building blocks of XDM schemas, including key principles and best practices in schema composition. Schema Editor tutorial : Learn how to create custom schemas using the Schema Editor UI.
- Real-Time Customer Profile : Provides a unified, real-time consumer profile based on aggregated data from multiple sources.

IMPORTANT
It is recommended to avoid newlines or carriage returns when ingesting JSON objects with an SFTP source connection. To work around the limitation, use a single JSON object per line and use multi-lines for ensuing files.
If you already have a valid SFTP connection, you may skip the remainder of this document and proceed to the tutorial on [configuring a dataflow](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

### Gather required credentials

Read the [SFTP authentication guide](/en/docs/experience-platform/sources/connectors/cloud-storage/sftp#gather-required-credentials) for detailed steps on how to retrieve your authentication credentials.

## Connect to your SFTP server

In the Experience Platform UI, select **Sources** from the left navigation bar to access the Sources workspace. The Catalog screen displays a variety of sources with which you can create an account.

You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the Cloud storage category, select **SFTP** and then select **Add data**.

The **Connect to SFTP** page appears. On this page, you can either use new credentials or existing credentials.

### Existing account

To connect an existing account, select the FTP or SFTP account you want to connect with, then select **Next** to proceed.

### New account

TIP
- Once created, you cannot change the authentication type of an SFTP base connection. To change the authentication type, you must create a new base connection.
- SFTP supports ed25519 , RSA or DSA type OpenSSH key. Ensure that your key file content starts with "-----BEGIN [RSA/DSA] PRIVATE KEY-----" and ends with "-----END [RSA/DSA] PRIVATE KEY-----" . If the private key file is a PPK-format file, use the PuTTY tool to convert from PPK to OpenSSH format.

If you are creating a new account, select **New account**, and then provide a name and an optional description for your new SFTP account.

The SFTP source supports both basic authentication and authentication via SSH public key.

Basic authentication
To use basic authentication, select **Password** and then provide the appropriate values for the following credentials:

- host
- port
- username
- password

During this step, you can also configure your max concurrent connections, define your folder path, and enable or disable chunking for your SFTP server. When finished, select **Connect to source** and allow for a few moments for the connection to establish.

For more information on authentication, read the guide on [gathering required credentials for SFTP](/en/docs/experience-platform/sources/connectors/cloud-storage/sftp#gather-required-credentials).

SSH public key authentication
To use SSH public key-based credentials, select **SSH public key** and then provide the appropriate values for the following credentials:

- host
- port
- username
- private key content
- passphrase

During this step, you can also configure your max concurrent connections, define your folder path, and enable or disable chunking for your SFTP server. When finished, select **Connect to source** and allow for a few moments for the connection to establish.

For more information on authentication, read the guide on [gathering required credentials for SFTP](/en/docs/experience-platform/sources/connectors/cloud-storage/sftp#gather-required-credentials).

## Next steps

By following this tutorial, you have established a connection to your SFTP account. You can now continue on to the next tutorial and [configure a dataflow to bring data from your cloud storage into Experience Platform](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage).

recommendation-more-help
