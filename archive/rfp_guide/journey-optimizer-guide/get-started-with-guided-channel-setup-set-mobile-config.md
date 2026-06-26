---
title: "Get started with Guided channel setup set-mobile-config"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/guided-setup/set-mobile-config"
category: "guides"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:22.583002+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started with Guided channel setup set-mobile-config

Last update: May 8, 2026
- Topics:
- [Channel Configuration](#)

CREATED FOR:

- Experienced
- Admin

**Guided Channel Setup** is a streamlined workflow in Adobe Journey Optimizer that helps you quickly configure mobile and web marketing channels. It lives under **Administration** > **Channels** > **Channel configuration** and automates the creation of essential resources—such as tag properties, datastreams, and channel configurations—across Adobe Experience Platform, Journey Optimizer, and Data Collection. Instead of manually configuring each component, you follow a guided flow that sets everything up for you, so your marketing team can start creating In-app messages, push notifications, and web experiences without delay.

The Guided Channel Setup supports the following platforms and channels.

iOS
**SDK:** Swift by Apple

**Channels:** Mobile In-App, Mobile Push Message

Android
**SDK:** Kotlin

**Channels:** Mobile In-App, Mobile Push Message

Web
**SDK:** Javascript

**Channels:** Web Basic

Note that for each platform that you would like to setup, it is required to create a separate configuration. This is because each app requires a unique Channel Configuration, and this provides the flexibility to determine which channels you would like for each platform.

## Prerequisites prereq

- To effectively implement this, it is essential that a member of the organization with the authority and technical ability to modify website or mobile code oversees the setup. Below are the permissions required to run the Guided Channel Setup. accordion Required permissions table 0-row-2 1-row-2 2-row-2 3-row-2 Solution Permissions Data collection Company Rights > Properties Property Rights: Develop, publish, manage extensions and environments App Surfaces: Manage app Configuration Adobe Experience Platform Data Collection: Manage datastreams Sandbox: grant access to sandboxes Manage segments: read, create, edit, and delete segment definitions Manage profiles: read, create, edit, and delete profiles Read datasets: read-only access to datasets Read schemas: read-only access to schemas Read Identity namespace: read-only access to identity namespace Adobe Journey Optimizer Campaigns: Manage and publish campaigns
- If you are using the Existing configuration option, please ensure that you are using the following Adobe Experience Platform Mobile SDK extension versions. For more details on the SDK setup including the required dependencies and initialization code, please refer to the following documentation .

For iOS
- Mobile Core v5.2.0 or later
- Adobe Journey Optimizer v5.1.1 or later

For Android
- Mobile Core v3.1.0 or later
- Adobe Journey Optimizer v3.1.0 or later

## Auto-created resources auto-create-resources

The Guided Channel Setup simplifies the rapid configuration of marketing channels, making all essential resources readily available in the Experience Platform, Journey Optimizer, and Data Collection apps. This allows your marketing team to quickly start creating campaigns and journeys. Below is a list of the resources that are auto generated and configured as a part of the Guided Channel Setup.

Browse the tabs below to access the comprehensive lists of all the resources that are auto generated:

iOS
For the **Initial configuration**, below is a comprehensive list of all the resources created on the **Configuration Details** screen when you click **Auto-Create Resources**.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| **Solution** | **Auto-created resources** |
| Tags | Mobile Tag Property Rules Data Elements Library Environments (staging, production, development) |
| Tags Extensions | Adobe Experience Platform Edge Network Adobe Journey Optimizer AEP Assurance Consent (with default consent policies enabled) Identity (with default ECID, with default stitching rules) Mobile Core |
| Assurance | Assurance Session |
| Datastreams | Datastream with Services |
| Experience Platform | Dataset Schema |

For the **Channel setup**, below is a comprehensive list of all the resources created on the **Add Channels** screen.

| table 0-row-2 1-row-2 |  |
| --- | --- |
| **Solution** | **Auto-created resources** |
| Journey Optimizer | Channel Configuration Upload Push Credential (mobile push message only) |

Android
For the **Initial configuration**, below is a comprehensive list of all the resources created on the **Configuration Details** screen when you click **Auto-Create Resources**.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| **Solution** | **Auto-created resources** |
| Tags | Mobile Tag Property Rules Data Elements Library Environments (staging, production, development) |
| Tags Extensions | Adobe Experience Platform Edge Network Adobe Journey Optimizer AEP Assurance Consent (with default consent policies enabled) Identity (with default ECID, with default stitching rules) Mobile Core |
| Assurance | Assurance Session |
| Datastreams | Datastream with Services |
| Experience Platform | Dataset Schema |

For the **Channel setup**, below is a comprehensive list of all the resources created on the **Add Channels** screen.

| table 0-row-2 1-row-2 |  |
| --- | --- |
| **Solution** | **Auto-created resources** |
| Journey Optimizer | Channel Configuration Upload Push Credential (mobile push message only) |

Web
For the **Initial configuration**, below is a comprehensive list of all the resources created on the **Configuration Details** screen when you click **Auto-Create Resources**.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 |  |
| --- | --- |
| **Solution** | **Auto-created resources** |
| Tags | Mobile Tag Property Rules Data Elements Library Environments (staging, production, development) |
| Tags Extensions | Adobe Experience Platform Edge Network Adobe Journey Optimizer AEP Assurance Consent (with default consent policies enabled) Identity (with default ECID, with default stitching rules) Mobile Core |
| Assurance | Assurance Session |
| Datastreams | Datastream with Services |
| Experience Platform | Dataset Schema |

recommendation-more-help
