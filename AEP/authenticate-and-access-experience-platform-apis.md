---
title: "Authenticate and access Experience Platform APIs"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication"
category: "reference"
topic: "experience-platform/experience-platform-overview"
created_at: "2026-05-29T16:54:46.915704+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Experience Platform overview

# Authenticate and access Experience Platform APIs

Last update: May 23, 2026
- Topics:
- [API](#)

CREATED FOR:

- Developer

This document provides a step-by-step tutorial for gaining access to an Adobe Experience Platform developer account in order to make calls to Experience Platform APIs. At the end of this tutorial, you will have generated or collected the following credentials that are required as headers in all Experience Platform API calls:

- {ACCESS_TOKEN}
- {API_KEY}
- {ORG_ID}

TIP
In addition to the three credentials above, many Experience Platform APIs also require a valid
{SANDBOX_NAME}
to be provided as a header. See the
sandboxes overview
for more information about sandboxes and the
sandbox management endpoint
documentation for information about listing the sandboxes available to your organization.
To maintain the security of your applications and users, all requests to Experience Platform APIs must be authenticated and authorized using standards such as OAuth.

This tutorial covers how to gather the required credentials to authenticate Experience Platform API calls, as outlined in the flowchart below. You can gather most of the required credentials in the initial one-time setup. The access token, however, must be refreshed every 24-hours.

## Prerequisites prerequisites

In order to successfully make calls to Experience Platform APIs, you must have the following:

- An organization with access to Adobe Experience Platform.
- An Admin Console administrator that is able to add you as a developer and a user for a product profile.
- An Experience Platform system administrator who can grant you the necessary attribute based access controls to perform read or write operations on different parts of Experience Platform through APIs.

You must also have an Adobe ID to complete this tutorial. If you do not have an Adobe ID, you can create one using the following steps:

- Go to [Adobe Developer Console](https://console.adobe.io).
- Select **Create a new account**.
- Complete the sign-up process.

## Gain developer and user access for Experience Platform gain-developer-user-access

Before creating integrations on Adobe Developer Console, your account must have developer and user permissions for an Experience Platform product profile in Adobe Admin Console.

### Gain developer access gain-developer-access

Contact an Admin Console administrator in your organization to add you as a developer to an Experience Platform product profile. See the Admin Console documentation for specific instructions on how to [manage developer access for product profiles](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/manage-developers.ug.html).

Once you are assigned as a developer, you can start creating integrations in [Adobe Developer Console](https://www.adobe.com/go/devs_console_ui). These integrations are a pipeline from external apps and services to Adobe APIs.

### Gain user access gain-user-access

Your Admin Console administrator must also add you as a user to the same product profile. With user access, you can see in the UI the outcome of the API operations that you perform.

See the guide on [managing user groups in Admin Console](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/user-groups.ug.html) for more information.

## Generate an API key (client ID) and organization ID generate-credentials

NOTE
If you are following this document from the
Privacy Service API guide
, you can now return to that guide to generate the access credentials unique to Privacy Service.
After you have been given developer and user access to Experience Platform through Admin Console, the next step is to generate your {ORG_ID} and {API_KEY} credentials in Adobe Developer Console. These credentials only need to be generated once and can be reused in future Experience Platform API calls.

TIP
Instead of going to Developer Console, you can get all the authentication credentials that you need to work with Experience Platform APIs directly from the API reference documentation pages.
Read more
about the functionality.
### Add Experience Platform to a project add-platform-to-project

Go to [Adobe Developer Console](https://www.adobe.com/go/devs_console_ui) and sign in with your Adobe ID. Next, follow the steps outlined in the tutorial on [creating an empty project](https://developer.adobe.com/developer-console/docs/guides/projects/projects-empty/) in the Adobe Developer Console documentation.

Once you have created a new project, select **Add API** on the **Project Overview** screen.

TIP
If you are provisioned for several organizations, use the organization selector in the upper right corner of the interface to make sure that you are in the organization you need.
The **Add an API** screen appears. Select the product icon for **Adobe Experience Platform**, then choose **Experience Platform API** before selecting **Next**.

TIP
Select the
View docs
option to navigate in a separate browser window to the complete
Experience Platform API reference documentation
.
### Select the OAuth Server-to-Server authentication type select-oauth-server-to-server

Next, select the **OAuth Server-to-Server** authentication type to generate access tokens and access the Experience Platform API. Give your credential a meaningful name in the **Credential name** text field before selecting **Next**.

IMPORTANT
The
OAuth Server-to-Server
method is the only token generation method supported moving forward. The formerly supported
Service Account (JWT)
method is deprecated and cannot be selected for new integrations. While existing integrations using the JWT authentication method will continue to work until June 30th, 2025, Adobe strongly recommends that you migrate existing integrations to the new OAuth Server-to-Server method before that date. Get more information in the section [Deprecated]{class="badge negative"}
Generate a JSON Web Token (JWT)
.
### Select the product profiles for your integration select-product-profiles

In the **Configure API** screen, select **AEP-Default-All-Users** along with any additional product profiles you wish to gain access to.

IMPORTANT
To get access to certain features in Experience Platform, you also need a system administrator to grant you the necessary attribute-based access control permissions. Read more in the section
Get the necessary attribute-based access control permissions
.
Select **Save configured API** when you are ready.

A walkthrough of the steps described above to set up an integration with the Experience Platform API is also available in the video tutorial below:

https://video.tv.adobe.com/v/28832/?learn=on
https://video.tv.adobe.com/vc/28832/eng.json
### Gather credentials gather-credentials

Once the API has been added to the project, the **OAuth Server-to-Server** page for the project displays the following credentials that are required in all calls to Experience Platform APIs:

- {API_KEY} (Client ID)
- {ORG_ID} (Organization ID)

## Generate an access token generate-access-token

The next step is to generate an {ACCESS_TOKEN} credential for use in Experience Platform API calls. Unlike the values for {API_KEY} and {ORG_ID}, a new token must be generated every 24 hours to continue using Experience Platform APIs. Select **Generate access token** which produces your access token, as shown below.

TIP
You can also use a Postman environment and collection to generate access tokens. For more information, read the section about
using Postman to authenticate and test API calls
.
## Create and retrieve authentication credentials directly in the API reference documentation get-credentials-functionality

Starting with the November 2024 release of Experience Platform, you can get credentials to use the Experience Platform APIs directly from the API reference pages, without needing to go to Developer Console. View the example below from the [Flow Service API - Destinations page](https://developer.adobe.com/experience-platform-apis/references/destinations/).

To get credentials to call Experience Platform APIs, navigate to any Experience Platform API reference page and select **Sign in** at the top of the page. Sign in with your **Personal Account** or **Company or School Account**.

After signing in, select **Create new credential** to create a new set of credentials to access Experience Platform APIs.

Next, use the dropdown selector to open the credentials window, generate an access token, and get your API key and organization ID. Copy the credentials into the **Try it** blocks on the API reference pages to start working with Experience Platform APIs.

TIP
The top-of-page credentials block remains displayed as you navigate between different endpoint pages in the Experience Platform API reference documentation.
## [Deprecated]{class="badge negative"} Generate a JSON Web Token (JWT) jwt

WARNING
The JWT method to generate access tokens has been deprecated. All new integrations must be created using the
OAuth Server-to-Server authentication method
. Adobe also requires that you migrate your existing integrations to the OAuth method by June 30th, 2025 for your integrations to continue to work. Read the following important documentation:
- [Migration guide for your applications from JWT to OAuth](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/)
- [Implementation guide for new and old applications with OAuth](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation/)
- [Advantages of using the OAuth Server-to-Server credentials method](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/migration/#why-oauth-server-to-server-credentials)

View deprecated information
The next step is to generate a JSON Web Token (JWT) based on your account credentials. This value is used to generate your {ACCESS_TOKEN} credential for use in Experience Platform API calls, which must be regenerated every 24 hours.

| note important |
| --- |
| IMPORTANT |
| For the purposes of this tutorial, the steps below outline how to generate a JWT within Developer Console. However, this generation method should only be used for testing and evaluation purposes. |
| For regular use, the JWT must be generated automatically. For more information on how to programmatically generate JWTs, see the [service account authentication guide](https://www.adobe.io/developer-console/docs/guides/authentication/JWT/) on Adobe Developer. |

Select **Service Account (JWT)** in the left navigation, then select **Generate JWT**.

In the textbox provided under **Generate custom JWT**, paste the contents of the private key that you previously generated when adding the Experience Platform API to your service account. Then, select **Generate Token**.

The page updates to show the generated JWT, along with a sample cURL command that allows you to generate an access token. For the purposes of this tutorial, select **Copy** next to **Generated JWT** to copy the token to your clipboard.

**Generate an access token**

Once you have generated a JWT, you can use it in an API call to generate your {ACCESS_TOKEN}. Unlike the values for {API_KEY} and {ORG_ID}, a new token must be generated every 24 hours to continue using Experience Platform APIs.

**Request**

The following request generates a new {ACCESS_TOKEN} based on the credentials provided in the payload. This endpoint only accepts form data as its payload, and therefore it must be given a Content-Type header of multipart/form-data.

| code language-shell |
| --- |
| curl -X POST https://ims-na1.adobelogin.com/ims/exchange/jwt \ -H 'Content-Type: multipart/form-data' \ -F 'client_id={API_KEY}' \ -F 'client_secret={SECRET}' \ -F 'jwt_token={JWT}' |

| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Property | Description |
| {API_KEY} | The {API_KEY} (Client ID) that you retrieved in a [previous step](#api-ims-secret). |
| {SECRET} | The client secret that you retrieved in a [previous step](#api-ims-secret). |
| {JWT} | The JWT that you generated in a [previous step](#jwt). |

| note |
| --- |
| NOTE |
| You can use the same API key, client secret, and JWT to generate a new access token for each session. This allows you to automate access token generation in your applications. |

**Response**

| code language-json |
| --- |
| { "token_type": "bearer", "access_token": "{ACCESS_TOKEN}", "expires_in": 86399992 } |

| table 0-row-2 1-row-2 2-row-2 3-row-2 |  |
| --- | --- |
| Property | Description |
| token_type | The type of token being returned. For access tokens, this value is always bearer. |
| access_token | The generated {ACCESS_TOKEN}. This value, prefixed with the word Bearer, is required as the Authentication header for all Experience Platform API calls. |
| expires_in | The number of milliseconds remaining until the access token expires. Once this value reaches 0, a new access token must be generated to continue using Experience Platform APIs. |

## Test access credentials test-credentials

Once you have gathered all three required credentials - access token, API key, and Organization ID - , you can try to make the following API call. This call lists all standard Experience Data Model (XDM) classes available to your organization. Import and execute the call in [Postman](#use-postman).

**Request**

```
curl -X GET https://platform.adobe.io/data/foundation/schemaregistry/global/classes \
  -H 'Accept: application/vnd.adobe.xed-id+json' \
  -H 'Authorization: Bearer {{ACCESS_TOKEN}}' \
  -H 'x-api-key: {{API_KEY}}' \
  -H 'x-gw-ims-org-id: {{ORG_ID}}'
```

**Response**

If your response is similar to the one shown below, then your credentials are valid and working. (This response has been truncated for space.)

```
{
  "results": [
    {
        "title": "XDM ExperienceEvent",
        "$id": "https://ns.adobe.com/xdm/context/experienceevent",
        "meta:altId": "_xdm.context.experienceevent",
        "version": "1"
    },
    {
        "title": "XDM Individual Profile",
        "$id": "https://ns.adobe.com/xdm/context/profile",
        "meta:altId": "_xdm.context.profile",
        "version": "1"
    }
  ]
}
```

style
shade-box
IMPORTANT
While the call above is sufficient to test your access credentials, be aware that you will not be able to access or modify several resources without having the right attribute-based access control permissions. Read more in the
Get the necessary attribute-based access control permissions
section below.
## Get the necessary attribute-based access control permissions get-abac-permissions

To access or modify several resources within Experience Platform, you must have the appropriate access control permissions. System administrators can grant you the [permissions you need](/en/docs/experience-platform/access-control/ui/permissions). Get more information in the section about [managing API credentials for a role](/en/docs/experience-platform/access-control/abac/permissions-ui/permissions#manage-api-credentials-for-role).

Detailed information about how a system administrator can grant the required permissions to access Experience Platform resources through the API is also available in the video tutorial below:

https://video.tv.adobe.com/v/28832/?learn=on&t=159
https://video.tv.adobe.com/vc/28832/eng.json
## Use Postman to authenticate and test API calls use-postman

[Postman](https://www.postman.com/) is a popular tool that allows developers to explore and test RESTful APIs. You can use Experience Platform Postman collections and environments to speed up your work with Experience Platform APIs. Read more about [using Postman in Experience Platform](/en/docs/experience-platform/landing/platform-apis/postman) and getting started with collections and environments.

Detailed information about using Postman with Experience Platform collections and environments is also available in the video tutorials below:

**Download and import a Postman environment to use with Experience Platform APIs**

https://video.tv.adobe.com/v/28832/?learn=on&t=106
https://video.tv.adobe.com/vc/28832/eng.json
**Use a Postman collection to generate access tokens**

Download the [Identity Management Service Postman collection](https://github.com/adobe/experience-platform-postman-samples/tree/master/apis/ims) and watch the video below to learn how to generate access tokens.

https://video.tv.adobe.com/v/29698/?learn=on
https://video.tv.adobe.com/vc/29698/eng.json
**Download Experience Platform API Postman collections and interact with the APIs**

https://video.tv.adobe.com/v/29704/?learn=on
https://video.tv.adobe.com/vc/29704/eng.json
## System administrators: Grant developer and API access control with Experience Platform permissions grant-developer-and-api-access-control

Before you can create integrations on Adobe Developer Console, your account must have developer and user permissions for an Experience Platform product profile.

NOTE
Only system administrators have the ability to view and manage API credentials in Permissions.
### Add developers to product profile add-developers-to-product-profile

Navigate to the [Admin Console](https://adminconsole.adobe.com/) and sign in with your Adobe ID.

Select **Products** from the navigation bar and then select **Adobe Experience Platform** from the list of products.

From the **Product Profiles** tab, select **AEP-Default-All-Users**. Alternatively, use the search bar to search for the product profile by entering the name.

Select the **Developers** tab, then select **Add Developer**.

The **Add developers** dialog appears. Enter the developer’s **Email or username**. A valid Email or username displays the developer details. Select **Save**.

The developer has been successfully added and appears on the **Developers** tab.

### Assign API credentials to a role

NOTE
Only a system administrator can assign APIs to roles in the Experience Platform UI.
To use and perform operations on Experience Platform APIs, a system administrator needs to add the API credentials in addition to a role’s given set of permissions. Get more information in the section about [managing API credentials for a role](/en/docs/experience-platform/access-control/abac/permissions-ui/permissions#manage-api-credentials-for-a-role).

A walkthrough of the steps described above for adding developers to product profiles and assigning APIs to roles is also available in the video tutorial below:

https://video.tv.adobe.com/v/3426407/?learn=on
https://video.tv.adobe.com/vc/3426407/eng.json
## Additional resources additional-resources

Refer to the additional resources linked below for further help getting started with Experience Platform APIs

- [Authenticate and access Experience Platform APIs](/en/docs/platform-learn/tutorials/platform-api-authentication) video tutorials page
- [Identity Management Service Postman Collection](https://github.com/adobe/experience-platform-postman-samples/tree/master/apis/ims) for generating access tokens
- [Experience Platform API Postman Collections](https://github.com/adobe/experience-platform-postman-samples/tree/master/apis/experience-platform)

## Next steps next-steps

By reading this document, you have gathered and successfully tested your access credentials for Experience Platform APIs. You can now follow along with the example API calls provided throughout the [documentation](/en/docs/experience-platform/landing/documentation/overview).

In addition to the authentication values you have gathered in this tutorial, many Experience Platform APIs also require a valid {SANDBOX_NAME} to be provided as a header. See the [sandboxes overview](/en/docs/experience-platform/sandbox/home) for more information.

recommendation-more-help
