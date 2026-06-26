---
title: "Adobe Experience Platform Identity Service"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/identity/home"
category: "overview"
topic: "experience-platform/experience-platform-identity-service-guide"
created_at: "2026-05-29T16:54:33.285566+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform Identity Service Guide

# Adobe Experience Platform Identity Service

Last update: May 13, 2026
- Topics:
- [Identities](#)

CREATED FOR:

- Admin
- Developer

In order to deliver relevant digital experiences, you need a comprehensive and accurate representation of the real-world entities that make up your customer base.

Organizations and businesses today face a large volume of disparate datasets: your individual customers are represented by a variety of different identifiers. Your customer can be linked to different web browsers (Safari, Google Chrome), hardware devices (Phones, Laptops), and other person identifiers (CRMIDs, Email accounts). This creates a disjointed view of your customer.

You can solve these challenges with Adobe Experience Platform Identity Service and its capabilities to:

- Generate an **identity graph** that links disparate identities together, thus giving you with a visual representation of how a customer interacts with your brand across different channels.
- Create a graph for Real-Time Customer Profile, which is then used to create a comprehensive view of the customer by merging attributes and behaviors.
- Perform validation and debugging using the various tools.

This document provides an overview of Identity Service and how you can use its functionalities within the context of Experience Platform.

## Terminology terminology

Before diving into the details of Identity Service, please read the following table for a summary of the key terms:

Term
Definition
Identity
An identity is data that is unique to an entity. Typically, this is a real-world object, such as an individual person, a hardware device, or a web browser (represented by a cookie). A fully qualified identity consists of two elements: an
identity namespace
and an
identity value
.
Identity namespace
An identity namespace is the context of a given identity. For example, a namespace of
Email
could correspond with the identity value:
julien@acme.com
. Similarly, a namespace of
Phone
could correspond with the identity value:
555-555-1234
. For more information, read the
identity namespace overview
.
Identity value
An identity value is a string that represents a real-world entity and is categorized within Identity Service through a namespace. For example, the identity value (string)
julien@acme.com
could be categorized as an
Email
namespace.
Identity type
An identity type is a component of an identity namespace. The identity type designates whether identity data is linked in an identity graph or not.
Link
A link or a linkage, is a method to establish that two disparate identities represent the same entity. For example, a link between “
Email
= julien@acme.com” and “
Phone
= 555-555-1234” means that both identities represent the same entity. This suggests that the customer who has interacted with your brand with both the email address of julien@acme.com and the phone number of 555-555-1234 is the same.
Identity Service
Identity Service is a service within Experience Platform that links (or unlinks) identities to maintain identity graphs.
Identity graph
The identity graph is a collection of identities that represent a single customer. For more information, read the guide on
using the identity graph viewer
.
Real-Time Customer Profile
Real-Time Customer Profile is a service within Adobe Experience Platform that:

- Merges profiles fragments to create a profile, based on an identity graph.
- Segments profiles so that they can then be sent to destination for activations.

Profile
A profile is a representation of a subject, an organization, or an individual. A profile is composed of four elements:

- Attributes: attributes provide information such as name, age, or gender.
- Behavior: behaviors provide information on the activities of a given profile. For example, a profile behavior can tell if a given profile was “searching for sandals” or “ordering t-shirts.”
- Identities: For a merged profile, this provides information of all the identities associated with the person. Identities can be classified into three categories: Person (CRMID, email, phone), device (IDFA, GAID), and cookie (ECID, AAID).
- Audience memberships: The groups in which the profile belongs to (loyal users, users who live in California, etc.)

## What is Identity Service?

In a Business-To-Customer (B2C) context, customers interact with your business and establish a relationship with your brand. A typical customer may be active in any number of systems within your organization’s data infrastructure. Any given customer may be active within your e-commerce, loyalty, and help-desk systems. That same customer may also engage both anonymously or through authenticated means on any number of different devices.

Consider the following customer journey:

- Julien has created an account on your e-commerce website and ordered some items in the past. Julien typically uses her personal laptop to shop and logs in to her account with each use time of use.
- However, during one of her visits to your site, she uses a tablet to search for sandals. During this session, because she used a different device, she neither logs in nor does she place an order.
- At this point, Julien’s activities are represented in two separate profiles: Her first profile is her e-commerce login ID. This profile is used when she uses a username and password combination to authenticate her session on your e-commerce site. This profile is identified by a cross-device identifier. Her second profile is her tablet device. This profile was created after she browses your e-commerce site anonymously using a tablet without logging in to her account. This profile is identified by a cookie identifier.
- Later, Julien resumes her tablet session. However, this time she logs in to her account. As a result, Identity Service now relates that Julien’s tablet device activity with her e-commerce login ID.
- Moving forward, your targeted content could reflect Julien’s full profile, purchase history, and anonymous browsing activity.

IMPORTANT
You can use Identity Service to link identities and piece together a complete picture of your customer that might otherwise be scattered across different systems.
## What does Identity Service do?

Identity Service provides the following operations to achieve its mission:

- Create custom namespaces to fit your organization’s needs.
- Create, update, and view identity graphs.
- Delete identities based on datasets.
- Delete identities to ensure regulatory compliance.

## How Identity Service links identities

IMPORTANT
Identity Service is case-sensitive. For example,
abc@gmail.com
and
ABC@GMAIL.COM
would be treated as two separate Email identities.
A link between two identities is established when the identity namespace and the identity values match.

A typical login event **sends two identities** into Experience Platform:

- The person identifier (such as a CRMID) that represents an authenticated user.
- The browser identifier (such as an ECID) that represents the web browser.

Consider the following example:

- You log in with your username and password combination to an e-commerce website using your laptop. This event qualifies you as an authenticated user, thus Identity Service recognizes your CRMID.
- Your use of a browser to access the e-commerce website is also recognized by Identity Service as an event. This event is represented in Identity Service through an ECID.
- Behind the scenes, Identity Service processes the two events as: CRM_ID:ABC, ECID:123 . CRMID: ABC is the namespace and value that represents you, as an authenticated user. ECID: 123 is the namespace and value that represents your web browser usage on your laptop.
- Next, if you log in with the same credentials to the same e-commerce website, but use the web browser on your phone instead of the web browser on your laptop, then a new ECID is registered in Identity Service.
- Behind the scenes, Identity Service processes this new event as {CRM_ID:ABC, ECID:456} , where CRM_ID: ABC represents your authenticated customer ID and ECID:456 represents the web browser on your mobile device.

Considering the scenarios above, Identity Service establishes a link between {CRM_ID:ABC, ECID:123}, as well as {CRM_ID:ABC, ECID:456}. This results in an identity graph where you “own” three identities: one for person identifier (CRMID) and two for cookie identifiers (ECIDs).

For more information, read the the guide on [how Identity Service links identities](/en/docs/experience-platform/identity/features/identity-linking-logic).

## Identity graphs

An identity graph is a map of relationships between different identity namespaces, allowing you to visualize and better understand what customer identities are stitched together, and how. Read the tutorial on [using the identity graph viewer](/en/docs/experience-platform/identity/features/identity-graph-viewer) for more information.

The following video is intended to support your understanding of identities and identity graphs.

https://video.tv.adobe.com/v/27841?quality=12&learn=on
https://video.tv.adobe.com/vc/27841/eng.json
## Understanding the role of Identity Service within the Experience Platform infrastructure

Identity Service plays a vital role within Experience Platform. Some of these key integrations include the following:

- [Schemas](/en/docs/experience-platform/xdm/home): Within a given schema, the schema fields that are marked as identity allow for identity graphs to be built.
- [Datasets](/en/docs/experience-platform/catalog/datasets/overview): When a dataset is enabled for ingestion into Real-Time Customer Profile, identity graphs are generated from the dataset, given that the dataset as at least two fields marked as identity.
- [Data collection](/en/docs/experience-platform/collection/home): Data collection libraries (such as the Web SDK) send experience events to Adobe Experience Platform. The Identity Service generates a graph when two or more identities exist in the event.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Before attributes and events for a given profile are merged, Real-Time Customer Profile could reference the identity graph. For more information, read the guide on [understanding the relationship between Identity Service and Real-Time Customer Profile](/en/docs/experience-platform/identity/identity-and-profile).
- [Destinations](/en/docs/experience-platform/destinations/home): Destinations can send profile information to other systems based on an identity namespace, such as hashed email.
- [Segment Match](/en/docs/experience-platform/segmentation/ui/segment-match/overview): Segment Match matches two profiles across two different sandboxes that have the same identity namespace and identity value.
- [Privacy Service](/en/docs/experience-platform/privacy/home): If the deletion request includes identity, then the specified namespace and identity value combination can be deleted from Identity Service using the privacy request processing feature in Privacy Service.

recommendation-more-help
