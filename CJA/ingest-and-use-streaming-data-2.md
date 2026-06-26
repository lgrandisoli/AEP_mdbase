---
title: "Ingest and use streaming data"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/streaming"
category: "guides"
topic: "analytics-platform/using/cja-data-ingestion/ingest-use-guides"
created_at: "2026-06-23T20:42:03.794163+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest and use streaming data

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

This quick start guide explains how you can ingest streaming data into Adobe Experience Platform and then use that data in Customer Journey Analytics.

To accomplish this, you need to:

- Set up a schema and dataset in Adobe Experience Platform to define the model (schema) of the data that you want to collect and where to actually collect the data (dataset).
- Use HTTP API source connector to easily stream your data into the dataset configured in Adobe Experience Platform.
- Set up a connection in Customer Journey Analytics. This connection should (at least) include your Adobe Experience Platform dataset.
- Set up a data view in Customer Journey Analytics to define metrics and dimension that you want to use in Analysis Workspace.
- Set up a project in Customer Journey Analytics to build your reports and visualizations.

NOTE
This quick start guide is a simplified guide on how to ingest streaming data into Adobe Experience Platform and use in Customer Journey Analytics. It is highly recommended to study the additional information when referred to.
## Set up a schema and dataset

To ingest data into Adobe Experience Platform, you first must define which data you want to collect. All data ingested into Adobe Experience Platform must conform to a standard, denormalized structure for it be recognized and acted upon by downstream capabilities and features. Experience Data Model (XDM) is the standard framework that provides this structure in the form of schemas.

Once you have defined a schema, you use one or more datasets to store and manage the collection of data. A dataset is a storage and management construct for a collection of data (typically a table) that contains a schema (columns) and fields (rows).

All data that is ingested into Adobe Experience Platform must conform to a pre-defined schema before it can be persisted as a dataset.

### Set up a schema

For this quick start, you want to collect some loyalty data, for example loyalty id, loyalty points, and loyalty status.You first must define a schema that models this data.

To set up your schema:

- In the Adobe Experience Platform UI, in the left rail, select Schemas within DATA MANAGEMENT.
- Select Create schema . .
- In the Select a class step of the Create schema wizard: Select Individual Profile . note info INFO An Experience Event schema is used to model the behavior of a profile (like scene name, push button to add to cart). An Individual Profile schema is used to model the profile attributes (like name, email, gender). Select Next .
- In the Name and review step of the Create schema wizard: Enter a Schema display name for your schema and (optional) a Description . Select Finish .
- In the Structure tab of Example Schema: Select + Add in Field groups. Field groups are reusable collection of objects and attributes that allow you to easily extend your schemas. In the Add fields groups dialog, select the Loyalty Details field group from the list. You can select the preview button, to see a preview of the fields that are part of this field group. Select Back to close the preview. Select Add field groups .
- Select + next to your schema name in the Structure panel.
- In the Field Properties panel, enter Identification as the name, Identification as the Display name, select Object as the Type and select Profile Core v2 as the Field Group. This identification object adds identification capabilities to your schema. In your case, you want to identify loyalty information using the email address in your batch data. Select Apply to add this object to your schema.
- Select the email field in the identification object you just added, and select Identity and Email from the Identity namespace in the Field Properties panel. You are specifying the email address as the identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles. Select Apply . You see that a fingerprint icon appears in the email attribute.
- Select the root level of your schema (with the schema name), then select the Profile switch. You are prompted to enable the schema for profile. Once enabled, when data is ingested into datasets based on this schema, that data is merged into the Real-Time Customer Profile. See Enable the schema for use in Real-Time Customer Profile for more information. note important IMPORTANT Once you save a schema enabled for profile, it can no longer be disabled for profile.
- Select Save to save your schema.

You have created a minimal schema that models the loyalty data you can ingest into Adobe Experience Platform . The schema allows profiles to be identified using the email address. By enabling the schema for profile, you ensure that data from your streaming source is added to the Real-Time Customer Profile.

See [Create and edit schemas in the UI](/en/docs/experience-platform/xdm/ui/resources/schemas) for more information on adding and removing field groups and individual fields to a schema.

### Set up a dataset

With your schema, you have defined your data model. You now have to define the construct to store and manage that data, which is done through datasets.

To set up your dataset:

