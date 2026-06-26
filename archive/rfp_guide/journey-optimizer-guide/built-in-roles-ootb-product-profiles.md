---
title: "Built-in roles ootb-product-profiles"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/access-control/ootb-product-profiles"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:21.695319+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Built-in roles ootb-product-profiles

Last update: May 8, 2026
- Topics:
- [Access Management](#)

CREATED FOR:

- Intermediate
- Admin
- User

Built-in roles are a set of unitary rights which allows users access to certain functionalities or objects in the interface. Refer to [this page](/en/docs/journey-optimizer/using/access-control/ootb-permissions) for the list of available permissions to build your role.

## Campaign Administrator campaign-administrator

The **Campaign Administrator** role allows the administration menus with the possibility to manage and publish Campaigns and Decision management.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **Read Identity namespace**: read-only access to identity namespace.
- **View schemas**: read-only access to schemas.
- **Sandbox**: grant access to sandboxes.

Campaigns
- **Manage campaigns**: read, create, edit, and delete campaigns.
- **Publish campaigns**: publish campaigns.
- **View campaigns report**: read and edit campaigns report.

Channel configurations
- **Export suppression list**: access to export suppression list as a CSV file.
- **Manage alerts**: enable/disable alerts for campaigns, messages and entitlements.
- **Manage IP pools**: read, create, edit, and delete ip pool.
- **Manage landing page settings**: read, create, edit, and delete landing page settings.
- **Manage messages general settings**: read, create, edit, and delete message general settings.
- **Manage messages presets**: read, create, edit, and delete content branding.
- **Manage PTR records**: read and edit PTR records.
- **Manage SMS settings**: read, create, edit, and delete SMS settings.
- **Manage subdomains delegation**: read, create, edit, and delete subdomain delegation.
- **Manage suppression rules**: access read, create, edit and delete suppression rules.
- **View PTR records**: read-only access to PTR records.
- **View suppression list**: read and export local suppression list.

Decision management
- **Manage decisions**: read, create, edit, and delete decisions.
- **Manage ranking strategies**: read, create, edit, and delete ranking strategies.

## Campaign Approver campaign-approver

The **Campaign Approver** role allows users to approve deliveries and publish them. They can later check the success of their deliveries with the **Campaigns** reports.

Resources
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **Manage profiles**: read, create, edit, and delete profiles.
- **View datasets**: read-only access to datasets.
- **View schemas**: read-only access to schemas.

Campaigns
- **Manage campaigns**: read, create, edit, and delete campaigns.
- **Publish campaigns**: publish campaigns.
- **View campaigns report**: read, edit campaign reports.

Channel configurations
- **View messages presets**: read-only access to messages presets.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom messages reports and use action features.

## Campaign Manager campaign-manager

The **Campaign Manager** role allows users to create and edit **Campaigns** and every capability linked to **Campaigns** but will not be able to publish them.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **View schemas**: read-only access to schemas.

Campaigns
- **Manage campaigns**: read, create, edit, and delete campaigns.
- **View campaigns report**: read, edit journey report.

Channel configurations
- **View messages presets**: read-only access to messages presets.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom messages reports and use action features.

## Campaign Viewer campaign-viewer

The **Campaign Viewer** role allows read-only access to the **Campaigns** and **Decision management** capabilities.

Users assigned to this role will not be able to edit or publish.

This role includes the following permissions:

Resources
Permissions
Campaigns
- **View campaigns**: read-only access to campaigns.
- **View campaigns report**: read-only access to campaigns reports.

Decision management
- **View decisions**: read-only access to decisions entities.

## Content Library Manager content-library-manager

The **Content Library Manager** role only allows access to the **Content templates** menu. Users assigned to this role will only be able to access the template library to create content without accessing the journeys or campaigns.

This permission includes the following permissions:

Capability
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **View schemas**: read-only access to schemas.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom reports and use action features.

Journey Optimizer Library
- **Manage library items**: read, create, edit, and delete Journey Optimizer Library items, including content templates and fragments.
- **Manage simulate content**: access to the **Simulate content** option for preview and proof.
- **Publish Fragment**: publish content fragments.

## Decisioning manager decisioning-manager

The **Decisioning manager** role only allows access to the **Decision management** menu. Users assigned to this role will only be able to manage, view and publish decisions.

This permission includes the following permissions:

Capability
Permissions
Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom reports and use action features.
- **View decisions**: read-only access to decisioning entities.
- **Publish decisions**: activate or deactivate decisioning activities.li>**Manage Experience decisions**: read, create, edit, and delete Decisioning entities.</li

## Journey Administrator journey-administrator

The **Journey Administrator** role allows the administration menus with the possibility to manage and publish Journeys and Decision management.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **Read Identity namespace**: read-only access to identity namespace.
- **View schemas**: read-only access to schemas.
- **Sandbox**: grant access to sandboxes.

Channel configurations
- **Manage alerts**: enable/disable alerts for journeys and entitlements.
- **Manage IP pools**: read, create, edit, and delete ip pool.
- **Manage Landing page settings**: create, edit and delete Landing page subdomains and Landing page presets.
- **Manage messages general settings**: read, create, edit, and delete message general settings.
- **Manage messages presets**: read, create, edit, and delete content branding.
- **Manage PTR records**: read and edit PTR records.
- **Manage SMS settings**: create, edit and delete API credentials and SMS channel configurations required to enable SMS channel.
- **Manage subdomains delegation**: read, create, edit, and delete subdomain delegation.
- **Manage suppression rules**: access read, create, edit and delete suppression rules.
- **View PTR records**: read-only access to PTR records.
- **View suppression list**: read and export local suppression list.

Data Governance
- **Manage data usage policies**: read, create, edit, and delete data usage policies.
- **Manage usage label**: read, create, and delete usage labels.
- **View data usage policies**: read-only access to data usage policies.
- **View user activity log**: read-only access to view recorded audit logs of Experience Platform activities…

Decision management
- **Manage decisions**: read, create, edit, and delete decisions.
- **Manage ranking strategies**: read, create, edit, and delete ranking strategies.

Journeys
- **Manage journeys**: read, create, edit, stop (live, test mode and dry run) and delete journeys.
- **Manage journeys events, data sources and actions**: read, create, edit, and delete events, sources or actions.
- **Publish journeys**: publish, start test mode, start dry run, pause and resume journeys.
- **View journeys report**: read and edit journeys report.

Journey Optimizer Library
- **Manage Library Items**: add and delete saved expressions in the Journey Optimizer Library.

## Journey Approver journey-approver

The **Journey Approver** role allows users to approve deliveries and publish them. They can later check the success of their deliveries with the **Journey** reports.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **View schemas**: read-only access to schemas.

Channel configurations
- **View channel configurations**: read-only access to channel configurations.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom reports and use action features.

Journeys
- **Manage journeys**: read, create, edit, stop (live, test mode and dry run) and delete journeys.
- **Publish journey**: publish, start test mode, start dry run, pause and resume journeys.
- **View journeys events, data sources and actions**: read-only access to journey events, journey custom actions and journey data sources sources.
- **View journeys report**: read, edit journey reports.

## Journey Manager journey-manager

The **Journey Manager** role allows users to create and edit **Journeys** and every capability linked to **Journeys** but will not be able to publish them.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **View schemas**: read-only access to schemas.

Channel configurations
- **View channel configurations**: read-only access to channel configurations.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom reports and use action features.

Journeys
- **Manage journeys**: read, create, edit, stop (live, test mode and dry run) and delete journeys.
- **View journeys events**: read-only access to journey events, journey custom actions and journey data sources sources.
- **View journeys report**: read, edit journey report.

## Journey Viewer journey-viewer

The **Journey viewer** role allows read-only access to the **Journeys** and **Decision management** capabilities.

Users assigned to this role will not be able to edit or publish.

This role includes the following permissions:

Resources
Permissions
Decision management
- **View decisions**: read-only access to decisions entities.

Journeys
- **View journeys**: read-only access to journeys.
- **View journeys event, data sources, actions**: read-only access to journeys events and data sources.
- **View journeys report**: read-only access to journeys reports.

## Orchestrated Campaign Administrators orchestrated-campaign-administrator

The **Orchestrated Campaign Administrator** role allows the administration menus with the possibility to manage and publish Orchestrated campaigns.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Enable AI Assistant**: enable or access AI-powered campaign and audience features.
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **Read Identity namespace**: read-only access to identity namespace.
- **View schemas**: read-only access to schemas.
- **Sandbox**: grant access to sandboxes.
- **View operational insights**: read-only access to system-level insights and monitoring dashboards.

Channel configurations
- **Export suppression list**: access to export suppression list as a CSV file.
- **Manage alerts**: enable/disable alerts for campaigns, messages and entitlements.
- **Manage custom dashboards**: read, create, edit, and delete custom dashboards.
- **Manage IP pools**: read, create, edit, and delete ip pool.
- **Manage landing page settings**: read, create, edit, and delete landing page settings.
- **Manage messages general settings**: read, create, edit, and delete message general settings.
- **Manage messages presets**: read, create, edit, and delete content branding.
- **Manage PTR records**: read and edit PTR records.
- **Manage SMS settings**: read, create, edit, and delete SMS settings.
- **Manage subdomains delegation**: read, create, edit, and delete subdomain delegation.
- **Manage suppression rules**: access read, create, edit and delete suppression rules.
- **View PTR records**: read-only access to PTR records.
- **View suppression list**: read and export local suppression list.

Dashboard
- **Manage standard dashboard**: read, create, edit and delete custom widgets and widget schema through the Widget library.

Data governance
- **View user activity log**: read-only access to view recorded audit logs of Experience Platform activities.

Data ingestion
- **Manage sources**: read, create, edit, and disable sources.

Data management
- **Manage datasets**: read, create, edit, and delete datasets.

Data modelling
- **Manage schemas**: read, create, edit, and delete schemas and related resources.

Decision management
- **Manage decisions**: read, create, edit, and delete decisions.
- **Manage ranking strategies**: read, create, edit, and delete ranking strategies.

Journey Optimizer rules
- **View frequency rules**: read-only access to frequency rules.
- **Manage frequency rules**: read, create, edit, or delete frequency rules.

Messages
- **Manage Messages**: read, create, edit, and delete messages.
- **Manage Messages Preview and Test** : approve and publish messages when a policy is applied. **Publish Messages**: publish messages.
- **View Messages Report**: read and edit message reports.

Orchestrated campaigns
- **Manage orchestrated campaigns**: read, create, edit, and delete Orchestrated campaigns.
- **Manage orchestrated campaigns admin**: read, create, edit and delete links and reconciliations between Adobe Experience Platform Profiles and Relational store entities.
- **Publish orchestrated campaigns**: publish Orchestrated campaigns.
- **View orchestrated campaigns report**: read and edit Orchestrated campaigns report.

## Orchestrated Campaign Approver orchestrated-campaign-approver

The **Orchestrated Campaign Approver** role allows users to publish Orchestrated campaigns.

Resources
Permissions
Adobe Experience Platform
- **Manage segments**: read, create, edit, and delete segment definitions.
- **Manage profiles**: read, create, edit, and delete profiles.
- **View datasets**: read-only access to datasets.
- **View schemas**: read-only access to schemas.
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Enable AI Assistant**: enable or access AI-powered campaign and audience features.
- **View operational insights**: read-only access to system-level insights and monitoring dashboards.

Channel configurations
- **View messages presets**: read-only access to messages presets.
- **Manage custom dashboards**: create, edit, and delete custom dashboards.

Dashboard
- **Manage standard dashboard**: read, create, edit and delete custom widgets and widget schema through the Widget library.

Data governance
- **View user activity log**: read-only access to view recorded audit logs of Experience Platform activities.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom messages reports and use action features.

Journey Optimizer rules
- **View frequency rules**: read-only access to frequency rules.

Messages
- **Manage Messages**: read, create, edit, and delete messages.
- **Manage Messages Preview and Test** : approve and publish messages when a policy is applied. **Publish Messages**: publish messages.
- **View Messages Report**: read and edit message reports.

Orchestrated campaigns
- **Manage orchestrated campaigns**: read, create, edit, and delete Orchestrated campaigns.
- **Publish orchestrated campaigns**: publish Orchestrated campaigns.
- **View orchestrated campaigns admin**: read-only access to links and reconciliations between Adobe Experience Platform Profiles and Relational store entities.
- **View orchestrated campaigns report**: read, edit Orchestrated campaign reports.

## Orchestrated Campaign Manager orchestrated-campaign-manager

The **Orchestrated Campaign Manager** role allows users to create and edit **Orchestrated campaigns** and every capability linked to **Orchestrated campaigns** but will not be able to publish them.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Enable AI Assistant**: enable or access AI-powered campaign and audience features.
- **Manage merge policies**: read, create, edit, and delete merge policies.
- **Manage profiles**: read, create, edit, and delete profiles.
- **Manage segments**: read, create, edit, and delete segment definitions.
- **View datasets**: read-only access to datasets.
- **View operational insights**: read-only access to system-level insights and monitoring dashboards.
- **View schemas**: read-only access to schemas.

Channel configurations
- **Manage custom dashboards**: create, edit, and delete custom dashboards.
- **View messages presets**: read-only access to messages presets.

Dashboard
- **Manage standard dashboard**: read, create, edit and delete custom widgets and widget schema through the Widget library.

Data governance
- **View user activity log**: read-only access to view recorded audit logs of Experience Platform activities.

Decision management
- **Manage decisions**: read, create, edit, and delete decisioning entities.
- **Manage ranking strategies**: read, create, edit, and delete custom messages reports and use action features.

Journey Optimizer rules
- **View frequency rules**: read-only access to frequency rules.

Messages
- **Manage Messages**: read, create, edit, and delete messages.
- **Manage Messages Preview and Test** : approve and publish messages when a policy is applied. **View Messages Report**: read and edit message reports.

Orchestrated campaigns
- **Manage orchestrated campaigns**: read, create, edit, and delete Orchestrated campaigns.
- **View orchestrated campaigns report**: read, edit Orchestrated campaigns.
- **View orchestrated campaigns admin**: read-only access to links and reconciliations between Adobe Experience Platform Profiles and Relational store entities.

## Orchestrated Campaign Viewer orchestrated-campaign-viewer

The **Campaign Viewer** role allows read-only access to the **Orchestrated campaigns** capabilities.

Users assigned to this role will not be able to edit or publish.

This role includes the following permissions:

Resources
Permissions
Adobe Experience Platform
- **Enable AI Assistant**: enable or access AI-powered campaign and audience features.
- **View operational insights**: read-only access to system-level insights and monitoring dashboards.

Channel configurations
- **Manage custom dashboards**: create, edit, and delete custom dashboards.

Dashboard
- **Manage standard dashboard**: read, create, edit and delete custom widgets and widget schema through the Widget library.

Data governance
- **View user activity log**: read-only access to view recorded audit logs of Experience Platform activities.

Decision management
- **View decisions**: read-only access to decisions entities.

Journey Optimizer rules
- **View frequency rules**: read-only access to frequency rules.

Orchestrated campaigns
- **View orchestrated campaigns**: read-only access to Orchestrated campaigns.
- **View orchestrated campaigns report**: read-only access to Orchestrated campaigns reports.

recommendation-more-help
