---
title: "Use templates"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/templates/use-templates"
category: "other"
topic: "analytics-platform/using/cja-workspace/templates"
created_at: "2026-06-02T19:05:11.978797+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use templates

Last update: May 19, 2026
- Topics:
- [Workspace Basics](#)

CREATED FOR:

- User
- Admin

Templates (or company templates) in Analysis Workspace provide quick insights into the most common reporting scenarios. Following are some examples of questions that you can answer with templates:

- How many people visit your site.
- How many of those visitors are unique visitors (counted only once).
- How they came to the site (such as whether they followed a link or came there directly).
- What keywords visitors used to search site content.
- How long visitors stayed on a given page or on the entire site.
- What links visitors clicked, and when they left the site.
- Which marketing channels are most effective at generating revenue or conversion events.
- How much time they spent watching a video.
- Which browsers and devices they used to visit your site.

The following information describes how to access and use templates from the Templates tab in Analysis Workspace.

## Access and run a template

- In Analysis Workspace, select the Workspace tab.
- In the Templates section, select either of the following tabs: Adobe templates : Shows all templates provided by Adobe. login_company_name templates : Shows all company templates that have been created for your organization. Only administrators can create company templates. For information about how to create a company template, see Create and manage templates .
- Use either of the following options to change how you view the available templates: Choose whether to view templates in a column view or a card view by selecting either the column view or the card view icon. When using the card view , choose from the following sort orders: Most recently used , Most popular , Alphabetical , Categorical .
- In the search field, begin typing the name of the template you want to find, then select it from the list of templates. Or Select the category of template that you want to view, then select the template from the list of templates. note tip TIP To navigate the menu using the arrow keys, press the Forward Slash key (/), and then press the Down Arrow key. Press Enter to load the selected template. For a list of templates that are available, see the Available templates section below.
- (Optional) You can view templates that contain components that are not available in your data view. (By default, templates are shown only if they use components that are available in your data view.) note NOTE Before you can use these templates, an administrator must first add the required context labels for these missing components to the data view. For more information, see Add missing components to the data view for a given template in Use templates . For more information about context labels, see Component settings . Select the segment icon. Select Not ready for use to show templates that require additional components.
- Select the template to create a report based on the template you chose.
- (Conditional) If the template contains components that are not available in your data view, the Incompatible data view dialog displays, stating that the data view is incompatible with the template and showing which components are missing. Do either of the following: Choose a different data view in the Change data view drop-down menu. Select Continue anyway to view the template with the missing components.

## Create a project based on a template use-reports

A template might not fit your needs exactly, but it can get you close. In these cases, you can use the template as a starting point for your project, then customize it to best suit your specific purposes.

If you navigate away from a template after making changes, you are prompted to save or discard your changes. Saving changes to a template saves the template as a new project.

To customize a template and save it as a project:

- In Customer Journey Analytics, select the Workspace tab.
- Select the Templates tab.
- Select the template that you want to view. For example, under Most popular , select the Pages template. The Pages template, as displayed in Analysis Workspace, shows two visualizations ( Bar chart and Summary number ) and a Freeform table . The metric used is Occurrences.update screenshot. The following is AA
- Do any of the following: View the template. Drag one or more segments into the Segment drop zone at the top. For example, drag the segment Mobile Customers and view the results. Change the date range by going to the calendar at the top-right. Add dimension breakdowns, drag in other metrics, and generally customize the template to suit your needs.
- (Optional) Save the template as a project by selecting Project > Save . The template is saved as a new project; it does not modify the existing template. For more information about saving projects, see Save projects .

## Available templates

To access all available pre-built templates:

- In Adobe Analytics, select the Workspace tab, then select the Templates tab. Pre-built templates are organized by category.add screenshot
- Select a category to view the templates within it. The following sections correspond to the available categories and provide information about each template. Most popular Web** > **Engagement Web** > **Conversion Web** > **Audience Web** > **Acquisition Mobile** > **Mobile App Mobile** > **Mobile Device Information Time Parting Cross-Channel Other Channels AJO

### Most popular most-popular

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Training tutorial
Learn common Analysis Workspace terminology and steps for building your first analysis
Pages
duplicated in Engagement section
Identify the most popular and least popular pages.
**This can help you** better understand your audience and the kind of information they’re most interested in.

**Based on what you learn, you might** do any number of things, like adjust page metadata in order to increase visibility on lesser-viewed pages, or spend time improving the content of your most-viewed pages.

This template uses the Page dimension and the Page Views metric.

Page views
duplicated in Engagement section
View the total number of page views. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how traffic on your site might be increasing or decreasing over time.

**Based on what you learn, you might** do any number of things, like assess the effectiveness of a recently launched marketing campaign by comparing site traffic before and after the campaign launched. Or you might compare year-over-year holiday traffic.

This template uses the Day dimension and the Page Views metric.

Web visits
duplicated in Engagement section
View the total number of visits. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how traffic on your site might be increasing or decreasing over time.

**Based on what you learn, you might** do any number of things, like assess the effectiveness of a recently launched marketing campaign by comparing site traffic before and after the campaign launched. Or you might compare year-over-year holiday traffic.

This template uses the Day dimension and the Visits metric.

Web visitors
duplicated in Engagement section
View the total number of unique visitors. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how the reach and audience size of your site is increasing or decreasing over time or compared with a prior period.

**Based on what you learn, you might** do any number of things, like assess whether a recently launched marketing campaign was successful at attracting new people to the site by comparing unique visitors before and after the campaign launched. Or you might compare the number of people to visit the site during the holidays year-over-year.

This template uses the Day dimension and the Unique Visitors metric.

Key metrics
duplicated in Engagement section
View a report that shows the page views, visits, and unique visitors metrics side by side. Data is shown over a
period of time and compared with prior periods.

**This can help you** compare these important metrics to gain a more complete picture of the number of unique people visiting the site, the number of times pages were visited, and the number of sessions.

**Based on what you learn, you might** do any number of things, like assess the average number of pages each person viewed when visiting the site in a given week or month, and how that changed during certain times of the year or before and after marketing campaigns were run.

This template uses the Day dimension, Page Views metric, Visits metric, and the Unique Visitors metric.

Site sections
View the most popular or highest performing sections of your site.

**This can help you** better understand which sections of your site are the most visited.

**Based on what you learn, you might** do any number of things, like assess which products or services that you provide generate the most interest.

This template uses the Site Section dimension and the Visits metric.

Next page
View the most common places people go immediately after visiting a certain page.

**This can help you** better understand user behavior after visiting a certain page.

**Based on what you learn, you might** do any number of things, like assess whether the page design or layout could be optimized to direct people to more desirable pages, such as a page to make a purchase or leave a review.

This template uses the Page dimension and the Events metric.

Previous page
View the most common places people go immediately before visiting a certain page.

**This can help you** better understand which pages direct the most traffic to a certain page.

**Based on what you learn, you might** do any number of things, like assess whether pages that aren’t appearing as previous pages need more prominent links to the current page.

This template uses the Page dimension and the Events metric.

Tracking code
View the links that were most successful in driving traffic to your site.

**This can help you** better understand which tracking codes (and the links they are associated with) were the most used in accessing your site.

**Based on what you learn, you might** do any number of things, like adjust your strategy for where you add links to your site.

This template uses the Tracking Code dimension and the Visits metric.

Products
View the number of orders by product. Data is shown over a period of time.

**This can help you** understand which products are in the highest or lowest demand.

**Based on what you learn, you might** do any number of things, like adjust your marketing strategies to promote high-performing products or to improve or discontinue under-performing products. You could also adjust your product inventory based on your analysis of the data.

This template uses the Product dimension and the Orders metric.

Last touch channel
View the most recent marketing channels visitors match with during their engagement period (30 days by default).

**This can help you** understand which marketing channels were most effective at bringing people to your site that result in conversions.

**Based on what you learn, you might** do any number of things, like allocate more resources to high-performing channels, or allocate fewer resources to under-performing channels.

This template uses the Last Touch Channel dimension and the Unique Visitors metric.

Last touch channel detail
View details about the most recent marketing channels visitors match with during their engagement period (30 days by default).

**This can help you** understand not only which marketing channels were most effective at bringing people to your site that result in conversions, but details about those marketing channels. For example, if a visitor arrived to your site and matched with the ‘Paid search’ Marketing channel, you could use the channel detail to see which search engine was used, or which keyword they searched for.

**Based on what you learn, you might** do any number of things, like allocate more resources to high-performing channels, or allocate fewer resources to under-performing channels.

This template uses the Last Touch Channel Detail dimension and the Unique Visitors metric.

Revenue
duplicated in Web Conversion section
View the monetary number of products purchased within all orders. Data is shown over a period of time and compared with prior periods.
**This can help you** understand how revenue is increasing or decreasing over time. You can combine this metric with any dimension to learn which dimension items contributed to revenue.

**Based on what you learn, you might** do any number of things, like project future revenue based on previous trends. You could also add another dimension, like the Tracking code dimension, to learn which campaigns are generating the most revenue.

This template uses the Day dimension and the Revenue metric.

Orders
duplicated in Web Conversion section
View the total number of purchase events. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how interest in your products and services is increasing or decreasing over time. You could apply a segment to learn which customers or geographies are placing the most orders and how those orders are trending over time.

**Based on what you learn, you might** do any number of things, like assess the effectiveness of a recently launched marketing campaign by comparing orders before and after the campaign launched. Or you might compare year-over-year holiday orders.

This template uses the Day dimension and the Orders metric.

### Web: Engagement web-engagement

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Key metrics
duplicated in Most popular section
View a report that shows the page views, visits, and unique visitors metrics side by side. Data is shown over a period of time and compared with prior periods.
**This can help you** compare these important metrics to gain a more complete picture of the number of unique people visiting the site, the number of times pages were visited, and the number of sessions.

**Based on what you learn, you might** do any number of things, like assess the average number of pages each person viewed when visiting the site in a given week or month, and how that changed during certain times of the year or before and after marketing campaigns were run.

This template uses the Day dimension, Page Views metric, Visits metric, and the Unique Visitors metric.

Page views
duplicated in Most popular section
View the total number of page views. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how traffic on your site might be increasing or decreasing over time.

**Based on what you learn, you might** do any number of things, like assess the effectiveness of a recently launched marketing campaign by comparing site traffic before and after the campaign launched. Or you might compare year-over-year holiday traffic.

This template uses the Day dimension and the Page Views metric.

Pages
duplicated in Most popular section
Identify the most popular and least popular pages.
**This can help you** better understand your audience and the kind of information they’re most interested in.

**Based on what you learn, you might** do any number of things, like adjust page metadata in order to increase visibility on lesser-viewed pages, or spend time improving the content of your most-viewed pages.

This template uses the Page dimension and the Page Views metric.

Visits
duplicated in Most popular section
View the total number of visits. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how traffic on your site might be increasing or decreasing over time.

**Based on what you learn, you might** do any number of things, like assess the effectiveness of a recently launched marketing campaign by comparing site traffic before and after the campaign launched. Or you might compare year-over-year holiday traffic.

This template uses the Day dimension and the Visits metric.

Visitors
duplicated in Most popular section
View the total number of unique visitors. Data is shown over a period of time and compared with prior periods.
**This can help you** better understand how the reach and audience size of your site is increasing or decreasing over time or compared with a prior period.

**Based on what you learn, you might** do any number of things, like assess whether a recently launched marketing campaign was successful at attracting new people to the site by comparing unique visitors before and after the campaign launched. Or you might compare the number of people to visit the site during the holidays year-over-year.

This template uses the Day dimension and the Unique Visitors metric.

Time spent
View the average time visitors spend on your site during each visit, as well as the average time users spend prior to a success event. Data is shown over a period of time and compared with prior periods.

**This can help you** better understand visitor engagement levels and how much time it takes visitors to perform a desired action, such as making a purchase.

**Based on what you learn, you might** do any number of things, like assess whether changes to your site improve visitors’ ability to quickly reach a success event.

This template uses the Day dimension and the Time Spent per Visit (seconds) metric, the Day dimension, and the Time Spent per Visit (seconds) metric.

Site sections
duplicated in Most popular section
View the most popular or highest performing sections of your site.
**This can help you** better understand which sections of your site are the most visited.

**Based on what you learn, you might** do any number of things, like assess which products or services that you provide generate the most interest.

This template uses the Site Section dimension and the Visits metric.

Web content consumption
View which web content is consumed most and is engaging users.

**This can help you** better understand where people go upon first entering the site, which sections of the site people are visiting most, and which pages are most likely to drive people away from the site.

**Based on what you learn, you might** do any number of things, like assess which paths on the site drive people to the most important pages, and which pages are more likely to lead people away from the site.

This template uses the Page dimension and the Page Views metric, the Visits metric, the Unique Visitors metric, the Entry Rate metric, the Bounce Rate metric, the Exit Rate metric, and the Content Velocity metric. It also uses Flow visualizations for entry, exit, and top sections.

Media content consumption
View which media content is consumed most and is engaging users.

**This can help you** better understand where people go upon first entering the site, which sections of the site people are visiting most, and which pages are most likely to drive people away from the site.

**Based on what you learn, you might** do any number of things, like assess which paths on the site drive people to the most important pages, and which pages are more likely to lead people away from the site not sure about these takeaways... .

This template uses the Page dimension and the Page Views metric, the Visits metric, the Unique Visitors metric, the Entry Rate metric, the Bounce Rate metric, the Exit Rate metric, and the Content Velocity metric. It also uses Flow visualizations for entry, exit, and top sections; a Scatterplot visualization that shows page views for the most common pages; a Bar visualization that shows page views by bucketed time; and a Line visualization that shows a trended view of the average time spent on the site.

Next and previous page flow
View a flow visualization of the most common places people go immediately after visiting and immediately before visiting a certain page.

**This can help you** understand how traffic moves from a given page to other parts of your site, and understand the paths people take to arrive at a given page.

**Based on what you learn, you might** do any number of things, like assess whether the page design or layout could be optimized to direct people to more desirable pages, such as a page to make a purchase or leave a review. Or assess whether the information on the current page is likely to provide the direction or actions that people are looking for as they arrive from previous pages. Or you might assess whether pages that aren’t appearing as previous pages need more prominent links to the current page.

This template uses the Next or previous item panel.

Page summary
View key information about any page across your properties. Shows page views, a trend line, a flow visualization, and more.

**This can help you** better understand how people interact with a given page.

**Based on what you learn, you might** do any number of things, like analyze the page’s performance over a period of time or better understand what drives traffic to the page.

This template uses the Page Views metric. It also uses the Line visualization and Flow visualization.

Entry pages
View the top pages that people access upon first visiting your site.

**This can help you** better understand which pages are driving the most traffic to your site or understand more about the first impressions visitors have on your site.

**Based on what you learn, you might** do any number of things, like optimize the initial experience people get on the site, or ensure that the pages people first see upon entering your site are welcoming and provide the necessary links to other areas of your site.

This template uses the Sessions metric. It also uses the Bar visualization and the Freeform table visualization.

Exit pages
View the top pages that people access immediately before leaving your site.

**This can help you** better understand which pages are leading people away from the site.

**Based on what you learn, you might** do any number of things, like update common exit pages to optimize the experience people get before they leave, or include content or links to encourage people to stay on your site.

This template uses the Sessions metric. It also uses the Bar visualization and the Freeform table visualization.

Product usage overview
View how the Customer Journey Analytics product is used within your organization.

**This can help you** better understand how many people use Customer Journey Analytics, how often they use it, and usage trends over time. You can also see the number of projects being created and details about those projects (such as which components, visualizations, and panels are most commonly used), and many other usage statistics.

**Based on what you learn, you might** do any number of things, like delete unused projects or components, or provide user training for popular features.

Content Analytics
Learn what content and content attributes are performing best.

**This can help you** learn how your content is performing at a granular level. You can look at the performance of individual assets, or specific attributes. Content Analytics uses AI to automatically generate attributes and tag your content with them. See [Content Analytics](/en/docs/analytics-platform/using/content-analytics/content-analytics#_blank) for more information.

**Based on what you learn, you might** do any number of things, like promote high performing assets on your home page, personalize content for specific segments to include high performing attributes, or rotate out content that has started to get stale.

### Web: Conversion web-conversion

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Product conversion funnel
View product conversion in a funnel visualization that shows carts, checkouts, and orders. You can also see conversion percentages, revenue averages, unit averages, and order averages.

**This can help you** better understand how people progress through and drop off during the conversion process.

**Based on what you learn, you might** do any number of things, like improve your website to facilitate a smoother checkout process.

Products
View which products are driving key metrics, such as top sellers or most viewed.

**This can help you** better understand which products are most successful.

**Based on what you learn, you might** do any number of things, like increase funding to successful products and decrease funding to less successful products.

This template uses the Orders metric and the Product dimension.

Product performance
View which products are the highest performing.

**This can help you** better understand which products are most successful.

**Based on what you learn, you might** do any number of things, like increase funding to successful products and decrease funding to less successful products.

This template uses the Product Views, Cart Additions, Orders, Revenue, and Units metrics. It also uses the Product dimension.

Cart conversion funnels
View the number of times people performed key checkout events, such as adding items to their cart, viewing their cart, removing items from their cart, and checking out.

**This can help you** better understand which parts of the checkout process funnel that lead to conversion and which are more prone to cart abandonment.

**Based on what you learn, you might** do any number of things, like reduce friction at certain steps of the checkout process.

Carts
View the number of people who added a product to their cart.

**This can help you** better understand the number of people who add a product to their cart, as opposed to the overall number of products that are added to a cart.

**Based on what you learn, you might** do any number of things, like measure the effectiveness of your product pages.

This template uses the Carts metric.

Cart views
View the number of times people viewed their shopping cart.

**This can help you** better understand the checkout experience in an effort to reduce cart abandonment rates, or analyze the time between cart additions and checkouts among different products.

**Based on what you learn, you might** do any number of things, like offer promotions for products that stay in carts the longest and are at the greatest risk for abandonment.

This template uses the Cart Views metric.

Cart additions
View the number of times people added something to their cart.

**This can help you** better understand the part of the conversion funnel where customer interest in a product is high enough that they add it to their cart.

**Based on what you learn, you might** do any number of things, like improve product recommendations for all customers. This can be done by analyzing which products are frequently added to the same carts and suggesting related products based on items already in the cart.

Cart removals
View the number of times people removed something from their cart.

**This can help you** better understand the part of the conversion funnel where customers are no longer interested in a product, or it can help you understand where problems might exist in the checkout process.

**Based on what you learn, you might** do any number of things, like remove any potential barriers that might exist in the checkout process, such as a complicated user experience.

This template uses the Cart Removals metric.

Purchase conversion funnel
View purchase conversion in a funnel visualization that shows sessions, carts, and orders. You can also see conversion percentages, revenue averages, unit averages, and order averages.

**This can help you** better understand how people progress through and drop off during the conversion process.

**Based on what you learn, you might** do any number of things, like improve your website to facilitate a smoother checkout process.

Revenue
duplicated in Most popular section
View the monetary number of products purchased within all orders.
**This can help you** better understand which dimension items contributed to revenue, by combining the Revenue metric with any dimension. For example, you could see the top campaigns (using the Tracking code dimension) that contributed to revenue.

**Based on what you learn, you might** do any number of things, like adjust campaigns that aren’t meeting the revenue targets you would expect.

This template uses the Revenue metric.

Orders
duplicated in Most popular section
View the total number of purchase events made on your site.
**This can help you** better understand which dimension items contributed to an order, by combining the Orders metric with any dimension. For example, you could see the top campaigns (using the Tracking code dimension) that contributed to purchases.

**Based on what you learn, you might** do any number of things, like adjust campaigns that aren’t meeting the purchase targets you would expect.

This template uses the Orders metric.

### Web: Audience web-audience

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Audience overview
View which audiences are represented among the people visiting your site.

**This can help you** better understand general information about the audiences, where the audiences originated (RTCDP, Customer Journey Analytics, and so forth), audience overlap, and more.

**Based on what you learn, you might** do any number of things, like use the data to focus on marketing efforts for these specific audiences, or create tailored experiences for customers who span multiple audiences.

This template uses the Audience Name, Audience Origin, Exited Audience Name, and Exited Audience Origin dimensions.

For more information, see [Analyze Experience Platform audiences in Customer Journey Analytics](/en/docs/analytics-platform/using/cja-connections/audience-analysis/analyze-audiences).

First vs repeat visitors
View a comparison of first-time visitors to repeat visitors.

**This can help you** better understand your site’s effectiveness in retaining customer loyalty, or the rate at which you are acquiring new customers.

**Based on what you learn, you might** do any number of things, like offer incentives for future purchases to first-time visitors in order to entice them to return.

This template uses the
Person ID
View individual user behavior across various channels.

**This can help you** better understand the complete customer journey and interactions across multiple touchpoints.

**Based on what you learn, you might** do any number of things, like personalize marketing efforts to better target user preferences.

This template uses the
Geo countries
View the country from which people visiting the site originated.

**This can help you** better understand what the most popular countries visitors originate from who visit your site.

**Based on what you learn, you might** do any number of things, like use the data to focus on marketing efforts in these countries, or make sure that your site experience is optimal in countries that have different primary languages.

This template uses the Countries dimension.

Geo US states
View the state (in the United States) from which people visiting the site originated. This is similar to the Geo Regions template, except that it is specific to the United States.

**This can help you** better understand the most popular U.S. states visitors originate from who visit your site.

**Based on what you learn, you might** do any number of things, like use the data to focus on marketing efforts in these states.

This template uses the US States dimension.

Geo regions
View the geographic region from which people visiting the site originated. A region is a geographic area that is smaller than a country but larger than a city. In some countries, a region is a state, province, or prefecture. In other areas, it is a constituent country, department, or metropolitan region.

**This can help you** better understand the most popular regions visitors originate from who visit your site.

**Based on what you learn, you might** do any number of things, like use the data to focus on marketing efforts in these regions, or make sure that your site experience is optimal in regions that have different primary languages.

This template uses the ID(variables/geocountry) and Regions dimensions.

Geo cities
View the city from which people visiting the site originated.

**This can help you** better understand the most popular cities visitors originate from who visit your site.

**Based on what you learn, you might** do any number of things, like use the data to focus on marketing efforts in these cities.

This template uses the Cities dimension.

Geo US DMA
View the designated marketing areas (DMAs) within the United States from which people visiting the site originated.

**This can help you** better understand the most popular regions visitors originate from who visit your site.

**Based on what you learn, you might** do any number of things, like use the data to focus on marketing efforts in the most successful regions.

This template uses the
Languages
View the top languages that visitors prefer to see content in.

**This can help you** better understand the most frequently preferred languages of visitors.

**Based on what you learn, you might** do any number of things, like focus localization efforts or marketing efforts for the most popular languages.

This template uses the Language dimension.

Technology overview
View information related to the technology that people use to access your site, such as the operating systems, browsers, and devices.

**This can help you** better understand which technologies are most often used when accessing your site.

**Based on what you learn, you might** do any number of things, like optimize your site for the technologies that are used.

Browsers
View the name and version of the top browsers people use to access your site.

**This can help you** better understand the most common browsers that visitors use.

**Based on what you learn, you might** do any number of things, like improve site quality by testing new versions of your site using the top browsers. Doing so can maximize quality control efforts.

This template uses the Browser dimension.

Browser types
View the names of the organizations who made the top browsers that people use to access your site. This differs from the Browser template in that it does not list different versions of the same browser as separate dimension items.

**This can help you** better understand the most common browsers that visitors use

**Based on what you learn, you might** do any number of things, like improve site quality by testing new versions of your site using the top browsers. Doing so can maximize quality control efforts.

This template uses the Browser type dimension.

### Web: Acquisition web-acquisition

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Marketing channels
>
Channel overview report
When using custom attribution, this template shows how visitors arrive on your site.

**This can help you** better understand which of your marketing channels are most effective.

**Based on what you learn, you might** do any number of things, like invest more heavily in effective marketing channels and divest from less effecting marketing channels.

This template uses the ID(variables/marketingchannel) dimension and the Revenue metric.

Marketing channels
>
First touch channel
View the first marketing channel that a visitor matches with during that visitor’s engagement period (30 days by default).

**This can help you** better understand which marketing channels drive initial traffic to your site.

**Based on what you learn, you might** do any number of things, like focus marketing efforts in areas that are most effective.

This template uses the First Touch Channel dimension.

Marketing channels
>
First touch channel detail
View details about the first marketing channel a visitor matches with during that visitor’s engagement period (30 days by default).

**This can help you** better understand what contributed to the hit matching a marketing channel. For example, if a visitor arrived to your site and matched with the ‘Paid search’ Marketing channel, you could use the channel detail to see which search engine was used, or which keyword they searched for.

**Based on what you learn, you might** do any number of things, like focus marketing efforts in areas that are most effective.

This template uses the First Touch Channel Detail dimension.

Marketing channels
>
Last touch channel
View the most recent marketing channel that a visitor matches with during that visitor’s engagement period (30 days by default).

**This can help you** better understand which marketing channels drive traffic to your site that result in conversions.

**Based on what you learn, you might** do any number of things, like focus marketing efforts in areas that are most effective.

This template uses the Last Touch Channel dimension.

Marketing channels
>
Last touch channel detail
View details about the most recent marketing channel a visitor matches with during that visitor’s engagement period (30 days by default)

**This can help you** better understand what contributed to the hit matching a marketing channel. For example, if a visitor arrived to your site and matched with the ‘Paid search’ Marketing channel, you could use the channel detail to see which search engine was used, or which keyword they searched for.

**Based on what you learn, you might** do any number of things, like focus marketing efforts in areas that are most effective.

This template uses the Last Touch Channel Detail dimension.

Campaigns
>
Tracking code
View the names of tracking codes on your site. You can place links with different query string parameter values in different places across the internet.

**This can help you** better understand which links were the most successful in driving traffic to your site. Appending tracking code query strings are common in emails, advertisements, social media posts, and other marketing efforts that your organization uses

**Based on what you learn, you might** do any number of things, like focus marketing efforts on the campaigns that drive the most revenue.

This template uses the Tracking Code dimension.

Campaigns
>
Campaign conversion funnel
View the number of clickthroughs and checkouts for your campaigns.

**This can help you** better understand how marketing campaigns are driving conversion.

**Based on what you learn, you might** do any number of things, like determine which marketing campaigns are generating the most ROI.

Campaigns
>
Campaign performance
View details about how your marketing campaigns are performing.

**This can help you** better understand more about the various success indicators associated with campaigns, such as revenue, product views, orders, and so forth.

**Based on what you learn, you might** do any number of things, like focus marketing efforts on the campaigns that drive the most revenue.

This template uses the Revenue metric, Product Views metric, Cart Additions metric, Orders metric, and Units metric. It also uses the Tracking Code dimension and the Referring Domain dimension.

Web acquisition
View how your website obtains visitors.

**This can help you** better understand more about the various factors that lead to acquisition, such as search keywords, referring domain, and so forth.

**Based on what you learn, you might** do any number of things, like focus marketing efforts into the most effective channels.

This template uses the Bounce Rate metric and the Bounces metric. It also uses the Search Engine dimension, Search Keyword dimension, Entry Page dimension, Referring Domain dimension, Tracking Code dimension, and Referrer dimension.

Search keywords - all
View the search keywords that visitors use to reach your site, regardless whether it is paid or natural.

**This can help you** better understand the keywords people use in searches that result in site traffic.

**Based on what you learn, you might** do any number of things, like identify and fill SEO gaps between keywords used and those that drive site traffic.

This template uses the Search Keyword dimension.

Search keywords - paid
View the search keywords that visitors use to reach your site, which matched paid search detection.

**This can help you** better understand the keywords people use in searches that result in site traffic.

**Based on what you learn, you might** do any number of things, like identify and fill SEO gaps between keywords used and those that drive site traffic.

This template uses the Search Keyword - Paid dimension.

Search keywords - natural
View the search keywords that visitors use to reach your site, which did not match paid search detection.

**This can help you** better understand the keywords people use in searches that result in site traffic.

**Based on what you learn, you might** do any number of things, like identify and fill SEO gaps between keywords used and those that drive site traffic.

This template uses the Search Keyword - Natural dimension.

Search engines - all
View the search engines that visitors use to reach your site, regardless whether it is paid or natural.

**This can help you** better understand the search engines people use that result in site traffic.

**Based on what you learn, you might** do any number of things, like focus your SEO efforts on the search engines that drive the most traffic to the site.

This template uses the Search Engine dimension.

Search engines - paid
View the search engines that visitors use to reach your site, which matched paid search detection.

**This can help you** better understand the search engines people use that result in site traffic.

**Based on what you learn, you might** do any number of things, like focus your SEO efforts on the search engines that drive the most traffic to the site.

This template uses the Search Engine - Paid dimension.

Search engines - natural
View the search keywords that visitors use to reach your site, which did not match paid search detection.

**This can help you** better understand the search engines people use that result in site traffic.

**Based on what you learn, you might** do any number of things, like focus your SEO efforts on the search engines that drive the most traffic to the site.

This template uses the Search Engine - Natural dimension.

Referring domains
View which domains people click through to reach your site.

**This can help you** better understand which third-party sites drive the most traffic to yours. (A link must exist on the external site and a visitor must click it for the dimension item to show up.)

**Based on what you learn, you might** do any number of things, like create or adjust content to better align with the interests of visitors coming from top referring domains.

This template uses the Referring Domain dimension.

Original referring domains
View the first referring domain that people clicked through to reach your site. (Once it is set, it contains the same value for the entire lifetime of that visitor ID.)

**This can help you** better understand which third-party sites originally drive traffic to your site.

**Based on what you learn, you might** do any number of things, like create or adjust content to better align with the interests of visitors coming from top original referring domains.

This template uses the Original Referring Domain dimension.

Referrers
View which URLs visitors were on when clicking through to reach your site. (A link must exist on the external URL and a visitor must click it for the dimension item to show up.)

**This can help you** better understand which specific URLs drive the most traffic to your site.

**Based on what you learn, you might** do any number of things, like create or adjust content to better align with the interests of visitors coming from top URLs.

This template uses the Referring Domain dimension

This template uses the Referrer dimension.

Referrer types
View which generic channels visitors clicked through to arrive at your site. Adobe maintains the rules for each channel. Possible channels include search engines, social networks, other web sites, hard drive, or email.

**This can help you** better understand which type of referrers drive the most traffic to your site.

**Based on what you learn, you might** do any number of things, like create or adjust content to better align with the interests of visitors coming from a certain channel.

This template uses the Referrer Type dimension.

### Mobile: Mobile App mobile-app

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Mobile app screens
View the number of events, sessions, and people associated with each screen on the mobile app.

**This can help you** better understand which screens on your site are the most popular.

**Based on what you learn, you might** do any number of things, like improve content on the most popular screens.

This template uses the Events, Sessions, People, and Percent change metrics. It also uses the Page Title dimension.

Mobile app actions
View the actions people are taking on your mobile app.

**This can help you** better understand how people use your app and the value that get from it.

**Based on what you learn, you might** do any number of things, like improve develop features that compliment or improve upon those that are most popular.

This template uses the Events, Sessions, People, and Percent change metrics.

Mobile app usage
View the number of users, launches, and first launches on your app, as well as the average session length.

**This can help you** better understand how much your app is used.

**Based on what you learn, you might** do any number of things, like improve app performance so it can scale to the amount of usage.

This template uses the
Mobile app journeys
View the prominent usage patterns for your mobile app.

**This can help you** better understand how people use your app.

**Based on what you learn, you might** do any number of things, like improve how people can get from one screen to another to target the most common workflows.

This template uses the
Mobile app metrics
View some of the most common mobile app metrics.

**This can help you** better understand the basic performance of your mobile app.

**Based on what you learn, you might** do any number of things, like assess the overall health and performance of your app.

This template uses the
Mobile app messaging
View performance data for in-app messaging and push messaging for your app.

**This can help you** better understand how people use in-app messaging capabilities, as well as how effectively push notifications are driving traffic to your app.

**Based on what you learn, you might** do any number of things, like improve the in-app messaging push notification experience.

This template uses the
Mobile app performance
View how your app is performing and where users are experiencing issues.

**This can help you** better understand if people using your app are encountering slowness or a degraded performance.

**Based on what you learn, you might** do any number of things, like fix existing issues or improve app performance before issues occur.

This template uses the
Mobile app retention
View which users are the most loyal customers of your app and what they do within the app.

**This can help you** better understand how your most loyal customers use your app.

**Based on what you learn, you might** do any number of things, like improve your marketing efforts for the features that your most loyal customers use.

This template uses the
### Mobile: Mobile Device Information mobile-devices

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Mobile carrier
View the telecommunications company that provides cellular network connectivity to the mobile devices.that people use to access your site.

**This can help you** better understand which mobile carriers are most popular among your user base.

**Based on what you learn, you might** do any number of things, like tailor your content delivery based on the network capabilities of different carriers to ensure a smooth user experience.

This template uses the Mobile Carrier dimension.

Devices
View the make and model of mobile devices that people use to access your site.

**This can help you** better understand which mobile devices are most popular among your user base.

**Based on what you learn, you might** do any number of things, like optimize the rendering of your site for the most common mobile devices.

This template uses the Mobile Device Name dimension.

Device type
View the mobile device types that people use to access your site, such as phones and tablets.

**This can help you** better understand the various kinds of mobile devices that are used to access your site.

**Based on what you learn, you might** do any number of things, like optimize your site for the types of mobile devices that are used the most.

This template uses the Mobile Device Type dimension.

Manufacturer
View which manufacturers produce the mobile devices that people use to access your site, such as Apple and Samsung.

**This can help you** better understand which manufacturers are most popular among your user base.

**Based on what you learn, you might** do any number of things, like tailor your content delivery based on the abilities of different manufacturers to ensure a smooth user experience.

This template uses the Mobile Manufacturer dimension.

### Time Parting time-parting

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Minute of hour
View the number of events, sessions, and people on your site, broken down by minute. For example, if you have a report with a reporting timeframe of a single day, the first minute of each hour in the day is grouped into the same dimension item.

**This can help you** better understand trends at a granular level.

**Based on what you learn, you might** do any number of things, like optimize resources for peak times, down to the minute.

This template uses the Minute of Hour dimension.

Hour of day
View events, sessions, and people on your site, broken down by hour of day. For example, if you have a report spanning January 1 - January 7, the first hour of each day is grouped into the same dimension item.

**This can help you** better understand the time of day when your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like assign more computing resources to your site during high-traffic hours.

This template uses the Hour of Day dimension.

AM/PM
View events, sessions, and people on your site, broken down by AM and PM. For example, if you have a report spanning January 1 - January 7, the AM hours of each day are grouped into the same dimension item.

**This can help you** better understand the time of day when your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like assign more computing resources to your site during high-traffic hours.

This template uses the AM/PM dimension.

Day of week
View events, sessions, and people on your site, broken down by day of week. For example, if you have a report spanning the month of January, each day of the week is grouped into the same dimension item.

**This can help you** better understand which days of the week your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like staff your call center more appropriately for high-traffic days.

This template uses the Day of Week dimension.

Day of month
View events, sessions, and people on your site, broken down by day of month. For example, if you have a report spanning a full year, each day of the month is grouped into the same dimension item.

**This can help you** better understand which days of each month your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like staff your call center more appropriately for high-traffic days.

This template uses the Day of Month dimension.

Day of year
View events, sessions, and people on your site, broken down by day of year. For example, if you have a report spanning multiple years, each day of the year is grouped into the same dimension item.

**This can help you** better understand which days of each year your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like staff your call center more appropriately for high-traffic days.

This template uses the Day of Year dimension.</>

Weekday/Weekend
View events, sessions, and people on your site, broken down by weekdays and weekends. For example, if you have a report spanning the month of January, weekdays and weekends are grouped into separate dimension items.

**This can help you** better understand the differences in site traffic for weekdays versus weekends.

**Based on what you learn, you might** do any number of things, like staff your call center more heavily on the weekends, if the report indicates that weekends are busier than weekdays.

This template uses the Weekday/Weekend dimension.

Week of year
View events, sessions, and people on your site, broken down by week of year. For example, if you have a report spanning multiple years, each week is grouped into the same dimension item.

**This can help you** better understand which weeks of the year your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like staff your call center more appropriately for high-traffic weeks, such as during the holidays.

This template uses the Week of Year dimension.

Month of year
View events, sessions, and people on your site, broken down by month of year. For example, if you have a report spanning multiple years, each month is grouped into the same dimension item.

**This can help you** better understand which months your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like staff your call center more appropriately for high-traffic months, such as during the holidays.

This template uses the Month of Year dimension.

Quarter of year
View events, sessions, and people on your site, broken down by quarter of the year. For example, if you have a report spanning multiple years, each quarter is grouped into the same dimension item.

**This can help you** better understand which quarters your site is most frequently and least frequently visited.

**Based on what you learn, you might** do any number of things, like time the launch of products in order to boost historically low-traffic quarters.

This template uses the Quarter of Year dimension.

### Cross-Channel cross-channel

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Multi-channel overview
View the distribution of traffic across multiple channels.

**This can help you** better understand which channels are more successfully driving traffic and engagement.

**Based on what you learn, you might** do any number of things, like focus marketing efforts on the channels that are achieving the highest return on investment.

This template uses the user, session, and event metrics.

Web+App
View web traffic and mobile traffic together.

**This can help you** better understand the distribution of web and mobile traffic to your site.

**Based on what you learn, you might** do any number of things, like dedicate more resources to your mobile app experience when it reaches a certain level of traffic.

This template uses the Web Sessions, Mobile App Sessions, and Web+App Cross-Channel Sessions metrics.

Online/Offline
View online and offline traffic together.

**This can help you** better understand the distribution of online and offline traffic to your site.

**Based on what you learn, you might** do any number of things, like dedicate more resources to your online experience when it reaches a certain level of traffic.

This template uses the ...
Call center deflection
View how web traffic affects call center traffic.

**This can help you** better understand how successfully the self-service content on your website is deflecting traffic to your call center.

**Based on what you learn, you might** do any number of things, like enhance self-service content in order to decrease traffic to your call center, or measure the ROI of your self-service content by calculating the amount saved through fewer support calls.

This template uses the Web Sessions, Mobile App Sessions, and Web+App Cross-Channel Sessions metrics.

### Other Channels other-channels

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Call center dashboard
View call center data, including why customers called and the number of times.

**This can help you** better understand where customers are experiencing problems and where call center resources are being spent.

**Based on what you learn, you might** do any number of things, like address product issues that are driving higher call center traffic, ultimately improving product profitability.

Point of sale
View point-of-sale (POS) transaction data, including revenue earned, orders made, and units sold. This template also includes visualizations that display information about top stores, top products, and top product categories, as well as online vs. offline sales.

**This can help you** better understand which are your top-selling products across store location and online.

**Based on what you learn, you might** do any number of things, like assign more marketing resources to your highest-performing products and channels.

This template uses the Users, Revenue, and Orders metrics.

Journey Optimizer email analysis
View how the emails that you design and send using Adobe Journey Optimizer are generating new memberships, loyalty members, and cross-sell opportunities.

**This can help you** better understand the effectiveness of emails that you design and send using Adobe Journey Optimizer.

**Based on what you learn, you might** do any number of things, like adjust your email strategy for a given email campaign.

Survey
View user engagement for your surveys. View the number of starts and completions, the top questions and answers, and the number of first vs. repeat participants.

**This can help you** better understand the engagement levels and success rate of your surveys.

**Based on what you learn, you might** do any number of things, like adjust future surveys to yield better participation.

This template uses the Users, Events, Survey starts, Survey completes, and Survey completion rate metrics.

Product usage overview
View how your organization uses Customer Journey Analytics.

**This can help you** better understand how many people in your organization use Customer Journey Analytics, how often they use it, and trend that data over time. You can also see the number of projects created and details about those projects. See which components, visualizations, and panels are most commonly used, among other usage statistics. [Learn more](/en/docs/analytics-platform/using/tools/product-usage/usage-overview)

**Based on what you learn, you might** do any number of things, like delete unused projects or components, or provide user training for popular features.

### Journey Optimizer AJO-templates

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Journey Optimizer campaigns
View essential metrics for your Journey Optimizer campaigns, including email campaigns, experimentation, in-app, SMS, and more.

**This can help you** better understand details such as the count of clicks and number of delivered messages, offering a comprehensive insight into your campaign’s effectiveness and level of engagement.

**Based on what you learn, you might** do any number of things, like adjust your campaigns based on the engagement levels of your target audience.

Journey Optimizer journeys
View essential metrics for your Journey Optimizer journeys, including email journeys, experimentation, in-app, SMS, and more.

**This can help you** better understand details such as the count of clicks and number of delivered messages, offering a comprehensive insight into your journey’s effectiveness and level of engagement.

**Based on what you learn, you might** do any number of things, like adjust your campaigns based on the engagement levels of your target audience.

Journey Optimizer landing pages
View user behavior, engagement patterns, conversion rates, and other key metrics.

**This can help you** better understand the effectiveness of your landing page.

**Based on what you learn, you might** do any number of things, like optimize your landing page performance.

Journey Optimizer overview report
View a thorough summary of traffic and engagement metrics for all campaigns and journeys within your environment.

**This can help you** better understand the high-level effectiveness of your campaigns and journeys.

**Based on what you learn, you might** do any number of things, like adjust your campaigns and journeys based on the engagement levels of your target audience.

Journey Optimizer subscriptions
View profiles’ subscriptions and unsubscriptions associated with particular lists.

**This can help you** better understand the effectiveness of different subscription campaigns and initiatives in driving engagement and conversions.

**Based on what you learn, you might** do any number of things, like adjust your subscription campaigns based on the engagement levels of your target audience.

### Brand Concierge brand-concierge-templates

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Brand Concierge overview
Analyze user engagement through conversation patterns, user feedback, and the effectiveness of your recommendations.

**This can help you** identify engagement patterns, evaluate conversation quality, track customer satisfaction trends, and measure the effectiveness of link recommendations.

**Based on what you learn, you might** do any number of things, like refine your AI agent’s responses, develop targeted content for frequent issues, improve recommendation algorithms, or create specialized pathways for different user segments.

Brand Concierge B2B Meetings
Track the complete lifecycle of B2B meeting requests. Monitor conversion rates, evaluate consultant booking performance, and identify your most effective lead generation channels.

**This can help you** track meeting conversion rates, identify high-performing team members, understand seasonal trends in booking behavior, and pinpoint which pages URLs generate the most valuable meeting requests.

**Based on what you learn, you might** do any number of things, like optimize your meeting request process, redistribute resources to high-converting page URLs, develop targeted training for consultants with lower booking rates, or implement new strategies to reduce missed meetings.

### B2B templates b2b-templates

[[B2B Edition]{class="badge informative" title="Customer Journey Analytics B2B Edition"}](/en/docs/analytics-platform/using/cja-overview/cja-b2b/cja-b2b-edition#_blank)

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
B2B Account Engagement Overview
See how active your accounts are across events, people, and opportunities.

**This can help you** better understand whether engagement at the account level is trending up or down, compare activity across accounts, and decide where to focus retention or acquisition efforts.

**Based on what you learn, you might** do any number of things, like refocus your attention on those accounts that are less engaged but require more attention due to the importance of the account.

B2B Opportunity Engagement Overview
Track engagement at the opportunity level and surface deals gaining or losing traction.

**This can help you** to forecast deal progression more accurately and focus enablement where engagement spikes or stalls.

**Based on what you learn, you might** do any number of things, like put some additional efforts on deals that are almost closed, and research why other deals are losing traction.

B2B Buying Group Activity
Visualize buying-group activity within each account to inform account and buying group-marketing plays.

**This can help you** to visualize which buying groups, and which people within those buying groups, are most engaged, highlighting gaps in group participation.

**Based on what you learn, you might** do any number of things, like trying to engage more with people in buying groups that do not seem to be involved.

### Mix Modeler templates mix-modeler-templates

The following templates are available:

Template name
Why use this template
What do you do with it? What can it help you learn? and What are the potential actions?
Mix Modeler incremental model insights
View insights from selected models generated by Mix Modeler.

**This can help you** to better understand the incremental insights from models generated in Mix Modeler.

**Based on these insights** you will be able to:

- Visualize and quantify the impact of your organization’s marketing activities.
- Identify which channels are high-performing.
- Identify which channels might need optimization.

recommendation-more-help
