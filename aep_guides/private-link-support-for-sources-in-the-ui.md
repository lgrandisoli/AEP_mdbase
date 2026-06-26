---
title: "Private Link Support for Sources in the UI"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/sources/ui-tutorials/private-link"
category: "tutorials"
topic: "experience-platform/source-connectors-guide"
created_at: "2026-06-26T17:33:04.071862+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Source Connectors Guide

# Private Link Support for Sources in the UI

Last update: June 18, 2026
- Topics:
- [Sources](#)

CREATED FOR:

- Developer

AVAILABILITY
This feature is supported by the following sources:
- [Azure Blob Storage](/en/docs/experience-platform/sources/connectors/cloud-storage/blob)
- [ADLS Gen2](/en/docs/experience-platform/sources/connectors/cloud-storage/adls-gen2)
- [Azure File Storage](/en/docs/experience-platform/sources/connectors/cloud-storage/azure-file-storage)

Private Link Support is currently only available for organizations that have purchased Adobe Healthcare Shield or Adobe Privacy & Security Shield.
Private Link Support is not available when using the VA6 region and connecting to
Adobe Experience Platform on AWS
.
You can use the Private Links feature to create private endpoints for your Adobe Experience Platform sources to connect to. Securely connect your sources to a virtual network using private IP addresses, eliminating the need for public IPs and reduce your attack surface. Simplify your network setup by removing the need for complex firewall or Network Address Translation configurations, while ensuring data traffic only reaches approved services.

Read this guide to learn how you can use the sources workspace in the Experience Platform UI to create and use a private endpoint.

## License usage entitlement for private link support

The license usage entitlement metrics for private link support in sources is as follows:

- Customers are entitled to up to 2 TB per year of data transfer through supported sources (Azure Blob Storage, ADLS Gen2, and Azure File Storage), across all sandboxes and organizations.
- Each organization can have a maximum of 10 endpoints for all production sandboxes.
- Each organization can have a maximum of 1 endpoint for all development sandboxes.

style
shade-box
## Create a private endpoint

To get started with Private Links, navigate to the *Sources* catalog of the Experience Platform UI and select **Private endpoints** from the menu of tabs in the sources workspace.

Use the interface to view information about existing private endpoints, such as their ID, associated source, and current status. To create a new private endpoint, select **Create private endpoint**.

Next, choose your desired source, and then enter values for the following properties:

Property
Description
name
The name of your private endpoint.
subscriptionId
The ID associated with your Azure subscription. For more information, read the Azure guide on
retrieving your subscription and tenant IDs from the Azure Portal
.
resourceGroupName
The name of your resource group on Azure. A resource group contains related resources for an Azure solution. For more information, read the Azure guide on
managing resource groups
.
resourceGroup
The name of your resource. In Azure, a resource refers to instances like virtual machines, web apps, and databases. For more information, read the Azure guide on
understanding the Azure resource manager
.
When finished, select **Submit**.

### Approve a private endpoint

A newly created endpoint remains in a pending state until it is approved by an administrator.

To approve a private endpoint request for the Azure Blob and Azure Data Lake Gen2 sources, log in to the Azure Portal. In the left navigation, select **Data storage**, then go to the **Security + networking** tab and choose **Networking**. Next, select **Private endpoints** to see a list of private endpoints associated with your account and their current connection states. To approve a pending request, select the desired endpoint and click **Approve**.

## Create an account with a private endpoint

Navigate to the sources catalog and select a source that supports private endpoints. Next, create a new account with your source and during account authentication, select the **Private endpoint** toggle. Provide your source’s authentication credentials and then select **Connect to source** Allow a few minutes for the connection to be established.

NOTE
If the Private endpoint option is enabled, Experience Platform checks whether an approved private endpoint exists for the selected source. If no approved endpoint is found, you will not be able to establish a connection.
Next, navigate to the Existing account interface of your source. Use this interface to view a list of your existing accounts and their corresponding statuses. You can select the filter icon to display only the accounts that have been enabled to connect with a private endpoint.

Select the account you want to use, then enable **Interactive Authoring**. This toggle activates Interactive Authoring, an Azure feature that allows you to test connections, browse folder lists, and preview data. Enabling Interactive Authoring is required for private endpoint connections. Note that you cannot manually turn off this toggle; it automatically disables after 60 minutes.

Interactive Authoring takes a few minutes to enable. Once the setting is enabled, select **Next** to proceed to the next step and select the data that you want to ingest.

## Next steps

Now that you have successfully created a private endpoint, you can create source connections and dataflows, and ingest data using private endpoints. Read the following guides for information on how to create dataflows in the UI:

- [Create a dataflow for a cloud storage source](/en/docs/experience-platform/sources/ui-tutorials/dataflow/cloud-storage)
- [Create a dataflow for a database source](/en/docs/experience-platform/sources/ui-tutorials/dataflow/databases)

recommendation-more-help
