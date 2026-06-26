---
title: "Decisioning Migration API decisioning-migration-api"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/experience-decisioning/migrate-to-decisioning/decisioning-migration-api"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:32.004830+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Decisioning Migration API decisioning-migration-api

Last update: May 8, 2026
- Topics:
- [Decisioning](#)

CREATED FOR:

- Experienced
- Developer

The Decisioning Migration Service API enables you to migrate Decision management objects from one sandbox to another. The migration process runs as asynchronous workflows that include dependency analysis, execution, and optional rollback capabilities.

This API allows you to seamlessly transition your decisioning content between environments (e.g., from development to staging, or staging to production) while maintaining data integrity and relationships.

To learn about the benefits and capabilities of Decisioning compared to Decision management, refer to [this page](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/migrate-to-decisioning/migrate-to-decisioning).

## Capabilities capabilities

The Decisioning Migration Service API provides the following capabilities:

- **Dependency analysis** - Identify all required dependencies between source and target sandboxes, including attributes, segments, and dataset requirements.
- **Flexible migration scope** - Run migrations at sandbox, offer, or decision level based on your needs.
- **Rollback support** - Revert a completed migration if issues are discovered during validation.

## Prerequisites prerequisites

### Required permissions permissions

To use the Migration API, you need appropriate permissions in both the source and target sandboxes:

**Source sandbox** - Read access to Decision management objects

**Target sandbox** - Create and edit access to Decisioning objects

Typical permissions include:

- Manage / View Decisioning
- Manage / View Decisions
- Manage Offers
- Manage Ranking Strategies
- Manage Campaigns (if migrating campaign-related artifacts)
- Manage / View Datastreams (if creating a datastream)
- Manage / View Schemas

NOTE
Learn how to assign Decisioning permissions in
this section
. For the full list of permissions, refer to the
Built-in permissions
page.
### Prepare your target sandbox target-sandbox-preparation

Before running a migration, ensure your target sandbox is properly configured:

- **Attributes** - Verify that required profile attributes and context attributes exist in the target sandbox, or prepare mappings for them.
- **Segments** - Ensure required segments exist in the target sandbox, or plan to map them using namespace and ID.
- **Dataset** - Identify a dataset name to use for the migration (dependency.datasetName).
- **Datastream** - Decide whether the migration should create a datastream (createDataStream).

For more information about sandbox management, refer to [Use and assign sandboxes](/en/docs/journey-optimizer/using/connect-systems/sandbox/sandboxes).

## API basics api-basics

### Base URL base-url

Use the following base URL:

- **Production**: https://decisioning-migration.adobe.io

### Authentication authentication

All API requests require the following headers:

- Authorization: Bearer <IMS_ACCESS_TOKEN>
- x-gw-ims-org-id: <IMS_ORG_ID>
- Content-Type: application/json

For detailed instructions on setting up authentication, refer to the [Journey Optimizer authentication guide](https://developer.adobe.com/journey-optimizer-apis/references/authentication#_blank).

### Workflow model workflow-model

Each API call creates or retrieves a workflow resource. Workflows are asynchronous operations that track the progress and results of migration tasks.

A workflow has the following properties:

- id - Unique workflow identifier (UUID)
- status - Current workflow status: New, Running, Completed, or Failed
- result - Workflow output when completed (includes migration results and warnings)
- errors - Structured error details when failed
- _links.self - Workflow URL for retrieving status

## Migration workflow migration-workflow

The migration process consists of two main steps: analyzing dependencies and executing the migration. Follow these steps to ensure a successful migration.

### Step 1: Analyze dependencies analyze-dependencies

Before migrating, use the dependency workflow to identify what needs to be mapped from Decision management to Decisioning in your target sandbox. This analysis helps you understand the relationships between objects and prepare the necessary mappings.

#### Create a dependency workflow create-dependency-workflow

Use the following API call to create a dependency analysis workflow.

**API format**

```
POST /workflows/generate-dependencies
```

**Sandbox-level dependency (recommended first)**

Start with a sandbox-level analysis to get a complete view of all dependencies:

```
curl --request POST \
  --url "https://decisioning-migration.adobe.io/workflows/generate-dependencies?request-level=sandbox" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "Content-Type: application/json" \
  --data '{
    "imsOrgId": "<IMS_ORG_ID>",
    "sourceSandboxDetails": { "sandboxName": "<SOURCE_SANDBOX_NAME>" },
    "targetSandboxDetails": { "sandboxName": "<TARGET_SANDBOX_NAME>" }
  }'
```

**Offer-level dependency**

To analyze dependencies for specific offers only, call the same endpoint with request-level=offer in the query string and provide an offersList array in the body with the offer IDs you want to analyze.

**Decision-level dependency**

To analyze dependencies for specific decisions only, use request-level=decision in the query string and provide a decisionsList array in the body with the decision IDs you want to analyze.

#### Check dependency workflow status poll-dependency-status

Poll the dependency workflow to check when the analysis is complete.

**API format**

```
GET /workflows/generate-dependencies/{id}
```

**Request**

```
curl --request GET \
  --url "https://decisioning-migration.adobe.io/workflows/generate-dependencies/<WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>"
```

When the status field shows Completed, the dependency analysis is ready. Use the workflow output to build your migration dependency mappings:

- **profileAttributes** - Maps source profile attributes to target profile attributes
- **contextAttributes** - Maps source context attributes to target context attributes
- **segments** - Maps source segment keys to target segment identifiers ({namespace, id})
- **datasetName** - Specifies the target dataset name for the migration

### Step 2: Execute the migration execute-migration

Once you have analyzed the dependencies and prepared your mappings, you can execute the migration.

#### Create a migration workflow create-migration-workflow

Use the dependency mappings from Step 1 to configure and execute your migration.

**API format**

```
POST /workflows/migration
```

**Sandbox-level migration**

To migrate all decisioning objects from one sandbox to another:

```
curl --request POST \
  --url 'https://decisioning-migration.adobe.io/workflows/migration?request-level=sandbox' \
  --header 'Authorization: Bearer <IMS_ACCESS_TOKEN>' \
  --header 'Content-Type: application/json' \
  --header 'x-gw-ims-org-id: <IMS_ORG_ID>' \
  --data '{
    "imsOrgId": "<IMS_ORG_ID>",
    "sourceSandboxDetails": { "sandboxName": "<SOURCE_SANDBOX_NAME>" },
    "targetSandboxDetails": { "sandboxName": "<TARGET_SANDBOX_NAME>" },
    "createDataStream": true,
    "dependency": {
      "profileAttributes": {
        "sourceAttr1": "targetAttr1"
      },
      "segments": {
        "sourceSegmentKey1": {
          "namespace": "<TARGET_SEGMENT_NAMESPACE>",
          "id": "<TARGET_SEGMENT_ID>"
        }
      },
      "contextAttributes": {
        "sourceCtx1": "targetCtx1"
      },
      "datasetName": "<TARGET_DATASET_NAME>"
    }
  }'
```

**Offer-level migration**

To migrate specific offers only, use request-level=offer in the query string and add an offersList array to the body:

```
"offersList": ["offer-id-1", "offer-id-2"]
```

**Decision-level migration**

To migrate specific decisions only, use request-level=decision in the query string and add a decisionsList array to the body:

```
"decisionsList": ["decision-id-1", "decision-id-2"]
```

#### Monitor migration status poll-migration-status

Poll the migration workflow to track its progress.

**API format**

```
GET /workflows/migration/{id}
```

**Request**

```
curl --request GET \
  --url "https://decisioning-migration.adobe.io/workflows/migration/<WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>"
```

**Migration results**

When the status field shows Completed, the migration was successful. The workflow result includes:

- Mappings of migrated objects
- Any warnings encountered during migration

When the status field shows Failed, review the errors[] array and result.error field for details about what went wrong.

## Validate your migration validate-migration

After the migration completes successfully, verify that all objects were migrated correctly.

### Validation checklist validation-checklist

- Segments - Verify that all referenced segments resolve correctly in the target sandbox according to your mappings.
- Attributes - Confirm that all profile attributes and context attributes exist in the target sandbox and are mapped correctly.
- Decisioning objects - Review migrated objects in the Journey Optimizer user interface: Offers (decision items) Eligibility rules Ranking formulas Selection strategies Decision policies
- Datastream testing - If a datastream was created, test runtime delivery using the Edge Interact API.

### Example test-runtime-delivery

If your migration created a datastream, you can test offer delivery using the following example:

```
curl --request POST \
  --url "https://edge.adobedc.net/ee/or2/v1/interact?configId=<DATASTREAM_ID>" \
  --header "Content-Type: application/json" \
  --header "x-request-id: <uuid>" \
  --data '{ "events": [ ... ] }'
```

## Rollback a migration rollback

If you discover issues during validation, you can roll back a completed migration to restore the target sandbox to its previous state.

### Create a rollback workflow create-rollback-workflow

Initiate a rollback by creating a rollback workflow that references the migration you want to revert.

**API format**

```
POST /workflows/rollback
```

**Request**

```
curl --request POST \
  --url "https://decisioning-migration.adobe.io/workflows/rollback" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>" \
  --header "Content-Type: application/json" \
  --data '{ "rollbackWorkflowId": "<MIGRATION_WORKFLOW_ID>" }'
```

Replace <MIGRATION_WORKFLOW_ID> with the ID of the migration workflow you want to roll back.

### Monitor rollback status poll-rollback-status

Poll the rollback workflow to track its progress.

**API format**

```
GET /workflows/rollback/{rollbackWorkflowId}
```

**Request**

```
curl --request GET \
  --url "https://decisioning-migration.adobe.io/workflows/rollback/<ROLLBACK_WORKFLOW_ID>" \
  --header "Authorization: Bearer <IMS_ACCESS_TOKEN>" \
  --header "x-gw-ims-org-id: <IMS_ORG_ID>"
```

## Handle concurrent workflows handle-concurrency

The Migration API allows only one workflow to run at a time per organization. If you attempt to create a new workflow while another is in progress, you will receive a **409 Conflict** error response (“A workflow is already in progress…”).

In this case, wait for the in-progress workflow to complete, or retrieve the workflow ID and poll its status. Once the current workflow finishes, you can create a new one.

## Entity mapping reference entity-mapping

When migrating from Decision management to Decisioning, entities are mapped as follows:

Decision management
Decisioning
Offer
Decision item
Offer collection
Item collection
Eligibility rule
Eligibility rule
Ranking formula
Ranking formula
Decision
Selection strategy + Decision policy
Campaign
Campaign
(basic content only)
Placement
Surface + Channel configuration
Tag
Unified tag
Offer attributes
migratedofferattributes
field in the Personalized offer item schema
Context attributes
migratedcontextattributes
field in the schema attached to the dataset provided during migration
## Workflow cleanup cleanup

Workflow deletion is not publicly available. If you need to delete a workflow resource, contact your system administrator.

## Related topics related-topics

- [Migrate from Decision management to Decisioning](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/migrate-to-decisioning/migrate-to-decisioning) - Understand the benefits and capabilities of migrating to Decisioning
- [Get started with Decisioning](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/gs-experience-decisioning)
- [Decisioning guardrails and limitations](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/decisioning-guardrails)
- [Get started with Decisioning APIs](/en/docs/journey-optimizer/using/decisioning/experience-decisioning/experience-decisioning-api-reference/getting-started)

recommendation-more-help
