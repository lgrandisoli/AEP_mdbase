---
title: "Ingest data via the Web SDK"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-data-ingestion/ingest-use-guides/edge-network/aepwebsdk"
category: "guides"
topic: "analytics-platform/using/cja-data-ingestion/ingest-use-guides"
created_at: "2026-06-02T19:04:36.254176+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Ingest data via the Web SDK

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

This quick start guide explains how you can ingest website tracking data directly into Adobe Experience Platform using the Adobe Experience Platform Web SDK and Edge Network and then use that data in Customer Journey Analytics.

To accomplish this, you need to:

- Set up a schema and dataset in Adobe Experience Platform to define the model (schema) of the data that you want to collect and where to actually collect the data (dataset).
- Set up a datastream to configure the Adobe Experience Platform Edge Network to route your collected data to the dataset you configured in Adobe Experience Platform.
- Use Tags to easily configure rules and data elements against the data in your data layer on your website. Then ensure that the data is sent to the datastream configured on the Adobe Experience Platform Edge Network.
- Deploy and validate . Have an environment where you can iterate on the development of tags and once everything is validated, publish it live on your production environment.
- Set up a connection in Customer Journey Analytics. This connection should (at least) include your Adobe Experience Platform dataset.
- Set up a data view in Customer Journey Analytics to define metrics and dimension that you want to use in Analysis Workspace.
- Set up a project in Customer Journey Analytics to build your reports and visualizations.

NOTE
This quick start guide is a simplified guide on how to ingest data collected from your site into Adobe Experience Platform and use in Customer Journey Analytics. It is highly recommended to study the additional information when referred to.
## Set up a schema and dataset

To ingest data into Adobe Experience Platform, you first must define which data you want to collect. All data ingested into Adobe Experience Platform must conform to a standard, denormalized structure for it be recognized and acted upon by downstream capabilities and features. Experience Data Model (XDM) is the standard framework that provides this structure in the form of schemas.

Once you have defined a schema, you use one or more datasets to store and manage the collection of data. A dataset is a storage and management construct for a collection of data (typically a table) that contains a schema (columns) and fields (rows).

All data that is ingested into Adobe Experience Platform must conform to a pre-defined schema before it can be persisted as a dataset.

### Set up a schema

You want to track some minimal data from profiles visiting your website, for example page name, identification.You first must define a schema that models this data.

To set up your schema:

- In the Adobe Experience Platform UI, in the left rail, select Schemas within DATA MANAGEMENT.
- Select Create schema . .
- In the Select a class step of the Create schema wizard: Select Experience Event . note info INFO An Experience Event schema is used to model the behavior of a profile (like scene name, push button to add to cart). An Individual Profile schema is used to model the profile attributes (like name, email, gender). Select Next .
- In the Name and review step of the Create schema wizard: Enter a Schema display name for your schema and (optional) a Description . Select Finish .
- In the Structure tab of Example Schema: Select + Add in Field groups. Field groups are reusable collections of objects and attributes that allow you to easily extend your schema. In the Add fields groups dialog, select the AEP Web SDK ExperienceEvent field group from the list. You can select the preview button, to see a preview of the fields that are part of this field group, like web > webPageDetails > name . Select Back to close the preview. Select Add field groups .
- Select + next to your schema name in the Structure panel.
- In the Field Properties panel, enter Identification as the name, Identification as the Display name, select Object as the Type and select ExperienceEvent Core v2.1 as the Field Group. note NOTE If that field group is not available, look for another field group containing identity fields. Or create a new field group and add new identity fields (like ecid , crmId , and others you need) to the field group and select that new field group. The identification object adds identification capabilities to your schema. In your case, you want to identify profiles visiting your site using the Experience Cloud ID and email address. There are many other attributes available to track your person’s identification (for example customer id, loyalty id). Select Apply to add this object to your schema.
- Select the ecid field in the identification object you just added, and select Identity and Primary Identity and ECID from the Identity namespace list in the right panel. You are specifying the Experience Cloud Identity as the primary identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles with the same ECID. Select Apply . You see that a fingerprint icon appears in the ecid attribute.
- Select the email field in the identification object you just added, and select Identity and Email from the Identity namespace list in the Field Properties panel. You are specifying the email address as another identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles. Select Apply . You see that a fingerprint icon appears in the email attribute. Select Save .
- Select the root element of your schema displaying the name of the schema, then select the Profile switch. You are prompted to enable the schema for profile. Once enabled, when data is ingested into datasets based on this schema, that data is merged into the Real-Time Customer Profile. See Enable the schema for use in Real-Time Customer Profile for more information. note important IMPORTANT Once you save a schema enabled for profile, it can no longer be disabled for profile.
- Select Save to save your schema.

You have created a minimal schema that models the data you can capture from your website. The schema allows profiles to be identified using the Experience Cloud Identity and email address. By enabling the schema for profile, you ensure data captured from your website is added to the Real-Time Customer Profile.

