---
title: "Ingest data via the Edge Network Server API"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/serverapi"
category: "guides"
topic: "analytics-platform/using/cja-data-ingestion/ingest-use-guides"
created_at: "2026-06-23T20:42:02.634651+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest data via the Edge Network Server API

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

This quick start guide explains how you can ingest tracking data from devices like IoT devices, set-top boxes, gaming consoles, desktop applications directly into Adobe Experience Platform using the Adobe Experience Platform Edge Network Server API and Edge Network. Then use that data in Customer Journey Analytics.

To accomplish this, you must:

- Set up a schema and dataset in Adobe Experience Platform to define the model (schema) of the data that you want to collect and where to actually collect the data (dataset).
- Set up a datastream to configure the Adobe Experience Platform Edge Network to route your collected data to the dataset you configured in Adobe Experience Platform.
- Use Server API to send data directly from your application or game running on a desktop, gaming console, IoT device, or set-top box to your datastream.
- Deploy and validate . Have an environment where you can iterate on your development and once everything is validated, publish it live on your production environment.
- Set up a connection in Customer Journey Analytics. This connection should (at least) include your Adobe Experience Platform dataset.
- Set up a data view in Customer Journey Analytics to define metrics and dimension that you want to use in Analysis Workspace.
- Set up a project in Customer Journey Analytics to build your reports and visualizations.

NOTE
This quick start guide is a simplified guide on how to ingest data collected from an application or game running on an IoT device, set-top box, gaming console, or desktop into Adobe Experience Platform and use in Customer Journey Analytics. It is highly recommended to study the additional information when referred to.
## Set up a schema and dataset

To ingest data into Adobe Experience Platform, you first must define which data you want to collect. All data ingested into Adobe Experience Platform must conform to a standard, denormalized structure for it be recognized and acted upon by downstream capabilities and features. Experience Data Model (XDM) is the standard framework that provides a structure in the form of schemas.

Once you have defined a schema, you use one or more datasets to store and manage the collection of data. A dataset is a storage and management construct for a collection of data (typically a table) that contains a schema (columns) and fields (rows).

All data that is ingested into Adobe Experience Platform must conform to a pre-defined schema before it can be persisted as a dataset.

### Set up a schema

You want to track some minimal data from profiles playing your game on a console, for example identification, scores, progress, and other information.You first must define a schema that models this data.

To set up your schema:

- In the Adobe Experience Platform UI, in the left rail, select Schemas within DATA MANAGEMENT.
- Select Create schema . .
- In the Select a class step of the Create schema wizard: Select Experience Event . note info INFO An Experience Event schema is used to model the behavior of a profile (like scene name, push button to add to cart). An Individual Profile schema is used to model the profile attributes (like name, email, gender). Select Next .
- In the Name and review step of the Create schema wizard: Enter a Schema display name for your schema and (optional) a Description . Select Finish .
- In the Structure tab of Example Schema: Select + Add in Field groups. Field groups are reusable collections of objects and attributes that allow you to easily extend your schema. In the Add fields groups dialog, select the Blinding Light field group from the list. This fieldgroup is created to track user progress playing a fictitious game titled Blinding Light on a console. You can select the preview button, to see a preview of the fields that are part of this field group, like scores > afterMatch . Select Back to close the preview. Select Add field groups .
- Select + next to your schema name.
- In the Field Properties panel, enter identification as the Field name, Identification as the Display name, select Object as the Type and select ExperienceEvent Core v2.1 as the Field Group. note NOTE If that field group is not available, look for another field group containing identity fields. Or create a new field group and add new identity fields (like ecid , crmId , and others you need) to the field group and select that new field group. The identification object adds identification capabilities to your schema. In your case, you want to identify profiles playing your game using the Experience Cloud Id and email address they use to log in to their gaming console. There are many other attributes available to track your person’s identification. Select Apply to add this object to your schema.
- Select the ecid field in the identification object you just added, and select Identity and Primary Identity and ECID from the Identity namespace list in the right panel. You are specifying the Experience Cloud Identity as the primary identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles with the same ECID. Select Apply . You see that a fingerprint icon appears in the ecid attribute.
- Select the email field in the identification object you just added, and select Identity and Email from the Identity namespace list in the Field Properties panel. You are specifying the email address as another identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles. Select Apply . You see that a fingerprint icon appears in the email attribute. Select Save .
- Select the root element of your schema displaying the name of the schema, then select the Profile switch. You are prompted to enable the schema for profile. Once enabled, when data is ingested into datasets based on this schema, that data is merged into the Real-Time Customer Profile. See Enable the schema for use in Real-Time Customer Profile for more information. note important IMPORTANT Once you save a schema enabled for profile, it can no longer be disabled for profile.
- Select Save to save your schema.

