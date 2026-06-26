---
title: "Work with Adobe Experience Manager content fragments aem-fragments"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/combine/aem/aem-fragments"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:44.720326+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with Adobe Experience Manager content fragments aem-fragments

Last update: May 8, 2026
CREATED FOR:

- Beginner
- User

The integration between Adobe Experience Manager and Journey Optimizer follows this data flow:

- Configure the Dispatcher : To enable Journey Optimizer to access Adobe Experience Manager Content Fragments via the Content Fragment Management API, you must first configure the Dispatcher. This is a prerequisite for the integration.
- Create and author : Content is created and configured in Adobe Experience Manager as Content Fragments.
- Tagging : Content Fragments must be tagged with the Journey Optimizer-specific tag ( ajo-enabled:{OrgId}/{SandboxName} ).
- Publish : Content Fragments are published in Adobe Experience Manager, making them available to Journey Optimizer.
- Access : Journey Optimizer fetches and displays available Content Fragments from Adobe Experience Manager publish instance in real-time.
- Integration : Content Fragments are selected and integrated into campaigns or journeys.

When a Content Fragment is published in Adobe Experience Manager, an event is sent to update the content on the Journey Optimizer side. If the update is successful, the Content Fragment becomes available within approximately 5 minutes for Unitary journeys, and in the next processing batch for batch use cases. Once the update is available in Journey Optimizer, the latest published content is used across all applicable campaigns and journeys.

AVAILABILITY
For Healthcare customers, the integration is enabled only upon licensing the Journey Optimizer Healthcare Shield and Adobe Experience Manager Extended Security for Healthcare add-on offerings.
## Create and assign a tag in Experience Manager

IMPORTANT
To enable Journey Optimizer to access Adobe Experience Manager Content Fragments via the Content Fragment Management API, you must first
configure the Dispatcher
.
Before using your Content fragment in Journey Optimizer, you need to create a tag specifically for Journey Optimizer:

- Access your Experience Manager environment.
- From the Tools menu, select Tagging .
- Click Create Tag .
- Ensure the ID adheres to the following syntax: ajo-enabled:{AJO-OrgId}/{AJO-SandboxName} .
- Click Create .
- Define your Content Fragment Model as detailed in Experience Manager documentation and assign your newly created Journey Optimizer tag.

This real-time connection ensures that your content is always up-to-date but also means that any changes to published fragments will immediately affect active campaigns and journeys.

