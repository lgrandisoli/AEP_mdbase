---
title: "Sandbox API guide appendix"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sandbox/api/appendix"
category: "reference"
topic: "experience-platform/sandboxes-guide"
created_at: "2026-05-29T17:06:06.202183+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Sandboxes Guide

# Sandbox API guide appendix

Last update: May 23, 2026
- Topics:
- [Sandboxes](#)

CREATED FOR:

- Developer

This document provides supplemental information related to working with the Sandbox API.

## Using query parameters query

The [Sandbox API](https://www.adobe.io/experience-platform-apis/references/sandbox) supports the use of query parameters to page and filter results when listing sandboxes.

NOTE
The
limit
and
offset
query parameters have to be specified together. If you specify only one, the API will return an error. If you specify none, default limit is 50 and offset is 0.
Parameter
Description
limit
The maximum number of records to be returned in the response.
offset
The number of entities from the first record to start (offset) the response list from.
recommendation-more-help
