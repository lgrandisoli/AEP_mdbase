---
title: "Authenticate and access the Reactor API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/getting-started"
category: "reference"
topic: "experience-platform/tags"
created_at: "2026-05-29T17:08:44.133070+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Tags

# Authenticate and access the Reactor API

Last update: May 23, 2026
- Topics:
- [Tags](#)

CREATED FOR:

- Developer

In order to use the [Reactor API](https://developer.adobe.com/experience-platform-apis/references/reactor/) to create and manage Tags extensions, each request must include the following authentication headers:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}
- Accept: application/vnd.api+json;revision=1
- Content-Type: application/vnd.api+json

This guide covers how to use the Adobe Developer Console to gather the values for each of these headers so you can start making calls to the Reactor API.

## Gain developer access to Adobe Experience Platform gain-developer-access

Before you can generate authentication values for the Reactor API, you must have developer access to Experience Platform. To gain developer access, follow the beginning steps in the [Experience Platform authentication tutorial](/en/docs/experience-platform/landing/platform-apis/api-authentication). Once you have completed the [Gain User Access](/en/docs/experience-platform/landing/platform-apis/api-authentication#gain-user-access) step, return to this tutorial to generate the credentials specific to the Reactor API.

## Generate access credentials generate-access-credentials

Using Adobe Developer Console, you must generate the following three access credentials:

- {ORG_ID}
- {API_KEY}
- {ACCESS_TOKEN}

Your organization’s ID ({ORG_ID}) and API key ({API_KEY}) can be reused in future API calls after they have been initially generated. However, your access token ({ACCESS_TOKEN}) is temporary and must be regenerated every 24 hours.

The steps for generating these values are covered in detail below.

### One-time setup one-time-setup

Go to [Adobe Developer Console](https://www.adobe.com/go/devs_console_ui) and sign in with your Adobe ID. Next, follow the steps outlined in the tutorial on [creating an empty project](https://developer.adobe.com/developer-console/docs/guides/projects/projects-empty/) in the Developer Console documentation.

Once you have created a project, select **Add API** on the **Project Overview** screen.

The **Add an API** screen appears. Select **Experience Platform Launch API** from the list of available APIs before selecting **Next**.

Next, select the authentication type to generate access tokens and access the Experience Platform API.

IMPORTANT
Select the
OAuth Server-to-Server
method, as this will be the only method supported moving forward. The
Service Account (JWT)
method is deprecated. While integrations using the JWT authentication method will continue to work until January 1st, 2025, Adobe strongly recommends that you migrate existing integrations to the new OAuth Server-to-Server method before that date. Get more information in the section [Deprecated]{class="badge negative"}
Generate a JSON Web Token (JWT)
in the Experience Platform API authentication tutorial.
Select **Next** to continue.

The next screen prompts you to select one or more product profiles to associate with the API integration.

NOTE
Product profiles are managed by your organization through the Adobe Admin Console, and contain specific sets of permissions for granular features. Product profiles and their permissions can only be managed by users with administrator privileges within your organization. If you are unsure which product profiles to select for the API, contact your administrator.
Select the desired product profiles from the list, then select **Save configured API** to complete the API registration.

### Gather credentials gather-credentials

Once the API has been added to the project, the **Experience Platform API** page for the project displays the following credentials that are required in all calls to Experience Platform APIs:

- {API_KEY} (Client ID)
- {ORG_ID} (Organization ID)

### Generate an access token generate-access-token

The next step is to generate an {ACCESS_TOKEN} credential for use in Experience Platform API calls. Unlike the values for {API_KEY} and {ORG_ID}, a new token must be generated every 24 hours to continue using Experience Platform APIs.

TIP
These tokens expire after 24 hours. If you are using this integration for an application, it is a good idea to obtain your bearer token programmatically from within your application.
You have two options to generate your access tokens, depending on your use case:

- [Generate tokens manually](#manual)
- [Automate token generation](#auto-token)

#### Generate access tokens manually manual

To manually generate a new {ACCESS_TOKEN}, navigate to **Credentials** > **OAuth Server-to-Server** and select **Generate access token**, as shown below.

A new access token is generated, and a button to copy the token to your clipboard is provided. This value is used for the required Authorization header, and must be provided in the format Bearer {ACCESS_TOKEN}.

#### Automate token generation auto-token

You can also use a Postman environment and collection to generate access tokens. For more information, read the section about [using Postman to authenticate and test API calls](/en/docs/experience-platform/landing/platform-apis/api-authentication#use-postman) in the Experience Platform API authentication guide.

## Test API credentials test-api-credentials

By following the steps in this tutorial, you should have valid values for {ORG_ID}, {API_KEY}, and {ACCESS_TOKEN}. You can now test these values by using them in a simple cURL request to the Reactor API.

Start by attempting to make an API call to [list all companies](/en/docs/experience-platform/tags/api/endpoints/companies#list).

NOTE
You may not have any companies in your organization, in which case the response will be HTTP status 404 (Not Found). As long as you do not get a 403 (Forbidden) error, your access credentials are valid and working.
Once you confirm that your access credentials are working, continue to explore the other API reference documentation to learn the API’s many capabilities.

## Reading sample API calls read-sample-api-calls

Each endpoint guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/platform-apis/api-guide#sample-api) in the getting started guide for Experience Platform APIs.

## Next steps next-steps

Now that you understand what headers to use, you are ready to begin making calls to the Reactor API. Select one of the endpoint guides to get started:

- [Reactor API reference documentation](https://developer.adobe.com/experience-platform-apis/references/reactor/)
- [Reactor API guide overview](/en/docs/experience-platform/tags/api/overview)

recommendation-more-help
