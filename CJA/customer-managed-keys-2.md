---
title: "Customer-managed keys"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-privacy/cmk"
category: "other"
topic: "analytics-platform/using/cja-privacy/cmk"
created_at: "2026-06-23T20:42:33.768666+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Customer-managed keys

Last update: June 5, 2026
- Topics:
- [Data governance](#)

CREATED FOR:

- Admin

Adobe Customer Journey Analytics provides the option for [Healthcare Shield](https://www.adobe.com/trust/compliance/hipaa-ready.html) and Privacy & Security Shield customers to use customer-managed keys (CMK) for Customer Journey Analytics data. Note that this process is separate from the [Adobe Experience Platform CMK setup](/en/docs/experience-platform/landing/governance-privacy-security/customer-managed-keys/overview). Customer-managed keys are only available for organizations that have purchased the [Healthcare Shield or Privacy & Security Shield](/en/docs/events/customer-data-management-voices-recordings/governance/healthcare-shield) add-on offering.

## Set up customer-managed keys for Customer Journey Analytics on Azure

Follow these steps to set up CMK for Customer Journey Analytics running on Azure:

- Ensure that you are entitled to Adobe Customer Journey Analytics CMK and that your organization uses Adobe Experience Platform running on Azure. You can check these entitlements by contacting your Adobe Account team.
- Ensure that, in Azure, you are an administrator with a privileged role such as Application Administrator, Cloud Application Administrator, or Global Administrator. See Microsoft Entra built-in roles for more information.
- Create a new Azure Key Vault to be used only with Customer Journey Analytics. See Microsoft Azure Key Vault documentation for more information.
- Grant the Adobe Azure App access to your key in the key vault. You can do so by using either of the following methods: Grant permissions via authorization consent via the following URL: https://login.microsoftonline.com/common/oauth2/authorize?response_type=code&client_id=251e3919-1940-4296-bb8b-6b9a5e8a4805&redirect_uri=https://experience.adobe.com&scope=user.read Follow the instructions in Configure customer-managed keys for an existing account . The Adobe Application ID is: 251e3919-1940-4296-bb8b-6b9a5e8a4805
- Create an Adobe Customer Care ticket requesting CMK setup. Include the Azure URI in your ticket. The URI can be found in the Key Identifier field of your Azure key:
- Adobe Customer Care confirms the completion of the CMK application on your Customer Journey Analytics data.

All data used by Platform is encrypted in transit and at rest to keep your data secure, with or without customer-managed keys. For information on Adobe Experience Platform encryption, see [Data encryption in Adobe Experience Platform](/en/docs/experience-platform/landing/governance-privacy-security/encryption).

## Set up customer-managed keys for Customer Journey Analytics on Amazon Web Services

AVAILABILITY
This section applies to implementations of Experience Platform running on Amazon Web Services (AWS). Experience Platform running on AWS is currently available to a limited number of customers. To learn more about the supported Experience Platform infrastructure, see the
Experience Platform multi-cloud overview
.
If your organization uses Adobe Experience Platform running on Amazon Web Services, CMK is already configured for you. No additional setup is needed.

recommendation-more-help
