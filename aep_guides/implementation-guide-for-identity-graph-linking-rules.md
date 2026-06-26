---
title: "Implementation guide for Identity Graph Linking Rules"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/identity/features/identity-graph-linking-rules/implementation-guide"
category: "guides"
topic: "experience-platform/experience-platform-identity-service-guide"
created_at: "2026-06-26T17:33:48.827233+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform Identity Service Guide

# Implementation guide for Identity Graph Linking Rules

Last update: June 18, 2026
- Topics:
- [Identities](#)

CREATED FOR:

- Admin
- Developer

IMPORTANT
This document assumes that you are starting your implementation in a new sandbox without any data.
Read this document for a step-by-step by guide that you can follow when implementing your data with Adobe Experience Platform Identity Service.

Step-by-step outline:

- [Complete prerequisites for implementation](#prerequisites-for-implementation)
- [Create the necessary identity namespaces](#namespace)
- [Use the graph simulation tool to familiarize yourself with the Identity Optimization Algorithm](#graph-simulation)
- [Use the identity settings UI to designate your unique namespaces and configure priority rankings for your namespaces](#identity-settings)
- [Create an Experience Data Model (XDM) schema](#schema)
- [Create a dataset](#dataset)
- [Ingest your data to Experience Platform](#ingest)

## Prerequisites for implementation prerequisites-for-implementation

This section outlines prerequisite steps that you must complete prior to implementing Identity Graph Linking Rules to your data.

### Unique namespace

#### Single person namespace requirement single-person-namespace-requirement

You must ensure that the unique namespace with the highest priority is always present in every known profile. Doing so allows Identity Service to detect the appropriate person identifier in a given graph.

Select to view an example of a graph without a singular person identifier namespace
Without a unique namespace to represent your person identifiers, you may end up with a graph that links to disparate person identifiers to the same ECID. In this example, both B2BCRM and B2CCRM are linked to the same ECID at the same time. This graph suggests that Tom, using his B2C login account, shared a device with Summer, using her B2B login account. However, the system will recognize that this is one profile (graph collapse).

{modal="regular"}

Select to view an example of a graph with a single person identifier namespace
Given a unique namespace, (in this case, a CRMID instead of two disparate namespaces), Identity Service is able to discern the person identifier that was last associated with the ECID. In this example, because a unique CRMID exists, Identity Service is able to recognize a “shared device” scenario, where two entities are sharing the same device.

{modal="regular"}

### Namespace priority configuration

If you are using the [Adobe Analytics source connector](/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/analytics) to ingest data, then you must give your ECIDs a higher priority than Adobe Analytics ID (AAID) because Identity Service blocks AAID. By prioritizing ECID, you can instruct Real-Time Customer Profile to store unauthenticated events to ECID instead of AAID.

### XDM experience events xdm-experience-events

During your pre-implementation process, you must ensure that the authenticated events that your system will send to Experience Platform always contain a **single** person identifier, such as a CRMID.

- (Recommended) Authenticated events with one unique person identifier.
- (Not recommended) Authenticated events with two unique person identifiers. If you have more than one unique person identifiers, then you may encounter an unwanted graph collapse.
- (Not recommended) Authenticated events without any unique person identifiers. If you do not have any unique person identifiers, then both unauthenticated and authenticated events will be stored against the ECID.

Authenticated events with one person identifier
| code language-json |
| --- |
| { "_id": "test_id", "identityMap": { "ECID": [ { "id": "62486695051193343923965772747993477018", "primary": false } ], "CRMID": [ { "id": "John", "primary": true } ] }, "timestamp": "2024-09-24T15:02:32+00:00", "web": { "webPageDetails": { "URL": "https://business.adobe.com/", "name": "Adobe Business" } } } |

Authenticated events with two person identifiers
If your system sends two person identifiers, the implementation may fail the single-person namespace requirement. For example, if the identityMap in your webSDK implementation contains a CRMID, a customerID, and an ECID namespace, then there is no guarantee that every single event will contain both CRMID and customerID.

You should **not** send a payload like below:

| code language-json |
| --- |
| { "_id": "test_id", "identityMap": { "ECID": [ { "id": "62486695051193343923965772747993477018", "primary": false } ], "CRMID": [ { "id": "John", "primary": true } ], "customerID": [ { "id": "Jane", "primary": false } ], }, "timestamp": "2024-09-24T15:02:32+00:00", "web": { "webPageDetails": { "URL": "https://business.adobe.com/", "name": "Adobe Business" } } } |

However, it is important to note that while you can send two person identifiers, there is no guarantee that an unwanted graph collapse will be prevented due to implementation or data errors. Consider the following scenario:

- timestamp1 = John logs in -> system captures CRMID: John, ECID: 111. However, customerID: John is not present in this event payload.
- timestamp2 = Jane logs in -> system captures customerID: Jane, ECID: 111. However, CRMID: Jane is not present in this event payload.

Therefore, it is best practice to only send just one person identifier with your authenticated events.

In graph simulation, this ingestion may look like:

{modal="regular"}

Authenticated events without any person identifiers
In this example, you can assume that the following event was sent to Experience Platform while John (the end-user) was browsing your website while authenticated. However, despite being authenticated, Experience Platform is unable to identify John due to the lack of person identifiers in the event. Therefore, this event gets interpreted as an anonymous user browsing the Adobe Business website, instead of recognizing it as an online activity associated specifically to John.

| code language-json |
| --- |
| { "_id": "test_id", "identityMap": { "ECID": [ { "id": "62486695051193343923965772747993477018", "primary": false } ] }, "timestamp": "2024-09-24T15:02:32+00:00", "web": { "webPageDetails": { "URL": "https://business.adobe.com/", "name": "Adobe Business" } } } |

## Set permissions set-permissions

The first step in the implementation process for Identity Service is to ensure that your Experience Platform account is added to a role that is provisioned with the necessary permissions. Your administrator can configure permissions for your account by navigating to the Permissions UI in Adobe Experience Cloud. From there, your account must be added to a role with the following permissions:

- View Identity Settings: apply this permission to be able to view unique namespaces and namespace priority in the identity namespace browse page.
- Edit Identity Settings: apply this permission to be able to edit and save your identity settings.

For more information on permissions, read the [permissions guide](/en/docs/experience-platform/access-control/abac/permissions-ui/permissions).

## Create your identity namespaces namespace

If your data requires it, you must first create the appropriate namespaces for your organization. For steps on how to create a custom namespace, read the guide on [creating a custom namespace in the UI](/en/docs/experience-platform/identity/features/namespaces#create-custom-namespaces).

## Use graph simulation tool graph-simulation

Next, navigate to the [graph simulation tool](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/graph-simulation) in the Identity Service UI workspace. You can use the graph simulation tool to simulate identity graphs, built with a variety of different unique namespace and namespace priority configurations.

By creating different configurations, you can use the graph simulation tool to learn and better understand how the Identity Optimization Algorithm and certain configurations can affect how your graph behaves.

## Configure identity settings identity-settings

Once you have a better idea of how you want your graph to behave, navigate to the [identity settings UI](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/identity-settings-ui) in the Identity Service UI workspace. To access the identity settings UI, select **Identities** from the left navigation and then select **Settings**.

{modal="regular"}

Use the identity settings UI to designate your unique namespaces and configure your namespaces by order of priority.

IMPORTANT
Once you are finished with applying your settings, you must wait at least 24 hours before you can proceed to ingest data, as it takes at least 24 hours for new settings to be reflected in Identity Service.
For more information, read the [identity settings UI guide](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/identity-settings-ui).

## Create an XDM schema schema

With your unique namespaces and namespace priorities established, you can now proceed to required set up in order to ingest your data. First, you must create an XDM schema. Depending on your data, you may need to create a schema for both XDM Individual Profile and XDM ExperienceEvent.

To ingest data into Real-Time Customer Profile, you must ensure that your schema contains at least one field that has been designated as the primary identity. By setting a primary identity, you can enable a given schema for Profile ingestion.

For instructions on how to create a schema, read the guide on [creating an XDM schema in the UI](/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

## Create a dataset dataset

Next, create a dataset to provide a structure for the data that you are going to ingest. A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows). Datasets work in tandem with schemas, and to ingest data to Real-Time Customer Profile, your dataset must be enabled for Profile ingestion. In order for your dataset to be enabled for Profile, it must reference a schema that is enabled for Profile ingestion.

For instructions on how to create a dataset, read the [dataset UI guide](/en/docs/experience-platform/catalog/datasets/user-guide).

## Ingest your data ingest

By this point, you should have the following:

- The necessary permissions to access Identity Service features.
- Namespaces for your data.
- Designated unique namespaces and configured priorities for your namespaces.
- At least one XDM schema. (Depending on your data and specific use case, you may need to create both profile and experience event schemas.)
- A dataset that is based off of your schema.

Once you have all of the items listed above, then you can begin ingesting your data to Experience Platform. You can perform data ingestion through several different ways. You can use the following services to bring your data to Experience Platform:

- [Batch and streaming ingestion](/en/docs/experience-platform/ingestion/home)
- [Data collection in Experience Platform](/en/docs/experience-platform/collection/home)
- [Experience Platform sources](/en/docs/experience-platform/sources/home)

TIP
Once your data is ingested, the XDM raw data payload does not change. You may still see your primary identity configurations iin the UI. However, these configurations will be overridden by identity settings.
For any feedback, use the **Beta feedback** option in the Identity Service UI workspace.

## Validate your graphs validate

Use the identity dashboard for insights on the state of your identity graphs, such as your overall identity count and graph count trends, identity count by namespace, and graph count by graph size. You can also use the identity dashboard to view trends on graphs with two or more identities, organized by namespace.

Select the ellipses (...) and then select **View more** for further information and to validate that there are no collapsed graphs.

{modal="regular"}

Use the window that appears to view information on your collapsed graphs. In this example, both email and phone are marked as unique namespace, so therefore, there are no collapsed graphs in your sandbox.

{modal="regular"}

## Appendix appendix

Read this section for additional information that you can refer to when implementing your identity settings and unique namespaces.

### Dangling loginID scenario dangling-loginid-scenario

The following graph simulates a “dangling” loginID scenario. In this example, two different loginIDs are bound to the same ECID. However, {loginID: ID_C} is not linked to the CRMID. Therefore, there is no way for Identity Service to detect that these two loginIDs represent two different entities.

Ambiguous loginID
In this example, {loginID: ID_C} is left dangling and unlinked to a CRMID. Thus, the person entity that this loginID should be associated with is left ambiguous.

{modal="regular"}

loginID is linked to a CRMID
In this example, {loginID: ID_C} is linked to {CRMID: Tom}. Therfore, the system is able to discern that this loginID is associated with Tom.

{modal="regular"}

loginID is linked to another CRMID
In this example, {loginID: ID_C} is linked to {CRMID: Summer}. Therefore, the system is able to discern that this loginID is associated with another person entity, in this case, Summer.

This example also shows that Tom and Summer are to disparate person entities that are sharing a device, which is represented by {ECID: 111}.

{modal="regular"}

## Next steps

For more information on Identity Graph Linking Rules, read the following documentation:

- [Identity Graph Linking Rules overview](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/overview)
- [Identity Optimization Algorithm](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/identity-optimization-algorithm)
- [Examples of graph configurations](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/example-configurations)
- [Troubleshooting and FAQ](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/troubleshooting)
- [Namespace priority](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/namespace-priority)
- [Graph simulation UI](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/graph-simulation)
- [Identity settings UI](/en/docs/experience-platform/identity/features/identity-graph-linking-rules/identity-settings-ui)

recommendation-more-help
