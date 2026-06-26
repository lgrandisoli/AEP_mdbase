---
title: "Create an SFTP base connection using the Flow Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/api-tutorials/create/cloud-storage/sftp"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:34:37.121952+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create an SFTP base connection using the Flow Service API

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

A base connection represents the authenticated connection between a source and Adobe Experience Platform.

This tutorial walks you through the steps to create a base connection for SFTP (Secure File Transfer Protocol) using the [Flow Service API](https://www.adobe.io/experience-platform-apis/references/flow-service/).

## Getting started

This guide requires a working understanding of the following components of Adobe Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

IMPORTANT
It is recommended to avoid newlines or carriage returns when ingesting JSON objects with an SFTP source connection. To work around the limitation, use a single JSON object per line and use multi-lines for ensuing files.
The following sections provide additional information that you will need to know in order to successfully connect to an SFTP server using the Flow Service API.

### Gather required credentials

Read the [SFTP authentication guide](/en/docs/experience-platform/sources/connectors/cloud-storage/sftp#gather-required-credentials) for detailed steps on how to retrieve your authentication credentials.

### Using Experience Platform APIs

For information on how to successfully make calls to Experience Platform APIs, see the guide on [getting started with Experience Platform APIs](/en/docs/experience-platform/landing/platform-apis/api-guide).

## Create a base connection

TIP
Once created, you cannot change the authentication type of an SFTP base connection. To change the authentication type, you must create a new base connection.
A base connection retains information between your source and Experience Platform, including your source’s authentication credentials, the current state of the connection, and your unique base connection ID. The base connection ID allows you to explore and navigate files from within your source and identify the specific items that you want to ingest, including information regarding their data types and formats.

The SFTP source supports both basic authentication and authentication via SSH public key. During this step, you can also designate the path to the sub folder that you want to provide access to.

To create a base connection ID, make a POST request to the /connections endpoint while providing your SFTP authentication credentials as part of the request parameters.

IMPORTANT
The SFTP connector supports
ed25519
,
RSA
or
DSA
type OpenSSH key. Ensure that your key file content starts with
"-----BEGIN [RSA/DSA] PRIVATE KEY-----"
and ends with
"-----END [RSA/DSA] PRIVATE KEY-----"
. If the private key file is a PPK-format file, use the PuTTY tool to convert from PPK to OpenSSH format.
**API format**

```
POST /connections
```

Basic authentication
| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SFTP connector with password", "description": "SFTP connector password", "auth": { "specName": "Basic Authentication for sftp", "params": { "host": "{HOST}", "port": 22, "userName": "{USERNAME}", "password": "{PASSWORD}", "maxConcurrentConnections": 5, "folderPath": "acme/business/customers/holidaySales", "disableChunking": "true" } }, "connectionSpec": { "id": "b7bf2577-4520-42c9-bae9-cad01560f7bc", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 Property Description auth.params.host The host name of your SFTP server. auth.params.port The port of the SFTP server. This integer value defaults to 22. auth.params.username The username associated with your SFTP server. auth.params.password The password associated with your SFTP server. auth.params.maxConcurrentConnections The maximum number of concurrent connections specified when connecting Experience Platform to SFTP. When enabled, this value must be set to at least 1. auth.params.folderPath The path to the folder that you want to provide access to. auth.params.disableChunking A boolean value used to determine whether or not your SFTP server supports chunking. connectionSpec.id The SFTP server connection specification ID: b7bf2577-4520-42c9-bae9-cad01560f7bc | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SFTP connector with password", "description": "SFTP connector password", "auth": { "specName": "Basic Authentication for sftp", "params": { "host": "{HOST}", "port": 22, "userName": "{USERNAME}", "password": "{PASSWORD}", "maxConcurrentConnections": 5, "folderPath": "acme/business/customers/holidaySales", "disableChunking": "true" } }, "connectionSpec": { "id": "b7bf2577-4520-42c9-bae9-cad01560f7bc", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 |  | Property | Description | auth.params.host | The host name of your SFTP server. | auth.params.port | The port of the SFTP server. This integer value defaults to 22. | auth.params.username | The username associated with your SFTP server. | auth.params.password | The password associated with your SFTP server. | auth.params.maxConcurrentConnections | The maximum number of concurrent connections specified when connecting Experience Platform to SFTP. When enabled, this value must be set to at least 1. | auth.params.folderPath | The path to the folder that you want to provide access to. | auth.params.disableChunking | A boolean value used to determine whether or not your SFTP server supports chunking. | connectionSpec.id | The SFTP server connection specification ID: b7bf2577-4520-42c9-bae9-cad01560f7bc |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SFTP connector with password", "description": "SFTP connector password", "auth": { "specName": "Basic Authentication for sftp", "params": { "host": "{HOST}", "port": 22, "userName": "{USERNAME}", "password": "{PASSWORD}", "maxConcurrentConnections": 5, "folderPath": "acme/business/customers/holidaySales", "disableChunking": "true" } }, "connectionSpec": { "id": "b7bf2577-4520-42c9-bae9-cad01560f7bc", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 |  |
| Property | Description |
| auth.params.host | The host name of your SFTP server. |
| auth.params.port | The port of the SFTP server. This integer value defaults to 22. |
| auth.params.username | The username associated with your SFTP server. |
| auth.params.password | The password associated with your SFTP server. |
| auth.params.maxConcurrentConnections | The maximum number of concurrent connections specified when connecting Experience Platform to SFTP. When enabled, this value must be set to at least 1. |
| auth.params.folderPath | The path to the folder that you want to provide access to. |
| auth.params.disableChunking | A boolean value used to determine whether or not your SFTP server supports chunking. |
| connectionSpec.id | The SFTP server connection specification ID: b7bf2577-4520-42c9-bae9-cad01560f7bc |

| accordion |
| --- |
| Response |
| A successful response returns the unique identifier ( id ) of the newly created connection. This ID is required to explore your SFTP server in the next tutorial. code language-json { "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094", "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\"" } | code language-json | { "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094", "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\"" } |
| code language-json |
| { "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094", "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\"" } |

SSH public key authentication
| accordion |
| --- |
| Request |
| code language-shell curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SFTP connector with SSH authentication", "description": "SFTP connector with SSH authentication", "auth": { "specName": "SSH PublicKey Authentication for sftp", "params": { "host": "{HOST}", "port": 22, "userName": "{USERNAME}", "privateKeyContent": "{PRIVATE_KEY_CONTENT}", "passPhrase": "{PASSPHRASE}", "maxConcurrentConnections": 5, "folderPath": "acme/business/customers/holidaySales", "disableChunking": "true" } }, "connectionSpec": { "id": "b7bf2577-4520-42c9-bae9-cad01560f7bc", "version": "1.0" } }' table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 Property Description auth.params.host The host name of your SFTP server. auth.params.port The port of the SFTP server. This integer value defaults to 22. auth.params.username The username associated with your SFTP server. auth.params.privateKeyContent The Base64-encoded SSH private key content. The supported OpenSSH key types are ed25519 , RSA , and DSA . auth.params.passPhrase The pass phrase or password to decrypt the private key if the key file or the key content is protected by a pass phrase. If PrivateKeyContent is password protected, this parameter needs to be used with the PrivateKeyContent’s passphrase as value. auth.params.maxConcurrentConnections The maximum number of concurrent connections specified when connecting Experience Platform to SFTP. When enabled, this value must be set to at least 1. auth.params.folderPath The path to the folder that you want to provide access to. auth.params.disableChunking A boolean value used to determine whether or not your SFTP server supports chunking. connectionSpec.id The SFTP server connection specification ID: b7bf2577-4520-42c9-bae9-cad01560f7bc | code language-shell | curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SFTP connector with SSH authentication", "description": "SFTP connector with SSH authentication", "auth": { "specName": "SSH PublicKey Authentication for sftp", "params": { "host": "{HOST}", "port": 22, "userName": "{USERNAME}", "privateKeyContent": "{PRIVATE_KEY_CONTENT}", "passPhrase": "{PASSPHRASE}", "maxConcurrentConnections": 5, "folderPath": "acme/business/customers/holidaySales", "disableChunking": "true" } }, "connectionSpec": { "id": "b7bf2577-4520-42c9-bae9-cad01560f7bc", "version": "1.0" } }' | table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 |  | Property | Description | auth.params.host | The host name of your SFTP server. | auth.params.port | The port of the SFTP server. This integer value defaults to 22. | auth.params.username | The username associated with your SFTP server. | auth.params.privateKeyContent | The Base64-encoded SSH private key content. The supported OpenSSH key types are ed25519, RSA, and DSA. | auth.params.passPhrase | The pass phrase or password to decrypt the private key if the key file or the key content is protected by a pass phrase. If PrivateKeyContent is password protected, this parameter needs to be used with the PrivateKeyContent’s passphrase as value. | auth.params.maxConcurrentConnections | The maximum number of concurrent connections specified when connecting Experience Platform to SFTP. When enabled, this value must be set to at least 1. | auth.params.folderPath | The path to the folder that you want to provide access to. | auth.params.disableChunking | A boolean value used to determine whether or not your SFTP server supports chunking. | connectionSpec.id | The SFTP server connection specification ID: b7bf2577-4520-42c9-bae9-cad01560f7bc |
| code language-shell |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/flowservice/connections' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -H 'Content-Type: application/json' \ -d '{ "name": "SFTP connector with SSH authentication", "description": "SFTP connector with SSH authentication", "auth": { "specName": "SSH PublicKey Authentication for sftp", "params": { "host": "{HOST}", "port": 22, "userName": "{USERNAME}", "privateKeyContent": "{PRIVATE_KEY_CONTENT}", "passPhrase": "{PASSPHRASE}", "maxConcurrentConnections": 5, "folderPath": "acme/business/customers/holidaySales", "disableChunking": "true" } }, "connectionSpec": { "id": "b7bf2577-4520-42c9-bae9-cad01560f7bc", "version": "1.0" } }' |
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 |  |
| Property | Description |
| auth.params.host | The host name of your SFTP server. |
| auth.params.port | The port of the SFTP server. This integer value defaults to 22. |
| auth.params.username | The username associated with your SFTP server. |
| auth.params.privateKeyContent | The Base64-encoded SSH private key content. The supported OpenSSH key types are ed25519, RSA, and DSA. |
| auth.params.passPhrase | The pass phrase or password to decrypt the private key if the key file or the key content is protected by a pass phrase. If PrivateKeyContent is password protected, this parameter needs to be used with the PrivateKeyContent’s passphrase as value. |
| auth.params.maxConcurrentConnections | The maximum number of concurrent connections specified when connecting Experience Platform to SFTP. When enabled, this value must be set to at least 1. |
| auth.params.folderPath | The path to the folder that you want to provide access to. |
| auth.params.disableChunking | A boolean value used to determine whether or not your SFTP server supports chunking. |
| connectionSpec.id | The SFTP server connection specification ID: b7bf2577-4520-42c9-bae9-cad01560f7bc |

| accordion |
| --- |
| Response |
| A successful response returns the unique identifier ( id ) of the newly created connection. This ID is required to explore your SFTP server in the next tutorial. code language-json { "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094", "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\"" } | code language-json | { "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094", "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\"" } |
| code language-json |
| { "id": "bf367b0d-3d9b-4060-b67b-0d3d9bd06094", "etag": "\"1700cc7b-0000-0200-0000-5e3b3fba0000\"" } |

## Next steps

By following this tutorial, you have created an SFTP connection using the Flow Service API, and have obtained the connection’s unique ID value. You can use this connection ID to [explore cloud storages using the Flow Service API](/en/docs/experience-platform/sources/api-tutorials/explore/cloud-storage).

recommendation-more-help
