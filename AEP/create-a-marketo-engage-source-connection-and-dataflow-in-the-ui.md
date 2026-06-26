---
title: "Create a Marketo Engage source connection and dataflow in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/create/adobe-applications/marketo"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-05-29T16:56:22.069300+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Create a Marketo Engage source connection and dataflow in the UI

Last update: May 23, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

IMPORTANT
Before creating a Marketo Engage source connection and a dataflow, you must first ensure that you have
mapped your Adobe Organization ID
in Marketo. Furthermore, you must also ensure that you have completed
auto-populating your Marketo B2B namespaces and schemas
prior to creating a source connection and a dataflow.
This tutorial provides steps for creating a Marketo Engage (hereinafter referred to as “Marketo”) source connector in the UI to bring B2B data into Adobe Experience Platform.

## Get started

This tutorial requires a working understanding of the following components of Adobe Experience Platform:

- [B2B namespaces and schema auto-generation utility](/en/docs/experience-platform/sources/connectors/adobe-applications/marketo/marketo-namespaces): The B2B namespaces and schema auto-generation utility allows you to use Postman to auto-generate values for your B2B namespaces and schemas. You must complete your B2B namespaces and schemas first, before creating a Marketo source connection and dataflow.
- [Sources](/en/docs/experience-platform/sources/home): Experience Platform allows data to be ingested from various sources while providing you with the ability to structure, label, and enhance incoming data using Experience Platform services.
- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data. Create and edit schemas in the UI : Learn how to create and edit schemas in the UI.
- [Identity namespaces](/en/docs/experience-platform/identity/features/namespaces): Identity namespaces are a component of Identity Service that serve as indicators of the context to which an identity relates. A fully qualified identity includes an ID value and a namespace.
- [Real-Time Customer Profile](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Sandboxes](/en/docs/experience-platform/sandbox/home): Experience Platform provides virtual sandboxes which partition a single Experience Platform instance into separate virtual environments to help develop and evolve digital experience applications.

### Gather required credentials

In order to access your Marketo account on Experience Platform, you must provide the following values:

Credential
Description
munchkinId
The Munchkin ID is the unique identifier for a specific Marketo instance.
clientId
The unique client ID of your Marketo instance.
clientSecret
The unique client secret of your Marketo instance.
For more information on acquiring these values, refer to the [Marketo authentication guide](/en/docs/experience-platform/sources/connectors/adobe-applications/marketo/marketo-auth).

Once you have gathered your required credentials, you can follow the steps in the next section.

## Connect your Marketo account

In the Experience Platform UI, select **Sources** from the left navigation to access the Sources workspace. You can select the appropriate category from the catalog on the left-hand side of your screen. Alternatively, you can find the specific source you wish to work with using the search option.

Under the *Adobe applications* category, select **Marketo Engage**, and then select **Add data**.

TIP
Sources in the sources catalog display the
Set up
option when a given source does not yet have an authenticated account. Once an authenticated account exists, this option changes to
Add data
.
The **Connect Marketo Engage account** page appears. On this page, you can either use a new account or access an existing account.

Create a new account
To create a new account, select **New account** and provide a name, an optional description, and your credentials.

When finished, select **Connect to source** and then allow some time for the new connection to establish.

Use an existing account
To use an existing account, select **Existing account** and then select the account that you want to use from the existing account catalog.

Select **Next** to proceed.

## Select a dataset

After creating your Marketo account, the next step provides an interface for you to explore Marketo datasets.

The left half of the interface is a directory browser, displaying the 10 Marketo datasets. A fully-functioning Marketo source connection requires the ingestion of the nine different datasets. If you are also using the Marketo account-based marketing (ABM) feature, then you must also create a 10th dataflow to ingest the Named Accounts dataset.

NOTE
For the purposes of brevity, the following tutorial uses Opportunities as an example, but the steps outlined below apply to any of the 10 Marketo datasets.
Select the dataset that you want to ingest. This updates the interface to display a preview of your dataset. When finished, select **Next**.

## Provide dataset and dataflow details provide-dataset-and-dataflow-details

Next, you must provide information on your dataset and your dataflow.

### Dataset details dataset-details

A dataset is a storage and management construct for a collection of data, typically a table, that contains a schema (columns) and fields (rows). Data that is successfully ingested into Experience Platform is stored within the data lake as datasets. During this step, you can create a new dataset or use an existing dataset.

Use a new dataset
To use a new dataset, select **New dataset** and then provide a name, and an optional description for your dataset. You must also select an Experience Data Model (XDM) schema that your dataset adheres to.

Use an existing dataset
If you already have an existing dataset, select **Existing dataset** and then use the **Advanced search** option to view a window of all datasets in your organization, including their respective details, such as whether they are enabled for ingestion to Real-Time Customer Profile or not.

### Dataflow configurations dataflow-configurations

IMPORTANT
The Marketo source uses batch ingestion to ingest all historical records and uses streaming ingestion for real-time updates. This allows the source to continue streaming while ingesting any erroneous records. Enable the
Partial ingestion
toggle and then set the Error threshold % to maximum to prevent the dataflow from failing.
If your dataset is enabled for Real-Time Customer Profile, then during this step, you can toggle **Profile dataset** to enable your data for Profile-ingestion. You can also use this step to enable **Error diagnostics** and **Partial ingestion**.

