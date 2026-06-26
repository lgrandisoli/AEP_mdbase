---
title: "Sequential segments"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-components/segments/seg-sequential-build"
category: "other"
topic: "analytics-platform/using/cja-components/segments"
created_at: "2026-06-23T20:44:52.316083+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Sequential segments

Last update: May 13, 2026
- Topics:
- [Filters](#)
- [Segments](#)

CREATED FOR:

- User
- Admin

You create sequential segments using the Then logical operator between components, containers and components, or containers. The Then logical operator implies that one segment condition occurs, followed by another.

See [Sequential segmentation](/en/docs/analytics-learn/tutorials/components/segmentation/sequential-segmentation#_blank) for a demo video.

This video demonstrates the functionality using Adobe Analytics. However, the functionality is similarly available in Customer Journey Analytics. Be aware of the differences in terminology between Adobe Analytics and Customer Journey Analytics (for example *visits* versus *sessions*).

style
shade-box
A sequential segment has some [basic functionality](#basics) and additional options that you can configure to add more complexity to the sequential segment:

- After and within constraints for the Then logic in the sequence segment definition:
- What data to include as part of the overall sequence for the segment definition. Or for a sequence defined as part of a container. By default all matching data are considered. That data is identified by Include Everyone. Select Only Before Sequence to consider only data before the sequence. Select Only After Sequence to consider only data after the sequence.
- What data to exclude as part of the sequential segment definition.
- How to logically group conditions in your sequential segment definition.

## Basics

The basics of building a sequential segment are no different than building a regular segment using the [Segment builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder). You can use the [Definition builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder#definition-builder) to construct your segment definition. In that construction, you use components, containers, operators and logic. A regular segment becomes a sequential segment as soon as you select the **Then** operator in the main definition or in any of the containers you use within the [Definition builder](/en/docs/analytics-platform/using/cja-components/segments/seg-builder#definition-builder).

### Examples

The examples below illustrate how you use sequential segments in various use cases.

#### Simple sequence

Identify persons who viewed a page and then viewed another page. The event-level data is segmented using this sequence. Irrespective of previous, past, or interim person sessions, or the time or number of page views occurring between the sessions.

#### Sequence across sessions

Identify persons who viewed a page in one session, then viewed another page in another session. To differentiate between sessions, use containers to build the sequence and define **Session** level for each container.

#### Mixed-level sequence

Identify persons who view two pages across an undetermined number of sessions, and then view a third page in a separate session. Again, use containers to build the sequence and define **Session** level on the container that defines the separate session.

#### Aggregate sequence

Identify persons who at their first session visited a specific page and then later visited some other pages. To differentiate between the sequence of events, use containers to separate the logic on a **Session** container level.

#### Nest a sequence

Identify all sessions where a person visits one page before another page and then have follow-up sessions that involve two other pages. For example, identify all sessions where a person first visits the home page, then a category 1 page and then has other sessions where in each session the category 2 and category 3 page are visited.

## After and Within

You can use **After** and **Within** the **Then** operator to define additional [time constraints](#time-constraints) or [constraints for Events, Sessions or Dimensions](#event-session-and-dimension-constraints).

### Time constraints

To apply time constraints to the **Then** operator:

- Select .
- Select **Within** or **After** from the context menu.
- Specify a time period (**Minute**, **Hour**, up until **Years**).
- Select the *number* to open a popup that allows you to type in or specify a number using **-** or **+**.

To remove a time constraint, use .

The table below explains in more detail the time constraint operators.

Operators
Description
After
The After operator is used to specify a minimum limit on the amount of time between two checkpoints. When setting the After values, the time limit begins when the segment is applied. For example, if the After operator is set on a container to identify persons who visit page A, but don’t return to visit page B until after one day, then that day will start when the visitor leaves page A. For the visitor to be included in the segment, a minimum of 1440 minutes (one day) must transpire after leaving page A to view page B.
Within
The Within operator is used to specify a maximum limit on the amount of time between two checkpoints. For example, if the Within operator is set on a container to identify persons who visit page A, and then return to visit page B within one day, then that day begins when the person leaves page A. To be included in the segment, the person has a maximum time of one day before opening page B. For the person to be included in the segment, opening page B must occur within a maximum of 1440 minutes (one day) after leaving page A to view page B.
After but Within
When using both the After and Within operators, both operators start and end in parallel, not sequentially.
For example, you build a segment with the container set to:
After = 1 Week(s) and Within = 2 Week(s)
.
The conditions to identify visitors in this segment are met only between one and two weeks. Both conditions are enforced from the time of the first page view.
#### Examples

Some examples of using the time constraints.

##### After operator

Identify persons that visited one page and then another page only after two weeks. For example, persons that visited the Home page, but the Women | Shoes page only after two weeks.

If a page view for the Home happens on June 1, 2024, at 00:01, then a page view to page Women | Shoes will match as long as that page view occurs after June 15, 2024 00:01.

##### Within operator

Identify persons that visited one page and then another page within five minutes. For example, persons that visited the Home page and then the Women | Shoes page within 5 minutes.

If a page view for the Home happens on June 1, 2024, at 12:01, then a page view to page Women | Shoes will match as long as that page view occurs before June 15, 2024 12:16.

##### After but Within operator

Identify persons that visited one page then visited another page after two weeks but within one month. For example, persons that visited the Home page and then after two weeks and within one month the Women | Shoes page.

Any persons hitting the Home page on June 1, 2024 and who are returning to visit the Women | Shoes page after June 15, 2019 00:01, but before July 1, 2019 qualify for the segment.

### Event, Session and Dimension constraints

The **After** and **Within** constraints allow you not only to specify a time constraint but also an event, session or dimension constraint. Select **Event(s)**, **Session(s)** or **Other dimensions** *Dimension name*. You can use the *Search* field to search for a dimension.

#### Example

Below is an example of a sequential segment looking for persons that visited one product category page (Women | Shoes), followed by a checkout page (Checkout | Thank You) within one page.

The following example sequences match or do not match:

Sequence
Page
Women | Shoes
followed by page
Checkout | Thank You
Page
Women | Shoes
followed by page
Women | Tops
followed by page
Checkout | Thank You
## Include

You can specify what data to include in your sequential segment or in a sequential container that is part of your sequential segment.

### Everyone include_everyone

To create a sequential segment that includes everyone, select the option **Include Everyone**.

The sequential segment identifies data that match the given pattern as a whole. Below is an example of a basic sequence segment looking for persons that visited one product category page (Women | Shoes), followed by a checkout page (Checkout | Thank You). The segment is set to **Include Everyone**.

The following example sequences match or do not match:

Sequence
1
Women | Shoes
then
Checkout | Thank You
in the same session
2
Women | Shoes
then
Men | Shoes
then
Checkout | Thank You
(across different sessions)
3
Checkout | Thank You
then
Women | Shoes
### Only Before Sequence and Only After Sequence

The options **Only Before Sequence** and **Only After Sequence** segment the data to a subset before or after the specified sequence.

- **Only Before Sequence**: Includes all data before a sequence and the first data of the sequence itself. If a sequence appears multiple times as part of the data, Only Before Sequence includes the first hit of the last occurrence of the sequence and all prior hits.
- **Only After Sequence**: Includes all hits after a sequence and the last data of the sequence itself. If a sequence appears multiple times as part of the data, Only After Sequence includes the last hit of the first occurrence of the sequence and all subsequent hits.

Consider a definition specifying a sequence of a component with criteria identified by B, followed (Then) by a component with criteria identified by D. The three options would identify data as follows:

B Then D
A
B
C
D
E
F
Include Everyone
Only Before Sequence
Only After Sequence
B Then D (occurs multiple times)
A
B
C
D
B
C
D
E
Include Everyone
Only Before Sequence
Only After Sequence
#### Example

You have defined three version of a sequential segment for site sections. One with the option **Include Everyone**, one with the option **Only Before Sequence**, and one with the option **Only After Sequence**. You named the three segments accordingly.

When reporting on site sections using these three segments, the example output in a freeform table looks like:

## Exclude

Segment definitions include all data unless you specifically exclude Person, Session, or Event data using **Exclude**.

Exclude allows you to dismiss common data and create segments with more focus. Exclude also allows you to create segments excluding specific groups of persons. For example, to define a segment that specifies persons that placed orders and then excluding that group of persons to identify *non-purchasers*. A best practice is to create rules that use a broad definition rather than trying to use Exclude to target specific persona that match specific include values.

Example of exclude definitions are:

- **Exclude pages**. Use a segment definition to strip out a specific page (such as *Home Page*) from a report, create an Event rule where the page equals Home Page, and then exclude the rule. This definition automatically includes all pages except the *Home Page*.
- **Exclude referring domains**. Use a definition that includes only referring domains from Google.com and excludes all others.
- **Identify non-purchasers**. Identify when orders are greater than zero and then exclude the Person.

Exclude can be used to identify a sequence where persons do not be part of specific sessions or perform specific events. Exclude can also be included within a Logic Group (see below).

You can exclude containers, not components.

### Examples

See below for examples of using Exclude.

#### Exclude within

Identify persons who visited one page, did not visited another page, then visited yet another page. You exclude the container using Exclude. An excluded container is identified by a thin red bar on the left.

#### Exclude at start

Identify persons who visited one page without ever going to another page. For example, people that checked out a purchase without ever visited the home page.

#### Exclude at end

Identify persons who visited one page but never visited other pages. For example, persons that visited your home page but never any of your checkout pages.

## Logic Group

NOTE
A Logic Group can only be defined in a sequential segment, meaning that the Then operator is used within the container.
Logic Group enables you to group conditions into a single sequential segment checkpoint. As part of the sequence, the logic defined in the container identified as Logic Group is evaluated after any prior sequential checkpoint and before any following sequential checkpoint.

The conditions within the Logic Group itself may be met in any order. By contrast, non-sequential containers (event, session, person) do not require their conditions to be met within the overall sequence, producing possible unintuitive results if used with a Then operator.

Logic Group was designed to treat *several conditions as a group, without any ordering* among the grouped conditions. Otherwise stated, the order of the conditions within a Logic Group is irrelevant.

Some best practices to use Logic Group are:

- To group sequential checkpoints.
- To simplify the construction of sequential segments.

### Examples

Here are examples on how to use the Logic Group container.

#### Any order

Identify persons that visited one page, then viewed each page out of another set of pages in any order. For example, persons that visited the Home page, then visited each of the Men page, the Women page, and the Kids page, irrespective of the order.

You can build this segment without a Logic Group, but the construction is going to be complex and laborious. Specify every sequence of pages that the visitor could view. For clarity, only the first container is opened and the other containers are closed . You can derive the contents of the other containers by the titles.

You can use Logic Group to simplify building this segment, as shown below. Ensure you select **Logic Group** for the container.

#### First match

Identify persons that visited one page or another page, then visited yet another page. For example, persons that visited the Women page or the Men page, then visited the Checkout | Thank You page.

#### Exclude And

Identify persons that visited one page then explicitly did not visit a set of other pages, but did visit yet another page. For example, persons that visited the Home Page, did not visit the Men or the Women page, but did visit the Kids page.

#### Exclude Or

Identify persons that visited one page then explicitly did not visit any page of a set of pages, but did visit yet another page. For example, persons that visited the Home Page and did not visit the Men and the Women page, but did visit the Kids page.

## A final example

As a final example, you want to identify persons that learned about a specific product page, without these persons ever touched by your Empower Your Move campaign. And in their first visit to your online store viewed the Home page but did not look further at any fitness (gear) products from the Men category. However, in their next session directly after that, they went to a product page and placed an online order without going through the Home page first.

recommendation-more-help
