---
title: "Ingest data via the Mobile SDK"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepmobilesdk"
category: "guides"
topic: "analytics-platform/using/cja-data-ingestion/ingest-use-guides"
created_at: "2026-06-02T19:04:34.933622+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest data via the Mobile SDK

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

This quick start guide explains how you can ingest mobile app tracking data directly into Adobe Experience Platform using the Adobe Experience Platform Mobile SDK and Edge Network. Then use that data in Customer Journey Analytics.

To accomplish this, you need to:

- Set up a schema and dataset in Adobe Experience Platform to define the model (schema) of the data that you want to collect and where to actually collect the data (dataset).
- Set up a datastream to configure the Adobe Experience Platform Edge Network to route your collected data to the dataset you configured in Adobe Experience Platform.
- Use Tags to easily configure rules and data elements against the data in your mobile application. Then ensure that the data is sent to the datastream configured on the Adobe Experience Platform Edge Network.
- Deploy and validate . Have an environment where you can iterate on the development of tags and once everything is validated, publish it live on your production environment.
- Set up a connection in Customer Journey Analytics. This connection should (at least) include your Adobe Experience Platform dataset.
- Set up a data view in Customer Journey Analytics to define metrics and dimension that you want to use in Analysis Workspace.
- Set up a project in Customer Journey Analytics to build your reports and visualizations.

NOTE
This quick start guide is a simplified guide on how to ingest data collected from your application into Adobe Experience Platform and use in Customer Journey Analytics. It is highly recommended to study the additional information when referred to.
## Set up a schema and dataset

To ingest data into Adobe Experience Platform, you first need to define which data you want to collect. All data ingested into Adobe Experience Platform must conform to a standard, denormalized structure for it be recognized and acted upon by downstream capabilities and features. Experience Data Model (XDM) is the standard framework that provides a structure in the form of schemas.

Once you have defined a schema, you use one or more datasets to store and manage the collection of data. A dataset is a storage and management construct for a collection of data (typically a table) that contains a schema (columns) and fields (rows).

All data that is ingested into Adobe Experience Platform must conform to a pre-defined schema before it can be persisted as a dataset.

### Set up a schema

You want to track some minimal data from profiles using your mobile app, for example scene name, identification.You first need to define a schema that models this data.

To set up your schema:

- In the Adobe Experience Platform UI, in the left rail, select Schemas within DATA MANAGEMENT.
- Select Create schema . .
- In the Select a class step of the Create schema wizard: Select Experience Event . note info INFO An Experience Event schema is used to model the behavior of a profile (like scene name, push button to add to cart). An Individual Profile schema is used to model the profile attributes (like name, email, gender). Select Next .
- In the Name and review step of the Create schema wizard: Enter a Schema display name for your schema and (optional) a Description . Select Finish .
- In the Structure tab of Example Schema: Select + Add in Field groups. Field groups are reusable collections of objects and attributes that allow you to easily extend your schema. In the Add fields groups dialog, select the AEP Mobile SDK ExperienceEvent field group from the list. You can select the preview button, to see a preview of the fields that are part of this field group, like application > name . Select Back to close the preview. Select Add field groups .
- Select + next to your schema name in the Structure panel.
- In the Field Properties panel, enter identification as the Field name, Identification as the Display name, select Object as the Type and select ExperienceEvent Core v2.1 as the Field Group. note NOTE If that field group is not available, look for another field group containing identity fields. Or create a new field group and add new identity fields (like ecid , crmId , and others you need) to the field group and select that new field group. The identification object adds identification capabilities to your schema. In your case, you want to identify profiles using your mobile app using the Experience Cloud ID and email address. There are many other attributes available to track your person’s identification (for example customer id, loyalty id). Select Apply to add this object to your schema.
- Select the ecid field in the identification object you just added, and select Identity and Primary Identity and ECID from the Identity namespace list in the right panel. You are specifying the Experience Cloud Identity as the primary identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles with the same ECID. Select Apply . You see that a fingerprint icon appears in the ecid attribute.
- Select the email field in the identification object you just added, and select Identity and Email from the Identity namespace list in the Field Properties panel. You are specifying the email address as another identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles. Select Apply . You see that a fingerprint icon appears in the email attribute. Select Save .
- Select the root element of your schema displaying the name of the schema, then select the Profile switch. You are prompted to enable the schema for profile. Once enabled, when data is ingested into datasets based on this schema, that data is merged into the Real-Time Customer Profile. See Enable the schema for use in Real-Time Customer Profile for more information. note important IMPORTANT Once you save a schema enabled for profile, it can no longer be disabled for profile.
- Select Save to save your schema.

