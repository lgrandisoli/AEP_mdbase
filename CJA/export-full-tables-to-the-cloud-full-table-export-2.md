---
title: "Export full tables to the cloud full-table-export"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/export/export-cloud"
category: "other"
topic: "analytics-platform/using/cja-workspace/export"
created_at: "2026-06-23T20:42:29.023338+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Export full tables to the cloud full-table-export

Last update: May 13, 2026
- Topics:
- [Curate and Share](#)

CREATED FOR:

- User

In Customer Journey Analytics, you can export full tables from Analysis Workspace to designated cloud destinations.

Other methods of exporting Customer Journey Analytics reports are also available, as described in [Export overview](/en/docs/analytics-platform/using/cja-workspace/export/export-project-overview).

## Understand full table export

You can export full tables from Analysis Workspace to cloud providers like Google, Azure, Amazon, and Adobe.

[Advantages of full table export](#advantages-of-full-table-export) include the ability to export millions of rows, include calculated metrics, structure data output in concatenated values, and more.

When exporting full tables, consider the following:

- Before you export to the cloud, make sure that your tables, your environment, and your permissions meet the minimum export requirements .
- Some features and components are not supported when exporting full tables to the cloud.

Use the following process when exporting full tables to the cloud:

- Configure a cloud account
- Configure a location on the account
- Export a full table from Workspace
- Access data in the cloudin your cloud account and Manage exports in Adobe

## Export full tables export-from-workspace

NOTE
Before you export data as described in this section, learn more about full table export in the
Understand full table export
section above.
To export full tables from Analysis Workspace:

- If you haven’t already, configure an export account and location, as described in Configure cloud export accounts and Configure export locations .
- In Analysis Workspace, right-click the heading of a freeform table to reveal the context menu, then select Export full table .
- In the New full table export dialog box, specify the following information: table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 16-row-2 layout-auto Field name Function Name Specify a name for the export. This name displays in the list of exports. Tags You can apply an existing tag to the export or you can create a new tag and apply it. To apply an existing tag to the export, select any tags from the drop-down menu. Any tags in your company are available to apply. To create a new tag, type the name of the new tag, then press Enter. Consider the following when applying tags to an export: Tags that you apply can be filtered on or searched for in the exports table. Tags applied to a project are not automatically applied when exporting a full table, as described in “Configure columns on the exports page” in Manage exports . (Alternatively, when scheduling a full project for export , any tags applied to the project are automatically applied to the export.) Description Add a description to the export. You can choose to view descriptions as a column in the Exports page when viewing exports. Data view Select the data view that contains the components that you want to include in the export. The Data view drop-down menu is located in the upper-left corner of the dialog. Note: If you select a data view that is missing components that are already included in your data table, then you are prompted to clear and re-create the panel using components that are included in the selected data view. Data structure Displays the Freeform table that you are exporting. You can modify the data structure by dragging components from the left panel to the table. You can apply a filter by dragging a component into the filter area. The table dynamically updates as you add components to the canvas. You can include up to 10 columns. Any segments that were applied to the full table in the project appear above the table. You can apply a segment or group of segments to an export. Report window Select the reporting time-frame to include in each export file. Options include Today , Yesterday , Last 7 days , Last 30 days , This week , and This month . This option is not displayed when the Export frequency is set to Send now (one-time) . Clear all Clears the contents of the data table. This allows you to start building a new table directly within the New full table export dialog. File format Choose whether the exported data should be in .csv, .json, or .parquet format. When choosing the Parquet file format, any of the following characters included in component names are replaced with an underscore (_): ’ ’ - ASCII space ‘,’ - ASCII comma ‘;’ - ASCII colon ‘{’ or ‘}’ - ASCII open/close brace ‘(’ or ‘)’ - ASCII open/close parenthesis ‘\n’ - ASCII newline ‘\t’ - ASCII tab ‘=’ - ASCII equals Include manifest file When enabled, a manifest file is included with any successful export delivery. The manifest file enables you to confirm that all files were delivered successfully. It includes the following information: A list of all files that were delivered The MD5 checksum of each file Exported data is available as a compressed file in the cloud destination that you configured, as described in Configure cloud export accounts and Configure cloud export locations . The filename of the compressed file is as follows, depending on whether you chose csv , json , or parquet as the file format: cja-export-{reportInstanceId}-{idx}.csv.gz cja-export-{reportInstanceId}-{idx}.json.gz cja-export-<instanceId>-<idx>.snappy.parquet Each column in the parquet file is compressed. Choose the file format in the File format field above. Frequency Set the schedule for how often the export should occur. You can choose Send now (one-time) to send the export only once. When you select this option, the export is initiated immediately. Or, you can choose to send the export on a defined schedule. When sending on a schedule, options include Daily , Weekly , Monthly by day of the week , Monthly by day of the month , Yearly by day of the month , and Yearly by specific date . When selecting an export frequency, consider the following: The options in the Lookback window field change depending on what you select here. Additional configuration fields display depending on the option that you choose. Starting on The day and time that the scheduled export should begin. This option is available only when choosing a scheduled export frequency. Ending on The day and time that the scheduled export expires. The scheduled export no longer runs after the date and time that you set. This option is available only when choosing a scheduled export frequency. View destinations for all users System administrators can select this option to view all accounts and locations, regardless of who created them. Account Select the cloud export account where you want the data to be sent. Or, if you haven’t already configured a cloud account that you want to use, you can configure a new account: In the Account drop-down menu, select Add account , then specify the following information: Location account name : Specify a name for the location account. This name appears when creating a location Location account description : Provide a short description of the account to help differentiate it from other accounts of the same account type. Make account available to all users in your organization : Select this option if you want to allow other users in your organization to use the account. Account type : Select the type of cloud account you are exporting to. Available account types are Amazon S3 Role ARN, Google Cloud Platform, Azure SAS, Azure RBAC, Snowflake, and AEP Data Landing Zone. To finish configuring your account, continue with the link below that corresponds to the Account type you selected: AEP Data Landing Zone Amazon S3 Role ARN Google Cloud Platform Azure SAS Azure RBAC Snowflake Location Select the location on the account where you want the export data to be sent. Or, if you haven’t already configured a cloud account that you want to use, you can configure a new account: In the Location drop-down menu, select Add location , then specify the following information: Name : The name of the location. Description : Provide a short description of the location to help differentiate it from other locations on the account. Make location available to all users in your organization : Select this option if you want to allow other users in your organization to use the location. Location account : Select the account where you want to create the location. To finish configuring your location, continue with the link below that corresponds to the account type that you selected in the Location account field: AEP Data Landing Zone . Amazon S3 Role ARN Google Cloud Platform Azure SAS Azure RBAC Snowflake Notifications Add users and groups who you want to receive notifications when this export fails or is about to expire. Begin typing the name or email address of a user, or begin typing the name of a group, then select it when it appears in the drop-down list.
- Select Save to save the export. Data is sent to the cloud account that you specified at the frequency that you specified.
- (Optional) After you create the export, whether you chose to send it now or on a defined schedule, you can view and manage it on the Exports page and view it in the Export logs .

## Manage exports

After data is exported from Analysis Workspace, you can edit, re-export, duplicate, tag, or delete existing exports, as described in [Manage exports](/en/docs/analytics-platform/using/cja-components/exports/manage-exports).

## Advantages of full table export advantages

Exporting Customer Journey Analytics data to the cloud allows you to:

- Export to a shared location, such as Adobe Experience Platform Data Landing Zone, Google Cloud Platform, Microsoft Azure, Amazon S3, or Snowflake.
- Store large amounts of historical data. This type of data can be used to detect long-term trends to gain business intelligence, and ultimately lead to better business decision-making.
- Export full tables that contain thousands or millions of rows (3 million, 30 million, 150 million, or 300 million rows, depending on license type). Other export methods allow a maximum of 50,000 rows.
- Include calculated metrics in the exported Customer Journey Analytics data.
- Structure data output as concatenated values.
- Export one-time or on a schedule. (Also available with other export options .)
- Export files in CSV, JSON, or Parquet format. (Also available with other export options .)
- Export tables that include multiple dimensions.

## Minimum requirements

Make sure that your tables, your environment, and your permissions meet the following requirements:

- Tables: All tables must include at least one dimension in the row and one metric in each column to be supported with a full-table export.
- Environment: Ensure that the IP addresses and Domains used by Customer Journey Analytics are allowed through their organization’s firewall.
- Permissions: In the Adobe Admin Console, users must be assigned a product profile that has the Full Table Export permission assigned to it to export full tables. For information about assigning a permission to a product profile in the Admin Console, see Customer Journey Analytics permission in Admin Console . note NOTE Users who are assigned the Product Admin role always have access to export full tables; these users do not need to be assigned the Full Table Export permission.

## Unsupported features

The following features are not supported and are automatically removed from full-table exports:

- Percentages
- Totals
- Search filtering
- Static rows
- Date aligning
- Metrics from summary datasets
- Dynamic dimension items Dynamic dimension items are created when you drop a dimension on a column header in a freeform table, resulting in the column being filtered dynamically by the top 5 dimension items. In Analysis Workspace, these top 5 dimension items update each time you load the project. In a full-table export, these dimension items become static. For more information, see Dynamic vs static dimension items in freeform tables .
- Dimensions in the first breakdown are converted and added as a secondary dimension in the row of the exported table. Any other breakdowns are not included in the table.
- Sorting is not supported for most datasets; data might be sorted for small datasets.

## Unsupported components

The following components are not supported, and Analysis Workspace prompts you to remove them from your table when performing a full-table export:

- Calculated metrics that use unsupported functions in the metric definition (see Unsupported calculated metric functions for more information)
- Components that have been restricted by an administrator from being exported (see the Segment on Data Governance policies in data views section in Labels and policies for more information)
- Any dimension that meets all of the following criteria: Is created from a field that is part of an array of objects (similar to multi-value variables in Adobe Analytics). Has persistence enabled . Is not using a binding dimension .
- Multiple dimensions that are from fields referencing different arrays of objects . (Multiple dimensions referencing the same array of objects are allowed.)
- More than 10 dimensions and 10 metrics per report (up to 10 dimensions and 10 metrics are supported)
- In table columns: Date ranges Dimensions
- In table rows: Calculated metrics Metrics Date ranges Segments

## Calculated metric functions support

The following basic and advanced sections list which calculated metric functions are supported when exporting full tables:

### Basic function support

Basic function
Support status
Absolute Value
Supported
Column Maximum
Supported
Column Minimum
Supported
Column Sum
Supported
Count
Supported
Exponent
Supported
Mean
Supported
Median
Not supported
Modulo
Supported
Percentile
Not supported
Power Operator
Supported
Quartile
Not supported
Row Count
Supported
Row Max
Supported
Row Min
Supported
Row Sum
Supported
Round
Supported
Square Root
Supported
Standard Deviation
Not supported
Variance
Planned
### Advanced function support

#### Algebra functions

Advanced function
Support status
Log Base 10 (Exponential Algebra)
Supported
Cube Root (Exponential Algebra)
Supported
Natural Log (Exponential Algebra)
Supported
Floor (Numeric Adjustment Algebra)
Supported
#### Logic functions

Advanced function
Support status
If (Logic)
Supported
#### Boolean functions

Advanced function
Support status
Not (Boolean Operator Logic)
Supported
Or (Boolean Operator Logic)
Supported
And (Boolean Operator Logic)
Supported
#### Comparison functions

Advanced function
Support status
Less Than (Comparison Logic)
Supported
Less Than or Equal (Comparison Logic)
Supported
Equal (Comparison Logic)
Supported
Greater Than or Equal (Comparison Logic)
Supported
Greater Than (Comparison Logic)
Supported
Not Equal (Comparison Logic)
Supported
#### Trigonometry functions

Advanced function
Support status
Pi
Supported
Sine (Standard)
Supported
Cosine (Standard)
Supported
Tangent (Standard)
Supported
Arc Sine (Standard)
Supported
Arc Cosine (Standard)
Supported
Arc Tangent (Standard)
Supported
#### Hyperbolic functions

Advanced function
Support status
Hyperbolic Cosine
Supported
Hyperbolic Sine
Supported
Hyperbolic Tangent
Supported
#### WASKR functions

Advanced function
Support status
Confidence (WASKR)
Not supported
Confidence (Lower) (WASKR)
Not supported
Confidence (Upper) (WASKR)
Not supported
#### Distribution functions

Advanced function
Support status
T-Score (Student T-Distribution)
Not supported
T-Test (Student T-Distribution)
Not supported
CDF-T (Student T-Distribution)
Not supported
Z-Score (Normal Distribution)
Not supported
Z-Test (Normal Distribution)
Not supported
CDF-Z (Normal Distribution)
Not supported
#### Regression functions

Advanced function
Support status
Correlation Coefficient (Exponential Regression)
Not supported
Intercept (Exponential Regression)
Not supported
Predicted Y (Exponential Regression)
Not supported
Slope (Exponential Regression)
Not supported
Correlation Coefficient (Linear Regression)
Not supported
Intercept (Linear Regression)
Not supported
Predicted Y (Linear Regression)
Not supported
Slope (Linear Regression)
Not supported
Correlation Coefficient (Log Regression)
Not supported
Intercept (Log Regression)
Not supported
Predicted Y (Log Regression)
Not supported
Slope (Log Regression)
Not supported
Correlation Coefficient (Power Regression)
Not supported
Intercept (Power Regression)
Not supported
Predicted Y (Power Regression)
Not supported
Slope (Power Regression)
Not supported
Correlation Coefficient (Quadratic Regression)
Not supported
Intercept (Quadratic Regression)
Not supported
Predicted Y (Quadratic Regression)
Not supported
Slope (Quadratic Regression)
Not supported
Correlation Coefficient (Reciprocal Regression)
Not supported
Intercept (Reciprocal Regression)
Not supported
Predicted Y (Reciprocal Regression)
Not supported
Slope (Reciprocal Regression)
Not supported
#### Other advanced functions

Advanced function
Support status
Approximate Count Distinct
Planned
Cumulative
Planned
Cumulative Average
Planned
Lift
Planned
Sample Variance
Planned
## Attribution behavior

Full table export supports calculated metrics that use a non-default attribution model (as described in the *Use non-default attribution model* section in [Column settings](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/column-row-settings/column-settings)).

If a non-default attribution model is being used in a report, the allocation model that is used in the report is either ignored or retained, depending on whether the report has a single dimension or multiple dimensions:

- For reports that include metric attribution in a single dimension: Metric attribution overrides the allocation model as is normally done when using metric attribution. For example, a “first touch” metric attribution overrides a “most recent” dimension allocation.
- For reports that include metric attribution on multiple dimensions at the same time: Metric attribution is applied in addition to the dimension allocation model . For example, a “first touch” metric attribution is applied in addition to a “most recent” dimension allocation. Additionally, metric attribution is applied to post-allocated dimension item pairs as if they were single dimension items, rather than to each dimension item independently as is normally done in a Freeform table. note NOTE Multi-dimensional reports are supported only when exporting data to the cloud, as described in this article.

## Comparison to Data Warehouse

If you previously used Data Warehouse to export Adobe Analytics data, the following table can help you understand the differences between exporting full tables in Customer Journey Analytics versus exporting data with Data Warehouse in Adobe Analytics.

Feature
Full Table Export in Customer Journey Analytics
Data Warehouse in Adobe Analytics
Build a custom report
Yes
Yes
Calculated metrics
Yes
No
Segments
Yes
Limited
Dimensions
Limit of 10
Unlimited
Metrics
Limit of 10
Unlimited
Reporting rows
Limit of 3 million, 30 million, 150 million, or 300 million, depending on tier
Unlimited
Number of reports
Unlimited
Unlimited
Ad hoc (one-time) delivery
Yes
Yes
Schedule recurring delivery
Yes
Yes
Email delivery
No
Yes
FTP / SFTP
No
Legacy support
Azure
Yes
Yes
Amazon S3
Yes
Yes
Google Cloud Platform
Yes
Yes
Snowflake
Yes
No
Delivery frequency
Daily
Hourly
recommendation-more-help
