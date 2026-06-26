---
title: "Destinations dashboard"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/dashboards/guides/destinations"
category: "guides"
topic: "experience-platform/dashboards-guide"
created_at: "2026-05-29T17:04:39.279595+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Dashboards Guide

# Destinations dashboard

Last update: May 13, 2026
- Topics:
- [Dashboards](#)

CREATED FOR:

- Developer
- User

The Adobe Experience Platform user interface (UI) provides a dashboard through which you can view important information about your organization’s active destinations, as captured during a daily snapshot. This guide outlines how to access and work with the destinations dashboard in the UI and provides more information regarding the metrics displayed in the dashboard.

For an overview of destinations, as well as a catalog of all available destinations within Experience Platform, please visit the [destinations documentation](/en/docs/experience-platform/destinations/home).

## Destinations dashboard data destinations-dashboard-data

The Destinations dashboard displays a snapshot of the destinations that your organization has enabled within Experience Platform. The data in the snapshot shows the data exactly as it appears at the specific point in time when the snapshot was taken. In other words, the snapshot is not an approximation or sample of the data, and the destinations dashboard is not updating in real-time.

NOTE
Any changes or updates made to the data since the snapshot was taken will not be reflected in the dashboard until the next snapshot is taken.
## Explore the Destinations dashboard explore

To navigate to the destinations dashboard within the Experience Platform UI, select **Destinations** in the left rail, then select the **Overview** tab to display the dashboard.

The date and time of the most recent snapshot is displayed at the top of the Overview next to the destination dropdown. All widget data is accurate as of that date and time. The timestamp of the snapshot is provided in UTC; it is not in the timezone of the individual user or organization.

NOTE
If your organization is new to Experience Platform and does not yet have active destinations, the Destinations dashboard and Overview tab are not visible. Instead, selecting Destinations from the left navigation displays the Catalog tab. To learn more about the Catalog tab, refer to the
Destinations workspace guide
.
### Modify the Destinations dashboard modify

Select **Modify dashboard** to change the appearance of the destinations dashboard. Changes to the dashboard are per user and not organization wide. You can move, add, resize, and remove widgets from the dashboard and access the widget library to customize your dashboard. From the widget library, you can explore the available widgets and create custom widgets for your organization.

Please refer to the [modifying dashboards](/en/docs/experience-platform/dashboards/customize/modify) and [widget library overview](/en/docs/experience-platform/dashboards/customize/widget-library) documentation to learn more.

### Add widgets add-widget

Select **Add widget** to navigate to the widget library and see a list of the available widgets to add to your dashboard.

From the widget library, you can browse the selection of standard and custom audience widgets. For information on how to add widgets, please see the widget library documentation on how to [add a widget](/en/docs/experience-platform/dashboards/customize/widget-library#add-widgets).

### View SQL view-sql

You can view the SQL that generates the insights visualized on your dashboard with a toggle on the Overview workspace. You can take inspiration from the SQL of your existing insights to create new queries that derive unique insights from Experience Platform data based on your business needs. To learn more about this feature, see the [View SQL UI guide](/en/docs/experience-platform/dashboards/view-sql).

## Default widgets default-widgets

A default widget load-out is provided for all new instances of Adobe Experience Platform that highlights the latest available insights from your data. The following widgets are pre-configured in your segments view from the outset. Full details on the purpose and function of the widgets can be found below.

- [Most used destinations](#most-used-destinations)
- [Recently created destinations](#recently-created-destinations)
- [Recently activated segments](#recently-activated-segments)

NOTE
As of July 26th 2023, Profiles, Audiences, and Destinations Overview dashboards have been reset to a new default widget load-out for all users who did not modify their views in the previous six months.
Refer to the documentation in the
Profiles
and
Audiences
default widget sections for details on which widgets are included as part of the default widget load-outs. You can continue to customize your dashboard widgets as before.
## Standard widgets standard-widgets

Adobe provides multiple standard widgets that you can use to visualize different metrics related to your destinations and assess the completeness of the audiences available for your data analysis. You can also create custom widgets to be shared with your organization using the Widget library. To learn more about creating custom widgets, please begin by reading the [Widget library overview](/en/docs/experience-platform/dashboards/customize/widget-library).

### Prerequisites prerequisites

Before continuing with the descriptions of standard widgets, please ensure that you are familiar with the definitions of the following key terms used throughout the documentation:

- **Segment definition:** A segment definition is a **set of rules** used to describe key characteristics or behavior of a target audience. These rules include attribute and event data that qualify the profiles as part of an audience.
- **Audience**: A set of people, accounts, households, or other entities that share common characteristics and behaviors.
- **Mapped / Mapping**: Data mapping is the process of mapping source data fields to related target fields in a destination.
- **Identity**: An identity is an identifier that uniquely represents an individual customer, such as a cookie ID, device ID, or email ID.
- **Activate**: Activate is the action taken by a user to map an audience or profiles to a destination such as Oracle Eloqua, Google, or Salesforce Marketing Cloud.

To learn more about each of the available standard widgets, select the name of a widget from the following list:

- [Most used destinations](#most-used-destinations)
- [Recently created destinations](#recently-created-destinations)
- [Recently activated audiences](#recently-activated-audiences)
- [Recently activated audiences by destination](#recently-activated-audiences-by-destination)
- [Audience size trend](#audience-size-trend)
- [Unmapped audiences by identity](#unmapped-audiences-by-identity)
- [Mapped audiences by identity](#mapped-audiences-by-identity)
- [Common audiences](#common-audiences)
- [Mapped audiences](#mapped-audiences)
- [Mapped audience health](#mapped-audience-health)
- [Destinations count](#destinations-count)
- [Destination status](#destination-status)
- [Active destinations by destination platform](#active-destinations-by-destination-platform)
- [Activated audiences across all destinations](#activated-audiences-across-all-destinations)
- [Activated audiences](#activated-audiences)

### Most used destinations most-used-destinations

The **Most used destinations** widget displays your organization’s top destinations by the number of mapped audiences, as of the last snapshot. This ranking provides insight into which destinations are being utilized while also potentially showing those that may be underutilized.

For example, if you configured a destination yesterday but have not mapped any audiences to it, you would be able to see that the destination is currently underutilized.

The number of mapped audiences shown in the Audience count column is accurate as of the last daily snapshot. Mapping a new audience to the destination does not update the count until the next snapshot is taken.

Select the name of a destination from the list shown on the widget to navigate to the destination details for that particular destination. You can also select **View All** to navigate to the **Browse** tab and then select the name of a destination to view its details.

### Recently created destinations recently-created-destinations

The **Recently created destinations** widget enables you to see a list of your organization’s most recently configured destinations.

The created date shown is accurate to the last daily snapshot. In other words, if you create a new destination, it will not appear in the list until after the next snapshot is taken.

Selecting the name of a destination from the list shown on the widget will take you to the destination details as linked from the **Browse** tab. You can also select **View All** to navigate to the **Browse** tab and then select the name of a destination to view its details.

To learn more about how to configure specific types of destinations, visit the [destinations documentation](/en/docs/experience-platform/destinations/home).

### Recently activated audiences recently-activated-audiences

The **Recently activated audiences** widget provides a list of the audiences most recently mapped to a destination. This list provides a snapshot of the audiences and destinations that are actively in use in the system and can help in troubleshooting any erroneous mappings.

The Updated date shown displays the last time the audience was activated to the destination and is accurate to the last daily snapshot. In other words, if you activate an audience to the destination, the updated date will not change until after the next snapshot is taken.

Selecting the name of an audience from the list shown on the widget takes you to the audience details. You can also select **View All** to navigate to the Audiences Browse tab and then select the name of an audience to view its details.

For more information on working with audiences in Experience Platform, please refer to the [Segmentation Service overview](/en/docs/experience-platform/segmentation/home).

### Recently activated audiences by destination recently-activated-audiences-by-destination

The **Recently activated audiences by destination** widget displays the top five most recently activated audiences in descending order according to the destination chosen in the overview dropdown. It is similar to the Recently activated audiences widget, but the data displayed **only** applies to the selected destination.

This widget contains two metrics: the audiences name and the date that the audiences was last activated to the destination. The data displayed is correct as of the last daily snapshot.

You can view an audience’s details by selecting the name of the audience from the list shown.

Please see the prerequisites section for the [definitions of terms used](#prerequisites) in this description.

### Audience size trend audience-size-trend

The **Audience size trend** widget depicts the relationship of the profile count over a period of time for an audience that has been mapped to that destination account. The widget uses a line graph to illustrate the number of profiles contained in the audience, that are being sent to the destination account daily.

A time period for the audience trend over the past 30 days, 90 days, or 12 months, can be adjusted using the first dropdown menu.

The second dropdown menu lists every available audience that can be sent to the destination account chosen at the top of the dashboard.

The **Audience size trend** widget provides a Captions button in the top right of the widget. Select **Captions** to open the automatic captions dialog. A machine learning model automatically generates captions to describe the key trends and important events by analyzing the chart and audience data.

### Unmapped audiences by identity unmapped-audiences-by-identity

The **Unmapped audiences by identity** widget lists the top five **unmapped** audiences ranked by descending identity count for a given destination and identity. It highlights audiences that are the most beneficial to map to the chosen destination account based on the chosen ID.

The destination ID dropdown filters your available audiences. The filter IDs listed in the dropdown change depending on the destination account selected at the top of the overview page.

The identities column counts the number of source IDs within the audience that could map to the ID chosen in the widget ID dropdown.

Please see the prerequisites section for the [definitions of terms used](#prerequisites) in this description.

### Mapped audiences by identity mapped-audiences-by-identity

This widget provides a top five list of **mapped** audiences. The list is ordered from high to low according to the number of source IDs contained within the audiences. The destination ID to be counted is selected from the dropdown menu below the widget title. The destination IDs available from the drop-down in the widget will change according to the destination account filter chosen at the top of the overview dashboard.

The **Mapped audiences by identity** widget highlights at a glance, the likelihood of successfully targeting profile opportunities for a campaign within the chosen destination. An efficient targeted campaign does not depend on the number of profiles sent to the destination but rather the number of source IDs that are likely to be matched with the destination IDs to provide useful and actionable data.

### Common audiences common-audiences

The **Common audiences** widget provides a list of the top five audiences activated across the destination account chosen at the top of the page, and the destination selected in the widget dropdown. The list of audiences is ordered according to how recently they were activated. The most recently activated audience is displayed at the top.

The AUDIENCE SIZE column provides the total profile count of each listed audience.

### Mapped audiences mapped-audiences

The Mapped audiences widget displays the total number of mapped audiences that can be activated to the destination selected at the top of the page.

Select **Audiences** to navigate to the Audiences dashboard Browse tab. This workspace displays a list of all the segment definitions for your organization.

### Mapped audience health mapped-audience-health

The widget provides a list of up to 20 mapped audiences whose total profile counts, as of the last daily snapshot, deviate by a factor of at least one standard deviation from the 30 days mean audience size mapped to that destination.

In brief, it provides a calculated metric for the dispersion of audience sizes from the mean over the last 30 days. It compares whether today’s audience size is outside of the historic standard deviation seen in the data over the past 30 days.

All audience sizes in the system are sorted from high to low audience size, as indicated in the LATEST SIZE column.

If your mapped audience profile count is outside one standard deviation from the average mapped profile size over the past 30 days, this indicates an anomaly in the system and it should be investigated.

If an audience within the Mapped audience health widget is deviating by a wide margin, you should refer to the audience size trend chart and locate the anomalous audience. The trend can provide further insight into your audience’s health.

NOTE
The default size of the Mapped audience health widget can obstruct the table information. Please modify the size of the widget to improve the legibility of your mapped audience names and column titles. See the modify dashboards documentation for guidance on
how to resize a widget
.
### Destinations count destinations-count

The Destinations count widget provides the total number of available endpoints where an audience can be activated and delivered within the system. This number includes both active and inactive destinations.

Below the total count, select **Destinations** to navigate to the destinations browse tab. This page lists all the destinations that you have established a connection with to date.

### Destination status destination-status

The Destination status widget displays the total number of enabled destinations as a single metric and uses a donut chart to illustrate the proportional difference between enabled and disabled destinations.

Individual counts for either enabled or disabled destinations are displayed in a dialog when the cursor hovers over the respective section of the donut chart.

### Active destinations by destination platform active-destinations-by-destination-platform

The widget provides a two column table to show a list of active destination platforms and the total number of active destinations for each destination platform. The list of destination platforms is ordered from high to low.

### Activated audiences across all destinations activated-audiences-across-all-destinations

The Activated audiences across all destinations widget provides the total number of audiences activated across all destinations in a single metric. This number is accurate to the most recent snapshot.

Select **Audiences** to navigate to the destinations Browse tab. This page provides a list of all enabled destinations and a variety of relevant metrics. See the documentation for more information on the [Browse tab](/en/docs/experience-platform/destinations/ui/destinations-workspace#browse).

Please see the prerequisites section for the [definitions of terms used](#prerequisites) in this description.

### Activated audiences activated-audiences

This widget provides a single metric for the total number of audiences activated to a destination.

Select **Audiences** to navigate to the details page of the destinations dashboard. The Activation data tab displays a list of audiences that have been mapped to the destination, including their start date and end date (if applicable), and other relevant information for the data export, such as export type, schedule, and frequency. To view the details about a particular audience, select its name from the Audience Name column.

This widget helps you to understand the value of your destinations based on the number of audiences activated at a glance. It also provides easy access to more detailed information for further analysis.

Please see the prerequisites section for the [definitions of terms used](#prerequisites) in this description.

## Next steps

By following this document you should now be able to locate the destinations dashboard and understand the metrics displayed in the available widgets. To learn more about working with destinations in Experience Platform, please refer to the [destinations documentation](/en/docs/experience-platform/destinations/home).

recommendation-more-help
