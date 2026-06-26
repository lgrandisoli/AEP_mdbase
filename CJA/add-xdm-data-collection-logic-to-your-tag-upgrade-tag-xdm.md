---
title: "Add XDM data collection logic to your tag upgrade-tag-xdm"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-tags/cja-upgrade-tag-xdm"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:50.583884+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Add XDM data collection logic to your tag upgrade-tag-xdm

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

After [creating the tag and adding the Web SDK extension](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/create-tags/cja-upgrade-tag-property), you must configure it with data elements and rules, according to how you want to track your site and send data to Adobe Experience Platform. After you configure data elements and rules for your tag, you can build and publish it.

## Configure data elements

Data elements are the building blocks for your data dictionary (or data map). Use data elements to collect, organize, and deliver data across marketing and ad technology. You set up data elements in your tag that read from your data layer and can be used to deliver data into Adobe Experience Platform. (For more information about data elements, see [Data elements](/en/docs/experience-platform/tags/ui/data-elements) in the Tags Documentation.)

The following sections describe suggested data elements and other common data elements that you can configure.

There are various types of data elements. Two common data elements that you might want to configure are: one that captures the page name that persons are viewing on your site, and another that captures the Experience Cloud ID of each person who visits your site.

After you configure these two data elements, you can configure additional data elements for the specific data you want to capture.

Finally, after you define all your desired data elements, you need to assign the data elements to the [schema you created](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create) earlier. To do this, you define an XDM data element, which provides a representation of your XDM schema.

### Create suggested data elements

The following sections describe how to create common data elements that apply to most organizations.

#### Page name data element

A common data element that applies to most organizations is a data element that captures the page name that persons are viewing.

To create a page name data element:

- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- On the Tag Properties page, select your newly created tag from the list of properties to open it.
- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog, specify the following information: Name : The name of your data element. For example Page Name . Extension : Select Core from the list. Data Element Type : Select Page Info from the list. Attribute : Select Title from the list. Alternatively you could have used the value from a variable of your data layer, for example pageName and the JavaScript Variable data element type to define the data element.
- Select Save . You now want to set up a data element referencing the Experience Cloud ID that is automatically provided by the Adobe Experience Platform Web SDK and available through the Experience Cloud ID Service extension.
- Continue with ECID data element .

#### ECID data element

A common data element that applies to most organizations is a data element that captures the Experience Cloud ID of each person who visits your site.

To create an ECID data element:

- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- Select your newly created tag from the list of Tag Properties to open it.
- (Conditional) Install the Experience Cloud ID Service extension if it is not already installed: Select Extensions in the left rail. The Installed tab is selected by default. If the Experience Cloud ID Service tile is listed, skip to Step 5. If the Experience Cloud ID Service tile is not listed, select the Catalog tab. In the search field, search for Experience Cloud ID Service , then select the tile when it appears Select Install > Save .
- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog, specify the following information: Name : The name of your data element. For example ECID . Extension : Select Experience Cloud ID Service from the list. Data Element Type : Select ECID from the list.
- Select Save .
- Continue with Create additional data elements .

### Create additional data elements

Create a data element for each type of data that you want to collect. Use the same process described in [Page name data element](#page-name-data-element) and [ECID data element](#ecid-data-element) to create each additional data element.

The data elements that you create should have a correlating field in your schema.

Common data elements vary depending on industry and business requirements. Consider the following common data elements, organized by industry:

**Retail data elements**

- Products
- Cart additions
- Checkouts

**Financial data elements**

- Transaction ID
- Transaction date
- Service type

**Healthcare data elements**

- Provider ID
- Visit date
- Treatment type

After you create all the data elements required by your organization for your implementation, continue with [XDM object data element](#xdm-object-data-element).

### XDM object data element

Finally, you now want to map any data element that you created to the [schema you created](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create) earlier. To do this, define an XDM object data element that provides a representation of your XDM schema.

To define an XDM object data element:

- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- Select your newly created tag from the list of Tag Properties to open it.
- Select Data Elements in the left rail.
- Select Add Data Element .
- In the Create Data Element dialog, specify the following information: Name : The name of your data element. For example XDM - Page View . Extension : Select Adobe Experience Platform Web SDK from the list. Data Element Type : Select XDM Object from the list. Sandbox : Select your sandbox from the list. Schema : Select your schema from the list.
- Map the identification > core > ecid attribute, defined in your schema, to the ECID data element. Select the cylinder icon to easily pick the ECID data element from your list of data elements.
- Map the web > webPageDetails > name attribute, defined in your schema, to the Page Name data element.
- Select Save .
- Continue with Configure rules .

## Configure rules

Tags in Adobe Experience Platform follow a rule-based system. They look for user interaction and associated data. When the criteria outlined in your rules are met, the rule triggers the extension, script, or client-side code you identified. You can use rules to send data (like an XDM object) into Adobe Experience Platform using the Adobe Experience Platform Web SDK extension.

To define a rule:

NOTE
The following steps are an example of defining a rule that sends XDM data, containing values from other data elements, to Adobe Experience Platform.
You can use rules in various ways in your tag to manipulate variables (using your data elements).
See
Rules
for more information.
- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- Select your newly created tag from the list of Tag Properties to open it.
- Select Rules in the left rail.
- Select Add Rule .
- In the Create Rule dialog, specify the following information: Name : The name of the rule. For example Page View . Events : Select + Add . Then, in the Event Configuration dialog, specify the following information. When you are finished, select Keep Changes . Extension : Select Core from the list. Event Type : Select Window Loaded from the list. Actions : Select + Add . Then, in the Action Configuration dialog, specify the following information. When you are finished, select Keep Changes . Extension : Select Adobe Experience Platform Web SDK from the list. Action Type : Select Send event from the list. Type : Select Web Webpagedetails Page Views from the list. XDM data : Select the cylinder icon, then select XDM - Page View from the list of data elements. Your rule should look like:
- Select Save .
- Repeat this process for each rule that you want to add to your site. For more information about rules, see Rules in the Tags Documentation.
- Continue with Build and publish your tag .

## Build and publish your tag

After you define data elements and rules, you must build and publish your tag. When you create a library build, you must assign it to an environment. The build’s extensions, rules, and data elements are then compiled and placed into the assigned environment. Each environment provides a unique embed code that allows you to integrate its assigned build into your site.

Adobe Experience Platform Tags support simple to complex publishing workflows that should accommodate your deployment of the Adobe Experience Platform Web SDK. See [Publishing overview](/en/docs/experience-platform/tags/publish/overview) for more information.

To build and publish your tag:

- Log in to experience.adobe.com using your Adobe ID credentials.
- In Adobe Experience Platform, go to Data Collection > Tags .
- Select your newly created tag from the list of Tag Properties to open it.
- Select Publishing Flow from the left rail.
- Select Add Library .
- In the Create Library dialog, specify the following information: Name : The name of the library. Environment : Select Development (development) from the list.
- Select + Add All Changed Resources .
- Select Save & Build to Development . Your tag is saved and is built for your development environment. A green dot indicates a successful build of your tag on your development environment.
- You can select … to rebuild the library or move the library to a staging or production environment.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
