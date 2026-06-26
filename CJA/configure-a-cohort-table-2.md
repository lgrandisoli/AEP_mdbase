---
title: "Configure a cohort table"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/cohort-table/t-cohort"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:43:17.867929+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Configure a cohort table

Last update: May 13, 2026
- Topics:
- [Visualizations](#)

CREATED FOR:

- User

To create and configure a Cohort table:

- Add a Cohort table visualization. See Add a visualization to a panel .
- Define the Inclusion Criteria , Return Criteria , Cohort Type , and Settings as defined in the table below. table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 Element Description Inclusion criteria You can apply up to 10 inclusion segments and up to 3 inclusion metrics. The metric specifies what to which cohort a user belongs. For example, if the inclusion metric is Orders, only users who placed an order during the time range of the cohort analysis are included in the initial cohort. The default operator between metrics is AND, but you can change it to OR. In addition, you can add numeric segmenting to these metrics. For example: Sessions >= 1 . Return criteria You can apply up to 10 return segments and up to 3 return metrics. The metric indicates whether the user has been retained (retention) or not (churn). For example, if the return metric is Video Views, only users who viewed videos during subsequent time periods (after the period in which they were added to a cohort) are represented as retained. Another metric that quantifies retention is Sessions. [B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"} Container By default the cohort analysis is tied to the Person container. If more containers beyond Person are available from the account based connection that supports the Workspace project, you can select another container for the cohort analysis from the Container drop-down menu. Granularity The time granularity of Day, Week, Month, Quarter, or Year. Type Retention (default): A Retention cohort measures how well your person cohorts return to your property over time. A retention cohort is the standard cohort and indicates return and repeat user behavior. A green color indicates a Retention cohort in the table. Churn : A Churn (also known as attrition or fallout) cohort measures how your person cohorts fall out of your property over time. Churn is the opposite of retention: Churn = 1 - Retention . Churn is a good measure of stickiness as well as opportunity by showing you how frequently customers do not come back. You can use churn to analyze and identify areas of focus: which cohort segments could use some attention? A red color indicates a Churn cohort in the table (similar to fallout in the Flow visualization). Settings Rolling calculation : Calculate retention or churn based on the previous column, rather than the Included column (default). Rolling Calculation changes the calculation method for your “return” periods. The normal calculation finds users who meet return criteria and were part of the inclusion period. Regardless of whether or not they were in the cohort for the previous period. Instead, Rolling Calculation finds users who meet “return” criteria and were part of the previous period. Therefore, Rolling Calculation segments and funnels the users who continually meet the “return” criteria period over period. Return criteria are applied to each of the periods leading up to the selected period. Latency Table : A Latency table measures the time that has elapsed before and after the inclusion event occurred. Latency table is great to use for pre/post analysis. For example, you have an upcoming product or campaign launch and you want to track behavior before and after the launch. The Latency table displays the pre- and post behavior side by side to see the direct impact. The pre-inclusion cells in the Latency table calculate users who meet the Inclusion criteria on the inclusion period and then meet the Return criteria in the periods before the inclusion period. Note that Latency table and Custom dimension cohort cannot be used together. Custom dimension cohort : Create cohorts based on the selected dimension, rather than time-based cohorts (default). Many customers want to analyze their cohorts by something other than time and the new Custom Dimension Cohort feature provides you with the flexibility to build cohorts based on dimensions of their choosing. Use dimensions, such as marketing channel, campaign, product, page, region, or any other dimension to show how retention changes based on the different values of these dimensions. The Custom Dimension Cohort segment definition applies the dimension item only as part of the inclusion period, not as part of the return definition. After choosing the Custom dimension cohort option, you can drag and drop whichever dimension you want into the drop zone. Adding dimensions allows you to compare similar dimension items across the same time period. For example, you can compare the performance of cities side by side, products, campaigns, etc. The Cohort table returns your top 14 dimension items. However, you can use a segment to display only desired dimension items. A Custom dimension cohort cannot be used with the Latency table feature.
- Click Build .
- To reconfigure the Cohort table, select .
- (Optional) Create a segment or audience from a selection. Select cells (contiguous or noncontiguous), then right-click > Create Segment From Selection .
- In the Segment builder , further edit the segment, then click Save . The saved segment is available for use in the Segment panel in Analysis Workspace.

## Settings

You can define specific settings for a Cohort table.

- Select to adjust the Cohort table settings. table 0-row-2 1-row-2 2-row-2 3-row-2 Setting Description Only show percent Removes the number value and only shows the percentage. Round percent to nearest whole Rounds the percent value to the nearest whole instead of showing the decimal value. Show Average Percent Row Inserts a new row at the top of the table and then adds the average for the values within each column.

Related Articles
Add a visualization to a panel
Visualization settings
Visualization context menu
recommendation-more-help
