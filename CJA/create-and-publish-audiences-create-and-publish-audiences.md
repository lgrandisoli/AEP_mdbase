---
title: "Create and publish audiences create-and-publish-audiences"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/audiences/publish"
category: "other"
topic: "analytics-platform/using/cja-components/audiences"
created_at: "2026-06-02T19:07:08.636549+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create and publish audiences create-and-publish-audiences

Last update: May 19, 2026
- Topics:
- [Audiences](#)

CREATED FOR:

- User

This topic discusses how to create and publish audiences identified in Customer Journey Analytics to [Real-Time Customer Profile](/en/docs/experience-platform/profile/home) in Adobe Experience Platform for customer targeting and personalization.

Read this [overview](/en/docs/analytics-platform/using/cja-components/audiences/audiences-overview) to familiarize yourself with the concept of Customer Journey Analytics audiences.

## Create and publish an audience create

- To create and publish an audience, do one of the following: table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto Creation method Details From within the Published audiences interface Select Components > Published audiences from the main Customer Journey Analytics menu. The Audiences interface displays. Select Create audience and the Audience builder opens. From a visualization in Analysis Workspace Many visualizations in Analysis Workspace allow you to create an audience using the context menu. For example, you can select Create audience from the context menu of an item in a Freeform table or a node in Journey canvas . Using this method pre-populates the segment in the Audience builder with the dimension or dimension item that you selected. The following visualizations allow you to create an audience using the right-click menu: Cohort table Fallout Flow Freeform table Journey canvas Map Note: This visualization is in the Limited Testing phase of release and might not be available yet in your environment. Venn Note: Audiences cannot include calculated metrics. If you try to create an audience that contains a calculated metric, the calculated metric is not included in the audience definition. From the segment creation/editing UI Check the box that says Create an audience from this segment . Using this method pre-populates the segment. See Create segments for more information.
- Build the audience using the Audience builder .
- Interpret the data using the Date preview panel.
- Select View sample IDs to view a sample of IDs in this audience. In the Sample IDs dialog you can use Search sample IDs to search for sample IDs.
- Double-check your audience configuration and select Publish . You receive a confirmation message that the audience is published. Publication takes only a minute or two for this audience to show up in Experience Platform.
- Select View audience in AEP within the same message and you are taken to the Segment UI in Adobe Experience Platform. See below for more information.

## Audience builder

Configure these settings to define or update your audience.

Setting
Description
Select a data view to use for the audience creation.
Name
The name of the audience. For example,
Really Interested in Potential Car Buyers
Tags
Any tags that you want to assign to the audience for organizational purposes. You can select one or more pre-existing tags or enter a new one.
Description
A description of the audience, to differentiate it from others. For example,
Build an audience of really interested potential car buyers
Refresh frequency
The frequency at which you want to refresh the audience.

You can choose between

- One time audience: an audience (default) that needs no refreshing. For example, this option could be helpful for specific, one-time campaigns. You have to specify a One time date range . You can use to enter a date range.
- A refreshing audience. You can select from the following options: Every 4 hour s: an audience that refreshes every 4 hours. Daily : an audience that refreshes daily Weekly : an audience that refreshes weekly. Monthly : an audience that refreshes monthly For refreshing audiences, you have to specify: Refresh lookback window . Define the number of lookback days from today that an audience is evaluated. You can select from options or define a Custom time. The maximum is 90 days. Expiration date : Define when the audience stops refreshing. You can use to select a date. The default is 1 year from the creation date. Expiring audiences are treated similarly to expiring scheduled reports. The admin gets an email a month before the audience expires. Note that there is a limit of 75 to 150 audience refreshes, depending on your Customer Journey Analytics entitlement.

Filter
Filters are the main input to the audience. Drag and drop one or more segments from the left **Segment** panel on to the Segment area. You can use the *Search segments* to search for segments. You can add up to 20 segments. Segments can be joined with **And** or **Or** operators.

When creating an audience from a visualization in Analysis Workspace (such as a freeform table or Journey canvas), any segments applied to the panel or to the column are preserved. You can remove any segments that are automatically applied.

Data preview
Select
to show or hide the
Data preview
for the selected date range.
## Data preview

The Data preview panel provides the following information.

Element
Description
Total people
A summary number of the total number of people in this audience. The maximum size is 20 million people. If your audience exceeds 20 million people, you must reduce the audience size before you can publish.
Audience size limit
Visualization to show how far from the 20 million limit this audience is.
Estimated audience return
You can use this value to retarget people in this audience that come back to your site, mobile app or other channel.

You can select the time frame (**Next 7 days**, **Next 2 weeks**, or **Next month**) for the estimated number of customers who may return.

Estimated to return
This number gives you an estimated number of returning customers over the time frame that you selected. This number is predicted using the historical churn rate for this audience.
Preview metrics
You can select a specific metric to see how data for that metric is based on the audience you define. Each Preview metric displays a total for the metric based on the audience. And a percentage of the audience based metric from the overall total of the metric, as defined by the data view. For example, 381 people (the metric you selected) are the result of your audience definition, which is 5% of the total people available in the data view. You can select any metric that is available in your data view.
Namespaces included
The specific namespaces that are associated with the people in your audience. Examples include ECID, CRM ID, email addresses, etc.
Sandbox
The
Experience Platform sandbox
in which this audience resides. When you publish this audience to Platform, you can only work with the audience within the confines of this sandbox.
## What happens after an audience is created and published? after-audience-created

After you create and publish an audience in Customer Journey Analytics, the audience is available in Experience Platform and can be viewed in the [Audience portal](/en/docs/experience-platform/segmentation/ui/audience-portal). With the audience available in Experience Platform, it can be used in other Experience Platform applications, such as Adobe Journey Optimizer.

An Adobe Experience Platform streaming segment is created only if your organization is set up for streaming segmentation.

Consider the following when working with audiences that are published from Customer Journey Analytics to Experience Platform:

- The audience in Experience Platform shares the same name and description as the Customer Journey Analytics audience. The name is appended with the Customer Journey Analytics audience ID to ensure that the audience is unique.
- Any changes made to the name or description of the audience in Customer Journey Analytics are reflected in Experience Platform.
- If an audience is deleted in Customer Journey Analytics, the audience continues to be available in Experience Platform until the profile membership of the audience expires. The profile membership expires after 420 days for one-time audiences and after 16 days for recurring audiences.

## Latency considerations latency

At several points prior to, during, and after audience publishing, latencies can occur. Here is an overview of possible latencies.

Latency point
Latency duration
Not shown
Adobe Analytics to Analytics source connector (A4T)
Up to 30 minutes
1
Data ingestion into Data Lake (from Analytics source connector or other sources)
Up to 90 minutes
2
Data ingestion from Experience Platform Data Lake into Customer Journey Analytics
Up to 90 minutes
3
Audience publishing to Real-Time Customer Profile, including automatic creation of the streaming segment, and allowing the segment to be ready to receive the data.
A few seconds
4
Refresh frequency for audiences
- One-time refresh (latency of less than 5 minutes)
- Refresh every 4 hours, daily, weekly, monthly (latency goes hand in hand with the refresh rate)

5
Creating destination in Adobe Experience Platform: Activating the new segment
1-2 hours
## Use Customer Journey Analytics audiences in Experience Platform audiences-aep

Customer Journey Analytics takes all the namespace and ID combinations from your published audience and streams them into Real-Time Customer Data Platform. Customer Journey Analytics sends the audience to Experience Platform with the primary identity set, according to what was selected as the Person ID when the connection was configured.

Real-Time Customer Data Platform then examines each namespace/ID combination and looks for a profile that it may be part of. A profile is basically a cluster of linked namespaces, IDs and devices. If it finds a profile, it adds the namespace and ID to the other IDs in this profile as a segment membership attribute. For example, [user@adobe.com](mailto:user@adobe.com) can be targeted across all their devices and channels. If a profile is not found, a new one is created.

To view Customer Journey Analytics audiences in Platform:

- Expand Customer in the left panel, then select Audiences .
- Select the Browse tab.
- To locate the audience that you published from Customer Journey Analytics, do any of the following: Sort the table by the Origin column to view audiences that show Customer Journey Analytics as the origin. Filter on Origin and select Customer Journey Analytics . Use the search field.

For more information about using Audiences in Platform, see the [Audiences](/en/docs/experience-platform/segmentation/ui/segment-builder) section in the [Segment Builder UI guide](/en/docs/experience-platform/segmentation/ui/segment-builder) in the Experience Platform documentation.

### Understand discrepancies in audience counts

Discrepancies in audience counts may occur between Customer Journey Analytics and Real-Time Customer Data Platform.

#### Estimated versus deterministic counts

The methodology by which audience membership numbers are being calculated differs between the two apps, as described below.

- **Customer Journey Analytics**: The **Total People** metric in Customer Journey Analytics is an estimated value. This means that the count is an estimate based on the rules of the audience and it can change between refresh intervals.
- **Real-Time Customer Data Platform**: The count in Real-Time Customer Data Platform is deterministic, based on daily evaluation jobs, and fixed at the time the audience finishes publishing into the audience portal.

#### Publishing interval and rate

Audiences publish to Real-Time Customer Data Platform at a rate of 1500 records per second (RPS). For example, an audience of 20 million members will take approximately 3.7 hours to fully publish (20M / 1500 RPS / 3600 seconds per hour). During this time, differences in audience membership between the two apps are likely.

#### Profile fragmentation

If profiles imported from Customer Journey Analytics already exist in Real-Time Customer Data Platform, they are not counted as new profiles. This can lead to lower-than-expected profile counts in Real-Time Customer Data Platform.

#### Batch versus streaming audiences

Customer Journey Analytics audiences are not included in the daily batch evaluation job and remain fixed until the next publish interval. In contrast, other batch audiences in Real-Time Customer Data Platform are re-evaluated every 24 hours.

### Key takeaways to remember

- **Estimated counts in Customer Journey Analytics**: Understand that the **Total People** count in Customer Journey Analytics is an estimate and can vary due to streaming data and identity behaviors.
- **Deterministic counts in Real-Time Customer Data Platform**: The count in Real-Time Customer Data Platform is fixed and does not change until the next publish interval.
- **Profile Fragmentation**: Be aware that existing profiles in Real-Time Customer Data Platform may not contribute to new profile counts when importing from Customer Journey Analytics.

By clearly differentiating these aspects, you can better understand and manage your audience data across Customer Journey Analytics and Real-Time Customer Data Platform.—>

## FAQs faq

Frequently asked questions on audience publishing.

What happens if a user is no longer a member of an audience in Customer Journey Analytics?
In this case, an exit event is sent to Experience Platform from Customer Journey Analytics.
What happens if you delete an audience in Customer Journey Analytics?
When a Customer Journey Analytics Audience is deleted, that audience is no longer shown in the Experience Platform UI. However, profiles associated with that audience are not deleted in Experience Platform.
If a corresponding profile does not exist in Real-Time Customer Data Platform, is a new profile created?
Yes, it will.
Does Customer Journey Analytics send the audience data over as pipeline events or as a flat file that also goes to the data lake?
Customer Journey Analytics streams the data into Real-Time Customer Data Platform via pipeline, and this data is also collected into a system dataset in the data lake.
What identities does Customer Journey Analytics send over?
Whichever identity/namespace pairs that were specified in the
Connection setup
. Specifically, the step when a user selects the field they want to use as the Person ID.
Which ID is chosen as the primary identity?
See above. Only one identity per Customer Journey Analytics person is sent.
Does Real-Time Customer Data Platform process the Customer Journey Analytics messages as well? Can Customer Journey Analytics add identities to a profile identity graph through audience sharing?
No. Only one identity per person is sent, so there would be no graph edges for Real-Time Customer Data Platform to consume.
What time of day do daily, weekly, and monthly refreshes occur? What day of the week do weekly refreshes occur?
The timing of the refresh is based on when the original audience was published and anchors to that time of day (and day of week or month).
Can you configure the daily, weekly, and monthly time of refresh?
No, users cannot configure the time of refresh.
## Next steps

- To manage this audience, go to the [Management UI](/en/docs/analytics-platform/using/cja-components/audiences/manage).

recommendation-more-help
