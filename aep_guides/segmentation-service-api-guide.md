---
title: "Segmentation Service API guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/api/overview"
category: "reference"
topic: "experience-platform/segmentation-service-guide"
created_at: "2026-06-26T17:34:44.504796+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Segmentation Service Guide

# Segmentation Service API guide

Last update: June 18, 2026
- Topics:
- [Segments](#)

CREATED FOR:

- Developer

Adobe Experience Platform Segmentation Service allows you to create audiences through segment definitions or other sources in Adobe Experience Platform from your Real-Time Customer Profile data.

The Segmentation Service API provides multiple endpoints that allow you to programmatically manage your segmentation operations in Experience Platform. This overview document provides high-level introductions to each of these endpoints, and links to their associated endpoint guides for details. Before reading the individual endpoint guides, please refer to the [getting started guide](/en/docs/experience-platform/segmentation/api/getting-started) for important information on required headers, reading sample API calls, and more.

To view all available endpoints and CRUD operations, please refer to the [Segmentation Service API reference](https://www.adobe.io/experience-platform-apis/references/segmentation/).

## Audiences

Audiences are a collection of people who share similar behaviors and/or characteristics. These can be generated either by using Experience Platform or from external sources. You can use the /audiences endpoint to retrieve all audiences, create a new audience, retrieve details of a specific audience, update a specific audience, or delete a specific audience.

For more information on using this endpoint, please read the [audiences endpoint guide](/en/docs/experience-platform/segmentation/api/audiences).

## Export jobs

Export jobs are asynchronous processes that are used to persist audience segment members to datasets. You can use the /export/jobs endpoint to retrieve all export jobs, create a new export job, retrieve details of a specific export job, or cancel a specific export job.

For more information on using this endpoint, please read the [export jobs endpoint guide](/en/docs/experience-platform/segmentation/api/export-jobs).

## External audiences

You can import external audiences into Experience Platform, retrieve an audience’s creation status, update an external audience, start an audience ingestion run, retrieve an external audience ingestion status, list audience ingestion runs, and delete an external audience by using the /core/ais/external-audiences endpoint.

For more information on using this endpoint, please read the [external audiences endpoint guide](/en/docs/experience-platform/segmentation/api/external-audiences).

## Previews and estimates

Previews provide a paginated list of qualifying profiles for a segment definition, allowing you to compare the results against what you expect. You can use the /preview endpoint to create a new preview job or look up results of a specific preview job.

Estimates provide statistical information for segment definitions, such as projected audience size, confidence interval, and error standard deviation. You can use the /estimate endpoint to view an estimate of a segment definition.

For more information on using these endpoints, please read the [previews and estimates endpoints guide](/en/docs/experience-platform/segmentation/api/previews-and-estimates).

## Schedules

Schedules are a tool that can be used to automatically run batch segmentation jobs once a day. You can use the /config/schedules endpoint to retrieve a list of schedules, create a new schedule, retrieve details of a specific schedule, update a specific schedule, or delete a specific schedule.

For more information on using this endpoint, please read the [schedules endpoint guide](/en/docs/experience-platform/segmentation/api/schedules).

## Segment definitions

Segment definitions define which profiles will be part of which audience. You can use the /segment/definitions endpoint to manage segment definitions.

For more information on using this endpoint, please read the [segment definitions endpoint guide](/en/docs/experience-platform/segmentation/api/segment-definitions).

## Segment jobs

Segment jobs process previously established segment definitions to generate an audience. You can use the /segment/jobs endpoint to manage segment jobs.

For more information on using this endpoint, please read the [segment jobs endpoint guide](/en/docs/experience-platform/segmentation/api/segment-jobs).

## Segment search

Segment search is used to search fields contained across various data sources and return them in near real-time. To begin working with segment search, see the [search endpoint guide](/en/docs/experience-platform/segmentation/api/segment-search)

## Next steps

To get started with the Segmentation Service API, review the different endpoint guides for detailed steps on how to make calls to the service’s various endpoints. To learn more about working with segments using the Experience Platform UI, see the [Segmentation user guide](/en/docs/experience-platform/segmentation/ui/overview).

recommendation-more-help
