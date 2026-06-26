---
title: "Test, validate & approve section-overview"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/test/test-landing-page"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:33:43.027291+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Test, validate & approve section-overview

Last update: May 8, 2026
- Topics:
- [Get Started](#)
- [Overview](#)

CREATED FOR:

- Beginner
- Intermediate
- User

This section covers all testing and approval capabilities in Journey Optimizer. You’ll find tools to preview content with test profiles, validate journey logic, check email rendering and spam scores, run A/B experiments, detect conflicts, and set up approval workflows.

This landing page helps you choose the right testing approach based on what you’re building (campaigns vs. journeys), walks you through recommended testing workflows, and provides quick access to all testing and approval resources. Start with [Choose your testing approach](#choose-your-testing-approach) below to identify which tools apply to your use case. For definitions of key testing terms, see [Key terminology](#key-terminology).

## Test & approve content

Preview, Test, and Validate Content

Learn how to preview, test, and validate personalized content using test profiles, email rendering tests, spam score evaluations, and more.

[Explore Preview & Test Content](/en/docs/journey-optimizer/using/test/preview-test/preview-test-landing-page)

Approval Workflows for Journeys and Campaigns

Understand how to set up, manage, and execute approval processes to ensure quality control for journeys and campaigns.

[Learn About Approval Workflows](/en/docs/journey-optimizer/using/test/approve/approve-landing-page)

Test Your Journey

Validate your journey before publishing by testing it with specific profiles to ensure events, conditions, and actions work as expected. Available for draft journeys that use a namespace.

[Test your journey](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)

Journey Dry Run

Perform a dry run to simulate and validate your journey's execution path, identifying potential issues before going live.

[Learn about Journey Dry run](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run)

Monitoring & Troubleshooting

Access comprehensive troubleshooting resources, system alerts, and error codes to resolve journey execution and performance issues.

[View Monitoring & Troubleshooting](/en/docs/journey-optimizer/using/monitor/troubleshoot-journey-landing-page)

Personalization Playground

Experiment with personalization expressions in a safe environment. Test code with sample data and preview results before applying to your campaigns and journeys.

[Learn About the Personalization Playground](/en/docs/journey-optimizer/using/content-management/personalization/personalize#playground)

Content Experiments & A/B Testing

Optimize your campaigns by testing multiple content variations and measuring performance to identify the best-performing treatments. Available for campaigns only (supports A/B and multi-armed bandit experiments).

[Learn About Content Experiments](/en/docs/journey-optimizer/using/content-management/content-experiment/get-started-experiment)

Seed Lists for Stakeholder Monitoring

Automatically include internal stakeholder addresses in deliveries to monitor actual messages sent to customers for quality assurance and compliance. Available for email channel only.

[Configure Seed Lists](/en/docs/journey-optimizer/using/configuration/seed-lists)

Conflict Detection

Identify potential overlaps between campaigns and journeys to prevent overwhelming customers with too many simultaneous communications. Available for campaigns and unitary, Audience Qualification, and Read Audience journeys.

[Detect Conflicts](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts)

## Why testing and approval matter

Testing and approval processes serve as essential quality gates that protect your brand reputation and ensure campaign success. Here’s why they matter:

- Catch errors before they reach customers - Identify broken links, incorrect personalization, rendering issues, and logic flaws in a controlled environment where fixes are quick and risk-free.
- Improve deliverability - Test spam scores, validate email authentication, and check rendering across email clients to maximize inbox placement and engagement rates.
- Ensure brand consistency - Preview content with different test profiles to verify that personalization displays correctly for various customer segments and maintains brand standards.
- Validate complex journeys - Simulate multi-step journey flows to confirm that triggers fire correctly, conditions evaluate properly, and customers receive the right messages at the right time.
- Establish accountability - Implement formal approval workflows that require stakeholder sign-off, creating clear ownership and reducing unauthorized or premature campaign launches.
- Save time and resources - Detect issues early in the development cycle when fixes are cheaper and faster, preventing costly post-launch corrections or customer service escalations.

## Choose your testing approach

The right testing approach depends on what you’re building and what you need to validate. Use this guide to identify the most relevant testing tools for your scenario.

Testing campaigns
**For all campaigns:**

- Preview and test content using [test profiles](/en/docs/journey-optimizer/using/test/preview-test/test-profiles) or [sample input data](/en/docs/journey-optimizer/using/test/preview-test/simulate-sample-input)
- Check [email rendering](/en/docs/journey-optimizer/using/test/preview-test/rendering) across devices and clients (email channel only)
- Run [spam score checks](/en/docs/journey-optimizer/using/test/preview-test/spam-report) (email channel only)
- Review [conflicts](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts) with other campaigns and journeys
- Set up [seed lists](/en/docs/journey-optimizer/using/configuration/seed-lists) for stakeholder monitoring (email channel only)
- Submit for [approval](/en/docs/journey-optimizer/using/test/approve/gs-approval) before activation

**For A/B testing and optimization:**

- Create [content experiments](/en/docs/journey-optimizer/using/content-management/content-experiment/get-started-experiment) to test multiple treatments and measure performance

**For API-triggered campaigns:**

- Use the [Campaign Simulation API](https://developer.adobe.com/journey-optimizer-apis/references/simulations){target-“_blank”} to trigger proof jobs programmatically

Testing journeys
**For all journeys:**

- Use [test mode](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey) to simulate profile progression (draft journeys only, requires namespace) or [dry run](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run) to analyze execution paths without sending messages
- Test individual messages using [preview and proofs](/en/docs/journey-optimizer/using/test/preview-test/preview-test)
- Check [conflicts](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts) with other journeys and campaigns
- Submit for [approval](/en/docs/journey-optimizer/using/test/approve/gs-approval) before publishing

**For complex journeys:**

- Use test mode and dry run together to thoroughly validate branching logic and execution paths
- Test different entry conditions and profile attributes systematically

**Note:** Conflict detection and journey capping are available for unitary, Audience Qualification, and Read Audience journeys only.

Testing personalization
**Before building content:**

- Experiment in the [personalization playground](/en/docs/journey-optimizer/using/content-management/personalization/personalize#playground) to learn syntax and test expressions with sample data

**During content creation:**

- Preview with [test profiles](/en/docs/journey-optimizer/using/test/preview-test/test-profiles) to validate personalization renders correctly
- Test multiple scenarios using [sample input data](/en/docs/journey-optimizer/using/test/preview-test/simulate-sample-input) from CSV/JSON files (supports up to 30 variants)

## Testing best practices

To maximize the effectiveness of your testing efforts, follow these recommended practices:

- Test early and often - Don’t wait until a campaign is fully built. Test content, personalization, and logic incrementally as you develop.
- Use realistic test profiles - Create test profiles that accurately represent your target audience segments, including edge cases and different personalization scenarios.
- Test across devices and clients - Verify email rendering on popular email clients (Gmail, Outlook, Apple Mail) and devices (desktop, mobile, tablet) to ensure consistent display (email channel only).
- Validate personalization thoroughly - Test with multiple test profiles that have different attribute values to confirm personalization tokens render correctly and fallback values work. Use the personalization playground to experiment with personalization expressions and test code with sample data before applying them to your campaigns.
- Test content variations with sample data - Use sample input data from CSV or JSON files to test up to 30 personalization scenarios without creating numerous test profiles, saving time while ensuring comprehensive coverage. Supports email, SMS, push, web, code-based experience, in-app, and content cards channels.
- Use seed lists for stakeholder monitoring - Configure seed lists to automatically include internal stakeholders who will receive copies of all deliveries at execution time for quality monitoring and compliance verification (email channel only).
- Simulate journey paths - For complex journeys with multiple branches, use test mode to test different entry conditions and profile attributes to validate all possible paths. Available for draft journeys that use a namespace.
- Check deliverability indicators - Review spam scores , authentication status, and email health metrics before large sends (email channel only).
- Document test results - Keep records of test outcomes, issues found, and resolutions to improve future testing processes and share learnings with your team.
- Involve stakeholders early - Share previews and test results with stakeholders before formal approval to gather feedback and align expectations.

## Recommended testing workflow

Follow this 4-phase approach to validate your campaigns and journeys before launch:

Phase
What to test
Key actions
1. Content validation
Personalization, design, rendering
Preview with test profiles
, test
multiple variations
with CSV/JSON, verify
rendering
across devices
2. Technical checks
Deliverability, links, conflicts
Run
spam score checks
, validate links, check for
conflicts
with other campaigns
3. Journey logic
(journeys only)
Entry conditions, flow, branching
Use
test mode
to simulate progression, run
dry run
for complex paths
4. Pre-launch
Settings, approvals, monitoring
Submit for
approval
, verify schedules and audiences, enable
alerts
**Pro tip:** Start with the [personalization playground](/en/docs/journey-optimizer/using/content-management/personalization/personalize#playground) to test expressions before building content, and always check [conflict detection](/en/docs/journey-optimizer/using/conflict-prioritization/conflicts) before launch to prevent over-messaging.

## Testing in action: Use cases

See how testing concepts apply to real-world scenarios:

**Send multi-channel messages**

Test a journey that combines Read Audience, reaction events, and email/push messages. Validate the entire flow from audience targeting to message delivery. Focus on multi-channel coordination, reaction events, end-to-end flow validation, and testing/publishing steps.

**Send a message to subscribers**

Test journeys that target subscription lists with dynamic email addressing. Validate personalization expressions for correct subscriber targeting. Focus on personalization expressions, dynamic addressing, and subscription list targeting.

**Send time-bound messages**

Test journeys with time-based conditions to ensure messages are sent on specific days. Validate wait activities and scheduling logic. Focus on time-based conditions, wait activities, and scheduling validation.

**Explore more journey use cases**

Access a comprehensive collection of practical examples covering experience events, multi-channel messaging, and external system integrations. Explore various scenarios, advanced patterns, and integration testing approaches.

## Key terminology

Familiarize yourself with these essential testing concepts to better understand Journey Optimizer’s testing and approval capabilities. Each term links to detailed documentation.

**Test profiles** - Synthetic customer profiles (not real customers) used to preview personalized content. Flagged in Real-time Customer Profile Service. Required for test mode and content preview. [Learn how to create test profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles)

**Test mode** - Journey simulation feature that sends test profiles through journey paths. Limitations: Draft journeys only, requires namespace, test profiles only. [See test mode documentation](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey)

**Dry run** - Journey execution analysis tool that traces paths without sending messages or making API calls. Use case: Validate logic without consuming resources. [Learn about dry run](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run)

**Sample input data** - CSV or JSON files containing profile attribute values for testing personalization. Supports up to 30 variants. Alternative to creating test profiles. [How to simulate content variations](/en/docs/journey-optimizer/using/test/preview-test/simulate-sample-input)

**Seed lists** - Email addresses of internal stakeholders automatically included in actual deliveries (not test sends). Email channel only. Use case: Quality monitoring and compliance. [Configure seed lists](/en/docs/journey-optimizer/using/configuration/seed-lists)

**Content experiments** - A/B testing or multi-armed bandit experiments comparing content variations. Campaigns only, not available in journeys. [Get started with experiments](/en/docs/journey-optimizer/using/content-management/content-experiment/get-started-experiment) | [Create experiments](/en/docs/journey-optimizer/using/content-management/content-experiment/content-experiment)

**Proofs** - Test email deliveries sent to specific email addresses using test profile data. Different from seed lists (proofs are manual test sends, seed lists are automatic stakeholder copies). [Send proofs](/en/docs/journey-optimizer/using/test/preview-test/proofs)

**Conflict detection** - Tool that identifies overlapping campaigns and journeys targeting same audiences. Limited journey support: unitary, Audience Qualification, and Read Audience types only. [Learn about conflict management](/en/docs/journey-optimizer/using/conflict-prioritization/gs-conflict-prioritization)

**Approval workflows** - Multi-step review process requiring stakeholder approval before activation. Requires approval policy configuration. [Set up approvals](/en/docs/journey-optimizer/using/test/approve/gs-approval) | [Create policies](/en/docs/journey-optimizer/using/test/approve/approval-policies)

**Rendering tests** - Email display validation across email clients (Gmail, Outlook, Apple Mail) and devices. Requires Litmus integration. [Test email rendering](/en/docs/journey-optimizer/using/test/preview-test/rendering)

**Personalization playground** - Interactive learning environment to experiment with personalization syntax and test expressions with sample data. No live datasets required. [Access the playground](/en/docs/journey-optimizer/using/content-management/personalization/personalize#playground)

## Additional Resources

Essential guides
- Simulate Content Variations - Test up to 30 personalization scenarios using CSV or JSON files. Ideal for multilingual content testing without creating multiple test profiles. Supports email, SMS, push, web, code-based, in-app, and content cards.
- Creating Test Profiles - Create and manage test profiles to simulate customer scenarios. Learn how to flag profiles for testing, set attributes, and organize test segments.
- Email Spam Report - Check spam scores before sending to improve deliverability and inbox placement. Get actionable recommendations for content optimization.
- Journey FAQ - Quick reference for common questions about journey testing, execution, and troubleshooting.

Dependencies & relationships
Understand how testing capabilities connect to each other and to your broader Journey Optimizer workflows. This section maps prerequisites, upstream/downstream dependencies, and common capability combinations.

### Prerequisites (required before testing)

- Test profiles must be created before using test mode or content preview
- Approval policies must be configured before submitting for approval
- Seed lists must be created before adding to campaigns/journeys
- Litmus integration required for email rendering tests
- Journey must be in draft status to use test mode
- Journey must have namespace configured to use test mode

### What testing depends on (upstream)

- Content creation: Need campaigns or journeys to test
- Test profiles: Required for test mode and content preview
- Approval policies: Required for approval workflows
- Configuration: Channel configurations, email authentication, domain settings

### What depends on testing (downstream)

- Campaign/journey activation: Cannot activate without resolving errors
- Publishing: Approval may be required before publishing
- Live monitoring: Post-launch monitoring and reporting
- Optimization: Use test results to refine future campaigns

### Related capabilities

- Testing + Approval workflows - Quality assurance process
- Testing + Conflict detection - Preventing customer over-messaging
- Testing + Content experiments - Performance optimization
- Testing + Reporting - Continuous improvement cycle
- Test profiles + Personalization - Content validation
- Dry run + Test mode - Comprehensive journey validation

### Common capability combinations

- Content testing: Test profiles + Sample input data + Personalization playground
- Email validation: Rendering tests + Spam scores + Test profiles + Proofs
- Journey validation: Test mode + Dry run + Test profiles
- Pre-launch checklist: All technical tests + Conflict detection + Approval workflows

Common questions
### Q: What testing is required before launching a campaign?

**Minimum:** Content preview with test profiles + Spam score check (email)**Recommended:** + Email rendering + Conflict detection + Approval workflow**Best practice:** + Sample input data testing + Seed lists + A/B experiment (if optimizing)

### Q: How do I test personalization without creating many test profiles?

**Primary solution:** Use [sample input data](/en/docs/journey-optimizer/using/test/preview-test/simulate-sample-input) with CSV/JSON files (supports up to 30 variants)**Alternative:** Create 3-5 representative [test profiles](/en/docs/journey-optimizer/using/audiences-profiles-identities/profiles/creating-test-profiles) covering key segments**Learning tool:** Experiment first in [personalization playground](/en/docs/journey-optimizer/using/content-management/personalization/personalize#playground)

### Q: What’s the difference between test mode and dry run for journeys?

**Test mode:** Sends test profiles through journey, triggers actual actions, generates test messages. Requires draft journey + namespace.**Dry run:** Traces execution paths without sending anything. Works on any journey status. No messages sent, no actions executed.**Use together:** Test mode for message testing + Dry run for logic validation - comprehensive coverage.

### Q: Can I test journeys in production/live status?

**Test mode:** No - draft journeys only**Dry run:** Yes - works on any journey status**Content preview:** Yes - preview individual messages anytime**Workaround:** Duplicate live journey to draft for full test mode validation

### Q: Which testing capabilities require external integrations?

**Email rendering:** Requires Litmus integration (separate license)**All others:** Built-in to Journey Optimizer, no additional integrations required**Note:** Test profiles require Real-time Customer Profile Service (included)

### Q: How do I test API-triggered campaigns?

**Option 1:** Use [Campaign Simulation API](https://developer.adobe.com/journey-optimizer-apis/references/simulations){target-“_blank”} for programmatic testing**Option 2:** Preview content with test profiles in UI**Option 3:** Send proofs to test email addresses**Best practice:** Combine all three for comprehensive validation

recommendation-more-help
