---
title: "Authenticate and access the Privacy Service API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/privacy/api/getting-started"
category: "reference"
topic: "experience-platform/privacy-service-guide"
created_at: "2026-05-29T16:58:24.160654+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Privacy Service Guide

# Authenticate and access the Privacy Service API

Last update: May 23, 2026
- Topics:
- [Privacy](#)

CREATED FOR:

- Developer

This guide provides an introduction to the core concepts you must know before attempting to make calls to the Adobe Experience Platform Privacy Service API.

## Prerequisites prerequisites

This guide requires a working understanding of [Privacy Service](/en/docs/experience-platform/privacy/home) and how it allows you to manage access and delete requests from your data subjects (customers) across Adobe Experience Cloud applications.

In order to create access credentials for the API, an administrator within your organization must have previously set up product profiles for Privacy Service within Adobe Admin Console. The product profile that you assign to an API integration determines what permissions that integration has when accessing Privacy Service capabilities. See the guide on [managing Privacy Service permissions](/en/docs/experience-platform/privacy/permissions) for more information.

## Gather values for required headers gather-values-required-headers

In order to make calls to the Privacy Service API, you must first gather your access credentials to be used in required headers:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

These values are generated using [Adobe Developer Console](https://developer.adobe.com/console). Your {ORG_ID} and {API_KEY} only need to be generated once and can be reused in future API calls. However, your {ACCESS_TOKEN} is temporary and must be regenerated every 24 hours.

The steps for generating these values are covered in detail below.

### One-time setup one-time-setup

Go to [Adobe Developer Console](https://developer.adobe.com/console) and sign in with your Adobe ID. Next, follow the steps outlined in the tutorial on [creating an empty project](https://developer.adobe.com/developer-console/docs/guides/projects/projects-empty/) in the Developer Console documentation.

Once you have created a new project, select **Add to Project** and choose **API** from the dropdown menu.

#### Select the Privacy Service API select-privacy-service-api

The **Add an API** screen appears. Select **Experience Cloud** to narrow the list of available APIs, then select the card for **Privacy Service API** before selecting **Next**.

TIP
Select the
View docs
option to navigate in a separate browser window to the complete
Privacy Service API reference documentation
.
Next, select the authentication type to generate access tokens and access the Privacy Service API.

IMPORTANT
Select the
OAuth Server-to-Server
method, as this will be the only method supported moving forward. The
Service Account (JWT)
method is deprecated. While integrations using the JWT authentication method will continue to work until January 1st, 2025, Adobe strongly recommends that you migrate existing integrations to the new OAuth Server-to-Server method before that date. Get more information in the section [Deprecated]{class="badge negative"}
Generate a JSON Web Token (JWT)
.
#### Assign permissions through product profiles product-profiles

The final configuration step is to select the product profiles that this integration will inherit its permissions from. If you select more than one profile, their permission sets will be combined for the integration.

NOTE
Product profiles and the granular permissions they provide are created and managed by administrators through Adobe Admin Console. See the guide on
Privacy Service permissions
for more information.
When finished, select **Save configured API**.

Once the API has been added to the project, the **Privacy Service API** page for the project displays the following credentials that are required in all calls to Privacy Service APIs:

- {API_KEY} (Client ID)
- {ORG_ID} (Organization ID)

### Authentication for each session authentication-each-session

The final required credential you must gather is your {ACCESS_TOKEN}, which is used in the Authorization header. Unlike the values for {API_KEY} and {ORG_ID}, a new token must be generated every 24 hours to continue using the API.

In general, there are two methods of generating an access token:

- [Generate the token manually](#manual-token) for testing and development.
- [Automate token generation](#auto-token) for API integrations.

#### Generate a token manually manual-token

To manually generate a new {ACCESS_TOKEN}, navigate to **Credentials** > **OAuth Server-to-Server** and select **Generate access token**, as shown below.

A new access token is generated, and a button to copy the token to your clipboard is provided. This value is used for the required Authorization header, and must be provided in the format Bearer {ACCESS_TOKEN}.

#### Automate token generation auto-token

You can also use a Postman environment and collection to generate access tokens. For more information, read the section about [using Postman to authenticate and test API calls](/en/docs/experience-platform/landing/platform-apis/api-authentication#use-postman) in the Experience Platform API authentication guide.

## Reading sample API calls read-sample-api-calls

Each endpoint guide provides example API calls to demonstrate how to format your requests. These include paths, required headers, and properly formatted request payloads. Sample JSON returned in API responses is also provided. For information on the conventions used in documentation for sample API calls, see the section on [how to read example API calls](/en/docs/experience-platform/landing/platform-apis/api-guide#sample-api) in the getting started guide for Experience Platform APIs.

## Next steps next-steps

Now that you understand what headers to use, you are ready to begin making calls to the Privacy Service API. Select one of the endpoint guides to get started:

- [Privacy jobs](/en/docs/experience-platform/privacy/api/privacy-jobs)
- [Consent](/en/docs/experience-platform/privacy/api/consent)

recommendation-more-help
