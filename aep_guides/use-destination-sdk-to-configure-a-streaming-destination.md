---
title: "Use Destination SDK to configure a streaming destination"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/destinations/destination-sdk/guides/configure-destination-instructions"
category: "guides"
topic: "experience-platform/destinations-guide"
created_at: "2026-06-26T17:28:25.717144+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Destinations Guide

# Use Destination SDK to configure a streaming destination

Last update: May 23, 2026
- Topics:
- [Destinations](#)

CREATED FOR:

- Admin
- User

## Overview overview

This page describes how to use the information in [Configuration options in Destinations SDK](/en/docs/experience-platform/destinations/destination-sdk/functionality/configuration-options) and in other Destination SDK functionality and API reference documents to configure a [streaming destination](/en/docs/experience-platform/destinations/destination-types#streaming-destinations). The steps are laid out in sequential order below.

## Prerequisites prerequisites

Before advancing to the steps illustrated below, read the [Destination SDK getting started](/en/docs/experience-platform/destinations/destination-sdk/getting-started) page for information on obtaining the necessary Adobe I/O authentication credentials and other prerequisites to work with Destination SDK APIs. This assumes that you have completed the partnership and permission prerequisites and are ready to start developing your destination.

## Steps to use the configuration options in Destination SDK to set up your destination steps

## Step 1: Create a server and template configuration create-server-template-configuration

Start by [creating a server and template configuration](/en/docs/experience-platform/destinations/destination-sdk/authoring-api/server-operations/create-destination-server) using the /destinations-server endpoint.

Shown below is an example configuration. Note that the message transformation template in the requestBody.value parameter is addressed in step 3, [Create transformation template](#create-transformation-template).

```
POST platform.adobe.io/data/core/activation/authoring/destination-servers
```

```
{
   "name":"Moviestar destination server",
   "destinationServerType":"URL_BASED",
   "urlBasedDestination":{
      "url":{
         "templatingStrategy":"PEBBLE_V1",
         "value":"https://api.moviestar.com/data/{{customerData.region}}/items"
      }
   },
   "httpTemplate":{
      "httpMethod":"POST",
      "requestBody":{
         "templatingStrategy":"PEBBLE_V1",
         "value":"insert after you create a template in step 3"
      },
      "contentType":"application/json"
   }
}
```

## Step 2: Create destination configuration create-destination-configuration

Shown below is an example configuration for a destination template, created by using the /destinations API endpoint. See [create a destination configuration](/en/docs/experience-platform/destinations/destination-sdk/authoring-api/destination-operations/create-destination-configuration) for more information.

To connect the server and template configuration in step 1 to this destination configuration, add the instance ID of the server and template configuration as destinationServerId here.

IMPORTANT
To create a correctly configured real-time (streaming) destination, you
must
add at least one target identity in
identityNamespaces
, as shown below. If no target identity is configured, users will not be able to proceed past the
Mapping step
of the activation workflow.
```
POST platform.adobe.io/data/core/activation/authoring/destinations
```

```
{
   "name":"Moviestar",
   "description":"Moviestar is a fictional destination, used for this example.",
   "status":"TEST",
   "customerAuthenticationConfigurations":[
      {
         "authType":"BEARER"
      }
   ],
   "customerDataFields":[
      {
         "name":"endpointsInstance",
         "type":"string",
         "title":"Select Endpoint",
         "description":"Moviestar manages several instances across the globe for REST endpoints that our customers are provisioned for. Select your endpoint in the dropdown list.",
         "isRequired":true,
         "enum":[
            "US",
            "EU",
            "APAC",
            "NZ"
         ]
      },
      {
         "name":"customerID",
         "type":"string",
         "title":"Moviestar Customer ID",
         "description":"Your customer ID in the Moviestar destination (e.g. abcdef).",
         "isRequired":true,
         "pattern":""
      }
   ],
   "uiAttributes":{
      "documentationLink":"http://www.adobe.com/go/destinations-moviestar-en",
      "category":"mobile",
      "connectionType":"Server-to-server",
      "frequency":"Streaming"
   },
   "identityNamespaces":{
      "external_id":{
         "acceptsAttributes":true,
         "acceptsCustomNamespaces":true
      },
      "another_id":{
         "acceptsAttributes":true,
         "acceptsCustomNamespaces":true
      }
   },
   "segmentMappingConfig":{
      "mapExperiencePlatformSegmentName":false,
      "mapExperiencePlatformSegmentId":false,
      "mapUserInput":false
   },
   "audienceMetadataConfig":{
      "audienceTemplateId":"cbf90a70-96b4-437b-86be-522fbdaabe9c"
   },
   "aggregation":{
      "aggregationType":"CONFIGURABLE_AGGREGATION",
      "configurableAggregation":{
         "aggregationPolicyId":null,
         "aggregationKey":{
            "includeSegmentId":true,
            "includeSegmentStatus":true,
            "includeIdentity":true,
            "oneIdentityPerGroup":true,
            "groups":null
         },
         "splitUserById":true,
         "maxBatchAgeInSecs":2400,
         "maxNumEventsInBatch":5000
      }
   },
   "destinationDelivery":[
      {
         "authenticationRule":"CUSTOMER_AUTHENTICATION",
         "destinationServerId":"9c77000a-4559-40ae-9119-a04324a3ecd4"
      }
   ]
}
```

## Step 3: Create message transformation template - use templating language to specify the message output format create-transformation-template

Based on the payloads that your destination supports, you must create a template that transforms the format of the exported data from Adobe XDM format into a format supported by your destination. See template examples in the section [Using a templating language for the identity, attributes, and audience membership transformations](/en/docs/experience-platform/destinations/destination-sdk/functionality/destination-server/message-format#using-templating) and use the [template authoring tool](/en/docs/experience-platform/destinations/destination-sdk/testing-api/streaming-destinations/create-template) provided by Adobe.

Once you have crafted a message transformation template that works for you, add it to the server and template configuration you created in step 1.

```
{
   "name":"Moviestar destination server",
   "destinationServerType":"URL_BASED",
   "urlBasedDestination":{
      "url":{
         "templatingStrategy":"PEBBLE_V1",
         "value":"https://api.moviestar.com/data/{{customerData.region}}/items"
      }
   },
   "httpTemplate":{
      "requestBody":{
         "templatingStrategy":"PEBBLE_V1",
         "value":"{\n    \"users\": [\n        {% for profile in input.profiles %}\n            {{profile|raw}}{% if not loop.last %},{% endif %}\n        {% endfor %}\n    ]\n}"
      },
      "contentType":"application/json"
   }
}
```

## Step 4: Create audience metadata configuration create-audience-metadata-configuration

For some destinations, Destination SDK requires that you configure an audience metadata configuration to programmatically create, update, or delete audiences in your destination. See [Audience metadata management](/en/docs/experience-platform/destinations/destination-sdk/functionality/audience-metadata-management) for information on when you need to set up this configuration and how to do it.

If you use an audience metadata configuration, you must connect it to the destination configuration you created in step 2. Add the instance ID of your audience metadata configuration to your destination configuration as audienceTemplateId.

```
{
   "name":"Moviestar",
   "description":"Moviestar is a fictional destination, used for this example.",
   "status":"TEST",
   "customerAuthenticationConfigurations":[
      {
         "authType":"BEARER"
      }
   ],
   "customerDataFields":[
      {
         "name":"endpointsInstance",
         "type":"string",
         "title":"Select Endpoint",
         "description":"Moviestar manages several instances across the globe for REST endpoints that our customers are provisioned for. Select your endpoint in the dropdown list.",
         "isRequired":true,
         "enum":[
            "US",
            "EU",
            "APAC",
            "NZ"
         ]
      },
      {
         "name":"customerID",
         "type":"string",
         "title":"Moviestar Customer ID",
         "description":"Your customer ID in the Moviestar destination (e.g. abcdef).",
         "isRequired":true,
         "pattern":""
      }
   ],
   "uiAttributes":{
      "documentationLink":"http://www.adobe.com/go/destinations-moviestar-en",
      "category":"mobile",
      "connectionType":"Server-to-server",
      "frequency":"Streaming"
   },
   "identityNamespaces":{
      "external_id":{
         "acceptsAttributes":true,
         "acceptsCustomNamespaces":true
      },
      "another_id":{
         "acceptsAttributes":true,
         "acceptsCustomNamespaces":true
      }
   },
   "segmentMappingConfig":{
      "mapExperiencePlatformSegmentName":false,
      "mapExperiencePlatformSegmentId":false,
      "mapUserInput":false
   },
   "audienceMetadataConfig":{
      "audienceTemplateId":"cbf90a70-96b4-437b-86be-522fbdaabe9c"
   },
   "aggregation":{
      "aggregationType":"CONFIGURABLE_AGGREGATION",
      "configurableAggregation":{
         "aggregationPolicyId":null,
         "aggregationKey":{
            "includeSegmentId":true,
            "includeSegmentStatus":true,
            "includeIdentity":true,
            "oneIdentityPerGroup":true,
            "groups":null
         },
         "splitUserById":true,
         "maxBatchAgeInSecs":2400,
         "maxNumEventsInBatch":5000
      }
   },
   "destinationDelivery":[
      {
         "authenticationRule":"CUSTOMER_AUTHENTICATION",
         "destinationServerId":"9c77000a-4559-40ae-9119-a04324a3ecd4"
      }
   ]
}
```

## Step 5: Set up authentication set-up-authentication

Depending on whether you specify "authenticationRule": "CUSTOMER_AUTHENTICATION" or "authenticationRule": "PLATFORM_AUTHENTICATION" in the destination configuration above, you can set up authentication for your destination by using the /destination or the /credentials endpoint.

NOTE
CUSTOMER_AUTHENTICATION
is the more common of the two authentication rules and is the one to use if you require users to provide some form of authentication to your destination before they can set up a connection and export data.
If you selected "authenticationRule": "CUSTOMER_AUTHENTICATION" in the destination configuration and your destination supports the OAuth 2 authentication method, read [OAuth 2 authentication](/en/docs/experience-platform/destinations/destination-sdk/functionality/destination-configuration/oauth2-authorization).

If you selected "authenticationRule": "PLATFORM_AUTHENTICATION", you must create a [credentials configuration](/en/docs/experience-platform/destinations/destination-sdk/credentials-api/create-credential-configuration) and pass the credential object’s ID in the authenticationId parameter in the [destination delivery](/en/docs/experience-platform/destinations/destination-sdk/functionality/destination-configuration/destination-delivery#platform-authentication) configuration.

## Step 6: Test your destination test-destination

After setting up your destination using the configuration endpoints in the previous steps, you can use the [destination testing tool](/en/docs/experience-platform/destinations/destination-sdk/testing-api/streaming-destinations/streaming-destination-testing-overview) to test the integration between Adobe Experience Platform and your destination.

As part of the process to test your destination, you must use the Experience Platform UI to create segments, which you will activate to your destination. Refer to the two resources below for instructions how to create audiences in Experience Platform:

- [Create an audience documentation page](/en/docs/experience-platform/segmentation/ui/audience-portal#create-audience)
- [Create an audience video walkthrough](/en/docs/platform-learn/tutorials/audiences/create-audiences)

## Step 7: Publish your destination publish-destination

NOTE
This step is not required if you are creating a private destination for your own use, and are not looking to publish it in the destinations catalog for other customers to use.
After configuring and testing your destination, use the [destination publishing API](/en/docs/experience-platform/destinations/destination-sdk/publishing-api/create-publishing-request) to submit your configuration to Adobe for review.

## Step 8: Document your destination document-destination

NOTE
This step is not required if you are creating a private destination for your own use, and are not looking to publish it in the destinations catalog for other customers to use.
If you are an Independent Software Vendor (ISV) or System Integrator (SI) creating a [productized integration](/en/docs/experience-platform/destinations/destination-sdk/overview#productized-custom-integrations), use the [self-service documentation process](/en/docs/experience-platform/destinations/destination-sdk/document-destination/documentation-instructions) to create a product documentation page for your destination in the [Experience Platform destinations catalog](/en/docs/experience-platform/destinations/catalog/overview).

## Step 9: Submit destination for Adobe’s review submit-for-review

NOTE
This step is not required if you are creating a private destination for your own use, and are not looking to publish it in the destinations catalog for other customers to use.
Finally, before the destination can be published in the Experience Platform catalog and visible to all Experience Platform customers, you need to officially submit the destination for Adobe’s review. Find complete information about how to [submit for review a productized destination authored in Destination SDK](/en/docs/experience-platform/destinations/destination-sdk/guides/submit-destination).

recommendation-more-help
