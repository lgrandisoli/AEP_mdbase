---
title: "Access control overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/access-control/home"
category: "overview"
topic: "experience-platform/access-control-guide"
created_at: "2026-06-26T17:21:34.724384+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Access Control Guide

# Access control overview

Last update: April 1, 2026
- Topics:
- [Access Control](#)

CREATED FOR:

- Admin

Access control for Adobe Experience Platform is provided through the **Permissions** in [Adobe Experience Cloud](https://experience.adobe.com/). This functionality leverages roles and policies, which link users with permissions and sandboxes.

## Access control hierarchy and workflow

In order to configure access control for Experience Platform, you must have system or product administrator privileges for an organization that has an Experience Platform product. The minimum role that can grant or withdraw permissions is a product administrator. Other administrator roles that can manage permissions are system administrators (no restrictions). See the Adobe Help Center article on [administrative roles](https://helpx.adobe.com/enterprise/using/admin-roles.html) for more information.

NOTE
From this point on, any mentions of “administrator” in this document refer to a product administrator or higher (as outlined above).
A high-level workflow for gaining and assigning access permissions can be summarized as follows:

- After licensing Adobe Experience Platform, or an Application/App Service that uses Experience Platform, an email is sent to the administrator specified during licensing.
- The administrator logs in to [Adobe Admin Console](#adobe-admin-console) and selects **Adobe Experience Platform** from the list of products on the overview page.
- To grant access to Experience Platform, it is recommended that the administrator add users to the default product profile: AEP-Default-All-Users.
- In Experience Platform Permissions, the administrator can create new roles or edit the permissions and users for any existing roles.
- When creating or editing a role, the administrator adds users to the role using the **users** tab, and grants permissions to these users (such as “Read Datasets” or “Manage Schemas”) by editing the role’s permissions. Similarly, the administrator can assign access to sandboxes using the same editing option.
- When users log in to the Experience Platform user interface, their access to Experience Platform capabilities is driven by the permissions that have been granted to them from the previous step. For example, if a user does not have the View Datasets permission, the **Datasets** tab in the side menu will not be visible to that user.

For more detailed steps on how to manage access control in Experience Platform, see the [access control user guide](/en/docs/experience-platform/access-control/ui/overview).

All calls to Experience Platform APIs are validated for permissions, and will return errors if the appropriate permission(s) are not found in the current user context. Within the UI, elements will be hidden or altered depending on permissions granted to the current user.

## Permissions platform-permissions

Permissions provides a central location for managing Experience Platform access for your organization. Through Permissions, you can grant groups of users access permissions for various Experience Platform capabilities, such as Manage Datasets, View Datasets, or Manage Profiles.

### Roles

In the Roles section, permissions are assigned to users through the use of roles. Roles allow you to grant permissions to one or multiple users, and also contain their access to the scope of the sandboxes that are assigned to them through roles. Users can be assigned to one or multiple roles belonging to your organization.

### Default roles

Experience Platform comes with two pre-configured default roles. The following table outlines what is provided in each default profile, including the sandbox they grant access to as well as the permissions they grant within the scope of that sandbox.

Role
Sandbox access
Permissions
Default production all access
Prod
All permissions applicable to Experience Platform, except for Sandbox Administration permissions.
Sandbox Administrators
N/A
Provides access to the
Prod
sandbox and to Sandbox Administration permissions.
## Sandboxes and permissions

Non-Production sandboxes are a form of data virtualization that allow you to isolate data from other sandboxes and are typically used for development experiments, testing, or trials. A role’s permissions give the role’s users access to Experience Platform features within the sandbox environments to which they’ve been granted access to. A default Experience Platform license grants you five sandboxes (one production and four non-production). You can add packs of ten non-production sandboxes up to a maximum of 75 sandboxes in total. Please contact your organization’s administrator or your Adobe sales representative for more details.

For more information about sandboxes in Experience Platform, please refer to the [sandboxes overview](/en/docs/experience-platform/sandbox/home).

### Access to sandboxes

Access to sandboxes is managed through roles. For detailed steps on how to enable access to a sandbox for a role, see the [attribute based access control roles guide](/en/docs/experience-platform/access-control/abac/permissions-ui/roles).

Users can be granted access to one or more sandboxes within a role. If one user is included in two or more roles, that user will have access to all sandboxes included in those roles.

The “Sandbox Management” permission allows users to manage, view, or reset sandboxes.

### Resource permissions permissions

Resource permissions grant access to specific Experience Platform capabilities. Resources are broken down into categories that contain a set of relevant permissions, which can be individually assigned to roles.

In Permissions, a role’s resources workspace displays the sandboxes and permissions that are active for that role:

The following table outlines the available resource categories for both Experience Platform and applications managed through Permissions:

Category
Description
Adobe Mix Modeler
Configure, manage, and view permissions for Adobe Mix Modeler.
AI Assistant
Configure permissions for AI Assistant.
Alerts
Configure manage, resolve, and view permissions for alerts and alerts history.
B2B Account Lists
Configure manage, view, and publish permissions for B2B account lists, including actions such as add, remove, import, and delete accounts from account lists.
B2B Admin Configurations
Configure manage and view permissions for B2B admin configurations, including digital asset management connections, asset repositories, and events.
B2B Assets
Configure manage and view permissions for B2B assets, including emails, SMS, landing pages, fragments, templates, and images.
B2B Buying Groups
Configure manage and view permissions for B2B buying groups, including features such as solution interests, roles templates, and buying group status.
B2B Channel Configurations
Configure manage and view permissions for B2B channel configurations, including settings such as communication limits, API credentials, and security settings.
B2B Dashboards
Configure view permissions for B2B dashboards, including features such as account engagement, buying group stages, surging accounts, and contact coverage.
B2B Journeys
Configure manage, view, and publish permissions for B2B journeys, including features such as account and person actions, event listeners, and split paths.
Campaigns
Configure manage, publish, and view permissions to campaigns in Journey Optimizer.
Channel Configurations
Configure manage, view, and export channel configurations features such as subdomains, IP pools, message presets, PTR records, suppression lists, landing page settings, SMS settings, and file routing.
Collaborations
Configure manage and view permissions to Real-Time Customer Data Profile Collaboration features.
Computed Attributes
Configure manage and view permissions to draft or published computed attributes.
Customer Managed Keys
Configure manage permissions to customer managed keys.
Dashboards
Configure manage and view permissions to standard, custom, and licensed dashboards.
Data Collection
Configure manage and view permissions to datastreams.
Data Governance
Configure manage, apply, and view permissions to data Ggvernance features such as labels, policies, and activity logs.
Data Ingestion
Configure manage and view permissions to data ingestion features such as sources and audience share.
Data Lifecycle
Configure manage and view permissions to data hygiene features.
Data Management
Configure manage and view permissions to data management features such as datasets and monitoring datasets and streams.
Data Modeling
Configure manage and view permissions to data modeling features such as schemas, relationships, and identity metadata.
Data Science Workspace
Configure manage permissions to Data Science Workspace.
Decision Management
Configure manage and view permissions to decisions, offers, and ranking strategy features in decision management.
Destinations
Configure manage and view permissions to destinations, including features such as activation and authoring with Destinations SDK.
Federated Data
Configure manage and view permissions to federated data features.
Identity Management
Configure manage and view permissions to Identity Service features such as identity namespaces and the identity graph.
Intelligent Service
Configure manage and view permissions to attribution AI and customer AI in intelligent service.
IP Warmup Configurations
Configure manage and view permissions to IP warmup plans and view permissions to view IP warmup reports.
Journey Optimizer Library
Configure manage permissions to library items in Adobe Journey Optimizer.
Journey Optimizer Rules
Configure manage and view permissions to frequency rules in Adobe Journey Optimizer.
Journeys
Configure manage, publish, and view permissions to journeys, including features such as journeys report, events, data sources, and actions.
Messages
Configure manage, publish, and view permissions to messages, including features such as messages preview and test.
Privacy Service
Configure manage and view permissions to Privacy Service features.
Profile Management
Configure manage, view, export, and evaluation permissions to profile service features such as audiences, profiles, and merge policies.
Prospects
Configure manage and view permissions to prospects schemas, profiles, and audiences, including features such as seeing the prospect accordion.
Query Service
Configure manage permissions to query service features such as non-expiring credential and structured SQL queries.
Reports
Configure view permissions to channel reports.
Run and Operate
Configure view permissions for Run and Operate features such as health checks and job schedules.
Sandbox Administration
Configure manage, view, and reset permissions when administering sandboxes.
Traits Configuration
Configure manage and view traits via the computed attributes UI.
Translation Services
Configure manage and view permissions to translation services for projects, tasks, reviews, inhouse, settings, and providers.
The following table outlines the available permissions for Experience Platform in the role, with descriptions of the specific Experience Platform capabilities they grant access to. For detailed steps on how to add permissions to a role, see the [attribute based access control roles guide](/en/docs/experience-platform/access-control/abac/permissions-ui/roles).

Category
Permission
Description
Adobe Mix Modeler
Manage Adobe Mix Modeler Harmonized Data
The ability to view and modify harmonized data.
Adobe Mix Modeler
View Adobe Mix Modeler Harmonized Data
Read-only access to harmonized data.
Adobe Mix Modeler
Manage Adobe Mix Modeler Models Configurations
The ability to view and modify models configurations.
Adobe Mix Modeler
View Adobe Mix Modeler Models Configurations
Read-only access to models configurations.
Adobe Mix Modeler
Manage Adobe Mix Modeler Models Plans Configurations
The ability to view and modify plans configurations.
Adobe Mix Modeler
View Adobe Mix Modeler Models Plans Configurations
Read-only access to plans configurations.
AI Assistant
Enable AI Assistant
Ability to ask the
AI assistant
questions.
AI Assistant
View Operational Insights
Access to obtain responses to
operational insights
queries.
AI Assistant
Generate Content
Enable users to generate content using the AI Assistant.
AI Assistant
Manage Brand Kit
Enable users to create brand guidelines using the AI Assistant.
Alerts
View Alerts History
Read-only access for alerts history.
Alerts
Resolve Alerts
Access to read, edit, and delete alerts.
Alerts
View Alerts
Read-only access for alerts.
Alerts
Manage Alerts
Access to read, create, edit, and delete alerts.
B2B Account Lists
Manage B2B Account Lists
Ability to view and access
Account Lists
in the left nav. Users with access to
Account Lists
should have access to all Account Lists CRUD functions:
/accounts-list
.
B2B Admin Configurations
Manage B2B Admin Configurations
Ability to view and access
B2B Admin Configurations
in the left nav. Users with access to
B2B Admin Configurations
should have access to all SMS API Credentials CRUD functions:
/admin-configs
.
B2B Assets
Manage B2B Assets
Ability to view and access
Assets
in the left nav. Users with access to
Assets
should have access to all Assets CRUD functions:
/assets-listing
.
B2B Assets
Manage B2B Templates
Ability to view and access
Templates
in the left nav. Users with access to
Templates
should have access to all Templates CRUD functions:
/b2b-content-templates
.
B2B Assets
Manage B2B Fragments
Ability to view and access
Fragments
in the left nav. Users with access to
Fragments
should have access to all Fragments CRUD functions:
/fragments
.
B2B Buying Groups
Manage B2B Buying Groups
Ability to view and access
Buying Groups
in the left nav. Users with access to
Buying Groups
should have access to all Buying Groups CRUD functions:
/buying-groups
.
B2B Dashboards
Manage B2B Engagement Dashboards
Ability to view and access
Dashboard
in the left nav. Users with access to
Dashboards
should have access to all Dashboards CRUD functions:
/insights-dashboard
.
B2B Channel Configurations
Manage B2B Channels Configurations
Ability to view and access
Channels
in the left nav. Users with access to
Channels
should have access to all Channels CRUD functions:
/channels-config
.
B2B Journeys
Manage B2B Account Journeys
Ability to view and access
Account Journeys
in the left nav. Users with access to
Account Journeys
should have access to all Account Journeys CRUD functions:
/account-journeys
.
Campaigns
Manage Campaigns
Access to read, create, edit, and delete campaigns.
Campaigns
Approve and Publish Campaigns
The ability to approve and publish campaigns.
Campaigns
Publish Campaigns
Ability to publish campaigns.
Campaigns
View Campaigns
Read-only access to campaigns.
Campaigns
View Campaigns Report
Read-only access to campaign reports.
Channel Configurations
View Messages General Settings
Read-only access to messages general settings.
Channel Configurations
Manage Subdomains Delegations
Access to read, create, edit, and delete subdomain delegations.
Channel Configurations
Manage IP Pools
Access to read, create, and edit IP pools.
Channel Configurations
Manage Messages General Settings
Access to read, create, edit, and delete messages general settings.
Channel Configurations
Manage Messages Presets
Access to read, create, edit, and delete messages presets.
Channel Configurations
View Messages Presets
Read-only access to messages presets.
Channel Configurations
Manage PTR Records
Access to read and edit PTR records.
Channel Configurations
View PTR Records
Read-only access to PTR records.
Channel Configurations
Manage Suppression
Access to read, create, edit, and delete suppression rules.
Channel Configurations
View Suppression List
Read-only access to the suppression list.
Channel Configurations
Export Suppression List
Access to export the suppression list as a CSV file.
Channel Configurations
Manage Landing Page Settings
Access to read, create, edit, and delete landing page settings.
Channel Configurations
Manage SMS Settings
Access to read, create, edit, and delete SMS settings.
Channel Configurations
Manage SMS Subdomains
Access to read, create, edit, and delete SMS subdomains.
Channel Configurations
Manage File Routing
Access to read, create, edit, and delete file routings.
Channel Configurations
View File Routing
Read-only access to file routings.
Channel Configurations
Manage Seedlist
The ability to create and edit the Seedlist.
Channel Configurations
Manage Language Settings
The ability to create and edit the language settings.
Channel Configurations
Manage Web Subdomains
The ability to create and edit CJM web subdomains.
Channel Configurations
Manage Push Credentials
The ability to create, edit, and delete push credentials.
Collaborations
Manage Collaboration Instances
View, create, update, and delete an organization’s collaboration instances. Discover other organizations’ collaboration instances.
Collaborations
Read Collaboration Instances
Read an organization’s collaboration instances and discover other organizations’ collaboration instances.
Collaborations
Manage Connection Invites
View, create, and delete connection invites initiated by your organization. Accept and decline connection invite initiated by other organizations.
Collaborations
Read Connection Invites
Read-only access to connection invites.
Collaborations
Manage Collaboration Connections
An advertiser can view, create, and update settings as well as submit and delete connections. A publisher can view, accept, or decline connections.
Collaborations
Read Collaboration Connections
Read-only access to connections.
Collaborations
Manage Audience Data
Onboard and discover audiences. Update public, private, and custom audiences and manage Audience Inventory metadata settings.
Collaborations
Read Audience Data
Read and discover audiences.
Collaborations
Manage Measurement Data
Onboard, update, and delete measurement data.
Collaborations
Read Measurement Data
Read-only access to measurement data.
Collaborations
Manage Projects
View, create, update, and delete projects for any of the discover, share, activate, and measurement activities.
Collaborations
Read Projects
View projects for any of the discover, share, activate, and measurement activities.
Collaborations
Read User Activities
Read-only access to user activities.
Collaborations
Export User Activities
Export user activities.
Collaborations
Read Collaboration Credit Monitoring
Credit monitoring at the organization and instance level.
Computed Attributes
View Computed attributes
Read-only access for computed attributes tab, inventory, and details.
Computed Attributes
Manage Computed attributes
Access to read, create, delete drafts, and deactivate computed attributes.
Customer Managed Keys
Manage Customer Managed Keys
Access to view and configure customer managed keys.
Dashboards
View License Usage Dashboard
Read-only access to view the license usage dashboard.
Dashboards
Manage Standard Dashboards
Add custom attributes that are not yet in the data warehouse.
Dashboards
View Standard Dashboards
Read-only access to the Profiles, Destinations, and Segments dashboards. Also enables access to Dashboards in the left navigation and the Dashboards inventory and integrations tab.
Dashboards
Manage Custom Dashboards
Access to create or edit a dashboard.
Dashboards
View Custom Dashboards
Read-only access to user defined dashboards.
Dashboards
Manage Report Schedules
Ability to create schedules.
Dashboards
Export Dashboard Data
Controls a user’s ability to export tabular data from query pro mode dashboards.
Data Collection
Manage Datastreams
Access to read, create, and edit datastreams.
Data Collection
View Datastreams
Read-only access to datastreams.
Data Governance
Manage Usage Labels
Access to read, create, and delete usage labels.
Data Governance
Manage Data Usage Policies
Access to read, create, edit, and delete data usage policies.
Data Governance
View Data Usage Policies
Read-only access for data usage policies belonging to your organization.
Data Governance
View User Activity Log
Read-only access to view recorded
audit logs
of Experience Platform activities.
Data Governance
View Privacy Console
Read-only access to privacy consoles.
Data Ingestion
Manage Sources
Access to read, create, edit, and disable sources.
Data Ingestion
View Sources
Read-only access to available sources in the
Catalog
tab and authenticated sources in the
Browse
tab.
Data Ingestion
Manage Audience Share Connections
Access to create, accept, and decline partner sharing to connect two organizations and enable Segment Match flows.
Data Ingestion
Manage Audience Share
Access to read, create, edit, and publish Segment Match feeds with active partners.
Data Lifecycle
View Data Lifecycle
Read-only access for data lifecycle.
Data Lifecycle
Manage Data Lifecycle
Access to read, create, edit, and delete data lifecycle.
Data Modeling
Manage Schemas
Access to read, create, edit, and delete schemas and related resources.
Data Modeling
View Schemas
Read-only access to schemas and related resources.
Data Modeling
Manage Relationships
Access to read, create, edit, and delete schema relationships.
Data Modeling
Manage Identity Metadata
Access to read, create, edit, and delete identity metadata for schemas.
Data Management
Manage Datasets
Access to read, create, edit, and delete datasets. Read-only access for schemas.
Data Management
View Datasets
Read-only access for datasets and schemas.
Data Management
Data Monitoring
Read-only access to monitoring datasets and streams.
Data Science Workspace
Manage Data Science Workspace
Access to read, create, edit, and delete in Data Science Workspace.
Decision Management
Manage Experience Decisioning
Ability to manage experience decisioning entities.
Decision Management
View Experience Decisioning
Read-only access to experience decisioning entities.
Decision Management
Manage Decisions
Access to read, create, edit, and delete decisioning entities.
Decisions Management
View Decisions
Read-only access to decision entities.
Decision Management
Manage Offers
Access to read, create, edit, and delete all offers and components. Read-only access to decisions and collections.
Decsion Management
Manage Ranking Strategies
Access to read, create, edit, and delete custom reports and use action features.
Destinations
View Destinations
Read-only access to view available destinations in the
Catalog
tab and authenticated destinations in the
Browse
tab.
Destinations
Manage Destinations
Access to read, create, and delete destinations connections and destination accounts.
Destinations
Activate Destinations
Ability to activate data to active destinations that have been created. This permission also requires either View Destinations or Manage Destinations to be granted to the user who will activate destinations.
Destinations
Activate Segment without Mapping
The ability to activate audiences to existing destinations, without displaying the
mapping step
. Users can add and remove audiences in activation workflows, but cannot add or remove mapped attributes or identities. This permission also requires the View Destinations permission to be granted to the user who will activate data to destinations.
Destinations
Manage and Activate Dataset Destinations
Ability to read, create, edit, and disable dataset export flows. Ability to also activate data to active datasets that have been created. This permission also requires the View Destinations permission to be granted to the user who will activate data to destinations.
Destinations
Destination Authoring
Ability to author destinations using
Adobe Experience Platform Destination SDK
.
Federated Data
Manage Federated Data
The ability to access all federated data features such as creating schemas, models, and compositions.
Identity Management
Manage Identity Namespaces
Access to read, create, edit, and delete identity namespaces.
Identity Management
View Identity Namespaces
Read-only access for identity namespaces.
Identity Management
View Identity Graph
Read-only access for identity graphs.
Identity Management
Manage Identity Settings
Access to read, create, and edit identity settings.
Identity Management
View Identity Settings
Read-only access to identity settings.
Intelligent Services
View Attribution AI
Read-only access for Attribution AI settings and insights.
Intelligent Services
Manage Attribution AI
Access to read, create, edit, and delete Attribution AI models.
Intelligent Services
View Customer AI
Access to read or view Customer AI models.
Intelligent Services
Manage Customer AI
Access to create, update, delete, enable, or disable Customer AI models.
IP Warmup Configurations
View IP Warmup Plans
Read-only access to IP warmup plans.
IP Warmup Configurations
Manage IP Warmup Plans
The ability to manage IP warmup plans.
IP Warmup Configurations
View IP Warmup Reports
Read-only access to IP warmup reports.
Journeys
Manage Journeys
Access to read, create, edit, and delete journeys.
Journeys
View Journeys
Read-only access to journeys.
Journeys
View Journeys Report
Read-only access to journeys report.
Journeys
Manage Journeys Events, Data Sources and Actions
Access to read, create, edit, and delete events, data sources, or actions.
Journeys
View Journeys Events, Data Sources and Actions
Read-only access to events, data sources, or actions.
Journeys
Approve and Publish Journeys
Ability to approve and publish journeys when a policy is applied.
Journeys
Publish Journeys
Ability to publish journeys.
Journey Optimizer Library
Manage Library Items
The ability to add and delete saved expressions.
Journey Optimizer Library
Publish Fragments
The ability to publish content fragments.
Journey Optimizer Library
Simulate Content
Access to the simulate content option for previewing and proofing.
Journey Optimizer Rules
View Frequency Rules
Read-only access to frequency rules.
Journey Optimizer Rules
Manage Frequency Rules
Access to read, create, edit, or delete frequency rules.
Messages
Manage Messages
Access to read, create, edit, and delete messages.
Messages
View Messages
Read-only access to messages.
Messages
View Messages Report
Access to read and edit message reports.
Messages
Publish Messages
Ability to publish messages.
Messages
Manage Messages Preview and Test
Ability to approve and publish messages when a policy is applied.
Privacy Service
Manage Privacy Service
Access to read and write privacy workflows.
Privacy Service
View Privacy Service
Read-only access to privacy workflows.
Profile Management
Manage Profiles
Access to read, create, edit, and delete datasets that are used for customer profiles. Read-only access to available profiles.
Profile Management
View Profiles
Read-only access to available profiles.
Profile Management
Manage Segments
Access to read, create, edit, and delete audiences.
Profile Management
View Segments
Read-only access to available audiences.
Profile Management
Manage Merge Policies
Access to read, create, edit, and delete merge policies.
Profile Management
View Merge Policies
Read-only access to available merge policies.
Profile Management
Import Audiences
Ability to use the CSV upload workflow to import new audiences.
Profile Management
Export Audience Segment
Ability to export an evaluated audience to a dataset.
Profile Management
Evaluate a Segment to an Audience
Ability to generate profiles for an audience by evaluating a segment definition.
Profile Management
View B2B AI
Read-only access to settings and configurations for all B2B AI/ML services.
Profile Management
Manage B2B AI
Access to read, create, edit, and delete settings and configurations for all B2B AI/ML services.
Profile Management
View B2B Profile
Read-only access to B2B entity profiles (such as Account, Opportunity, and so on), settings and configurations for all B2B AI/ML services, and B2B dashboard widgets.
Profile Management
Manage B2B Profile
Access to read, create, edit, and delete B2B entity profiles (such as Account, Opportunity, and so on). Read-only access for settings and configurations for all B2B AI/ML services, and B2B dashboard widgets.
Profile Management
Manage Lookalikes
Ability to create or delete look-alike audiences.
Profile Management
View B2B Experience
Ability to view B2B profiles and attributes.
Profile Management
View Profile Settings
Read-only access to all profile settings.
Profile Management
Manage Profile Settings
Access to read and edit all profile settings.
Prospects
View Prospects
Read-only access to prospect schemas, profiles, audiences, and the prospect accordion.
Prospects
Manage Prospects
Ability to create and manage prospect schemas, profiles, and audiences. Read-only access to the prospect accordion.
Query Service
Manage Queries
Access to read, create, edit, and delete structured SQL queries for Experience Platform data.
Query Service
Manage Query Service Integration
Access to create, update, and delete non-expiring credentials for Query Service access.
Query Service
Manage Query Sessions
Ability to evict existing sessions.
Query Service
Manage Allow List
Ability to manage IP restrictions for your organization.
Reports
View Channel Reports
The ability to view and modify channel reports.
Run and Operate
View Health Checks
Read-only access to health checks.
Run and Operate
View Job Schedules
Read-only access to job schedules.
Sandbox Administration
Manage Sandboxes
Access to read, create, edit, and delete sandboxes.
Sandbox Administration
View Sandboxes
Read-only access for sandboxes belonging to your organization.
Sandbox Administration
Reset a Sandbox
Ability to reset a sandbox.
Sandbox Administration
Manage Packages
Access to create, import, or export packages.
Sandbox Administration
Share Packages
Access to share packages across different organizations.
Traits Configurations
View Traits
Read-only access for traits.
Traits Configurations
Manage Traits
Access to manage traits.
Translation Service
Manage Translation Projects
The ability to manage translation projects.
Translation Service
View Translation Projects
Read-only access to translation projects.
Translation Service
Manage Translation Tasks
The ability to manage translation tasks.
Translation Service
View Translation Tasks
Read-only access to translation tasks.
Translation Service
Manage Translation Reviews
The ability to manage translation reviews.
Translation Service
View Translation Reviews
Read-only access to translation reviews.
Translation Service
Manage Translation In-house
The ability to manage translation in-house.
Translation Service
View Translation In-house
Read-only access to translation in-house.
Translation Service
Manage Translation Settings
The ability for administrators to manage translation settings.
Translation Service
Manage Translation Providers
The ability to manage translation providers.
## Next steps

By reading this guide, you have been introduced to the main principles of access control in Experience Platform. You can now continue to the [attribute based access control user guide](/en/docs/experience-platform/access-control/abac/overview) for detailed steps on how use Experience Cloud to create roles and assign permissions for Experience Platform.

recommendation-more-help
