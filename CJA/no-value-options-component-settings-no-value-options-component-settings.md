---
title: "No Value Options component settings no-value-options-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/no-value-options"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-02T19:05:31.022786+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# No Value Options component settings no-value-options-component-settings

Last update: May 13, 2026
- Topics:
- [Data Views](#)

CREATED FOR:

- Admin

No value options let you to determine how Analysis Workspace handles situations where an event in a dataset contains a metric but the dimension did not contain a value. You can choose the name of this dimension item, hide it entirely, or even treat it as an actual value.

## Settings settings

Setting
Description
If shown, call “No value”
A text field that lets you rename the
No value
dimension item to something else.
Don’t show “No value” by default
Does not show this value in reporting. Metric occurrences not tied to this dimension are not visible in the report.
Show “No value” by default
Shows this value in reporting.
Treat “No value” as a value
(Not supported for numeric dimensions) Replaces blank values in the data with the text that you specified under If shown, call “No value”. For example, if you had Mobile device types as the dimension, you could rename the
No value
item to “Desktop”. When you change this field to a custom value, the custom value is treated as a legitimate string value. Therefore, if you enter the value “Red” into this field, any instances of the string “Red” appearing in the data itself rolls under the same line item that you have specified.
## “No value” support for numeric dimensions numeric

When using a numeric value as a dimension, you can

- Configure the “No value” option in a data view. Note that all configuration settings shown above are supported except for **Treat “No value” as a value**.
- Use **Include “No value”** for numeric dimensions in a Freeform table in Workspace.
- In the Segment builder, use the **exists** or **does not exist** operators with numeric dimensions.

Related Articles
The complete playbook for handling “No value” in Adobe Customer Journey Analytics
.
recommendation-more-help
