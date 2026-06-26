---
title: "Work with the Capping API work"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/external-systems/capping"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:05.592596+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with the Capping API work

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [API](#)

CREATED FOR:

- Beginner
- Developer

The Capping API helps you create, configure and monitor your capping configurations.

This section provides global information on how to work with the API. A detailed API description is available in [Adobe Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis#_blank).

## Capping API description & Postman collection description

The table below lists the available commands for the capping API. Detailed information including request samples, parameters, and response formats is available in the [Adobe Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/journeys-throttling#_blank).

Method
Path
Description
POST
list/endpointConfigs
Get a list of the endpoint capping configurations
POST
/endpointConfigs
Create an endpoint capping configuration
POST
/endpointConfigs/
{uid}
/deploy
Deploy an endpoint capping configuration
POST
/endpointConfigs/
{uid}
/undeploy
Undeploy an endpoint capping configuration
POST
/endpointConfigs/
{uid}
/canDeploy
Check if an endpoint capping configuration can be deployed or not
PUT
/endpointConfigs/
{uid}
Update an endpoint capping configuration
GET
/endpointConfigs/
{uid}
Retrieve an endpoint capping configuration
DELETE
/endpointConfigs/
{uid}
Delete an enpoint capping configuration
When a configuration is created or updated, a check is automatically performed to guarantee the syntax and the integrity of the payload.If some problems occur, the operation returns warning or errors to help you correct the configuration.

In addition, a Postman collection is available [here](https://github.com/AdobeDocs/JourneyAPI/blob/master/postman-collections/Journeys_Capping-API_postman-collection.json) to help you in your testing configuration.

This collection has been set up to share the Postman Variable collection generated via **Adobe I/O Console’s Integrations > Try it out > Download for Postman**, which generates a Postman Environment file with the selected integrations values.

Once downloaded and uploaded into Postman, you need to add three variables: {JO_HOST},{BASE_PATH} and {SANDBOX_NAME}.

- {JO_HOST} : Journey Optimizer Gateway URL.
- {BASE_PATH} : entry point for the API.
- {SANDBOX_NAME} : the header **x-sandbox-name** (for example, ‘prod’) corresponding to the sandbox name where the API operations will take place. See the [sandboxes overview](/en/docs/experience-platform/sandbox/home#_blank) for more information.

## Endpoint configuration

Here is the basic structure of an endpoint configuration:

```
{
    "url": "<endpoint URL>",  //wildcards are allowed in the endpoint URL
    "methods": [ "<HTTP method such as GET, POST, >, ...],
    "services": {
        "<service name>": { . //must be "action" or "dataSource"
            "maxHttpConnections": <max connections count to the endpoint (optional)>
            "rating": {
                "maxCallsCount": <max calls to be performed in the period defined by period/timeUnit>,
                "periodInMs": <integer value greater than 0>
            }
        },
        ...
    }
}
```

IMPORTANT
The
maxHttpConnections
parameter is optional. It allows you to restrict the number of connections Journey Optimizer will open to the external system.
The max value that can be set is 400. If nothing is specified, then the system may open up to multiple thousands of connections depending on the dynamic scaling of the system.
When the capping configuration is deployed, if no
maxHttpConnections
value has been set, a default
maxHttpConnections = -1
is added into the deployed configuration, and Journey Optimizer uses the default system value.
Example:

```
{
  "url": "https://api.example.org/data/2.5/*",
  "methods": [
    "GET"
  ],
  "services": {
    "dataSource": {
      "rating": {
        "maxCallsCount": 500,
        "periodInMs": 1000
      }
    }
  }
}
```

IMPORTANT
The configuration will only be active after calling the
deploy
endpoint.
## Warning and errors

When a **canDeploy** method is called, the process validates the configuration and returns the validation status identified by its Unique ID, either:

```

"ok" or "error"
```

The potential errors are:

- **ERR_ENDPOINTCONFIG_100**: capping config: missing or invalid url
- **ERR_ENDPOINTCONFIG_101**: capping config: malformed url
- **ERR_ENDPOINTCONFIG_102**: capping config: malformed url: wildchar in url not allowed in host:port
- **ERR_ENDPOINTCONFIG_103**: capping config: missing HTTP methods
- **ERR_ENDPOINTCONFIG_104**: capping config: no call rating defined
- **ERR_ENDPOINTCONFIG_107**: capping config: invalid max calls count (maxCallsCount)
- **ERR_ENDPOINTCONFIG_108**: capping config: invalid max calls count (periodInMs)
- **ERR_ENDPOINTCONFIG_111**: capping config: can’t create endpoint config: invalid payload
- **ERR_ENDPOINTCONFIG_112**: capping config: can’t create endpoint config: expecting a JSON payload
- **ERR_AUTHORING_ENDPOINTCONFIG_1**: invalid service name <!--<given value>-->: must be ‘dataSource’ or ‘action’

The potential warning is:

**ERR_ENDPOINTCONFIG_106**: capping config: max HTTP connections not defined: no limitation by default

## Use cases

This section lists key use cases for managing capping configurations in Journey Optimizer and the associated API commands required to implement the use case.

Details on each API command is available in the [API description & Postman collection](#description).

Create and deploy a new capping configuration
API calls to use:

- **list** – Retrieves existing configurations.
- **create** – Creates a new configuration.
- **candeploy** – Checks whether the configuration can be deployed.
- **deploy** – Deploys the configuration.

Update and deploy a capping configuration (not yet deployed)
API calls to use:

- **list** – Retrieves existing configurations.
- **get** – Fetches details of a specific configuration.
- **update** – Modifies the configuration.
- **candeploy** – Checks deployment eligibility.
- **deploy** – Deploys the configuration.

Undeploy and delete a deployed capping configuration
API calls to use:

- **list** – Retrieves existing configurations.
- **undeploy** – Undeploys the configuration.
- **delete** – Removes the configuration.

Delete a deployed capping configuration in one step
In only one API call, you can undeploy and delete the configuration with the use of the forceDelete parameter.

API calls to use:

- **list** – Retrieves existing configurations.
- **delete (with forceDelete parameter)** – Forces deletion of a deployed configuration in a single step.

Update a capping configuration already deployed
| note |
| --- |
| NOTE |
| A redeployment is required after updating an already deployed configuration. |

API calls to use:

- **list** – Retrieves existing configurations.
- **get** – Fetches details of a specific configuration.
- **update** – Modifies the configuration.
- **undeploy** – Undeploys the configuration before applying changes.
- **candeploy** – Checks deployment eligibility.
- **deploy** – Deploys the updated configuration.

recommendation-more-help
