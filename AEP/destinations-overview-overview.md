---
title: "Destinations overview overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/destinations/home"
category: "overview"
topic: "experience-platform/destinations-guide"
created_at: "2026-05-29T16:55:03.272036+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Destinations Guide

# Destinations overview overview

Last update: May 23, 2026
- Topics:
- [Destinations](#)

CREATED FOR:

- Admin
- User

**Destinations** are pre-built integrations with destination platforms that allow for the seamless activation of data from Adobe Experience Platform. You can use destinations to activate your known and unknown data for cross-channel marketing campaigns, email campaigns, targeted advertising, and many other use cases.

recs-overview-body-1
recs-overview-body-2
recs-overview-body-3
recs-overview-body-4
recs-overview-body-5
recs-overview-body-6
## Destinations and sources destinations-and-sources

One of the core functionalities of Experience Platform is ingesting your first-party data and activating it for your business needs. Use [sources](/en/docs/experience-platform/sources/home) to ingest data into Experience Platform and destinations to export data from Experience Platform.

## Destinations steps steps

- Choose from a [self-service catalog](/en/docs/experience-platform/destinations/catalog/overview) of all the destinations available in Experience Platform.
- Use destinations to send audiences or datasets to marketing automation platforms, digital advertising platforms, and more.
- Schedule data exports to your preferred destinations at regular times.

## Controls controls

Use the controls in the [destinations workspace](/en/docs/experience-platform/destinations/ui/destinations-workspace) to:

- Browse the catalog of destination platforms where you can activate your data;
- Create, edit, activate, and disable data flows to the destinations in the catalog;
- Create an account in a storage location or link Experience Platform to the account in the destination platform;
- Select which audiences or datasets should be activated to destinations;
- Select which [Experience Data Model (XDM) fields](/en/docs/experience-platform/xdm/home) to export when activating audiences to certain destinations like email marketing destinations, CRM platforms, cloud storage locations, and more.
- Activate different types of profiles and audiences to destinations - people, accounts, and prospects.

## Destination types and categories types-and-categories

With Experience Platform, you can activate data to various types of destinations, to satisfy your activation use cases. Destinations range from API-based integrations, to integrations with file reception systems, profile lookup destinations, and more. For detailed information about all available destinations, read the [destination types and categories overview](/en/docs/experience-platform/destinations/destination-types).

## Adobe-built and partner-built destinations adobe-and-partner-built-destinations

Some of the connectors in the Experience Platform destinations catalog are built and maintained by Adobe, while others are built and maintained by partner companies using [Destination SDK](/en/docs/experience-platform/destinations/destination-sdk/overview). A note at the top of the documentation page for each partner-built connector calls out if a destination is created and maintained by the partner. For example, the [Amazon S3 connector](/en/docs/experience-platform/destinations/catalog/cloud-storage/amazon-s3) is created by Adobe, while the [TikTok connector](/en/docs/experience-platform/destinations/catalog/social/tiktok) is created and maintained by the TikTok team.

For partner-authored and maintained connectors, this means that issues with the connector might need to be resolved by the partner team (contact method provided in the note in the documentation page). For issues with Adobe-authored and maintained connectors, contact your Adobe representative or Customer Care.

## Destinations and access controls access-controls

The destinations functionality in Experience Platform works with Adobe Experience Platform access control permissions. Depending on your user’s permission level, you can view, manage, and activate destinations. For information about the individual permissions, go to [access control in Adobe Experience Platform](/en/docs/experience-platform/access-control/home) and scroll down to the table at the bottom of the page.

The following table outlines the permissions and permission combinations required to perform certain actions on destinations.

Permission level
Description
View Destinations
To access the destinations tab in the Experience Platform UI, you need the
View Destinations
access control permission
.
View Destinations
,
Manage Destinations
To connect to destinations, you need the
View Destinations
and
Manage Destinations
access control permissions
.
View Destinations
,
Activate Destinations
,
View Profiles
, and
View Segments
To activate audiences to destinations and enable the
mapping step
of the workflow, you need the
View Destinations
,
Activate Destinations
,
View Profiles
, and
View Segments
access control permissions
.
View Destinations
,
Activate Segments without Mapping
,
View Profiles
, and
View Segments
To add or remove audiences from existing dataflows without having access to the
mapping step
of the workflow, you need the
View Destinations
,
Activate Segments without Mapping
,
View Profiles
, and
View Segments
access control permissions
.
View Destinations
,
Manage and Activate Dataset Destinations
To export datasets to destinations, you need the
View Destinations
and
Manage and Activate Dataset Destinations
access control permissions
.
View Identity Graph
To export
identities
to destinations, you need the
View Identity Graph
access control permission
.
{width="100" modal="regular"}
The diagram below visually displays which permissions you need depending on the operations that you want to perform on destinations.

For more information about access controls, see the [Access control user guide](/en/docs/experience-platform/access-control/ui/overview).

### Attribute-based access control for destinations attribute-based-access

Attribute-based access control in Adobe Experience Platform allows administrators to control access to specific objects and/or capabilities based on attributes.

With attribute-based access control, you can apply mapping configurations to fields that you have permissions to. Furthermore, you cannot export data to a destination if you do not have access to all fields in the dataset.

For more information on how destinations work with attribute-based access controls, read the [attribute-based access control overview](/en/docs/experience-platform/access-control/abac/overview#destinations).

## Profile removal from destinations profile-removal

When a profile is removed from an audience that is activated to a destination, that profile is also removed from the corresponding audience in the destination platform. For example, if a profile is removed from an audience that was previously activated to LinkedIn, that profile will be removed from the associated LinkedIn Matched Audience.

Profile removal from destinations — also referred to as unsegmentation — occurs on the same cadence as segmentation. As soon as a profile is removed from an audience in Experience Platform, the next scheduled dataflow to the destination reflects that change and removes the profile from the destination audience.

The actual speed at which profile removal takes effect in the destination platform may vary based on the destination’s ingestion and processing behavior.

## Destinations monitoring destinations-monitoring

After establishing a connection to a destination and completing the activation workflow, you can monitor the data exports to your reception system. Read the [guide on monitoring dataflows to destinations in the UI](/en/docs/experience-platform/dataflows/ui/monitor-destinations) for more information.

You can also validate if data is coming through successfully to your destination. Most destination documentation pages in the catalog have a *Validate data export section*, which indicates how you can check in the destination platform that data is being successfully brought in from Experience Platform. View an example of this section for the [Amazon Ads destination](/en/docs/experience-platform/destinations/catalog/advertising/amazon-ads#exported-data).

## Data encryption encryption

All data in transit exported from Experience Platform through destinations travels over secure, encrypted connections using [HTTPS TLS 1.2](https://datatracker.ietf.org/doc/html/rfc5246) or newer. The TLS protocol used by Experience Platform in outbound communication also supports [Server Name Indication (SNI)](https://www.rfc-editor.org/rfc/rfc6066#page-6).

For more information about how data is ingested, encrypted, and persisted, see [data encryption in Experience Platform](/en/docs/experience-platform/landing/governance-privacy-security/encryption).

## Data governance restrictions on activating data to destinations data-governance

Data governance is enforced for Experience Platform destinations through:

- *Marketing actions* that you can select in the create destinations workflow;
- *Data usage policies* that restrict data containing certain usage labels from being activated to destinations with certain marketing actions.

See the Data Governance in Experience Platform documentation for more information about [marketing actions](/en/docs/experience-platform/data-governance/policies/overview) and [resolving data policy violations](/en/docs/experience-platform/data-governance/enforcement/auto-enforcement).

For more information about selecting marketing actions in the create destination workflow, see the following pages for the different destination types in Experience Platform:

- [Advertising destinations - Google Ad Manager](/en/docs/experience-platform/destinations/catalog/advertising/google-ad-manager)
- [Advertising destinations - Google Ads](/en/docs/experience-platform/destinations/catalog/advertising/google-ads-destination)
- [Advertising destinations - Google Display & Video 360](/en/docs/experience-platform/destinations/catalog/advertising/google-dv360)
- [Advertising Account destinations - Bombora ABM Audience connection](/en/docs/experience-platform/destinations/catalog/advertising/bombora)
- [Advertising Account destinations - Demandbase connection](/en/docs/experience-platform/destinations/catalog/advertising/demandbase)
- [Cloud storage destinations](/en/docs/experience-platform/destinations/catalog/cloud-storage/overview)
- [Email marketing destinations](/en/docs/experience-platform/destinations/catalog/email-marketing/overview)
- [Social destinations](/en/docs/experience-platform/destinations/catalog/social/overview)

For more information about data policy violations in the audience activation workflow, see the **Review** step in the following guides:

- [Activate audience data to streaming audiences export destinations](/en/docs/experience-platform/destinations/ui/activate/activate-segment-streaming-destinations#review)
- [Activate audience data to streaming profile export destinations](/en/docs/experience-platform/destinations/ui/activate/activate-streaming-profile-destinations#review)
- [Activate audience data to batch profile export destinations](/en/docs/experience-platform/destinations/ui/activate/activate-batch-profile-destinations#review)

## Terms and conditions terms-and-conditions

By using any of the Destinations labeled as beta (“Beta”), You hereby acknowledge that the Beta is provided *“as is” without warranty of any kind*.

Adobe shall have no obligation to maintain, correct, update, change, modify, or otherwise support the Beta. You are advised to use Informative and not to rely in any way on the correct functioning or performance of such Beta and/or accompanying materials. The Beta is considered Confidential Information of Adobe.

Any “Feedback” (information regarding the Beta including but not limited to problems or defects you encounter while using the Beta, suggestions, improvements, and recommendations) provided by You to Adobe is hereby assigned to Adobe including all rights, title, and interest in and to such Feedback.

Submit Open Feedback or create a Support Ticket to share your suggestions or report a bug, seek a feature enhancement.

recommendation-more-help
