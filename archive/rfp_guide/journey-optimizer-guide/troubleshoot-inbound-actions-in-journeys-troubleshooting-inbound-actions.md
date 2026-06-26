---
title: "Troubleshoot inbound actions in journeys troubleshooting-inbound-actions"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-inbound"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:17.601999+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Troubleshoot inbound actions in journeys troubleshooting-inbound-actions

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)
- [Monitoring](#)

CREATED FOR:

- Intermediate
- User

Inbound actions, such as In-app, web, and code-based experiences, are critical components of Journey Optimizer as they enable personalized engagement with users during their journey. However, unexpected behavior, such as missing inbound content, or continued delivery after a profile exits the journey, can occur.

This guide provides a step-by-step process to debug issues related to inbound actions in a journey, in order to help you identify and resolve them independently before reaching out to support.

## Prerequisites prerequisites

Before you can start troubleshooting, ensure the following:

- Set up an Assurance session. Learn how in the Adobe Experience Platform Assurance documentation .
- Navigate to the journey containing the inbound action to retrieve the journey name and version ID. note NOTE The journey version ID can be found in the URL after ‘journey/’ (for example: 86232fb1-2932-4036-8198-55dfec606fd7 ).
- Click the inbound action to view its details. Retrieve the inbound action label and ID.
- Get the profile namespace and ID to identify the profile encountering issues. Based on your configuration, the namespace can be ECID, email, or customer ID for example. Learn how to look up a profile in the Experience Platform documentation .

## Scenario 1: The user hasn’t received the inbound content scenario-1

In this scenario, a profile has entered the inbound action in the journey, but even after 30 minutes, the corresponding inbound content is not showing up in the device/client at the setup trigger step.

### Pre-checks pre-checks

- Journey Inbound dataset is enabled for profile ingestion The inbound action uses the Journey Inbound dataset for the profile updates during execution. Ensure that the dataset is enabled for Profiles in the current sandbox. Learn more on datasets
- ‘joai’ identity defined in platform identities The inbound action uses the joai namespace in the profile segmentMembership for activating the profile for the inbound step. Ensure it has been defined in Platform Identities for the sandbox. Learn more on Experience Platform Identity Service

### Debugging Steps debugging-steps

The chart below shows the sequence of debugging steps you can follow:

{align="center" width="70%"}

### Step 1: check if the device/client is receiving the content from the edge network step-1

Start by checking if the device/client is getting the expected content.

In-app channel
- Go to the Assurance session and select the In-App Messaging section from the left panel.
- In the Messages on Device tab, click the Messages drop-down list. {width="80%"}
- Look for a message with the journey name followed by ‘- In-app message’. If present, it means the In-app message is present on the device/client and the issue might be related to the In-app trigger.
- If the message is not found, the In-app message was not received by the device/client.

Web channel
Visit the page and inspect the networking tab, or check the Edge response payload in the
Edge Delivery
section of the
Assurance
session.
Code-based experience channel
Perform a curl request using
Adobe’s API
and check the Edge response payload in the
Edge Delivery
section of the
Assurance
session.
### Step 2: check if the edge network is returning the content step-2

This step is to make sure the Edge Network is returning the expected inbound content to be rendered on the device/client.

When a profile enters an inbound action in a journey, it is automatically qualified into a special audience segment (in the **joai** namespace) corresponding to the inbound journey action.

When a client makes a request to the Edge Network for a given profile and surface, the profile qualifies to receive content for the inbound journey actions targeting that surface - only if the profile is currently a member of the corresponding **joai** segment.

To debug the Edge Network behavior, follow the steps below.

- Open the Edge Delivery view in the Assurance session. This view provides information about the execution of the inbound action on the Edge Network server. Learn more in the Experience Platform documentation .
- Verify if the Edge activity corresponding to the inbound action is listed in the Qualified Activities or Unqualified Activities sections. If in the Qualified Activities section, the profile qualified for the inbound journey action, and the content should be returned. If in the Unqualified Activities section, the profile did not qualify for the inbound journey action. See the exclusion reasons for more details. If in neither section , either there was a problem with publishing the inbound journey action to the Edge Network, or the requested surface URI did not match the channel configuration settings for the inbound action. note NOTE To find your Edge activity in the Assurance session, look for the activity where the audienceNamespace is joai and the audienceSegmentId is < JourneyVersionID >_< JourneyActionID > (for example: 86232fb1-2932-4036-8198-55dfec606fd7_708f718d-8503-4427-ad8d-8e28979b554c ). {width="70%"}
- If your activity is in the Unqualified Activities section and the exclusion reason is ‘Segment is not active’ , it means the Edge Network delivery server does not think the profile is part of the relevant joai audience segment. You can double check whether the joai segment is present in the Edge Network delivery server’s view of the profile by opening the segmentsMap element of the Profile section and looking for the presence of the joai segment ID.
- If the Edge Network delivery server does not view the profile as being in the relevant joai segment, go to the next step.

### Step 3: check if the ‘joai’ audience membership has propagated to the edge network step-3

This step is to verify that the Edge profile was correctly updated when the profile entered the inbound journey action and the profile was qualified into the corresponding **joai** segment.

When a profile is qualified into a **joai** segment, the profile is first updated on the Hub and then the segment membership is projected to the Edge Profile for use by the Edge Network delivery server.

NOTE
The propagation from Hub to Edge can take up to 15-30 minutes from the moment the profile is updated on the Hub.
To check for the presence of the **joai** segment in the Edge profile’s segmentMembership attribute, follow the steps below.

- Navigate to the Customer > Profiles menu in the Journey Optimizer left navigation pane and browse to the profile using namespace and ID. Learn more on Real-time Customer Profiles
- Select the Attributes tab and choose the Edge view.
- Click View JSON to open the JSON view for the profile. {width="80%"}
- Go to the segmentMembership attribute and check if the segment ID < JourneyVersionID> _< JourneyActionID > is present in the joai namespace and if in realized status. {width="90%"} If present, the joai segment corresponding to the inbound journey action was correctly propagated to the Edge profile. If not displayed in the Edge Network delivery server’s view of the profile, there might be a problem with how the delivery server is loading the Edge profile.
- If the joai segment ID is not present or is in exited state, it means it was not (yet) propagated to Edge. Wait 15 to 30 minutes for the segmentMembership values to be propagated from the Hub to the Edge. If still not present, go to the next step.

### Step 4: check if the ‘joai’ audience membership is present in the profile on the hub step-4

This step is to verify that the Hub profile was correctly updated when the profile entered the inbound journey action and the profile was qualified into the corresponding **joai** segment.

NOTE
The ingestion of the
joai
segment membership into the Hub profile can take up to 15-30 minutes from the moment the profile entered the inbound journey action.
To check for the presence of the **joai** segment in the Hub profile’s segmentMembership attribute, follow the steps below.

- Navigate to the Customer > Profiles menu in the Journey Optimizer left navigation pane and browse to the profile using namespace and ID. Learn more on Real-time Customer Profiles
- Select the Attributes tab and choose the Hub view.
- Click View JSON to open the JSON view for the profile.
- Go to the segmentMembership attribute and check if the segment ID < JourneyVersionID> _< JourneyActionID > is present in the joai namespace and if in realized status. If present, the joai segment corresponding to the inbound journey action was correctly ingested in the Hub profile. If not found in the Edge profile after at least 30 minutes, there might be a problem with the Edge projection system.
- If the joai segment ID is not present or is in exited state, it means the profile was not (yet) correctly qualified into the special joai audience segment upon entry into the corresponding inbound journey action. Wait 15 to 30 minutes for the segmentMembership values to be ingested into the profile on the Hub. If still not present, go to the next step.

### Step 5: If the client/device is still not getting the expected content step-5

If you’ve gone through all the steps above and aren’t seeing the expected behavior after waiting 30 to 60 minutes for the segment membership to propagate to the Edge Network, contact Adobe Customer Care or your Adobe representative.

Include as much detail as you can from the debugging steps, such as:

- the step where you see the unexpected behavior;
- the journey version ID;
- the journey action ID;
- the full Assurance trace;
- the JSON view of Edge profile;
- the JSON view of Hub profile;
- etc.

## Scenario 2: The user is still receiving the inbound content scenario-2

This scenario is the reverse of [Scenario 1](#scenario-1): the profile has exited the journey, but the user is still receving the inbound content.

However, when a profile exits a journey, it should no longer qualify for the **joai** audience segments corresponding to the inbound actions in the journey.

Go through the same debugging steps as for [Scenario 1](#debugging-steps) to check whether the Hub profile, Edge profile and Edge Network delivery server correctly reflect the segment membership status of the relevant **joai** segment, and whether the client is no longer receiving the inbound content.

recommendation-more-help
