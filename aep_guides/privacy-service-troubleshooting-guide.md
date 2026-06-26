---
title: "Privacy Service troubleshooting guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/privacy/troubleshooting-guide"
category: "guides"
topic: "experience-platform/privacy-service-guide"
created_at: "2026-06-26T17:28:11.691084+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Privacy Service Guide

# Privacy Service troubleshooting guide

Last update: May 23, 2026
- Topics:
- [Privacy](#)

CREATED FOR:

- User
- Admin

Adobe Experience Platform Privacy Service provides a RESTful API and user interface to help companies manage customer data privacy requests. With Privacy Service, you can submit requests to access and delete private or personal customer data, facilitating automated compliance with organizational and legal privacy regulations.

This document provides answers to frequently asked questions about Privacy Service, as well as information on commonly encountered errors in the API.

## When making privacy requests in the API, what is the difference between a user and a user ID? user-ids

In order to make a new privacy job in the API, the JSON payload of the request must contain a users array that lists specific information for each user to which the privacy request applies. Each item in the users array is an object which represents a particular user, identified by its key value.

In turn, each user object (or key) contains its own userIDs array. This array lists specific ID values **for that one particular user**.

Consider the following example users array:

```
"users": [
  {
    "key": "DavidSmith",
    "action": ["access"],
    "userIDs": [
      {
        "namespace": "email",
        "value": "dsmith@acme.com",
        "type": "standard"
      }
    ]
  },
  {
    "key": "user12345",
    "action": ["access", "delete"],
    "userIDs": [
      {
        "namespace": "email",
        "value": "ajones@acme.com",
        "type": "standard"
      },
      {
        "namespace": "ECID",
        "type": "standard",
        "value":  "443636576799758681021090721276",
        "isDeletedClientSide": false
      }
    ]
  }
]
```

The array contains two objects, representing individual users identified by their key values (“DavidSmith” and “user12345”). “DavidSmith” only has one listed ID (their email address), whereas “user12345” has two (their email address and ECID).

For more information on providing user identity information, see the guide on [identity data for privacy requests](/en/docs/experience-platform/privacy/identity-data).

## Can I use Privacy Service to clean up data that was accidentally sent to Experience Platform?

Adobe does not support using Privacy Service for clearing out data that was accidentally submitted to a product. Privacy Service is designed to assist you in meeting your obligations for data subject (or consumer) access or delete requests. Any other usage of Privacy Service for data cleanup or maintenance is not supported or allowed.

Privacy requests are time-sensitive and are completed related to applicable privacy law. the submission of requests which are not data-subject/consumer access or delete requests impacts all Privacy Service customers and the ability for Privacy Service to support the appropriate legal timelines. A hard daily upload limit is now in place to help prevent abuse of the service.

Please contact your Adobe account team to coordinate and provide a level of effort to remove any PII or data issues.

## How do I get information about the status of my privacy request or job?

You can retrieve details about a particular job by using the Privacy Service API or user interface.

### Using the API

To retrieve the status of a particular job using the Privacy Service API, make a request to the root (GET /) endpoint, using the job’s ID in the request path. For more details, see the section on [checking the status of a job](/en/docs/experience-platform/privacy/api/privacy-jobs#check-the-status-of-a-job) in the Privacy Service API guide.

### Using the UI

All active job requests are listed in the **Job Requests** widget on the Privacy Service UI dashboard. The status for each job request is displayed under the **Status** column. For more information on viewing job requests in the UI, please see the [Privacy Service user guide](/en/docs/experience-platform/privacy/ui/user-guide).

## How do I download the results of my completed privacy jobs?

The Privacy Service API and user interface both provide methods for downloading the results of completed jobs in ZIP format.

### Using the API

Make a request to the root (GET /) endpoint in the Privacy Service API, using the ID of the job whose results you want to download in the request path. If the job’s status is complete, the API will include a downloadURL attribute in the response body. This attribute contains a URL that you can paste into the address bar of your browser to download the ZIP file.

For more details, see the section on [looking up a job by its ID](/en/docs/experience-platform/privacy/api/privacy-jobs#check-the-status-of-a-job) in the Privacy Service API guide.

### Using the UI

On the Privacy Service UI dashboard, find the job you want to download from the **Job Requests** widget. Select the ID of the job to open the Job Details page. From here, select **Download** in the top-right corner to download the ZIP file. See the [Privacy Service user guide](/en/docs/experience-platform/privacy/ui/user-guide) for more detailed steps.

## Common error messages common-error-messages

The following table outlines some common errors in Privacy Service, with descriptions to help resolve their respective issues.

Error message
Description
User IDs were not found.
Some of the user IDs provided in the request could not be found and were skipped. Ensure that you are using the correct namespace(s) and ID values in the request payload. See the document on
providing identity data
for a more detailed explanation.
Invalid Namespace
A provided identity namespace for a user ID was invalid. See the section on
standard identity namespaces
in the Privacy Service API guide appendix for a list of accepted namespaces. If you are using a custom namespace, ensure you are setting the ID’s
type
property to “custom”.
Partially Completed
The job completed successfully, but some data was not applicable for the given request and was skipped.
The data is not in the required format.
One or more of the data values for the specified application was incorrectly formatted. Check the job details for more info.
The IMS Org has not been provisioned.
This message occurs when your organization has not been provisioned for Privacy Service. Contact your administrator for more information.
Access and permissions are required.
Access and permissions are required in order to use Privacy Service. Contact your administrator to gain access.
There was a problem uploading and archiving the access data.
When this error occurs, re-upload the access data and try again.
The workload was exceeded for the current document rate limit.
When this error occurs, reduce the submission rate and try again.
Too Many Requests
(HTTP 429 errors)
If your submission patterns exceed the monitored limit of allowed data subject jobs, you will receive a HTTP 429 error in response to continued traffic from your organization. Privacy Service is intended for the processing of data subject privacy requests. It is not to be used for data cleanup. If you receive HTTP 429 errors, throttling and request limits are implemented to protect Adobe from abuse that could put legitimate compliance work at risk.
Alternative methods to minimize your data are provided by
setting dataset expiration schedules
and using the
record delete feature
. See their respective documentation for more information on how to apply these capabilities.
recommendation-more-help
