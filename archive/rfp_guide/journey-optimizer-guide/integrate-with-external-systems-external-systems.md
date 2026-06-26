---
title: "Integrate with external systems external-systems"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/external-systems/external-systems"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:36:51.866458+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Integrate with external systems external-systems

Last update: May 8, 2026
- Topics:
- [Integrations](#)

CREATED FOR:

- Beginner
- User

This page presents the different guardrails provided by Journey Optimizer when integrating an external system, as well as best practices: how to optimize the protection of your external system using the capping API, how to configure journey timeout, and how retries work.

Journey Optimizer allows you to configure connections to external systems via [custom data sources](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources) and [custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action). This allows you, for example, to enrich your journeys with data coming from an external reservation system, or send messages using a third-party system such as Epsilon or Facebook.

When integrating an external system, you can encounter several issues, the system can be slow, can stop responding, or it might not be able to handle a large volume. Journey Optimizer offers several guardrails to protect your system from over-loading.

All external systems are different in terms of performance. You need to adapt the configuration to your use cases.

When Journey Optimizer executes a call to an external API, the technical guardrails are executed as follows:

- Capping or throttling rules are applied: if the maximum rate is reached, remaining calls are discarded or queued.
- Timeout and retry: if the capping or throttling rule is fulfilled, Journey Optimizer tries to perform the call until the end of the timeout duration is reached.

TIP
We recommend leaving at least a one-minute buffer between the external API’s token expiration period and your Journey Optimizer
cacheDuration
setting
, especially under heavy workloads, to avoid expiration mismatches and 401 errors.
## Capping & throttling APIs capping

### About capping & throttling apis

When configuring a datasource or an action, you establish a connection to a system to either retrieve additional information to use in your journeys or send messages or API calls.

Journeys APIs support up to 5,000 event per second but some external systems or API may not have an equivalent throughput. To prevent overloading these systems, you can use the **Capping** and **Throttling** APIs to limit the number of events sent per second.

Every time an API call is performed by journeys, it passes through the API engine. If the limit set in the API is reached, the call is either rejected if you are using the Capping API, or queued for up to 6 hours and processed as soon as possible in the order they were received if you are using the Throttling API.

For example, let’s say that you have defined a capping or throttling rule of 200 calls per second for your external system. Your system is called by a custom action in 10 different journeys. If one journey receives 300 calls per second, it will use the 200 slots available and discard or queue the 100 remaining slots. Since the maximum rate has exceeded, the other 9 journeys will not have any slot left. This granularity helps to protect the external system from over-loading and crashing.

IMPORTANT
Capping rules
are configured at sandbox level, for a specific endpoint (the URL called) but global to all journeys of that sandbox. Capping is available on both data sources and custom actions.
Throttling rules
are configured on production sandboxes only, for a specific endpoint but global to all journeys across all sandboxes. You can have only one throttling configuration per organization. Throttling is only available on custom actions.
The
maxCallsCount
value has to be greater than 1.
For more information on how to work with the APIs, refer to these sections:

- [Capping API](/en/docs/journey-optimizer/using/connect-systems/external-systems/capping)
- [Throttling API](/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling)

A detailed description of the APIs is available in [Adobe Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/journeys-throttling)

### Data sources & custom actions capacity capacity

For **external data sources**, the maximum number of calls per second is limited to 15. If this limit is exceeded, any additional calls are either discarded or queued depending on the API in use. It is possible to increase this limit for private external data sources by contacting Adobe to include the endpoint in the allowlist, but this is not an option for public external data sources. * [Learn how to configure data sources](/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/about-data-sources).

NOTE
If a datasource uses a custom authentication with a different endpoint than the one used for the datasource, you need to contact Adobe to also include that endpoint in the allowlist.
For **custom actions**, you need to evaluate the capacity of your external API. For example, if Journey Optimizer sends 1000 calls per second and your system can only support 200 calls per second, you need to define a capping or throttling configuration so that your system does not saturate. [Learn how to configure actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action)

NOTE
As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases. For more information on responses, see this
section
## Endpoints with slow response time response-time

When an endpoint has a response time greater than 0.75 seconds, its custom action calls are routed through a dedicated **slow custom action service** instead of the default service.

This slow custom action service applies a capping limit of 150,000 calls every 30 seconds. The limit is enforced using a sliding window, which can begin at any millisecond within that 30-second period. Once the window is full, additional calls are rejected with capping errors. The system does not wait for the next fixed interval but begins capping immediately after the 30-second threshold is reached.

Because slow endpoints can cause delays across all queued actions in the pipeline, it is recommended not to configure custom actions with endpoints that have slow response times. Routing such actions to the slow service helps protect overall system performance and prevents added latency for other custom actions.

## Timeout and retries timeout

If the capping or throttling rule is fulfilled, then the timeout rule is applied.

In each journey, you can define a timeout duration. This allows you to set a maximum duration when calling an external system. Timeout duration is configured in the properties of a journey. Refer to [this page](/en/docs/journey-optimizer/using/orchestrate-journeys/create-journey/journey-properties#timeout_and_error).

This timeout is global to all external calls (external API calls in custom actions and custom data sources). By default, it is set to 30 seconds.

During the defined timeout duration, Journey Optimizer tries to call the external system. After the first call, a maximum of three retries can be performed until the end of timeout duration is reached. The number of retries cannot be changed.

Each retry uses one slot. If you have a capping of 100 calls per second and each of your calls require two retries, the rate drops to 30 calls per second (each call uses 3 slots: the first call and two retries).

The timeout duration value depends on the use case. If you want to send your message quickly, for example when the client enters the store, then you do not want to set up a long timeout. Also, the longer the timeout is, the more items will be placed in queue. This can greatly impact performance. If Journey Optimizer performs 1000 calls per seconds, keeping 5 or 15 seconds of data can quickly overwhelm the system.

Let’s take an example for a timeout of 5 seconds.

- The first call lasts less than 5 seconds: the call is successful, no retry is performed.
- The first call lasts longer 5 seconds: the call is canceled and there is no retry. It is counted as a timeout error in reporting.
- The first call fails after 2 seconds (the external system returns an error): 3 seconds are left for retries, if capping slots are available. If one of the three retries is successful before the end of the 5 seconds, the call is performed, and there is no error. If the end of the timeout duration is reached during the retries, the call is canceled and counted as a timeout error in reporting.

## Frequently asked questions faq

You will find below Frequently Asked Questions about integrating Journey Optimizer with external systems.

Need more details? Use the feedback options at the bottom of this page to raise your question, or connect with [Adobe Journey Optimizer community](https://experienceleaguecommunities.adobe.com/t5/adobe-journey-optimizer/ct-p/journey-optimizer?profile.language=en#_blank).

How can I configure a capping or throttling rule? Is there a default rule?
To create capping or throttling rules, please refer to
this section
. By default, there is no throttling rule but a capping limit of 300,000 calls over one minute defined for all custom actions, per host and per sandbox. The “per host” limit applies at the domain level (e.g., example.com). This limit has been set based on customers usage, to protect external endpoints targeted by custom actions. If needed, you can override this setting by defining a greater capping or throttling limit through our Capping/Throttling APIs. Refer to
this page
for more details on how to request capping increases.
How many retries are performed? Can I change the number of retries or define a minimum wait period between retries?
For a given call, a maximum of three retries can be performed after the first call, until the end of timeout duration is reached. The number of retries and the time between each retry cannot be changed. Refer to
this section
.
Where can I configure the timeout? Is there a maximum value?
In each journey, you can define a timeout duration. Timeout duration is configured in the properties of a journey. Timeout duration must be between 1 second and 30 seconds. Refer to
this section
and
this page
.
What is the egress proxy and when should I use it?
The egress proxy provides a **static IP address** for outbound calls from Journey Optimizer **Custom actions** to your external systems. Use it when your third-party endpoints require IP allowlisting.

**Important:** The egress proxy does NOT control throughput, rate limits, or the number of concurrent connections. To manage call volume and connection limits, use the [Capping API](/en/docs/journey-optimizer/using/connect-systems/external-systems/capping) or [Throttling API](/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling).

**Use the egress proxy for:**

- Allowlisting a static IP on your third-party firewall or endpoint

**Use capping/throttling APIs for:**

- Limiting the number of API calls per second
- Controlling concurrent connections to your endpoint
- Protecting your external system from overload

Contact Adobe to enable the egress proxy for your organization if you need a static IP for allowlisting purposes.

What is the max number of connections opened by Journey Optimizer when custom actions are used?
With the IP proxy enabled and a throttling configuration defined on the targeted endpoint, the number of connections is based on the rate (those are estimates, not guaranteed numbers):

- between 200 and 2000 c/s: 50 connections
- between 2000 and 3000: 75 connections
- between 3000 and 4000: 100 connections
- between 4000 and 5000: 125 connections

If no throttling configuration is defined on an endpoint, Journey Optimizer’s engine is designed to scale up and it can get to a high number of connections (more than 2,000). In order to get limited number of connections, customers need to use a throttling configuration.

recommendation-more-help
