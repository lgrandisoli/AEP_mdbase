---
title: "Multi-entity segmentation overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/tutorials/multi-entity-segmentation"
category: "tutorials"
topic: "experience-platform/segmentation-service-guide"
created_at: "2026-05-29T16:57:32.326300+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Segmentation Service Guide

# Multi-entity segmentation overview

Last update: May 23, 2026
- Topics:
- [Segments](#)

CREATED FOR:

- User

Multi-entity segmentation is an advanced feature available as part of Adobe Experience Platform Segmentation Service. This feature enables you to extend Real-Time Customer Profile data with additional “non-people” data (also known as “dimension entities”) that your organization may define, such as data related to products or stores. Multi-entity segmentation provides flexibility when defining segment definitions based on data relevant to your unique business needs and can be performed without having expertise in querying databases. With multi-entity segmentation, you can add key data to your segment definitions without having to make costly changes to data streams or wait for a back-end data merge.

## Getting started

Multi-entity segmentation requires a working understanding of the various Adobe Experience Platform services involved in segmentation. Before continuing with this guide, please review the following documentation:

- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified consumer profile in real time, based on aggregated data from multiple sources. Profile guardrails : Best practices for creating data models supported by Profile.
- [Adobe Experience Platform Segmentation Service](/en/docs/experience-platform/segmentation/home): Allows you to build audiences from Real-Time Customer Profile data.
- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. Basics of schema composition : Learn best practices for composing schemas to be used in Experience Platform. To best make use of Segmentation, please ensure your data is ingested as profiles and events according to the best practices for data modeling .

## Use cases

To illustrate the value of multi-entity segmentation, consider three standard marketing use cases that illustrate the challenges present in most marketing applications:

### Combining online and offline purchase data

A marketer building an email campaign may have attempted to build an audience by using recent customer store purchases within the last three months. Ideally, this audience would require both the item name and the name of the store where the purchase was made. Previously, the challenge would have been capturing the store identifier from the purchase event and assigning it to an individual customer profile.

### Email retargeting for cart abandonment

Creating and qualifying users into segment definitions targeting cart abandonment is complex. Knowing which products to include in a personalized retargeting campaign requires data regarding which products were abandoned by each individual. This data is tied to commerce events which were formerly challenging to monitor and extract data from.

## Creating multi-entity segment definitions

Creating a multi-entity segment definition first requires defining relationships between schemas before using the Segmentation API or Segment Builder UI to build the segment definition.

### Define relationships

Defining relationships within the structure of your Experience Data Model (XDM) schemas is an integral part of multi-entity segment creation. For relationships, the field in the destination needs to be marked as the primary identity of that schema. An identity can only be marked on strings and cannot be marked on arrays. Additionally, relationships do not necessarily need to be one-to-one, as you can connect profiles and experience events to multiple destinations.

Defining relationships can be done either using the Schema Registry API or the Schema Editor. For detailed steps showing how to define a relationship between two schemas, please choose from the following tutorials:

- [Defining a relationship between two schemas using the API](/en/docs/experience-platform/xdm/tutorials/relationship-api)
- [Defining a relationship between two schemas using the Schema Editor UI](/en/docs/experience-platform/xdm/tutorials/relationship-ui)

### Build a multi-entity segment definition

Once you have defined the necessary XDM relationships, you can begin to build a multi-entity segment definition. This can be done using either the Segmentation API or the Segment Builder UI. For more information, please choose from the following guides:

- [Creating a segment definition using the Segmentation API](/en/docs/experience-platform/segmentation/tutorials/create-a-segment)
- [Creating a segment definition using the Segment Builder UI](/en/docs/experience-platform/segmentation/ui/overview)

## Evaluate and access multi-entity segment definitions

After creating a segment definition, you can evaluate and access the results using the Segmentation API. Evaluating a multi-entity segment definition is very similar to evaluating a standard segment definition. This process can only be done using the Segmentation API. For a detailed guide showing how to use the API to evaluate and access segment definitions, please read the [evaluating and accessing segment definitions](/en/docs/experience-platform/segmentation/tutorials/evaluate-a-segment) tutorial.

recommendation-more-help
