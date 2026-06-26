---
title: "Delegate email subdomains section-overview"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomains-landing-page"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:23.044168+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Delegate email subdomains section-overview

Last update: May 8, 2026
Delegating email subdomains is a core step in [channel configuration](/en/docs/journey-optimizer/using/configuration/get-started-configuration)—required before you can send emails from Journey Optimizer. Subdomains let you isolate traffic types (e.g., marketing vs. transactional), protect your main domain’s reputation, and speed up [IP warmup](/en/docs/journey-optimizer/using/configuration/implement-ip-warmup-plan/ip-warmup-gs). They work alongside [email channel configuration](/en/docs/journey-optimizer/using/channels/email/configure-email/get-started-email-config) and [deliverability monitoring](/en/docs/journey-optimizer/using/monitor/deliverability/deliverability) to ensure messages reach inboxes.

You can choose from several setup methods: **full delegation** (Adobe manages DNS), **CNAME setup**, or **custom delegation** (you own certificates and DNS). If you start with CNAME, you can later [migrate to custom delegation](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/custom-subdomain-migration) for stricter security. This section also covers DMARC and PTR records, Google TXT records for Gmail, and IP pools. For broader deliverability guidance, see [Get started with deliverability](/en/docs/journey-optimizer/using/monitor/deliverability/deliverability) and [Monitor email addresses](/en/docs/journey-optimizer/using/configuration/monitor-reputation/monitor-reputation-landing-page).

## Delegate Email Subdomains

Get Started with Subdomain Delegation

Learn the benefits, configuration methods, and considerations for delegating subdomains in Adobe Journey Optimizer.

[Start Delegating Subdomains](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/about-subdomain-delegation)

Delegate a Subdomain

Step-by-step guidance for delegating subdomains to Adobe, including full delegation and CNAME setup.

[Learn How to Delegate](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomain)

Set Up a Custom Subdomain

Take full ownership of your subdomains with custom delegation—upload your own SSL certificates and maintain full control over domain configuration.

[Set up a custom subdomain](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-custom-subdomain)

Migrate from CNAME to Custom Delegation

Migrate existing CNAME-configured subdomains to custom delegation to meet security policies and gain full control over certificates.

[Migrate your subdomain](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/custom-subdomain-migration)

Set Up DMARC Records

Configure DMARC records to enhance email security and deliverability for delegated subdomains.

[Set Up DMARC Now](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/dmarc-record)

Add a Google TXT Record

Verify subdomains for Gmail deliverability by adding Google TXT records in Adobe Journey Optimizer.

[Add Google TXT Records](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/google-txt)

Access & Edit PTR Records

Manage PTR records for delegated subdomains, including editing and understanding update statuses.

[Edit PTR Records](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/ptr-records)

Create IP Pools

Group IP addresses for improved email deliverability and manage subdomain reputation effectively.

[Create IP Pools](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/ip-pools)

## Additional resources

- **Configure landing page subdomains** - Set up subdomains for landing pages and subscription forms.
- **Configure web subdomains** - Delegate subdomains for web experiences and tracking.
- **Get started with channels configuration** - Overview of all channel setup steps, including subdomain delegation.

recommendation-more-help