Next to behavior data, you can also capture profile attribute data from your site (for example details of profiles subscribing to a newsletter).

To capture this profile data, you would:

- Create a schema based on the XDM Individual Profile class.
- Add the Profile Core v2 field group to the schema.
- Add an identification object based on the Profile Core v2 field group.
- Define Experience Cloud ID as primary identifier and email as identifier.
- Enable the schema for profile

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

## Set up a datastream

A datastream represents the server-side configuration when implementing the Adobe Experience Platform Web and Mobile SDKs. When collecting data with the Adobe Experience Platform SDKs, data is sent to the Adobe Experience Platform Edge Network. It is the datastream that determines to which services that data is forwarded.

In your setup, you want the data you collect from the website to be sent to your dataset in Adobe Experience Platform.

To set up your datastream:

- In the Adobe Experience Platform UI, select Datastreams from DATA COLLECTION in the left rail.
- Select New Datastream .
- Name and describe your datastream. Select your schema from the Event Schema list.
- Select Save .
- Select Add Service .
- In the Add Service screen: Select Adobe Experience Platform from the Service list. Ensure Enabled is selected. Select your dataset from the Event Dataset list. Leave the other settings and select Save to save the datastream.

Your datastream is now configured to forward the data collected from your website to your dataset in Adobe Experience Platform.

See [Datastreams overview](/en/docs/experience-platform/datastreams/overview) for more information on how to configure a datastream and how to handle sensitive data.

## Use Tags

To implement code on your site to actually collect data, use the Tags feature within Adobe Experience Platform . This tag management solution lets you deploy code alongside other tagging requirements. Tags offer seamless integration with Adobe Experience Platform using the Adobe Experience Platform Web SDK extension.

### Create your tag

- In the Adobe Experience Platform UI, in the left rail, select Tags within DATA COLLECTION.
- Select New Property . Name the tag, select Web and enter a domain name. Select Save to continue.

### Configure your tag

After creating the tag, you must configure it with the correct extensions and configure data elements and rules according to how you want to track your site and send data to Adobe Experience Platform.

Select your newly created tag from the list of Tag Properties to open it.

#### Extensions

To ensure you can send data to Adobe Experience Platform (via your datastream), add the Adobe Platform Web SDK extension to your tag.

To create and configure the Adobe Experience Platform Web SDK extension:

- Select Extensions in the left rail.
- Select Catalog in the top bar.
- Search for or scroll to the Adobe Experience Platform Web SDK extension, and Select Install to install it. {width="35%"}
- Select your sandbox and your earlier created datastream for your Production Environment and (optional) Staging Environment and Development Environment. Select Save .

See [Configure the Adobe Experience Platform Web SDK extension](/en/docs/experience-platform/tags/extensions/client/web-sdk/web-sdk-extension-configuration) for more information.

The Web SDK includes the Adobe Experience Cloud ID Service natively, so you do not need to add the ID service extension to your tag.

#### Data Elements

Data elements are the building blocks for your data dictionary (or data map). Use data elements to collect, organize, and deliver data across marketing and ad technology. You set up data elements in your tag that read from your data layer and can be used to deliver data into Adobe Experience Platform.

There are different types of data elements. You first set up a data element to capture the page name persons are viewing on your site.

To define a page name data element:

- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog: Name your data element, for example Page Name . Select Core from the Extension list. Select Page Info from the Data Element Type list. Select Title from the Attribute list. Alternatively you could have used the value from a variable of your data layer, for example pageName and the JavaScript Variable data element type to define the data element. Select Save .

You now want to set up a data element referencing the Experience Cloud ID that is automatically provided by the Adobe Experience Platform Web SDK and available through the Experience Cloud ID Service extension.

To define an ECID data element:

- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog: Name your data element, for example ECID . Select Experience Cloud ID Service from the Extension list. Select ECID from the Data Element Type list. Select Save .

Finally, you now want to map any of your specific data elements to the schema you defined earlier. You define another data element which provides a representation of your XDM schema.

To define an XDM object data element:

- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog: Name your data element, for example XDM - Page View . Select Adobe Experience Platform Web SDK from the Extension list. Select XDM Object from the Data Element Type list. Select your sandbox from the Sandbox list. Select your schema from the Schema list. Map the identification > core > ecid attribute, defined in your schema, to the ECID data element. Select the cylinder icon to easily pick the ECID data element from your list of data elements. Map the web > webPageDetails > name attribute, defined in your schema, to the Page Name data element. Select Save .

#### Rules

Tags in Adobe Experience Platform follow a rule-based system. They look for user interaction and associated data. When the criteria outlined in your rules are met, the rule triggers the extension, script, or client-side code you identified. You can use rules to send data (like an XDM object) into Adobe Experience Platform using the Adobe Experience Platform Web SDK extension.

To define a rule:

- Select Rules in the left rail.
- Select Create New Rule .
- In the Create Rule dialog: Name the rule, for example Page View . Select + Add underneath Events. In the Event Configuration dialog: Select Core from the Extension list. Select Window Loaded from the Event Type list. Select Keep Changes . Select + Add underneath Actions. In the Action Configuration dialog: Select Adobe Experience Platform Web SDK from the Extension list. Select Send Event from the Action Type list. Select web.webpagedetails.pageViews from the Type list. Select the cylinder icon next to XDM data and Select XDM - Page View from the list of data elements. Select Keep Changes . Your rule should look like: Select Save .

The above is just an example of defining a rule that sends XDM data, containing values from other data elements, to Adobe Experience Platform.

You can use rules in various ways in your tag to manipulate variables (using your data elements).

See [Rules](/en/docs/experience-platform/tags/ui/rules) for more information.

### Build and Publish your tag

After having defined data elements and rules, you must build and publish your tag. When you create a library build, you must assign it to an environment. The build’s extensions, rules, and data elements are then compiled and placed into the assigned environment. Each environment provides a unique embed code that allows you to integrate its assigned build into your site.

To build and publish your tag:

- Select Publishing Flow from the left rail.
- Select Select a working library , followed by Add Library… .
- In the Create Library dialog: Name the library. Select Development (development) from the Environment list. Select + Add All Changed Resources . Select Save & Build to Development . Your tag is saved and is built for your development environment. A green dot indicates a successful build of your tag on your development environment.
- You can select … to rebuild the library or move the library to a staging or production environment.

Adobe Experience Platform Tags support simple to complex publishing workflows that should accommodate your deployment of the Adobe Experience Platform Web SDK.

See [Publishing overview](/en/docs/experience-platform/tags/publish/overview) for more information.

### Retrieve your tag code

Finally you must install your tag on the website you want to track, which implies placing code in the header tag of your website’s template.

To get the code that references your tag:

- Select Environments in the left rail.
- From the list of environments, select the correct install (box) button. In the Web Install Instructions dialog, select the copy button next to the script code that should read like: code language-none <script src="https://assets.adobedtm.com/2a518741ab24/.../launch-...-development.min.js" async></script>>
- Select Close .

Instead of the code for the development environment, you could have selected another environment (staging, production) based on where you are in the process of deploying the Adobe Experience Platform Web SDK.

See [Environments](/en/docs/experience-platform/tags/publish/environments/environments) for more information.

## Deploy and validate

You can now deploy the code on the development version of your website inside the <head> tag. When deployed, your website starts collecting data into Adobe Experience Platform.

Validate your implementation, correct it where necessary, and once correct, deploy it to your staging and production environment using the publishing workflow feature of Tags.

## Set up a connection

To use the Adobe Experience Platform data in Customer Journey Analytics, you create a connection that includes the data resulting from setting up your schema, dataset, and workflow.

A connection lets you integrate datasets from Adobe Experience Platform into Workspace. To report on these datasets, you first have to establish a connection between datasets in Adobe Experience Platform and Workspace.

To create your connection:

- In the Customer Journey Analytics UI, select Connections , optionally from Data management , in the top menu.
- Select Create new connection .
- In the Untitled connection screen: Name and describe your connection in Connection Settings. Select the correct sandbox from the Sandbox list in Data settings and select the number of daily events from the Average number of daily events list. Select Add datasets . In the Select datasets step in Add datasets: Select the dataset that you created earlier ( Example dataset ) and any other dataset you want to include in your connection. Select Next . In the Datasets settings step in Add datasets: For each dataset: Select a Person ID from the available identities defined in the dataset schemas in Adobe Experience Platform. Select the correct data source from the Data source type list. If you specify Other , then add a description for your data source. Set Import all new data and Dataset backfill existing data according to your preferences. Select Add datasets . Select Save .

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
- To create your first report, start dragging and dropping dimensions and metrics on the Freeform table in the Panel. As an example, drag Program Points Balance and Page View as metrics and email as dimension to get a quick overview of profiles that have visited your website and are part of the loyalty program collecting loyalty points.

See [Analysis Workspace overview](/en/docs/analytics-platform/using/cja-workspace/home) for more information on how to create projects and build your analysis using components, visualizations, and panels.

SUCCESS
You have completed all the steps. Starting by defining what data you want to collect (schema) and where to store it (dataset) in Adobe Experience Platform. You then configured a datastream on the Edge Network to ensure that data can be forwarded to that dataset. Then you defined and deployed your tag containing the extensions (Adobe Experience Platform Web SDK, Experience Cloud ID Service), data elements, and rules to capture data from your website and send that data to your datastream. You defined a connection in Customer Journey Analytics to use your website tracking data and other data. Your data view definition allowed you to specify which dimension and metrics to use and finally you created your first project visualizing and analyzing your data.
recommendation-more-help