You have created a minimal schema that models the data you can capture from your mobile application. The schema allows profiles to be identified using the Experience Cloud Identity and email address. By enabling the schema for profile, you ensure data captured from your mobile application is added to the Real-Time Customer Profile.

Next to behavior data, you can also capture profile attribute data from your mobile application (for example details of profiles subscribing to a newsletter).

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

A datastream represents the server-side configuration when implementing the Adobe Experience Platform Web and Mobile SDKs. When collecting data with the Adobe Experience Platform SDKs, data is sent to the Adobe Experience Platform Edge Network. It is the datastream that determines to which services that data is forwarded.

In your setup, you want the data you collect from the mobile app to be sent to your dataset in Adobe Experience Platform.

To set up your datastream:

- In the Adobe Experience Platform UI, select Datastreams from DATA COLLECTION in the left rail.
- Select New Datastream .
- Name and describe your datastream. Select your schema from the Event Schema list.
- Select Save .
- Select Add Service .
- In the Add Service screen: Select Adobe Experience Platform from the Service list. Ensure Enabled is selected. Select your dataset from the Event Dataset list. Leave the other settings and select Save to save the datastream.

Your datastream is now configured to forward the data collected from your mobile app to your dataset in Adobe Experience Platform.

See [Datastreams overview](/en/docs/experience-platform/datastreams/overview) for more information on how to configure a datastream and how to handle sensitive data.

## Use Tags

To implement code on your site to actually collect data, use the Tags feature within Adobe Experience Platform. This tag management solution lets you deploy code alongside other tagging requirements. Tags offer seamless integration with Adobe Experience Platform using the Adobe Experience Platform Mobile SDK extension.

### Create your tag

- In the Adobe Experience Platform UI, in the left rail, select Tags within DATA COLLECTION.
- Select New Property . Name the tag, select Mobile . Select Save to continue.

### Configure your tag

After creating the tag, you need to configure it with the correct extensions and configure data elements and rules according to how you want to track your site and send data to Adobe Experience Platform.

To configure, select your newly created tag from the list of Tag Properties.

#### Extensions

Add the Adobe Platform Edge Network extension to your tag to ensure you can send data to Adobe Experience Platform (via your datastream).

To create and configure the Adobe Experience Platform Mobile SDK extension:

- Select Extensions in the left rail. You see that the Mobile Core and Profile extensions are already available.
- Select Catalog in the top bar.
- Search for or scroll to the Adobe Experience Platform Edge Network extension, and Select Install in the right pane to install it.
- Select your sandbox and your earlier created datastream for your Production Environment and (optional) Staging Environment and Development Environment.
- Enter your Edge Network domain underneath Domain configuration. Typically use <organizationName>.data.adobedc.net .
- Select Save .

