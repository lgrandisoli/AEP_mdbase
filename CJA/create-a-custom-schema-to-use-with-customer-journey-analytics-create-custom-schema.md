---
title: "Create a custom schema to use with Customer Journey Analytics create-custom-schema"
url: "https://experienceleague.adobe.com/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-create"
category: "other"
topic: "analytics-platform/using/compare-aa-cja/upgrade-to-cja"
created_at: "2026-06-02T19:06:54.855435+00:00"
---
Breadcrumbs: Documentation > Customer Journey Analytics > Customer Journey Analytics Guide

# Create a custom schema to use with Customer Journey Analytics create-custom-schema

Last update: May 13, 2026
- Topics:
- [Basics](#)

CREATED FOR:

- Admin

NOTE
Follow the steps on this page only after you complete all previous upgrade steps. You can follow the recommended upgrade steps (recommended for most organizations), or you can follow steps that are dynamically generated for your organization with the Customer Journey Analytics Upgrade Guide.
- Recommended upgrade steps (Recommended for most organizations) A set of steps that lead to an ideal Customer Journey Analytics implementation. For detailed information, see Upgrade from Adobe Analytics to Customer Journey Analytics .
- Customer Journey Analytics Upgrade Guide (Custom steps tailored to the specific needs of your organization) A new upgrade guide is available that dynamically generates upgrade steps that are tailored for your organization and your unique circumstances. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

IMPORTANT
Before you begin creating your custom schema, work with your data team and other stakeholders throughout your organization to identify your organization’s ideal schema design for Customer Journey Analytics and the other Adobe Experience Platform applications you use. For more information, see
Architect your schema for use with Customer Journey Analytics
.
The following sections describes how to create a schema that can be used with Customer Journey Analytics. The following schema options are available:

- Custom XDM schema: (Recommended) Allows for a streamlined schema that is tailored to the needs of your organization and the specific Platform applications that you use. Any required future changes are straightforward.
- Adobe Analytics schema that uses the Adobe Analytics ExperienceEvent field group: Requires the addition of thousands of unneeded fields. Any required future changes are more difficult.

For more information about these schema options, see [Choose your schema for Customer Journey Analytics](/en/docs/analytics-platform/using/compare-aa-cja/upgrade-to-cja/schema/cja-upgrade-schema-existing).

## Create the schema

The custom schema you define for your Web SDK implementation represents the model of the data that you collect into Adobe Experience Platform.

To create a custom schema:

- In Adobe Experience Platform, in the left rail, select Schemas within DATA MANAGEMENT.
- Select Create schema .
- In the Select a class step of the Create schema wizard: Select Experience Event . note info INFO An Experience Event schema is used to model the behavior of a profile (like scene name, push button to add to cart). An Individual Profile schema is used to model the profile attributes (like name, email, gender). Select Next .
- In the Name and review step of the Create schema wizard: Enter a Schema display name for your schema and (optional) a Description . Select Finish .
- Add all field groups that contain any fields that you want to include in your schema. Field groups are reusable collections of objects and attributes that allow you to easily extend your schema. In the Field groups section, select + Add . In the Add fields groups dialog, select the AEP Web SDK ExperienceEvent field group from the list. You can select the preview button, to see a preview of the fields that are part of this field group, like web > webPageDetails > name . Select Back to close the preview. (Optional) Select any additional field groups that you want to include. If you chose to use the default Adobe Analytics schema rather than creating a custom XDM schema, you can add the Adobe Analytics ExperienceEvent field group now. However, Adobe recommends creating a custom XDM schema rather than adding this field group. For more information about these schema options, see Choose your schema for Customer Journey Analytics . Select Add field groups .
- (Optional) If you have custom fields that you want to include in your schema, create a custom field group and add the custom fields to the field group. In the Field groups section, select + Add . In the Add fields groups dialog, select Create new field group . Specify a display name and optional description, then select Add field groups .
- Select + next to your schema name in the Structure panel.
- In the Field Properties panel, enter Identification as the name, Identification as the Display name, select Object as the Type and select ExperienceEvent Core v2.1 as the Field Group. note NOTE If that field group is not available, look for another field group containing identity fields. Or create a new field group and add new identity fields (like ecid , crmId , and others you need) to the field group and select that new field group. The identification object adds identification capabilities to your schema. In your case, you want to identify profiles visiting your site using the Experience Cloud ID and email address. There are many other attributes available to track your person’s identification (for example customer id, loyalty id). Select Apply to add this object to your schema.
- Select the ecid field in the identification object you just added, and select Identity and Primary Identity and ECID from the Identity namespace list in the right panel. You are specifying the Experience Cloud Identity as the primary identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles with the same ECID. Select Apply . You see that a fingerprint icon appears in the ecid attribute.
- Select the email field in the identification object you just added, and select Identity and Email from the Identity namespace list in the Field Properties panel. You are specifying the email address as another identity the Adobe Experience Platform Identity service can use to combine (stitch) the behavior of profiles. Select Apply . You see that a fingerprint icon appears in the email attribute. Select Save .
- (Optional) If you want to integrate Customer Journey Analytics with RTCDP, select the root element of your schema displaying the name of the schema, then select the Profile switch. You are prompted to enable the schema for profile. Once enabled, when data is ingested into datasets based on this schema, that data is merged into the Real-Time Customer Profile. See Enable the schema for use in Real-Time Customer Profile for more information. note important IMPORTANT After you enable a schema for profile, it cannot be disabled for profile.
- Select Save to save your schema. You have created a minimal schema that models the data you can capture from your website. The schema allows profiles to be identified using the Experience Cloud Identity and email address. By enabling the schema for profile, you ensure data captured from your website is added to the Real-Time Customer Profile. Next to behavior data, you can also capture profile attribute data from your site (for example details of profiles subscribing to a newsletter). To capture this profile data, you would: Create a schema based on the XDM Individual Profile class. Add the Profile Core v2 field group to the schema. Add an identification object based on the Profile Core v2 field group. Define Experience Cloud ID as primary identifier and email as identifier. Enable the schema for profile See Create and edit schemas in the UI for more information on adding and removing field groups and individual fields to a schema.
- Continue following the recommended upgrade steps or the dynamically generated upgrade steps in the Customer Journey Analytics Upgrade Guide. To access the guide from Customer Journey Analytics, select the Workspace tab, then select Upgrade to Customer Journey Analytics in the left panel. Follow the on-screen instructions.

recommendation-more-help
