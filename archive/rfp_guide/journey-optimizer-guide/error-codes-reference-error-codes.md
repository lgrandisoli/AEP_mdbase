---
title: "Error codes reference error-codes"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/monitor/monitor-alerts-errors/error-codes-reference"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:34:14.333649+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Error codes reference error-codes

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Monitoring](#)

CREATED FOR:

- Intermediate
- User

Adobe Journey Optimizer uses standardized error codes to help you quickly identify and resolve issues across journeys, campaigns, and message configurations. Understanding these error codes can significantly reduce troubleshooting time and help you maintain optimal campaign performance.

## Understanding error code structure error-code-structure

Adobe Journey Optimizer error codes follow a consistent naming pattern that helps identify the component and issue type:

- **Service prefix**: Indicates which Adobe Journey Optimizer service generated the error.Examples: CJMPTS (Push/Transport Service), CJMRT (Journey Runtime), CJMMAS (Message Authoring Service), CJMCMP (Campaign), CJMTL (Transport Layer), CJMRPS (Reporting/Provisioning Service)
- **Error number**: Unique identifier for the specific error condition
- **HTTP status code**: Standard HTTP status code (e.g., 400, 403, 422, 500)

Example: CJMRT-030012-422 indicates a Journey Runtime error (CJMRT) with error number 030012 and HTTP status 422 (Unprocessable Entity).

## Where to find error codes find-error-codes

Error codes appear in several locations within Adobe Journey Optimizer:

- Journey execution reports and logs
- Campaign activation screens
- Message validation warnings
- System notifications and alerts
- API responses (when using REST APIs)

When an error occurs, note the complete error code and any accompanying request ID, as these are essential for troubleshooting and support escalation.

## Common error codes by service error-codes-by-service

Use this section to find error codes grouped by service.

### CJMPTS: Push and transport service errors cjmpts-errors

These errors occur during push notification delivery and message transport operations.

Error Code
Description
Root Cause
Resolution
CJMPTS-1410-500
Internal server error on push/channel send action
Channel backend outage, expired credentials, misconfiguration, or provider bug
1. Retry after delay
2. Check provider configurations and quotas
3. Verify push credentials are valid
4. Test with an alternate channel
5. If persistent, contact Adobe Support with request ID
Related documentation
:
Push configuration
CJMPTS-1006-404
Push/SMS fails with “resource not found”
Referenced provider/channel does not exist, is misspelled, or was deprovisioned
1. Review and correct provider/channel references and IDs
2. Audit sandbox/organization configuration
3. Verify channel configurations are active
4. Re-create channel configuration if necessary
Related documentation
:
Channel surfaces
CJMPTS-1510-500
Internal server error on push-channel send
Backend push/transport malfunction; provider or infrastructure error
1. Check channel provisioning settings
2. Verify push credentials are valid
3. Retry the operation
4. If persistent, contact Adobe Support with request ID
Related documentation
:
Push configuration
CJMPTS-1023-500
Internal server error during push send/process (third-party gateways)
Temporary cloud malfunction or unknown service error
1. Verify provider/channel configuration
2. Check third-party gateway status
3. Retry after a few minutes
4. Review logs for additional context
Related documentation
:
Push notifications
CJMPTS-1310-500
Internal error from Render Service (preview or live send)
Downstream template renderer failed, usually due to JSON/template syntax issues
1. Validate template syntax and structure
2. Check all personalization variables are valid
3. Use a test payload to identify the issue
4. Simplify template complexity if needed
Related documentation
:
Message templates
,
Personalization syntax
### CJMRT: Journey Runtime and API errors cjmrt-errors

These errors occur during journey execution, event processing, and API operations.

Error Code
Description
Root Cause
Resolution
CJMRT-110001-500
Maximum runs exceeded for workflow step (e.g., IP Affinity Provisioning step times out)
Workflow/provisioning job did not complete within retries/time allowed, often due to infrastructure/service lag or temporary backend issue
1. Retry after some time
2. Check
Adobe Status
for outages
3. Escalate to Adobe Support with workflow/job/org details
4. Provide logs and network captures if available
Related documentation
:
Journey troubleshooting
CJMRT-000071-400
Bad request during journey/test event or API call
Payload/parameters are malformed or missing; input references a non-existent or inactive resource
1. Review the request body for error details
2. Correct reference/parameter
3. Remove advanced configuration and retry
4. Add features back one by one to identify the issue
Related documentation
:
Journey troubleshooting
,
Events configuration
CJMRT-000013-401
Unauthorized error during message runtime operation/API event
Authentication failure: token is expired, permissions are missing, or the integration/user has lost environment access
1. Verify permissions and roles
2. Refresh authentication token
3. Use a known-valid user/service account
4. Review product profile assignments
Related documentation
:
Permissions
CJMRT-080605-400
Bad request from journey runtime (e.g., node trigger, action, etc.)
Configuration references a removed/renamed or out-of-date feature/template/channel
1. Validate all resource references
2. Audit journey configuration and feature flags
3. Update broken references
4. Review recent system updates and migrations
Related documentation
:
Journey creation
CJMRT-030012-422
Unprocessable entity - failed action, invalid event, or bad payload
Invalid input data (e.g., nonexistent audience, event, or attribute)
1. Double-check input/event payload structure
2. Verify referenced objects (audiences, datasets) exist and are active
3. Validate all required fields are present
4. Test with a known-good payload
Related documentation
:
Journey troubleshooting
,
Events configuration
CJMRT-130004-400
Bad request - malformed input in journey node or channel config
Journey payload or configuration references removed/invalid resource
1. Review journey node configuration
2. Verify all referenced resources (messages, audiences, actions) exist
3. Fix or update broken references
4. Rebuild journey configuration if necessary
Related documentation
:
Journey creation
,
Custom actions
CJMRT-000032-409
Conflict - resource already exists
Attempt to create resource with duplicate ID or name
1. Use unique IDs and names for all resources
2. Check for existing resources with same identifier
3. Delete or rename conflicting objects
4. Review naming conventions
Related documentation
:
Journey creation
CJMRT-170016-400
Bad request during journey config/preview
Payload missing required dependency or broken template link
1. Validate all required resources are active
2. Ensure templates and content blocks are published
3. Check all dependencies are properly linked
4. Review journey test mode results
Related documentation
:
Testing journeys
,
Journey dependencies
CJMRT-080608-400
Bad request in domain/channel/delegation
Required DNS records or email/SMS configuration missing
1. Complete DNS configuration for email domains
2. Verify subdomain delegation is complete
3. Run configuration wizards again
4. Allow time for DNS propagation (up to 72 hours)
Related documentation
:
Channel surfaces
,
Subdomain delegation
CJMRT-110100-500
Internal error on payload
Backend data/config bug or unsupported configuration
1. Retry the operation
2. Simplify configuration if using advanced features
3. Escalate to Adobe Support with request ID and exact payload
4. Check for known issues in release notes
Related documentation
:
Journey troubleshooting
### CJMMAS: message authoring service errors cjmmas-errors

These errors occur when creating, editing, or publishing messages, presets, and content.

Error Code
Description
Root Cause
Resolution
CJMMAS-1732-500
Proof has failed - All assets not published when sending proof/test with AEM asset
Recently published asset isn’t in AJO yet; asset ID mismatch; cross-repo use; AEM sync lag
1. Use only published asset IDs from the correct repository/environment
2. Allow time for sync between AEM and AJO
3. Retry with a known-good asset
4. Verify asset publishing status in AEM
Related documentation
:
Assets integration
CJMMAS-1069-500
Internal error saving or publishing message template
Backend exception (infrastructure/service bug or content issue); unsupported markup/feature
1. Simplify or reduce the template complexity
2. Re-add content in incremental steps to identify the issue
3. Check the
Adobe Status page
4. Remove unsupported features or markup
Related documentation
:
Content templates
CJMMAS-1149-400
Bad request when saving message, preset, or variant
Required fields missing in message or bad configuration
1. Complete all required fields (marked with asterisk)
2. Validate message/preset configuration
3. Check field value formats and constraints
4. Review validation messages in UI
Related documentation
:
Email channel
,
Channel surfaces
CJMMAS-2073-422
Unprocessable entity in message preset edit
Validation error, unsupported field, or improper syntax
1. Correct syntax/field errors as indicated
2. Compare to a known-good configuration
3. Use message UI validation before saving
4. Review field requirements in documentation
Related documentation
:
Message presets
,
Email settings
CJMMAS-1300-500
Internal error from message authoring
Backend crash due to infrastructure issue, large content, or service downtime
1. Simplify template/content (reduce size/complexity)
2. Retry the operation
3. Save work incrementally
4. If persistent, escalate to Adobe Support
Related documentation
:
Content templates
CJMMAS-2001-200
Success status but error banner: opt-out link missing
Required unsubscribe link missing in email variant
1. Add opt-out/unsubscribe link to all email variants
2. Ensure link is present in every language version
3. Use personalization helper to insert opt-out link
4. Test all variants before publishing
Related documentation
:
Opt-out management
,
Email design
CJMMAS-1603-403
Forbidden when updating/publishing template or preset
User lacks required permission/role, or action not allowed in current state
1. Verify user has appropriate permissions (Message Manager, Author, etc.)
2. Check preset/template status (draft, published, archived)
3. Request access from administrator if needed
4. Review product profile assignments
Related documentation
:
Permissions
,
Access control
### CJMCMP: Campaign errors cjmcmp-errors

These errors occur during campaign creation, configuration, and activation.

Error Code
Description
Root Cause
Resolution
CJMCMP-6003-400
“There is at least one incorrect campaign” when publishing/test mode journey/message
Node references a missing, unpublished, or invalid campaign; legacy or cloned journey not creating inlines
1. Open each message node and verify configuration
2. Re-link or re-add message nodes
3. Activate test mode to force creation of inline campaigns
4. Move to the new journey wizard if issue is frequent
Related documentation
:
Journey creation
,
Testing journeys
CJMCMP-2003-400
UI banner: “The experiment is incorrect” in Email Designer
Stale or missing experiment/data provider; failed experiment cleanup, schema mismatch, or UI validation bug
1. Remove unused experiment fields
2. Validate schema and data provider connections
3. Reload UI and clear browser cache
4. Recreate node/email if issue unresolved
Related documentation
:
Content experiments
CJMCMP-3001-400
Simulation/preview “incorrect surface type filter”
Node built using legacy structure sends type=surfaceId, backend expects brandingPresetId
1. Delete and recreate the affected node
2. Use the new journey version/template
3. Use test mode to clear configuration
4. Bulk recreate nodes if issue is widespread
Related documentation
:
Channel surfaces
,
Message simulation
CJMCMP-2050-400
Bad request in campaign activation or approval
Campaign references invalid/missing policy or segment
1. Audit all campaign node configurations
2. Verify policy/segment links are current and valid
3. Update with correct configuration
4. Re-test campaign before activation
Related documentation
:
Campaign creation
,
Campaign approval
### CJMTL: transport layer errors cjmtl-errors

These errors occur during message transport and delivery operations.

Error Code
Description
Root Cause
Resolution
CJMTL-010018-422
“Personalization not allowed in domain name” when saving/sending content
Overly strict validation temporarily broke dynamic href domain personalization
1. Refactor links if using domain variables
2. Verify the latest AJO version is in use
3. Retry the operation
4. Use static domains if issue persists
Related documentation
:
Personalization syntax
,
Email design
CJMTL-010011-422
Unprocessable entity - Push/SMS/Email send fails, says “invalid field”
Payload or recipient/contact data missing or invalid
1. Inspect logs for specific field errors
2. Fix profile/contact information
3. Validate with test profile
4. Refactor payload format as needed
Related documentation
:
Profile management
,
Test profiles
### CJMRPS: reporting and provisioning service errors cjmrps-errors

These errors occur during reporting configuration and dataset provisioning operations.

Error Code
Description
Root Cause
Resolution
CJMRPS-1047-409
“Conflict. Dataset has been added already” when adding reporting dataset
Attempting to add a dataset which is already provisioned
1. Review dataset configuration in reporting settings
2. Do not re-add datasets already present
3. Use official migration checklists for reporting migration
4. Remove duplicate dataset references
Related documentation
:
Reporting overview
,
Campaign reports
,
Journey reports
## General troubleshooting approach troubleshooting-approach

When encountering an error code, follow this systematic approach:

- Identify the error : Note the complete error code, HTTP status, and any accompanying message or request ID.
- Find the service : Use the service prefix (CJMPTS, CJMRT, CJMMAS, CJMCMP, CJMTL, CJMRPS) to identify which component is affected.
- Check the status code : 400 (Bad Request) : Review input data and configuration 403 (Forbidden) : Check permissions and access rights 409 (Conflict) : Look for duplicate or conflicting resources 422 (Unprocessable Entity) : Validate data against schema requirements 500 (Internal Server Error) : Retry and potentially escalate to support
- Review recent changes : Consider what was modified recently (journey updates, new campaigns, configuration changes, etc.).
- Consult documentation : Use the links provided in this guide to access detailed documentation for the affected feature.
- Retry when appropriate : For 500-series errors, a simple retry after a few minutes often resolves transient issues.
- Escalate when needed : If the error persists after following resolution steps, contact Adobe Support with the complete error code, request ID (if available), steps to reproduce, and relevant configuration details.

## Best practices to avoid common errors best-practices

Use these practices to reduce avoidable errors and improve reliability.

### Before journey activation journey-best-practices

- **Validate all resources**: Ensure all referenced audiences, events, data sources, and custom actions are properly configured
- **Test thoroughly**: Use test mode to identify issues before publishing ([Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/testing-the-journey))
- **Validate volumes**: Use dry run to validate audience reach and branch logic before going live ([Learn more](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-dry-run))
- **Check permissions**: Verify you have necessary access rights for all components
- **Review dependencies**: Ensure all linked messages and content are published

### When creating messages message-best-practices

- **Complete required fields**: Always fill in all mandatory fields before saving
- **Include opt-out links**: Add unsubscribe links to all email variants ([Learn more](/en/docs/journey-optimizer/using/privacy/consent/opt-out))
- **Validate personalization**: Test all dynamic content with sample profiles ([Learn more](/en/docs/journey-optimizer/using/content-management/personalization/personalization-build-expressions))
- **Keep templates manageable**: Avoid overly complex templates that may cause rendering issues

### For campaign management campaign-best-practices

- **Verify audience data**: Ensure target audiences are properly configured and populated
- **Check approval status**: Understand approval requirements before attempting to activate ([Learn more](/en/docs/journey-optimizer/using/test/approve/gs-approval))
- **Monitor configurations**: Regularly review channel surfaces and presets for validity
- **Plan DNS changes**: Allow sufficient time for DNS propagation when updating domains

## Additional resources additional-resources

- [Journey troubleshooting](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting)
- [Execution troubleshooting](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-execution)
- [Inbound activities troubleshooting](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting-inbound)
- [Custom actions troubleshooting](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshoot-custom-action)
- [Journey FAQs](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-faq)
- [Guardrails and limitations](/en/docs/journey-optimizer/using/get-started/essentials/guardrails)

## Getting support getting-support

If you encounter persistent errors that cannot be resolved using this guide:

- **Gather information**: Collect the error code, request ID, timestamps, and steps to reproduce
- **Check system status**: Visit [Adobe Status](https://status.adobe.com/#_blank) for known service issues
- **Search documentation**: Review [Adobe Experience League](/en/docs/journey-optimizer#_blank) for solutions
- **Engage community**: Post questions in the [Adobe Journey Optimizer Community](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer/ct-p/journey-optimizer#_blank)
- **Contact Adobe Support**: [Submit a support ticket](/en/docs/journey-optimizer/using/get-started/work-efficiently/user-interface#support-ticket-guidelines) with all relevant details

NOTE
This error code reference is continuously updated as new codes are identified and documented. For the most current information, check the
Adobe Journey Optimizer Community blogs
regularly.
**Related topics**

- [Demystifying Adobe Journey Optimizer Error Codes: Part 1](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/demystifying-adobe-journey-optimizer-error-codes-root-causes-and/ba-p/760884#_blank)
- [Demystifying Adobe Journey Optimizer Error Codes: Part 2](https://experienceleaguecommunities.adobe.com/t5/journey-optimizer-blogs/demystifying-adobe-journey-optimizer-error-codes-root-causes-and/bc-p/782661#_blank)

recommendation-more-help
