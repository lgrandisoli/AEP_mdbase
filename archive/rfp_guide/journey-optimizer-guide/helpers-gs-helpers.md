---
title: "Helpers gs-helpers"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/personalization/functions/helpers"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:35:51.840710+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Helpers gs-helpers

Last update: May 8, 2026
- Topics:
- [Personalization](#)

CREATED FOR:

- Experienced
- Developer

## Default fallback value default-value

The Default Fallback Value helper is used to return a default fallback value if an attribute is empty or null. This mechanism works for Profile attributes and Journey events.

**Syntax**

```
Hello {%=profile.personalEmail.name.firstName ?: "there" %}!
```

In this example, the value there is displayed if the firstName attribute of this profile is empty or null.

## Conditions if-function

The if helper is used to define a conditional block.If the expression evaluation returns true, the block is rendered otherwise it is skipped.

**Syntax**

```
{%#if contains(profile.personalEmail.address, ".edu")%}
<a href="https://www.adobe.com/academia">Check out this link</a>
```

Following the if helper, you can enter an else statement to specify a block of code to be executed, if the same condition is false.The elseif statement will specify a new condition to test if the first statement returns false.

**Format**

```
{
    {
        {%#if condition1%} element_1
        {%else if condition2%} element_2
        {%else%} default_element
        {%/if%}
    }
}
```

**Examples**

- Render different store links based on conditional expressions code language-sql {%#if profile.homeAddress.countryCode = "FR"%} <a href="https://www.somedomain.com/fr">Consultez notre catalogue</a> {%else%} <a href="https://www.somedomain.com/en">Checkout our catalog</a> {%/if%}
- Determine email address extension code language-sql {%#if contains(profile.personalEmail.address, ".edu")%} <a href="https://www.adobe.com/academia">Checkout our page for Academia personals</a> {%else if contains(profile.personalEmail.address, ".org")%} <a href="https://www.adobe.com/orgs">Checkout our page for Non Profits</a> {%else%} <a href="https://www.adobe.com/users">Checkout our page</a> {%/if%}
- Add a conditional link The following operation will add a link to the ‘www.adobe.com/academia’ website for profiles with ‘.edu’ email addresses only, to the ‘www.adobe.com/org’ website for profiles with ‘.org’ email addresses, and the default URL ‘www.adobe.com/users’ for all other profiles: code language-sql {%#if contains(profile.personalEmail.address, ".edu")%} <a href="https://www.adobe.com/academia">Checkout our page for Academia personals</a> {%else if contains(profile.personalEmail.address, ".org")%} <a href="https://www.adobe.com/orgs">Checkout our page for Non Profits</a> {%else%} <a href="https://www.adobe.com/users">Checkout our page</a> {%/if%}
- Conditional content based on audience membership code language-sql {%#if profile.segmentMembership.get("ups").get("5fd513d7-d6cf-4ea2-856a-585150041a8b").status = "existing"%} Hi! Esteemed gold member. <a href="https://www.somedomain.com/gold">Checkout your exclusive perks </a> {%else if profile.segmentMembership.get("ups").get("5fd513d7-d6cf-4ea2-856a-585150041a8c").status = "existing"%} Hi! Esteemed silver member. <a href="https://www.somedomain.com/silver">Checkout your exclusive perks </a> {%/if%}

NOTE
To learn more about audiences and the segmentation service, refer to
this section
.
## Unless unless

The unless helper is used to define a conditional block. By opposition to the if helper, if the expression evaluation returns false, the block is rendered.

**Syntax**

```
{%#unless unlessCondition%} element_1 {%else%} default_element {%/unless%}
```

**Example**

Render some content based on email address extension:

```
{%#unless endsWith(profile.personalEmail.address, ".edu")%}
Some Normal Content
{%else%}
Some edu specific content
{%/unless%}
```

## Each each

The each helper is used to iterate over an array.The syntax of the helper is

```

The syntax of the helper is We can refer to the individual array items by using the keyword this inside the block. The index of the array’s element can be rendered by using {{@index}}.

The syntax of the helper is

The syntax of the helper is Syntax

The syntax of the helper is

The syntax of the helper is
```

- {{this.name}}

```

**Example**

```sql
{{#each profile.homeAddress.city}}
  {{@index}} : {{this}}<br>
{{/each}}
```

**Example**

Render a list of products that this user has in their cart:

```
{{#each profile.products as |product|}}
    <li>{{product.productName}} {{product.productRating}}</li>
{{/each}}
```

NOTE
You can also use the
each
helper to iterate over arrays returned from custom action responses. For an example of iterating over nested arrays from a custom action response, see
Using custom action responses in native channels
.
## With with

The with helper is used to change the evaluation token of template-part.

**Syntax**

```
{{#with profile.person.name}}
{{this.firstName}} {{this.lastName}}
{{/with}}
```

The with helper is useful to define a shortcut variable too.

**Example**

Use with for aliasing long variable names to shorter ones:

```
{{#with profile.person.name as |name|}}
 Hi {{name.firstName}} {{name.lastName}}!
 Checkout our trending products for today!
{{/with}}
```

## Let let

The let function allows an expression to be stored as a variable to be used later in a query.

**Syntax**

```
{% let variable = expression %} {{variable}}
```

**Example**

The following example lets you calculate the total sum of prices for products in the cart with prices between 100 and 1000.

```
{% let sum = 0%}
    {{#each profile.productsInCart as |p|}}
        {%#if p.price>100 and p.price<1000%}
            {%let sum = sum + p.price %}
        {%/if%}
    {{/each}}
{{sum}}
```

## Dataset lookup dataset-lookup

AVAILABILITY
This feature is currently available to all customers as a limited availability release.
For now, the
datasetLookup
helper function can be used within expression fragments for a limited set of customers. To gain access, contact your Adobe representative.
The datasetLookup helper retrieves data from Adobe Experience Platform record datasets during personalization so you can use field values that are not stored on the profile or in the event payload.

**Syntax**

```
{{datasetLookup datasetId="datasetId" id="key" result="store" required=false}}
```

Reference retrieved fields with {{result.fieldId}}, where result is the value you pass to the result parameter.

For dataset enablement, parameter details, examples, and testing, see [Use Adobe Experience Platform data for personalization](/en/docs/journey-optimizer/using/content-management/personalization/aep-data-perso).

## Execution Metadata execution-metadata

The executionMetadata helper allows to dynamically capture and store custom key-value pairs into the message execution context.

**Syntax**

```
{{executionMetadata key="your_key" value="your_value"}}
```

In this syntax, key refers to the metadata name and value is the metadata to persist.

**Use case**

With this function, you can append contextual information to any native action from your campaigns or journeys. This enables you to export real-time delivery contextual data to external systems for various purposes such as tracking, analytics, personalization and downstream processing.

NOTE
- The Execution Metadata function is not supported by [custom actions](/en/docs/journey-optimizer/using/configure-journeys/action-journeys/action).
- The Execution Metadata function is not visible when the content itself is displayed.

For instance, you can use the Execution Metadata helper to append a specific ID to each delivery sent to each profile. This information is generated during runtime and the enriched execution metadata can then be exported for downstream reconciliation with an external reporting platform.

**How it works**

Select any element from your channel content inside a campaign or a journey and, using the personalization editor, add the executionMetadata helper to this element.

Upon runtime, the metadata value is added to the existing **Message Feedback Event Dataset** with the following schema addition:

```
"_experience": {
  "customerJourneyManagement": {
    "messageExecution": {
      "metadata": {
        "your_key": "your_value"
      }
    }
  }
}
```

NOTE
Learn more on datasets in
this section
.
**Limitations**

There is an upper limit of 2kb on the key value pairs per action. If the 2Kb limit is exceeded, the message is still delivered, but any of the key value pairs can be truncated.

Metadata is not captured for profiles excluded from the action. When a profile is excluded from receiving a message, no metadata entry is created for that profile in the dataset.

**Example**

```
{{executionMetadata key="firstName" value=profile.person.name.firstName}}
```

In this example, assuming profile.person.name.firstName = “Alex”, the resulting entity is:

```
{
  "key": "firstName",
  "value": "Alex"
}
```

## Encrypt url-parameter-encryption-helper

AVAILABILITY
This feature is available in Limited Availability. Contact your Adobe representative to gain access.
This capability is currently only available for the Email channel.
The Encrypt function lets you encrypt any expression value at render time—commonly a profile attribute, a token, or even a stringified JSON structure you build in the expression—before it is written into a query parameter on tracking links or landing pages.

Values that would appear as plain text in the URL (including PII or other sensitive data) are not readable when the link is inspected or forwarded. Only the values you wrap with this helper are encrypted; the rest of the URL is unchanged.

**Use case**

This helper allows you to protect sensitive profile data (PII) before including it in rendered output.

**Prerequisite**

An administrator must create at least one active key in the sandbox-level key registry. [Learn how to create and manage keys](/en/docs/journey-optimizer/using/content-management/personalization/url-parameter-encryption#create-keys)

NOTE
Using a revoked or otherwise non-active key should cause the personalization to fail at render time so a message is not sent with an invalid key.
**Syntax**

```
{{encrypt dataPath keyName="keyName" version="version" result="variableName"}}
```

**Usage**

This helper encrypts sensitive data and stores the result in a template variable.The encryption is performed using the AES-256-GCM algorithm.

You can apply the helper to one parameter, several, or all parameters in a link, depending on your URL design and length constraints.

- **Input**: dataPath (data reference that must resolve to a string), keyName (encryption key identifier), version (optional key version), result (variable name for encrypted output)
- **Output**: Makes the encrypted value available in the specified result variable.
- **Result format**: The result variable contains a dot-separated string: keyName.version.nonce.authTag.cipherText (all segments except keyName and version are URL-safe Base64 encoded without padding).
- **Static key requirements**: The keyName and version must be static string literals (dynamic references are not supported).
- **Default version**: The version parameter is optional; if omitted, the encryption key service resolves the default version

**Examples**

Example expression
Result
{{encrypt profile.person.email keyName="email-key" version="1" result="enc"}}{{enc}}
email-key.1.RkFrZU5vbmNlQUJD.T3V0cHV0QXV0aFRhZ0Fh.am9obkBleGFtcGxlLmNvbQ
{{encrypt profile.person.name.firstName keyName="pii-key" version="2" result="encName"}}{{encName}}
pii-key.2.U29tZVJhbmRvbUlW.QXV0aGVudGljYXRpb25UYQ.Sm9obg
**Guardrails**

- Decryption is handled outside Journey Optimizer on your landing pages, apps, or APIs. Plan key lifecycle and rotation with your security team so historical payloads can still be decrypted where needed.
- Revoked keys must not be used for new encryption. Follow your security policy for rotation and decommissioning.
- The encryption process being ressource-intensive, using the Encrypt function may impact throughput at render time.

recommendation-more-help
