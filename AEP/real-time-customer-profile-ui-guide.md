---
title: "Real-Time Customer Profile UI guide"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/profile/ui/user-guide"
category: "guides"
topic: "experience-platform/real-time-customer-profile-guide"
created_at: "2026-05-29T16:55:51.895707+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Real-Time Customer Profile Guide

# Real-Time Customer Profile UI guide

Last update: May 23, 2026
- Topics:
- [Profiles](#)

CREATED FOR:

- User

Real-Time Customer Profile creates a holistic view of each of your individual customers, combining data from multiple channels including online, offline, CRM, and third-party data. This document serves as a guide for interacting with Real-Time Customer Profile data in the Adobe Experience Platform user interface (UI).

## Getting started

This UI guide requires an understanding of the various Experience Platform services involved with managing Real-Time Customer Profiles. Before reading this guide, or working in the UI, please review the documentation for the following services:

- [Real-Time Customer Profile overview](/en/docs/experience-platform/profile/home): Provides a unified, real-time consumer profile based on aggregated data from multiple sources.
- [Identity Service](/en/docs/experience-platform/identity/home): Enables Real-Time Customer Profile by bridging identities from disparate data sources as they are ingested into Experience Platform.
- [Experience Data Model (XDM)](/en/docs/experience-platform/xdm/home): The standardized framework by which Experience Platform organizes customer experience data.

## Overview

In the Experience Platform UI, select **Profiles** in the left navigation to open the **Overview** tab displaying the profile dashboard.

NOTE
If your organization is new to Experience Platform and does not yet have active Profile datasets or merge policies created, the Profiles dashboard is not visible. Instead, the Overview tab displays links and documentation to help you get started with Real-Time Customer Profile.
### Profile dashboard profile-dashboard

The profile dashboard outlines key metrics related to your organization’s profile data.

To learn more, visit the [profile dashboard guide](/en/docs/experience-platform/dashboards/guides/profiles).

## Browse tab

On the **Browse** tab you can view your profiles either in a **card** view or a **table** view by selecting the toggle.

Additionally, you can browse your profiles using a merge policy or look up specific profiles using an identity namespace and value.

### Browse by Merge policy

The **Browse** tab is set to the default merge policy for your organization by default. To choose a different merge policy, select the X beside the merge policy name and then use the selector to open the **Select merge policy** dialog.

NOTE
If there is no merge policy selected, use the selector button next to the
Merge policy
field to open the selection dialog.
To choose a merge policy from the **Select merge policy** dialog, select the radio button beside the policy name and then use **Select** to return to the Browse tab. You can then select **View** to refresh the sample profiles and see a sampling of profiles with the new merge policy applied.

The profiles that are shown represent a sample of up to 20 profiles from your organization’s Profile store, after the selected merge policy has been applied. The sample profiles for the selected merge policy are refreshed when new data is added to your organization’s Profile store.

To view the details of one of the sample profiles, select the **Profile ID**. For more information, see the section later in this guide on [viewing profile details](#profile-detail).

To learn more about merge policies and their role within Experience Platform, see the [merge policies overview](/en/docs/experience-platform/profile/merge-policies/overview).

### Browse by Identity browse-identity

On the **Browse** tab, you can use an identity namespace in order to look up a specific profile by an identity value. Browsing by an identity requires you to provide a merge policy, an identity namespace, and an identity value.

If necessary, use the **Merge policy** selector to open the **Select merge policy** dialog and choose the merge policy that you would like to use.

Then use the **Identity namespace** selector to open the **Select identity namespace** dialog and choose the namespace by which you would like to search. If your organization has many namespaces, you can use the search bar in the dialog to begin typing the name of a namespace.

You can select a namespace to view additional details or select the radio button to choose a namespace. You can then use **Select** to continue.

After selecting an Identity namespace and returning to the Browse tab, you can enter an **Identity value** related to the namespace that you selected.

NOTE
This value is specific to an individual customer profile and must be a valid entry for the namespace provided. For example, selecting the identity namespace “Email” would require an identity value in the form of a valid email address.
Once a value has been entered, select **View** and a single profile matching the value is returned. Select the **Profile ID** to view a profile.

## View profile view-profile

After selecting a **Profile ID**, the **Detail** tab opens. The profile information displayed on the **Detail** tab has been merged together from multiple profile fragments to form a single view of the individual customer. This includes customer details such as basic attributes, linked identities, and channel preferences.

Additionally, you can view other details about profiles such as its [attributes](#attributes), [events](#events), and [audience membership](#audience-membership).

### Details tab profile-detail

The **Details** tab provides more detailed information about the selected profile. The details tab is separated into various sections, depending if you’re in card or graph view. For card view, the customer profile insights, AI insight widgets, customizable widgets, and auto-classified widgets are displayed while for graph view, the profile attributes and experience events sections are displayed.

Additionally, you can toggle whether the AI-generated insights are displayed, show the details for hub compared to edge, as well as choosing between card or graph views.

#### Customer profile insights customer-profile-insights

The **Customer profile insights** section displays a brief introduction to the profile’s attributes. This includes the profile ID, email, phone number, gender, date of birth, as well as the identities and audience memberships of the profile.

#### AI insight widgets ai-insight-widgets

IMPORTANT
If you are a Healthcare Shield customer, you will
not
be able to use AI insight widgets.
The **AI insight widgets** section displays widgets that are generated by AI. These widgets provide quick insights to the profile, based off of the profile data including demographics (such as age, gender, or location), user behaviors (such as purchase history, website activity, or social media engagement), as well as psychographics (such as interests, preference, or lifestyle choices). All the AI widgets use data that **already** exists in the profile.

#### Customizable widgets customizable-widgets

The **Customizable widgets** section displays widgets that you can customize to match your business needs. You can group attributes into separate widgets, remove unwanted widgets, or adjust the widgets’ layout.

The default fields shown can also be changed at an organizational-level to display preferred Profile attributes. To learn more about customizing these fields, including step-by-step instructions for adding and removing attributes and resizing dashboard panels, please read the [profile detail customization guide](/en/docs/experience-platform/profile/ui/profile-customization).

You can also choose to toggle between viewing the attribute names as their display names and their field path names. To switch between these two displays, select the **Show display names** toggle.

#### Auto-classified widgets auto-classified-widgets

The **Auto-classified widgets** section displays widgets that leverage the union schema to determine the source field groups an attribute belongs to, providing clearer context on where the data originates from. You can use the search bar to more easily look for keywords within your widgets.

These widgets combine both event data (with the Experience events widget) and attribute data, letting you have a unified view of your profile. You can use these widgets to explore the structure of your profile’s data to better structure your [customizable widgets](#customizable-widgets).

NOTE
If there are multiple source field groups, the widgets will only use
one
of the available options.
#### Profile attributes profile-attributes

The **Profile attributes** section displays a hierarchical graph representation of the profile data. In this view, the central node represents the profile itself, secondary nodes represent the field groups, and the remaining nodes represent properties within each field group.

Within the graph view, you can drag and drop the nodes to re-arrange the node order, collapse and expand the nodes to see more details about the attributes, search and filter by attribute, as well as zoom in and out to better view the attribute details.

#### Experience events experience-events

The **Experience events** section displays a timeline of experience events that contain the profile. By default, this section displays experience events within the last 48 hours. However, you can set the date range for up to 30 days.

If you select **View event**, you can see the event attributes linked to the selected event. These details include the path, attribute, display name, and the value.

### Attributes tab attributes

The **Attributes** tab provides a list view summarizing all of the attributes related to a single profile, after the specified merge policy has been applied.

These attributes can also be viewed as a JSON object by selecting to **View JSON**. This is helpful for any users wishing to better understand how the profile attributes are ingested into Experience Platform.

To view the attributes that are available on the Edge, select **Edge** on the data location selector.

For more information on edge profiles, please read the [edge profiles documentation](/en/docs/experience-platform/profile/edge-profiles).

### Events tab events

NOTE
Display of the events can be delayed by up to 15 minutes.
By default, **Events** tab contains data from the past 48 hours with the 100 most recent ExperienceEvents associated with the customer. This data could include email opens, cart activities, and page views. You can also set the date range for up to 30 days. Selecting **View all** for any individual event provides additional fields and values captures as part of the event.

Events can also be viewed as a JSON object by selecting to **View JSON**. This is helpful for understanding how events are captured in Experience Platform.

### Audience membership tab audience-membership

The **Audience membership** tab displays a list with the name and description of audiences to which the individual customer profile currently belongs. This list is updated automatically as the profile qualifies or expires from audiences. The total count of audiences for which the profile is currently qualified is shown on the right-hand side of the tab.

For more information about segmentation in Experience Platform, please refer to the [Adobes Experience Platform Segmentation Service documentation](/en/docs/experience-platform/segmentation/home).

To view the audience membership of the profiles that are available on the Edge, select **Edge** in the data location selector. More information about edge segmentation can be found in the [edge segmentation guide](/en/docs/experience-platform/segmentation/methods/edge-segmentation).

## Merge policies

From the main **Profiles** menu, select the **Merge Policies** tab to view a list of merge policies belonging to your organization. Each listed policy displays its name, whether or not it is the default merge policy, and the schema class that it applies to.

For more information on merge policies, see the [merge policies overview](/en/docs/experience-platform/profile/merge-policies/overview).

## Union schema union-schema

From the main **Profiles** menu, select the **Union Schema** tab to view available union schemas for your ingested data. A union schema is an amalgamation of all Experience Data Model (XDM) fields under the same class, whose schemas have been enabled for use in Real-Time Customer Profile.

For more information on union schemas, please visit the [union schema UI guide](/en/docs/experience-platform/profile/union-schemas/union-schema).

## Computed attributes computed-attributes

From the main **Profiles** menu, select the **Computed attributes** tab to view a list of computed attributes that belong to your organization.

For more information on computed attributes, please read the [computed attributes overview](/en/docs/experience-platform/profile/computed-attributes/overview). For more information on how to use computed attributes within the Experience Platform UI, please read the [computed attributes UI guide](/en/docs/experience-platform/profile/computed-attributes/ui).

## Next steps

By reading this guide, you know how to view and manage your organization’s profile data using the Experience Platform UI. For information on how to work with profile data using Experience Platform APIs, please refer to the [Real-Time Customer Profile API guide](/en/docs/experience-platform/profile/api/overview).

recommendation-more-help
