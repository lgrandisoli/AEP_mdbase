---
title: "Ingest and use Experience Platform audiences"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-ingestion/ingest-aep-segments"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-ingestion"
created_at: "2026-06-23T20:44:25.531794+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest and use Experience Platform audiences

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- Admin

This use case explores an interim solution to ingest Experience Platform audiences into Customer Journey Analytics. These audiences might have been created in the Experience Platform Segment Builder, or Adobe Audience Manager, or other tools, and are stored in Real-time Customer Profile. The audiences consist of a set of Profile IDs, along with any applicable attributes, events, and more. You want to bring that audience data into Customer Journey Analytics for further analysis.

## Prerequisites

- Access to [Experience Platform](/en/docs/experience-platform/access-control/home), specifically Real-time Customer Profile.
- Access to create and manage Experience Platform [schemas](/en/docs/experience-platform/xdm/home) and [datasets](/en/docs/experience-platform/catalog/datasets/overview).
- Access to [Experience Platform Query Service](/en/docs/experience-platform/query/home) (and the ability to write SQL).
- Access to a tool that can perform some transformations of data.
- Access to Customer Journey Analytics. You need to be a [Customer Journey Analytics product admin](/en/docs/analytics-platform/using/technotes/access-control) to create and modify Customer Journey Analytics connections and data views.
- [Authenticate and access to Experience Platform APIs (Catalog Service API and Segmentation Service API)](/en/docs/experience-platform/landing/platform-apis/api-authentication). You need to create a project in the Developer console of the organization and sandbox and ensure you have the information that is required to successfully submit API calls.

## Steps

The interim solution involves the following steps:

