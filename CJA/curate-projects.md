---
title: "Curate projects"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-workspace/curate-share/curate"
category: "other"
topic: "analytics-platform/using/cja-workspace/curate-share"
created_at: "2026-06-02T19:05:47.044216+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Curate projects

Last update: May 13, 2026
- Topics:
- [Curate and Share](#)

CREATED FOR:

- User

Curation lets you limit the components (dimensions, metrics, segments, date ranges) before sharing a project. When a recipient opens the project, they see a limited set of components that you have curated for them. Curation is an optional but recommended step before sharing a project.

NOTE
Product profiles are the primary mechanism governing which components a user can see. They are managed through the
CX Enterprise Admin Console
. Curation is a secondary segment.
## Apply project curation

- Select **Share** > **Curate Project Data**.The components that are used in the project are automatically added.If a project has multiple data view, you see a curate drop target for each data view in the project.
- (Optional) To add more components, drag components you want to share from the left panel to the **Curate components** drop zone for the data view.
- Select **Done**.

When a recipient opens a curated project, they only see the curated set of components you have defined:

## Remove project curation

To remove project curation and restore the full set of components in the left panel:

- Select **Share** > **Curate Project Data**.
- Select **Remove Curation**.
- Select **Done**.

## Component curation options

In a curated project, the recipient is presented with the option to **Show All** components in the left panel. Show All reveals different sets of components, depending on:

- The user’s permission level (admin or non-admin)
- Project role (owner/editor or not)
- Type of curation applied (at the project level)

Curation type
Admin can see
Non-admin project owner (or edit role) can see
Non-admin duplicate role can see
Components
hidden
from a data view
All data view components are available for reporting (hidden components require you to select
Show all
)
Not available for reporting
Not available for reporting
Components added or removed from a data view
Only components added to the data view (hidden or not hidden). Admins cannot report on fields or components that are not defined in the data view.
Only components added to the data view, or components owned by or shared with the user. Hidden components are not available (like Virtual report suite curation).
Only components added to the data view are not hidden and are included in the Project curation.
Curated components in a Project
All data view components that are available for reporting (hidden components require you to select
Show all
)
All non-hidden data view components (requires clicking “show all”)
Only curated components, plus any components owned or shared with the user
Curated Project using a data view with hidden components
All data components available for reporting (hidden and non-curated components require you to select
Show all
)
All non-curated project components, all non-hidden data view components, and any components owned by or shared with the user
Only curated components, plus any components owned by or shared with the user
recommendation-more-help
