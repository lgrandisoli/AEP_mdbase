---
title: "Derived fields derived-fields"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-dataviews/derived-fields"
category: "other"
topic: "analytics-platform/using/cja-dataviews/derived-fields"
created_at: "2026-06-23T20:42:07.139079+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Derived fields derived-fields

Last update: May 13, 2026
- Topics:
- [Analysis Workspace](#)
- [Components](#)

CREATED FOR:

- Admin

Derived fields are an important aspect of the real-time reporting functionality in Adobe Customer Journey Analytics. A derived field allows you to define (often complex) data manipulations on the fly, through a customizable rule builder. You can then use that derived field as a component (metric or dimension) in [Workspace](/en/docs/analytics-platform/using/cja-workspace/home) or even further define the derived field as a component in [Data view](/en/docs/analytics-platform/using/cja-dataviews/data-views).

Derived fields can save a significant amount of time and effort, compared to transforming or manipulating your data in other locations outside of Customer Journey Analytics. Such as [Data Prep](/en/docs/experience-platform/data-prep/home), [Data Distiller](/en/docs/experience-platform/query/data-distiller/overview), or within your own Extract Transform Load (ETL) / Extract Load Transform (ELT) processes.

Derived fields are defined within [Data views](/en/docs/analytics-platform/using/cja-dataviews/data-views), are based on a set of functions defined as rules, and applied to available standard and/or schema fields.

NOTE
Standard components
are tied to and associated with event datasets. As a result, standard components that are used as part of a derived field only work against data from an event dataset.
Example use cases are:

- Define a derived Page Name field that corrects improper collected page name values to correct page name values.
- Define a derived Marketing Channel field that determines the proper marketing channel based on one or more conditions (for example URL parameter, page URL, page name).

Standard components are only supported on event datasets in derived fields.

TIP
See
guidelines
for best practices, guardrails, and common pitfalls when working with derived fields.
## Derived field interface interface

When you create or edit a derived field, you use the derived field interface.

Name
Description
1
Selector
You use the selector area to select and drag and drop your function, function template, schema field, or standard field on to the rule builder.
Use the drop-down to select between:
Functions - lists available
functions
,
Function templates - lists available
function templates
,
Schema fields - lists fields available from dataset categories (event, profile, lookup) and previously defined derived fields, and
Standard fields - standard available fields (like Platform Dataset ID). Only string and numeric standard fields are displayed in the selector. If the function supports other data types, standard fields with these other data types can be selected for values or fields within the rule interface.
You can search for function, function templates, schema, and standard fields using the
Search box.
You can filter the selected object list by selecting
Filter and specify filters in the Filter fields by dialog. You can easily remove filters using
for each filter.
2
Rule builder
You build your derived field sequentially using one or more rules. A rule is a specific implementation of a function and is therefore always associated with only one function. You create a rule by dragging and dropping a function into the rule builder. The function type determines the interface of the rule.
See the
Rule interface
for more information.
You can insert a function at the start, end, or in between rules already available in the rule builder. The last rule in the rule builder determines the final output of the derived field.
3
Field Settings
You can name and describe your derived field and inspect its field type.
4
Final Output
This area shows an on-the-fly updated preview of output values, based on data over the last 30 days and the changes you make to the derived field in the rule builder.
## Field template wizard wizard

When you access the derived field interface for the first time, the Start with a field template wizard is shown.

- Select the template that best describes the type of field you are trying to create.
- Select the **Select** button to continue.

Your derived field dialog is populated with rules (and functions) required or useful for the type of field that you selected. See [Function templates](#function-templates) for more information on the available templates.

## Rule interface rules

When you define a rule in the rule builder, you use the rule interface.

Name
Description
A
Rule Name
By default the rule name is
Rule X
(X referring to a sequence number). To edit the name of a rule, select its name and type in the new name, for example
Query Parameter
.
B
Function Name
The selected function name for the rule, for example URL PARSE. When the function is the last in the sequence of functions and determines the final output values, the function name is followed by - FINAL OUTPUT, for example URL PARSE - FINAL OUTPUT.
To show a popup with more information on the function, select
.
C
Rule Description
You can optionally add a description to a rule.
Select
, then select
Add Description
to add a description or
Edit Description
to edit an existing description.
Use the editor to enter a description. You can use the toolbar to format the text (using style selector, bold, italic, underline, right, left, centered, color, number list, bullet list) and adding links to external information.
To finish editing the description, click outside of the editor.
D
Function Area
Defines the logic of the function. The interface depends on the type of function. The drop-down menufor Field or Value shows all categories of fields (rules, standard fields, fields) available, based on the type of input the function expects. Alternatively, you can drag and drop a field from the Schema and Standard fields selector on to a Field or Value. When that dragged field is originating from a Lookup dataset, a Lookup function is automatically inserted before the function you define.
See
Function reference
on detailed information for each of the functions supported.
## Create a derived field create

- Select an existing Data view or create a Data view. See Data views for more information.
- Select the Components tab of the Data view.
- Select Create derived field from the left rail.
- To define your derived field, use the Create derived field interface. See Derived field interface . To save your new derived field, select Save .
- Your new derived field is added to the Derived fields > container, as part of Schema fields in the left rail of your Data view.

## Edit a derived field edit

- Select an existing Data view. See Data views for more information.
- Select the Components tab of the Data view.
- Select Schema fields tab in the Connection pane on the left.
- Select Derived fields > container.
- Hover over the derived field that you want to edit, and select .
- To edit your derived field, use the Edit derived field interface. See Derived field interface . Select Save to save your updated derived field. Select Cancel to cancel any changes you made to the derived field. Select Save As to save the derived field as a new derived field. The new derived field has the same name as the original edited derived field with (copy) added to it.

Alternatively, if you have used a derived field as a component for dimensions or metrics in your data view:

- Select the component. Note that the component might have a different name than your derived field.
- In the Component panel, select the next to your derived field, underneath Schema field name.
- To edit your derived field, use the Edit derived field interface. See Derived field interface . Select Save to save your updated derived field. Select Cancel to cancel any changes you made to the derived field. Select Save As to save the derived field as a new derived field. The new derived field has the same name as the original edited derived field with (copy) added to it.

## Delete a derived field delete

- Select an existing Data view. See Data views for more information.
- Select the Components tab of the Data view.
- Select Schema fields tab in Connection pane.
- Select Derived fields > container.
- Hover over the derived field that you want to delete, and select .
- In the Edit derived field interface, select Delete . A Delete component dialog asks you to confirm the deletion. Consider any external references there might exist to the derived field outside of the Data view. Select Continue to delete the derived field.

Alternatively, if you have used a derived field as a component for dimensions or metrics in your data view:

- Select the component. Note that the component might have a different name than your derived field.
- In the Component panel, select the next to your derived field, underneath Schema field name.
- In the Edit derived field interface, select Delete . A Delete component dialog asks you to confirm the deletion. Consider any external references there might exist to the derived field outside of the Data view. Select Continue to delete the derived field.

NOTE
Derived fields are managed at a Connection level in Customer Journey Analytics. Any change made to a derived field in any of the Data views associated with that Connection applies across all these associated Data views.
## Function templates templates

To quickly create a derived field for specific use cases, function templates are available. These function templates can be accessed from the selector area in the derived field interface or are presented upon first use in the Start with a field template wizard.

### Marketing channels mchannel

This function template uses a collection of rules to build marketing channels.

Details
To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Bounces bounces

This function template uses a collection of rules to identify site bounces.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Multi-Dimension Combine multi-dim

This function template combines two values into one.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Friendly Dataset Name friendlyname

This function template provides a readable dataset name.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Page Name from URL pagename

This function template creates a simple page name.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Holiday Season holiday

This function template classifies key times of the year.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Monthly Goals goals

This function template sets custom monthly goals.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Get All Values in Delimited List allvalues

This function template converts a limited list to an array.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Get First Value in Delimited List firstvalue

This function template gets the first value in a delimited list.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Get Last Value in Delimited List lastvalue

This function template gets the last value in a delimited list.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Domain Name domain

This function template extracts the domain name using a regular expression.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Get Query String Parameter querystring

This function template extracts query string values for the specified query parameter. The query parameter is case sensitive. Insert a [Lowercase](#lowercase) function to ensure all upper and lower case variations of the query parameter are considered.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Transition Field transition

This function template transitions reporting from one field to another field.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Simple Bot Detection botdetection

This function template implements light bot identification.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Exit Link exit

This function template identifies last link clicked in a session.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### Download Link download

This function template flags common download links.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### State Latitude state-latitude

This function template gets the latitude for a US state with a precision of 5 digits.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### State Longitude state-longitude

This function template gets the longitude for a US state with a precision of 5 digits.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the correct parameters for each function listed as part of the rules in the template. See [Function reference](#function-reference) for more information.

### UTM Parameters Parse

This function template extracts the value of specified UTM query parameters (e.g., utm_source, utm_campaign) from the selected URL field. Use this function to label and group events by campaign attribution for marketing reporting.

Details
| note |
| --- |
| NOTE |
| You must have the **Select** package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have. |

To use the template, you have to specify the parameters for each function listed as part of the rules in the template. Remove functions (for example [Parse URL](#url-parse)) or parameters in functions (for example for [Concatenate](#concatenate) and [Case When](#case-when)) for the UTM query parameters you do not use. See [Function reference](#function-reference) for more information.

## Function reference functionref

NOTE
You must have the
Select
package or higher in order to use the functionality described in this section. Contact your administrator if you’re unsure which Customer Journey Analytics package you have.
For each supported function, find details below on:

- specifications: input data type: type of data supported, input: possible values for input, included operators: operators supported for this function (if any), limitations: limitations that apply for this specific function, output.
- use cases, including: data before defining the derived field, how to define the derived field, data after defining the derived field.
- constraints (if applicable).

### Case When casewhen

Applies conditionals, based on defined criteria from one or more fields. These criteria are then used to define the values in a new derived field, based on the sequence of the conditions.

Details
## Specifications casewhen-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| String Numeric Date | If, Else If container: Value Rules Standard fields Fields Criterion (see included operators, based on selected value type) Then set value to, Otherwise set value to: Value Rules Standard fields Fields | Strings Equals Equals any term Contains the phrase Contains any term Contains all terms Starts with Starts with any term Ends with Ends with any term Does not equal Does not equal any term Does not contain the phrase Does not contain any term Does not contain all terms Does not start with Does not start with any term Does not end with Does not end with any term Is set Is not set Numeric Equals Does not equal Is greater than Is greater than or equal to Is less than Is less than or equal to Is set Is not set Dates Equals Does not equal Is later than Is later than or equal to Is before Is before or equal to Is set Is not set | 5 functions per derived field 200 operators per derived field. An example of one single operator is ‘Referring Domain contains google’. | New derived field |

## Use case 1 casewhen-uc1

You want to define rules to identify various marketing channels, by applying cascading logic to set a marketing channel field to the proper value:

- If the referrer is from a search engine and the page has a query string value where cid contains ps_, the marketing channel should be identified as a *Paid Search*.
- If the referrer is from a search engine and the page does not have the query string cid, the marketing channel should be identified as a *Natural Search*.
- If a page has a query string value where cid contains em_, the marketing channel should be identified as an *Email*.
- If a page has a query string value where cid contains ds_, the marketing channel should be identified as a *Display Ad*.
- If a page has a query string value where cid contains so_, the marketing channel should be identified as a *Paid Social*.
- If the referrer is from a referring domain of twitter.com, facebook.com, linkedin.com, or tiktok.com, the marketing channel should be identified as a *Natural Social*.
- If none of the above rules are matched, then the marketing channel should be identified as *Other Referrer*.

In case your site receives the following sample events, containing Referrer and Page URL, these events should be identified as follows:

| table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 5-row-4 6-row-4 1-align-center 6-align-center 11-align-center 16-align-center 21-align-center 26-align-center 31-align-center layout-auto |  |  |  |
| --- | --- | --- | --- |
| Event | Referrer | Page URL | Marketing Channel |
| 1 | https://facebook.com | https://site.com/home | Natural Social |
| 2 | https://abc.com | https://site.com/?cid=ds_12345678 | Display |
| 3 |  | https://site.com/?cid=em_12345678 | Email |
| 4 | https://google.com | https://site.com/?cid=ps_abc098765 | Paid Search |
| 5 | https://google.com | https://site.com/?cid=em_765544332 | Email |
| 6 | https://google.com |  | Natural Search |

### Data before casewhen-uc1-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 layout-auto |  |
| --- | --- |
| Referrer | Page URL |
| https://facebook.com | https://site.com/home |
| https://abc.com | https://site.com/?cid=ds_12345678 |
|  | https://site.com/?cid=em_12345678 |
| https://google.com | https://site.com/?cid=ps_abc098765 |
| https://google.com | https://site.com/?cid=em_765544332 |
| https://google.com |  |

### Derived field casewhen-uc1-derivedfield

You define a Marketing Channel derived field. You use the CASE WHEN functions to define rules that create values for the based on existing values for both the Page URL and Referring URL field.

Note the usage of the function URL PARSE to define rules to fetch the values for Page Url and Referring Url before the CASE WHEN rules are applied.

### Data after casewhen-uc1-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 layout-auto |
| --- |
| Marketing Channel |
| Natural Social |
| Display |
| Email |
| Paid Search |
| Email |
| Natural Search |

## Use case 2 casewhen-uc2

You have collected several different variations of search within your Product Finding Methods dimension. To understand the overall performance of search vs. browse, you must spend a great deal of time combining the results manually.

Your site collects the following values for your Product Finding Methods dimension. In the end, all of these values indicate a search.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 layout-auto |  |
| --- | --- |
| Collected value | Actual value |
| search p13n_no | search |
| search p13n_yes | search |
| search refine p13n_no | search |
| search refine p13n_yes | search |
| search redirect p13n_yes | search |
| search-redirect | search |

### Data before casewhen-uc2-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 8-row-1 9-row-1 layout-auto |
| --- |
| Product Finding Methods |
| search p13_no |
| search p13_yes |
| browse |
| search refine p13_no |
| search refine p13_yes |
| browse |
| search redirect p13_yes |
| search-redirect |
| browse |

### Derived field casewhen-uc2-derivedfield

You define a Product Finding Methods (new) derived field. You create the following CASE WHEN rules in rule builder. These rules apply logic to all possible variations of the old Product Finding Methods field values for search and browse using the Contains the phrase criterion.

### Data after casewhen-uc2-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 8-row-1 9-row-1 layout-auto |
| --- |
| Product Finding Methods (new) |
| search |
| search |
| browse |
| search |
| search |
| browse |
| search |
| search |
| browse |

## Use case 3 casewhen-uc3

As a travel company, you would like to bucket trip duration for booked trips so you can report on bucketed lengths of trips.

Assumptions:

- The organization is collecting trip duration into a numeric field.
- They would like to bucket 1-3 day durations into a bucket called ‘short trip’
- They would like to bucket 4-7 day durations into a bucket called ‘medium trip’
- They would like to bucket 8+ day durations into a bucket called ‘long trip’
- 132 trips were booked for a 1-day duration
- 110 trips were booked for a 2-day duration
- 105 trips were booked for a 3-day duration
- 99 trips were booked for a 4-day duration
- 92 trips were booked for a 5-day duration
- 85 trips were booked for a 6-day duration
- 82 trips were booked for a 7-day duration
- 78 trips were booked for an 8-day duration
- 50 trips were booked for a 9-day duration
- 44 trips were booked for a 10-day duration
- 38 trips were booked for an 11-day duration
- 31 trips were booked for a 12-day duration

Your desired report should look like:

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Trip Duration Type | Bookings |
| medium trip | 358 |
| short trip | 347 |
| long trip | 241 |

### Data before casewhen-uc3-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 8-row-1 9-row-1 10-row-1 11-row-1 12-row-1 1-align-right 3-align-right 5-align-right 7-align-right 9-align-right 11-align-right 13-align-right 15-align-right 17-align-right 19-align-right 21-align-right 23-align-right 25-align-right |
| --- |
| Trip Duration |
| 1 |
| 12 |
| 3 |
| 6 |
| 4 |
| 8 |
| 6 |
| 2 |
| 1 |
| 2 |
| 21 |
| 8 |

### Derived field casewhen-uc3-derivedfield

You define a Trip Duration (bucketed) derived field. You create the following CASE WHEN rule in rule builder. This rule applies logic to bucket the old Trip Duration field values into three values: short trip, medium trip, and long trip.

### Data after casewhen-uc3-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 8-row-1 9-row-1 10-row-1 11-row-1 12-row-1 |
| --- |
| Trip Duration (bucketed) |
| short trip |
| long trip |
| short trip |
| medium trip |
| medium trip |
| long trip |
| medium trip |
| short trip |
| short trip |
| short trip |
| long trip |
| long trip |

## More information casewhen-more-info

Customer Journey Analytics uses a nested container structure, modeled after Adobe Experience Platform’s [XDM](/en/docs/experience-platform/xdm/home) (Experience Data Model). See [Containers](/en/docs/analytics-platform/using/cja-dataviews/create-dataview#containers) and [Segment containers](/en/docs/analytics-platform/using/cja-components/segments/seg-overview#containers) for more background information. This container model, albeit flexible by nature, imposes some constraints when using the rule builder.

Customer Journey Analytics uses the following default container model:

{width="50%"}

The following constraints apply and are enforced when *selecting* and *setting* values.

| table 0-row-2 1-row-2 2-row-2 3-row-2 1-align-center 4-align-center 7-align-center 10-align-center layout-auto |  |
| --- | --- |
|  | Constraints |
| **A** | Values you *select* within the same If, Else If construct (using And or Or) in a rule must originate from the same container and can be of any type (string , numeric , and so forth). |
| **B** | All the values you *set* across a rule must be from the same container and have the same type or a derived value of the same type. |
| **C** | The values you *select* across If, Else If constructs in the rule do *not* have to originate from the same container and do *not* have to be of the same type. |

### Classify classify

Defines a set of values that are replaced by corresponding values in a new derived field.

Details
## Specifications classify-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| String Numeric Date | Field to classify: Rules Standard fields Fields When value equals and Replace values with: String Show original values Boolean | N/A | 5 functions per derived field 200 operators per derived field. Every entry for When value equals original value Replace value with New value is considered an operation. | New derived field |

## Use case 1 classify-uc1

You do have a CSV-file that includes a key column for hotelID and one or more additional columns associated with the hotelID: city, rooms, hotel name.You are collecting Hotel ID in a dimension but would like to create a Hotel Name dimension derived from the hotelID in the CSV file.

**CSV-file structure and content**

| table 0-row-4 1-row-4 2-row-4 3-row-4 4-row-4 3-align-right 8-align-right 13-align-right 18-align-right 23-align-right layout-auto |  |  |  |
| --- | --- | --- | --- |
| hotelID | city | rooms | hotel name |
| SLC123 | Salt Lake City | 40 | SLC Downtown |
| LAX342 | Los Angeles | 60 | LA Airport |
| SFO456 | San Francisco | 75 | Market Street |
| AMS789 | Amsterdam | 50 | Okura |

**Current Report**

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right layout-auto |  |
| --- | --- |
| Hotel ID | Product Views |
| SLC123 | 200 |
| LX342 | 198 |
| SFO456 | 190 |
| AMS789 | 150 |

**Desired Report**

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Hotel Name | Product Views |
| SLC Downtown | 200 |
| LA Airport | 198 |
| Market Street | 190 |

### Data before classify-uc1-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 layout-auto |
| --- |
| Hotel ID |
| SLC123 |
| LAX342 |
| SFO456 |
| AMS789 |

### Derived field classify-uc1-derivedfield

You define a Hotel Name derived field. You use the CLASSIFY function to define a rule where you can classify values of the Hotel ID field and replace with new values.

If you want to include original values that you have not defined as part of the values to classify (for example Hotel ID AMS789), ensure you select **Show original values**. This ensures AMS789 is part of the output for the derived field, despite that value not being classified.

### Data after classify-uc1-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 layout-auto |
| --- |
| Hotel Name |
| SLC Downtown |
| LA Airport |
| Market Street |

## Use case 2 classify-uc2

You have collected URLs instead of the friendly page name for several pages. This mixed collection of values breaks the reporting.

### Data before classify-uc2-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 layout-auto |
| --- |
| Page Name |
| Home Page |
| Flight Search |
| http://www.adobetravel.ca/Hotel-Search |
| https://www.adobetravel.com/Package-Search |
| Deals & Offers |
| http://www.adobetravel.ca/user/reviews |
| https://www.adobetravel.com.br/Generate-Quote/preview |

### Derived field classify-uc2-derivedfield

You define a Page Name (updated) derived field. You use the CLASSIFY function to define a rule where you can classify values of your existing Page Name field and replace with updated correct values.

### Data after classify-uc2-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 6-row-1 7-row-1 |
| --- |
| Page Name (updated) |
| Home Page |
| Flight Search |
| Hotel Search |
| Package Search |
| Deals & Offers |
| Reviews |
| Generate Quote |

## More information classify-moreinfo

The following additional functionality is available in the Classify rule interface:

- To quickly clear all table values, select **Clear all table values**.
- To upload a CSV file containing original values for When values equal and new values for Replace values with, select **Upload CSV**.
- To download a template for creating a CSV file with original and new values to upload, select **Download CSV template**.
- To download a CSV file with all original and new values populated in the rule interface, select **Download CSV values**.

### Concatenate concatenate

Combines field values into a single new derived field with defined delimiters.

Details
## Specifications concatenate-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| String | Value: Rules Standard fields Fields String Delimiter: String | N/A | 2 functions per derived field | New derived field |

## Use case concatenate-uc

You currently collect origin and destination airport codes as separate fields. You would like to take the two fields and combine them into a single dimension separated by a hyphen (-). So you can analyze the combination of origin and destination to identify top routes booked.

Assumptions:

- Origin and destination values are collected in separate fields in the same table.
- The user determines to use the delimiter ‘-’ between the values.

Imagine the following bookings occur:

- Customer ABC123 books a flight between Salt Lake City (SLC) and Orlando (MCO)
- Customer ABC456 books a flight between Salt Lake City (SLC) and Los Angeles (LAX)
- Customer ABC789 books a flight between Salt Lake City (SLC) and Seattle (SEA)
- Customer ABC987 books a flight between Salt Lake City (SLC) and San Jose (SJO)
- Customer ABC654 books a flight between Salt Lake City (SLC) and Orlando (MCO)

The desired report should look like:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right layout-auto |  |
| --- | --- |
| Origin / Destination | Bookings |
| SLC-MCO | 2 |
| SLC-LAX | 1 |
| SLC-SEA | 1 |
| SLC-SJO | 1 |

### Data before concatenate-uc-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right 17-align-right layout-auto |  |
| --- | --- |
| Origin | Destination |
| SLC | MCO |
| SLC | LAX |
| SLC | SEA |
| SLC | SJO |
| SLC | MCO |

### Derived field concatenate-derivedfield

You define an Origin - Destination derived field. You use the CONCATENATE function to define a rule to concatenate the Original and Destination fields using the - Delimiter.

### Data after concatenate-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 layout-auto |
| --- |
| Origin - Destination(derived field) |
| SLC-MCO |
| SLC-LAX |
| SLC-SEA |
| SLC-SJO |
| SLC-MCO |

### Date Math datemath

Returns the difference between two dates or two date-time fields.

Details
## Specifications datemath-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| Date Date-time | Scope Event Session Person Value: Date Date-Time Static Date (user entered) Static Date-time (user entered) Dynamic Date Today Dynamic Date-time Now Granularity: Seconds Minutes Hours Days Weeks Months Quarters Years For each Date or Date-time return: First (within session or person) Last (within session or person) | N/A | 2 functions per derived field | New derived field |

## Use case 1 datemath-uc1

As the marketing analyst of an hotel company you would like to understand the difference of the number of days between customers check-in dates and booking dates over the last week.

### Derived field datemath-uc1-derivedfield

You define a Days between booking and check-in derived field. You use the DATE MATH function to define a rule to calculate the days for Scope Person between the Booking Date and Check-in Date. You select Day as Output granularity. And you select Return the last for both Booking Date and Check-in Date to ensure the last person scoped value is used in the calculation.

## Use case 2 datemath-uc2

As a marketing analyst of a brick and mortar shop you want to understand how many days ago was the last visit of a customer to the store. You use geolocation functionality within a mobile app and beacons in the shop to capture physical visits of customers.

### Derived field datemath-uc2-derivedfield

You define a new Days Since Visit To Shop derived field. You use the DATE MATH function to define a rule to calculate the days between a Custom Date-Time (which you specify in Date) and the Local Time (from your placeContext field group of your event dataset) with a Deduplication scope of Person. You select Return the last to ensure the last person scoped value for Local time is used in the calculation. You select Day as the Output granularity.

Alternatively, you can use the convenience Dynamic date range value Now to calculate between now and the Local Time (from your placeContext field group of your event dataset)

## Use case 3 datemath-uc3

You want to understand the search time in minutes before a customer within a session places an order.

You define a new Time Between Search And Order In Minutes derived field that is the result of two [CASE WHEN functions](#case-when) to define Search Time and Order Time values.Then you use these two values to calculate the difference with a DATE MATH function with Scope set to Session, values set to Search Time and Order Time and Output granularity set to Minute. For both values you select Return the first to ensure the first Search Time and Order Time is returned.

## More information datemath-more-info

The options for Return the first or Return the last are not available when you select a person-based (from a profile dataset) field. A person-based field can have only one value for a Date or Date-time field for a person.

### Deduplicate dedup

Prevents counting a value multiple times.

Details
## Specifications deduplicate-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| String Numeric | Value: Rules Standard fields Fields String Scope: Person Session Deduplication ID: Rules Standard fields Fields String Value to keep: Keep first instance Keep last instance | N/A | 5 functions per derived field | New derived field |

## Use case 1 deduplicate-uc1

You want to prevent counting duplicate revenue when a user reloads the booking confirmation page. You use the booking confirmation ID at the identifier to not count the revenue again, when received on the same event.

### Data before deduplicate-uc1-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Booking Confirmation ID | Revenue |
| ABC123456789 | 359 |
| ABC123456789 | 359 |
| ABC123456789 | 359 |

### Derived field deduplicate-uc1-derivedfield

You define a Booking Confirmation derived field. You use the DEDUPLICATE function to define a rule to deduplicate the Value Booking for Scope Person using Deduplication ID Booking Confirmation ID. You select Keep first instance as Value to keep.

### Data after deduplicate-uc1-dataafter

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Booking Confirmation ID | Revenue |
| ABC123456789 | 359 |
| ABC123456789 | 0 |
| ABC123456789 | 0 |

## Use case 2 deduplicate-uc2

You use events as a proxy for campaign click-throughs with external marketing campaigns. Reloads & redirects are causing the event metric to be inflated. You would like to deduplicate the tracking code dimension so only the first is collected and minimize the event overcounting.

### Data before deduplicate-uc2-databefore

| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 7-row-3 3-align-right 7-align-right 11-align-right 15-align-right 19-align-right 23-align-right 27-align-right 31-align-right layout-auto |  |  |
| --- | --- | --- |
| Visitor ID | Marketing Channel | Events |
| ABC123 | paid search | 1 |
| ABC123 | paid search | 1 |
| ABC123 | paid search | 1 |
| DEF123 | email | 1 |
| DEF123 | email | 1 |
| JKL123 | natural search | 1 |
| JKL123 | natural search | 1 |

### Derived field deduplicate-uc2-derivedfield

You define a new Tracking Code (deduplicated) derived field. You use the DEDUPLICATE function to define a rule to deduplicate the Tracking Code with a Deduplication scope of Session and Keep first instance as the Value to keep.

### Data after deduplicate-uc2-dataafter

| table 0-row-3 1-row-3 2-row-3 3-row-3 3-align-right 7-align-right 11-align-right 15-align-right layout-auto |  |  |
| --- | --- | --- |
| Visitor ID | Marketing Channel | Events |
| ABC123 | paid search | 1 |
| DEF123 | email | 1 |
| JKL123 | natural search | 1 |

### Depth depth

Returns the depth of a field, similar to what is possible with the out-of-the-box [standard Event Depth dimension](/en/docs/analytics-platform/using/cja-components/dimensions/overview#standard-dimensions).

Details
## Specifications depth-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| Any | Any field | N/A | 3 functions per derived field | New derived field |

## Use case depth-uc1

You want to understand the internal search depth (which you can also interpret as the number of searches). So you can use that internal search depth later to break down on the search term associated with a specific search depth.

### Derived field depth-uc1-derivedfield

You define a new Internal Search Depth derived field. You use the DEPTH function to define a rule to retrieve the depth of Internal Search Term and store that in a new derived field.

And then use that new derived field in a visualization to break down on what term has been used to search for at the first search.

### Find and Replace find-and-replace

Finds all values in a selected field and replaces those values with a different value in a new derived field.

Details
## Specifications findreplace-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limitations | Output |
| String | Value Rules Standard fields Fields Find all, and replace all with: String | Strings Find all, and replace all with | 5 functions per derived field | New derived field |

## Use case findreplace-uc

You have received some malformed values for your external marketing channels report, for example email%20 marketing instead of email marketing. These malformed values fracture your reporting and make it more difficult to see how email is performing. You want to replace email%20marketing with email marketing.

**Original Report**

| table 0-row-2 1-row-2 2-row-2 2-align-right 5-align-right 8-align-right layout-auto |  |
| --- | --- |
| External Marketing Channels | Sessions |
| email marketing | 500 |
| email %20marketing | 24 |

**Preferred Report**

| table 0-row-2 1-row-2 2-align-right 5-align-right |  |
| --- | --- |
| External Marketing Channels | Sessions |
| email marketing | 524 |

### Data before findreplace-uc-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 layout-auto |
| --- |
| External Marketing |
| email marketing |
| email%20marketing |
| email marketing |
| email marketing |
| email%20marketing |

### Derived field findreplace-uc-derivedfield

You define an Email Marketing (updated) derived field. You use the FIND AND REPLACE function to define a rule to find and replace all occurrences of email%20marketing with email marketing.

### Data after findreplace-uc-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 5-row-1 layout-auto |
| --- |
| External Marketing (updated) |
| email marketing |
| email marketing |
| email marketing |
| email marketing |
| email marketing |

### Lookup lookup

Lookup values using a field from a lookup dataset and returns a value in a new derived field or for further rule processing.

Details
## Specification lookup-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric Date | Field to apply lookup: Rules Standard fields Fields Lookup dataset Dataset Matching key Rules Fields Values to return Rules Fields | N/A | 3 functions per derived field | New derived field or value for further processing in next rule |

## Use case lookup-uc

You would like to lookup the activity name using the activity id collected when your customers clicked on a personalized banner shown through Adobe Target. You want to use a lookup dataset with Analytics for Target (A4T) activities containing activity ids and activity names.

### A4T lookup dataset lookup-uc-lookup

| table 0-row-2 1-row-2 2-row-2 3-row-2 layout-auto |  |
| --- | --- |
| Activity Id | Activity Name |
| 415851 | MVT Test Category Pages |
| 415852 | Luma - Campaign Max 2022 |
| 402922 | Home Page Banners |

### Derived field lookup-uc-derivedfield

You define an Activity Name derived field. You use the LOOKUP function to define a rule to lookup the value from your collected data, specified in the Field to apply lookup field (for example **ActivityIdentifier**). You select the lookup dataset from the Lookup dataset list (for example **New CJA4T Activities**). Then you selecting the identifier field (for example **ActivityIdentifier**) from the Matching key list and the field to return from the Values to return list (for example **ActivityName**).

## More information lookup-more-info

The Lookup function is applied at report time to the data retrieved by Customer Journey Analytics from the lookup dataset you have configured as part of your connection.

You can quickly insert a Lookup function in the rule builder, already containing one or more other functions.

- Select **Schema fields** from selector.
- Select **Lookup datasets**.
- Select your lookup dataset and find the field you want to use for lookup.
- Drag and drop the lookup field on any of the available input fields for a function (for example Case When). When valid, a blue box, labeled **+ Add**, allows you to drop the field and automatically insert a Lookup function before the function you dropped the lookup field on. The inserted Lookup function is automatically populated with relevant values for all fields.

### Lowercase lowercase

Converts values from a field to lowercase and stores it into a new derived field.

Details
## Specification lowercase-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric Date | Field: Rules Standard fields Fields | N/A | 2 functions per derived field | New derived field |

## Use case lowercase-uc

You would like to convert all collected product names into lowercase for proper reporting.

### Data before lowercase-uc-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right 17-align-right 20-align-right layout-auto |  |
| --- | --- |
| Collected Product Names | Product Views |
| Tennis racket | 35 |
| Tennis Racket | 33 |
| tennis racket | 21 |
| Baseball bat | 15 |
| Baseball Bat | 12 |
| baseball bat | 10 |

### Derived field lowercase-uc-derivedfield

You define a Product Names derived field. You use the LOWERCASE function to define a rule to convert the value from the Collected Product Names field to lowercase and store that in the new derived field.

### Data after lowercase-uc-dataafter

| table 0-row-2 1-row-2 2-row-2 layout-auto |  |
| --- | --- |
| Product Names | Product Views |
| tennis racket | 89 |
| baseball bat | 37 |

### Math math

Use basic mathematical operators (add, subtract, multiply, divide & raise to a power) on numeric fields.

Details
## Specification math-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| Numeric | One or multiple numeric fields One or multiple operators (add, subtract, multiply, divide, raise to a power) User input value | + (add) - (subtract) * (multiply) / (divide) ^ (raise to power) | 25 operations per derived field 5 Math functions per derived field | New derived field |

## Use case math-uc

Due to inflation you want to correct the revenue numbers of ingested CRM data with 5% inflation.

### Data before math-uc-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right layout-auto |  |
| --- | --- |
| CRM ID | Annual Revenue |
| 1234 | 35,070,000 |
| 4133 | 7,500,000 |
| 8110 | 10,980 |
| 2201 | 42,620 |

### Derived field math-uc-derivedfield

You define a Corrected Annual Revenue derived field. You use the MATH function to define a rule that multiplies the original Annual Revenue number with 1.05.

### Data after math-uc-dataafter

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right layout-auto |  |
| --- | --- |
| CRM ID | Corrected Annual Revenue |
| 1234 | 36,823,500 |
| 4133 | 7,875,000 |
| 8110 | 11,529,00 |
| 2201 | 44,751 |

## More information math-more-info

To create a formula:

- Simply start typing in the Formula field and numeric fields that match what you type will appear in a popup menu. Alternatively, you can drag and drop a numeric field from the available fields in the left pane.
- Add the operand (for example * to multiply) followed by another field or a static value. You can use parenthesis to define more complex formulas.
- To insert a static value (for example 1.05 ), type the value and select Add x as a static value or Add - x as a negative static value from the popup menu.
- A green checkmark indicates whether your math formula is valid, otherwise you will see a warning and the message Invalid formula expression.

There are some important considerations when working with static numbers in the MATH function:

- Static values need to be associated with a field. For example, using the MATH function with only static fields is not supported.
- You cannot use the raise to power operator ( ˆ ) on a static value.
- If you are using multiple static values in a formula, these static values should be grouped using parenthesis for the formula to be valid. For example: This formula returns an error. This formula is valid.

Use the Math function for hit-level based calculations. Use the [Summarize](#summarize) function for event, session or person scope based calculations.

### Merge Fields merge

Merges values from two different fields into a new derived field.

Details
## Specification merge-fields-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric Date | Field: Rules Standard fields Fields | N/A | 5 functions per derived field | New derived field |

## Use case merge-fields-uc

You would like to create a dimension made up from the page name field and the call reason field with the intent of analyzing the journey across channels.

### Data before merge-fields-uc-databefore

| table 0-row-3 1-row-3 2-row-3 3-row-3 2-align-right 3-align-right 6-align-right 7-align-right 10-align-right 11-align-right 14-align-right 15-align-right layout-auto |  |  |
| --- | --- | --- |
| Page Name | Session | Visitors |
| help page | 250 | 200 |
| home page | 500 | 250 |
| product detail page | 300 | 200 |

| table 0-row-3 1-row-3 2-row-3 3-row-3 2-align-right 3-align-right 6-align-right 7-align-right 10-align-right 11-align-right 14-align-right 15-align-right layout-auto |  |  |
| --- | --- | --- |
| Call Reason | Session | Visitors |
| questions about my order | 275 | 250 |
| make a change to my order | 150 | 145 |
| problem with ordering | 100 | 95 |

### Derived field merge-fields-uc-derivedfield

You define a Cross Channel Interactions derived field. You use the MERGE FIELDS function to define a rule to merge the values from the Page Name field and Call Reason field and store that in the new derived field.

### Data after merge-fields-uc-dataafter

| table 0-row-3 1-row-3 2-row-3 3-row-3 4-row-3 5-row-3 6-row-3 2-align-right 3-align-right 6-align-right 7-align-right 10-align-right 11-align-right 14-align-right 15-align-right 18-align-right 19-align-right 22-align-right 23-align-right 26-align-right 27-align-right layout-auto |  |  |
| --- | --- | --- |
| Cross Channel Interactions | Sessions | Visitors |
| home page | 500 | 250 |
| product detail page | 300 | 200 |
| questions about my order | 275 | 250 |
| help page | 250 | 200 |
| make a change to my order | 150 | 145 |
| problem with ordering | 100 | 95 |

## More information merge-fields-moreinfo

You must select the same type of fields within a Merge Fields rule. For example, if you select a Date field, all other fields you want to merge have to be Date fields.

### Next or Previous next-previous

Takes a field as input and resolves the next or previous value for that field within the scope of the session or use. This will only apply to the Visit and Event table fields.

Details
## Specification prevornext-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric | Field: Rules Standard fields Fields Method: Previous value Next value Scope: Person Session Index: Numeric Include repeats: Boolean | N/A | 3 functions per derived field | New derived field |

## Use case prevornext-uc1

You would like to understand what the **next** or **previous** value is of the data that you receive, taken into account repeat values.

### Data prevornext-uc1-databefore

**Example 1 - Handling include repeats**

| table 0-row-5 1-row-5 2-row-5 3-row-5 4-row-5 5-row-5 6-row-5 7-row-5 8-row-5 9-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data received | Next valueSessionIndex = 1Include Repeats | Next valueSessionIndex = 1NOT Include Repeats | Previous valueSessionIndex = 1Include Repeats | Previous valueSessionIndex = 1NOT Include Repeats |
| home | home | search | *No value* | *No value* |
| home | search | search | home | *No value* |
| search | search | product detail | home | home |
| search | product detail | product detail | search | home |
| product detail | search | search | search | search |
| search | product details | product detail | product detail | product detail |
| product detail | search | search | search | search |
| search | search | *No value* | product detail | product detail |
| search | *No value* | *No value* | search | product detail |

**Example 2 - Handling include repeats with blank values in data received**

| table 0-row-5 1-row-5 2-row-5 3-row-5 4-row-5 5-row-5 6-row-5 7-row-5 8-row-5 9-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data received | Next valueSessionIndex = 1Include Repeats | Next valueSessionIndex = 1NOT Include Repeats | Previous valueSessionIndex = 1Include Repeats | Previous valueSessionIndex = 1NOT Include Repeats |
| home | home | search | *No value* | *No value* |
| home | home | search | home | *No value* |
| home | search | search | home | *No value* |
| search | search | product detail | home | home |
| search | search | product detail | search | home |
| search | product detail | product detail | search | home |
| product detail | *No value* | *No value* | search | search |

### Derived field prevnext-uc1-derivedfield

You define a Next Value or Previous value derived field. You use the NEXT OR PREVIOUS function to define a rule that selects the Data received field, select Next value or Previous value as Method, Session as Scope and set the value of Index to 1.

## More information prevnext-moreinfo

You can only select fields that belong to the Visit or Event table.

Include repeats determines how to handle repeating values for the NEXT OR PREVIOUS function.

- Include repeats looks and the next or previous values. If Include Repeats is selected, it will ignore any sequential repeats of next or previous values from the current hit.
- Rows with no (blank) values for a selected field will not have next or previous values returned as part of the NEXT OR PREVIOUS function output.

### Regex Replace regex-replace

Replaces a value from a field using a regular expression into a new derived field.

Details
## Specification regex-replace-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric | Field: Rules Standard fields Fields Regex: String Output Format: String Case sensitive Boolean | N/A | 1 function per derived field | New derived field |

## Use case regex-replace-uc

You would like to grab a potion of a URL and use that as a unique page identifier to analyze traffic. You use [^/]+(?=/$|$) for the regular expression to capture the end of the URL and $1 as the output pattern.

### Data before regex-replace-uc-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 layout-auto |
| --- |
| Page URL |
| https://business.adobe.com/products/analytics/adobe-analytics-benefits.html |
| https://business.adobe.com/products/analytics/adobe-analytics.html |
| https://business.adobe.com/products/experience-platform/customer-journey-analytics.html |
| https://business.adobe.com/products/experience-platform/adobe-experience-platform.html |

### Derived field regex-replace-uc-derivedfield

You create a Page Identifier derived field. You use the REGEX REPLACE function to define a rule to replace value of the Referring URL field using a Regex of [^/]+(?=/$|$) and Output format of $1.

### Data after regex-replace-uc-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 |
| --- |
| Page Identifier |
| adobe-analytics-benefits.html |
| adobe-analytics.html |
| customer-journey-analytics.html |
| adobe-experience-platform.html |

## More information regex-replace-more-info

Customer Journey Analytics uses a subset of the Perl regex syntax. The following expressions are supported:

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 8-row-2 9-row-2 10-row-2 11-row-2 12-row-2 13-row-2 14-row-2 15-row-2 16-row-2 17-row-2 18-row-2 19-row-2 20-row-2 21-row-2 22-row-2 23-row-2 24-row-2 25-row-2 26-row-2 27-row-2 28-row-2 29-row-2 |  |
| --- | --- |
| Expression | Description |
| a | A single character a. |
| a|b | A single character a or b. |
| [abc] | A single character a, b, or c. |
| [^abc] | Any single character except a, b, or c. |
| [a-z] | Any single character in the range of a-z. |
| [a-zA-Z0-9] | Any single character in the range of a-z, A-Z, or digits 0-9. |
| ^ | Matches the beginning of the line. |
| $ | Matches the end of the line. |
| \A | Start of string. |
| \z | End of string. |
| . | Matches any character. |
| \s | Any whitespace character. |
| \S | Any non-whitespace character. |
| \d | Any digit. |
| \D | Any non-digit. |
| \w | Any letter, number, or underscore. |
| \W | Any non-word character. |
| \b | Any word boundary. |
| \B | Any character that is not a word boundary. |
| \< | Start of word. |
| \> | End of word. |
| (...) | Capture everything enclosed. |
| (?:...) | Non-marking capture. Prevents the match from being referenced in the output string. |
| a? | Zero or one of a. |
| a* | Zero or more of a. |
| a+ | One ore more of a. |
| a{3} | Exactly 3 of a. |
| a{3,} | 3 or more of a. |
| a{3,6} | Between 3 and 6 of a. |

You can use these sequences in the Output format any number of times and in any order to achieve the desired string output.

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 layout-auto |  |
| --- | --- |
| Output placeholder sequence | Description |
| $& | Outputs what matched the whole expression. |
| $n | Outputs what matched the nth sub-expression. For example, $1 outputs the first sub-expression. |
| $` | Outputs the text between the end of the last match found (or the start of the text if no previous match was found), and the start of the current match. |
| $+ | Outputs what matched the last marked sub-expression in the regular expression. |
| $$ | Outputs the string character "$". |

### Split split

Splits a value from a field into a new derived field.

Details
## Specification split-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric | Field: Rules Standard fields Fields Method: From the left From the right Convert to array For Delimiter: String For Index: Numeric | N/A | 2 functions per derived field Returns a maximum of 10 values | New derived field |

## Use case 1 split-uc1

You collect voice app responses into a delimited list in a single dimension. You would like each value in the list to be a unique value in the responses report.

### Data before split-uc1-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Voice App Responses | Events |
| it was great,made perfect sense,will recommend to others | 1 |
| it was great,somewhat confusing,will recommend to others | 1 |
| it was not great,very confusing,will not recommned to others | 1 |

### Derived field split-u1-derivedfield

You create a Responses derived field. You use the SPLIT function to define a rule to use the Convert to array method to convert the values from the Voice App Response field using , as the Delimiter.

### Data after split-uc1-dataafter

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right 17-align-right 20-align-right 23-align-right layout-auto |  |
| --- | --- |
| Responses | Events |
| it was great | 2 |
| will recommend to others | 2 |
| it was not great | 1 |
| made perfect sense | 1 |
| somewhat confusing | 1 |
| very confusing | 1 |
| will not recommend to others | 1 |

## Use case 2 split-uc2

You collect voice app responses into a delimited list in a single dimension. You would like the responses from the first value in the list into its own dimension. You would like to put the last value in the list into its own dimension.

### Data before split-uc2-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Responses | Events |
| it was great,made perfect sense,will recommed to others | 1 |
| it was great,somewhat confusing,will recommend to others | 1 |
| it was not great,very confusing,will not recommned to others | 1 |

### Derived field split-u2-derivedfield

You create a First Response derived field. You use the SPLIT function to define a rule to take the first value from the Responses field from the left of the response , as the delimiter.

You create a Second Response derived field to take the last value from the Responses field by selecting From the right, 1 as the Delimiter and 1 as the Index.

### Data after split-uc2-dataafter

| table 0-row-2 1-row-2 2-row-2 2-align-right 5-align-right 8-align-right layout-auto |  |
| --- | --- |
| First Response | Events |
| it was great | 2 |
| it was not great | 1 |

| table 0-row-2 1-row-2 2-row-2 2-align-right 5-align-right 8-align-right layout-auto |  |
| --- | --- |
| Second Response | Events |
| will recommend to others | 2 |
| will not recommend to others | 1 |

### Summarize summarize

Applies aggregation-type functions to metrics or dimensions at event, session, and user levels.

Details
## Specification summarize-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String Numeric Date | Value Rules Standard fields Fields Summarize methods Scope Event Session Person | Numeric MAX - return largest value from a set of values MIN - returns smallest value from a set of values MEDIAN - returns median for a set of values MEAN - returns average for a set of values SUM - returns the sum for a set of values COUNT - returns the number of values received DISTINCT - returns set of distinct values Strings DISTINCT - returns set of distinct values COUNT DISTINCT - returns the number of distinct values MOST COMMON - returns the string value most often received LEAST COMMON - returns the string value least often received FIRST - The first value received; only applicable for the session & event tables LAST- The last value received; only applicable for the session & event tables Dates DISTINCT - returns set of distinct values COUNT DISTINCT - returns the number of distinct values MOST COMMON - returns the string value most often received LEAST COMMON - returns the string value least often received FIRST - The first value received; only applicable for the session & event tables LAST- The last value received; only applicable for the session & event tables EARLIEST - The earliest value received (determined by time); only applicable for the session & event tables LATEST - The latest value received (determined by time); only applicable for the session & event tables | 3 function per derived field | New derived field |

## Use case summarize-uc

You would like to categorize Add to Cart Revenue into three different categories: Small, Medium, and Large. This allows you to analyze and identify the characteristics of high-value customers.

### Data before summarize-uc-databefore

Assumptions:

- Add to Cart Revenue is collected as a numeric field.

Scenarios:

- CustomerABC123 adds $35 to their cart for ProductABC, then separately adds ProductDEF to their cart for $75.
- CustomerDEF456 adds $50 to their cart for ProductGHI, then separately adds ProductJKL to their cart for $275.
- CustomerGHI789 adds $500 to their cart for ProductMNO.

Logic:

- If Total Add to Cart Revenue for a visitor is less than $150, set to Small.
- If Total Add to Cart Revenue for a visitor is greater than $150, but less than $500, set to Medium.
- If Total Add to Cart Revenue for a visitor is greater than or equal to $500, set to Large.

Results:

- Total Add to Cart Revenue for $110 for CustomerABC123.
- Total Add to Cart Revenue for $325 for CustomerDEF456.
- Total Add to Cart Revenue for $500 for CustomerGHI789.

### Derived field summarize-uc-derivedfield

You create an Add To Cart Revenue Size derived field. You use the SUMMARIZE function and the Sum Summarize method with Scope set to Person to sum the values of the cart_add field. Then you use a second CASE WHEN rule to split the result in the tree category sizes.

### Data after summarize-uc-dataafter

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Add To Cart Revenue Size | Visitors |
| Small | 1 |
| Medium | 1 |
| Large | 1 |

## More information summarize-more-info

Use the Summarize function for event, session or person scope based calculations. Use the [Math](#math) function for hit-level based calculations.

### Trim trim

Trims whitespace, special characters, or number of characters from either the beginning or the end of field values into a new derived field.

Details
## Specification trim-io

| table 0-row-5 1-row-5 |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String | Field Rules Standard fields Fields Trim whitespace Trim special characters Input of special characters Trim from left From String start Position Position # String String value Index Flag to include string To String end Position Position # String String value Index Flag to include string Length Trim from right From String end Position Position # String String value Index Flag to include string To String start Position Position # String String value Index Flag to include string Length | N/A | 1 function per derived field | New derived field |

## Use case 1 trim-uc1

You collect product data, however that data contains hidden whitespace characters which fragment reporting. You would like to easily trim any excess whitespace

### Data before trim-uc1-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 2-align-right 5-align-right 8-align-right 11-align-right layout-auto |  |
| --- | --- |
| Product ID | Events |
| "prod12356 " | 1 |
| "prod12356" | 1 |
| " prod12356" | 1 |

### Derived field trim-u1-derivedfield

You create a Product Identifier derived field. You use the TRIM function to define a rule to **Trim whitespace** from the **Product ID** field.

### Data after trim-uc1-dataafter

| table 0-row-2 1-row-2 2-align-right 5-align-right layout-auto |  |
| --- | --- |
| Product Identifier | Events |
| "prod12356" | 3 |

## Use case 2 trim-uc2

Your data on page names collected includes some erroneous special characters at the end of the page name which must be removed.

### Data before trim-uc2-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right 17-align-right layout-auto |  |
| --- | --- |
| Name | Events |
| home page# | 1 |
| home page? | 1 |
| home page% | 1 |
| home page& | 1 |
| home page/ | 1 |

### Derived field trim-u2-derivedfield

You create a Page Name derived field. You use the TRIM function to define a rule to Trim special characters from the Name field using the Special characters #?%&/.

### Data after trim-uc2-dataafter

| table 0-row-2 1-row-2 2-align-right 5-align-right layout-auto |  |
| --- | --- |
| Page Name | Events |
| home page | 5 |

## Use case 3 trim-uc3

You collect data including a storeID. The storeID contains the abbreviated US state code as the first two characters. You want to only use that state code in your reporting.

### Data before trim-uc3-databefore

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 6-row-2 7-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right 17-align-right 20-align-right 23-align-right layout-auto |  |
| --- | --- |
| storeID | Events |
| CA293842 | 1 |
| CA423402 | 1 |
| UT123418 | 1 |
| UT189021 | 1 |
| ID028930 | 1 |
| OR234223 | 1 |
| NV22342 | 1 |

### Derived field trim-u3-derivedfield

You create a Store Identifier derived field. You use the TRIM function to define a rule to Truncate from right the storeID field from String end to position 3.

### Data after trim-uc3-dataafter

| table 0-row-2 1-row-2 2-row-2 3-row-2 4-row-2 5-row-2 2-align-right 5-align-right 8-align-right 11-align-right 14-align-right 17-align-right layout-auto |  |
| --- | --- |
| Store Identifier | Events |
| CA | 2 |
| UT | 2 |
| ID | 1 |
| OR | 1 |
| NV | 1 |

### Typecast typecast

Changes the field type of a field to make it available for additional transformations within Customer Journey Analytics.

Details
## Specifications typecast-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| Numeric Date Date-time String | Field | Integer To String Double To String Include # of decimal places to inherit (max 5?) To Integer Byte To String Long To String Date To String Provide the ability to define the output format Examples Date (Example of January 7, 2025) MM-DD-YY Ex. 01-07-25 MM-DD-YYYY Ex. 01-07-2025 DD-MM-YY Ex. 07-01-25 DD-MM-YYYY Ex. 07-01-2025 YY-MM-DD Ex. 25-01-07 YYYY-MM-DD Ex. 2025-01-07 MM/DD/YY Ex. 01/07/25 MM/DD/YYYY Ex. 01/07/2025 YYYY/MM/DD Ex. 2025/01/07 YY/MM/DD Ex. 25/01/07 MMM DD, YYYY Ex. January 07, 2025 Date-time To String Provide the ability to define the output format Examples Date-Time (Example of January 7, 2025 at 1:30pm, 52 seconds) MM-DD-YY hhmmss Ex. 01-07-25 13:30:52 MM-DD-YYYY hhmmss Ex. 01-07-2025 13:30:52 DD-MM-YY hhmmss Ex. 07-01-25 13:30:52 DD-MM-YYYY hhmmss Ex. 07-01-2025 13:30:52 YY-MM-DD hhmmss Ex. 25-01-07 13:30:52 YYYY-MM-DD hhmmss Ex. 2025-01-07 13:30:52 MM/DD/YY hhmmss Ex. 01/07/25 13:30:52 MM/DD/YYYY hhmmss Ex. 01/07/2025 13:30:52 YYYY/MM/DD hhmmss Ex. 2025/01/07 13:30:52 YY/MM/DD hh:mm :ss Ex. 25/01/07 13:30:52 MMM DD, YYYY hhmmss Ex. January 07, 2025 13:30:52 String To Numeric If we have values that are not numeric in nature, they will return null. We will need the user to input the precision and the locale to use. | 3 functions per derived field | New derived field |

## Use case 1 typecast-uc1

You have an integer field, screen height (for example device.screenHeight from your event dataset), that you would like to use as a string based dimension.

### Derived field typecast-uc1-derivedfield

You define a Screen Height derived field. You use the TYPECAST function to define a rule to Typecast to String the Screen height field and store that in the new derived field.

## Use case 2 typecast-uc2

You want to use Revenue in a Cohort table (which only supports integers), but the Revenue field has a Double type.

### Derived field typecast-uc2-derivedfield

You define a Revenue (integer) derived field. You use the TYPECAST function to define a rule to Typecast to Integer the Revenue field and store that in the new derived field.

### URL Parse urlparse

Parses out different parts of a URL including protocol, host, path, or query parameters.

Details
## Specifications urlparse-io

| table 0-row-5 1-row-5 layout-auto |  |  |  |  |
| --- | --- | --- | --- | --- |
| Input Data Type | Input | Included Operators | Limit | Output |
| String | Field: Rules Standard fields Fields Option: Get protocol Get host Get path Get query string value Query parameter: String Get hash value | N/A | 5 functions per derived field | New derived field |

## Use case 1 urlparse-uc1

You only want use the referring domain from the referring URL as part of a marketing channel’s set of rules.

### Data before urlparse-uc1-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 layout-auto |
| --- |
| Referring URL |
| https://www.google.com/ |
| https://duckduckgo.com/ |
| https://t.co/ |
| https://l.facebook.com/ |

### Derived field urlparse-uc1-derivedfield

You define a Referring Domain derived field. You use the URL PARSE function to define a rule to fetch the host from the Referring URL field and store that in the new derived field.

### Data after urlparse-uc1-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 4-row-1 layout-auto |
| --- |
| Referrer Domain |
| www.google.com |
| duckduckgo.com |
| t.co |
| l.facebook.com |

## Use case 2 urlparse-uc2

You want to use the value of the cid parameter of a query string in a Page URL as part of the output of a derived tracking code report.

### Data before urlparse-uc2-databefore

| table 0-row-1 1-row-1 2-row-1 3-row-1 layout-auto |
| --- |
| Page URL |
| https://www.adobe.com/?cid=abc123 |
| https://www.adobe.com/?em=email1234&cid=def123 |
| https://www.adobe.com/landingpage?querystring1=test&test2=1234&cid=xyz123 |

### Derived field urlparse-uc2-derivedfield

You define a Query String CID derived field. You use the URL PARSE function to define a rule to fetch the value of the query string parameter in the Page URL field, specifying cid as the query parameter. The output value is stored in the new derived field.

### Data after urlparse-uc2-dataafter

| table 0-row-1 1-row-1 2-row-1 3-row-1 layout-auto |
| --- |
| Query String CID |
| abc123 |
| def123 |
| xyz123 |

## Limitations

The following limitations apply to the Derived field functionality in general:

- You can use a maximum of ten different schema fields (not including standard fields) when defining rules for a derived field. From this maximum of ten different schema fields, only a maximum of three lookup schema or profile schema fields are allowed.
- You can have a maximum number of derived fields per Customer Journey Analytics connection depending on the package you license. See [Product Description](https://helpx.adobe.com/legal/product-descriptions/customer-journey-analytics.html#_blank) for more information.

### Summary of function limitations

Function
Limitations
Case When
- 5 Case When functions per derived field
- 200 [operators](#operators) per derived field

Classify
- 5 Classify functions per derived field
- 200 [operators](#operators) per derived field

Concatenate
- 2 Concatenate functions per derived field
- 3 values per Concatenate function

Date Math
- 2 Date Math functions per derived field

Deduplicate
- 5 Deduplicate functions per derived field

Depth
- 3 Depth functiond per derived field

Find & Replace
- 2 Find & Replace functions per derived field

Lookup
- 5 Lookup functions per derived field

Lowercase
- 2 Lowercase functions per derived field

Math
- 25 operations per derived field
- 5 Math functions per derived field

Merge Fields
- 2 Merge Fields functions per derived field

Next or Previous
- 3 Next or Previous functions per derived field

Regex Replace
- 1 Regex Replace function per derived field

Split
- 2 Split functions per derived field
- Maximum of 10 values are returned

Summarize
- 3 Summarize functions per derived field

Trim
- 1 Trim function per derived field

Typecast
- 3 Typecast functions per derived field

URL Parse
- 5 URL Parse functions per derived field

### Operators

An operator in an If or Else If construct within a Case When function is the combination of a criterion with **one** value. Every additional value for the criterion adds to the number of operators.

As an example, the condition below uses 13 operators.

An operator in the Classify function is a single entry for When value equal Original value Replace value with New value.

As an example, the Classify rule below uses 3 operators.

## More information trim-more-info

[Trim](#trim) and [Lowercase](#lowercase) are features already available in the component settings in [Data views](/en/docs/analytics-platform/using/cja-dataviews/component-settings/overview). Using Derived Fields allows you to combine these functions to do more complex data transformation directly in Customer Journey Analytics. For example, you can use Lowercase to remove case sensitivity in an event field, and then use [Lookup](#lookup) to match the new lowercase field to a lookup dataset that only has lookup keys in lowercase. Or you can use Trim to remove characters before setting up Lookup on the new field.

Support for lookup and profile fields in Derived Fields enables you to transform data based on event lookups and profile attributes. This can be especially helpful in B2B scenarios with account-level data in lookup or profile datasets. Additionally, this support is useful to manipulate data in common fields from lookup data (like campaign info and offer type), or from profile data (like member tier and account type).

Related Articles
- [Blog: Making the Most of Your Data: A Framework for Using Derived Fields in Customer Journey Analytics](https://experienceleaguecommunities.adobe.com/t5/adobe-analytics-blogs/making-the-most-of-your-data-a-framework-for-using-derived/ba-p/601670)
- [Blog: Derived Fields Use Cases for Customer Journey Analytics](https://experienceleaguecommunities.adobe.com/t5/adobe-analytics-blogs/derived-fields-use-cases-for-customer-journey-analytics/ba-p/601679)
- [Blog: Adobe Customer Journey Analytics Derived Fields Enhancements](https://experienceleaguecommunities.adobe.com/t5/adobe-analytics-blogs/adobe-customer-journey-analytics-derived-fields-enhancements/ba-p/697808)

recommendation-more-help
