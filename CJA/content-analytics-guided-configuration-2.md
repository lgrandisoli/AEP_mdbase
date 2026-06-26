---
title: "Content Analytics guided configuration"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/content-analytics/configuration/guided"
category: "guides"
topic: "analytics-platform/using/content-analytics/configuration"
created_at: "2026-06-23T20:44:34.123360+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Content Analytics guided configuration

Last update: May 13, 2026
- Topics:
- [Data management](#)
- [Components](#)

CREATED FOR:

- Admin

The guided configuration helps you to configure Content Analytics quickly and easily. The guided configuration uses a wizard to set up the requirements to configure Content Analytics automatically for your organization. In the **Configuration** screen, you can either create a new configuration or edit an existing configuration.

IMPORTANT
You can only have one Content Analytics configuration per sandbox in your organization.
NOTE
The configuration wizard supports multiple dataviews and channels and is different from the earlier version that only supported one data view and only the web channel. You have to select a sandbox and connection before you can select one or more data views in the
Data views
section. The configurations for
Experience capture
,
Data collection
and
Header overrides
are channel dependent and are part of each of the channels you configure in the
Channels
section.
To access the Content Analytics configuration

- Select **Data Management** > **Content Analytics Configuration** from the main menu in Customer Journey Analytics.

In the **Content Analytics Configurations** screen, you see a table of existing Content Analytics configurations.

For each configuration, the following details are available:

Column
Description
Name
The name of the configuration.
Created by
The technical account that created the configuration.
Created on
The timestamp when the configuration was created.
Modified on
The timestamp when the configuration was last modified.
Sandbox
The sandbox within the organization in which Content Analytics is (planned to be) configured and implemented.
Status
The status of the configuration. The status indicates for how many of the enabled channels the configuration is completed. Use
to open a popup with more detais.
You can use to customize the table. Select which columns to display in the **Customize table** dialog and select **Apply** to apply the changes.

From the Content Analytics **Configuration** screen, you can create a new configuration or edit an existing configuration.

To create a new configuration:

- Select **Create configuration**. This action opens the [guided configuration wizard](#guided-configuration-wizard).

To edit an existing configuration:

- Select and then **Edit** for an existing Content Analytics configuration. This action opens the [guided configuration wizard](#guided-configuration-wizard).

## Guided configuration wizard

The guided configuration wizard consists of four sections ([Details](#details), [Connection](#connection), [Data view](#data-view), and [Channels](#channels)), each prompting you for details that are required to set up and configure Content Analytics properly. Complete each section before moving to the next section, as some settings in a section might depend on configuration values in earlier sections.

### Details onboarding-details

Each configuration requires a unique name. For example, Example Content Analytics configuration. The name is required to save or implement a configuration.

For each configuration you also need to select the sandbox for which you want to configure Content Analytics.

- Name : Each configuration requires a unique name. For example, Example Content Analytics configuration . The name is required to save or implement a configuration.
- Sandbox : The configuration requires a sandbox. Select a sandbox from the list of sandboxes you have access to and on which data is collected that you want to use for Content Analytics. If you change a configured sandbox for which you have defined a connection and optionally data views, you are notified that the connection and data views need to be reconfigured.

### Connection

You need to select a connection to which you want to add Content Analytics data collection.

If you have not selected a connection for your configuration:

- Use **Select a connection** to open the **Select a connection** dialog that lists all connections that are available on the sandbox.
- In the **Select a connection** dialog, select a connection that you want to use. You can only select one connection.
- Select **Use connection**.

If you already have selected a connection, but you want to change that connection:

- Select **Edit**.
- In the **Select a connection** dialog, modify the connection that you want to use.
- Select **Use connection**.

### Data views onboarding-data-view

Your configuration requires the selection of one or more [data views](/en/docs/analytics-platform/using/cja-dataviews/data-views).

If you have not selected data views for your configuration:

- Use **Select data view** to open the **Data view** dialog that lists all data views available for the connection that you have configured for Content Analytics.
- In the **Data view** dialog, select one or more data views that you want to use.
- Select **Save**.

If you already have selected one or more data views, but you want to change that selection:

- Select **Edit data view selection**.
- In the **Data view** dialog, modify the selection of the data views that you want to use.
- Select **Save**.

Once you select **Save**, you see a **Selected data views** dialog that informs you about implications of including Content Analytics for the selected data views. Select **Continue** to continue or **Cancel** to cancel.

The following actions are available within the **Data view** dialog:

- To search for a specific data view, use the field.
- To filter the list of available data views, select . You can filter the list on Owner.Use **Hide filters** to hide the segment pane.
- To define which columns to show in the table, select . Select which columns to display in the **Customize table** dialog and select **Apply** to apply the changes.

### Channels

In the **Channels** section, you select the channels you want to enable for Content Analytics. You can select between **Mobile** and **Web**.

- To select a channel you have not yet configured, select **Enable**.
- To select a channel that is already configured but for which you want to change the configuration, select **Edit configuration**.

You can then configure the channel in more detail. That configuration is different depending on whether you enable and configure or edit a configuration for the [mobile](#mobile) or [web](#web) channel.

#### Mobile mobile

For the mobile channel, you can configure [experience capture and definition](#experience-capture-and-definition), [data collection](#data-collection), and [header overrides](#header-overrides).

##### Experience capture and definition mobile-experience-capture-and-definition

In this section, you can select to include experiences in the mobile data you collect with Content Analytics. For the mobile channel, an experience is what you have registered as an experience using the Adobe Experience Platform SDK for Content Analytics.

By default, **Include experiences** is disabled.

Only consider to include experiences when you have instrumented your mobile app to register experiences and to track experience views and experience clicks.

##### Data collection mobile-data-collection

The data collection settings allow you to define what data (experience locations, asset locations, asset URLs) you want to collect for Content Analytics. Ensure you do not collect any personally identifiable information as part of that data collection.

To configure data collection:

- Use an existing mobile Tags property or create a new mobile Tags property. To use an existing mobile Tags property: Select Choose existing . Select an existing property from the Tags property drop-down menu. You can start typing to search for and limit the available options. You cannot select a Tags property that another implemented Content Analytics configuration already uses. To create a new mobile Tags property: Select Create new . Specify a Tags name , for example ACA Test for Documentation . Specify Domains , for example, example.com .
- Indicate which experience locations should be excluded when collecting data for Content Analytics. Ensure you exclude personally identifiable experience locations. Specify a Regular expression string for Experience locations to exclude . For example: ^(?!.*documentation).* to exclude all documentation experience locations from Content Analytics.
- Indicate which asset locations should be excluded when collecting data for Content Analytics. Ensure you exclude personally identifiable asset locations. Specify a Regular expression string for Asset locations to exclude . For example: ^(?!.*(logo\.jpg)).*$ to exclude all asset locations with logo JPEG images from Content Analytics.
- Indicate which asset URLs should be excluded when collecting data for Content Analytics. Ensure you exclude personally identifiable asset URLs. Specify a Regular expression string for Asset URLs to exclude . For example: ^(?!.*(logo\.jpg)).*$ to exclude all asset URLs referring to logo JPEG images from Content Analytics.

##### Header overrides mobile-header-overrides

Optionally, you can specify in the **Header overrides** section a header name and secret header value. This header overrides configuration ensures that Content Analytics sends a custom HTTP header to retrieve mobile app assets, bypassing bot detection or traffic gating technologies.

- Enable **Configure header overrides**.
- Enter the **Header name**. For example, x-asset-service.
- Enter the **Header value**. Whatever you specify is secret and not visible in the user interface (unless you explicitly select to disclose the value during input).

##### Save mobile-save

Once you have configured the mobile channel, select **Save** to save the configuration. Select **Cancel** to cancel the configuration.

#### Web web

For the web channel, you can configure [experience capture and definition](#experience-capture-and-definition-1), [data collection](#data-collection-1), and [header overrides](#header-overrides-1).

##### Experience capture and definition web-experience-capture-and-definition

In this section, you can select to include experiences in the web data you collect with Content Analytics. An experience consists of all text on a web page that is reproducible using the URL from the initial user visit.

By default, **Include experiences** is turned off. When selected, define the URLs for which you want to include experiences.

Only consider to include experiences when the following is applicable:

- The pages on the site must be reproducible using the page URL.
- The text content seen by any given user can be reproduced using the page URL and does not depend on cookies or other personalization mechanisms.

IMPORTANT
Implement
Content Analytics versioning
to collect changes that you make to the experiences (pages) subject to Content Analytics.
###### New configuration new-experiences-configuration

To include experiences in a new or not implemented configuration:

- Enable Include experiences . The toggle to enable experiences affects the following: Data collection in the Content Analytics extension The process that generates experience attributes from Content Analytics event data The reporting template in Customer Journey Analytics.
- Select Add Regex to add a combination of a domain regular expression and query parameters.
- Specify how content renders on your website by defining combinations of a Domain regular expression and Query parameters that affect page content. Enter a Domain regular expression , for example /^(?!.*\b(store|help|admin)\b)/ . Ensure you escape regular expressions, using / . The domain regular expression indicates which URLs these parameters apply to. For example, you may have multiple sites, and for each site different parameters drive the content. If the query parameters apply to all of your pages, then you can use .* to indicate all pages. Specify a comma separated list of Query parameters , for example outdoors, patio, kitchen .
- Select Remove if you want to remove a combination of domain regular expression and query parameters.
- Select Add Regex if you want to add another combination of a regular expression and query parameters.

###### Implemented configuration implemented-experiences-configuration

To edit existing or include new experiences in an implemented configuration:

- Toggle Include experiences to enable or disable: The process that generates experience attributes from Content Analytics event data The reporting template in Customer Journey Analytics.
- Select Edit to edit the configuration of data collection for experiences in Content Analytics further. You are redirected to the Adobe Content Analytics extension in the Tags property that is associated with the current configuration.

##### Data collection web-data-collection

The data collection settings allow you to define what data (pages, assets) you want to collect for Content Analytics. Do not collect any personally identifiable information as part of that data collection.

To configure data collection:

- Use an existing web Tags property or create a new web Tags property. To use an existing web Tags property: Select Choose existing . Select an existing property from the Tags property drop-down menu. You can start typing to search for and limit the available options. You cannot select a Tags property that another implemented Content Analytics configuration already uses. To create a new web Tags property: Select Create new . Specify a Tags name , for example ACA Test for Documentation . Specify Domains , for example, example.com . Use a new Tags property if you want to create a Tags agnostic implementation for the web channel, using the Content Analytics Javascript library . The Tags property is created, but you will not use the property in the agnostic implementation. However, the agnostic implementation requires that you have run the guided configuration wizard at least once.
- Indicate which pages should be included or excluded when collecting data for Content Analytics. Ensure you exclude personally identifiable pages. Specify a Regular expression string for Pages to include / exclude . For example: ^(?!.*documentation).* to exclude all documentation pages from Content Analytics.
- Indicate which assets should be included or excluded when collecting data for Content Analytics. Ensure you exclude personally identifiable assets. Specify a Regular expression string for Asset to include / exclude . For example: ^(?!.*(logo\.jpg)).*$ to exclude all logo JPEG images from Content Analytics.

##### Header overrides web-header-overrides

Optionally, you can specify in the **Header overrides** section a header name and secret header value. This header override configuration ensures that Content Analytics sends custom HTTP headers to bypass any bot detection or traffic-gating technologies you have implemented.

- Enable **Configure header overrides**.
- Enter the **Header name**. For example, x-asset-service.
- Enter the **Header value**. Whatever you specify is secret and not visible in the user interface (unless you explicitly select to disclose the value during input).

#### Save web-save

After you have specified the details for the web channel, select **Save** to save the configuration. Select **Cancel** to cancel the configuration.

### Summary summary

Once you have provided all necessary details, a summary provides details on the artifacts that are created or modified.

- You see a You’re almost ready to implement configuration name for Content Analytics summary when you implement a new configuration.
- For existing implemented configurations, you see a You have implemented configuration name for Content Analytics summary.

### Actions actions

When you create or edit a configuration you have these options:

- Discard : All changes made as part of configuration are discarded.
- Save for later : Changes made to a configuration are saved. You can revisit the configuration at a later stage to make further changes, or implement the configuration. Only a value for Name is required to save a configuration.
- Implement : Settings for or changes made to a configuration are saved and implemented. All fields marked as need to have proper values. The implementation consists of: Customer Journey Analytics configuration: The selected data view is updated to include Content Analytics dimensions and metrics. The Connection tied to the selected data view is modified to include Content Analytics events and attributes datasets. A Content Analytics reporting template is added to Workspace. Adobe Experience Platform configuration: The creation of schemas to model Content Analytics events, asset attributes, and (if configured) experience attributes. The creation of datasets to collect Content Analytics events, asset attributes and (if configured) experience attributes. The creation of a dataflow that uses the featurization service to generate and update content attributes from Content Analytics events. Data collection configuration: The new or existing Tags property is configured to support Content Analytics data collection. This configuration implies the inclusion of the Adobe Content Analytics extension for Tags. A datastream is created for Content Analytics events. The Adobe Content Analytics extension is configured to ensure that Content Analytics events are sent to the datastream for Content Analytics. If the Web SDK or Mobile SDK is not configured for the Tags property, a new Web SDK or Mobile SDK configuration is created to send only Content Analytics events. If the Web SDK or Mobile SDK is configured for the Tags property, no changes are made to the existing Web SDK or Mobile SDK configuration.
- Save : Changes made to an implemented configuration are saved and the implementation is updated.
- Exit . Exits the guided configuration. All changes made to an implemented configuration are discarded.

## Publish publish

To start collecting data for your Content Analytics configuration, you need to [manually](/en/docs/analytics-platform/using/content-analytics/configuration/manual) publish the created Tags properties for the channels that you enabled.

Related Articles
Manual configuration
recommendation-more-help
