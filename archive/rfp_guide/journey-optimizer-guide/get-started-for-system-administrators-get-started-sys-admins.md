---
title: "Get started for system administrators get-started-sys-admins"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/get-started/by-role/administrator"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:16.344660+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started for system administrators get-started-sys-admins

Last update: May 8, 2026
- Topics:
- [Get Started](#)

CREATED FOR:

- Intermediate
- Admin

As a **System Administrator**, you set up the Journey Optimizer environment and manage access to enable your teams to work efficiently and securely. You perform essential configuration steps so that the [Data Engineer](/en/docs/journey-optimizer/using/get-started/by-role/data-engineer), [Developer](/en/docs/journey-optimizer/using/get-started/by-role/developer), and [Marketer](/en/docs/journey-optimizer/using/get-started/by-role/marketer) can start working with Adobe Journey Optimizer.

Your primary responsibilities include setting up user groups and permissions, creating and managing sandboxes for partitioning data and journeys for different user groups, and configuring delivery channels and message presets to ensure consistent branding across the various messages and assets delivered through Journey Optimizer. You ensure the right people have access to the right capabilities while maintaining security and governance.

These capabilities can be managed by **Product administrators** that have access to the Permissions product. [Learn more about Permissions](/en/docs/journey-optimizer/using/access-control/permissions#_blank).

## Set up access and permissions

Follow these steps to configure access management:

- Create sandboxes to partition your instances into separate, isolated virtual environments. Sandboxes are created in Journey Optimizer. Learn more in the Sandboxes section. note NOTE As a System Administrator , if you cannot see the Sandboxes menu in Journey Optimizer, you need to update your permissions. Learn how to update your role on this page .
- Understand roles . Roles are a set of unitary rights which allows users access to certain functionalities or objects in the interface. Learn more in the out-of-the-box roles section.
- Set permissions for roles, including Sandboxes , and give access to your team members by assigning them to different roles. Permissions are unitary rights that allow you to define the authorizations assigned to Role . Each permission is gathered under capabilities, e.g. Journey or Offers, which represents the different functionalities or objects in Journey Optimizer. Learn more in the Permission levels section.
- Use object-level access control (optional). Apply access labels to objects like journeys, campaigns, and channel configurations to control which users can access specific resources. Learn more about Object-level access control (OLAC) .

In addition, you must add users who need access to Assets Essentials to the **Assets Essentials Consumer Users** or/and **Assets Essentials Users** roles. [Read more in Assets Essentials documentation](/en/docs/experience-manager-assets-essentials/help/get-started-admins/deploy-administer#_blank).

When accessing Journey Optimizer for the first time, you are provisioned a production sandbox and allocated a certain number of IPs depending on your contract.

## Configure channels and messages

To enable [Marketers](/en/docs/journey-optimizer/using/get-started/by-role/marketer) to create and send messages, access the **ADMINISTRATION** menu. Browse the **Channels** menu to configure channel settings.

NOTE
As a
System Administrator
, if you cannot see the
Channels
menu in Journey Optimizer, update your permissions in the
Permissions
product.
Follow these steps:

- Set up channel configurations . Define all the technical parameters required for email, SMS, push notifications, web push, direct mail, and other channels: Define push notification settings in both Adobe Experience Platform and Adobe Experience Platform Data Collection. Learn more Configure web push notifications to deliver notifications to mobile and desktop browsers. Learn more Create channel configurations to configure all the technical parameters required for email, SMS, push, in-app, web, and other channels. Learn more Configure the SMS channel to set up all the technical parameters required for SMS. Learn more Manage the number of days during which retries are performed before sending email addresses to the suppression list. Learn more Enable message export at the channel configuration level to archive sent email and SMS content when required (add-on offering). Learn more
- Delegate subdomains : for any new subdomain to be used in Journey Optimizer, the first step will be to delegate it. Learn more . You can migrate subdomains from CNAME to custom delegation when needed. Learn more
- Create IP pools : improve your email deliverability and reputation by grouping together IP addresses provisioned with your instance. Learn more
- Manage the suppression and allowed lists : improve your deliverability with suppression and allowed lists A suppression list consists of email addresses that you want to exclude from your deliveries, because sending to these contacts could hurt your sending reputation and delivery rates. You can monitor all the email addresses that are automatically excluded from sending in a journey, such as invalid addresses, addresses that consistently soft-bounce, and could adversely affect your email reputation, and recipients who issue a spam complaint of some kind against one of your email messages. Learn how to manage the suppression list and retries . The allowed list enables you to specify individual email addresses or domains that will be the only recipients or domains authorized to receive the emails you are sending from a specific sandbox. This can prevent you from sending emails accidentally to real customer addresses when you are in a testing environment. Learn how to enable the allowed list . Learn more about deliverability management in Adobe Journey Optimizer on this page .

## Additional capabilities

As your organization’s needs grow, consider these advanced capabilities:

- Consent policies : If your organization has purchased Healthcare Shield or Privacy and Security Shield, create consent policies to respect customer preferences across channels. Learn more
- Data governance policies : Apply data usage labels and policies to control how data is used in marketing actions. Learn more
- IP warmup plans : Gradually increase email sending volumes to build sender reputation with email providers. Learn more
- Quiet hours : Configure rule sets for time-based exclusions when messages should not be sent during specific periods. Learn more

## Collaborate across roles

Your administrative work enables all teams to succeed:

Support Data Engineers
Collaborate with [Data Engineers](/en/docs/journey-optimizer/using/get-started/by-role/data-engineer) on data management and access. Review the [Get started with data management](/en/docs/journey-optimizer/using/data-management/gs-data) overview to understand the schemas, datasets, and data sources your data engineers need to configure.

- Grant permissions for data management and schema creation
- Approve sandbox access for development and testing
- Coordinate on data retention policies and governance rules
- Enable access to advanced features like Federated Audience Composition

Enable Developers
Collaborate with [Developers](/en/docs/journey-optimizer/using/get-started/by-role/developer) on API access and testing:

- Provide API credentials through Adobe Developer Console
- Set up sandbox environments for development and testing
- Approve channel configurations (push certificates, SMS providers)
- Coordinate on testing environments and deployment strategy

Empower Marketers
Collaborate with [Marketers](/en/docs/journey-optimizer/using/get-started/by-role/marketer) on permissions and channel setup:

- Assign appropriate permissions to create journeys and campaigns
- Configure channels they’ll use (email, push, SMS, etc.)
- Support testing environments and approval workflows
- Enable access to new features and capabilities

## Next steps

Once the environment is configured:

- **Verify setup**: Confirm that all team members can access their required features
- **Monitor usage**: Use the administration dashboards to track system usage and identify issues
- **Maintain permissions**: Regularly review and update permissions as team roles evolve

recommendation-more-help
