---
title: "Customer Journey Analytics BI extension"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/bi-extension"
category: "other"
topic: "analytics-platform/using/cja-dataviews/bi-extension"
created_at: "2026-06-02T19:07:18.440779+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Customer Journey Analytics BI extension

Last update: May 13, 2026
- Topics:
- [BI Extension](#)

CREATED FOR:

- Admin

NOTE
You must have the
Select
package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have.
The Customer Journey Analytics BI extension enables SQL access to the [data views](/en/docs/analytics-platform/using/cja-dataviews/data-views) that you have defined in Customer Journey Analytics. Your data engineers and analysts might be more familiar with Power BI, Tableau Desktop, or other business intelligence and visualization tools (further referred to as BI tools). They can now create reporting and dashboards based on the same data views that Customer Journey Analytics users are using when creating their Analysis Workspace projects.

Adobe Experience Platform [Query Service](/en/docs/experience-platform/query/home) is the SQL interface to data available in the data lake of Experience Platform. With the Customer Journey Analytics BI extension enabled, the functionality of Query Service is extended to see your Customer Journey Analytics data views as tables or views in a Query Service session. As a result, business intelligence tools that use Query Service as their PostgresSQL interface benefit seamlessly from this extended functionality.

The main benefits are:

- No need to recreate an equivalent representation of Customer Journey Analytics data views within the BI tool itself.See [Data views](/en/docs/analytics-platform/using/cja-dataviews/data-views) for more information on the functionality of data views to understand what must be recreated.
- Greater consistency in reporting and analysis between BI tools and Customer Journey Analytics.
- Combine Customer Journey Analytics data with other data sources already available in BI tools.

## Prerequisites

To use this functionality, you can use expiring or non-expiring credentials to connect BI tools to the Customer Journey Analytics BI extension. The [Credentials guide](/en/docs/experience-platform/query/ui/credentials) provides more information on setting expiring credentials or non-expiring credentials.Below are additional steps to set up the required permissions.

### Expiring credentials

To use expiring credentials, you can:

- Grant access to Experience Platform and Customer Journey Analytics.
- Grant Product admin access to Customer Journey Analytics, so you can view, edit, update, or delete connections and data views.

Or you can:

- Grant access to the data views you want to access.
- Grant access to the Customer Journey Analytics BI extension.

### Non-Expiring credentials

To use non-expiring credentials:

- Create non-expiring credentials in Experience Platform . If you want to use already existing non-expiring credentials, ensure these credentials are migrated to OAuth .
- Ensure the non-expiring credential is available for the Customer Journey Analytics product and product profiles. You need to be system administrator for the organization to execute the following steps. Select Admin Console from . Verify that the non-expiring credential is added to the list of API credentials. Select Users from the top menu. Select API credentials from the left rail. The new or migrated non-expiring credentials should be listed and start with EQS-… . Ensure the non-expiring API credential has access to the Customer Journey Analytics product and profiles. Select for the EQS-… non-expiring API credential. From the EQS-… product details pane, select and select Edit API credentials . In the Edit API credentials dialog, validate the Assigned profiles . If no Customer Journey Analytics product is listed: Select and select Customer Journey Analytics . Select one or more product profiles that contain the users that you want to provide access to for Query Service and the BI extension. Select Apply .
- Validate that you see the non-expiring API credential in Experience Platform Query Service. Select Experience Platform from . Select Queries from the left rail. Select Credentials from the top menu. You should see your non-expiring API credential, using the name you provided in step 1, in the Non-expiring credentials list.

See [Customer Journey Access Control](/en/docs/analytics-platform/using/technotes/access-control) for more information, specifically the [Product Admin additional permissions](/en/docs/analytics-platform/using/technotes/access-control#product-admin-additional-permissions) and [Customer Journey Analytics Permissions in the Admin Console](/en/docs/analytics-platform/using/technotes/access-control#customer-journey-analytics-permissions-in-admin-console).

## Usage

To use the Customer Journey Analytics BI extension functionality, you can either use SQL directly or use the drag and drop experience available in the specific BI tool.

### SQL

You can use the functionality directly in SQL statements using either the Query Editor or a standard PostgresSQL command-line interface (CLI) client.

Query editor
In Adobe Experience Platform:

- Select Queries from DATA MANAGEMENT in the left rail.
- Select Create query .
- Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja .
- To execute the query, type your SQL statement and select the button (or press [SHIFT] + [ENTER] ).

PostgresSQL CLI
- Look up and copy your PostgresSQL credentials in Adobe Experience Platform: Select Queries from the left rail (under DATA MANAGEMENT ). Select Credentials from the top bar. Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja . To copy the command string, use in the PSQL command section.
- Open a command or terminal window.
- To log in and start executing your queries, paste the command string in your terminal.

See the [Query Editor UI guide](/en/docs/experience-platform/query/ui/user-guide) for more information.

### BI tools

Currently, the Customer Journey Analytics BI extension is supported and tested for the tools listed below. Other BI tools using the PSQL interface might work as well, but are not yet supported officially.

Power BI
- Look up the details of your PostgresSQL credentials in Adobe Experience Platform: Select Queries from the left rail (under DATA MANAGEMENT ). Select Credentials from the top bar. Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja . Use to copy each of the Postgres credentials parameters (Host, Port, Database, Username, and others) when needed in Power BI.
- In Power BI: In the main window, select Get data from the top toolbar. Select More… in the left rail. In the Get Data screen, search for PostgresSQL and select the PostgresSQL database from the list. In the PostgressSQL database dialog: Paste the Host parameter from Experience Platform Queries Credentials in the Server text field. Paste the Database parameter from Experience Platform Queries Credentials in the Database text field. Add ?FLATTEN to the Database parameter, so it reads like prod:cja?FLATTEN for example. See Flatten nested data structures for use with third-party BI tools for more information. When prompted for Data Connectivity mode, select DirectQuery . You are prompted for Username and Password . Use the equivalent parameters from Experience Platform Queries Credentials. After successful login, the Customer Journey Analytics data view tables appear in Power BIs Navigator . Select the data view tables that you want to use and select Load . All dimensions and metrics associated with one or more selected tables appear in the right pane, ready to be used in your visualizations. See Connect Power BI to Query Service for more information. See also BI extension use cases for a detailed example.

Tableau Desktop
- Look up the details of your PostgresSQL credentials in Adobe Experience Platform: Select Queries from the left rail (under DATA MANAGEMENT ). Select Credentials from the top bar. Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja . Use to copy each of the Postgres credentials parameters (Host, Port, Database, Username, and others) when needed in Tableau Desktop.
- In Tableau Desktop: Select More from To a Server in the left rail. Select PostgresSQL from the list. In the PostgresSQL dialog: Paste the Host parameter from Experience Platform Queries Credentials into the Server text field. Paste the Port parameter from Experience Platform Queries Credentials into the Port text field. Paste the Database parameter from Experience Platform Queries Credentials into the Database text field. Add %3FFLATTEN to the Database parameter, so it reads like prod:cja%3FFLATTEN for example. See Flatten nested data structures for use with third-party BI tools for more information. Select Username and Password from Authentication list. Paste Username parameter from Experience Platform Queries Credentials into Username text field. Paste the Password parameter from Experience Platform Queries Credentials into the Password text field. Select the Sign In . Customer Journey Analytics data views show up as tables in the Table list. Drag the tables that you want to use on the canvas. You can now work with the data from the data view tables to build your reports and visualizations. See Connect Tableau to Query Service for more information. See also BI extension use cases for a detailed example.

Looker
- Look up the details of your PostgresSQL credentials in Adobe Experience Platform: Select Queries from the left rail (under DATA MANAGEMENT ). Select Credentials from the top bar. Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja . Use to copy each of the Postgres credentials parameters (Host, Port, Database, Username, and others) when needed in Looker.
- In Looker: Select Admin from the left rail. Select Connections . Select Add Connection . In the Connect your database to Looker screen, paste the appropriate values when you set up your new connection. Ensure you select PostgreSQL 9.5+ as the dialect. Select Test to test your connection. When successful, select Update to save your connection. You can now work with the data from the data view tables to build your reports and visualizations. See Connect Looker to Query Service for more information. See also BI extension use cases for a detailed example.

Jupyter Noteboook
- Look up the details of your PostgresSQL credentials in Adobe Experience Platform: Select Queries from the left rail (under DATA MANAGEMENT ). Select Credentials from the top bar. Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja . Use to copy each of the Postgres credentials parameters (Host, Port, Database, Username, and others) when needed in Jupyter Notebook.
- In Jupyter Notebook: Ensure you use the required libraries. Use the appropriate values when setting up and executing the connection. Test your connection by executing a relevant query. When successful, you can work with the data to build your reports and visualizations. See Connect Jupyter Notebook to Query Service for more information. See also BI extension use cases for a detailed example.

RStudio
- Look up the details of your PostgresSQL credentials in Adobe Experience Platform: Select Queries from the left rail (under DATA MANAGEMENT ). Select Credentials from the top bar. Select the cja database for your sandbox from the list of databases in the Database drop-down menu. For example prod:cja . Use to copy each of the Postgres credentials parameters (Host, Port, Database, Username, and others) when needed in Jupyter Notebook.
- In RStudio: Ensure you use the required libraries. Use the appropriate values when setting up and executing the connection. Test your connection by executing a relevant query. When successful, you can work with the data to build your reports and visualizations. See Connect RStudio to Query Service for more information. See also BI extension use cases for a detailed example (that is using the RPostgres package instead).

See [Connect clients to Query Service](/en/docs/experience-platform/query/clients/overview) for an overview of and more information on the various tools available.

See [Use cases](/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/bi-extension-usecases) on how to accomplish a number of use cases using the Customer Journey Analytics BI extension.

## Functionality

By default, your data views have a table-safe name generated from their friendly name. For example, the data view named My Web Data View has the view name my_web_data_view. You can define a preferred name to use in your BI tool for your data view. See [Data view settings](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#settings) for more information.

If you want to use the data view IDs as the table names, you can add the optional CJA_USE_IDS setting to your database name when connecting. For example, prod:cja?CJA_USE_IDS shows your data views with names like dv_ABC123.

### Data governance

The data governance-related settings in Customer Journey Analytics are inherited from Adobe Experience Platform. The integration between Customer Journey Analytics and Adobe Experience Platform Data Governance allows for labeling of sensitive Customer Journey Analytics data and enforcement of privacy policies.

Privacy labels and policies that were created on datasets consumed by Experience Platform can be surfaced in the Customer Journey Analytics data views workflow. Therefore, data queried using the Customer Journey Analytics BI extension show appropriate warnings or errors when not complying with the privacy labels and policies defined.

### List data views

In the standard PostgreSQL CLI, you can list your views using \dv

```
prod:all=> \dv
                       List of relations
 Schema |                    Name                    | Type |  Owner
--------+--------------------------------------------+------+----------
 public | my_web_data_view                           | view | postgres
 public | my_mobile_data_view                        | view | postgres
```

### Nested versus flattened

By default, the schema of your data views uses nested structures, just like the original XDM schemas. The integration also supports the FLATTEN option. You can use this option to force the schema for the data views (and any other table in the session) to be flattened. Flattening allows for easier use in BI tools that don’t support structured schemas. See [Working with nested data structures in Query Service](/en/docs/experience-platform/query/key-concepts/flatten-nested-data) for more information.

### Defaults and limitations

The following additional defaults and limitations apply when using the BI Extenion:

- The BI extension requires a row limit for the query results. The default is 50, but you can override this in SQL using LIMIT n , where n is 1 - 50000.
- The BI extension requires a date range to limit the rows used for calculations. The default is the last 30 days, but you can override this in your SQL WHERE clause using the special timestamp or daterange columns.
- The BI extension requires aggregate queries. You can’t use SQL like SELECT * FROM ... to get the raw, underlying rows. At a high level, your aggregate queries should use: Select totals using SUM and/or COUNT . For example, SELECT SUM(metric1), COUNT(*) FROM ... Select metrics broken down by a dimension. For example, SELECT dimension1, SUM(metric1), COUNT(*) FROM ... GROUP BY dimension1 Select distinct metric values. For example, SELECT DISTINCT dimension1 FROM ... See for more details Supported SQL .

### Supported SQL

See [Query Service SQL reference](/en/docs/experience-platform/query/sql/overview) for the full reference on what type of SQL is supported.

See the table below for examples of the SQL you can use.

Examples
| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 layout-auto |  |
| --- | --- |
| Pattern | Example |
| Schema discovery | code language-none SELECT * FROM dv1 WHERE 1=0 | code language-none | SELECT * FROM dv1 WHERE 1=0 |
| code language-none |  |
| SELECT * FROM dv1 WHERE 1=0 |  |
| Ranked or Breakdown | code language-none SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 code language-none SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' AND filterId = '12345' GROUP BY dim1 code language-none SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' AND AND (dim2 = 'A' OR dim3 IN ('X', 'Y', 'Z')) GROUP BY dim1 | code language-none | SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 | code language-none | SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' AND filterId = '12345' GROUP BY dim1 | code language-none | SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' AND AND (dim2 = 'A' OR dim3 IN ('X', 'Y', 'Z')) GROUP BY dim1 |
| code language-none |  |
| SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 |  |
| code language-none |  |
| SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' AND filterId = '12345' GROUP BY dim1 |  |
| code language-none |  |
| SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' AND AND (dim2 = 'A' OR dim3 IN ('X', 'Y', 'Z')) GROUP BY dim1 |  |
| HAVING clause | code language-none SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 HAVING m1 > 100 | code language-none | SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 HAVING m1 > 100 |
| code language-none |  |
| SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 HAVING m1 > 100 |  |
| Distinct, top dimension values | code language-none SELECT DISTINCT dim1 FROM dv1 code language-none SELECT dim1 AS dv1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 code language-none SELECT dim1 AS dv1 FROM dv1 WHERE `timestamp` >= '2022-01-01' AND `timestamp` < '2022-01-02' GROUP BY dim1 ORDER BY SUM(metric1) LIMIT 15 | code language-none | SELECT DISTINCT dim1 FROM dv1 | code language-none | SELECT dim1 AS dv1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 | code language-none | SELECT dim1 AS dv1 FROM dv1 WHERE `timestamp` >= '2022-01-01' AND `timestamp` < '2022-01-02' GROUP BY dim1 ORDER BY SUM(metric1) LIMIT 15 |
| code language-none |  |
| SELECT DISTINCT dim1 FROM dv1 |  |
| code language-none |  |
| SELECT dim1 AS dv1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 |  |
| code language-none |  |
| SELECT dim1 AS dv1 FROM dv1 WHERE `timestamp` >= '2022-01-01' AND `timestamp` < '2022-01-02' GROUP BY dim1 ORDER BY SUM(metric1) LIMIT 15 |  |
| Metric totals | code language-none SELECT SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' | code language-none | SELECT SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' |
| code language-none |  |
| SELECT SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' |  |
| Multi-dimension breakdowns and top-distincts | code language-none SELECT dim1, dim2, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1, dim2 code language-none SELECT dim1, dim2, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY 1, 2 ORDER BY 1, 2 code language-none SELECT DISTINCT dim1, dim2 FROM dv1 | code language-none | SELECT dim1, dim2, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1, dim2 | code language-none | SELECT dim1, dim2, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY 1, 2 ORDER BY 1, 2 | code language-none | SELECT DISTINCT dim1, dim2 FROM dv1 |
| code language-none |  |
| SELECT dim1, dim2, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1, dim2 |  |
| code language-none |  |
| SELECT dim1, dim2, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY 1, 2 ORDER BY 1, 2 |  |
| code language-none |  |
| SELECT DISTINCT dim1, dim2 FROM dv1 |  |
| Subselect: Filter additional results | code language-none SELECT dim1, m1 FROM ( SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 ) WHERE dim1 in ('A', 'B') | code language-none | SELECT dim1, m1 FROM ( SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 ) WHERE dim1 in ('A', 'B') |
| code language-none |  |
| SELECT dim1, m1 FROM ( SELECT dim1, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 ) WHERE dim1 in ('A', 'B') |  |
| Subselect: Querying across data views | code language-none SELECT key, SUM(m1) AS total FROM ( SELECT dim1 AS key, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 UNION SELECT dim2 AS key, SUM(m1) AS m1 FROM dv2 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim2 ) GROUP BY key ORDER BY total | code language-none | SELECT key, SUM(m1) AS total FROM ( SELECT dim1 AS key, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 UNION SELECT dim2 AS key, SUM(m1) AS m1 FROM dv2 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim2 ) GROUP BY key ORDER BY total |
| code language-none |  |
| SELECT key, SUM(m1) AS total FROM ( SELECT dim1 AS key, SUM(metric1) AS m1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim1 UNION SELECT dim2 AS key, SUM(m1) AS m1 FROM dv2 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY dim2 ) GROUP BY key ORDER BY total |  |
| Subselect: Layered source, filtering, and aggregation | Layered using subselects: code language-none SELECT rows.dim1, SUM(rows.m1) AS total FROM ( SELECT _.dim1,_.m1 FROM ( SELECT * FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' ) _ WHERE _.dim1 in ('A', 'B', 'C') ) rows GROUP BY 1 ORDER BY total Layers using CTE WITH: code language-none WITH rows AS ( WITH _ AS ( SELECT * FROM data_ares WHERE `timestamp` BETWEEN '2021-01-01' AND '2021-02-01' ) SELECT _.item, _.units FROM _ WHERE _.item IS NOT NULL ) SELECT rows.item, SUM(rows.units) AS units FROM rows WHERE rows.item in ('A', 'B', 'C') GROUP BY rows.item | code language-none | SELECT rows.dim1, SUM(rows.m1) AS total FROM ( SELECT _.dim1,_.m1 FROM ( SELECT * FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' ) _ WHERE _.dim1 in ('A', 'B', 'C') ) rows GROUP BY 1 ORDER BY total | code language-none | WITH rows AS ( WITH _ AS ( SELECT * FROM data_ares WHERE `timestamp` BETWEEN '2021-01-01' AND '2021-02-01' ) SELECT _.item, _.units FROM _ WHERE _.item IS NOT NULL ) SELECT rows.item, SUM(rows.units) AS units FROM rows WHERE rows.item in ('A', 'B', 'C') GROUP BY rows.item |
| code language-none |  |
| SELECT rows.dim1, SUM(rows.m1) AS total FROM ( SELECT _.dim1,_.m1 FROM ( SELECT * FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' ) _ WHERE _.dim1 in ('A', 'B', 'C') ) rows GROUP BY 1 ORDER BY total |  |
| code language-none |  |
| WITH rows AS ( WITH _ AS ( SELECT * FROM data_ares WHERE `timestamp` BETWEEN '2021-01-01' AND '2021-02-01' ) SELECT _.item, _.units FROM _ WHERE _.item IS NOT NULL ) SELECT rows.item, SUM(rows.units) AS units FROM rows WHERE rows.item in ('A', 'B', 'C') GROUP BY rows.item |  |
| Selects where the metrics come before or are mixed with the dimensions | code language-none SELECT SUM(metric1) AS m1, dim1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY 2 | code language-none | SELECT SUM(metric1) AS m1, dim1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY 2 |
| code language-none |  |
| SELECT SUM(metric1) AS m1, dim1 FROM dv1 WHERE `timestamp` BETWEEN '2022-01-01' AND '2022-01-02' GROUP BY 2 |  |

### Dimensions

You can select any of the dimensions available by default or defined in the data view. You select a dimension by its ID.

### Metrics

The metrics available to select are:

- Any of the metrics available by default;
- Defined in the data view;
- Calculated metrics that are compatible with the data view that the user has access to.

You select a metric by its ID wrapped in a SUM(metric) expression just like you would do with other SQL sources.

You can use:

- SELECT COUNT(*) or COUNT(1) to get the occurrences metric.
- SELECT COUNT(DISTINCT dimension) or SELECT APPROX_COUNT_DISTINCT(dimension) to count the approximate distinct values of a dimension. See details in [Counting distinct values](#counting-distinct-values).
- [Inline calculations](#inline-calculations) to combine metrics on the fly and/or doing math on them.

#### Counting distinct values

Due to the underlying nature of how Customer Journey Analytics works, the only dimension you can get an exact distinct count for is the adobe_personid dimension. The following SQL statements SELECT COUNT(DISTINCT adobe_personid) or SELECT APPROX_COUNT_DISTINCT(adobe_personid) return the value of the default persons metric, which is the count of distinct people. For other dimensions, an approximate distinct count is returned.

#### Conditional metrics

You can embed an IF or CASE clause in the SUM or COUNT functions to add additional segmenting that is specific to a selected metric. Adding these clauses is similar to applying a segment to a metric column in a Workspace report table.

Examples:

```
SUM(IF(dim1 = 'X' AND dim2 = 'A', metric1, 0)) AS m1
```

```
SUM(CASE WHEN dim1 = 'X' AND dim2 = 'A' THEN metric1 END) AS m1
```

#### Inline calculations

You can apply additional math to metric expressions in your SELECT. This math can be used instead of defining the math in a calculated metric. The following table lists what types of expressions are supported.

Operator or Function
Details
+
,
-
,
*
,
/
, and
%
Add, subtract, multiply, divide, and modulous/remainder
-X
or
+X
Changing the sign or a metric where X is the metric expression
PI()
π constant
POSITIVE
,
NEGATIVE
,
ABS
,
FLOOR
,
CEIL
,
CEILING
,
EXP
,
LN
,
LOG10
,
LOG1P
,
SQRT
,
CBRT
,
DEGREES
,
RADIANS
,
SIN
,
COS
,
TAN
,
ACOS
,
ASIN
,
ATAN
,
COSH
,
SINH
, and
TANH
Unary math functions
MOD
,
POW
,
POWER
,
ROUND
,
LOG
Binary math functions
### Special columns

#### Timestamp

The timestamp special column is used to provide the date ranges for the query. A date range can be defined with a BETWEEN expression or a pair of timestamp >, >=, <, <= checks ANDed together.The timestamp is optional and if no full range is provided, defaults are used:

- If only a minimum is provided (timestamp > X or timestamp >= X), the range is from X to now.
- If only a max is provided (timestamp < X or timestamp <= X), the range is from X minus 30 days to X.
- If nothing is provided, the range is from now minus 30 days to now.

The timestamp range is converted to a date range global segment in the RankedRequest.The timestamp field can also be used in date/time functions to parse or truncate the event timestamp.

#### Date range

The daterange special column works similar to timestamp; however the segmenting is limited to full days. The daterange is also optional and has the same range defaults as timestamp.The daterange field can also be used in date/time functions to parse or truncate the event date.

The daterangeName special column can be used to segment your query using a named date range like Last Quarter.

NOTE
Power BI is not supporting
daterange
metrics that are less than a day (hour, 30 minute, 5 minute, etc.).
#### Segment ID

The filterId special column is optional and is used to apply an externally defined segment to the query. Applying an externally defined segment to a query is similar to dragging a segment on a panel in Workspace. Multiple segment IDs can be used by AND-ing them.

Along with filterId, you can use filterName to use a segment’s name instead of ID.

### Where clause

The WHERE clause is handled in three steps:

- Find the date range from the timestamp , daterange , or daterangeName special fields.
- Find any externally defined filterId s or filterName s to include in the segment.
- Turn the remaining expressions into ad-hoc segments.

The handling is done by parsing the first level of ANDs in the WHERE clause. Each top-level AND-ed expression must match one of the above. Anything deeper than the first level of ANDs, or, if the WHERE clause uses ORs at the top level, is handled as an ad-hoc segment.

### Sorting order

By default, the query sorts the results by the first selected metric in descending order. You can overwrite the default sorting order by specifying ORDER BY ... ASC or ORDER BY ... DESC. If you use ORDER BY, you must specify ORDER BY on the first selected metric.

You can also flip the order by using - (minus) in front of the metric. Both statements below result in the same ordering:

```
ORDER BY metric1 ASC
```

```
ORDER BY -metric1 DESC
```

### General function support

Function
Example
Details
Cast
CAST(`timestamp` AS STRING)
or
`timestamp`::string
Type casting is not currently supported, but no error is thrown. The
CAST
function is ignored.
Timestamp
WHERE `timestamp` >= TIMESTAMP('2022-01-01 00:00:00') AND `timestamp` < TIMESTAMP('2022-01-02 00:00:00')
Parse a time string as a timestamp for use within a
WHERE
clause.
To timestamp
WHERE `timestamp` >= TO_TIMESTAMP('01/01/2022', 'MM/dd/yyyy') AND `timestamp` < TO_TIMESTAMP('01/02/2022', 'MM/dd/yyyy')
Parse a time string as a timestamp for use within a
WHERE
clause, optionally providing a format for that time string.
Date
WHERE `timestamp` >= DATE('2022-01-01') AND `timestamp` < DATE('2022-01-02')
Parse a date string as a timestamp for use within a
WHERE
clause.
To date
WHERE `timestamp` >= TO_DATE('01/01/2022', 'MM/dd/yyyy') AND `timestamp` < TO_DATE('01/02/2022', 'MM/dd/yyyy')
Parse a date string as a timestamp for use within a
WHERE
clause, optionally providing a format for that date string.
### Dimension function support

These functions can be used on dimensions in the SELECT, WHERE clause, or in conditional metrics.

**String functions**

Function
Example
Details
Lower
SELECT LOWER(name) AS lower_name
Generate a dynamic dimension identity on the passed in field.
**Date-time functions**

Function
Example
Details
Year
SELECT YEAR(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Month
SELECT MONTH(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Day
SELECT DAY(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Day of week
SELECT DAYOFWEEK(`timestamp`)
Generate a dynamic dimension identity on the passed in field. Use the item ID instead of the value as you need the number not the friendly name.
Day of year
SELECT DAYOFYEAR(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Week
SELECT WEEK(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Quarter
SELECT QUARTER(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Hour
SELECT HOUR(`timestamp`)
Generate a dynamic dimension identity on the passed in field. Use the item ID instead of the value as you need the number not the friendly name.
Minute
SELECT MINUTE(`timestamp`)
Generate a dynamic dimension identity on the passed in field.
Extract
SELECT EXTRACT(MONTH FROM `timestamp`)
Generate a dynamic dimension identity on the passed in field. Use the item ID instead of the value for some parts of this function as you need the number not the friendly name.
Supported parts are:
- Keywords:
YEAR
,
MONTH
,
DAYOFMONTH
,
DAYOFWEEK
,
DAYOFYEAR
,
WEEK
,
QUARTER
,
HOUR
,
MINUTE
.
- Strings:
'YEAR'
,
'Y'
,
'MONTH'
,
'M'
,
'DAYOFMONTH'
,
'DAY'
,
'D'
,
'DAYOFWEEK'
,
'DOW'
,
'DAYOFYEAR'
,
'DOY'
,
'WEEK'
,
'WOY
’,
'W'
,
'QUARTER'
,
'QOY'
,
'Q'
,
'HOUR'
, or
'MINUTE'
.
Date (part)
SELECT DATE_PART('month', `timestamp`)
Generate a dynamic dimension identity on the passed in field. Use the item ID instead of the value for some parts of this function as you need the number not the friendly name.
Supported string parts are:
'YEAR'
,
'Y'
,
'MONTH'
,
'M'
,
'DAYOFMONTH'
,
'DAY'
,
'D'
,
'DAYOFWEEK'
,
'DOW'
,
'DAYOFYEAR'
,
'DOY'
,
'WEEK'
,
'WOY
’,
'W'
,
'QUARTER'
,
'QOY'
,
'Q'
,
'HOUR'
, or
'MINUTE'
.
Date (truncated)
SELECT DATE_TRUNC('quarter', `timestamp`)
Generate a dynamic dimension identity on the passed in field.
Supported string granularities are:
'YEAR'
,
'Y'
,
'MONTH'
,
'M'
,
'DAYOFMONTH'
,
'DAY'
,
'D'
,
'DAYOFWEEK'
,
'DOW'
,
'DAYOFYEAR'
,
'DOY'
,
'WEEK'
,
'WOY
’,
'W'
,
'QUARTER'
,
'QOY'
,
'Q'
,
'HOUR'
, or
'MINUTE'
.
### Partial Support

Some SQL functionality is only partially supported with the BI extension and does not return the same results you see with other databases. This specific functionality is used in SQL generated by various BI tools, for which the BI extension does not have an exact match. As a result, the BI extension focuses on a limited implementation that covers the minimum BI tool usage without throwing errors. See the table below for more details.

Function
Example
Details
MIN() & MAX()
MIN(daterange)
or
MAX(daterange)
MIN()
on
timestamp
,
daterange
, or any of the
daterangeX
like
daterangeday
will return 2 years ago.
MAX()
on
timestamp
,
daterange
, or any of the
daterangeX
like
daterangeday
will return the current date/time.
MIN()
or
MAX()
on any other dimmension, metric, or expression will return 0.
recommendation-more-help
