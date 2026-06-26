---
title: "Behavior component settings behavior-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/behavior"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-23T20:42:42.456382+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Behavior component settings behavior-component-settings

Last update: May 13, 2026
- Topics:
- [Data Views](#)

CREATED FOR:

- Admin

Behavior settings are available on both dimensions and metrics. The availability of settings depend on the component type and schema data type.

## Dimension behavior settings

Setting
Description
Lower case
De-duplicates rows that have the same value but different case. If enabled, all instances of a dimension with the same value are reported as lower case. For example, your data contains the values
"liverpool"
,
"Liverpool"
, and
"LIVERPOOL"
in a string dimension. If Lower case is enabled, all three values are combined into
"liverpool"
. If disabled, all three values are treated as distinct.
NOTE
If you enable Lower case on a lookup dataset dimension, multiple lookup values can exist for the same identifier. If this conflict happens, Customer Journey Analytics uses the first ASCII collated value (Uppercase values precede lowercase values). Adobe advises against using lookup datasets that contain the same value when Lower case is enabled.
## Metric behavior settings

Setting
Description/Use case
Count values
Visible on Integer and Double schema data types. Increase the metric by the specified amount. For example, increases a metric by 50 if the value of the column is
50
.
Count instances
Visible on Integer and Double schema data types. Increase the metric by one, regardless of the value. The presence of any value increases the metric. For example, increases a metric by 1 if the value of the column is
50
.
Values to count
Visible on Boolean schema data types. Lets you determine if the metric increases by counting
true
,
false
, or both.
You can generate both an ‘Orders’ and ‘Revenue’ metric in Analysis Workspace using the same event dataset column with different behaviors. Drag the ‘Revenue’ dataset column into the data view twice and set one to ‘Count values’ and the other to ‘Count instances’. The ‘Orders’ metric counts instances, while the ‘Revenue’ metric counts values.

recommendation-more-help
