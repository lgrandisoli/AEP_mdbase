---
title: "Subdomain delegation in Journey Optimizer subdomain-delegation"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configuration/delegate-subdomains/about-subdomain-delegation"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:16.182119+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Subdomain delegation in Journey Optimizer subdomain-delegation

Last update: May 8, 2026
- Topics:
- [Subdomains](#)

CREATED FOR:

- Experienced
- Admin

Creating a subdomain for your email journeys andcampaigns allows brands to isolate varying types of traffic (marketing vs. corporate for example) into specific IP pools and with specific domains, which will speed up the IP warming process and improve deliverability overall.

If you share a domain and it gets blocked or added to the deny list, it could impact your corporate mail delivery. However, reputation issues or blocks on a domain specific to your email marketing communications will impact just that flow of email. Using your main domain as the sender or ‘From’ address for multiple mail streams could also break email authentication, causing your messages to be blocked or placed in the spam folder.

CAUTION
You cannot use the same sending domain to send out messages from Adobe Journey Optimizer and from another product, such as Adobe Campaign or Adobe Marketo Engage.
## Why setting up subdomains? why-set-up-subdomains

A subdomain is a division of your domain that can be used to isolate your brands, or various types of traffic - for example transactional messages and marketing communications.

Let’s take the example of the “mybrand.com” domain, that is used to send both transactional and marketing communications. In this situation, you can decide to set up two subdomains:

- “info.mybrand.com” subdomain for your transactional communications (purchases confirmation, password reset, etc.),
- “marketing.mybrand.com” subdomain for your prospecting emailings.

By doing so, you will help preserve the reputation of your domain and other subdomains. For example, if the “marketing.mybrand.com” subdomains ended up being added to the block list by Internet Service Providers due to bad deliverability, this would prevent the whole “mybrand.com” domain and the “info.mybrand.com” subdomain from being added to the block list.

When implementing a solution, there are requirements for externally-facing components: these include setting up links and web pages to be tracked, displaying mirror pages, etc.

While these requirements are being managed through components hosted by both Adobe and the customer, they include URLs which can be seen by the recipients of the emails. To avoid having URLs which indicate the underlying technical solution or hosting provider, subdomains can be set up to make this transparent to the recipients of the emails.

**Learn more**

- Learn how to [delegate your subdomains](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomain) directly from the interface
- Learn how to [add Google TXT records](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/google-txt) to your subdomains to ensure the successful delivery of emails to Gmail addresses
- Learn how to [access the PTR records](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/ptr-records) generated for your subdomains, allowing them to be verified by sending mail servers

## Subdomain configuration methods subdomain-delegation-methods

Subdomain configuration allows you to configure a subsection of your domain (technically a “DNS zone”) for use with Adobe Journey Optimizer.

The available setup methods are as follows.

### Fully delegate a subdomain to Adobe (recommended) full-subdomain-delegation

Journey Optimizer allows you to fully delegate your subdomains to Adobe directly from the product interface. By doing so, Adobe will be able to deliver messages as a managed service by controlling and maintaining all aspects of DNS that are required for delivering, rendering and tracking.

You can rely on Adobe to maintain the DNS infrastructure required to meet industry-standard deliverability requirements for your email marketing sending domains, while continuing to maintain and control DNS for your internal email domains.

IMPORTANT
The full subdomain delegation is the preferred method.
Learn how to fully delegate a subdomain to Adobe in [this section](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomain#set-up-subdomain).

### Set up a subdomain with CNAMEs cname-subdomain-setup

If you have domain-specific restriction policies and you want Adobe to have only partial control over DNS, you can choose to carry out all DNS-related activities on your side.

CNAME subdomain set up enables you to create a subdomain and use CNAMEs to point to Adobe-specific records. Using this configuration, both you and Adobe share responsibility for maintaining DNS in order to setup environment for sending, rendering and tracking emails.

CAUTION
The CNAME method is recommended if your organization’s policies restrict the full subdomain delegation method. This approach requires you to maintain and manage DNS records on your own.
Adobe will not be able to assist in changing, maintaining or managing DNS for a subdomain configured through the CNAME method.
Learn how to create a subdomain using CNAMEs to point to Adobe-specific records in [this section](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-subdomain#cname-subdomain-setup).

### Use a custom subdomain custom-subdomain-delegation

The custom delegation method enables you to fully own controlling and maintaining all aspects of DNS that are required for delivering, rendering and tracking messages.

In this case, you completely own and manage our own subdomains and have full control over the certificates which are generated as part of this process.

Learn how to [set up a custom subdomain](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/delegate-custom-subdomain). If your subdomain currently uses CNAME, you can also [migrate from CNAME to custom delegation](/en/docs/journey-optimizer/using/configuration/delegate-subdomains/custom-subdomain-migration).

## Comparing the configuration methods

The table below provides a summary of how these methods work, as well as the implied level of effort:

Configuration method
How it works
Level of effort
Full delegation
Create the subdomain and namespace record. Adobe will then configure all DNS records required for Adobe Journey Optimizer.
In this setup, Adobe is fully responsible for managing the subdomain and all the DNS records.
Low
CNAME method
Create the subdomain and namespace record. Adobe will then provide the records to be placed in your DNS servers and will configure the corresponding values in Adobe Journey Optimizer DNS servers.
In this setup, both you and Adobe share responsibility for maintaining DNS.
High
Custom delegation method
Create the subdomain and namespace record - Adobe will then provide the records to be placed in your DNS servers. Upload the SSL Certificate obtained from the Certificate Authority and complete the Feedback Loop steps by verifying domain ownership and reporting email address.
In this setup, you have full responsibility for maintaining DNS.
Very high
Additional information on domain configuration is available in [this documentation](/en/docs/deliverability-learn/deliverability-best-practice-guide/additional-resources/campaign/ac-domain-name-setup#_blank).

If you have any question regarding subdomain configuration methods, reach out to Adobe, or contact Customer Care to request Deliverability consulting.

recommendation-more-help
