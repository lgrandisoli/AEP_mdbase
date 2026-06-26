---
title: "Caveats"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/caveats"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-23T20:45:42.680899+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Caveats

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Data management](#)

CREATED FOR:

- User

Each of the supported BI tools has some caveats in working with the Customer Journey Analytics BI extension.

BI tools
| tabs |  |
| --- | --- |
| Power BI Desktop | Power BI Desktop Advanced date range filtering is exclusive. For your end date, you need to select one past the day you want to report on. For example, is on or after 1/1/2023 and before 1/2/2023 . Power BI Desktop defaults to Import when you create a connection. Please ensure you use Direct Query . Power BI Desktop exposes data transformations through Power Query. Power Query primarily works with Import type connections so a many transformations that you apply like date or string functions throw an error saying you need to switch to an Import type connection. If you need to transform data at query time, you should use derived dimensions and metrics so Power BI doesn’t need to do the transforms itself. Power BI Desktop does not understand how to handle date-time type columns so the daterange X dimensions like daterangehour and daterangeminute are not supported. Power BI Desktop by default tries to make multiple connections using up more Query Service sessions. Go in to the Power BI settings for your project and disable parallel queries. Power BI Desktop does all the sorting and limiting client-side. Power BI Desktop also has different semantics for top X filtering that includes tied values. So, you cannot create the same sorting and limiting as you can do in Analysis Workspace. Earlier versions of the Power BI Desktop October 2024 release break PostgreSQL data sources. Ensure you use the version mentioned in this article. |
| Tableau Desktop | Tableau Desktop Range of Dates filtering is exclusive. For your end date, you need to select one past the day you want to report on. By default, when you add a date or date-time dimension like Daterangemonth to the rows of a sheet, Tableau Desktop wraps the field in a YEAR() function. To get what you want, you need to select that dimension and from the drop-down menu select the date function you want to use. For example, change Year to Month when you are trying to use Daterangemonth . Limiting results to the Top X is not obvious in Tableau Desktop. You can limit the results explicitly or using a calculated-field and the INDEX() function. Adding a Top X filter to a dimension generates complex SQL using an inner-join that is not supported. |
| Looker | Looker has a maximum number of connections per node setting that is required to be between 5-100. You cannot set this value to 1. This setting implies that a Looker connection always uses at a minimum 5 of the available Query Service sessions. Looker lets you create a project with a view based on a Customer Journey Analytics Data view. Looker then creates a model based on the dimensions and metrics, available in the Data view, using LookerML. This Project View does not automatically update to match the source. If you make changes or additions to the CJA Data View dimensions, metrics, calculated-metrics, or segments, then these changes do not automatically show up in Looker. You have to manually update the Project View or create a new Project. Looker’s user-experience on date or date-time fields like Daterange Date or Daterangeday Date is confusing. Looker’s date range is exclusive instead of inclusive. The until (before) is in gray so you may miss that aspect. For your end day, you need to select one past the day you want to report on. Looker doesn’t automatically treat your metrics as metrics. When you select a metric, by default Looker tries to treat the metric as a dimension in the query. To treat a metrics as a metric, you need to create a custom field as illustrated above. As a shortcut you can select ⋮ , select Aggregate , and then select Sum . |
| Jupyter Notebook | The main caveat for Jupyter Notebook is that the tool does not a drag-and-drop user interface like other BI tools. You can create good visuals, but you have to write code to accomplish this. |
| RStudio | R dplyr works with a flat schema so the FLATTEN option is required. The main caveat for RStudio is that the tool does not a drag-and-drop user interface like other BI tools. You can create good visuals, but you have to write code to accomplish this. |

recommendation-more-help
