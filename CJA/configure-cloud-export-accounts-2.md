---
title: "Configure cloud export accounts"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/exports/cloud-export-accounts"
category: "other"
topic: "analytics-platform/using/cja-components/exports"
created_at: "2026-06-23T20:44:16.438480+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure cloud export accounts

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User
- Admin

Before you can export Customer Journey Analytics reports to a cloud destination (either from Analysis Workspace, as described in [Export Customer Journey Analytics reports to the cloud](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud) or from Report Builder, as described in [Export reports from Report Builder](/en/docs/analytics-platform/using/cja-reportbuilder/report-builder-export)), you need to add and configure the destination where you want the data to be sent.

This process consists of adding and configuring the account (such as Amazon S3, Google Cloud Platform, and so forth) as described in this article, and then adding and configuring the location within that account (such as a folder within the account) as described in [Configure cloud export locations](/en/docs/analytics-platform/using/cja-components/exports/cloud-export-locations).

For information about how to manage existing accounts, including viewing, editing, and deleting accounts, see [Manage cloud export locations and accounts](/en/docs/analytics-platform/using/cja-components/exports/manage-export-locations).

## Begin creating a cloud export account

- Make sure you meet the minimum requirements for exporting reports to the cloud.
- In Customer Journey Analytics, select Components > Exports .
- On the Exports page, select the Location accounts tab.
- Select Add account . The Add account dialog displays.
- In the Location account name field, specify a name for the location account. This name appears when creating a location.
- In the Location account description field, provide a short description of the account to help differentiate it from other accounts of the same account type.
- Enable the option to Make account available to all users in your organization if you want to allow other users in your organization to use the account. Consider the following when sharing accounts: Accounts that you share cannot be unshared. Shared accounts can be edited only by the owner of the account. Anyone can create a location for the shared account.
- In the Account type field, select the type of cloud account you are exporting to. Available account types are Amazon S3 Role ARN, Google Cloud Platform, Azure SAS, Azure RBAC, Snowflake, and AEP Data Landing Zone.
- Continue with the section below that corresponds to the Account type you selected. AEP Data Landing Zone Amazon S3 Role ARN Google Cloud Platform Azure SAS Azure RBAC Snowflake

### AEP Data Landing Zone

IMPORTANT
Consider the following when using AEP Data Landing Zone for your export account:
- When exporting Customer Journey Analytics reports to Adobe Experience Platform Data Landing Zone, make sure that you download the data within 7 days, then delete it from AEP Data Landing Zone. After 7 days, the data is automatically deleted from AEP Data Landing Zone.
- AEP Data Landing Zone uses either Azure or AWS storage. If your organization is using an IMS org configured to use Azure, then AEP Data Landing Zone uses Azure. If the login company is configured to use AWS, then AEP Data Landing Zone uses AWS.

- Begin creating a cloud export account in either of the following ways: From the Exports page as described above, in Begin creating a cloud export account When exporting full tables from Analysis Workspace
- After you select AEP Data Landing Zone in the Account type field, select Save . Either of the following dialogs displays, depending on whether your AEP Data Landing Zone is configured to use Azure or AWS storage: Azure storage: The Export account created dialog displays. AWS storage: note availability AVAILABILITY This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the Experience Platform multi-cloud overview . The Account created dialog displays.
- (Conditional) If you are using Azure storage: Copy the contents of the SAS URI field to your clipboard. You will use this SAS URI to access the exported Analysis Workspace data from AEP Data Landing Zone. If this field is empty, you need to be granted permission to access Adobe Experience Platform. In Adobe Experience Platform, configure your Data Landing Zone container to use the SAS URI that you copied. note NOTE When using an AEP Data Landing Zone account that is based on Azure, the easiest way to access reports that you export to AEP Data Landing Zone is by using the Azure Storage Explorer. The following steps use this method. If you haven’t already, download the Microsoft Azure Storage Explorer . In the Adobe Experience Platform documentation, follow the steps described in Connect your Data Landing Zone container to Azure Storage Explorer . You can skip the tasks described in the sections Retrieve the credentials for your Data Landing Zone and Update Data Landing Zone credentials , because the URI that you copied contains these credentials. When following the Adobe Experience Platform documentation and you come to the Blob container SAS URL field, paste the SAS URI that you copied in an earlier step. note NOTE You need to perform this action every 7 days, because the SAS URI expires 7 days after it is created. You can create a script to automate this process. Select Next > Connect . In Customer Journey Analytics, in the Export account created dialog, select OK .
- (Conditional) If you are using AWS storage: Copy the contents of the following fields to your clipboard (You will use this information to access the data that is exported from Analysis Workspace from the AEP Data Landing Zone): Access key id Secret access key Session token Bucket name DLZ folder Select OK .
- Continue with Configure cloud export locations .

### Amazon S3 Role ARN

- Begin creating a cloud export account in either of the following ways: From the Exports page as described above, in Begin creating a cloud export account When exporting full tables from Analysis Workspace
- In the Account properties section of the Add account dialog box, specify the following information: table 0-row-2 1-row-2 layout-auto Field Function Role ARN You must provide a Role ARN (Amazon Resource Name) that Adobe can use to gain access to the Amazon S3 account. To do this, you create an IAM permission policy for the source account, attach the policy to a user, and then create a role for the destination account. For specific information, see this AWS documentation .
- Select Save . The Export account created dialog displays.
- Copy the contents of the User ARN field to your clipboard. The User ARN (Amazon Resource Name) is provided by Adobe. You must attach this user to the policy you created in Amazon S3 Role ARN.
- Select OK .
- Continue with Configure cloud export locations .

