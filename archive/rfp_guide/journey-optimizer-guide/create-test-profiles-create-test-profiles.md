---
title: "Create test profiles create-test-profiles"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:45.553111+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Create test profiles create-test-profiles

Last update: May 8, 2026
- Topics:
- [Profiles](#)
- [Test Profiles](#)

CREATED FOR:

- Intermediate
- User

Test profiles are required when using the [test mode](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) in a journey, and to [preview and test your content](/en/docs/journey-optimizer/using/test/preview-test/preview-test).

NOTE
Journey Optimizer allows testing different variants of your content by previewing it and sending proofs using sample input data uploaded from a CSV or JSON file, or added manually.
Learn how to test your content using sample input data
You can create test profiles by [uploading a CSV file](#create-test-profiles-csv) or using [API calls](#create-test-profiles-api). Adobe Journey Optimizer also provides a specific [in-product use case](#use-case-1) to facilitate test profile creation.

You can upload a JSON file into an existing dataset. For more information, refer to the [Data Ingestion documentation](/en/docs/experience-platform/ingestion/tutorials/ingest-batch-data#add-data-to-dataset#_blank).

Creating a test profile is similar to creating regular profiles in Adobe Experience Platform. For more information, refer to the [Real-time Customer Profile documentation](/en/docs/experience-platform/profile/home#_blank).

➡️ [Learn how to create test profiles in this video](#video)

## Prerequisites test-profile-prerequisites

To create profiles, you first need to create a schema and a dataset in Adobe Journey Optimizer.

### Create a schema create-schema

To **create a schema**, follow these steps:

- In the DATA MANAGEMENT menu section, click Schemas and select the Create schema button.
- Select Standard as the schema creation option.
- Select a schema type, for example Individual Profile , and click Next .
- Enter a name for your schema and click Finish .
- In the Field groups section, on the left, click Add and select the appropriate field groups. Make sure you add the Profile test details field group. Once done, click Add field groups : the list of field groups is displayed on the schema overview screen. note NOTE Click the name of the schema to update its properties.
- In the list of fields, click the field that you want to define as the primary identity.
- In the Field properties right pane, check the Identity and Primary Identity options and select a namespace. If you want the primary identity to be an email address, choose the Email namespace. Click Apply .
- Select the schema and enable the Profile option in the Schema properties pane.
- Click Save .

For more information about schema creation, refer to the [XDM documentation](/en/docs/experience-platform/xdm/ui/resources/schemas#prerequisites#_blank).

IMPORTANT
When creating or replacing a dataset for test profile ingestion, ensure that the schema has the correct identity descriptor applied to the primary identity field (e.g.,
/personID
) for the intended namespace. If the identity descriptor is missing or incorrectly configured, profiles ingested into this dataset may not be flagged as test profiles (
testProfile = true
), even if the ingestion process completes successfully.
If your test profiles are not flagged correctly after ingestion:
- Review the schema associated with your dataset.
- Confirm that the primary identity field has the correct identity descriptor for your namespace (see steps 6–7 above).
- If the descriptor is missing, update the schema to add the identity descriptor and re-ingest your data.

### Create a dataset create-dataset

Then you need to **create the dataset** in which the profiles will be imported. Follow these steps:

- Browse to **Datasets**, then click **Create dataset**.
- Choose **Create dataset from schema**.
- Select the previously created schema then click **Next**.
- Choose a name then click **Finish**.
- Enable the **Profile** option.

NOTE
For more information on dataset creation, refer to the
Catalog Service documentation
.
## In-product use case use-case-1

From Adobe Journey Optimizer home page, you can leverage the test profiles in-product use case. This use case facilitates the creation of test profiles used for testing journeys before publishing.

Click the **Begin** button to start the use case.

The following information is required:

- Identity namespace : The identity namespace used to uniquely identify the test profiles. For example, if email is used to identify the test profiles, the identity namespace Email should be selected. If the unique identifier is the phone number, then the identity namespace Phone should be selected.
- CSV file : A comma separated file containing the list of test profiles to create. The use case expects a predefined format for the CSV file that contains the list of test profiles to create. Each row in the file should include the following fields in the correct order as follows: Person Id : Unique identifier of the test profile. The values of this field should reflect the identity namespace that was selected. (As an example, if Phone is selected for the identity namespace, then the values of this field should be phone numbers. Similarly if Email is selected, then the values of this field should be emails) Email Address : Test profile email address. (The Person Id field and the Email Address field could potentially contain the same values if Email is selected as the identity namespace) First Name : Test profile first name. Last Name : Test profile last name. City : Test profile city of residence Country : Test profile country of residence Gender : Test profile gender. Available values are male , female and non_specified

After selecting the identity namespace and providing the CSV file based on the format above, select the **Run** button at the top right. The use case might take a few minutes to complete. Once the use case completes processing and creating the test profiles, a notification will be sent to notify the user.

NOTE
Test profiles may override existing profiles. Before executing the use case make sure the CSV contains test profiles only and that it is executed against the correct sandbox.
## Create test profiles using a CSV file create-test-profiles-csv

In Adobe Experience Platform, you can create profiles by uploading a csv file containing the different profile fields into your dataset. This is the easiest method.

- Create a simple csv file using a spreadsheet software.
- Add one column for each required field. Make sure you add the primary identity field (personID in our example above) and the testProfile field set to true.
- Add one line per profile and fill in the values for each field.
- Save the spreadsheet as a csv file. Make sure commas are used as separators.
- Browse to Adobe Experience Platform **Workflows**.
- Choose **Map CSV to XDM schema**, then click **Launch**.
- Select the dataset you want to import the profiles into. Click **Next**.
- Click **Choose files** and select your csv file. When the file is uploaded, click **Next**.
- Map the source csv fields to the schema fields, then click **Finish**.
- The data import begins. The status will move from **Processing** to **Success**. Click **Preview dataset**, in the top right.
- Check that the test profiles have been correctly added.

Your test profiles are added and can now be used when testing a journey. Refer to [this section](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey).

NOTE
For more information on csv imports, refer to the
Data Ingestion documentation
.
## Create test profiles using API calls create-test-profiles-api

You can also create test profiles via API calls. Learn more in [Adobe Experience Platform documentation](/en/docs/experience-platform/profile/home#_blank).

You must use a Profile schema that contains the **Profile test details** field group. The testProfile flag is part of this field group.When creating a profile, make sure you pass the value: testProfile = true.

You can also update an existing profile to change its testProfile flag to true.

Here is an example of an API call to create a test profile:

```
curl -X POST \
'https://dcs.adobedc.net/collection/xxxxxxxxxxxxxx' \
-H 'Cache-Control: no-cache' \
-H 'Content-Type: application/json' \
-H 'Postman-Token: xxxxx' \
-H 'cache-control: no-cache' \
-H 'x-api-key: xxxxx' \
-H 'x-gw-ims-org-id: xxxxx' \
-d '{
"header": {
"msgType": "xdmEntityCreate",
"msgId": "xxxxx",
"msgVersion": "xxxxx",
"xactionid":"xxxxx",
"datasetId": "xxxxx",
"imsOrgId": "xxxxx",
"source": {
"name": "Postman"
},
"schemaRef": {
"id": "https://example.adobe.com/mobile/schemas/xxxxx",
"contentType": "application/vnd.adobe.xed-full+json;version=1"
}
},
"body": {
"xdmMeta": {
"schemaRef": {
"contentType": "application/vnd.adobe.xed-full+json;version=1"
}
},
"xdmEntity": {
"_id": "xxxxx",
"_mobile":{
"ECID": "xxxxx"
},
"testProfile":true
}
}
}'
```

## How-to video video

Learn how to create test profiles.

https://video.tv.adobe.com/v/334236?quality=12&learn=on
recommendation-more-help
