---
title: "Troubleshoot failed exports"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/exports/troubleshoot-exports"
category: "other"
topic: "analytics-platform/using/cja-components/exports"
created_at: "2026-06-23T20:42:28.280841+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Troubleshoot failed exports

Last update: May 13, 2026
- Topics:
- [Components](#)

CREATED FOR:

- User

When you [export full tables from Analysis Workspace to cloud destinations](/en/docs/analytics-platform/using/cja-workspace/export/export-cloud), you can view the status of those exports both from the [Exports tab](/en/docs/analytics-platform/using/cja-components/exports/manage-exports) and from the [Logs tab](/en/docs/analytics-platform/using/cja-components/exports/manage-export-logs). Failed exports show a status of **Failed**.

## Common failures and actions

Exports can fail for various reasons. The following table describes some of the most common reasons, with actions you can take to address the failures:

Reason for failure
Suggested action
More information
Invalid location or account information
Make sure your credentials and other information is correct for the cloud account and location you are exporting to.
Configure cloud export accounts
and
Configure cloud export locations
.
A dimension or metric in the report was removed from the data view
Contact your system administrator to see which components were removed from the data view. You might need to use a different data view in your export, or remove components from your table that are no longer available.
Export Customer Journey Analytics reports to the cloud
Row limit exceeded
Depending on your license type, you can export a maximum of 3 million, 30 million, 150 million, or 300 million rows. Update the table you are exporting to reduce the number of total rows.
Export Customer Journey Analytics reports to the cloud
Scheduled export expiration
The scheduled export that you configured has expired. Update the export’s expiration.
Manage exports
Dimension not supported
Any dimension that meets all of the following criteria is not supported in Full Table Export:

- Was created from a field that is part of an array of objects
- Has persistence enabled
- Is not using a binding dimension

- [Use arrays of objects](/en/docs/analytics-platform/using/cja-usecases/complex-data/object-arrays)
- [Persistence component settings](/en/docs/analytics-platform/using/cja-dataviews/component-settings/persistence)
- [Use binding dimensions and metrics in Customer Journey Analytics](/en/docs/analytics-platform/using/cja-usecases/data-views/binding-dimensions-metrics)

A data governance policy that is enforced by your organization restricts components in your table from being exported
Contact your system administrator to see which components are restricted from being exported. Remove the restricted components prior to exporting.
Filter on Data Governance policies in data views
section in
Labels and policies
## Contact Adobe Customer Care

If you continue to experience issues, contact Adobe Customer Care. When contacting customer care regarding a failed export, make sure you have the following information available:

- Export name
- Export ID
- Instance ID
- Data view name
- Location
- Account
- Connection
- Company name

recommendation-more-help