- [Select audiences (Experience Platform UI)](#select-audiences).
- [Create a profile-enabled dataset (Experience Platform API)](#create-a-profile-enabled-dataset).
- [Export audiences (Experience Platform API)](#export-audiences).
- [Transform the output (Experience Platform UI and more)](#transform-the-output).
- [Create a schema and dataset (Experience Platform UI)](#create-a-schema-and-dataset).
- [Add or edit a connection (Customer Journey Analytics UI)](#add-or-edit-a-connection).
- [Configure a data view (Customer Journey Analytics UI)](#configure-a-data-view).
- [Report and analyze (Customer Journey Analytics UI)](#report-and-analyze).

### Select audiences

The solution start with the identification of audiences you want to ingest in Customer Journey Analytics.

Identify audiences
In the Experience Platform UI:

- Select Customer > Audiences .
- Select Browse and search for the audiences that you want to ingest and use in Customer Journey Analytics. Note the Audience Id for each of the audiences for later use.

### Create a profile-enabled dataset

You need to create a dataset based on the core-based **XDM Individual Profile** schema. You cannot select that core based XDM Individual Profile as the schema when you create a dataset in the Experience Platform UI. Instead, use the [Catalog Service API to create a dataset](/en/docs/experience-platform/catalog/datasets/create#create-a-dataset) based on the _xdm.context.profile__union schema.

Create dataset request
#### Request

| code language-shell |
| --- |
| curl -X POST \ 'https://platform.adobe.io/data/foundation/catalog/dataSets?requestDataSource=true' \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'Content-Type: application/json' \ -H 'x-api-key: {API_KEY}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "name": "{DATASET_NAME}", "schemaRef": { "id": "_xdm.context.profile__union", "contentType": "application/vnd.adobe.xed+json;version=1" }, "fileDescription": { "persistet": true, "containerFormat": "parquet", "format": "parquet" } }' |

Where:

- DATASET_NAME is the friendly name of the dataset. For example, Segment Export Job Dataset for CJA.

#### Response

| code language-json |
| --- |
| ["@/dataSets/{DATASET_ID}"] |

Where:

- DATASET_ID is the dataset identifier for the created dataset.

### Export audiences

Export the selected audiences into the dataset you just created. Use the [Segmentation Service API to create an export job](/en/docs/experience-platform/segmentation/api/export-jobs#create) that sends the audiences into the dataset.

Export job request
| code language-shell |
| --- |
| curl -X POST https://platform.adobe.io/data/core/ups/export/jobs \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'Content-Type: application/json' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' \ -d '{ "fields": "{COMMA_SEPARATED_LIST_OF_FULLY_QUALIFIED_FIELD_NAMES}", "filter": { "segments": [ { "segmentId": "{AUDIENCE_ID_1}", "segmentNs": "ups", "status": [ "realized" ], "segmentId": "{AUDIENCE_ID_2}", "segmentNs": "ups", "status": [ "realized" ], "segmentId": "{AUDIENCE_ID_3}", "segmentNs": "ups", "status": [ "realized" ] } ] }, "destination":{ "datasetId": "{DATASET_ID}", "segmentPerBatch": false }, "schema":{ "name": "_xdm.context.profile" } }' |

Where

- COMMA_SEPARATED_LIST_OF_FULLY_QUALIFIED_FIELD_NAMES could be something like _demoemea.identification.core.ecid, _demoemea.identification.core.email, _demoemea.identification.core.phoneNumber, person.gender, person.name.firstName, person.name.lastName. Ensure you include at least the relevant fields (like the personID (email)) that you want to use in your Customer Journey Analysis.
- AUDIENCE_ID_x are the audience identifiers of the audiences that you want to export.
- DATASET_ID is the dataset that you created.

### Response

| code language-json |
| --- |
| { "..." "id": "{EXPORT_JOB_ID}", "..." } |

Where

- EXPORT_JOB_ID is the identifier of the export job.

Use the [Segmentation Service API to check the status of the export job](/en/docs/experience-platform/segmentation/api/export-jobs#get).

Retrieve a specific export job request
#### Request

| code language-shell |
| --- |
| curl -X GET https://platform.adobe.io/data/core/ups/export/jobs/{EXPORT_JOB_ID} \ -H 'Authorization: Bearer {ACCESS_TOKEN}' \ -H 'x-gw-ims-org-id: {ORG_ID}' \ -H 'x-api-key: {API_KEY}' \ -H 'x-sandbox-name: {SANDBOX_NAME}' |

#### Response

| code language-json |
| --- |
| { "..." "id": "{EXPORT_JOB_ID}", "..." "status": "SUCCEEDED", "..." } |

After the export job has succeeded, verify whether the dataset contains successfully ingested batches.

Check ingestion status
In the Experience Platform UI:

- Select Data Management > Datasets .
- Select the dataset that you created, for example: Segment Export Job Dataset for CJA .
- Verify the ingested batches. If the dataset contains failed batches, use Data Management > Monitoring to see what is the reason. For example, you used a field name that does not exist in the schema.
- Copy the Table name of the dataset. For example: segment_export_job_dataset_for_cja . You use that name in the next step.

### Transform the output

The data in the dataset is not in the correct format for Customer Journey Analytics. To transform the data, use the Experience Platform Query Service to fetch the data.

SQL to fetch exported audience data
Use a PSQL client that connects to Experience Platform Query Service.

In the Experience Platform UI:

- Select **Data Management** > **Queries**.
- Select **Credentials**.

Use the credentials to configure your PSQL client to connect to Customer Journey Analytics Query Service.

#### Query

Execute this query to retrieve the audience data from the dataset:

| code language-sql |
| --- |
| SELECT ROW_NUMBER() OVER (ORDER BY key)::text as _id, personID, key as audienceMembershipId FROM ( SELECT {IDENTITY_TO_USE_AS_PERSON_ID} AS personID, explode(segmentMembership.ups) FROM {DATASET_TABLE_NAME} ) WHERE value.status = 'realized' AND (key = '{AUDIENCE_ID_1}' OR key = 'AUDIENCE_ID_2' OR key = 'AUDIENCE_ID_3') |

Where:

- IDENTITY_TO_USE_AS_PERSON_ID is one of the fields you defined as part of the export job. For example: _demoemea.identification.core.email.
- DATASET_TABLE_NAME is the table name of the dataset.
- AUDIENCE_ID_x are the audiences you defined as part of the export job. You need to specify these audiences once more as the specification in the export job is a row-level filter. That row-level filter returns profiles for the specified segments with all the segment memberships for each of the profiles.

#### Results

The result of the query, in JSON format, should look like:

| code language-json |
| --- |
| [ { "_id": "1", "personID": "{PERSON_ID_x}", "audienceMembershipId": "{AUDIENCE_ID_x}" }, { "_id": "2", "personID": "PERSON_ID_y", "audienceMembershipId": "{AUDIENCE_ID_x}" } ] |

Where:

- PERSON_ID_x are the identifier values for the identifier you want to use as the person ID. For example, john.doe@gmail.com when you use email.
- AUDIENCE_ID_x are the audience identifiers.

You need to transform this JSON data to add the tenant name of the environment and to provide a more user-friendly name for the audience.

Transform JSON
The final JSON should look like:

| code language-json |
| --- |
| [ { "_id": "1", "personID": "{PERSON_ID_x}", "{TENANT_NAME}": { "audienceMembershipId": "{AUDIENCE_ID_x}", "audienceMembershipName": "{AUDIENCE_FRIENDLY_NAME_x}" } }, { "_id": "2", "personID": "{PERSON_ID_y}", "{TENANT_NAME}": { "audienceMembershipId": "{AUDIENCE_ID_y}", "audienceMembershipName": "{AUDIENCE_FRIENDLY_NAME_y}" } } } ] |

Where:

- TENANT_NAME is the name of the tenant. For example: _demoemea.
- PERSON_ID_x are the identifier values for the identifier that you want to use as the person ID. For example, john.doe@gmail.com when you use email.
- AUDIENCE_ID_x are the audience identifiers.
- AUDIENCE_FRIENDLY_NAME_x are friendly audience names for the audience ids. For example: Luma - Blue+ Members.

Use your favorite tool to transform the original JSON to this format.

### Create a schema and dataset

To use the transformed JSON as exported audience data in Customer Journey Analytics, you need to create a dedicated schema.

Create schema
To create the schema:

In the Experience Platform UI:

- Select Data Management > Schemas .
- Select Create schema . Select Standard from the drop-down menu.
- Select Manual in the Create a schema dialog and use Select to continue.
- In the Create schema wizard, in the Select a class step: Select Individual Profile . Select Next .
- In the Create schema wizard, in the Name and review step: Enter a Schema display name . For example: Audience Export for CJA Schema . (optional) Enter a Description . Select Finish .
- Set up your schema to contain a custom field group (named, for example, Audience Membership ) that contains two fields named audienceMembershipId and audienceMembershipName .
- Ensure that the personID field is an Identity , Primary Identity and has Email as the I dentity namespace .
- Apply all changes. Select Save to save the schema.

Create a dataset and use that dataset to ingest the transformed JSON data.

Create dataset and ingest data
In the Experience Platform UI:

- Select Data Management > Datasets .
- Select Create dataset .
- Select Create dataset from schema .
- In the Create dataset from schema wizard, in the Select schema step: Select the schema you just created. For example: Audience Export for CJA Schema . Select Next .
- In the Create dataset from schema wizard, in the Configure dataset step: Enter a Name for the dataset. (optional) Enter a Description for the dataset. Select Finish .
- In the Datasets > name of the dataset , drag the transformed JSON data file and drop the file onto Drag and drop files . This action starts the ingestion of the exported JSON data into the dataset.
- Verify the ingested batches. If the dataset contains failed batches, use Data Management > Monitoring to see what is the reason. For example, you defined a field name in the JSON that does not exist in the schema.

### Add or edit a connection

Once the transformed JSON data that contains the audience data from Experience Platform is successfully ingested, you can add the dataset to a new or existing connection in Customer Journey Analytics.

Add dataset to connection
In the Customer Journey Analytics UI:

- Select Data Management > Connections .
- Create a new connection/ Define Connection settings and Data settings . Or select an existing connection and use Edit Connection to edit the connection.
- Select Add datasets .
- Select the dataset that you created and in which you ingested the transformed JSON data.
- Configure the dataset. For example:
- Save the connection.

### Configure a data view

Configure a data view for the connection you just created or edited.

Define audience components
- Select Data Management > Data views .
- Edit an existing data view or create a new data view.
- In the Components tab of the data view, ensure Audience Membership Id and Audience Membership Name are added as dimension components.
- Select Save and Continue to save the data view.

### Report and analyze

Finally, use Analysis Workspace to report on Experience Platform audience data in one or more panels that use the data view with the audience membership components like audienceMembershipId, audienceMembershipIdName, and personID.

## Additional notes

- You should perform this process on a regular cadence, so that audience data is constantly refreshed within Customer Journey Analytics.
- You can import multiple audiences within a single Customer Journey Analytics connection. This adds additional complexity to the process, but it is possible. For this to work, you need to make a few modifications to the above process: Perform this process for each desired audience in your audience collection within RTCP. Customer Journey Analytics supports arrays/object arrays in profile datasets. Using an array of objects for the audienceMembershipId or audienceMembershipIdName is the best option. In your data view, create a new dimension using the Substring transformation on the audienceMembershipId field to convert the comma-separated values string to an array. NOTE: there is currently a limit of 10 values in the array. You can now report on this new dimension audienceMembershipIds within Customer Journey Analytics Workspace.

recommendation-more-help
