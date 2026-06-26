---
title: "Journey Fragments journey-fragments"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/journey-fragments"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:26.719630+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

[Limited Availability]{class="badge informative"}

# Journey Fragments journey-fragments

Last update: May 8, 2026
- Applies to:
- Journey Orchestration

- Topics:
- [Journeys](#)

CREATED FOR:

- Intermediate
- User

AVAILABILITY
This capability is currently in Limited Availability. To request access, contact your Adobe representative.
Journey Fragments are reusable sets of journey nodes that you can build once and drop into any journey across your sandbox. Whether it’s an eligibility check, a preferred channel routing logic, or a welcome sequence, fragments help teams move faster and stay consistent — without rebuilding the same logic from scratch every time. [See use case examples.](#examples)

Once created, fragments are stored in a dedicated **Fragment Inventory** and can be inserted into any journey using the **Journey fragments** activity.

NOTE
Journey fragments use a
copy behavior
: inserting a fragment into a journey creates a static copy of the original nodes. Any updates made to the original fragment are not reflected in journeys that have already used it.
## Permissions journey-fragments-permissions

To work with journey fragments, you need the following [permissions](/en/docs/journey-optimizer/using/access-control/permissions):

- **Manage Journeys** — required to create, edit, and delete fragments.
- **Publish Journeys** — required to activate a fragment.

## Access the Fragment Inventory journey-fragments-inventory

Journey fragments are accessible from the **Journeys** section. Open the **Fragments** tab to browse all available fragments in your sandbox.

You can filter the list by fragment name, status, creation date, creator, last modified date, or tag.

## Create a journey fragment create-journey-fragment

You can create a journey fragment in two ways: directly from the journey canvas (recommended), or from the Fragment Inventory.

From the journey canvas
To save journey nodes as a fragment directly from the journey canvas:

- Open a journey and select one or more connected nodes on the canvas.
- Click the Save as Fragment icon in the toolbar.
- Enter a unique name for the fragment within your sandbox.
- Click Save . The fragment is saved as a draft.

| note tip |
| --- |
| TIP |
| If you create a fragment from a journey, [test or simulate your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) **before** saving the fragment to ensure the selected nodes behave as expected. |

From the fragment inventory
To create a fragment directly from the inventory:

- Navigate to **Journeys** > **Journey fragments** tab.
- Click **Create journey fragment**.
- In the fragment authoring canvas, add and configure journey activities.
- When done, click **Save** to save the fragment as a draft.

| note caution |
| --- |
| CAUTION |
| Test mode and simulation are not available in the fragment editor. This means you cannot validate the behavior of the configured activities before the fragment is activated and inserted into a journey. For fragments where logic accuracy is critical, consider [building and testing or simulating the nodes in a full journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) first, then saving them as a fragment from the canvas tab above. |

## Edit a fragment edit-journey-fragment

To edit a fragment, open it from the **Fragment Inventory** by clicking its name. In the fragment authoring UI, you can:

- Add, remove, or modify activities.
- Set or update fragment properties: name, tags, and labels.

NOTE
- Only Draft fragments can be edited. To modify an Active fragment, deactivate it first.
- Test mode and simulation are not available in the fragment editor. Test or simulate any journey-level logic in the full journey before saving nodes as a fragment.
- Jump activities are not allowed inside a fragment.

## Manage your fragments manage-journey-fragments

### Fragment statuses fragment-statuses

Journey fragments follow a lifecycle with the following statuses:

Status
Description
Draft
The fragment is being authored and is not yet available for use in journeys.
Active
The fragment is ready to be used in journeys.
Archived
The fragment has been archived and is no longer available for use in journeys.
The following rules apply to fragment status transitions:

- Only **Draft** fragments can be activated. Open a draft fragment and use the **Activate** icon.
- Only **Active** fragments can be deactivated or archived.
- Only **Archived** fragments can be unarchived. Unarchiving a fragment returns it to **Draft** state.
- Only **Draft** fragments can be deleted.

NOTE
When activating a fragment, most of the same validation checks that run during journey publication are applied. However,
contextual attributes are not validated
and
governance policies are not enforced
at activation time — both are evaluated when the fragment is inserted and used in a journey.
### Fragment actions fragment-actions

From the fragment inventory, you can perform the following actions on a fragment:

- **Open**: edit the fragment by clicking on its name.
- **Duplicate**: create a copy of the fragment, from the **More actions** (…) icon.
- **Archive**: archive a fragment (available for **Active** fragments only), from the **More actions** (…) icon. Archived fragments are no longer available in the fragment picker.
- **Unarchive**: restore an archived fragment (available for **Archived** fragments only), from the **More actions** (…) icon. The fragment returns to **Draft** state.
- **Delete**: permanently delete a fragment (available for **Draft** fragments only), from the **More actions** (…) icon.
- **Edit tags**: add or remove tags of a fragment, from the **More actions** (…) icon.

## Use a fragment in a journey use-journey-fragment

To insert a fragment into a journey:

- Open your journey and drag the **Journey fragments** activity from the left rail.
- Drop it into an existing branch, or onto an empty canvas. A fragment picker appears.
- Browse or search for the fragment you want to use. You can preview a fragment or open it in another tab before inserting it.
- Select the fragment. Its nodes are copied into the canvas at the drop point.

NOTE
Only
Active
fragments are available in the picker. Inserting a fragment creates a
static copy
of its nodes — any subsequent updates to the original fragment are not reflected in the journey.
When dropping a fragment onto an empty canvas, the fragment must start with a
Read Audience
,
Audience Qualification
, or
Event
node (same rule as when starting any journey).
## Guardrails and limitations guardrails

The following guardrails apply to journey fragments:

**Fragment creation**

- Fragment names must be **unique per sandbox**.
- A fragment can only have **one entry path**. Selections with more than one entry point cannot be saved as a fragment.
- Only **connected nodes** can be saved together as a fragment.
- A fragment **cannot contain a Jump activity**.
- A fragment can contain a **maximum of 20 nodes**.
- A sandbox can have a **maximum of 200 active fragments**.

**Fragment usage**

- Only **Active** fragments can be inserted into a journey.
- Inserting a fragment creates a **static copy** of its nodes. Updates to the original fragment are not propagated to journeys where it has been used.
- A fragment can be dropped into an existing branch or onto an empty canvas. When dropped onto an empty canvas, the fragment must start with a **Read Audience**, **Audience Qualification**, or **Event** node.

**General**

- Fragments can be found using the [Unified Search](/en/docs/journey-optimizer/using/get-started/work-efficiently/search-filter-categorize) bar under the **Journey Fragments** category.
- [Tags](/en/docs/journey-optimizer/using/orchestrate-journeys/manage-journey/tags) and **Labels** are supported on fragments.
- [Audit Logs](/en/docs/journey-optimizer/using/privacy/audit-logs) are supported.
- Journeys running on the old stack (using Inline Campaigns) do not support journey fragments. Duplicate such a journey to move to the new stack before using this feature.

## Use case examples examples

The following examples illustrate common journey patterns that can be saved and reused as journey fragments.

**Eligibility checks**

A standard entry pattern — such as a [Read Audience](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/read-audience) node followed by eligibility filters — can be encapsulated into a fragment. This allows teams to maintain consistency in how profiles enter journeys while reducing setup time. The fragment can be the [Optimize](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize) activity only, or the Read Audience and Optimize activity together.

**Preferred channel**

A fragment can evaluate a profile’s preferred communication channel — email, push, or SMS — and route the profile accordingly. This logic can be reused across any journey involving outbound messaging, ensuring consistent channel preference management. The fragment can include the [Optimize](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize) activity and all three channel branches.

**Onboarding welcome sequence**

A timed welcome sequence — such as a series of three messages introducing a product or service — can be saved as a fragment. This is useful for onboarding new users across different audience segments or product lines. The fragment can include the [Wait](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/wait-activity) activities and the message nodes.

**Reaction-based wait and reminder**

A fragment can encapsulate an Email activity followed by a [Reaction](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/reaction-events), waiting for the profile to open the email within a set number of days and sending a reminder if they did not. This logic is commonly reused in nurturing journeys and trial conversion flows. The fragment can include the Email and Reaction activities.

recommendation-more-help
