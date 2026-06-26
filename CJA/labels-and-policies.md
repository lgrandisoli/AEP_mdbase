---
title: "Labels and policies"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/data-governance"
category: "other"
topic: "analytics-platform/using/cja-dataviews/data-governance"
created_at: "2026-06-02T19:07:20.502072+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Labels and policies

Last update: May 13, 2026
- Topics:
- [Data Views](#)
- [Data Governance](#)

CREATED FOR:

- Admin

When you create a dataset in Experience Platform, you can create [data usage labels](/en/docs/experience-platform/data-governance/labels/reference) for some or all elements in the dataset. You can view these labels and policies in Customer Journey Analytics.

The following labels are of special interest to Customer Journey Analytics:

- The C8 label - No measurement . This label signifies that data cannot be used for analytics on your organization’s websites or apps.
- The C12 label - No general data export . Schema fields labeled this way cannot be exported or downloaded from Customer Journey Analytics (via reporting, export, API, etc.)

NOTE
Data usage labels are not automatically propagated to stitched datasets. They can, however, be added manually.
Labeling in itself does not mean that these data usage labels are enforced. That’s what policies are used for. You can create your policies using the [Experience Platform UI](/en/docs/experience-platform/data-governance/policies/user-guide) or via the [Policy Service API](/en/docs/experience-platform/data-governance/api/overview) in Experience Platform.

Two Adobe-defined policies are available in Experience Platform that can surface in Customer Journey Analytics and affect reporting and data export:

- **Restrict usage analytics and user based measurement** policy, using the C8 label, and
- **Restrict data export** policy, using the C12 label.

## View data labels in Customer Journey Analytics data views

Data labels that you or others created in Experience Platform are shown in three locations in the data views user interface:

Location
Description
Info button on a schema field
Clicking this button indicates which Data Usage Labels currently apply to a field:

Right rail under
Component settings
Any Data Usage Labels are listed here:

Add Data Labels as a column
You can add Data Usage Labels as a column to the Included Components columns in data views. Just select the column selector icon and select **Data Usage Labels**:

## Filter on Data Governance labels in data views

In the data views editor, select the filter icon in the left trail and filter the data views components by **Data Governance** and type of **Label**:

Click **Apply** to see which components have labels attached to them.

## Filter on Data Governance policies in data views

You can check to see if a policy (for example, a policy you created, named **Enforce Analytics**) is turned on. And whether that policy blocks the use of certain Customer Journey Analytics data view elements for analytics or data export.

Again, select the filter icon in the left rail and under **Data Governance**, select **Policies**:

Click **Apply** to see which policies are enabled.

## How enabled policies affect data views

If one or more policies are turned on with C8 or C12 labels, those schema components that have certain data labels applied cannot be added to data views.

These components are grayed out in the left rail Schema fields list:

You also cannot save a data view that has blocked fields in it.

Be cautious to try to apply access and data governance labels (through policies) on fields or field groups in Experience Platform, for which you already have components defined in your data view. You might see this dialog.

You first need to resolve the violation (for example remove the components from the data view).

Related Articles
Download sensitive data
Related Articles
What are restricted labels in Report Builder?
recommendation-more-help
