---
title: "Create hyperlinks in freeform tables"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table-hyperlinks"
category: "other"
topic: "analytics-platform/using/cja-workspace/visualizations"
created_at: "2026-06-23T20:44:49.221083+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create hyperlinks in freeform tables

Last update: June 5, 2026
- Topics:
- [Analysis Workspace](#)

CREATED FOR:

- User

You can create hyperlinks for dimension items to make them clickable within a freeform table in Analysis Workspace.

This functionality is particularly useful when creating hyperlinks for the following types of dimension items:

- Dimension items that have URL values (for example, a Page URL dimension).
- Dimension items that contain breakdowns that have URL values (for example, a Page Name dimension that has a breakdown of a Page URL dimension).
- Dimension items or breakdowns that have values that are part of a URL (for example, a Page Name dimension that is part of a URL).

See [Create hyperlinks in a freeform table](/en/docs/analytics-learn/tutorials/analysis-workspace/tips-and-tricks/create-hyperlinks-in-freeform-tables#_blank) for a demo video.

style
shade-box
## Create hyperlinks

Consider the following when you create hyperlinks for one or more dimension items:

- The hyperlinks you create are stored on the freeform table within the Analysis Workspace project. Hyperlinks do not persist when using the same dimension or dimension items in another table or in another project.
- If you change the data view of the freeform table, any hyperlinks that were created for dimensions or dimension items in the table are still available. This functionality assumes that the dimension still exists in the data view.
- URLs are not checked for validity when you create the hyperlink. If you create a hyperlink that has an invalid URL, or create a hyperlink that references a dimension item that does not have a URL value (by either referencing the dimension item directly or by using the $value or $breakdown variables), then users who click the hyperlink see an error message stating that the URL is invalid.
- Hyperlinks that are created for a single dimension item override hyperlinks that are created on the dimension.
- Hyperlinks are not functional in downloaded PDF files .

To create hyperlinks for one or more dimension items:

- In a freeform table in Analysis Workspace, do one of the following: Create a hyperlink for a single dimension item: Right-click the dimension item within the table for which you want to create the hyperlink, then select Create hyperlink . Open the context menu for the dimension item. Select Create hyperlink from the context menu. The Create hyperlink dialog is displayed. The name of the dimension item for which you are creating a hyperlink is shown in the dialog. Create hyperlinks for all dimension items in a dimension column: Right-click the dimension name in the dimension column header, then select Create hyperlinks for all dimension items . Open the context menu from the dimension column header. Select Create hyperlink for all dimension items from the context menu. The Create hyperlinks for all dimension items dialog is displayed. The name of the dimension for which you are creating hyperlinks is shown in the dialog.
- Choose from the following options: Use the value of the dimension item as the URL : Choose this option for dimension items that have URL values, such as a Page URL dimension. For example, if you are using a Page URL dimension where the value of each dimension item is a URL, then selecting this option creates a hyperlink to the URL. Create a custom URL : Specify either a static or dynamic custom URL. Choose this option to create hyperlinks for dimension items that do not have URL values. For example: You are using a Page Name dimension where the value of each dimension item is the name of a page (and not a full URL). Then select this option to specify a hyperlink to use as the link for the dimension item. If you want to create dynamic URLs for multiple dimension items, you can use the $value and $breakdown variables within your custom URL. See the table below for more information. To create a custom URL, specify the following information: table 0-row-2 1-row-2 2-row-2 Field Description Custom URL Specify a custom URL that you want to use for the hyperlink. URLs must be entered as fully qualified URLs. For example: https://www.example.com The custom URL that you create can be static or dynamic: Static URLs: You can specify a static URL for a single dimension item or for all dimension items when you want the items to link all to the same URL. For example: https://wiki.internal.company_name/page_name#item_definition Dynamic URLs: You can create a dynamic URL if you want to create unique hyperlinks for multiple dimension items, or for all dimension items in a dimension column. To make custom URLs dynamic, you include a variable in the URL to change the URL based on the value of the dimension or the value of the breakdown dimension. When using variables, any dimension items that contain characters that are not valid in URLs (such as spaces) are URL-encoded. The following variables are available: ( Note : While you can use these variables in the same URL, it is more common to use them separately.) $value : Allows you to insert the value of the dimension item into the URL that you specify. Suppose that you want to create hyperlinks for all Page Name dimension items in a freeform table, where the value of each dimension item is part of a webpage’s URL. In this case, you can construct a single custom URL that dynamically adjusts for each dimension item. For example: https://company-name.com/browse/product#\$value When this custom URL is applied to your Page Name dimension items whose values are “ProductY” and “ProductZ”, the generated hyperlinks would look something like this: https://company-name.com/browse/product#ProductY and https://company-name.com/browse/product#ProductZ Tip : Addingd only the $value variable into the Custom URL field, is the same as selecting the Use the value of the dimension item option when creating the URL. $breakdown : Allows you to insert the value of the breakdown dimension item into the URL that you specify. With $breakdown , you can use a dimension with a user-friendly name in your report (such as a Product Name dimension). And generate a hyperlink based on a breakdown dimension that might be less user-friendly (such as a Product ID or Page URL dimension). When referencing a breakdown dimension, it’s most common to have only one breakdown item for a given dimension item. If there are multiple breakdown items for a given dimension item, the value of the first breakdown item is used in the URL. If no breakdown items are listed, the URL is invalid. The same sort order is applied to the breakdown items as is applied to the table. You specify the breakdown dimension in the Breakdown dimension field below. Consider the example scenario described for the Breakdown dimension field below. Breakdown dimension (optional) Begin typing the name of the breakdown dimension that you want to use, then select it from the drop-down menu. If you select a breakdown dimension in this field, you must reference it by using the $breakdown variable in the URL that you specify in the Custom URL field. Suppose that you want to create hyperlinks for all Product Name dimension items in a freeform table. Each Product Name dimension item contains a breakdown of a Product ID dimension. In this case, you can create hyperlinks for each Product Name dimension that directs users to the product page by using the value of the Product ID breakdown dimension. Add the $breakdown variable to the end of the custom URL that you specify in the Custom URL field. For example: https://company-name.com/browse/product/$breakdown When this custom URL is applied to your Product Name dimension items (that have breakdown dimension items whose values are “ProductY” and “ProductZ”), the generated hyperlinks look like: https://company-name.com/browse/product/ProductY and https://company-name.com/browse/product/ProductZ You would then select the Product ID dimension in the Breakdown dimension field
- Select Create . Users who view the freeform table see the hyperlinked dimension items. When clicking a dimension item, users are taken to the hyperlinked pages in a separate browser tab. add screenshot of a table with hyperlinks.
- Save the project to save your changes.

## Edit hyperlinks

You can edit hyperlinks that have been created on dimensions or dimension items in a freeform table.

- In a freeform table in Analysis Workspace, do one of the following: Edit a hyperlink for a single dimension item: Open the context menu for the dimension item. Select Edit hyperlink from the context menu. Edit hyperlinks for all dimension items in a dimension column: Open the context menu from the dimension column header. Select Edit hyperlink for all dimension items from the context menu.
- Select Edit hyperlinks for all dimension items from the right-click menu. The Edit hyperlinks for dimension items dialog is displayed.
- For information about the configuration options for editing the hyperlink, see Step 3 in the Create hyperlinks for one or more dimension items section above, then select Apply when you are finished with your updates.
- Save the project to save your changes.

## Remove hyperlinks

You can remove hyperlinks that have been created for dimension items in a freeform table.

NOTE
In a freeform table, if you delete a dimension that contains hyperlinks, the hyperlinks do not persist if you add the same dimension back to the freeform table.
To remove hyperlinks from dimension items:

- In a freeform table in Analysis Workspace, do one of the following: Remove a hyperlink from a single dimension item: Open the context menu for the dimension item. Select Remove hyperlink from the context menu. Remove hyperlinks from all dimension items in a dimension column: Open the context menu from the dimension column header. Select Remove hyperlink for all dimension items from the context menu. The hyperlink is removed from the single dimension item if you selected a single dimension item. Or from all dimension items if you selected the dimension name in the dimension column header.
- Save the project to save your changes.

recommendation-more-help
