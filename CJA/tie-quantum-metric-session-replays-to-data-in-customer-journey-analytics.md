---
title: "Tie Quantum Metric session replays to data in Customer Journey Analytics"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-usecases/third-party/qm/tie-session-replays"
category: "other"
topic: "analytics-platform/using/cja-usecases/third-party"
created_at: "2026-06-02T19:09:12.693234+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Tie Quantum Metric session replays to data in Customer Journey Analytics

Last update: May 13, 2026
- Topics:
- [Use Cases](#)

CREATED FOR:

- User
- Admin

By linking Quantum Metric session replays with CJA data, customers can better understand “the why” behind “the what”. Workspace can be used to discover sessions with friction, then you can click hyperlinked session IDs to explore the session replay in Quantum Metric. This data allows for viewing behavior within a session and a better understanding of what drives consumer friction. Through session replays tied with CJA, you can capture critical context around customer behavior in your experience.

## Prerequisites

These steps assume that you use tags in Adobe Experience Platform Data Collection. You can adapt these data collection methods towards a manual Web SDK implementation if your organization does not use tags.

See the [Quantum Metric tag extension](/en/docs/experience-platform/destinations/catalog/analytics/quantum-metric) documentation for more information.

## Step 1: Create a schema field to accommodate Quantum Metric session ID

This use case requires a dedicated schema field to send data to. You can create this field in any desired location in your schema and name it whatever you’d like. Example values are provided if your organization does not have a preference on name or location.

- Log in to [experience.adobe.com](https://experience.adobe.com).
- Navigate to **Data Collection** > **Schemas**.
- Select the desired schema from the list.
- Select the icon next to the desired object. For example, next to Implementation Details.
- On the right, enter the desired Name. For example, qmSessionId.
- Enter the desired Display name. For example, Quantum Metric session ID.
- Select the Type as **String**.
- Select **Save**.

## Step 2: Capture the Quantum Metric session ID using the Quantum Metric tag extension

Follow these steps to append the Quantum Metric session ID to the data that you send to Adobe Experience Platform.

- Log in to experience.adobe.com .
- Navigate to Data Collection > Tags .
- Select the desired tag property.
- Select Data Elements , then select Add Data Element .
- Set the following settings: Name : Quantum Metric session ID Extension : Core Data Element Type : Custom Code
- Select the Open Editor button and paste in the following code: code language-js // Check for the presence of the Quantum Metric session ID cookie const qmCookie = _satellite.cookie.get("QuantumMetricSessionID"); if(qmCookie != null) return qmCookie; // If a cookie is not set, check local storage const qmLocalStorage = JSON.parse(localStorage.getItem("QM_S") || "{}"); if (qmLocalStorage?.s != null) return qmLocalStorage.s;
- Select Save .

## Step 3: Map the data element to the desired XDM schema field

Now that the data element has logic to obtain the desired value, map the data element to the XDM object.

- Within the tag property, select **Data Elements**, then select the data element that houses your XDM object.
- In the right column of this data element, navigate to the path established when creating the schema field.
- Set the value to the name of the data element surrounded by percent signs. For example, %Quantum Metric session ID%.
- Select **Save**.
- Add a library, then publish your changes to production.

If your XDM object is already included in a send event action configuration, then you’ll start seeing data when the changes are published.

NOTE
Sometimes the Web SDK runs faster than the Quantum Metric code. In these cases, the session ID is sent on the subsequent hit. If a visitor bounces, then the session ID is not collected in these instances.
## Step 3: Add Quantum Metric session ID as an available dimension

Once your implementation has the above changes published, edit your existing data view to add the session ID as an available dimension in Customer Journey Analytics.

- Log in to [experience.adobe.com](https://experience.adobe.com).
- Navigate to Customer Journey Analytics, and select **Data views** in the top menu.
- Select the desired existing data view.
- Locate the Quantum Metric session ID field on the left, and drag it to the dimensions area in the center.
- In the right pane, set the [persistence](/en/docs/analytics-platform/using/cja-dataviews/component-settings/persistence) setting to Session.
- Select **Save**.

## Step 4: Configure Analysis Workspace to accommodate the session ID dimension

Create a freeform table in Workspace and configure it so that session ID values link directly to Quantum Metric.

- Log in to experience.adobe.com .
- Navigate to Customer Journey Analytics, and select Workspace in the top menu.
- Select an existing project, or create a project.
- Create a Freeform table .
- Drag the session ID dimension to the Workspace canvas.
- Right-click the dimension column header, then select Create hyperlinks for all dimension items .
- Select Create a custom URL .
- Paste the following URL structure: code language-none https://adobe.quantummetric.com/#/replay/cookie:$value
- Click Create .

Each session ID is now a clickable link. See [Create hyperlinks in a freeform table](/en/docs/analytics-platform/using/cja-workspace/visualizations/freeform-table/freeform-table-hyperlinks) for more information on adding hyperlinks to Analysis Workspace dimension items.

## Step 5: View sessions from Customer Journey Analytics

Once you’ve found an interesting segment that you want to explore session replays, you can apply it to the panel that includes your session ID links. The table returns all sessions in that segment, and you can click any one of them to explore further in Quantum Metric.

See [The enterprise guide to session replay](https://www.quantummetric.com/resources/ebook/the-enterprise-guide-to-session-replay) on Quantum Metric for more information. You can also contact your Quantum Metric customer support representative or submit a request through the [Quantum Metric Customer Request Portal](https://community.quantummetric.com/s/public-support-page).

recommendation-more-help
