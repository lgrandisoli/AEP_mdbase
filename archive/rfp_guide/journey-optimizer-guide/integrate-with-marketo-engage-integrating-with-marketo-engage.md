---
title: "Integrate with Marketo Engage integrating-with-marketo-engage"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/adobe-solutions/marketo-engage"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:08.040521+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Integrate with Marketo Engage integrating-with-marketo-engage

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Actions](#)
- [Custom Actions](#)

CREATED FOR:

- Intermediate
- Developer
- Admin

Embark on a journey of seamless data integration with Marketo Engage. A specific custom action is available in your journeys to integrate Adobe Journey Optimizer and Marketo Engage. This custom action supports the ingestion of two key data types:

- **Persons** (Profiles): Marketo transforms profiles into actionable insights.
- **Custom Objects**: Tailor your data with custom objects, such as products, for a personalized marketing approach.

## Prerequisites prerequisites

The following prerequisites apply to this integration:

- The customer instance of Marketo Engage must be IMS-enabled
- Marketo Engage instance and Adobe Experience Platform/Journey Optimizer instance must be in the same organization
- The customer must be provisioned with **MktoSync: Ingestion Service access**

## Configure the action configure-marketo-action

In Journey Optimizer, you must configure a custom action for Marketo Engage. Follow these steps:

- Select Configurations in the ADMINISTRATION menu section.
- In the Actions section, click Create Action . The action configuration pane opens on the right side of the screen.
- Enter Name, Description, and select Adobe Marketo Engage as Action type {align="left" width="40%"}
- Click the Edit payload icon for your Request and Response payloads.
- For both, compose your payload and paste it in the dedicated popup. {align="left" width="70%"}
- Inspect and configure payload values Note: To pass values dynamically, for each field change Constant to Variable . {align="left" width="70%"}
- Click Save in the Field configuration screen, then Save your custom action.

You can now use your custom action on your journey canvas.

## Payload syntax payload-syntax

### Person

### CustomObject

**Payload Example for Person**

```
{
   "munchkinID": "388-KKG-245",
   "person": {
    "priority": "normal",
    "partitionName": "XYZ",
    "dedupeFields": {
      "field1": "email",
      "field2": "firstName"
    },
    "objects": [
      {
        "email": "Email address",
        "firstName": "First name",
        "lastName": "Last name"
      }
    ]
  }
}
```

**Payload Example for Custom Object**

```
{
  "munchkinID": "388-KKG-245",
  "customObject": {
    "priority": "normal",
    "objectName": "products",
    "objects": [
      {
        "email": "Email Address",
        "productName": "Product Name",
        "productQty": "Product Quantity",
        "priceTotal": "Price Total"
      }
    ]
  }
}
```

## Use the action engage-using

For each action configured, a Marketo Engage action activity is available in the journey designer palette.

To use it, follow these steps:

- Drag the custom action onto the journey canvas.
- Enter the label and the description of this action.
- In the Request parameters section, click the Edit icon for each of the parameters and select the dynamic values that you have configured in the payload.

{align="left" width="70%"}

recommendation-more-help
