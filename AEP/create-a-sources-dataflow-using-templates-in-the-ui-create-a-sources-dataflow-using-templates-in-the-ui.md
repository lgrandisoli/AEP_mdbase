---
title: "Create a sources dataflow using templates in the UI create-a-sources-dataflow-using-templates-in-the-ui"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/templates"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T17:07:55.209303+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

[Beta]{class="badge informative"}

# Create a sources dataflow using templates in the UI create-a-sources-dataflow-using-templates-in-the-ui

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
Templates are in beta and are supported by the following sources:
- [Marketo Engage](/en/docs/experience-platform/sources/connectors/adobe-applications/marketo/marketo)
- [Microsoft Dynamics](/en/docs/experience-platform/sources/connectors/crm/ms-dynamics)
- [Salesforce](/en/docs/experience-platform/sources/connectors/crm/salesforce)

The documentation and functionalities are subject to change.
Adobe Experience Platform provides pre-configured templates that you can use to accelerate your data ingestion process. Templates include auto-generated assets such as schemas, datasets, identities, mapping rules, identity namespaces, and dataflows that you can use when bringing in data from a source to Experience Platform.

With templates, you can:

- Reduce time-to-value of ingestion through acceleration of templatized asset creation.
- Minimize errors that can occur during the manual data ingestion process.
- Update auto-generated assets at any point to suit your use cases.

The following tutorial provides steps on how to use templates in the Experience Platform UI.

## Getting Started

This tutorial requires a working understanding of the following components of Experience Platform:

- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Experience Data Model (XDM) System](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

## Use templates in the Experience Platform UI use-templates-in-the-platform-ui

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace and see a catalog of sources available in Experience Platform.

Use the *Categories* menu to filter sources by category. Alternatively, enter a source name in the search bar to find a specific source from the catalog.

Go to the Adobe applications category to see the Marketo Engage source card and then, select Add data to begin.

A pop-up window appears presenting you with the option to browse templates or use existing schemas and datasets.

- **Browse templates**: Sources templates auto-creates schemas, identities, datasets, and dataflows with mapping rules for you. You can customize these assets as needed.
- **Use my existing assets**: Ingest your data using existing datasets and schemas that you created. You can also create new datasets and schemas if needed.

NOTE
Templates can auto-generate relational schemas when working with sources that require change data capture workflows or support multiple data models. These schemas enable Data Mirror capabilities for real-time data synchronization.
When using templates with relational schemas, the auto-generated assets will include the required primary key, version identifier, and timestamp identifier fields.
For more information, see the
Data Mirror overview
and
relational schemas technical reference
.
To use auto-generated assets, select **Browse templates** and then select **Select**.

### Authentication

The authentication step appears, prompting you to either create a new account or use an existing account.

Use an existing account
To use an existing account, select Existing account and then select the account that you want to use from the list that appears.

Create a new account
To create a new account, select **New account**, and then provide your source connection details and account authentication credentials. When finished, select **Connect to source** and allow some time for the new connection to establish.

### Select templates

With your account authenticated, you can now select the template that you would like to use for your dataflow.

Marketo Engage templates
The following table outlines the templates available for the Marketo Engage source.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 layout-auto |  |
| --- | --- |
| Marketo Engage templates | Description |
| Activities | The Activities template captures event-based snapshots of activities such as email interactions, website interactions, and sales calls. |
| Companies | The Companies template captures business account details such as company firmographic information, location, and billing information. |
| Named Accounts | The Named Accounts template captures details for accounts that have been determined as target accounts to pursue. |
| Opportunities | The Opportunities template captures business opportunity details such as type, sales stage, and related accounts. |
| Opportunity Contact Roles | The Opportunity Contact Roles template captures details about the roles for leads associated with a particular opportunity. |
| Persons | The Persons template captures attributes for individual people such as demographic details, contact information, and consent preferences. |
| Program Memberships | The Program Memberships template captures details for contacts associated with a business campaign, include nurture cadences and contact responses. |
| Programs | The Programs template captures business campaign details like status, channels, timelines, and costs. |
| Static List Memberships | The Static List Memberships template captures teh relationships between people and their membership in static lists. |
| Static Lists | The Static List template captures instantiated lists of people for specific use cases. |

Salesforce B2B templates
The following table outlines the B2B templates available for the Salesforce source.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 layout-auto |  |
| --- | --- |
| Salesforce B2B templates | Description |
| Account Contact Relation | The Account Contact Relation template captures the relationship between a contact and one or more accounts. |
| Accounts | The Account template captures business account details such as company firmographic information, location, and billing information. |
| Campaign Members | The Campaign Members template captures the relationship between an individual lead or contact and a specific Salesforce campaign. |
| Campaigns | The Campaigns template captures business account details such as company firmographic information, location, and billing information. |
| Contacts | The Contact template captures attributes for contacts such as demographics details, contact information, and related business entities. |
| Leads | The Leads template captures attributes for leads such as demographics details, contact information, and related business entities. |
| Opportunities | The Opportunities template captures business opportunity details such as type, sales stage, and related account. |
| Opportunity Contact Roles | The Opportunity Contact Roles template captures details about the roles for leads associated with a particular opportunity. |

Salesforce B2C templates
The following table outlines the B2C templates available for the Salesforce source.

| table 0-row-2 1-row-2 2-row-2 layout-auto |  |
| --- | --- |
| Salesforce B2C templates | Description |
| Contact | The Contact template captures attributes for contacts such as demographics details, contact information, and related business entities. |
| Lead | The Lead template captures attributes for leads such as demographics details, contact information, and related business entities. |

Microsoft Dynamics B2B templates
The following table outlines the B2B templates available for the Microsoft Dynamics source.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 layout-auto |  |
| --- | --- |
| Microsoft Dynamics B2B templates | Description |
| Accounts | The Account template captures business account details such as company firmographic information, location, and billing information. |
| Campaigns | The Campaigns template captures business account details such as company firmographic information, location, and billing information. |
| Contacts | The Contact template captures attributes for contacts such as demographics details, contact information, and related business entities. |
| Leads | The Leads template captures attributes for leads such as demographics details, contact information, and related business entities. |
| Marketing List | The Marketing List template captures a group of existing or potential customers created for a marketing campaign or other sales purposes. |
| Marketing List Members | The Marketing List Members captures the details of any one type of customer record, such as leads, accounts, or contacts, in a marketing list. |
| Opportunities | The Opportunities template captures business opportunity details such as type, sales stage, and related account. |
| Opportunity Contact Roles | The Opportunity Contact Roles template captures details about the roles for leads associated with a particular opportunity. |

Microsoft Dynamics B2C templates
The following table outlines the B2C templates available for the Microsoft Dynamics source.

| table 0-row-2 1-row-2 2-row-2 layout-auto |  |
| --- | --- |
| Microsoft Dynamics B2C templates | Description |
| Contact | The Contact template captures attributes for contacts such as demographics details, contact information, and related business entities. |
| Lead | The Lead template captures attributes for leads such as demographics details, contact information, and related business entities. |

Depending on the business type that you selected, a list of templates appears. Select the preview icon beside a template name to preview sample data from the template.

The preview window appears allowing you to explore and inspect sample data from your template. When finished, select **Got it**.

Next, select the template that you would like to use from the list. You can select multiple templates and create multiple dataflows at once. However, a template can only be used once per account. Once you have selected your templates, select **Finish** and allow a few moments for the assets to generate.

If you select one or partial items from the list of available templates, all B2B schemas and identity namespaces will still be generated to ensure that B2B relationships across schemas are configured correctly.

NOTE
Templates that have already been used will be disabled from selection.
### Set a schedule

The Microsoft Dynamics and the Salesforce sources both support scheduling dataflows.

Use the scheduling interface to configure an ingestion schedule for your dataflows. Set your ingestion frequency to **Once** to create a one-time ingestion.

Alternatively, you can set your ingestion frequency to **Minute**, **Hour**, **Day**, or **Week**. If schedule your dataflow for multiple ingestions, then you must set an interval to establish a time frame between every ingestion. For example, an ingestion frequency set to **Hour** and an interval set to **15** means that your dataflow is scheduled to ingest data every **15 hours**.

During this step, you can also enable **backfill** and define a column for the incremental ingestion of data. Backfill is used to ingest historical data, while the column you define for incremental ingestion allows new data to be differentiated from existing data.

Once you have completed configuring your ingestion schedule, select **Finish**.

### Review assets review-assets

The Review template assets page displays the assets auto-generated as part of your template. In this page, you can view the auto-generated schemas, datasets, identity namespaces, and dataflows associated with your source connection. It can take up to five minutes to generate all assets. If you choose to leave the page, you will get a notification to return once the assets are completed. You can review the assets once they are generated and make additional configurations to your dataflow at any time.

By default, auto-generated dataflows are set to a draft state to allow further customization on configurations, such as mapping rules or scheduled frequencies. Select the ellipses (...) beside the dataflow name and then select **Preview mappings** to see the mapping sets created for your draft dataflow.

A preview page appears allowing you to inspect the mapping relationship between your source data fields and your target schema fields. Once you have viewed your dataflow’s mappings. Select **Got it.**

You can update your dataflows at any time after execution. Select the ellipses (...) beside the dataflow name and then select **Update dataflow**. You are taken to the sources workflow page where you can update your dataflow details, including settings for partial ingestion, error diagnostics, and alert notifications, as well as your dataflow’s mapping.

You can use the schema editor view to make updates to your auto-generated schema. Visit the guide on [using the schema editor](/en/docs/experience-platform/xdm/tutorials/create-schema-ui) for more information.

TIP
You can access your draft dataflow through the Dataflows catalog page in the sources workspace. Select
Dataflows
from the top header and then select the dataflow that you want to update from the list.
### Publish your dataflow

Begin the publishing process by going through the sources workflow. After you select Update dataflow, you are taken to the *Add data* step of the workflow. Select **Next** to proceed.

Next, confirm your dataflow details and configure settings for error diagnostics, partial ingestion, and alert notifications. When finished, select **Next**.

NOTE
You can select
Save as draft
at any point to stop and save the changes you have made to your dataflow.
The mapping step appears. During this step, you can reconfigure the mapping configurations of your dataflow. For a comprehensive guide on the data prep functions used for mapping, visit the [data prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Finally, review the details of your dataflow and then select **Save & ingest** to publish your draft.

## Next steps

By following this tutorial, you have now created dataflows, as well as assets like schemas, datasets, and identity namespaces using templates. For general information on sources, visit the [sources overview](/en/docs/experience-platform/sources/home).

## Alerts and notifications alerts-and-notifications

Templates are supported by Adobe Experience Platform Alerts and you can use the notifications panel to receive updates on the status of your assets and also to navigate back to the review page.

Select the notification icon the top header of Experience Platform UI and then select the status alert to see the assets that you want to review.

You can update the alert settings of your templates to receive both email and in-Experience Platform notifications on the status of your dataflows. For more information on configuring alerts, read the guide on [how to subscribe to alerts for sources dataflows](/en/docs/experience-platform/sources/ui-tutorials/alerts).

recommendation-more-help
