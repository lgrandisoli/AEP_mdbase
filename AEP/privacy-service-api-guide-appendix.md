---
title: "Privacy Service API guide appendix"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/privacy/api/appendix"
category: "reference"
topic: "experience-platform/privacy-service-guide"
created_at: "2026-05-29T17:04:54.892106+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Privacy Service Guide

# Privacy Service API guide appendix

Last update: May 23, 2026
- Topics:
- [Privacy](#)

CREATED FOR:

- Developer

The following sections contain additional information for working with the Adobe Experience Platform Privacy Service API.

## Standard identity namespaces standard-namespaces

All identities that are sent to Privacy Service must be provided under a specific identity namespace. Identity namespaces are a component of [Adobe Experience Platform Identity Service](/en/docs/experience-platform/identity/home) that indicate the context to which an identity relates.

The following table outlines several commonly used, pre-defined identity types made available by Experience Platform, along with their associated namespace values:

Identity type
namespace
namespaceId
Email
Email
6
Phone
Phone
7
Adobe Advertising ID
AdCloud
411
Adobe Audience Manager UUID
CORE
0
Adobe Experience Cloud ID
ECID
4
Adobe Target ID
TNTID
9
Apple ID for Advertisers
IDFA
20915
Google Ad ID
GAID
20914
Windows AID
WAID
8
NOTE
Each identity type also has a
namespaceId
integer value, which can be used in place of the
namespace
string when setting the identity’s
type
property to “namespaceId”. See the section on
namespace qualifiers
for more information.
You can retrieve a list of identity namespaces in use by your organization by making a GET request to the idnamespace/identities endpoint in the Identity Service API. See the [Identity Service developer guide](/en/docs/experience-platform/identity/api/getting-started) for more information.

## Namespace qualifiers namespace-qualifiers

When specifying a namespace value in the Privacy Service API, a **namespace qualifier** must be included in a corresponding type parameter. The following table outlines the different accepted namespace qualifiers.

Qualifier
Definition
standard
One of the standard namespaces defined globally, not tied to an individual organization data set (for example, email, phone number, etc.). Namespace ID is provided.
custom
A unique namespace created in the context of an organization, not shared across the Experience Cloud. The value represents the friendly name (“name” field) to be searched for. Namespace ID is provided.
integrationCode
Integration code - similar to “custom”, but specifically defined as the integration code of a datasource to be searched for. Namespace ID is provided.
namespaceId
Indicates the value is the actual ID of the namespace that was created or mapped through the namespace service.
unregistered
A freeform string that is not defined in the namespace service and is taken “as is”. Any application that handles these kinds of namespaces checks against them and handle if appropriate for the company context and data set. No namespace ID is provided.
analytics
A custom namespace that is mapped internally in Analytics, not in the namespace service. This is passed in directly as specified by the original request, without a namespace ID
target
A custom namespace understood internally by Target, not in the namespace service. This is passed in directly as specified by the original request, without a namespace ID
## Accepted product values accepted-product-values

This section lists the product identifier values accepted in the include attribute when creating Privacy Service jobs (API or UI). Use these values in the include array of your job request.

The following table lists the supported products, their UI display names, and their corresponding code values.

NOTE
- Product values are case-insensitive; camel case is recommended for consistency.
- Only the products listed above are supported in the UI and API. If a product is not provisioned for your organization, it may be ignored or cause a validation error—refer to your Adobe contract or provisioning documentation to confirm entitlement.

Branded product name
UI display name
include
value
Adobe Analytics
Analytics
analytics
Adobe Audience Manager
Audience Manager
audienceManager
Adobe Advertising
Ad Cloud
adCloud
Adobe Experience Platform (Profile store)
Profile
profileService
Adobe Experience Platform (data lake)
AEP Data Lake
aepDataLake
Adobe Campaign
Campaign
campaign
Adobe Target
Target
target
Customer Attributes
Customer Attributes (CRS)
CRS
Adobe Journey Optimizer
Adobe Journey Optimizer
cjm
Marketo Engage
Marketo Engage / AJO B2B
marketo
Identity Service
Identity
identity
Marketo Measure
Marketo Measure
marketomeasure
Adobe Commerce
Commerce (Personalization)
commerceMarketingData
recommendation-more-help