See [Configure the Adobe Experience Platform Edge Network extension](https://developer.adobe.com/client-sdks/documentation/edge-network) for more information.

You also want to set up the following additional extensions from the catalog:

- Identity.
- AEP Assurance.
- Consent.

See [Configure a tag property](/en/docs/platform-learn/implement-mobile-sdk/initial-configuration/configure-tags) in the Mobile App Tutorial for Experience platform for much more information on extensions and their configuration.

#### Data Elements

Data elements are the building blocks for your data dictionary (or data map). Use data elements to collect, organize, and deliver data across marketing and ad technology. You set up data elements in your tag that read from mobile app data or events and can be used to deliver data into Adobe Experience Platform.

For example, you want to collect the carrier name from the mobile app.

To define a carrier name data element:

- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog: Name your data element, for example Carrier Name . Select Mobile Core from the Extension list. Select Carrier Name from the Data Element Type list. Select Save .

You can create as many data elements you want, and use them in rules.

#### Rules

Tags in Adobe Experience Platform follow a rule-based system. They look for user interaction and associated data. When the criteria outlined in your rules are met, the rule triggers the extension, script, or client-side code you identified. You can use rules to send data (like an XDM object) into Adobe Experience Platform using the Adobe Experience Platform Edge Network extension.

For example, you want to send event data when the mobile app is used (in the foreground) and when the mobile app is not used (pushed back to the background).

To define a rule:

- Select Rules in the left rail.
- Select Create New Rule .
- In the Create Rule dialog: Name the rule, for example Application Status . Select + Add underneath Events. In the Event Configuration dialog: Select Mobile Core from the Extension list. Select Foreground from the Event Type list. Select Keep Changes . Click next to Mobile Core - Foreground. Select Mobile Core from the Extension list. Select Background from the Event Type list. Select Keep Changes . Click Add underneath ACTIONS. In the Action Configuration dialog: Select Adobe Experience Platform Edge Network from the Extension list. Select Forward event to Edge Network from the Action Type list. Select Keep Changes . Your rule should look like: Select Save .

The above is just an example of defining a rule that sends XDM data, containing application status, to the Adobe Edge Network and to Adobe Experience Platform.

You can use rules in various ways in your tag to manipulate variables (using your data elements).

See [Rules](https://developer.adobe.com/client-sdks/documentation/lifecycle-for-edge-network/#configure-a-rule-to-forward-lifecycle-metrics-to-platform) for more information.

### Build and Publish your tag

After having defined data elements and rules, you need to build and publish your tag. When you create a library build, you must assign it to an environment. The build’s extensions, rules, and data elements are then compiled and placed into the assigned environment. Each environment provides a unique embed code that allows you to integrate its assigned build into your site.

To build and publish your tag:

- Select Publishing Flow from the left rail.
- Select Select a working library , followed by Add Library… .
- In the Create Library dialog: Name the library. Select Development (development) from the Environment list. Select + Add All Changed Resources . Select Save & Build to Development . Your tag is saved and is built for your development environment. A green dot indicates a successful build of your tag on your development environment.
- You can select … to rebuild the library or move the library to a staging or production environment.

Adobe Experience Platform Tags support simple to complex publishing workflows that should accommodate your deployment of the Adobe Experience Platform Edge Network.

See [Publishing overview](https://developer.adobe.com/client-sdks/documentation/getting-started/create-a-mobile-property/#publish-the-configuration) for more information.

### Retrieve your tag code

Finally you need to use your tag within the mobile app you want to track.

To get code instructions that explain how to set up your mobile app and use your tag in the app:

- Select Environments in the left rail.
- From the list of environments, select the correct install button. In the Mobile Install Instructions dialog, select the appropriate platform (iOS, Android). Then use the copy button next to each of the relevant code snippets that you want to use to set up and initialize your mobile app:
- Select Close .

Instead of the code for the development environment, you could have selected another environment (staging, production) based on where you are in the process of deploying the Adobe Experience Platform Mobile SDK.

See [Environments](/en/docs/experience-platform/tags/publish/environments/environments) for more information.

## Deploy and validate

You can now deploy the code within your mobile app. When deployed, your mobile app starts collecting data into Adobe Experience Platform.

Validate your implementation, correct it where necessary, and once correct, deploy it to your staging and production environment using the publishing workflow feature of Tags.

See [Implement Adobe Experience Cloud in mobile apps tutorial](/en/docs/platform-learn/implement-mobile-sdk/overview) for much more detailed information.

## Set up a connection

To use the Adobe Experience Platform data in Customer Journey Analytics, you create a connection that includes the data resulting from setting up your schema, dataset, and workflow.

A connection lets you integrate datasets from Adobe Experience Platform into Workspace. To report on these datasets, you first have to establish a connection between datasets in Adobe Experience Platform and Workspace.

To create your connection:

- In the Customer Journey Analytics UI, select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In the Untitled connection screen: Name and describe your connection in Connection Settings. Select the correct sandbox from the Sandbox list in Data settings and select the number of daily events from the Average number of daily events list. Select Add datasets . In the Select datasets step in Add datasets: Select datasets that you created earlier and/or other relevant datasets you want to include in your connection (for example Push Tracking Experience Events data and Push Profile data from Adobe Journey Optimizer) Select Next . In the Datasets settings step in Add datasets: For each dataset: Select a Person ID from the available identities defined in the dataset schemas in Adobe Experience Platform. Select the correct data source from the Data source type list. If you specify Other , then add a description for your data source. Set Import all new data and Dataset backfill existing data according to your preferences. Select Add datasets . Select Save .

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
- To create your first report, start dragging and dropping dimensions and metrics on the Freeform table in the Panel . As an example, drag Events as metrics and Push Title as dimension, broken down by Event Type to get an overview of your push notifications for your mobile app and what happened to them.

See [Analysis Workspace overview](/en/docs/analytics-platform/using/cja-workspace/home) for more information on how to create projects and build your analysis using components, visualizations, and panels.

SUCCESS
You have completed all the steps. Starting by defining what data you want to collect (schema) and where to store it (dataset) in Adobe Experience Platform, you configured a datastream on the Edge Network to ensure that data can be forwarded to that dataset. Then you defined and deployed your tag containing the extensions (Adobe Experience Platform Edge Network, and others), data elements, and rules to capture data from your mobile app and send that data to your datastream. You defined a connection in Customer Journey Analytics to use your mobile app push notification tracking data and other data. Your data view definition allowed you to specify which dimension and metrics to use and finally you created your first project visualizing and analyzing your mobile app data.
recommendation-more-help
