---
title: "Detect potential conflicts in journeys & campaigns conflict"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/conflict-prioritization/conflicts"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:32.871094+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Detect potential conflicts in journeys & campaigns conflict

Last update: May 8, 2026
CREATED FOR:

- Beginner
- User

As marketers increase the volume of Campaigns and Journeys in Journey Optimizer, it becomes increasingly difficult for a marketer to know if they are bombarding their customers with too many marketing interactions. It is therefore essential to easily identify when there are overlapping campaigns and journeys to ensure they are striking the right balance of marketing communications while mitigating the risk of customer fatigue.

Key areas to monitor for potential overlap are:

- **Timeline** (start and end dates): Are too many journeys running simultaneously?
- **Audience**: What percentage of my journey audience is also part of other journeys?
- **Channel**: Are there other communications scheduled for the same timeframe, and if so, how many?
- **Capping Rule Set**: Which types of journeys am I capping and is there overlap within those?
- **Channel Configuration**: Are there other journeys or campaigns using any channel configuration that is being used in the same journey or campaign that might prevent the journey or campaign from being shown to the end user?

➡️ [Discover this feature in video](#video)

## How Journey Optimizer detects conflicts detection

Below is a summary of how Journey Optimizer identifies potential conflicts for journeys and campaigns:

- **Conflict identification scope**: Conflicts are shown only for live or scheduled campaigns and journeys.
- **Unitary journeys**: If the selected journey is unitary, other journeys that start with the same event are displayed, as this event will trigger all such journeys.
- **Audience qualification and Read Audience/Business Event** journeys: If the selected journey is either an Audience qualification or a Read Audience/Business Event journey, all other journeys of the same type with a valid audience are displayed, as there can be overlaps between the audiences.
- **Campaigns**: Since all campaigns are targeting audiences and there is no concept of events, all campaigns potentially conflict with segment-triggered journeys (starting with a Read audience activity).
- **Live/Scheduled campaigns**: Live and scheduled campaigns may conflict with one another due to potential audience overlap. For any given campaign, all live or scheduled campaigns are listed in the conflict viewer.

## View identified conflicts for a given journey or campaign view

When authoring a journey or campaign, Journey Optimizer allows you to check whenever there’s a possibility of overlap with other journeys or campaigns. To do this, follow these steps:

- At the time of authoring a journey or campaign, click the View Potential Conflicts button in the journey or campaign properties. note NOTE The View potential conflicts button becomes available to select as soon as you have assigned any of the following settings: Start / end date , Audience , Channel , Channel configuration , and Rule set . Ensure you select Save after assigning these settings, as the button will not be selectable until changes are saved.
- The Potential conflicts window opens, allowing you to visualize all elements that are overlapping the current journey/campaign. You can open an overlapping journey or campaign directly from this screen by selecting its name. note NOTE Newly published journeys and campaigns might take up to 3-7 minutes to show up in the conflict viewer, due to caching implemented.

To further refine your search for potential overlaps, you can filter your list of campaigns and journeys based on whichever field(s) are relevant. To do this, select the filter icon in the inventory view. [Learn how to work with filters](/en/docs/journey-optimizer/using/get-started/work-efficiently/search-filter-categorize#filter-lists)

## Resolve conflicts resolve

Here are some tips to reduce the potential conflicts once they have been identified:

- Adjust the **start/end dates** to avoid overlapping campaigns or journeys.
- Refine **audience targeting** to minimize overlap between journeys.
- Implement **frequency caps** to prevent customers from receiving too many communications.
- Reduce the number of **active journeys** to manage customer experience more effectively.
- Set **priorities** on inbound actions to ensure the most important action is displayed to customers.

By leveraging these capabilities, you can ensure your marketing efforts are aligned and that you maintain the right balance in your communications strategy.

## How-to video video

https://video.tv.adobe.com/v/3435528?quality=12&learn=on
recommendation-more-help
