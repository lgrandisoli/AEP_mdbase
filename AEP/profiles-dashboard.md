---
title: "Profiles dashboard"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/dashboards/guides/profiles"
category: "guides"
topic: "experience-platform/dashboards-guide"
created_at: "2026-05-29T16:59:33.017956+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Dashboards Guide

# Profiles dashboard

Last update: May 13, 2026
- Topics:
- [Dashboards](#)

CREATED FOR:

- Developer
- User

The Adobe Experience Platform user interface (UI) provides a dashboard through which you can view important information about your Real-Time Customer Profile data, as captured during a daily snapshot. This guide outlines how to access and work with the Profiles dashboard in the UI and provides information regarding the metrics displayed in the dashboard.

Refer to the [Real-Time Customer Profile UI guide](/en/docs/experience-platform/profile/ui/user-guide) for an overview of the Profile features within the Experience Platform user interface.

## Profile dashboard data

The Profiles dashboard displays a snapshot of the attribute (record) data that your organization has within the Profile store in Experience Platform. The snapshot does not include any event (time series) data.

The attribute data in the snapshot shows the data exactly as it appears at the specific point in time when the snapshot was taken. In other words, the snapshot is not an approximation or sample of the data, and the Profile dashboard is not updating in real-time.

NOTE
Any changes or updates made to the data since the snapshot was taken will not be reflected in the dashboard until the next snapshot is taken.
## Explore the Profiles dashboard explore-dashboard

To navigate to the Profiles dashboard within the Experience Platform UI, select **Profiles** in the left rail, then select the **Overview** tab to display the dashboard.

NOTE
If your organization is new to Experience Platform and does not yet have active Profile datasets or merge policies created, the Profiles dashboard is not visible. Instead, the Overview tab displays links and documentation to help you get started with Real-Time Customer Profile.
### Modify the Profiles dashboard modify-dashboard

You can modify the appearance of the Profiles dashboard by selecting **Modify dashboard**. You can move, add, resize, and remove widgets from the dashboard, as well as to access the **Widget library** to explore available widgets, and create custom widgets for your organization.

To learn more, refer to the [modifying dashboards](/en/docs/experience-platform/dashboards/customize/modify) and [Widget library overview](/en/docs/experience-platform/dashboards/customize/widget-library) documentation.

### Add widgets add-widget

Select **Add widget** to navigate to the widget library and see a list of the available widgets to add to your dashboard.

From the widget library you can browse the selection of standard and custom audience widgets. For information on how to add widgets, please see the widget library documentation on how to [add a widget](/en/docs/experience-platform/dashboards/customize/widget-library#add-widgets).

### View SQL view-sql

You can view the SQL that generates the insights visualized on your dashboard with a toggle on the Overview workspace. You can take inspiration from the SQL of your existing insights to create new queries that derive unique insights from Experience Platform data based on your business needs. To learn more about this feature, see the [View SQL UI guide](/en/docs/experience-platform/dashboards/view-sql).

## Browse profiles browse-profiles

The Browse tab allows you to search and view the read-only profiles ingested into your organization. From here you can see important information belonging to the profile regarding their preferences, past events, interactions, and audiences.

## Profile details profile-details

To open the Profiles Detail workspace, select a Profile ID from the list.

The Profiles Detail workspace displays several pre-configured widgets that convey information specific to that profile. This information allows you to understand key attributes of the profile at a glance. You can also customize your Profiles Detail workspace by creating your own widgets. See the section on [how to add widgets](#add-widgets) for more details.

### Profile details widgets widgets

The pre-configured profile details widgets are as follows:

#### Customer profile customer-profile

The Customer profile widget displays the first and last name of the user associated with the profile, as well as their Profile ID. A profile ID is an auto-generated identifier associated with an identity type and represents a profile. To learn more about identities and identity namespaces, see the [identities overview](/en/docs/experience-platform/rtcdp/identity/identities-overview).

#### Basic attributes basic-attributes

The Basic attributes widget displays the most commonly used attributes that are used to define an individual profile.

#### Linked identities linked-identities

The Linked identities widget displays any other identities associated with the profile.

To view the identity details of the profile in greater depth and navigate to the Identities workspace, select **View identity graph**.

#### Channel preferences channel-preferences

The Channel preferences widget displays the channels of communication that the user has consented to receive communication from. A check mark indicates each channel that the user has consented to receive communication from.

Customer consent and contact preferences are complex topics. To learn how consent and context preferences can be collected, processed, and filtered in Experience Platform, you are recommended to read the following documents:

- To learn about the schema field groups required to collect consent data according to the Adobe standard , see the documentation on these Profile-enabled schema field groups. Consent and Preference Details IdentityMap (required if using the Experience Platform Web or Mobile SDK to send consent signals)
- To learn how to process customer consent and preference data using the Adobe standard, see the overview on consent processing in Experience Platform .
- A combined data governance and consent policy can be used to filter profiles for segmentation based on their consent preferences and your established organizational rules. To learn how to create and use these combined policies, see the user guide on managing data usage policies .

### Add widgets add-widgets

To add customized widgets to your Profiles Detail workspace, select **Customize profile details**.

You can now edit the workspace by resizing or relocating the widgets. Select **Add widget** to create a widget with custom attributes.

The widget creator appears. Enter a descriptive name for your widget in the Card title text field and select **Add attributes**.

A dialog appears that contains a visualization of the profile’s union schema. Use the search field or scroll to find the attributes that you want to report on with your widget. Select the checkbox for any attributes that you want to include. Select **Select** to continue the creation workflow.

TIP
A selection of the top level checkbox includes any child elements.
A preview of the completed widget is displayed on the canvas. Once you are happy with your chosen attributes, select **Save** to confirm your choices and return to the Profiles Detail workspace. The newly created widget is now visible in the workspace.

## Merge policies merge-policies

The metrics displayed in the Profiles dashboard are based on merge policies being applied to your Real-Time Customer Profile data. When data is brought together from multiple sources to create the customer profile, the data can contain conflicting values. For example, one dataset may list a customer as “single” while another dataset may list the customer as “married”. It is the job of the merge policy to determine which data to prioritize and display as part of the profile.

For more information on merge policies, including how to create, edit, and declare a default merge policy for your organization, refer to the [merge policies overview](/en/docs/experience-platform/profile/merge-policies/overview).

The dashboard automatically selects a merge policy to use. The applied merge policy can be changed using the dropdown menu next to the merge policy name.

NOTE
The dropdown menu shows only merge policies that use the
_xdm.context.profile
schema. However, if your organization has created multiple merge policies, it may mean that you need to scroll in order to view the complete list of available merge policies.
## Union schemas

The Union Schema dashboard displays the union schema for a specific XDM class. By selecting the **Class** dropdown, you can view the union schemas for different XDM classes.

Union schemas are composed of multiple schemas that share the same class and have been enabled for Profile. They enable you to see in a single view, an amalgamation of every field contained within each schema that shares the same class.

To learn more about [viewing union schemas within the Experience Platform UI](/en/docs/experience-platform/profile/union-schemas/union-schema#view-union-schemas), refer to the union schema UI guide.

## Widgets and metrics

The dashboard is composed of widgets, which are read-only metrics providing important information regarding your Profile data.

The date and time of the most recent snapshot is displayed at the top of the Overview tab next to the merge policy dropdown. All widget data is accurate as of that date and time. The timestamp of the snapshot is provided in UTC; it is not in the timezone of the individual user or organization.

## Default widgets default-widgets

A default widget load-out is provided for all new instances of Adobe Experience Platform that highlights the latest available insights from your data. The following widgets are pre-configured in your segments view from the outset. Full details on the purpose and function of the widgets can be found below.

- [Profile count](#profile-count)
- [Profile count change](#profile-count-change)
- [Profiles count change trend](#profiles-count-change-trend)
- [Profiles by identity](#profiles-by-identity)
- [Identity overlap](#identity-overlap)

NOTE
As of July 26th 2023, the Profiles, Audiences, and Destinations Overview dashboards have been reset to a new default widget load-out for all users who did not modify their views in the previous six months. Refer to the documentation in the
Destinations
and
Audiences
default widget sections for details on which widgets are included as part of the default widget load-outs. You can continue to customize your dashboard widgets as before.
## Customer AI widgets customer-ai-profiles-widgets

Customer AI is used to generate custom propensity scores such as churn and conversion for individual profiles at-scale. Customer AI does this by analyzing existing consumer Experience Event data to predict **churn or conversion propensity scores**. These high accuracy customer propensity models allow for more exact segmentation and targeting. The [distribution of scores](#customer-ai-distribution-of-scores) and [scoring summary](#customer-ai-scoring-summary) insights demonstrate the division in your audience. They highlight which profiles are the high/low/medium propensity and how they are distributed across your profile counts.

- [Customer AI scoring summary](#customer-ai-scoring-summary)
- [Customer AI distribution of scores](#customer-ai-distribution-of-scores)

### Customer AI distribution of scores customer-ai-distribution-of-scores

The Customer AI distribution of scores widget categorizes the total number of profiles by their propensity scores. The distribution of the profile count is determined by the AI model and the selected merge policy, then visualized in five percent increments that indicate their propensity. The count of profiles is provided along the Y-axis, and the propensity scores are provided along the X-axis.

NOTE
If the visualization is a conversion propensity score, the high scores show in green and the low scores in red. If you are predicting churn propensity this is flipped, the high scores are in red and the low scores are green. The medium bucket remains yellow regardless of what propensity type you choose.
The AI model that determines the propensity scores is chosen from the dropdown selector under the widget title. The dropdown contains a list of all configured Customer AI models. Select the appropriate AI model for your analysis from the list of available models. If no Customer AI model is available, a message within the widget directs you to configure at least one Customer AI model and provides a hyperlink to the Customer AI model configuration page. See the documentation for instructions on [how to configure a Customer AI instance](/en/docs/experience-platform/intelligent-services/customer-ai/user-guide/configure).

NOTE
Select the dropdown immediately below the overview tab to change the merge policy that determines which profiles are included in the analysis. See the section on
merge policies
for a brief description, or the
merge policy overview
for more details.
To navigate to the detailed insights page for the selected Customer AI model, select **View model details**.

The detailed model insights page appears.

More information on Customer AI can be found on the [discover insights UI guide](/en/docs/experience-platform/intelligent-services/customer-ai/user-guide/discover-insights).

### Customer AI scoring summary customer-ai-scoring-summary

This widget displays the total number of profiles scored, and categorizes them into buckets containing high, medium, and low propensity as green, yellow, and red respectively. A donut chart illustrates the proportional composition of profiles between high, medium, and low propensities. A profile qualifies for high propensity at over 75, medium propensity between 25 and 74, and low propensity under 24. A legend indicates the colour code and thresholds of propensities. Profile counts for the high, medium, and low propensities are displayed in a dialog when the cursor hovers over the respective section of the donut chart.

NOTE
If the visualization is a conversion propensity score, the high scores show in green and the low scores in red. If you are predicting churn propensity this is flipped, the high scores are in red and the low scores are green. The medium bucket remains yellow regardless of what propensity type you choose.
The dropdown menu underneath the widget title provides a list of all configured Customer AI models. Select the appropriate AI model for your analysis from the list of available models. If no Customer AI model is available, a message within the widget directs you to configure at least one Customer AI model and provides a hyperlink to the Customer AI model configuration page. See the documentation on [how to configure a Customer AI instance](/en/docs/experience-platform/intelligent-services/customer-ai/user-guide/configure) for detailed instructions.

NOTE
The total number of profiles calculated is dependent on the chosen merge policy. To change the merge policy used, select the dropdown immediately below the overview tab. See the section on
merge policies
for a brief description, or the
merge policy overview
for more details.
To navigate to the detailed insights page for the selected Customer AI model, select **View model details**. More information on Customer AI can be found on the [discover insights UI guide](/en/docs/experience-platform/intelligent-services/customer-ai/user-guide/discover-insights).

## Standard widgets standard-widgets

Adobe provides multiple standard widgets that you can use to visualize different metrics related to your Profile data. You can also create custom widgets to be shared with your organization using the Widget library. To learn more about creating custom widgets, begin by reading the [Widget library overview](/en/docs/experience-platform/dashboards/customize/widget-library).

To learn more about each of the available standard widgets, select the name of a widget from the following list:

- [Profile count](#profile-count)
- [Profile count trend](#profile-count-trend)
- [Profile count change](#profile-count-change)
- [Profiles count change trend](#profiles-count-change-trend)
- [Profiles count change trend by identity](#profiles-count-change-trend-by-identity)
- [Profiles by identity](#profiles-by-identity)
- [Identity overlap](#identity-overlap)
- [Single identity profiles](#single-identity-profiles)
- [Single identity profiles by identity](#single-identity-profiles-by-identity)
- [Unsegmented profiles](#unsegmented-profiles)
- [Unsegmented profiles change trend](#unsegmented-profiles-change-trend)
- [Unsegmented profiles by identity](#unsegmented-profiles-by-identity)
- [Audiences](#audiences)
- [Audiences mapped to destination status](#audiences-mapped-to-destination-status)
- [Audiences size](#audiences-size)
- [Audience overlap by merge policy](#audience-overlap-by-merge-policy)
- [Audience overlap report](#audience-overlap-report)

### Profile count profile-count

The **Profile count** widget displays the total number of merged profiles within the Profile store at the time the snapshot was taken. This number is the result of the selected merge policy being applied to your Profile data in order to merge profile fragments together to form a single profile for each individual.

See the [section on merge policies earlier in this document](#merge-policies) to learn more.

NOTE
The Profile count widget may show a different number than the profile count shown on the Browse tab in the Profiles section of the UI for multiple reasons. The most common reason for this difference is that the Browse tab references the total number of merged profiles based on your organization’s default merge policy, while the Profile count widget references the total number of merged profiles based on the merge policy that you have selected to view in the dashboard.
Another common reason is due to the differences between the time when the dashboard snapshot is taken and the time when the sample job is run for the Browse tab. You can see when the Profile count widget was last updated by looking at the timestamp on the widget. To learn more about how the sample job is triggered on the Browse tab, see the
profile count section in the Real-Time Customer Profile UI guide
.
### Profile count trend profile-count-trend

The Profile count trend widget uses a line graph to illustrate the trend in the total number of profiles contained in the system over time. This total number includes any profiles imported into the system since the last daily snapshot. The data can be visualized over 30 days, 90 days, and 12-month periods. The time period is chosen from a dropdown menu in the widget.

### Profile count change profile-count-change

The **Profile count change** widget displays the number of merged profiles added to the Profile store since the previous snapshot. This number is the result of the selected merge policy being applied to your Profile data in order to merge profile fragments together to form a single profile for each individual. You can use the dropdown selector to view the number of profiles added over the last 30 days, 90 days, or 12 months.

NOTE
The Profile count change widget reflects the number of profiles added
after
the initial profile ingestion and Profile store set-up. In other words, if your organization set up the Profile store and ingested 4,000,000 on Day 1, within 24 hours the dashboard would be available, however the Profile count change widget would be set to 0. This counting method is done to avoid a spike associated with the initial ingestion of profiles into the system. Over the next 30 days, your organization ingests an additional 1,000,000 profiles into the Profile store. After the next snapshot is taken, the Profile count change widget would show a total of 1,000,000 profiles added, while the Profile count widget would display 5,000,000 total profiles.
### Profiles count change trend profiles-count-change-trend

The **Profiles count change trend** widget displays the total number of merged profiles that have been added to the Profile store daily over the last 30 days, 90 days, or 12 months. This number is updated each day when the snapshot is taken, therefore if you were to ingest profiles into Experience Platform, the number of profiles would not be reflected until the next snapshot is taken. The count of profiles added is the result of the selected merge policy being applied to your Profile data in order to merge profile fragments together to form a single profile for each individual.

To learn more, refer to the [section on merge policies earlier in this document](#merge-policies).

The **Profiles count change trend** widget displays a ‘captions’ button in the top right of the widget. To open the automatic captions dialog, select **Captions**.

A machine learning model automatically generates captions for describing the key trends and important events by analyzing the chart and the data. Annotations are added to the chart based on the captions. Select a caption to focus on its corresponding annotation.

### Profiles count change trend by identity profiles-count-change-trend-by-identity

This widget filters the profile count based on a selected source identity and merges policy, then illustrates the change in number for various periods using a line graph. The merge policy is selected from the overview dropdown at the top of the page, the source identity, and time period are selected from the widget dropdown menus. The trend can be visualized over 30 days, 90 days, and 12-month periods.

This widget helps you to manage your destination activation needs by demonstrating the growth pattern of profiles filtered by a required identity.

### Profiles by identity profiles-by-identity

The **Profiles by identity** widget displays the breakdown of identities across all of the merged profiles in your Profile store. The total number of profiles by identity (in other words, adding together the values shown for each namespace) may be higher than the total number of merged profiles because one profile could have multiple namespaces associated with it. For example, if a customer interacts with your brand on more than one channel, multiple namespaces would be associated with that individual customer.

To learn more, refer to the [section on merge policies earlier in this document](#merge-policies).

To open the automatic captions dialog, select **Captions**.

A machine learning model automatically generates data insights by analyzing the overall distribution and key dimensions of the data.

To learn more about identities, refer to the [Adobe Experience Platform Identity Service documentation](/en/docs/experience-platform/identity/home).

### Identity overlap identity-overlap

The **Identity overlap** widget uses a Venn diagram, or set diagram, to display the overlap of profiles in your Profile store that contain the two selected identities.

Use the widget dropdown menus to select the identities that you wish to compare. Circles display the relative total count of profiles that contain each identity. The number of profiles containing both identities is represented by the size of the overlap between the circles. If a customer interacts with your brand on more than one channel, multiple identities would be associated with that individual customer. In this situation it is likely that your organization has multiple profiles containing fragments from more than one identity.

For more information on profile fragments, refer to the section on [profile fragments vs merged profiles](/en/docs/experience-platform/profile/home#profile-fragments-vs-merged-profiles) in the Real-Time Customer Profile overview.

To learn more about identities, refer to the [Adobe Experience Platform Identity Service documentation](/en/docs/experience-platform/identity/home).

### Single identity profiles single-identity-profiles

The Single Identity Profiles widget provides a count of your organization’s profiles that only have one type of ID type that creates their identity. This ID type can either be an email or ECID. The profile count is generated from the data contained in the most recent snapshot.

### Single identity profiles by identity single-identity-profiles-by-identity

This widget uses a bar chart to illustrate the total number of profiles that are identified with only a single unique identifier. The widget supports up to five of the most commonly occurring identities.

To see a dialog detailing the total count of profiles for an identity, use the cursor to hover over individual bars.

### Unsegmented profiles unsegmented-profiles

The Unsegmented Profiles widget provides the total number of all profiles not attached to any audience. The number generated is accurate as of the last snapshot and represents the opportunity for profile activation across your organization. It also indicates the opportunity to expunge profiles that do not provide adequate ROI.

### Unsegmented profiles change trend unsegmented-profiles-change-trend

The Unsegmented profiles change trend widget uses a line graph to illustrate the number of profiles added since the last daily snapshot that are not attached to any audience. The change-trend of profiles not attached to any audience can be visualized over 30 days, 90 days, and 12 month periods. The time period is chosen from a dropdown menu in the widget. The profile count is reflected on the y-axis and time on the x-axis.

### Unsegmented profiles by identity unsegmented-profiles-by-identity

NOTE
The Unsegmented profiles by identity widget have been deprecated as of October 2022 and is no longer available.
### Audiences audiences

This widget provides the total number of audiences that are ready to be activated, according to the chosen merge policy applied to your profile data.

Select **Audiences** to navigate to the Audiences dashboard Browse tab. From there, you can see a list of all the segment definitions for your organization.

### Audience overlap report audience-overlap-report

This widget tabularizes the data overlap from all available audiences filtered by merge policy. A list of five audiences ranked from highest to lowest overlap percentages is provided for the merge policy chosen from the dropdown menu at the top of the screen. The two analyzed audiences are listed in the AUDIENCE A NAME and AUDIENCE B NAME columns. The percentage overlap is provided in the third column accurate to twelve decimal places.

The audience overlap report helps you to build new, high-performance audiences. Observing high percentage overlaps enables you to suppress audiences and prevent sending the same audience to different destinations. They also help you identify hidden insights that might help with better segmentation. Low percentage overlap helps to locate unique profiles to pursue.

Select **View more** to open a full-screen dialog that contains more audience overlap data.

The Audience overlap report dialog appears. This dialog can contain up to 50 rows of audience overlap analyses broken down into six columns. To remove or add columns from the table, select the settings icon ( ).

NOTE
To change the ranking of results between highest to lowest or lowest to highest, select the
Overlapping
column header.
To download the entire report in PDF format, select the options menu (**...**) followed by **Download**.

To open a Venn diagram of the overlap analysis, select a row from the report. To see the profile count in a dialog, hover over a section of the Venn diagram.

Select **Close** to return to the Profiles dashboard.

### Audiences mapped to destination status audiences-mapped-to-destination-status

The Audiences mapped to destination status widget displays the total number of both mapped and unmapped audiences in a single metric and uses a donut chart to illustrate the proportional difference between their totals. The numbers calculated are dependent on the chosen merge policy.

Individual counts for either mapped or unmapped audiences are displayed in a dialog when the cursor hovers over the respective section of the donut chart.

### Audiences size audiences-size

The Audiences size widget provides a two-column table that lists the names of up to 20 audiences and the total number of profiles contained in each audience. The list is ordered from high to low according to the total number of profiles contained within the audience. The total audience size count is dependent on the merge policy applied.

To see comprehensive information on an audience, select an audience name from the list provided to navigate to the Audiences Detail page. Also, by selecting **View all audiences** from the end of the widget, you can navigate to the Audiences Browse tab to find any existing audience.

More information about audience details can be found in the [Audience Portal documentation](/en/docs/experience-platform/segmentation/ui/audience-portal).

### Audience overlap by merge policy audience-overlap-by-merge-policy

This widget uses a Venn diagram to display the overlap of two selected audiences. The merge policy is chosen from the overview dropdown at the top of the page and the audiences for analysis are selected from two dropdown menus within the widget. The total number of profiles contained within the relevant segment definition can be seen by hovering over a circle or the intersection.

As the widget displays the visual crossover of segment definitions, you can optimize your segmentation strategy by studying similarities between your segment definitions.

## Next steps

By following this document, you should now be able to locate the profiles dashboard and understand the metrics displayed in the available widgets. To learn more about working with Profile data in the Experience Platform UI, refer to the [Real-Time Customer Profile UI guide](/en/docs/experience-platform/profile/ui/user-guide).

recommendation-more-help