- In the Adobe Experience Platform UI, in the left rail, select Datasets within DATA MANAGEMENT.
- Select Create dataset .
- Select Create dataset from schema .
- Select the schema that you created earlier and select Next .
- Name your dataset and (optional) provide a description.
- Select Finish .
- Select the Profile switch. You are prompted to enable the dataset for profile. Once enabled, the dataset enriches real-time customer profiles with its ingested data. note important IMPORTANT You can only enable a dataset for profile when the schema, to which the dataset adheres, is also enabled for profile.

See [Datasets UI guide](/en/docs/experience-platform/catalog/datasets/user-guide) for much more information on how to view, preview, create, delete a dataset. And how to enable a dataset for Real-Time Customer Profile.

## Set up an HTTP API streaming connection

Your source application streams data that conforms to the schema that you created, and looks like.

```
{
    ...
    "_demosystem4": {
        "identification": {
            "core": {
                "email": "abrocking0@blog.com",
                "loyaltyId": "793406",
            }
        }
    },
    "loyalty": {
        "loyaltyID": [
            "793406"
        ],
        "points": 82.16,
        "status": "Silver"
    }
    ...
}
```

To stream this data into the dataset that you created, you must define a streaming endpoint for that data to be sent to. A streaming endpoint is created using an HTTP API source connector.

To create an HTTP API source connector:

- In the Experience Platform UI, select Sources under CONNECTIONS in the left rail.
- Select Streaming from list of CATEGORIES.
- Select Set up in the HTTP API tile.
- In the Authentication step of the Add data screen: Enter a name and description for your HTTP API connection. Select XDM compatible to indicate the data that you stream is compatible with an existing XDM schema. Select Connect to source . After a successful connection, you will see Connected. Select Next to continue.
- In the Dataflow detail step of the Add data screen: Select Existing dataset , select your dataset from the dataset list, and name your Dataflow name. Select Next .
- The Review step of the Add data screen provides you with an overview of the HTTP API connection. Select Finish .
- You see the final definition of your HTTP API streaming endpoint.

You can copy the streaming endpoint URL and use it to configure your loyalty application to stream data into the Adobe Experience Platform loyalty dataset.

See [Create an HTTP API streaming connection using the UI](/en/docs/experience-platform/sources/ui-tutorials/create/streaming/http) for a much more comprehensive tutorial explaining:

- how to use authentication,
- how to map data when your incoming data is not compatible with your XDM schema, and
- how to create a dataset as part of setting up the streaming connector.

## Set up a connection

To use the Adobe Experience Platform data in Customer Journey Analytics, you create a connection that includes the data resulting from setting up your schema, dataset, and workflow.

A connection lets you integrate datasets from Adobe Experience Platform into Workspace. To report on these datasets, you first have to establish a connection between datasets in Adobe Experience Platform and Workspace.

To create your connection:

- In the Customer Journey Analytics UI, select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In the Untitled connection screen: Name and describe your connection in Connection Settings. Select the correct sandbox from the Sandbox list in Data settings and select the number of daily events from the Average number of daily events list. Select Add datasets . In the Select datasets step in Add datasets: Select the dataset that you created earlier ( Example Loyalty Dataset ) and any other dataset you want to include in your connection. Select Next . In the Datasets settings step in Add datasets: For each dataset: Select a Person ID from the available identities defined in the dataset schemas in Adobe Experience Platform. Select the correct data source from the Data source type list. If you specify Other , then add a description for your data source. Set Import all new data and Dataset backfill existing data according to your preferences. Select Add datasets . Select Save .

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
- To create your first report, start dragging and dropping dimensions and metrics on the Freeform table in the Panel . As an example, drag Program Points Balance and Page View as metrics and email as dimension to get a quick overview of profiles that have visited your website and are part of the loyalty program collecting loyalty points.

See [Analysis Workspace overview](/en/docs/analytics-platform/using/cja-workspace/home) for more information on how to create projects and build your analysis using components, visualizations, and panels.

SUCCESS
You have completed all the steps. Starting by defining what loyalty data you want to collect (schema) and where to store it (dataset) in Adobe Experience Platform, you configured an HTTP API source connector to stream loyalty data directly into the dataset. Your data view definition allowed you to specify which dimension and metrics to use and finally you created your first project visualizing and analyzing your data.
recommendation-more-help