### Google Cloud Platform

- Begin creating a cloud export account in either of the following ways: From the Exports page as described above, in Begin creating a cloud export account When exporting full tables from Analysis Workspace
- In the Account properties section of the Add account dialog box, specify the following information: table 0-row-2 1-row-2 layout-auto Field Function Project ID Your Google Cloud project ID that you copy from your Google Cloud account. See the Google Cloud documentation about getting a project ID .
- Select Save . The Export account created dialog displays.
- Copy the contents of the Principal field to your clipboard, then ensure that you grant permission to the Principal to upload files to this bucket in Google Cloud Platform.
- Select OK .
- Continue with Configure cloud export locations .

### Azure SAS

- Begin creating a cloud export account in either of the following ways: From the Exports page as described above, in Begin creating a cloud export account When exporting full tables from Analysis Workspace
- In the Account properties section of the Add account dialog box, specify the following information: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 layout-auto Field Function Application ID Copy this ID from the Azure application that you created. In Microsoft Azure, this information is located on the Overview tab within your application. For more information, see the Microsoft Azure documentation about how to register an application with the Microsoft identity platform . Tenant ID Copy this ID from the Azure application that you created. In Microsoft Azure, this information is located on the Overview tab within your application. For more information, see the Microsoft Azure documentation about how to register an application with the Microsoft identity platform . Key vault URI The path to the SAS URI in Azure Key Vault. To configure Azure SAS, you need to store an SAS URI as a secret using Azure Key Vault. For information, see the Microsoft Azure documentation about how to set and retrieve a secret from Azure Key Vault . After the key vault URI is created: Add an access policy on the Key Vault in order to grant permission to the Azure application that you created. For information, see the Microsoft Azure documentation about how to assign a Key Vault access policy . Or If you want to grant an access role directly without creating an access policy, see the Microsoft Azure documentation about how to assign Azure roles using Azure portal . This adds the role assignment for the application ID to access the key vault URI. Make sure the Application ID has been granted the Key Vault Certificate User built-in role in order to access the key vault URI. For more information, see Azure built-in roles . Key vault secret name The secret name you created when adding the secret to Azure Key Vault. In Microsoft Azure, this information is located in the Key Vault you created, on the Key Vault settings pages. For information, see the Microsoft Azure documentation about how to set and retrieve a secret from Azure Key Vault . Location account secret Copy the secret from the Azure application that you created. In Microsoft Azure, this information is located on the Certificates & secrets tab within your application. For more information, see the Microsoft Azure documentation about how to register an application with the Microsoft identity platform .
- Select Save . The Export account created dialog displays.
- If you haven’t already, ensure that you grant permissions to the bucket in Azure SAS.
- Select OK .
- Continue with Configure cloud export locations .

### Azure RBAC

- Begin creating a cloud export account in either of the following ways: From the Exports page as described above, in Begin creating a cloud export account When exporting full tables from Analysis Workspace
- In the Account properties section of the Add account dialog box, specify the following information: table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto Field Function Application ID Copy this ID from the Azure application that you created. In Microsoft Azure, this information is located on the Overview tab within your application. For more information, see the Microsoft Azure documentation about how to register an application with the Microsoft identity platform . Tenant ID Copy this ID from the Azure application that you created. In Microsoft Azure, this information is located on the Overview tab within your application. For more information, see the Microsoft Azure documentation about how to register an application with the Microsoft identity platform . Location account secret Copy the secret from the Azure application that you created. In Microsoft Azure, this information is located on the Certificates & secrets tab within your application. For more information, see the Microsoft Azure documentation about how to register an application with the Microsoft identity platform .
- Select Save . The Export account created dialog displays.
- If you haven’t already, ensure that you grant permissions to the container in Azure RBAC.
- Select OK .
- Continue with Configure cloud export locations .

### Snowflake

- Begin creating a cloud export account in either of the following ways: From the Exports page as described above, in Begin creating a cloud export account When exporting full tables from Analysis Workspace
- In the Account properties section of the Add account dialog box, specify the following information: table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto Field Function Account identifier Uniquely identifies a Snowflake account within your organization, as well as throughout the global network of Snowflake-supported cloud platforms and cloud regions. You need to get the account identifier from your Snowflake account, then paste the information here. To learn where to get this information, see the Account Identifiers page in the Snowflake documentation . User The login name of the user that will be used for the connection. We recommend creating a new user that will be used specifically for Adobe. Specify the name here, then create a user in Snowflake with the same name. You can create a user in Snowflake using the CREATE USER command. For more information, see the User, Role, & Privilege Commands . Role The role that will be assigned to the user. We recommend creating a new role that will be used specifically for Adobe. Specify the role here, then create a role in Snowflake with the same name and grant the role to the user. You can create a role in Snowflake using the CREATE ROLE command. For more information, see the User, Role, & Privilege Commands .
- Select Save . The Export account created dialog displays.
- Copy the contents of the Public key field to your clipboard. The Public key is provided by Adobe. Use the public key in Snowflake to connect to your Snowflake account. You must associate the user that you created with this public key. For example, in Snowflake, specify the following command: code language-none CREATE USER <your_adobe_user> RSA_PUBLIC_KEY = '<your_public_key>'; For more information, see the Key Pair Authentication & Key Pair Rotation page in the Snowflake documentation .
- Select OK .
- Continue with Configure cloud export locations .

recommendation-more-help
