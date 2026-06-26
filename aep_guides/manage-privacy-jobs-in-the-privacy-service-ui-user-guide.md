---
title: "Manage privacy jobs in the Privacy Service UI user-guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/privacy/ui/user-guide"
category: "guides"
topic: "experience-platform/privacy-service-guide"
created_at: "2026-06-26T17:24:01.843442+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Privacy Service Guide

# Manage privacy jobs in the Privacy Service UI user-guide

Last update: May 23, 2026
- Topics:
- [Privacy](#)

CREATED FOR:

- User
- Admin

This document provides steps for creating and managing privacy requests using the Privacy Service user interface.

IMPORTANT
Privacy Service is only meant for data subject and consumer rights requests. Any other usage of Privacy Service for data cleanup or maintenance is not supported or allowed. Adobe has a legal obligation to fulfill them in a timely manner. As such, load-testing on Privacy Service is not allowed as it is a production only environment and creates an unnecessary backlog of valid privacy requests.
A hard daily upload limit is now in place to help prevent abuse of the service. Users found to abuse the system will have their access to the service disabled. A subsequent meeting will then be held with them to address their actions and discuss the acceptable use for Privacy Service.
## Browse the Privacy Service UI dashboard

The dashboard for the Privacy Service UI provides two widgets that allow you to view the status of your privacy jobs: “Status Report” and “Job Requests”. The dashboard also displays the current selected regulation for the displayed jobs.

### Regulation Type

Privacy Service supports job requests for several privacy regulations. The following table lists the supported regulations and their corresponding label as represented in the UI.

Refer to the [Privacy regulations overview](/en/docs/experience-platform/privacy/regulations/overview) for a description of each regulation that explains the consumer rights and mandated business obligations.

TIP
The API regulation type has been included for general convenience.
UI Label
API
regulation_type
Regulation
APA_AUS (Australia)
apa_aus
Australia Privacy Act
CCCA (California)
ccpa
California Consumer Privacy Act (CCPA)
CPA_CO_USA (Colorado)
cpa_co_usa
Colorado Privacy Act
CPRA_CA_USA (California)
cpra_ca_usa
California Privacy Rights Act (CPRA)
CTDPA_CT_USA (Connecticut)
ctdpa_ct_usa
Connecticut Data Privacy Act
DPDPA_DE_USA (Delaware)
dpdpa_de_usa
Delaware Personal Data Privacy Act
FDBR_FL_USA (Florida)
fdbr_fl_usa
Florida Digital Bill of Rights
GDPR (European Union)
gdpr
The European Union’s General Data Protection Regulation
HIPAA_USA (United States)
hipaa_usa
Health Insurance Portability and Accountability Act
ICDPALIA_USA (Iowa)
icdpa_ia_usa
Iowa Consumer Data Protection Act
LGPD_BRA (Brazil)
lgpd_bra
Brazil’s “General Data Protection Law” Lei Geral de Proteção de Dados
MCDPA_MN_USA (Minnesota)
mcdpa_mn_usa
Minnesota Consumer Data Privacy Act
MCDPA_MT_USA (Montana)
mcdpa_mt_usa
Montana Consumer Data Privacy Act
MHMDA_WA_USA (Washington)
mhmda_wa_usa
Washington My Health My Data Act
MODPA_MD_USA (Maryland)
modpa_md_usa
Maryland Online Data Privacy Act
NDPA_NE_USA (Nebraska)
ndpa_ne_usa
Nebraska Data Protection Act
NHPA_NH_USA (New Hampshire)
nhpa_nh_usa
New Hampshire Privacy Act
NJDPA_NJ_USA (New Jersey)
njdpa_nj_usa
New Jersey Data Protection Act
NZPA_NZL (New Zealand)
nzpa_nzl
New Zealand’s Privacy Act (PA)
OCPA_OR_USA (Oregon)
ocpa_or_usa
Oregon Consumer Privacy Act
PDPA_THA (Thailand)
pdpa_tha
Thailand’s Personal Data Protection Act (PDPA)
PIPA_KOR (South Korea)
pipa_kor
South Korea’s Personal Information Privacy Act (PIPA)
QL25_QC_CAN (Quebec)
ql25_qc_can
Quebec Law 25
TDPSA_TX_USA (Texas)
tdpsa_tx_usa
Texas Data Privacy and Security Act
TIPA_TN_USA (Tennessee)
tipa_tn_usa
Tennessee Information Protection Act
UCPA_UT_USA (Utah)
ucpa_ut_usa
Utah Consumer Privacy Act
VCDPA_VA_USA (Virginia)
vcdpa_va_usa
Virginia Consumer Data Protection Act (VCDPA)
NOTE
See the overview on
supported privacy regulations
for more information on the legal context of each regulation.
Jobs for each regulation type are tracked separately. To switch between regulation types, select the **Regulation Type** dropdown menu and select the desired regulation from the list.

Upon changing the regulation type, the dashboard updates to show all operations, filters, widgets, and job-creation dialogs that apply to the selected regulation.

### Status Report

The graph on the left-hand side of the Status Report widget tracks submitted jobs against any jobs that may have reported back with errors. The graph on the right-hand side tracks jobs nearing the end of the 30-day compliance window.

Select one of the two toggle buttons above the graph to show or hide their respective metrics.

You can view the exact number of jobs associated with any data point on the graphs by hovering your mouse over the data point in question.

To view further details about a given data point, select the data point in question to display the associated jobs in the Job Requests widget. Take note of the filter that is applied just above the job list.

NOTE
When a filter has been applied to the Job Requests widget, you can remove the filter by selecting the
X
on the filter pill. Job Requests then return to the default tracking list.
### Job Requests job-requests

The Job Requests workspace lists details about the recent job requests in your organization. Details include the request type, current status, due date, requestor email, and so on. Sets of 100 records are loaded at a time. By default, the most recently created jobs are displayed at the top with more sets of records loaded as you scroll down to browse.

NOTE
The data for previously created jobs is only accessible for 30 days after the completion date.
You can filter the list by typing keywords into the search bar below the Job Requests title. The list automatically filters as you type, showing requests that contain values that match your search terms. The search field performs a “quick” search that matches Privacy Job IDs to the currently rendered/loaded jobs in the UI. It is not a comprehensive search of all your submitted jobs. Rather, it is a filter applied to the loaded results. Use the Privacy Service API to [return jobs based on a specific regulation, date ranges, or a single job](/en/docs/experience-platform/privacy/api/privacy-jobs#list).

TIP
To load records into the UI from the past 30 days, you must scroll down the table and load more batches of records.
Alternatively, use the search button to perform a privacy job query that spans a particular date range. This action returns all the privacy jobs submitted by your organization during the given time frame. Select the **Requested on** dropdown menu to choose a start and finish date for the query. The available options include Today, Last 7 Days, Last 2 Weeks, Last 30 Days, or Custom. When used with the Requested on option, the search feature only displays job requests that were submitted between your chosen date ranges.

To view the details of a particular job request, select the request’s job ID from the list to open the **Job Details** page.

This dialog contains status information about each Experience Cloud solution and its current state in relation to the overall job. As every privacy job is asynchronous, the page displays the latest communication date and time (GMT) from each solution, as some require more time than others to process the request.

If a solution has provided any additional data, it is viewable in this dialog. You can view this data by selecting individual product rows.

To download the complete job data as a CSV file, select **Export to CSV** at the top-right of the dialog.

## Create a new privacy job request create-a-new-privacy-job-request

NOTE
In order to create a privacy job request, you must provide identity information for the specific customers whose data is to be accessed or deleted. Please review the document on
identity data for privacy requests
before continuing with this section.
The Privacy Service UI provides two methods to create new job requests:

- [Use the Request Builder](#request-builder)
- [Upload a JSON file](#json)

Steps for using each of these methods are provided in the following sections.

### Use the Request Builder request-builder

Using the Request Builder, you can manually create a new privacy job request in the user interface. The Request Builder is best used for simpler and smaller sets of requests, because the Request Builder limits requests to have only ID type per user. For more complicated requests, it may better to [upload a JSON file](#json) instead.

To start using the Request builder, select **Create Request** below the Status Report widget on the right-hand side of the screen.

The **Create Request** dialog opens, displaying the available options for submitting a privacy job request for the currently selected regulation type.

{width="500"}

Select the **Job Type** of the request (“Delete” or “Access”) and one or more available products from the list.

Privacy Service supports two kinds of job requests for personal data: Access (read) and/or Delete. You can either submit a request to receive all information held in the product that relates to the subject of the inquiry, or request to delete all the information that relates to the subject of the inquiry.

{width="500"}

Under **Namespace type**, select the appropriate namespace type for the customer IDs being sent to Privacy Service.

{width="500"}

When using the standard namespace type, select a namespace from the drop-down menu (email, ECID, or AAID), then type the ID values in the textbox to the right, pressing **<enter>** for each ID to add it to the list.

{width="500"}

When using the custom namespace type, you must manually type in the namespace before providing the ID values below.

{width="500"}

When finished, select **Create**.

{width="500"}

The dialog disappears, and the new job (or jobs) are listed in the Job Requests widget along with their current processing status.

### Upload a JSON file json

When creating more complicated requests, such as those that use multiple ID types for each data subject being processed, you can create a request by uploading a JSON file.

Select the arrow next to **Create Request**, below the Status Report widget on the right-hand side of the screen. From the list of options that appears, select **Upload JSON**.

The **Upload JSON** dialog appears, providing a window for you to drag and drop your JSON file into.

{width="500"}

If you do not have a JSON file to upload, select **Download Adobe-GDPR-Request.json** to download a template that you can populate according to the values you have collected from your data subjects.

{width="500"}

Locate the JSON file on your computer, and drag it into the dialog window. If the upload is successful, the file name appears in the dialog. You can continue to add more JSON files as necessary by dragging and dropping them into the dialog.

When finished, select **Create**. The dialog disappears, and the new job (or jobs) are listed in the Job Requests widget along with their current processing status.

### Next steps

By reading this document, you have learned how to use the Privacy Service UI to create a privacy job, view a job’s details and monitor its processing status, and download the results once it has completed.

For steps on how to perform these operations programmatically using the Privacy Service API, please refer to the [API guide](/en/docs/experience-platform/privacy/api/overview).

recommendation-more-help
