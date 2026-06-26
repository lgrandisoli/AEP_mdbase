---
title: "Work with segments"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-reportbuilder/work-with-filters"
category: "other"
topic: "analytics-platform/using/cja-reportbuilder/work-with-filters"
created_at: "2026-06-02T19:08:56.417501+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Work with segments

Last update: May 13, 2026
- Topics:
- [Report Builder](#)

CREATED FOR:

- User

You can apply segments when you create a new data block or when you select **Edit data block** from the **Commands** panel.

## Apply segments to a data block

To apply a segment to the entire data block, Double select a segment or drag and drop segments from the components list into the segments section of the Table.

## Apply filters to individual metrics

To apply filters using segments to individual metrics:

- Drag and drop one or more segments from Segments onto a metric in the table.
- Alternatively: Select for a specific metric in the Table pane and then select Filter metric . {modal="regular"} Select one or more segments from Segments drop-down menu. The segments are added to the Segments applied list. Select to remove a segment from the Segment applied list. Or select Clear all to remove all segments from the Segment applied list. Select Apply .

To view applied filters, hover over or select a metric in the Table pane. Metrics with applied segments display a segment icon.

## Quick edit segments

You can use the **Quick edit** panel to add, remove, or replace segments for existing data blocks.

When you select a range of cells in the spreadsheet, the **Segments** link in the **Quick edit** panel displays a summary list of the segments used by the data blocks in that selection.

To edit segments using the **Quick edit** panel:

- Select a range of cells from one or multiple data blocks.
- Select the Segments link to launch the Quick edit Segments panel.

### Add or remove segments

You can add or remove segments using the Add/Remove options.

- Select the Add/Remove tab in the Quick edit Segments panel. Select one or more segments from Segments drop-down menu. The segments are added to the Segments applied list. Select to remove a segment from the Segment applied list. Select Apply .

Report Builder displays a message to confirm the applied segment changes.

### Replace segments

You can replace an existing segment with another segment to change how the data is segmented.

- Select the Replace tab in the Quick edit Segments panel.
- Use the Search list search field to locate specific segments.
- Select one or more segments that you want to replace.
- Search for one or more segments from the Replace with drop-down menu to add the segment to the Replace with list.
- Select Apply .

Report Builder updates the list of segments to reflect the replacement.

## Define data block segments from cell

Data blocks can reference segments from a cell. Multiple data blocks can reference the same cell for segments, allowing you to switch segments easily for multiple data blocks at a time.

To apply segments from a cell:

- Create a new data block or edit an existing data block.
- Select the Segments tab to define segments.
- Select . {modal="regular"}
- Select the cell from which you want the data blocks to reference a segment.
- Double select to add a segment to the cell. Alternatively, drag and drop one or more segments into the Segments included section.
- Select Apply to create the reference cell.
- From the Segments tab, add the newly created reference cell segment to your data block. {modal="regular"}
- Select Finish .

To apply the reference cell as a segment to other data blocks, use the cell reference as one of the segments in the **Segments** list in the **Table** tab.

### Use a reference cell to change data block segments

- Select the reference cell in your spreadsheet.
- Select the link under Segments from cell in the Quick Edit menu. {modal="regular"}
- Select your segment from the drop-down menu.
- Select Apply .

recommendation-more-help
