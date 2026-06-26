---
title: "Work with the Throttling API"
url: "https://experienceleague.adobe.com/en/docs/journey-optimizer/using/connect-systems/external-systems/throttling"
category: "other"
topic: "documentation/journey-optimizer/journey-optimizer-guide"
created_at: "2026-05-13T15:37:04.304706+00:00"
---
Breadcrumbs: Documentation > Journey Optimizer > Journey Optimizer Guide

# Work with the Throttling API

Last update: May 8, 2026
- Topics:
- [Journeys](#)
- [API](#)

CREATED FOR:

- Beginner
- Developer

The Throttling API helps you create, configure and monitor your throttling configurations in order to limit the number of events sent per second.

This section provides global information on how to work with the API. A detailed API description is available in [Adobe Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis#_blank).

## Must-read

- One configuration per organization: Only one configuration is currently allowed per organization. A configuration must be defined on a production sandbox (given through x-sandbox-name in the headers).
- Organization-level application: A configuration is applied at organization level.
- API limit handling: When the limit set in the API is reached, further events are queued for up to 6 hours. This value cannot be modified.
- maxHttpConnections parameter: The maxHttpConnections parameter is an optional parameter available in Capping API only allowing you to restrict the number of connections Journey Optimizer will open to the external system. Learn how to work with the Capping API If you want to restrict the number of connections but also throttle those external calls, you can configure two configurations, one throttling and one capping, on the same endpoint. Both configurations can co-exist for one endpoint. To set ‘maxHttpConnections’ for a throttled endpoint, use the Throttling API to set the throttling threshold and the Capping API to set the ‘maxHttpConnections’. When calling the Capping API, you can set the capping threshold to something higher than the throttling threshold so the capping rule will effectively never come into play.

## Throttling API description & Postman collection description

The table below lists the available commands for the throttling API. Detailed information including request samples, parameters, and response formats is available in the [Adobe Journey Optimizer APIs documentation](https://developer.adobe.com/journey-optimizer-apis/references/journeys-throttling).

Method
Path
Description
POST
list/throttlingConfigs
Get a list of the throttling configurations
POST
/throttlingConfigs
Create a throttling configuration
POST
/throttlingConfigs/
{uid}
/deploy
Deploy a throttling configuration
POST
/throttlingConfigs/
{uid}
/undeploy
Undeploy a throttling configuration
POST
/throttlingConfigs/
{uid}
/canDeploy
Check if a throttling configuration can be deployed or not
PUT
/throttlingConfigs/
{uid}
Update a throttling configuration
GET
/throttlingConfigs/
{uid}
Retrieve a throttling configuration
DELETE
/throttlingConfigs/
{uid}
Delete a throttling configuration
In addition, a Postman collection is available [here](https://github.com/AdobeDocs/JourneyAPI/blob/master/postman-collections/Journeys_Throttling-API_postman-collection.json#_blank) to help you in your testing configuration.

This collection has been set up to share the Postman Variable collection generated via **Adobe I/O Console’s Integrations > Try it out > Download for Postman**, which generates a Postman Environment file with the selected integrations values.

Once downloaded and uploaded into Postman, you need to add three variables: {JO_HOST},{BASE_PATH} and {SANDBOX_NAME}.

- {JO_HOST} : Journey Optimizer Gateway URL.
- {BASE_PATH} : entry point for the API.
- {SANDBOX_NAME} : the header **x-sandbox-name** (for example, ‘prod’) corresponding to the sandbox name where the API operations will take place. See the [sandboxes overview](/en/docs/experience-platform/sandbox/home#_blank) for more information.

## Throttling configuration configuration

Here is the structure of a throttling configuration. **name** and **description** attributes are optional.

```
{
    "name": "<given name - free text>",
    "description": "<given description - free text>"
    "urlPattern": "<endpoint URL - wildcards are allowed>",
    "methods": [ "<HTTP method such as GET, POST, PUT>" ],
    "maxThroughput": <max call throughput>
}
```

Example:

```
{
  "name": "throttling-config-external",
  "description": "example of throttling config for an external endpoint",
  "urlPattern": "https://api.example.org/data/2.5/*",
  "methods": ["POST", "PUT"],
  "maxThroughput": 4000
}
```

IMPORTANT
The configuration will only be active after calling the
deploy
endpoint.
## Errors

When creating or updating a configuration, the process validates the given configuration and returns the validation status identified by its Unique ID, either:

```

"ok" or "error"
```

IMPORTANT
The attributes
maxThroughput
,
urlPattern
and
methods
are mandatory.
maxThroughput
value must be in 200-5000 range.
When creating, deleting or deploying throttling configuration, the following errors can occur :

- **ERR_THROTTLING_CONFIG_100**: throttling config: <mandatory attribute> required
- **ERR_THROTTLING_CONFIG_101**: throttling config: maxThroughput is required and must be greater than or equal to 200 and less than or equal to 5,000
- **ERR_THROTTLING_CONFIG_104**: throttling config: malformed url pattern
- **ERR_THROTTLING_CONFIG_105**: throttling config: wildcards not allowed in host part of the url pattern
- **ERR_THROTTLING_CONFIG_106**: throttling config: invalid payload
- **THROTTLING_CONFIG_DELETE_FORBIDDEN_ERROR: 1456**, “Can’t delete a deployed throttling config. Undeploy it before deleting it”
- **THROTTLING_CONFIG_DELETE_ERROR: 1457**, “Can’t delete throttling config: unexpected error occurs”
- **THROTTLING_CONFIG_DEPLOY_ERROR: 1458**, “Can’t deploy throttling config: unexpected error occurs”
- **THROTTLING_CONFIG_UNDEPLOY_ERROR: 1459**, “Can’t undeploy throttling config: unexpected error occurs”
- **THROTTLING_CONFIG_GET_ERROR: 1460**, “Can’t get throttling config: unexpected error occurs”
- **THROTTLING_CONFIG_UPDATE_NOT_ACTIVE_ERROR: 1461**, “Can’t update throttling config: runtime version is not active”
- **THROTTLING_CONFIG_UPDATE_ERROR: 1462**, “Can’t update throttling config: unexpected error occurs”
- **THROTTLING_CONFIG_NON_PROD_SANDBOX_ERROR: 1463**, “Operation not allowed on throttling config: non prod sandbox”
- **THROTTLING_CONFIG_CREATE_ERROR: 1464**, “Can’t create throttling config: unexpected error occurs”
- **THROTTLING_CONFIG_CREATE_LIMIT_ERROR: 1465**, “Can’t create throttling config: only one config allowed per org”
- **THROTTLING_CONFIG_ALREADY_DEPLOYED_ERROR: 14466**, “Can’t deploy throttling config: already deployed”
- **THROTTLING_CONFIG_NOT_FOUND_ERROR: 14467**, “throttling config not found”
- **THROTTLING_CONFIG_NOT_DEPLOYED_ERROR: 14468**, “Can’t undeploy throttling config: not deployed yet”

**Errors examples**

When trying to create a config on non-prod sandbox:

```
{
    "status": 400,
    "error": "{\"code\":1463,\"family\":\"INPUT_OUTPUT_ERROR\",\"message\":\"Operation not allowed on throttling config: non prod sandbox\",\"service\":\"vyg-authoring-api\",\"version\":\"ed87515\",\"context\":\"com.adobe.voyager.service.authoring.restapis.v1_0.ThrottlingConfigService:384\",\"schema\":\"throttlingConfigs$ui-tests\"}",
    "requestId": "5sgnAYXs8mpswwjAFEIaAU2faQYbtyHc"
}
```

In case given sanbox does not exist:

```
{
    "status": 500,
    "error": "{\"code\":4000,\"family\":\"INTERNAL_ERROR\",\"message\":\"INTERNAL ERROR\",\"service\":\"vyg-authoring-api\",\"version\":\"ed87515\",\"context\":\"com.adobe.voyager.common.exceptions.ApiErrorException:43\"}",
    "requestId": "04ZJ4e5ki4bYs3lfO17a7hovRGewjvdK"
}
```

When trying to create another config:

```
{
    "status": 400,
    "error": "{\"code\":1465,\"family\":\"INPUT_OUTPUT_ERROR\",\"message\":\"Can't create throttling config: only one config allowed per org\",\"service\":\"vyg-authoring-api\",\"version\":\"ed87515\",\"context\":\"com.adobe.voyager.service.authoring.restapis.v1_0.ThrottlingConfigService:108\",\"schema\":\"throttlingConfigs$prod\"}",
    "requestId": "A7ezT8JhOQT4WIAf1Fv7K2wCDA8281qM"
}
```

## Configuration life-cycle at runtime level config

When a configuration is undeployed, it is marked as inactive at runtime level and pending events continue to be processed during 24 hours. It is then deleted in the runtime service.

After a configuration has been undeployed, it is possible to update and redeploy the configuration. This will create a new runtime configuration that will be considered in the upcoming actions execution.

When updating a configuration already deployed, the new values are taken into account immediately. The underlying system resources are automatically adapted. This is optimal compared to undeploy then redeploy the configuration.

## Responses examples responses

**Creation - POST**

```
{
    "canDeploy": {
        "validationStatus": "ok"
    },
    "createdElement": {
        "name": "throttling-config-external",
        "description": "example of throttling config for an external endpoint",
        "urlPattern": "https://api.example.org/data/2.5/*",
        "methods": [
            "PUT",
            "POST"
        ],
        "maxThroughput": 4000,
        "orgId": "AC202A3A5F615BD30A495FDE@AdobeOrg",
        "sandboxId": "8872a010-f91e-11ea-895c-11ef8f98ba52",
        "sandboxName": "prod",
        "uid": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
        "metadata": {
            "createdBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "createdById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "lastModifiedBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "lastModifiedById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "createdAt": "2023-03-22T10:48:16.099647Z",
            "lastModifiedAt": "2023-03-22T10:48:16.099647Z"
        },
        "state": "created",
        "authoringFormatVersion": "1.0"
    },
    "uid": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
    "uri": "/voyager/apis/throttlingConfigs/043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
    "resStatus": "created"
}
```

**Update - PUT**

```
{
    "updatedElement": {
        "_id": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6_8872a010-f91e-11ea-895c-11ef8f98ba52",
        "name": "throttling-config-external -- optional",
        "description": "example of throttling config for an external endpoint -- optional",
        "urlPattern": "https://api.example.org/data/2.5/*",
        "methods": [
            "POST"
        ],
        "maxThroughput": 5000,
        "orgId": "AC202A3A5F615BD30A495FDE@AdobeOrg",
        "sandboxId": "8872a010-f91e-11ea-895c-11ef8f98ba52",
        "sandboxName": "prod",
        "uid": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
        "metadata": {
            "createdBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "createdById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "lastModifiedBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "lastModifiedById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "createdAt": "2023-03-22T10:48:16.099647Z",
            "lastModifiedAt": "2023-03-22T11:39:14.212983Z"
        },
        "state": "updated",
        "authoringFormatVersion": "1.0",
        "hasBeenDeployed": false
    },
    "uid": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
    "uri": "/voyager/apis/throttlingConfigs/043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
    "resStatus": "updated",
    "canDeploy": {
        "validationStatus": "ok"
    }
}
```

**Read (after update) - GET**

```
{
    "result": {
        "_id": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6_8872a010-f91e-11ea-895c-11ef8f98ba52",
        "name": "throttling-config-external -- optional",
        "description": "example of throttling config for an external endpoint -- optional",
        "urlPattern": "https://api.example.org/data/2.5/*",
        "methods": [
            "POST"
        ],
        "maxThroughput": 5000,
        "orgId": "AC202A3A5F615BD30A495FDE@AdobeOrg",
        "sandboxId": "8872a010-f91e-11ea-895c-11ef8f98ba52",
        "sandboxName": "prod",
        "uid": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
        "metadata": {
            "createdBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "createdById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "lastModifiedBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "lastModifiedById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "createdAt": "2023-03-22T10:48:16.099647Z",
            "lastModifiedAt": "2023-03-22T11:39:14.212983Z"
        },
        "state": "updated",
        "authoringFormatVersion": "1.0",
        "hasBeenDeployed": false
    }
}
```

**Read (after deployment) - GET**

```
{
    "result": {
        "_id": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6_8872a010-f91e-11ea-895c-11ef8f98ba52",
        "orgId": "AC202A3A5F615BD30A495FDE@AdobeOrg",
        "sandboxId": "8872a010-f91e-11ea-895c-11ef8f98ba52",
        "sandboxName": "prod",
        "uid": "043a1aea-2dfd-4965-b93a-cb9a1eced0e6",
        "urlPattern": "https://api.example.org/data/2.5/*",
        "methods": [
            "POST"
        ],
        "maxThroughput": 5000,
        "authoringFormatVersion": "1.0",
        "name": "throttling-config-external -- optional",
        "description": "example of throttling config for an external endpoint -- optional",
        "version": "1.0",
        "state": "deployed",
        "metadata": {
            "createdBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "createdById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "createdAt": "2023-03-22T10:48:16.099647Z",
            "lastModifiedBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "lastModifiedById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "lastModifiedAt": "2023-03-22T11:39:14.212983Z",
            "lastDeployedBy": "dacce1c3-d08b-4862-b434-2a4449c7e642@techacct.adobe.com",
            "lastDeployedById": "309F2A46640B0B300A495C83@techacct.adobe.com",
            "lastDeployedAt": "2023-03-22T11:46:07.532648Z"
        },
        "hasBeenDeployed": true
    }
}
```

## Use cases uc

This section lists key use cases for managing throttling configurations in Journey Optimizer and the associated API commands required to implement the use case.

Details on each API command is available in the [API description & Postman collection](#description).

Creation and deployment of a new throttling configuration
API calls to use:

- **list** – Retrieves existing configurations.
- **create** – Creates a new configuration.
- **candeploy** – Checks whether the configuration can be deployed.
- **deploy** – Deploys the configuration.

Update and deploy a throttling configuration (not yet deployed)
API calls to use:

- **list** – Retrieves existing configurations.
- **get** – Fetches details of a specific configuration.
- **update** – Modifies the configuration.
- **candeploy** – Checks deployment eligibility.
- **deploy** – Deploys the configuration.

Undeploy and delete a deployed throttling configuration
API calls to use:

- **list** – Retrieves existing configurations.
- **undeploy** – Undeploys the configuration.
- **delete** – Removes the configuration.

Delete a deployed throttling configuration
In only one API call, you can undeploy and delete the configuration with the use of the forceDelete parameter.

API calls to use:

- **list** – Retrieves existing configurations.
- **delete (with forceDelete parameter)** – Forces deletion of a deployed configuration in a single step.

Update a throttling configuration already deployed
| note |
| --- |
| NOTE |
| It is not required to undeploy the configuration before updating |

API calls to use:

- **list** – Retrieves existing configurations.
- **get** – Fetches details of a specific configuration.
- **update** – Modifies the configuration.

recommendation-more-help
