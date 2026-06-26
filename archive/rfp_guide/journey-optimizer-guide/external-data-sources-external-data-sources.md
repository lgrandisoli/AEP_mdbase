---
title: "External data sources external-data-sources"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/configure-journeys/data-source-journeys/external-data-sources"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:01.033897+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# External data sources external-data-sources

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [Data Sources](#)
- [Integrations](#)

CREATED FOR:

- Intermediate
- Experienced
- Developer
- Admin

## Work with external data sources gs-ext-data-sources

External data sources allow you to define a connection to third-party systems, for example if you are using a hotel booking system to check if the person has registered a room. As opposed to the built-in Adobe Experience Platform data source, you can create as many external data sources as you need.

NOTE
- Guardrails when working with external systems are listed on this page .
- As the responses are now supported, you should use custom actions instead of data sources for external data sources use-cases. For more information on responses, see custom action responses . Custom Actions without Data Lake persistence are the right choice when the data is only useful inside the journey and the external system is accessible via an API endpoint. For a comparison of all data access options, see Choose your data access strategy .

REST APIs using POST or GET and returning JSON are supported. API Key, basic and custom authentication modes are supported.

Let’s take the example of a weather API service that I want to use to customize my journey’s behaviors according to real-time weather data.

Here are two examples of the API call:

- *https://api.adobeweather.org/weather?city=London,uk&appid=1234*
- *https://api.adobeweather.org/weather?lat=35&lon=139&appid=1234*

The call is composed of a main URL (*https://api.adobeweather.org/weather*), two parameter sets (“city” for the city and “lat/long” for the latitude and longitude) and the API key (appid).

TIP
We recommend leaving at least a one-minute buffer between the external API’s token expiration period and your Journey Optimizer
cacheDuration
setting
, especially under heavy workloads, to avoid expiration mismatches and 401 errors.
## Create and configure an external data source create-ext-data-sources

Below are the main steps to create and configure a new external data source:

- From the list of data sources, click Create Data Source to create a new external data source. This opens the data source configuration pane on the right-hand side of the screen.
- Enter a name for your data source.

Only alphanumeric characters and underscores are allowed. The maximum length is 30 characters.

- Add a description to your data source. This step is optional.
- Add the URL of the external service. In our example: https://api.adobeweather.org/weather . note caution CAUTION We strongly recommend using HTTPS for security reasons. Also note that we do not allow the use of Adobe addresses that are not publicly available and the use of IP addresses.
- Configure the authentication depending on the external service configuration: No authentication , Basic , Custom or API key . For the basic authentication mode, you need to fill in a username and a password. note NOTE When the authentication call is performed, the <username>:<password> string, encoded in base64, is added in the Authentication header. Adobe Journey Optimizer automatically encrypts secrets defined in custom actions. Each organization’s encryption keys are securely managed in a dedicated vault tied to their organization. When credentials are displayed in the interface, they are masked by default to prevent accidental exposure. For more information about the custom authentication mode, see the custom authentication mode section . In our example, we choose the API key authentication mode, as below: Type : “API key” Name : “appid” (this is the API key parameter name) Value : “1234” (this is the value of our API key) Location : “Query parameter” (the API key is located in the URL)
- Add a new field group for each API parameter set by clicking Add a New Field Group . Only alphanumeric characters and underscores are allowed in the field group name. The maximum length is 30 characters. In our example, we need to create two field groups, one for each parameter set (city and long/lat).

For the “long/lat” parameter set, we create a field group with the following information:

- **Used in**: displays the number of journeys that use a field group. You can click the **View journeys** icon to display the list of journeys using this field group.
- **Method**: select the POST or GET method. In our case, we select the GET method.
- **Dynamic Values**: enter the different parameters separated by a comma, “long,lat” in our example. Since the parameter values depend on the execution context, they will be defined in the journeys. [Learn more about expressions](/en/docs/journey-optimizer/using/orchestrate-journeys/building-advanced-conditions-journeys/expressionadvanced)
- **Response Payload**: click inside the **Payload** field and paste an example of the payload returned by the call. For our example, we used a payload found on a weather API website. Verify that the field types are correct. Each time the API is called, the system will retrieve all the fields included in the payload example. Note that you can click on **Paste a new payload** if you want to change the payload currently passed.
- **Sent Payload**: this field does not appear in our example. It is only available if you select the POST method. Paste the payload that will be sent to the third-party system.

In case of a GET call requiring parameter(s), you enter the parameter(s) in the **Dynamic Values** field and they are automatically added at the end of the call. In case of a POST call, you need to:

- list the parameters to be passed at call time in the **Dynamic Values** field (in the example below: “identifier”).
- specify them also with the exact same syntax in the body of the sent payload. To do so, you need to add: “param”: “name of your parameter” (in the example below: “identifier”). Follow the syntax below:

```
{"id":{"param":"identifier"}}
```

Once your changes are saved, the data source is configured and ready to be used in your journeys, for example in your conditions or to personalize an email. If the temperature is above 30°C, you can decide to send a specific communication.

## Custom authentication mode custom-authentication-mode

The custom authentication mode is used for complex authentication, frequently used to call API wrapping protocols such as OAuth2, to retrieve an access token to be injected in the real HTTP request for the action.

When you configure the custom authentication, use the **Click to check the authentication** button to control if the custom authentication payload is correctly configured.

When the test is successful, the button turns green.

With this authentication mode, the action execution is a two-step process:

- Call the endpoint to generate the access token.
- Call the REST API by injecting in the proper way the access token.

NOTE
This authentication has two parts.
### Definition of the endpoint to be called to generate the access token custom-authentication-endpoint

- endpoint : URL to use to generate the endpoint
- method of the HTTP request on the endpoint ( GET or POST )
- headers : key-value pairs to be injected as headers in this call if required
- body : describes the body of the call if the method is POST. We support a limited body structure, defined in the bodyParams (key-value pairs). The bodyType describes the format and encoding of the body in the call: form : meaning that the content type will be application/x-www-form-urlencoded (charset UTF-8) and the key-value pairs will be serialized as is: key1=value1&key2=value2&… json : meaning that the content type will be application/json (charset UTF-8) and the key-value pairs will be serialized as a json object as is: { “key1”: “value1”, “key2”: “value2”, …}

### Definition of the way the access token must be injected in the HTTP request of the action custom-authentication-access-token

- authorizationType : defines how the generated access token must be injected in the HTTP call for the action. The possible values are: bearer : indicates that the access token must be injected in the Authorization header, such as: Authorization: Bearer <access token> header : indicates that the access token must be injected as a header, the header name defined by the property tokenTarget . For instance, if the tokenTarget is myHeader , the access token will be injected as a header as: myHeader: <access token> queryParam : indicates that the access token must be injected as a queryParam, the query param name defined by the property tokenTarget. For instance, if the tokenTarget is myQueryParam, the URL of the action call will be: <url>?myQueryParam=<access token>
- tokenInResponse : indicates how to extract the access token from the authentication call. This property can be: response : indicates that the HTTP response is the access token a selector in a json (assuming that the response is a json, we do not support other formats such as XML). The format of this selector is json://<path to the access token property> . For instance, if the response of the call is: { “access_token”: “theToken”, “timestamp”: 12323445656 } , the tokenInResponse will be: json: //access_token

The format of this authentication is:

```
{
    "type": "customAuthorization",
    "endpoint": "<URL of the authentication endpoint>",
    "method": "<HTTP method to call the authentication endpoint, in 'GET' or 'POST'>",
    (optional) "headers": {
        "<header name>": "<header value>",
        ...
    },
    (optional, mandatory if method is 'POST') "body": {
        "bodyType": "<'form'or 'json'>,
        "bodyParams": {
            "param1": value1,
            ...
        }
    },
    "tokenInResponse": "<'response' or json selector in format 'json://<field path to access token>'",
    "cacheDuration": {
        (optional, mutually exclusive with 'duration') "expiryInResponse": "<json selector in format 'json://<field path to expiry>'",
        (optional, mutually exclusive with 'expiryInResponse') "duration": <integer value>,
        "timeUnit": "<unit in 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'months', 'years'>"
    },
    "authorizationType": "<value in 'bearer', 'header' or 'queryParam'>",
    (optional, mandatory if authorizationType is 'header' or 'queryParam') "tokenTarget": "<name of the header or queryParam if the authorizationType is 'header' or 'queryParam'>",
}
```

NOTE
Encode64 is the only function available in the authentication payload.
You can change the cache duration of the token for a custom authentication data source. Below is an example of a custom authentication payload. The cache duration is defined in the cacheDuration parameter. It specifies the retention duration of the generated token in the cache. The unit can be milliseconds, seconds, minutes, hours, days, months, years.

Here is an example for the bearer authentication type:

```
{
    "type": "customAuthorization",
    "endpoint": "https://<your_auth_endpoint>/epsilon/oauth2/access_token",
    "method": "POST",
    "headers": {
      "Authorization": "Basic EncodeBase64(<epsilon Client Id>:<epsilon Client Secret>)"
    },
    "body": {
      "bodyType": "form",
      "bodyParams": {
        "scope": "cn mail givenname uid employeeNumber",
        "grant_type": "password",
        "username": "<epsilon User Name>",
        "password": "<epsilon User Password>"
      }
    },
    "tokenInResponse": "json://access_token",
    "cacheDuration": {
      "duration": 5,
      "timeUnit": "minutes"
    },
  },
```

NOTE
- The authentication token is cached per journey: if two journeys are using the same custom action, each journey has its own token cached. That token is not shared between those journeys.
- Cache duration helps to avoid too many calls to the authentication endpoints. Authentication token retention is cached in services, there is no persistence. If a service is restarted, it starts with a clean cache. The cache duration by default is 1 hour. In the custom authentication payload, it can be adapted by specifying another retention duration.

Here is an example for the header authentication type:

```
{
  "type": "customAuthorization",
  "endpoint": "https://myapidomain.com/v2/user/login",
  "method": "POST",
  "headers": {
    "x-retailer": "any value"
  },
  "body": {
    "bodyType": "form",
    "bodyParams": {
      "secret": "any value",
      "username": "any value"
    }
  },
  "tokenInResponse": "json://token",
  "cacheDuration": {
    "expiryInResponse": "json://expiryDuration",
    "timeUnit": "minutes"
  },
  "authorizationType": "header",
  "tokenTarget": "x-auth-token"
}
```

Here is an example of the response of the login API call:

```
{
  "token": "xDIUssuYE9beucIE_TFOmpdheTqwzzISNKeysjeODSHUibdzN87S",
  "expiryDuration" : 5
}
```

CAUTION
When configuring custom authentication for a custom action, note that nested JSON objects (e.g., sub-objects within
bodyParams
) are
supported
.
recommendation-more-help