- **Error diagnostics**: Select **Error diagnostics** to instruct the source to produce error diagnostics that you can later reference when monitoring your dataset activity and dataflow status.
- **Partial ingestion**: [Partial batch ingestion](/en/docs/experience-platform/ingestion/batch/partial) is the ability to ingest data containing errors, up to a certain configurable threshold. This feature allows you to successfully ingest all of your accurate data into Experience Platform, while all of your incorrect data is batched separately with information on why it is invalid.

During this step, you can enable **Sample dataflow** to limit data ingestion and avoid additional costs that come with ingesting all historical data, including Person identities.

**Quick guide on using sample dataflow**

Sample dataflow is a configuration that you can set for your Marketo dataflow to limit your ingestion rate and then try out Experience Platform features without having to ingest large amounts of data.

- Enable sample dataflow to limit historical data by ingesting up to 100k (from the largest record ID) records or up to the last 10 days of activity during the backfill job.
- When using the sample dataflow configuration for all B2B entities, you must consider that it is possible that some related records may be missing because the entire history of the source data does not get ingested.

style
shade-box
Additionally, if you are ingesting data from the companies dataset, you can enable **Exclude unclaimed accounts** to exclude unclaimed accounts from ingestion.

When individuals fill out a form, Marketo creates a phantom account record based on the Company Name that contains no other data. For new dataflows, the toggle to exclude unclaimed accounts is enabled by default. For existing dataflows, you can enable or disable the feature, with changes applying to newly ingested data and not existing data.

## Map your Marketo dataset source fields to target XDM fields

The Mapping step appears, providing you with an interface to map the source fields from your source schema to their appropriate target XDM fields in the target schema.

Each Marketo dataset has its own specific mapping rules to follow. See the following for more information on how to map Marketo datasets to XDM:

- [Activities](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#activities)
- [Programs](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#programs)
- [Program memberships](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#program-memberships)
- [Companies](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#companies)
- [Static lists](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#static-lists)
- [Static list memberships](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#static-list-memberships)
- [Named Accounts](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#named-accounts)
- [Opportunities](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#opportunities)
- [Opportunity contact roles](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#opportunity-contact-roles)
- [Persons](/en/docs/experience-platform/sources/connectors/adobe-applications/mapping/marketo#persons)

Based on your needs, you can choose to map fields directly, or use data prep functions to transform source data to derive computed or calculated values. For comprehensive steps on using the mapping interface, see the [Data Prep UI guide](/en/docs/experience-platform/data-prep/ui/mapping).

Once your mapping sets are ready, select **Next** and allow for a few moments for the new dataflow to be created.

## Review your dataflow

The **Review** step appears, allowing you to review your new dataflow before it is created. Details are grouped within the following categories:

- **Connection**: Shows the source type, the relevant path of the chosen source entity, and the amount of columns within that source entity.
- **Assign dataset & map fields**: Shows which dataset the source data is being ingested into, including the schema that the dataset adheres to.

Once you have reviewed your dataflow, select **Save & ingest** and allow some time for the dataflow to be created.

## Monitor your dataflow

Once your dataflow has been created, you can monitor the data that is being ingested through it to see information on ingestion rates, success, and errors. For more information on how to monitor dataflows, see the tutorial on [monitoring dataflows in the UI](/en/docs/experience-platform/dataflows/ui/monitor-sources).

## Delete your attributes

Custom attributes in datasets cannot be retroactively hidden or removed. If you want to hide or remove a custom attribute from an existing dataset, then you must create a new dataset without this custom attribute, a new XDM schema, and configure a new dataflow for the new dataset that you create. You must also disable or delete the original dataflow that consists of the dataset with the custom attribute you want to hide or remove.

## Delete your dataflow

You can delete dataflows that are no longer necessary or were incorrectly created using the **Delete** function available in the Dataflows workspace. For more information on how to delete dataflows, see the tutorial on [deleting dataflows in the UI](/en/docs/experience-platform/sources/ui-tutorials/delete).

## Next steps

By following this tutorial, you have successfully created a dataflow to ingest B2B data from your Marketo Engage source to Experience Platform.

## Appendix appendix

The following sections provide additional guidelines that you may follow when using the Marketo source.

### Error messages in the UI error-messages

The following error messages are displayed in the UI when Experience Platform detects issues with your setup:

#### Munchkin ID is not mapped to the appropriate organization

Authentication will be denied if your Munchkin ID is not mapped to the Experience Platform organization that you are using. Configure the mapping between your Munchkin ID and your organization using the [Marketo interface](https://app-sjint.marketo.com/#MM0A1).

#### Primary identity is missing

A dataflow will fail to save and ingest if a primary identity is missing. Ensure that [a primary identity exists within your XDM schema](/en/docs/experience-platform/xdm/tutorials/create-schema-ui), before attempting to configure a dataflow.

recommendation-more-help
