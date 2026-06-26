---
title: "Include Exclude values component settings include-exclude-values-component-settings"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/component-settings/include-exclude-values"
category: "other"
topic: "analytics-platform/using/cja-dataviews/component-settings"
created_at: "2026-06-23T20:42:43.291307+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Include Exclude values component settings include-exclude-values-component-settings

Last update: June 5, 2026
- Topics:
- [Data management](#)

CREATED FOR:

- Admin

Include Exclude values lets you create rules that depend on the value of a dimension item. Values that don’t meet the criteria that you set are treated in Analysis Workspace as if they never existed, though the data still exists in the underlying dataset.

Setting
Description/Use case
Set include/exclude values
A checkbox that lets you enable conditions where data is included in a data view.
Case sensitive
Visible on String schema data types. Defaults to on. This setting applies only to the Include/Exclude Values logic, not to the resulting value. It allows you to specify if the rule is case sensitive.
Match
Lets you specify which values you would like to consider for reporting prior to attribution and segments (e.g., only use values containing the phrase “error”). You can specify
If all criteria are met
or
If any criteria are met
. Separate each value using a space.
Criteria
Lets you specify the match logic that should be applied to a specific segment rule.

- **String**: Contains the phrase, Contains any term, Contains all terms, Does not contain any term, Does not contain the phrase, Equals, Does not equal, Starts with, Ends with
- **Double/Integer**: Equals, Does not equal, Is greater than, Is less than, Is greater than or equal to, Is less than or equal to
- **Date**: Equals, Does not equal, Is later than, Is before, Occurs within

Match operand
Lets you specify the match operand that the match operator should be applied to.

- **String**: Text field
- **Double/Integer**: Text Field with up/down arrows for numeric values
- **Date**: Day granularity selector (calendar)
- **Date Time**: Date and time granularity selector

Add rule
Lets you specify an additional match operator and operand.
recommendation-more-help
