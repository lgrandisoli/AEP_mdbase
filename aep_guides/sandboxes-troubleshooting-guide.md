---
title: "Sandboxes troubleshooting guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sandbox/troubleshooting-guide"
category: "guides"
topic: "experience-platform/sandboxes-guide"
created_at: "2026-06-26T17:29:19.813566+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Sandboxes Guide

# Sandboxes troubleshooting guide

Last update: June 18, 2026
- Topics:
- [Sandboxes](#)

CREATED FOR:

- Developer
- User
- Admin
- Leader

This document provides answers to frequently asked questions about sandboxes in Adobe Experience Platform. For questions and troubleshooting related to other Experience Platform services, please refer to the [Experience Platform troubleshooting guide](/en/docs/experience-platform/landing/troubleshooting).

Sandboxes partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications. See the [sandboxes overview](/en/docs/experience-platform/sandbox/home) for more information.

## What is a sandbox?

Sandboxes are virtual partitions within a single instance of Experience Platform. Each sandbox maintains its own independent library of Experience Platform resources (including schemas, datasets, profiles, and so on). All content and actions taken within a sandbox are confined to only that sandbox and do not affect any other sandboxes. See the [sandboxes overview](/en/docs/experience-platform/sandbox/home) for more information.

## What types of sandboxes are available, and what are their differences? sandbox-types

There are two sandbox types available in Experience Platform:

- Production sandbox : A production sandbox is meant to be used with profiles in your production environment. Experience Platform allows you to create multiple production sandboxes in order to provide the right functionality for data while still maintaining operational isolation. This feature allows you to dedicate specific production sandboxes to distinct lines of business, brands, projects, or regions. Production sandboxes support a volume of production profiles up to your licensed Profile commitment (measured cumulatively across all of your authorized production sandboxes). You are entitled to use your entire licensed Total Data Volume (measured cumulatively across all of your authorized production sandboxes).
- Development sandbox : A development sandbox is a sandbox that can be used exclusively for development and testing with non-production profiles. Development sandboxes support a volume of non-production profiles up to 10% of your licensed Profile commitment (measured cumulatively across all of your authorized development sandboxes). You are entitled to up to: One batch segmentation job per day, per development sandbox; An average of 120 Profile API calls, per Profile, per year (measured cumulatively across all of your authorized development sandboxes.

See the [sandboxes overview](/en/docs/experience-platform/sandbox/home) for more information.

## Can I access a resource from more than one sandbox?

Sandboxes are isolated partitions of a single Experience Platform instance, with each sandbox maintaining its own independent library of resources. A resource that exists in one sandbox cannot be accessed from any other sandbox, regardless of sandbox type (production or non-production).

## What is the default production sandbox?

The default production sandbox is the first production sandbox that is created when an organization is first provisioned. The default production sandbox allows you to ingest or consume data from Experience Platform, as well as accept requests that do not include values for a sandbox name or a sandbox ID. The default production sandbox can be reset but not deleted.

## How many production sandboxes can I have?

An Experience Platform instance supports multiple production and development sandboxes, with each sandbox maintaining its own independent library of Experience Platform resources (including schemas, datasets, and profiles).

A default Experience Platform license grants you a total of five sandboxes, which you can classify as production or development. You can license additional packs of 10 sandboxes up to a maximum of 75 sandboxes in total.

Production sandboxes can be reset or deleted, except for production sandboxes that are also being used by Adobe Analytics for the [Cross Device Analytics (CDA)](/en/docs/analytics/components/cda/overview) feature, or if the identity graph hosted within it is also being used by Adobe Audience Manager for the [People Based Destinations (PBD)](/en/docs/audience-manager/user-guide/features/destinations/people-based/people-based-destinations-overview) feature.

You can update the title of a production sandbox. However, a production sandbox cannot be renamed.

NOTE
The sandbox name is used for lookup purposes in API calls, whereas the sandbox title is used as the display name.
## How many development sandboxes can I have?

Experience Platform currently allows a maximum of 75 total sandboxes (production and development) to be active within a single organization.

Development sandboxes support both reset and delete functionalities.

## I just created a sandbox. How do I set permissions for the users who will be working with this sandbox?

The Adobe Admin Console links users to sandboxes and permissions through the use of product profiles. After creating a new sandbox, navigate to the **Permissions** tab of the product profile you wish to grant access to, then click **Sandboxes**. From here, you can add or remove access to the new sandbox in the same manner as other permissions.

If you wish to add unique permissions to users of a particular sandbox, you may need to create a new product profile with the appropriate sandboxes and permissions applied, and assign those users to that profile.

See the [access control user guide](/en/docs/experience-platform/access-control/ui/overview) for more information on managing sandboxes and permissions in the Admin Console.

recommendation-more-help
