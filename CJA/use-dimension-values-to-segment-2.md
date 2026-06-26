---
title: "Use dimension values to segment"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/use-dimension-values-to-segment"
category: "other"
topic: "analytics-platform/using/cja-usecases/data-views"
created_at: "2026-06-23T20:45:49.581353+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use dimension values to segment

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)
- [Data management](#)

CREATED FOR:

- User

You use the dynamic **Hunting** value for **Product Category** to segment products from the hunting category. Alternatively, for those BI tools that do not support the dynamic retrieval of product category values, you create a new segment in Customer Journey Analytics that segments on products from the hunting product category.Then you want to use the new segment to report on product names and occurrences (events) for products from the hunting category during January 2023.

Customer Journey Analytics
Create a new segment with **Title** Hunting Products in Customer Journey Analytics.

You then can use that segment in an example **Using Dimension Values To Filter** panel for the use case:

BI tools
| note prerequisites |
| --- |
| PREREQUISITES |
| Ensure you have validated [a successful connection, can list data views, and use a data view](/en/docs/analytics-platform/using/cja-usecases/data-views/bi-extension/connect-and-validate) for the BI tool for which you want to try out this use case. |

| tabs |  |
| --- | --- |
| Power BI Desktop | Select Home from the menu, then select Refresh from the toolbar. You need to refresh the connection to pick up the new filter you just defined in Customer Journey Analytics. In the Data pane: Select daterange . Select product_category . Select product_name . Select sum occurrences . You see a visualization displaying Error fetching data for this visual . In the Filters pane: Select filterName is (All) from Filters on this visual . Select Basic filtering as the Filter type . Select daterange is (All) from Filters on this visual . Select Advanced filtering as the Filter type . Define the filter to Show items when the value is on or after 1/1/2023 And is before 2/1/2023 . Select Basic filter as the Filter type for product_category , and select Hunting from the list of possible values. Select to remove filterName from Columns . Select to remove daterange from Columns . You see the table updated with the applied product_category filter. Your Power BI Desktop should look like below. |
| Tableau Desktop | Tableau Desktop does not support fetching the dynamic list of product categories from Customer Journey Analytics. Instead, this use case uses the newly created filter for Hunting Products and use the filter name critetia. In the Data Source view, underneath Data , from the context menu on cc_data_view(prod:cja%3FFLATTEN) , select Refresh . You need to refresh the connection to pick up the new filter you just defined in Customer Journey Analytics. Select the Sheet 1 tab at the bottom to switch from Data source . In the Sheet 1 view: Drag the Filter Name entry from the Tables list in the Filters shelf. In the Filter [Filter Name] dialog ensure Select from list is selected, and select Hunting Products from the list. Select Apply and OK . Drag Daterange entry from the Tables list in the Filters shelf. In the Filter Field [Daterange] dialog, select Range of Dates and select Next > . In the Filter [Daterange] dialog, select Range of dates , and select 01/01/2023 - 1/2/2023 . Select Apply and OK . Drag Product Name from the Tables list to Rows . Drag Occurrences entry from the Tables list and drop the entry in the field next to Columns . The value changes to SUM(Occurrences) . Select Text Table from Show Me . Select Fit Width from the Fit drop-down menu. Your Tableau Desktop should look like below. |
| Looker | In the 1. In the Explore interface of Looker, refresh your connection. Select Clear cache and refresh . In the Explore interface of Looker, ensure you do have a clean setup. If not, select Remove fields and filters . Select + Filter underneath Filters . In the Add Filter dialog: Select ‣ Cc Data View From the list of fields, select ‣ Daterange Date then Daterange Date . Specify the Cc Data View Daterange Date filter as is in range 2023/01/01 until (before) 2023/02/01 . Select + Filter underneath Filters to add another filter. In the Add Filter dialog: Select ‣ Cc Data View From the list of fields, select ‣ Product Category . Ensure is as the selection for the filter. Lookes does not show the list of possible values for Product Category . |
| Jupyter Notebook | Enter the following statements in a new cell. code language-python data = %sql SELECT DISTINCT product_category FROM cc_data_view WHERE daterange BETWEEN '2023-01-01' AND '2024-01-01'; style = {'description_width': 'initial'} category_filter = widgets.Dropdown( options=[d for d, in data], description='Product Category:', style=style ) display(category_filter) Execute the cell. You should see output similar to the screenshot below. Select Hunting from the drop-down menu. Enter the following statements in a new cell. code language-python import seaborn as sns import matplotlib.pyplot as plt data = %sql SELECT product_name AS `Product Name`, COUNT(*) AS Events \ FROM cc_data_view \ WHERE daterange BETWEEN '2023-01-01' AND '2023-02-01' \ AND product_category = '{category_filter.value}' \ GROUP BY 1 \ ORDER BY Events DESC \ LIMIT 10; df = data.DataFrame() df = df.groupby('Product Name', as_index=False).sum() plt.figure(figsize=(15, 3)) sns.barplot(x='Events', y='Product Name', data=df) plt.show() display(data) Execute the cell. You should see output similar to the screenshot below. | code language-python | data = %sql SELECT DISTINCT product_category FROM cc_data_view WHERE daterange BETWEEN '2023-01-01' AND '2024-01-01'; style = {'description_width': 'initial'} category_filter = widgets.Dropdown( options=[d for d, in data], description='Product Category:', style=style ) display(category_filter) | code language-python | import seaborn as sns import matplotlib.pyplot as plt data = %sql SELECT product_name AS `Product Name`, COUNT(*) AS Events \ FROM cc_data_view \ WHERE daterange BETWEEN '2023-01-01' AND '2023-02-01' \ AND product_category = '{category_filter.value}' \ GROUP BY 1 \ ORDER BY Events DESC \ LIMIT 10; df = data.DataFrame() df = df.groupby('Product Name', as_index=False).sum() plt.figure(figsize=(15, 3)) sns.barplot(x='Events', y='Product Name', data=df) plt.show() display(data) |
| code language-python |  |
| data = %sql SELECT DISTINCT product_category FROM cc_data_view WHERE daterange BETWEEN '2023-01-01' AND '2024-01-01'; style = {'description_width': 'initial'} category_filter = widgets.Dropdown( options=[d for d, in data], description='Product Category:', style=style ) display(category_filter) |  |
| code language-python |  |
| import seaborn as sns import matplotlib.pyplot as plt data = %sql SELECT product_name AS `Product Name`, COUNT(*) AS Events \ FROM cc_data_view \ WHERE daterange BETWEEN '2023-01-01' AND '2023-02-01' \ AND product_category = '{category_filter.value}' \ GROUP BY 1 \ ORDER BY Events DESC \ LIMIT 10; df = data.DataFrame() df = df.groupby('Product Name', as_index=False).sum() plt.figure(figsize=(15, 3)) sns.barplot(x='Events', y='Product Name', data=df) plt.show() display(data) |  |
| RStudio | Enter the following code block in a new chunk. Ensure you use an appropriate category. For examplee, Hunting . code language-r ## Dimension 1 Filtered by Dimension 2 value df <- dv %>% filter(daterange >= "2023-01-01" & daterange < "2023-02-01" & product_category == "Hunting") %>% group_by(product_name) %>% count() %>% arrange(desc(n), .by_group = FALSE) print(df) Run the chunk. You should see output similar to the screenshot below. | code language-r | ## Dimension 1 Filtered by Dimension 2 value df <- dv %>% filter(daterange >= "2023-01-01" & daterange < "2023-02-01" & product_category == "Hunting") %>% group_by(product_name) %>% count() %>% arrange(desc(n), .by_group = FALSE) print(df) |
| code language-r |  |
| ## Dimension 1 Filtered by Dimension 2 value df <- dv %>% filter(daterange >= "2023-01-01" & daterange < "2023-02-01" & product_category == "Hunting") %>% group_by(product_name) %>% count() %>% arrange(desc(n), .by_group = FALSE) print(df) |  |

recommendation-more-help
