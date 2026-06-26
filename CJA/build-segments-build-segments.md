---
title: "Build segments build-segments"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/segments/seg-builder"
category: "other"
topic: "analytics-platform/using/cja-components/segments"
created_at: "2026-06-02T19:06:09.715271+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Build segments build-segments

Last update: May 13, 2026
- Topics:
- [Filters](#)
- [Segments](#)

CREATED FOR:

- User

The **Segment builder** dialog is used to create new or edit existing segments. The dialog is titled **New segment** or **Edit segment** for segments that you create or manage from the [Segment manager](/en/docs/analytics-platform/using/cja-components/segments/seg-manage).

Segment builder
Create or Edit segment
- Specify the following details ( is required): table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 layout-auto Element Description Data view You can select the data view for the segment. The segment you define is available as a segment in the Settings tab of a data view. Project-only segment An info box to explain that the segment is only visible in the project where it is created and that the segment will not be added to your component list. Enable Make this segment available to all your projects and add it to your component list to change that setting. This info box is only visible when you create a quick segment and turn the quick segment info a regular segment using Open builder from the Quick segment interface. Title Name the segment, for example, Last month mobile customers . Description Provide a description for the segment, for example, Segment to define the mobile customers for the last month . Tags Organize the segment by creating or applying one or more tags. Start typing to find existing tags you can select. Or press ENTER to add a new tag. Select to remove a tag. Definition Define your segment using the Definition builder .
- To verify whether your segment definition is correct, use the constantly updated preview of the results of the segment at the top right.
- To create an audience from the segment and share the audience with Experience Platform, select Create audience from segment . See Create and publish audiences for more information.
- Select: Save to save the segment. Save As to save a copy of the segment. Delete to delete the segment. Cancel to cancel any changes you made to the segment or cancel the creation of a new segment.

## Definition builder

You use the Definition builder to construct your segment definition. In that construction, you use components, containers, operators and logic.

You can configure the type and scope of your definition:

- To specify the type of your definition, specify whether you want the build an include or exclude definition. Select **Options** and from the drop-down menu **Include** or **Exclude**.
- To specify the scope of your definition, select from the **Include** or **Exclude** drop-down menu whether you want the scope of the definition to be **Event**, **Session**, **Person**, **Global Account** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), **Account** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), **Opportunity** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), or **Buying Group** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)

You can always change these settings later.

### Components

A vital part of the construction of your segment definition is using dimensions, metrics, existing segments and date ranges. All these components are available from the component panel in the Segment builder.

{width="100%"}

To add a component:

- Drag and drop a component from the components panel onto **Drag and drop Metric(s), Segment(s), and/or Dimensions here**. You can use the in the components bar to search for specific components.
- Specify details for the component. For example, select a value from **Select value**. Or enter a value. What and how you can specify one or more values depends on the component and the operator.
- Optionally modify the default operator. For example, from **equals** to **equals any of**. See [Operators](/en/docs/analytics-platform/using/cja-components/segments/seg-operators) for a detailed overview of the available operators.

To edit a component:

- Select a new operator for the component from the operator drop-down menu.
- Select or specify a different value for the operator if appropriate.
- If the component type is a dimension, you can define the attribution model. See [Attribution model](#attribution) for more information.

To delete a component:

- Select in a component.

### Containers

You can group multiple components in one or more containers and define logic within and between containers. Containers allow you to build complex definitions for your segment.

- To add a container, select **Add container** from **Options**.
- To add an existing component to the container, drag and drop the component into the container.
- To add another component to the container, drag and drop a component from the component panel into the container. Use the blue insertion line as a guide.
- To add another component outside of the container, drag and drop a component from the component panel outside of the container, but inside the main definition container. User the blue insertion line as a guide.
- To modify the logic between components in a container, between containers or between a container and a component, select the appropriate **And**, **Or**, **Then**. When you select Then, you turn the segment into a sequential segment. See [Create sequential segment](/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build) for more information.
- To switch the container level, select **Global Account** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), **Account** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), **Opportunity** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), **Buying Group** [[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank), **Event**, **Session** or **Person**.

You can use in a container for the following actions:

Container action
Description
Add container
Add a nested container to the container.
Exclude
Exclude the result from the container in the segment definition. A thin red left bar identifies an exclude container.
Include
Include the result from the container in the segment definition. Include is the default. A thin gray left bar identifies an include container.
Name container
Rename the container from its default description. Type a name in the text field. If you provide no input, the default description is used.
Delete container
Delete the container from the definition.
## Date ranges

You can build segments that contain rolling date ranges. This way, you are able to answer questions about ongoing campaigns or events. For example, you can build a segment that includes *everyone who has made an online purchase over the last 60 days*.

See [Rolling date ranges in segments](/en/docs/analytics-learn/tutorials/components/segmentation/rolling-date-ranges-in-segments#_blank) for a demo video.

style
shade-box
## Stack segments stack

You can build a segment using segments. When you use segments in a segment, you can optimize your segment and reduce the complexity.

Imagine you want to segment on the combination of device type (2) and US states (50). You could either build 100 segments, each for the unique combination of device type (mobile phone versus tablet) and US state. To get the tablet users in California, you would use one of the 100 segments:

Or, you could define 52 segments: 50 segments for the US states, one for mobile phone and one for tablet. And then stack the segments to obtain the same results. To get the California tablet users, you would stack two segments:

## Attribution attribution

When you use a dimension in the Segment builder, you have the options to specify the attribution model for that dimension. The attribution model you select determines whether data qualifies for the condition you have specified for the dimension component.

Select within the dimension component and select one of the Attribution models from the popup:

Models
Description
Repeating model (default)
Include instance and persisted values for the dimension to determine qualification.
Instance
Include only instance values for the dimension to determine qualification.
Non-repeating instance
Include unique instance (non-repeating) values for the dimension to determine qualification.
### Example

As part of a segment definition you have specified the following condition: Page Name equals Women. Similar to the example above. You repeat this segment definition using the two other attribution models. So you have three segments each with their own attribution model:

- Women Page - Attribution - Repeating (default)
- Women Page - Attribution - Instance
- Women Page - Attribution - Non-repeating instance

The table below explains, for each attribution model, which incoming events are qualified for that condition.

Women Page - Attribution -
attribution model
Event 1:
Page Name equals
Women
Event 2:
Page Name equals
Men
Event 3:
Page Name equals
Women
Event 4:
Page Name equals
Women
(persisted)
Event 5:
Page Name equals
Checkout
Event 6:
Page Name equals
Women
Event 7:
Page Name equals
Home
Repeating (default)
Instance
Non-repeating instance
An example report on events using the three segments looks like:

recommendation-more-help