You can now begin creating and configuring your Content Fragment for later use in Journey Optimizer. Learn more in [Experience Manager documentation](/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/managing#_blank).

## Add Experience Manager Content fragments aem-add

After creating and personalizing your AEM Content Fragments, you can now import it to your Journey optimizer campaign or journey.

- Create your Campaign or Journey .
- To access your AEM content fragment, click within any text field, or open the source code through an HTML content component.
- From the AEM Content Fragment menu in the left-pane, click Open AEM CF selector .
- Browse the list and select a Content Fragment to import into your Journey Optimizer content. note NOTE If the fragment has one or more published variations, a Variation dropdown appears in the selector. If no Variation is selected, the Main variation is used automatically. Learn more in Working with Content Fragment variations .
- Click Show filters to fine tune your Content Fragments list. By default, the Content Fragment filter is preset to display only approved Content.
- After selecting your Content Fragment , click Select to add it.
- Click View fragment to display your Fragment information. Note that opening the Fragment Info menu places the editor in read-only mode. Select Preview from the right-hand menu to view your fragment in Adobe Experience Manager.
- Click to access the advanced menu of your Fragment: Swap fragment Explore references Open in AEM
- Choose the desired fields from your Fragment to add to your content. Note that if you choose to copy the value, any future updates to the Content Fragment will not be reflected in your campaign or journey. However, using dynamic placeholders ensures real-time updates.
- To surface an image URL that is stored in a Content Fragment attribute, e.g. a path or URL field from the fragment model, insert it in your HTML with an <img> tag and the fragment attribute as the source, for example: code language-html <img src="[insert your AEM Content Fragment attribute here]"> note NOTE Relative image URLs from Adobe Experience Manager are not supported, use absolute URLs.
- Select Pills: Off to enable the pills experience to improve readability by hiding long attribute paths.
- To use personalization placeholders authored in Adobe Experience Manager inside your fragment text, define them in the Content Fragment in Adobe Experience Manager as follows: {{name}} . In Journey Optimizer, those tokens are placeholders. With the pills experience on, they appear in the AEM Content Fragment section of the right rail alongside fragment fields.
- To enable real-time personalization, all placeholders used within a Content fragment must be explicitly declared by the user as parameters in the fragment helper tag. Map those placeholders to profile attributes, contextual attributes, static strings, or predefined variables as follows: Profile or Contextual Attribute Mapping : Assign the placeholder to a profile or contextual attribute, e.g. name = profile.person.name.firstName. Static String Mapping : Assign a fixed string value by placing it within double quotes, e.g. name = “John”. Variable Mapping : Reference a variable declared earlier within the same HTML, e.g. name = ‘variableName’. In this case, ensure variableName is declared before adding the fragment ID, using following syntax: code language-html {% let variableName = attribute name %} In the example below, the month placeholder is mapped to the profile.person.birthDate attribute within the fragment. {modal="regular"}
- Click Save . You can now test and check your message content as detailed in this section . Note that the Content Fragment you selected stays active for this message. When you open the Personalization Editor in another field or content block, you can keep working with the same fragment from the AEM Content Fragment section and add more fields without reopening Open AEM CF selector .

Once you have performed your tests and validated the content, you can [send your campaign](/en/docs/journey-optimizer/using/campaigns/action-campaigns/review-activate-campaign) or [publish your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/publish-journey) to your audience.

Adobe Experience Manager allows you to identify the Journey Optimizer campaigns or journeys where a Content Fragment is being used. Learn more in [Adobe Experience Manager documentation](/en/docs/experience-manager-cloud-service/content/sites/administering/content-fragments/extension-content-fragment-ajo-external-references#_blank).

## Working with content fragment variations aem-variations

In Adobe Experience Manager, each Content Fragment is made up of the following:

- **Main**: the core content of the fragment which always exists, cannot be deleted, and is the basis for all variations.
- **Variations**: one or more permutations of **Main** that authors create for specific channels or scenarios. Variations live inside the fragment not as separate assets and can be compared and synchronized with **Main**.

Examples of variation use cases:

- A short version of copy for a push notification and a longer version for email.
- Regional tone adjustments without creating a separate fragment.
- Channel-specific messaging (for example web compared to mobile).

➡️ [Learn more in Adobe Experience Manager documentation](/en/docs/experience-manager-65/content/assets/content-fragments/content-fragments-variations)

Journey Optimizer lets you choose which variation to use when you insert a fragment, so different campaigns or journeys can rely on different renditions of the same source content in Adobe Experience Manager without duplicating fragments.

To select a variation:

- Open a campaign or journey .
- Click in any text field, or open the HTML source from an HTML content component.
- From AEM Content Fragment , click Open CF selector .
- To select a locale-specific Adobe Experience Manager Content Fragment in table view, use Customize table to add the Language column. Locale values are displayed in the table, enabling you to identify and select the appropriate fragment.
- Select your Content Fragment .
- Click the to open Details menu. If the fragment has one or more published variations, a Variation dropdown appears next to the fragment details.
- From the Quick details menu, click Explore references to open related options in Adobe Experience Manager for variation details, preview, and proof when available.
- Choose your variation, then click Select . note NOTE If you do not select a variation, or if the fragment was added before variation support was available, Journey Optimizer uses the Main variation automatically at delivery time.

After you insert a fragment with a variation, republishing it in Adobe Experience Manager updates every **referenced variation** in active campaigns or journeys automatically. Previews and proofs still use the variation you chose, with the latest published content for that variation.

recommendation-more-help
