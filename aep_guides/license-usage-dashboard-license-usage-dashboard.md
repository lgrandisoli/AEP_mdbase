---
title: "License usage dashboard license-usage-dashboard"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/dashboards/guides/license-usage"
category: "guides"
topic: "experience-platform/dashboards-guide"
created_at: "2026-06-26T17:21:25.844988+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Dashboards Guide

# License usage dashboard license-usage-dashboard

Last update: June 18, 2026
- Topics:
- [Dashboards](#)

CREATED FOR:

- Developer
- User

You can view important information about your organization’s license usage through the **License usage** dashboard. The dashboard is available to eligible Experience Cloud organizations, including those that license Adobe Experience Platform and those that do not. The information displayed is captured during a daily snapshot of your organization’s environment and is not updated in real time.

License usage reports provide a high degree of granularity. Most metrics are shared across multiple products and reflect aggregated usage across all products that use them, not per-product totals.

This guide outlines how to access and work with the license usage dashboard in the UI and provides more information regarding the visualizations displayed in the dashboard.

For a general overview of the Experience Platform UI, refer to the [Experience Platform UI guide](/en/docs/experience-platform/landing/platform-ui/ui-guide).

## License usage dashboard data

The License usage dashboard displays a list of all the Experience Platform products that you have purchased and any add-ons for those products. From this dashboard, you can find a snapshot of your organization’s license-related data for Experience Platform across any associated sandbox.

The data in this dashboard is displayed exactly as it appeared at the specific point in time when the snapshot was taken. It is not an approximation or sample, but the dashboard is not updated in real time.

For organizations without an Adobe Experience Platform application (such as Real-time Customer Data Platform, Adobe Journey Optimizer, Customer Journey Analytics, and so on), the dashboard displays AI credit usage metrics only.

NOTE
Most metrics in the dashboard are updated daily, based on a snapshot of your Experience Platform instance. CJA Rows Available is an exception and is updated monthly. Metrics labeled with “packs”, such as Adhoc Query Service Users Packs, Profile Richness No of Packs, and Streaming Segmentation No of Packs, reflect license entitlements for add-on offerings and do not track ongoing usage. Changes made after the snapshot are not visible until the next snapshot is taken.
## Exploring the license usage dashboard explore

To navigate to the license usage dashboard within the Experience Platform UI, select **License usage** in the left rail. The dashboard contains two tabs: **Metrics** and **Products**.

NOTE
The license usage dashboard is not enabled by default. You must be granted the
“View License Usage Dashboard”
permission to access it.
If your organization licenses Adobe Experience Platform applications, grant this permission in the applicable product profile and sandbox.
For organizations without an Adobe Experience Platform application (for example, AEM-only or Workflow-only organizations), this permission is available in the Adobe Admin Console under the Adobe Experience Platform product card (if provisioned for your organization). An administrator must add the permission to a product profile before users can view the dashboard.
## Metrics tab metrics-tab

The **Metrics** tab provides a centralized view of all license usage metrics across your organization. Because most metrics are shared across products, there is no separate per-product breakdown for these metrics.

The metrics table includes the following columns:

Column name
Description
Metric Name
The name of the license usage metric. Each entry includes an info icon (
ⓘ
) that displays a description and list of associated products.
Licensed
The number of units your organization is entitled to use, as defined in your contract. This metric is the same value as the
License Amount
in the Products tab.
Measured
The amount of the metric currently used by your organization.
Usage %
The percentage of your licensed value currently in use.
Predicted Usage %
The forecasted range of metric usage over the next 6 weeks.
Use the **Production** or **Development** sandbox toggle to filter the metrics displayed by sandboxes.

NOTE
Consumption reporting is cumulative by sandbox type. Selecting Production or Development shows combined usage across all sandboxes of that type.
WARNING
Permission to view the license usage dashboard must be specified at a sandbox level. Add permissions to each individual sandbox to view them within the dashboard. This limitation will be addressed in a future release. In the meantime, the following workaround is available:
- Create a product profile in the Adobe Admin Console.
- Under Permission in the Sandbox category, add all sandboxes you wish to view in the license usage dashboard.
- Under the User Dashboard Permission category, add “View License Usage Dashboard” permission.

### View metric details view-metric-details

To view usage details for a specific metric, select a metric name in the list. A detailed view of the metric appears, including:

- A historical line graph showing usage over time
- A comparison of licensed and measured values
- Usage by individual sandbox
- A sandbox selector to filter data
- An export option for CSV download

This visualization allows you to track trends, understand how each sandbox contributes to overall usage, and export the data for offline analysis.

Each chart includes dropdown menus to filter the data. Use the date range dropdown to adjust the lookback period (default: last 30 days) or use the sandbox dropdown to view usage for a specific Production or Development sandbox.

You can also select a **Custom date** to choose the time period that is shown.

### CSV export export-metric-usage-data

You can export historical usage data for the selected metric and sandbox as a CSV file directly from the metric detail view. Select the **Export** icon to download the chart’s data in tabular format. The exported CSV makes it easy to analyze trends offline or share usage insights across teams.

## Products tab products-tab

The **Products** tab presents license usage data grouped by purchased products and any associated add-ons. The Products tab contains two tables:

- **Core products table**: This table lists the main Adobe Experience Platform products licensed by your organization. Each product lists its primary metric, usage tracking, and predicted usage.
- **Add-ons table**: Lists supplementary items whose license amounts contribute to core product metrics. Add-ons do not have separate metrics but enhance the usage tracking of the core products they are associated with.

Column name
Description
Product
The Adobe solution licensed by your organization.
Primary Metric
The primary metric used for tracking within that product.
License Amount
The contracted value for the maximum amount of the primary metric.
Usage
The amount of your primary metric used.
Usage %
The percentage of your primary metric used according to your license amount.
Predicted Usage
The predicted usage percentage of your primary metric.
NOTE
The License Amount for add-ons is included in the total license amount of the core product. Add-ons are not tracked separately but enhance the capabilities of their associated products. For example, if you buy one pack of five sandboxes as an add-on, the amount is added to that of the base product. The add-ons table shows a License Amount specific to the add-on, but the actual usage is tracked through the base product.
### Predicted usage predicted-usage

Proactively manage and optimize your licensing resources with accurate, up-to-date usage predictions. The Predicted Usage column forecasts future license usage at the sandbox level across all production and development sandboxes for all purchased products. Predictions now update weekly, providing a six-week forecast based on the latest usage data. Each prediction includes both a lower and upper bound to support informed planning.

IMPORTANT
Predictions are refreshed on a weekly basis every Friday. The date of refresh is included in an info icon (
) above the column title.
View a summary of a product’s entitlement usage from the Product tab under the Core products table.

NOTE
Please note that license usage predictions are approximations based on past usage. You are responsible for understanding your organization’s actual usage and ensuring that usage does not go beyond the scope of your organization’s license with Adobe.
The percentage of predicted usage is determined as follows:

- If the lower and upper bounds are significantly different, they are displayed as a range (for example, 32% - 35%).
- If the lower and upper bounds are nearly identical and not zero, they are displayed as an approximated value (for example, ~34%).
- If the lower and upper bounds are nearly identical and zero, they are displayed as exactly 0%.

NOTE
“Nearly identical” in this context means that the values are statistically significant to two decimal places (for example, a lower bound of 0.342 and an upper bound of 0.344 are both rounded to 34%).
The predicted usage feature supports the following metrics:

- Addressable audience
- Businessperson profiles
- Compute hours
- Customer Journey Audience number of rows
- Engageable profiles
- Total Data Volume

## Available metrics available-metrics

IMPORTANT
Starting August 20th, customers with entitlements for ‘Average Profile Richness’ and ‘Total Storage’ instead saw ‘Total Data Volume’ in the License Usage Dashboard. There was no change to customer entitlements, only a simplification of tracking metrics. Total Data Volume represents the data available in Real-Time Customer Profile for engagement and personalization workflows. This simplified metric improved the management and measurement of Real-Time Customer Profile use. Customers were are encouraged to contact their Adobe representative for further clarification on this change.
The metrics that appear in your dashboard depend on the products and entitlements associated with your organization. If your organization participates in the [Adobe Experience Platform Agents usage-bound trial](/en/docs/experience-cloud-ai/experience-cloud-ai/agents/trial) or licenses Adobe Experience Platform Agents, the dashboard includes the AI credits metric. If your organization does not license Adobe Experience Platform, AI credit usage appears as the primary metric.

Metric
Description
AI credits
The number of AI credits consumed by your organization when using Adobe Experience Platform Agents. AI credits are used during the Adobe Experience Platform Agents usage-bound trial and when licensed for paid agent usage. This metric enables you to monitor AI credit consumption against your available entitlement.
Audience Activation Size
The total size of profiles activated to any file-based destination in a year. Note: This does not include profiles sent through streaming destinations.
Addressable Audience
The set of person profiles in Real-Time Customer Profile that your organization is entitled to engage, including both directly identifiable and Pseudonymous Profiles. These profiles may contain attributes, behaviors, and segment membership data. Profile volumes are calculated using Adobe Experience Platform’s default deterministic Identity Graph and are considered a shared feature.
Adhoc Query Service Users Packs
An add-on to increase your authorized concurrent Query Service Users entitlement by five additional concurrent Query Service users and one additional concurrently running ad hoc query per pack. Multiple additional Ad Hoc Query User packs may be licensed.
Average profile richness
Deprecated
- The sum of all production data stored within the Hub Profile Service at any point in time, divided by five times the number of authorized business person profiles. Average profile richness is a shared feature.
CJA Rows Available
The daily average rows of data available for analysis within Customer Journey Analytics.
Computed Attributes
Aggregated profile behavioral data based on experience events that are converted into a Profile attribute and can be included in a Person Profile.
Consumer Audience
The number of person profiles identified as “Consumer Audience” on the sales order.
Data Export Size
The amount of data sent through dataset activations in a year.
Data Exports
The total size of datasets that can be exported to any non-Adobe solution (directly or indirectly) in a year.
Data Lake Storage
The quantity used of the analytical data store within Adobe Experience Platform.
Engageable Audience
A group of person profiles in Real-Time Customer Profile that you have attempted to engage within the past 12 months using Journey Optimizer’s authoring, decisioning, delivery, experimentation, or orchestration capabilities.
Look-alike Audiences
A Consumer Look-Alike Audience is an audience generated by modeling an existing Consumer Audience to identify Person Profiles with similar attributes or behaviors.
Number of AMM Models
A count of the machine learning model (built in Adobe Mix Modeler) used to measure and/or predict a specified outcome based on your investments.
Number of Sandboxes
The count of logical separations within your instance of any Adobe On-demand Service that accesses Adobe Experience Platform isolating data and operations.
Profile Richness No of Packs
An increase in your authorized Total Data Volume by 25 KB per profile for each Additional Profile Richness pack.
Query Service Compute Hours
A measure of the amount of time taken by the Query Service engines to read, process, and write data back into the data lake when a batch query is executed.
Streaming Segmentation No of Packs
The packs update segment membership for a person profile as new data enters the Segmentation Service through a streaming flow. Segment membership is evaluated based on the current person profile attributes and the value of the current event, without taking historical behavior into account. Streaming Segmentation is a shared feature.
Total Data Volume
The total amount of data available for Real-Time Customer Profile to use in engagement workflows. Total Data Volume is calculated using the following formula:
Total Data Volume = Addressable Audience × Average Profile Richness
. This metric reflects data stored only in the Profile Store and excludes data lake storage. It provides a more focused view of data relevant to profile-based engagement. See the
frequently asked questions about Total Data Volume
to learn more.
Total Volume of Data Egress
The cumulative annual volume of data exported from Adobe Experience Platform to third-party data warehouses.
TIP
You can check your license entitlements in your sales order to calculate metrics such as your ‘Storage Allowance’.
For example,
- Storage Allowance = The number of “authorized profiles” in your contract X Average Profile Richness

The availability of these metrics and the specific definition of each of these metrics varies depending on the licensing that your organization has purchased. For detailed definitions of each metric, refer to the appropriate Product Description documentation:

License
Product Description
- ADOBE EXPERIENCE PLATFORM:OD LITE
- ADOBE EXPERIENCE PLATFORM:OD STANDARD
- ADOBE EXPERIENCE PLATFORM:OD HEAVY

Adobe Experience Platform
- ADOBE EXPERIENCE PLATFORM:OD

Experience Platform, App Services, and Intelligent Services
- RT CUSTOMER DATA PLATFORM:OD
- RT CUSTOMER DATA PLATFORM:OD PRFL TO 10M
- RT CUSTOMER DATA PLATFORM:OD PRFL TO 50M

Adobe Real-Time Customer Data Platform
- AEP:OD ACTIVATION
- AEP:OD ACTIVATION PRFL TO 10M
- AEP:OD ACTIVATION PRFL UP TO 50M

Adobe Experience Platform Activation
- AEP:OD INTELLIGENCE

Adobe Experience Platform Intelligence
- JOURNEY OPTIMIZER SELECT:OD
- JOURNEY OPTIMIZER PRIME:OD
- JOURNEY OPTIMIZER ULTIMATE:OD
- UNP AJO PRIME STARTER:OD
- UNP AJO ULTIMATE STARTER:OD
- UNP Real-Time CDP:OD PROFILE ORCHESTRATION

Adobe Journey Optimizer
WARNING
The license usage dashboard only reports on the latest license that has been provisioned for your organization. If the latest license provisioned for your organization does not appear in the table above, the license usage dashboard may not display properly. Support for additional licenses and multiple licenses in a single organization is planned for a future release.
## Next steps

After reading this document, you are able to locate the license usage dashboard and view usage metrics for each purchased product, for all production or development sandboxes, and for a specific sandbox. You can find more information about available metrics for your organization, based on the licensing your organization has purchased.

To learn more about other features available in the Experience Platform UI, refer to the [Experience Platform UI guide](/en/docs/experience-platform/landing/platform-ui/ui-guide).

recommendation-more-help