You have created a minimal schema that models the data you can capture from your game. The schema allows profiles to be identified using the Experience Cloud Identity and email address. By enabling the schema for profile, you ensure data captured from your console game is added to the Real-Time Customer Profile.

Next to behavior data, you can also capture profile attribute data from your console (for example details of profiles signed into the console).

To capture profile data, you would:

- Create a schema based on the XDM Individual Profile class.
- Add the Profile Core v2 field group to the schema.
- Add an identification object based on the Profile Core v2 field group.
- Define Experience Cloud ID as primary identifier and email as identifier.
- Enable the schema for profile

See [Create and edit schemas in the UI](/en/docs/experience-platform/xdm/ui/resources/schemas) for more information on adding and removing field groups and individual fields to a schema.

### Set up a dataset

With your schema, you have defined your data model. You now have to define the construct to store and manage that data by using datasets.

To set up your dataset:

- In the Adobe Experience Platform UI, in the left rail, select Datasets within DATA MANAGEMENT.
- Select Create dataset .
- Select Create dataset from schema .
- Select the schema that you created earlier and select Next .
- Name your dataset and (optional) provide a description.
- Select Finish .
- Select the Profile switch. You are prompted to enable the dataset for profile. Once enabled, the dataset enriches real-time customer profiles with its ingested data. note important IMPORTANT You can only enable a dataset for profile when the schema, to which the dataset adheres, is also enabled for profile.

See [Datasets UI guide](/en/docs/experience-platform/catalog/datasets/user-guide) for much more information on how to view, preview, create, delete a dataset. And how to enable a dataset for Real-Time Customer Profile.

## Set up a datastream

A datastream represents the server-side configuration when implementing the Adobe Experience Platform Web and Mobile SDKs and the Adobe Experience Platform Edge Network Server API. When collecting data with the Adobe Experience Platform SDKs and Edge Network Server APIs, data is sent to the Adobe Experience Platform Edge Network. It is the datastream that determines to which services that data is forwarded.

In your setup, you want the data you collect from the game to be sent to your dataset in Adobe Experience Platform.

To set up your datastream:

- In the Adobe Experience Platform UI, select Datastreams from DATA COLLECTION in the left rail.
- Select New Datastream .
- Name and describe your datastream. Select your schema from the Event Schema list.
- Select Save .
- Select Add Service .
- In the Add Service screen: Select Adobe Experience Platform from the Service list. Ensure Enabled is selected. Select your dataset from the Event Dataset list. Leave the other settings and select Save to save the datastream.

Your datastream is now configured to forward the data collected from your game to your dataset in Adobe Experience Platform.

See [Datastreams overview](/en/docs/experience-platform/datastreams/overview) for more information on how to configure a datastream and how to handle sensitive data.

## Use Edge Network Server API

In the development of your game, you can add relevant calls to the Adobe Experience Platform Edge Network Server API where appropriate.

For example, to update the score of player, you would use:

```
curl -X POST "https://server.adobedc.net/ee/v2/interact?dataStreamId={DATASTREAM_ID}"
-H "Authorization: Bearer {TOKEN}"
-H "x-gw-ims-org-id: {ORG_ID}"
-H "x-api-key: {API_KEY}"
-H "Content-Type: application/json"
-d '{
   "event": {
      "xdm": {
         "identityMap": {
            "Email_LC_SHA256": [
               {
                  "id": "0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b",
                  "primary": true
               }
            ]
         },
         "eventType": "game.scoreUpdate",
         "{sandbox}": {
            "scores": {
               "afterMatch": 132391",
            }
         },
         "timestamp": "2021-08-09T14:09:20.859Z"
      }
   }
}'
```

