---
title: "Quota endpoint"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-lifecycle/api/quota"
category: "reference"
topic: "experience-platform/advanced-data-lifecycle-management-guide"
created_at: "2026-05-29T16:59:32.203631+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Advanced Data Lifecycle Management Guide

# Quota endpoint

Last update: May 13, 2026
- Topics:
- [Data Hygiene](#)

CREATED FOR:

- Developer

Use the /quota endpoint in the Data Hygiene API to check your organization’s current usage and limits. Quotas vary based on entitlements, such as Privacy and Security Shield or Healthcare Shield.

Monitor your current quota consumption to ensure compliance with organizational limits for each job type.

## Getting started

The endpoint used in this guide is part of the Data Hygiene API. Before continuing, please review the [overview](/en/docs/experience-platform/data-lifecycle/api/overview) for the following information:

- Related documentation links
- How to read sample API calls
- Required headers for Experience Platform API calls

## Quotas and processing timelines quotas

Record delete requests are subject to quotas and service-level expectations based on your license entitlement. These limits apply to both UI- and API-based delete requests.

TIP
This document shows you how to query your usage against entitlement-based limits. For a full description of quota tiers, record delete entitlements, and SLA behavior, see the
UI-based record delete
or
API-based record delete
documents.
## List quotas list

You can view your organization’s quota information by making a GET request to the /quota endpoint.

**API format**

```
GET /quota
GET /quota?quotaType={QUOTA_TYPE}
```

NOTE
Quota consumption resets daily and monthly on the 1st of each month at 00:00 GMT.
Only accepted requests count toward your quota. Rejected work orders do not reduce your quota.
Parameter
Description
{QUOTA_TYPE}
An optional query parameter that specifies the type of quota to retrieve. If no quotaType parameter is provided, all quota values are returned in the API response. Accepted values include:

- datasetExpirationQuota: The number of active dataset expirations and your total allowance.
- dailyConsumerDeleteIdentitiesQuota: The number of record deletes today and your daily quota.
- monthlyConsumerDeleteIdentitiesQuota: The number of record deletes this month and your monthly quota.

**Request**

```
curl -X GET \
  https://platform.adobe.io/data/core/hygiene/quota \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'x-api-key: {API_KEY}' \
  -H 'x-gw-ims-org-id: {ORG_ID}' \
  -H 'Content-Type: application/json'
```

**Response**

A successful response returns the details of your data lifecycle quotas.

```
{
  "quotas": [
    {
      "name": "datasetExpirationQuota",
      "description": "The number of concurrently active dataset-expiration delete operations in all work order requests for the organization.",
      "consumed": 11,
      "quota": 75
    },
    {
      "name": "dailyConsumerDeleteIdentitiesQuota",
      "description": "The consumed number of deleted identities in all work order requests for the organization for today.",
      "consumed": 314,
      "quota": 700000
    },
    {
      "name": "monthlyConsumerDeleteIdentitiesQuota",
      "description": "The consumed number of deleted identities in all work order requests for the organization this month.",
      "consumed": 2764,
      "quota": 12000000
    }
  ]
}
```

Property
Description
quotas
Lists the quota information for each data lifecycle job type. Each quota object contains the following properties:

- name
- description
- consumed
- quota

name
The quota type identifier.
description
A description of what this quota limits.
consumed
The amount of quota currently consumed. The consumed amount resets on the 1st of the month at 00:00 GMT and 00:00 GMT for daily quota.
quota
The maximum allotment of this quota type for your organization.
recommendation-more-help
