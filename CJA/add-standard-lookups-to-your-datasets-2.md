---
title: "Add standard lookups to your datasets"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-connections/standard-lookups"
category: "other"
topic: "analytics-platform/using/cja-connections/standard-lookups"
created_at: "2026-06-23T20:41:58.351944+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Add standard lookups to your datasets

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- Admin

IMPORTANT
Standard Lookups are only available for Analytics source connector data sources in Customer Journey Analytics. You can use them with standard Adobe Analytics implementations, or the
Adobe Experience Platform Web SDK
, or the Experience Platform data collection APIs.
Standard lookups (also known as Adobe-supplied lookups) enhance the ability of Customer Journey Analytics to report on some dimensions/attributes that are not useful by themselves but are useful when joined with other data. Examples include attributes of mobile devices, and attributes of OS and Browser dimensions, such as browser version numbers. A ‘Standard Lookup’ is similar to a lookup dataset. Standard lookups are applicable across CX Enterprise organizations. They are automatically applied to all event datasets that contain certain XDM schema fields (see below for the specific fields.) A standard lookup dataset exists for each schema location that Adobe is classifying.

In traditional Adobe Analytics, these dimensions show up on their own, whereas in Customer Journey Analytics, you have to actively include these dimensions when you create data views. In the Connections workflow, you select a dataset that is flagged as one with a key for standard lookup. The Data Views UI automatically knows to include all the standard lookup dimensions as available for reporting. The lookup files are automatically kept up to date and available, across all regions and for all accounts. They are stored in region-specific organizations associated with the customer.

## Use standard lookups with Analytics source connector datasets

Standard lookup datasets automatically get applied at report time. If you use the Analytics source connector and you bring in a dimension for which Adobe provides a standard lookup, we automatically apply this standard lookup. If an event dataset contains XDM fields, we can apply standard lookups to it.

### Available standard lookup fields

- browser browser , group_id , id
- browser_group browser_group , id
- os os , group_id , id
- os_group os_group , id
- mobile_audio_support - multi
- mobile_color_depth
- mobile_cookie_support
- mobile_device_name
- mobile_device_number_transmit
- mobile_device_type
- mobile_drm - multi
- mobile_image_support - multi
- mobile_information_services
- mobile_java_vm - multi
- mobile_mail_decoration
- mobile_manufacturer
- mobile_max_bookmark_url_length
- mobile_max_browser_url_length
- mobile_max_mail_url_length
- mobile_net_protocols - multi
- mobile_os
- mobile_push_to_talk
- mobile_screen_height
- mobile_screen_size
- mobile_screen_width
- mobile_video_support - multi

## Report on standard lookup dimensions

In order to report on Adobe standard lookup dimensions, you have to add one or more of these dimensions when you create a [data view](/en/docs/analytics-platform/using/cja-dataviews/data-views) in Customer Journey Analytics. In **Data view** > **Components**:

- Select Schema fields from the drop-down menu in the left rail.
- Select Adobe lookups from the list of schema fields containers.
- Drill down into Browser , Mobile , or Operating System until you find the dimension you want to add.
- Drag the dimension into the Metrics or Dimensions table within Included components .

You can then use the lookup data in Workspace:

recommendation-more-help
