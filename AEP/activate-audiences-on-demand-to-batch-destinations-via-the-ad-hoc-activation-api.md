---
title: "Activate audiences on-demand to batch destinations via the ad-hoc activation API"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/destinations/api/ad-hoc-activation-api"
category: "reference"
topic: "experience-platform/destinations-guide"
created_at: "2026-05-29T16:55:43.745697+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Destinations Guide

# Activate audiences on-demand to batch destinations via the ad-hoc activation API

Last update: May 23, 2026
- Topics:
- [Destinations](#)

CREATED FOR:

- Admin
- User

IMPORTANT
After completing the Beta phase, the ad-hoc activation API is now generally available (GA) to all Experience Platform customers. In the GA version, the API has been upgraded to version 2. Step 4 (
Obtain the latest audience export job ID
) is not required anymore, since the API does not require the export ID anymore.
See
Run the ad-hoc activation job
further below in this tutorial for more information.
## Overview overview

The ad-hoc activation API allows marketers to programmatically activate audience audiences to destinations, in a fast and efficient manner, for situations where immediate activation is required.

Use the ad-hoc activation API to export full files to your desired file reception system. Ad-hoc audience activation is only supported by [batch file-based destinations](/en/docs/experience-platform/destinations/destination-types#file-based).

The diagram below illustrates the end-to-end workflow for activating audiences via the ad-hoc activation API, including the segmentation jobs that take place in Experience Platform every 24 hours.

## Use cases use-cases

### Flash sales or promotions flash-sales

An online retailer is preparing a limited flash sale and wants to notify customers on a short notice. Through the Experience Platform ad-hoc activation API, the marketing team can export audiences on-demand, and quickly send promotional emails to the customer base.

### Current events or breaking news current-events

A hotel expects inclement weather over the following days, and the team wants to inform the arriving guests quickly, so they can plan accordingly. The marketing team can use the Experience Platform ad-hoc activation API to export audiences on-demand, and notify the guests.

### Integration testing integration-testing

IT managers can use the Experience Platform ad-hoc activation API to export audiences on-demand, so they can test their custom integration with Adobe Experience Platform, and ensure everything is working correctly.

## Guardrails guardrails

Keep in mind the following guardrails when using the ad-hoc activation API.

- Currently, each ad-hoc activation job can activate up to 80 audiences. Attempting to activate more than 80 audiences per job will cause the job to fail. This behavior is subject to change in future releases.
- Ad-hoc activation jobs cannot run in parallel with scheduled [audiences export jobs](/en/docs/experience-platform/segmentation/api/export-jobs). Before running an ad-hoc activation job, make sure the scheduled audience export job has finished. See [destination dataflow monitoring](/en/docs/experience-platform/dataflows/ui/monitor-destinations) for information on how to monitor the status of activation flows. For example, if your activation dataflow shows a **Processing** status, wait for it to finish before running the ad-hoc activation job.
- Do not run more than one concurrent ad-hoc activation job per audience.

## Segmentation considerations segmentation-considerations

Adobe Experience Platform runs scheduled segmentation jobs once every 24 hours. The ad-hoc activation API runs based on the latest segmentation results.

## Step 1: Prerequisites prerequisites

Before you can make calls to the Adobe Experience Platform APIs, make sure you meet the following prerequisites:

- You have an organization account with access to Adobe Experience Platform.
- Your Experience Platform account has the developer and user roles enabled for the Adobe Experience Platform API product profile. Contact your [Admin Console](/en/docs/experience-platform/access-control/home) administrator to enable these roles for your account.
- You have an Adobe ID. If you do not have an Adobe ID, go to the [Adobe Developer Console](https://developer.adobe.com/console) and create a new account.

## Step 2: Gather credentials credentials

To make calls to Experience Platform APIs, you must first complete the [authentication tutorial](https://www.adobe.com/go/platform-api-authentication-en). Completing the authentication tutorial provides the values for each of the required headers in all Experience Platform API calls, as shown below:

- Authorization: Bearer {ACCESS_TOKEN}
- x-api-key: {API_KEY}
- x-gw-ims-org-id: {ORG_ID}

Resources in Experience Platform can be isolated to specific virtual sandboxes. In requests to Experience Platform APIs, you can specify the name and ID of the sandbox that the operation will take place in. These are optional parameters.

- x-sandbox-name: {SANDBOX_NAME}

NOTE
For more information on sandboxes in Experience Platform, see the
sandbox overview documentation
.
All requests that contain a payload (POST, PUT, PATCH) require an additional media type header:

- Content-Type: application/json

### API reference documentation api-reference-documentation

You can find accompanying reference documentation for all the API operations in this tutorial. See the [Ad Hoc Activation API reference](https://developer.adobe.com/experience-platform-apis/references/ad-hoc-activation).

## Step 3: Create activation flow in the Experience Platform UI activation-flow

Before you can activate audiences through the ad-hoc activation API, you must first have an activation flow configured in the Experience Platform UI, for the chosen destination.

This includes going into the activation workflow, selecting your audiences, configuring a schedule, and activating them. You can use the UI or API to create an activation flow:

- [Use the Experience Platform UI to create an activation flow to batch profile export destinations](/en/docs/experience-platform/destinations/ui/activate/activate-batch-profile-destinations)
- [Use the Flow Service API to connect to batch profile export destinations and activate data](/en/docs/experience-platform/destinations/api/connect-activate-batch-destinations)

## Step 4: Obtain the latest audience export job ID (Not required in v2) segment-export-id

IMPORTANT
In the v2 of the ad-hoc activation API, you do not need to obtain the latest audience export job ID. You can skip this step and proceed to the next one.
After you configure an activation flow for your batch destination, scheduled segmentation jobs start running automatically every 24 hours.

Before you can run the ad-hoc activation job, you must obtain the ID of the latest audience export job. You must pass this ID in the ad-hoc activation job request.

Follow the instructions described [here](/en/docs/experience-platform/segmentation/api/export-jobs#retrieve-list) to retrieve a list of all the audience export jobs.

In the response, look for the first record that includes the schema property below.

```
"schema":{
   "name":"_xdm.context.profile"
}
```

The audience export job ID is in the id property, as shown below.

## Step 5: Run the ad-hoc activation job activation-job

Adobe Experience Platform runs scheduled segmentation jobs once every 24 hours. The ad-hoc activation API runs based on the latest segmentation results.

IMPORTANT
Note the following one-time constraint: Before running an ad-hoc activation job, make sure that at least one hour has passed from the moment that the audience was first activated according to the schedule you set in
Step 3 - Create activation flow in the Experience Platform UI
.
Before running an ad-hoc activation job, make sure the scheduled audience export job for your audiences has finished. See [destination dataflow monitoring](/en/docs/experience-platform/dataflows/ui/monitor-destinations) for information on how to monitor the status of activation flows. For example, if your activation dataflow shows a **Processing** status, wait for it to finish before running the ad-hoc activation job to export a full file.

Once the audience export job has completed, you can trigger the activation.

NOTE
Currently, each ad-hoc activation job can activate up to 80 audiences. Attempting to activate more than 80 audiences per job will cause the job to fail. This behavior is subject to change in future releases.
### Request request

IMPORTANT
It is mandatory to include the
Accept: application/vnd.adobe.adhoc.activation+json; version=2
header in your request to use v2 of the ad-hoc activation API.
For non–segmentation service audiences (for example, [external or custom upload audiences](/en/docs/experience-platform/segmentation/ui/audience-portal#import-audience)), you must specify the audience ID generated by Experience Platform in your request, not the external audience ID. You can find the system-generated ID at the top of the [audience summary panel](/en/docs/experience-platform/segmentation/ui/audience-portal#audience-summary), displayed as **ID#** followed by a UUID, when you open the audience details page in the audiences UI.

```

curl --location --request POST 'https://platform.adobe.io/data/core/activation/disflowprovider/adhocrun' \
--header 'x-gw-ims-org-id: 5555467B5D8013E50A494220@AdobeOrg' \
--header 'Authorization: Bearer {{token}}' \
--header 'x-sandbox-id: 6ef74723-3ee7-46a4-b747-233ee7a6a41a' \
--header 'x-sandbox-name: {sandbox-id}' \
--header 'Accept: application/vnd.adobe.adhoc.activation+json; version=2' \
--header 'Content-Type: application/json' \
--data-raw '{
   "activationInfo":{
      "destinationId1":[
         "segmentId1",
         "segmentId2"
      ],
      "destinationId2":[
         "segmentId2",
         "segmentId3"
      ]
   }
}'
```

Property
Description
- destinationId1
- destinationId2

The IDs of the destination instances to which you want to activate audiences. You can get these IDs from the Experience Platform UI, by navigating to
Destinations
>
Browse
tab, and clicking on the desired destination row to bring up the destination ID in the right rail. For more information, read the
destinations workspace documentation
.
- segmentId1
- segmentId2
- segmentId3

The IDs of the audiences that you want to activate to the selected destination. You can use the ad-hoc API to export Experience Platform-generated audiences as well as external (custom upload) audiences. When activating external audiences, use the system-generated ID instead of the audience ID. You can find the system-generated ID in the audience summary view in the audiences UI.
{width="100" modal="regular"}
{width="100" modal="regular"}
### Request with export IDs request-export-ids

```

curl -X POST https://platform.adobe.io/data/core/activation/disflowprovider/adhocrun \
 -H 'Authorization: Bearer {ACCESS_TOKEN}' \
 -H 'Content-Type: application/json' \
 -H 'x-gw-ims-org-id: {ORG_ID}' \
 -H 'x-api-key: {API_KEY}' \
 -d '
{
   "activationInfo":{
      "destinationId1":[
         "segmentId1",
         "segmentId2"
      ],
      "destinationId2":[
         "segmentId2",
         "segmentId3"
      ]
   },
   "exportIds":[
      "exportId1"
   ]
}
```

Property
Description
- destinationId1
- destinationId2

The IDs of the destination instances to which you want to activate audiences. You can get these IDs from the Experience Platform UI, by navigating to
Destinations
>
Browse
tab, and clicking on the desired destination row to bring up the destination ID in the right rail. For more information, read the
destinations workspace documentation
.
- segmentId1
- segmentId2
- segmentId3

The IDs of the audiences that you want to activate to the selected destination.
- exportId1

The ID returned in the response of the
audience export
job. See
Step 4: Obtain the latest audience export job ID
for instructions on how to find this ID.
### Response response

A successful response returns HTTP status 200.

```
{
   "order":[
      {
         "segment":"db8961e9-d52f-45bc-b3fb-76d0382a6851",
         "order":"ef2dcbd6-36fc-49a3-afed-d7b8e8f724eb",
         "statusURL":"https://platform.adobe.io/data/foundation/flowservice/runs/88d6da63-dc97-460e-b781-fc795a7386d9"
      }
   ]
}
```

Property
Description
segment
The ID of the activated audience.
order
The ID of the destination to which the audience was activated.
statusURL
The status URL of the activation flow. You can track the flow progress using the
Flow Service API
.
## API error handling api-error-handling

Destination SDK API endpoints follow the general Experience Platform API error message principles. See [API status codes](/en/docs/experience-platform/landing/troubleshooting#api-status-codes) and [request header errors](/en/docs/experience-platform/landing/troubleshooting#request-header-errors) in the Experience Platform troubleshooting guide.

### API error codes and messages specific to the ad-hoc activation API specific-error-messages

When using the ad-hoc activation API, you can come across error messages that are specific to this API endpoint. Review the table to understand how to address them when they do appear.

Error message
Resolution
Run already going on for audience
segment ID
for order
dataflow ID
with run id
flow run ID
This error message indicates that an ad-hoc activation flow is currently ongoing for an audience. Wait for the job to finish before triggering the activation job again.
Segments
<segment name>
are not part of this dataflow or out of schedule range!
This error message indicates that the audiences you selected to activate are not mapped to the dataflow or that the activation schedule set up for the audiences has either expired or not yet started. Check if the audience is indeed mapped to the dataflow and verify that the audience activation schedule overlaps with the present date.
## Related information related-information

- [Connect to batch destinations and activate data using the Flow Service API](/en/docs/experience-platform/destinations/api/connect-activate-batch-destinations)
- [Export files on-demand to batch destinations using the Experience Platform UI](/en/docs/experience-platform/destinations/ui/activate/export-file-now)

recommendation-more-help
