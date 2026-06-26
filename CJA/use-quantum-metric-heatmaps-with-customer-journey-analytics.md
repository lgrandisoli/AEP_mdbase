---
title: "Use Quantum Metric heatmaps with Customer Journey Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/third-party/qm/heatmap"
category: "other"
topic: "analytics-platform/using/cja-usecases/third-party"
created_at: "2026-06-02T19:09:12.361563+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Use Quantum Metric heatmaps with Customer Journey Analytics

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- User
- Admin

Linking Quantum Metric heatmapping to CJA data lets you better understand page-level engagement and optimize pages based on consumer behavior. Workspace can be used to understand consumer user flows and see what paths consumers follow from one page to the next. Then, you can click hyperlinked Page URLs to visually heatmap how users engage with the content. By linking Quantum Metric Heatmapping to CJA, you can now associate page-level interactions with business outcomes, taking your analysis to the next level.

The table will return all the sessions in that segment, and you can click any one of them to explore further in QM. Learn more about Quantum Metric session replay at https://www.quantummetric.com/platform/session-replay

## Prerequisites

You must be entitled to Quantum Metric’s **UX Ops** package in order to access Quantum Metric’s heatmap capabilities.

## Step 1: Configure links in Analysis Workspace

- Log in to experience.adobe.com .
- Navigate to Customer Journey Analytics, and select Workspace in the top menu.
- Select an existing project, or create a project.
- Create a Freeform table .
- Drag the page URL dimension to the Workspace canvas.
- Right-click the dimension column header, then select Create hyperlinks for all dimension items .
- Select Create a custom URL .
- Paste the following URL structure: code language-none $value?qm-visible=true
- Click Create .
- Test one of the links to see if it opens in the URL with the Quantum Metric extension visible. These links open in a new tab so your Workspace project remains open.

## Step 2: View heatmaps by clicking links within Customer Journey Analytics

Once you’ve found a page that you want to explore heatmapping, you can apply it to the desired panel. The table returns a URL that lets you explore heatmaps, scroll depth, and key zones for interaction using Quantum Metric. See [Quantum Metric heatmap product overview](https://www.quantummetric.com/platform/interaction-heatmaps) for more information. You can also contact your Quantum Metric customer support representative or submit a request through the [Quantum Metric Customer Request Portal](https://community.quantummetric.com/s/public-support-page).

recommendation-more-help
