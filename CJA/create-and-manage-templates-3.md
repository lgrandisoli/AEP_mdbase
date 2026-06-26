---
title: "Create and manage templates"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/templates/create-templates"
category: "other"
topic: "analytics-platform/using/cja-workspace/templates"
created_at: "2026-06-23T20:43:40.423143+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create and manage templates

Last update: May 13, 2026
- Topics:
- [Workspace Basics](#)

CREATED FOR:

- User
- Admin

Administrators can create templates and save them for others in their login company to use.

People in the login company can use these company templates as described in [Use templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates).

## Create a template create-templates

To create a new template that can be used by people in your login company:

- In Analysis Workspace, build a project to your desired state.
- Select Project > Save as template… .
- Specify the following information in the Save as template dialog box: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 Field Description Name Provide a descriptive name for the template. Description Provide a short description for the template that describes its intended uses. Why use this template Provide a short explanation to inform people in the organization about how this template could be used. This explanation displays on the template’s Preview page. Channels Choose any applicable channels that apply to this template. You can select multiple channels: Web , Mobile , Cross-channel , Call center , and In-store . The selections you choose determine where the template is displayed and which segments apply for users accessing it from the Organization Templates page. Use cases Choose any use cases that apply to this template. You can select multiple use cases: Engagement , Conversion , Audience , Acquisition , and Journey Optimizer . The selections you choose determine the location of the template on the Organization Templates page. Users can navigate to the template or they can filter the list by use case. Note: When you select the Journey Optimizer option, the template is available for use in Adobe Journey Optimizer. In Journey Optimizer, a drop-down menu is available on the Reports page, allowing users to select this template or the default template. For more information, see Get started with the updated reporting experience in the Journey Optimizer documentation. Consider the following when selecting the Journey Optimizer option: This option is available only if Journey Optimizer data exists in the data view you are using in Customer Journey Analytics. When you use this template in Journey Optimizer, the data view that is set as the default data view in Adobe Journey Optimizer is used, regardless of the data view that is selected with this template in Customer Journey Analytics. For more information about setting a data view as the default data view in Journey Optimizer, see Compatibility in Create or edit a data view . Journey Optimizer activity type Choose the Journey Optimizer activity type to associate with this template: Campaigns , Journeys , Landing pages , Reports , or Subscriptions . Leave this field blank if you want this template to be associated with all activity types. This field displays only if Journey Optimizer is selected in the Use cases field. Journey Optimizer activity Choose the Journey Optimizer activity to associate with this template. Leave this field blank if you want this template to be associated with all activities of the selected activity type. This field displays only if Journey Optimizer is selected in the Use cases field. Tags Specify any tags that you want to apply to the template. People can filter the list of templates by the tags you add.
- Select Save as template .

For information about how users can create a project based on a template, see [Create a project based on a template](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#create-a-project-based-on-a-template) in [Use templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates).

## Edit or delete a template

Administrators can edit or delete company templates.

- In Analysis Workspace, select the Workspace tab, then under Templates in the left rail, select login_company_name templates .
- If you are viewing templates in a column view : Go to the template that you want to edit or delete, select the info icon next to the template name. Select Preview . Select the More icon, then select Edit or Delete .
- If you are viewing templates in a card view : Locate the template that you want to edit or delete. Hover over the template, then select Preview . Select the More icon, then select Edit or Delete .
- If you are editing a template, make any desired edits, then select Project > Save as template… .
- Specify the following information in the Save as template dialog box: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 Field Description Name Provide a descriptive name for the template. Description Provide a short description for the template that describes its intended uses. Why use this template Provide a short explanation to inform people in the organization about how this template could be used. This explanation displays on the template’s Preview page. Channels Choose any applicable channels that apply to this template. You can select multiple channels: Web , Mobile , Cross-channel , Call center , and In-store . If no channels are selected, the template is included with all channels. The selections you choose determine where the template is displayed and which filters apply for users accessing it from the Organization Templates page. Use cases Choose any use cases that apply to this template. You can select multiple use cases: Engagement , Conversion , Audience , Acquisition , and Journey Optimizer . The selections you choose determine the location of the template on the Organization Templates page. Users can navigate to the template or they can filter the list by use case. Note: When you select the Journey Optimizer option, the template is available for use in Adobe Journey Optimizer. In Journey Optimizer, a drop-down menu is available on the Reports page, allowing users to select this template or the default template. For more information, see Get started with the updated reporting experience in the Journey Optimizer documentation. Consider the following when selecting the Journey Optimizer option: This option is available only if Journey Optimizer data exists in the data view you are using in Customer Journey Analytics. When you use this template in Journey Optimizer, the data view that is set as the default data view in Adobe Journey Optimizer is used, regardless of the data view that is selected with this template in Customer Journey Analytics. For more information about setting a data view as the default data view in Journey Optimizer, see Compatibility in Create or edit a data view . Journey Optimizer activity type Choose the Journey Optimizer activity type to associate with this template: Campaigns , Journeys , Landing pages , Reports , or Subscriptions . Leave this field blank if you want this template to be associated with all activity types. This field displays only if Journey Optimizer is selected in the Use cases field. Journey Optimizer activity Choose the Journey Optimizer activity to associate with this template. Leave this field blank if you want this template to be associated with all activities of the selected activity type. This field displays only if Journey Optimizer is selected in the Use cases field. Tags Specify any tags that you want to apply to the template. People can filter the list of templates by the tags you add.
- Select Save as template .

## Rename, tag, or approve templates

Administrators can Rename, tag, and approve company templates.

- In Analysis Workspace, select the Workspace tab, then select the Projects tab in the left rail.
- Select the filter icon to filter the list of projects.
- In the filter rail, select Other filters and then select Company templates . A list of the company templates are displayed. All regular projects, unless they’re pinned, are not displayed. Company templates can be identified by the that precedes the template name.
- Click the … elilpsis icon next to a template to view the available options.
- Select Rename , Tag , or Approve . You can also delete a template, or you can delete a template as described in Edit or delete templates .
- (Optional) To return to the regular view, in the filter rail, deselect Company templates .

## Add missing components to the data view for a given template

By default, some templates provided by Adobe can’t be used because they contain components that are not in your data view.

For each missing component, a matching context label is available in your data view. You need to either add the matching context label to a component that is already in your data view, or you need to add a new component to your data view and add the context label to it.

To add missing components to a template:

- In Analysis Workspace, select the Workspace tab, then under Templates in the left rail, select Adobe templates .
- Select the filter icon to filter the list of templates.
- Select Not ready for use to show templates that require components that are not in your data view.
- Locate a template that is not yet ready to use with your data view.
- Do either of the following: If you are viewing templates in a column view : Go to the template that is not yet ready to use with your data view, then select the info icon next to the template name. Select Preview . If you are viewing templates in a card view : Locate the template that is not yet ready to use with your data view. Hover over the template, then select Preview .
- In the Missing components section, a list of components that are missing from the data view are displayed. Select Add these components to your data view . The configuration page for the data view is displayed in a new tab.
- Select the Components tab for the data view.
- For each component that was listed as missing from the template, do either of the following on the Components tab: In the Included components section, select a component that is already included in the data view that you want to use for the missing component. Add a new component to the data view that you want to use for the missing component, then select the component. To add a new component to the data view, search the list of schema fields, then drag it into the Included components section.
- With the component selected, locate the Context labels drop-down menu in the right column.
- In the Context labels drop-down menu, select the context label that has the same name as the missing component.
- Select Save and continue .
- For each missing component, repeat the process of adding the matching context label to a component in the data view.

## Access a company template

Like with templates that are provided by Adobe, users in the organization can access templates that administrators create.

For information about how to access a company template, see [Access and run a template](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates#access-and-run-a-template) in [Use templates](/en/docs/analytics-platform/using/cja-workspace/templates/use-templates).

## Hide the Templates tab

Administrators can hide the Templates tab for all users within their organization.

- Go to **Customer Journey Analytics** > **Components** > **Preferences** > **Company**.
- Select the option to **Hide Templates tab**.

recommendation-more-help
