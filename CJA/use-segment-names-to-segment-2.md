---
title: "Use segment names to segment"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/use-segment-names-to-segment"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-23T20:45:50.385685+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use segment names to segment

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Data management](#)

CREATED FOR:

- User

In this use case, you want to use an existing segment for the Fishing product category, that you have defined in Customer Journey Analytics. To segment and report on product names and occurrences (events) during January 2023.

Customer Journey Analytics
Inspect the segment that you want to use in Customer Journey Analytics.

You then can use that segment in an example **Using Segment Names To Segment** panel for the use case:

BI tools
| note prerequisites |
| --- |
| PREREQUISITES |
| Ensure you have validated [a successful connection, can list data views, and use a data view](/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/connect-and-validate) for the BI tool for which you want to try out this use case. |

| tabs |  |
| --- | --- |
| Power BI Desktop | In the Data pane: Select daterange . Select filterName . Select product_name . Select sum occurrences . You see a visualization displaying Error fetching data for this visual . In the Filters pane: Select filterName is (All) from Filters on this visual . Select Basic filtering as the Filter type . Underneath the Search field, select Fishing Products , which is the name of the existing filter defined in Customer Journey Analytics. Select daterange is (All) from Filters on this visual . Select Advanced filtering as the Filter type . Define the filter to Show items when the value is on or after 1/1/2023 And is before 2/1/2023 . Select to remove filterName from Columns . Select to remove daterange from Columns . You see the table updated with the applied filterName filter. Your Power BI Desktop should look like below. |
| Tableau Desktop | Select the Sheet 1 tab at the bottom to switch from Data source . In the Sheet 1 view: Drag the Filter Name entry from the Tables list in the Filters shelf. In the Filter [Filter Name] dialog ensure Select from list is selected, and select Fishing Products from the list. Select Apply and OK . Drag Daterange entry from the Tables list in the Filters shelf. In the Filter Field [Daterange] dialog, select Range of Dates and select Next > . In the Filter [Daterang] dialog, select Range of dates , and select 01/01/2023 - 01/02/2023 . Select Apply and OK . Drag Product Name from the Tables list to Rows . Drag Occurrences entry from the Tables list and drop the entry in the field next to Columns . The value changes to SUM(Occurrences) . Select Text Table from Show Me . Select Fit Width from the Fit drop-down menu. Your Tableau Desktop should look like below. |
| Looker | In the Explore interface of Looker, ensure you do have a clean setup. If not, select Remove fields and filters . Select + Filter underneath Filters . In the Add Filter dialog: Select ‣ Cc Data View From the list of fields, select ‣ Daterange Date then Daterange Date . Specify the Cc Data View Daterange Date filter as is in range 2023/01/01 until (before) 2023/02/01 . Select + Filter underneath Filters to add another filter. In the Add Filter dialog: Select ‣ Cc Data View From the list of fields, select ‣ Filter name . Ensure is the selection for the filter. Select Fishing Products from the list of possible values. From the ‣ Cc Data View section in the left rail: Select Product Name . Select Count underneath MEASURES in the left rail (at the bottom). Select Run . Select ‣ Visualization . You should see a visualization and table similar as shown below. |
| Jupyter Notebook | Enter the following statements in a new cell. code language-python data = %sql SELECT filterName FROM cc_data_view; style = {'description_width': 'initial'} filter_name = widgets.Dropdown( options=[d for d, in data], description='Filter Name:', style=style ) display(filter_name) Execute the cell. You should see output similar to the screenshot below. Select Fishing Products from the drop-down menu. Enter the following statements in a new cell. code language-python import seaborn as sns import matplotlib.pyplot as plt data = %sql SELECT product_name AS `Product Name`, COUNT(*) AS Events \ FROM cc_data_view \ WHERE daterange BETWEEN '2023-01-01' AND '2023-02-01' \ AND filterName = '{filter_name.value}' \ GROUP BY 1 \ LIMIT 10; df = data.DataFrame() df = df.groupby('Product Name', as_index=False).sum() plt.figure(figsize=(15, 3)) sns.barplot(x='Events', y='Product Name', data=df) plt.show() display(data) Execute the cell. You should see output similar to the screenshot below. | code language-python | data = %sql SELECT filterName FROM cc_data_view; style = {'description_width': 'initial'} filter_name = widgets.Dropdown( options=[d for d, in data], description='Filter Name:', style=style ) display(filter_name) | code language-python | import seaborn as sns import matplotlib.pyplot as plt data = %sql SELECT product_name AS `Product Name`, COUNT(*) AS Events \ FROM cc_data_view \ WHERE daterange BETWEEN '2023-01-01' AND '2023-02-01' \ AND filterName = '{filter_name.value}' \ GROUP BY 1 \ LIMIT 10; df = data.DataFrame() df = df.groupby('Product Name', as_index=False).sum() plt.figure(figsize=(15, 3)) sns.barplot(x='Events', y='Product Name', data=df) plt.show() display(data) |
| code language-python |  |
| data = %sql SELECT filterName FROM cc_data_view; style = {'description_width': 'initial'} filter_name = widgets.Dropdown( options=[d for d, in data], description='Filter Name:', style=style ) display(filter_name) |  |
| code language-python |  |
| import seaborn as sns import matplotlib.pyplot as plt data = %sql SELECT product_name AS `Product Name`, COUNT(*) AS Events \ FROM cc_data_view \ WHERE daterange BETWEEN '2023-01-01' AND '2023-02-01' \ AND filterName = '{filter_name.value}' \ GROUP BY 1 \ LIMIT 10; df = data.DataFrame() df = df.groupby('Product Name', as_index=False).sum() plt.figure(figsize=(15, 3)) sns.barplot(x='Events', y='Product Name', data=df) plt.show() display(data) |  |
| RStudio | Enter the following code block in a new chunk. Ensure you use the appropriate filter name. For example, Fishing Products . code language-r ## Dimension filtered by name df <- dv %>% filter(daterange >= "2023-01-01" & daterange < "2023-02-01" & filterName == "Fishing Products") %>% group_by(product_name) %>% count() %>% arrange(desc(n), .by_group = FALSE) print(df) Run the chunk. You should see output similar to the screenshot below. | code language-r | ## Dimension filtered by name df <- dv %>% filter(daterange >= "2023-01-01" & daterange < "2023-02-01" & filterName == "Fishing Products") %>% group_by(product_name) %>% count() %>% arrange(desc(n), .by_group = FALSE) print(df) |
| code language-r |  |
| ## Dimension filtered by name df <- dv %>% filter(daterange >= "2023-01-01" & daterange < "2023-02-01" & filterName == "Fishing Products") %>% group_by(product_name) %>% count() %>% arrange(desc(n), .by_group = FALSE) print(df) |  |

recommendation-more-help
