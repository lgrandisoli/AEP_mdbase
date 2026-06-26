---
title: "Data Governance overview data-governance-overview"
url: "https://experienceleague.adobe.com/en/docs/experience-platform/data-governance/home"
category: "overview"
topic: "experience-platform/data-governance-guide"
created_at: "2026-05-29T16:54:35.019022+00:00"
---
Breadcrumbs: Documentation > Experience Platform > Data Governance Guide

# Data Governance overview data-governance-overview

Last update: May 13, 2026
- Topics:
- [Data Governance](#)

CREATED FOR:

- User
- Developer
- Admin

One of the core capabilities of Adobe Experience Platform is to bring data from multiple enterprise systems together to better allow marketers to identify, understand, and engage customers. This data may be subject to usage restrictions defined by your organization or by legal regulations. It is therefore important to ensure that your data operations within Experience Platform are compliant with data usage policies.

Manage customer data and ensure compliance with regulations, restrictions, and policies applicable to data use with Adobe Experience Platform Data Governance. Data governance plays a key role within Experience Platform at various levels, including cataloging, data lineage, data usage labeling, data usage policies, and controlling usage of data for marketing actions.

NOTE
In Experience Platform, data governance is only concerned with how data is used or activated, regardless of the user performing the action. For information on how to control access to specific data fields for certain Experience Platform users within your organization, see the documentation on
attribute-based access control
instead.
## Data governance roles data-governance-roles

As a concept, data governance is neither automatic, nor does it occur in a vacuum. What began as a role for one individual, typically recognized as a data steward, has grown considerably as the data governance ecosystem has expanded. Today, data governance requires continual management and monitoring in order to be successful. Effective data governance relies on data stewards having tools with which data can be properly labeled, usage policies can be created, and compliance with those policies can be enforced.

While data governance should be the responsibility of every individual in the organization, here are some of the essential roles within the data governance cycle:

### Data steward data-steward

Data stewards are the heart of data governance. This role is responsible for interpreting regulations, contractual restrictions, and policies, and applying them directly to the data. Informed by their understanding of these regulations, restrictions, and policies, the role of a data steward includes:

- Reviewing data, datasets, and data samples to apply and manage metadata usage labeling.
- Creating data policies and applying them to datasets and fields.
- Communicating data policies to the organization.

### Marketer marketer

Marketers are the end point of data governance. They request data from the data governance infrastructure created by data stewards, scientists, and engineers. Marketers encompass a number of different specialties under the marketing umbrella, including the following:

- Marketing Analysts request data to enable understanding of customers, both as individuals and in groups (also known as segments).
- Marketing Specialists and Experience Designers use data to design new customer experiences.

## Data Governance framework data-governance-framework

The Data Governance framework simplifies and streamlines the process of categorizing data and creating data usage policies. Once data labels have been applied and data usage policies are in place, marketing actions can be evaluated to ensure the correct use of data.

There are three key elements to the Data Governance framework: Labels, Policies, and Enforcement.

- **Labels:** Classify data that reflects privacy-related considerations and contractual conditions to be compliant with regulations and organization policies.
- **Policies:** Describe what kinds of marketing actions are allowed or not allowed to be taken on specific data.
- **Enforcement:** Uses the policy framework to advise and enforce policies across different data access patterns.

## Data usage labels data-usage-labels

Data Governance enables data stewards to apply usage labels at the schema field level to categorize data according to the type of policies that apply.

The Data Governance framework includes predefined data usage labels that can be used to categorize data in three ways:

- **Contract “C” Data Labels:** Label and categorize data that has contractual obligations or is related to customer data governance policies.
- **Identity “I” Data Labels:** Label and categorize data that can identify or contact a specific person.
- **Sensitive “S” Data Labels:** Label and categorize data related to sensitive data such as geographic data.

NOTE
See the guide on
supported data usage labels
for a complete list of available labels, and definitions for each label type.
Labels can be applied at any time, providing flexibility in how you choose to govern data. Best practice encourages labeling data when it is ingested into Experience Platform, or as soon as data becomes available in Experience Platform.

See the overview on [data usage labels](/en/docs/experience-platform/data-governance/labels/overview) for more information on how data usage labels are used to help enforce data governance compliance.

## Data usage policies data-usage-policies

For data usage labels to effectively support data compliance, data usage policies must be implemented. Data usage policies are rules that describe the kinds of marketing actions that you are allowed to, or restricted from, performing on data within Experience Platform.

An example of a marketing action might be the desire to export a dataset to a third-party service. If there is a policy in place declaring that Personally Identifiable Information (PII) cannot be exported, and an “I” label (identity data) has been applied to the field level from its schema. Policy Service then prevents any action that would export this dataset to a third-party destination. Should one of these action attempts occur, Policy Service sends a message telling you that a data usage policy has been violated.

There are two types of policies available:

- **Data governance policy**: Restrict data activation based on the marketing action being performed and the data usage labels carried by the data in question.
- **Consent policy**: Filter the profiles that can be activated to [destinations](/en/docs/experience-platform/destinations/home) based on your customers’ consent or preferences.

Once data usage labels have been applied, data stewards can create policies using the Policy Service API or the Experience Platform user interface. For more information on data usage policies and marketing actions, see the [policies overview](/en/docs/experience-platform/data-governance/policies/overview).

IMPORTANT
All data usage policies (including core policies provided by Adobe) are disabled by default. For an individual policy to be considered for enforcement, you must manually enable that policy.
## Next steps

This document provided a high-level introduction to Data Governance and the Data Governance framework. You can now continue to the [data usage labels user guide](/en/docs/experience-platform/data-governance/labels/user-guide) and start adding usage labels to your experience data.

## Appendix

The following section provides additional information regarding Data Governance.

### Data Governance terminology data-governance-terminology

The following table outlines key terms related to Data Governance and theData Governance framework.

Term
Definition
Contract labels
Contract “C” labels are used to categorize data that has contractual obligations or is related to your organization’s data governance policies.
Cross-site data
Cross-site data is the combination of data from several sites. Cross-site data includes both on-site and off-site data, or a combination of data from several off-site sources.
Data governance
Data governance encompasses the strategies and technologies used to ensure that data is in compliance with regulations and corporate policies with respect to data usage.
Data steward
The data steward is the person responsible for the management, oversight, and enforcement of an organization’s data assets. A data steward also ensures that data governance policies are safeguarded and maintained to be compliant with government regulations and organization policies.
Data usage labels
Data usage labels provide users the ability to categorize data that reflects privacy-related considerations and contractual conditions to be compliant with regulations and corporate policies.
Dataset labels
Labels can be added to a schema. All fields within a dataset inherit the schema’s labels.
Field labels
Field labels are data governance labels that are either inherited from a schema or applied directly to a field. Data governance labels applied to a field are not inherited up to the schema level.
Geofence
A geofence is a virtual geographic boundary, defined by GPS or RFID technology, that enables software to trigger a response when a mobile device enters or leaves a particular area.
Identity labels
Identity “I” labels are used to categorize data that can identify or contact a specific person.
Interest-based targeting
Interest-based targeting, also known as personalization, occurs if the following three conditions are met:Data collected on-site is,

- Used to make inferences about a users’ interest,
- Used in another context, such as on another site or app (off-site)
- Used to select which content or ads are served based on those inferences.

Marketing action
A marketing action, in the context of the data governance framework, is an action that an Experience Platform data consumer takes, for which there is a need to check for violations of data usage policies
Policy
In the data governance framework, a policy is a rule that describes what kinds of marketing actions are allowed or not allowed to be taken on specific data.
Schema Labels
Manage the labels for data governance, consent, and access control at the schema level. This propagates the labels to every dataset that uses that schema.
Sensitive Labels
Sensitive “S” labels are used to categorize data that you, and your organization, consider sensitive.
## Additional resources

The following video is intended to support your understanding of the Data Governance framework.

IMPORTANT
The video references applying labels to individual dataset fields. This workflow has been deprecated.
Labels must now be applied at the schema field level
. The concepts in the video remain accurate, but the labeling workflow has changed.
https://video.tv.adobe.com/v/29708?quality=12&enable10seconds=on&speedcontrol=on&learn=on
https://video.tv.adobe.com/vc/29708/eng.json
The following video provides guidance on how to apply data usage labels to your schemas or the entirety of a dataset in Experience Platform.

https://video.tv.adobe.com/v/29709/?learn=on
https://video.tv.adobe.com/vc/29709/eng.json
recommendation-more-help
