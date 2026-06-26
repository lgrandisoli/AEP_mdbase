---
title: "Get started for developers get-started-developers"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/get-started/by-role/developer"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:16.900930+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Get started for developers get-started-developers

Last update: May 8, 2026
- Topics:
- [Get Started](#)

CREATED FOR:

- Experienced
- Developer

As a **Developer**, you are responsible for implementing and integrating Adobe Journey Optimizer into your applications and systems. You can start working with Adobe Journey Optimizer once the [System Administrator](/en/docs/journey-optimizer/using/get-started/by-role/administrator) and the [Data Engineer](/en/docs/journey-optimizer/using/get-started/by-role/data-engineer) have granted you access and prepared your environment.

## Your role in the Journey Optimizer ecosystem

While other team members configure Journey Optimizer through the user interface, you’ll focus on:

- **Implementing SDKs** in mobile and web applications
- **Sending events** from your applications to trigger journeys
- **Building API endpoints** that Journey Optimizer can call via custom actions
- **Integrating** Journey Optimizer with your existing systems and infrastructure
- **Testing and debugging** your implementations

Your [Data Engineer](/en/docs/journey-optimizer/using/get-started/by-role/data-engineer) will handle data schemas, event configurations, and data sources. Your [Administrator](/en/docs/journey-optimizer/using/get-started/by-role/administrator) will set up permissions and channel configurations. [Marketers](/en/docs/journey-optimizer/using/get-started/by-role/marketer) will design the journeys and content that use your implementations.

This guide covers the essential technical implementation steps to get you started with Journey Optimizer. Whether you’re building mobile apps, web experiences, or API integrations, follow the sections below to set up your implementation.

## Prerequisites prerequisites

Before starting your implementation, ensure you have:

Category
Requirements
Technical skills
* Experience with JavaScript (for Web SDK) or Swift/Kotlin (for Mobile SDK)
* Understanding of RESTful APIs and JSON
* Familiarity with asynchronous programming and event-driven architectures
* Knowledge of your organization’s application architecture
Access and tools
* Access to
Adobe Developer Console
for API credentials
* Development environment with access to your application’s codebase
* Testing tools like Postman for API testing
* Browser developer tools or mobile debugging tools
From other team members
* Environment access granted by your
Administrator
* XDM schemas and event definitions from your
Data Engineer
* Requirements and use cases from your
Marketers
## Understand the technical foundation technical-foundation

Before diving into implementation, familiarize yourself with the core technical concepts:

- Adobe Experience Platform integration : Journey Optimizer is built natively on Adobe Experience Platform. Understanding the underlying architecture will help you build more effective implementations. Learn more about how Journey Optimizer works .
- XDM data models : Journey Optimizer uses Experience Data Model (XDM) to structure event and profile data. As a developer, you’ll need to understand how to send data that conforms to the schemas configured by your Data Engineer . Learn about XDM schemas .
- Authentication and security : All implementations require proper authentication. Understand how to set up authentication for SDKs and APIs. Learn about API authentication .

## Set up mobile app integrations mobile-integration

### Configure the Adobe Experience Platform Mobile SDK

To enable push notifications, in-app messages, and other mobile capabilities, integrate the Adobe Experience Platform Mobile SDK into your mobile applications.

- Install and configure the Mobile SDK : Follow the Adobe Experience Platform Mobile SDK documentation to get started with SDK integration.
- Create a mobile property : Set up a mobile property in Adobe Experience Platform Data Collection. Learn how to create and configure a mobile property .
- Configure push notifications : For iOS apps : Register your app with APNs (Apple Push Notification service). Learn more in Apple’s documentation . For Android apps : Set up Firebase Cloud Messaging for your Android app. Learn more in Google’s documentation .
- Test your mobile integration : Use the mobile onboarding quick start workflow to rapidly configure and test your mobile setup.

Detailed steps to configure push notifications are available on [this page](/en/docs/journey-optimizer/using/channels/push/push-config/push-configuration).

### Implement code-based experiences (Mobile SDK)

For native mobile app personalization using code-based experiences:

- Follow [this tutorial](https://developer.adobe.com/client-sdks/edge/adobe-journey-optimizer/code-based/tutorial#_blank) for Mobile SDK implementation
- Review sample implementations for [iOS](https://github.com/adobe/aepsdk-messaging-ios/tree/main/TestApps/MessagingDemoAppSwiftUI#_blank) and [Android](https://github.com/adobe/aepsdk-messaging-android/tree/main/code/testapp#_blank)

## Implement web experiences web-implementation

### Set up the Adobe Experience Platform Web SDK

For web-based implementations, the Web SDK is your primary integration point:

- Install the Web SDK : Follow the Web SDK implementation guide to set up the SDK on your website.
- Configure datastreams : Create and configure a datastream in Adobe Experience Platform Data Collection with Journey Optimizer enabled. Learn more in the datastreams documentation .
- Enable web push notifications (optional): Web push notifications are now generally available. Configure the pushNotifications property in your Web SDK configuration and use the sendPushSubscription command to register push subscriptions. Learn about web push configuration .

### Implement code-based experiences (Web SDK)

Code-based experiences allow you to personalize any digital touchpoint:

- Choose your implementation method : Client-side, server-side, or hybrid. Review implementation samples for each approach.
- Define surfaces : Identify the locations in your application where you want to deliver personalized content. Learn about surface configuration .
- Implement content rendering : Use the Web SDK to fetch and apply personalization content. See code-based implementation tutorials .
- Send display and interaction events : Track when content is displayed and when users interact with it for analytics and optimization.

Explore [sample implementations on GitHub](https://github.com/adobe/alloy-samples/tree/main/ajo#_blank) to see code-based experiences in action.

Learn more about [getting started with code-based experiences](/en/docs/journey-optimizer/using/channels/code-based-experience/get-started-code-based).

## Implement event streaming event-streaming

### Send events to trigger journeys

As a developer, you’ll implement the code to send events that trigger journeys. Your [Data Engineer](/en/docs/journey-optimizer/using/get-started/by-role/data-engineer) will configure the event schemas and definitions in Journey Optimizer.

- Understand the event payload : Work with your Data Engineer to get the event schema and required payload structure. The payload must conform to the XDM schema they’ve configured. Learn about event schema requirements .
- Implement event streaming : Send events to Adobe Experience Platform using the Streaming Ingestion APIs . Learn the steps to send events .
- Handle event types : Unitary events : Implement event sending for person-specific actions (e.g., button click, purchase completion) Business events : Send business-related events (e.g., inventory updates, price changes)
- Test event delivery : Verify that events are properly received and trigger journeys as expected. Learn about event troubleshooting .

**Example implementation** for sending an event via API:

```
POST https://{DATACOLLECTION_ENDPOINT}/collection/{DATASTREAM_ID}
Content-Type: application/json

{
  "header": {
    "datasetId": "{DATASET_ID}",
    "imsOrgId": "{ORG_ID}",
    "source": {
      "name": "Web SDK"
    }
  },
  "body": {
    "xdmMeta": {
      "schemaRef": {
        "id": "{SCHEMA_ID}"
      }
    },
    "xdmEntity": {
      "_id": "unique-event-id",
      "eventType": "purchase",
      "timestamp": "2024-01-01T12:00:00Z",
      // ... your event data
    }
  }
}
```

Learn more about [working with journey events](/en/docs/journey-optimizer/using/configure-journeys/events-journeys/about-events).

## Develop custom action endpoints custom-actions

Custom actions allow journeys to call your APIs. As a developer, you’ll build the API endpoints that custom actions invoke:

- Build your API endpoint : Create RESTful API endpoints that Journey Optimizer will call during journey execution. Your endpoint should: Accept JSON payloads Authenticate requests (OAuth, API key, or JWT) Process requests within appropriate timeout limits Return responses in expected format
- Understand custom action capabilities : Custom actions can connect to third-party systems like Epsilon, Slack, Firebase, or your own services. Learn more about custom actions .
- Work with action configurations : Your Administrator or Data Engineer will configure the custom action in Journey Optimizer, defining the API endpoint URL, authentication method, and parameters. You’ll provide them with your API specification. Learn about custom action configuration . You can define an optional error response payload for richer fallback logic in timeout/error branches.
- Return actionable data : Design your API to return data that can be used in subsequent journey steps. Learn about action responses .
- Monitor custom action health : Use the custom action monitoring dashboard to track successful calls, errors, throughput, response times, and queue wait times. Learn about custom action reporting .
- Implement rate limiting : Ensure your endpoints can handle the expected volume. Journey Optimizer applies a 5000 calls/second limit, but your system should be resilient. Learn about capping and throttling .

**Example use case**: [Writing journey events to Experience Platform](/en/docs/journey-optimizer/using/orchestrate-journeys/journey-use-cases/custom-action-aep) using custom actions.

## Work with Journey Optimizer APIs apis

Journey Optimizer provides comprehensive REST APIs for programmatic access:

- Understand API capabilities : Journey Optimizer APIs allow you to create, read, update, and delete various resources programmatically. Learn about Journey Optimizer APIs .
- Authentication : Follow this tutorial to set up API authentication using Adobe Developer Console.
- Explore API references : Browse the complete API documentation and try APIs directly in the Adobe Journey Optimizer API reference .
- API-triggered campaigns : Build transactional messaging with API-triggered campaigns. For high-volume scenarios (up to 5000 TPS), explore High Throughput mode (requires add-on license).
- Decision Management APIs : Use specialized APIs for offer management and decisioning. Learn more in the Decision Management API guide .
- Decisioning migration APIs : Programmatically migrate Decision Management entities to Decisioning with flexible scopes, automated validation, and rollback support. Learn more in the Decisioning migration API guide .
- SMS Webhooks : Configure inbound webhooks to capture incoming messages and feedback webhooks to receive delivery receipts and status updates. Learn more .

## Testing and debugging testing

- Debug SDK implementation : Use Adobe Experience Platform Assurance to inspect SDK events, validate data collection, and troubleshoot integration issues in real-time. Learn more about Assurance .
- Test event delivery : Verify that events from your application are correctly received by Adobe Experience Platform and trigger journeys as expected. Monitor event ingestion and validate payload structure.
- Validate API integrations : Test your custom action endpoints to ensure they handle Journey Optimizer requests correctly, respond within timeout limits, and return expected data formats.
- Use test mode with test profiles : Work with your Data Engineer to get access to test profiles, then validate your implementation using journey test mode. Learn how to test journeys .
- Monitor SDK logs : Enable debug logging in your SDK implementation to troubleshoot issues during development: Mobile SDK : Enable logging to see SDK events and API calls Web SDK : Use browser console to monitor SDK activity
- Verify datastream configuration : Ensure your datastream is correctly configured to send data to Journey Optimizer. Check that events flow through the datastream to the correct destinations.
- Query journey data for analysis : Use SQL queries on the Data Lake to analyze journey step events, debug issues, and monitor custom action performance. Explore query examples for journey analysis including: Profile entry/exit tracking and discard reasons Custom action performance metrics (latency, throughput, errors) Event delivery and error patterns Journey instance states

## Advanced developer topics advanced-topics

### Working with contextual data and enrichment

- **Iterate over arrays**: Use Handlebars syntax to display dynamic lists from events, custom action responses, and dataset lookups in messages. Learn about [iterating contextual data](/en/docs/journey-optimizer/using/content-management/personalization/iterate-contextual-data).
- **Dataset lookup**: Implement dataset lookups to enrich journey data from Adobe Experience Platform datasets. Work with your Data Engineer on configuration. Learn about [dataset lookup](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/dataset-lookup).

### Working with consent and governance

Implement data governance and consent policies in your integrations:

- **Data governance**: Apply data usage policies to custom actions. Learn more about [data governance](/en/docs/journey-optimizer/using/privacy/action-privacy).
- **Consent management**: Handle customer consent preferences in your implementations. Learn about [consent](/en/docs/journey-optimizer/using/privacy/consent/consent).

### Optimization and best practices

- **Capping and throttling**: Understand rate limits and implement appropriate throttling. Learn about [external systems](/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems).
- **Journey optimization**: Follow best practices for [journey optimization](/en/docs/journey-optimizer/using/orchestrate-journeys/about-journey-building/optimize-activity/optimize).
- **Error handling**: Implement robust error handling. Review [error codes](/en/docs/journey-optimizer/using/monitor/monitor-alerts-errors/error-codes-reference) and [troubleshooting guides](/en/docs/journey-optimizer/using/monitor/troubleshooting/troubleshoot-journey/troubleshooting).

## Additional resources additional-resources

- **Developer Console**: Access the [Adobe Developer Console](https://developer.adobe.com#_blank) to create integrations and manage API credentials.
- **Sample code**: Explore [sample implementations on GitHub](https://github.com/adobe/alloy-samples/tree/main/ajo#_blank).
- **Tutorial videos**: Learn through hands-on tutorials on [Experience League](/en/docs/journey-optimizer-learn/tutorials/overview#_blank).
- **Developer community**: Connect with other developers and get support in the Adobe community forums.

## Collaborate across roles next-steps

Your implementation work intersects with other team members:

Work with Data Engineers
Collaborate with [Data Engineers](/en/docs/journey-optimizer/using/get-started/by-role/data-engineer) on data and event configurations:

- Get the XDM schemas and event structures you need to implement
- Understand which events you need to send and their required payload format
- Align on data collection requirements and data quality standards
- Test event delivery and data ingestion together

Work with Administrators
Collaborate with [Administrators](/en/docs/journey-optimizer/using/get-started/by-role/administrator) on access and configurations:

- Provide API specifications for custom actions they’ll configure
- Request necessary permissions and API credentials
- Coordinate on channel configuration requirements (e.g., push certificates)
- Align on testing environments and sandbox strategy

Work with Marketers
Collaborate with [Marketers](/en/docs/journey-optimizer/using/get-started/by-role/marketer) on journey requirements and testing:

- Understand which user interactions should trigger events
- Implement tracking for content performance and user engagement
- Support testing of journeys with your implemented features
- Troubleshoot issues with message delivery or personalization

## Start implementing

Ready to start building? Choose your first implementation area from the sections above:

- **Mobile app?** Start with [Mobile SDK integration](#mobile-integration)
- **Website?** Begin with [Web SDK setup](#web-implementation)
- **API integration?** Jump to [Working with APIs](#apis)
- **Custom system?** Check out [Custom actions](#custom-actions)

Each section includes links to detailed technical documentation, code samples, and tutorials to guide your implementation.

recommendation-more-help