In the example POST request, {DATASTREAM_ID} points to the identifier of the example datastream you configured earlier. {sandbox} is the unique name of your sandbox identifying the path to the custom Blinding Light field group.

See [Interactive data collection](/en/docs/experience-platform/edge-network-server-api/data-collection/interactive-data-collection) and [Non-interactive data collection](/en/docs/experience-platform/edge-network-server-api/data-collection/non-interactive-data-collection) for more information on how to use the Edge Network Server API.

## Set up a connection

To use the Adobe Experience Platform data in Customer Journey Analytics, you create a connection that includes the data resulting from setting up your schema, dataset, and workflow.

A connection lets you integrate datasets from Adobe Experience Platform into Workspace. To report on these datasets, you first have to establish a connection between datasets in Adobe Experience Platform and Workspace.

To create your connection:

- In the Customer Journey Analytics UI, select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In the Untitled connection screen: Name and describe your connection in Connection Settings. Select the correct sandbox from the Sandbox list in Data settings and select the number of daily events from the Average number of daily events list. Select Add datasets . In the Select datasets step in Add datasets: Select datasets that you created earlier and/or other relevant datasets you want to include in your connection Select Next . In the Datasets settings step in Add datasets: For each dataset: Select a Person ID from the available identities defined in the dataset schemas in Adobe Experience Platform. Select the correct data source from the Data source type list. If you specify Other , then add a description for your data source. Set Import all new data and Dataset backfill existing data according to your preferences. Select Add datasets . Select Save .

See [Connections overview](/en/docs/analytics-platform/using/cja-connections/overview) for more information on how to create and manage a connection and how to select and combine datasets.

## Set up a data view

A data view is a container specific to Customer Journey Analytics that lets you determine how to interpret data from a connection. It specifies all dimensions and metrics available in Analysis Workspace and which columns those dimensions and metrics obtain their data from. Data views are defined in preparation for reporting in Analysis Workspace.

To create your data view:

- In the Customer Journey Analytics UI, select Data views , optionally from Data management , in the top menu.
- Select Create new data view .
- In the Configure step: Select your connection from the Connection list. Name and (optionally) describe your connection. Select Save and continue .
- In the Components step: Add any schema field and/or standard component that you want to include to the METRICS or DIMENSIONS component boxes. Select Save and continue .
- In the Settings step: Leave the settings as they are and select Save and finish .

See [Data views overview](/en/docs/analytics-platform/using/cja-dataviews/data-views) for more information on how to create and edit a data view, what components are available for you to use in your data view and how to use segment and sessions settings.

## Set up a project

Analysis Workspace is a flexible browser tool that allows you to quickly build analyses and share insights based on your data. You use Workspace projects to combine data components, tables, and visualizations to craft your analysis and share with anyone in your organization.

To create your project:

- In the Customer Journey Analytics UI, select Projects in the top menu.
- Select Projects in the left navigation.
- Select Create project . Select Blank project .
- Select your data view from the list. .
- To create your first report, start dragging and dropping dimensions and metrics on the Freeform table in the Panel.

See [Analysis Workspace overview](/en/docs/analytics-platform/using/cja-workspace/home) for more information on how to create projects and build your analysis using components, visualizations, and panels.

SUCCESS
You have completed all the steps. Starting by defining what data you want to collect (schema) and where to store it (dataset) in Adobe Experience Platform. You configured a datastream on the Edge Network to ensure that data can be forwarded to that dataset. Then you used the Edge Network Server API to send that data to your datastream. You defined a connection in Customer Journey Analytics to use your game data and other data. Your data view definition allowed you to specify which dimension and metrics to use and finally you created your first project visualizing and analyzing your game data.
recommendation-more-help
