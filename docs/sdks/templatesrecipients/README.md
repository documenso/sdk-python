# TemplatesRecipients
(*templates.recipients*)

## Overview

### Available Operations

* [get](#get) - Get template recipient
* [create](#create) - Create template recipient
* [create_many](#create_many) - Create template recipients
* [update](#update) - Update template recipient
* [update_many](#update_many) - Update template recipients
* [delete](#delete) - Delete template recipient

## get

Returns a single recipient. If you want to retrieve all the recipients for a template, use the "Get Template" endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-getTemplateRecipient" method="get" path="/template/recipient/{recipientId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.get(recipient_id=9436.42)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientGetTemplateRecipientResponse](../../models/recipientgettemplaterecipientresponse.md)**

### Errors

| Error Type                                              | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| models.RecipientGetTemplateRecipientBadRequestError     | 400                                                     | application/json                                        |
| models.RecipientGetTemplateRecipientNotFoundError       | 404                                                     | application/json                                        |
| models.RecipientGetTemplateRecipientInternalServerError | 500                                                     | application/json                                        |
| models.APIError                                         | 4XX, 5XX                                                | \*/\*                                                   |

## create

Create a single recipient for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-createTemplateRecipient" method="post" path="/template/recipient/create" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.create(template_id=5712.95, recipient={
        "email": "Gerhard88@yahoo.com",
        "name": "<value>",
        "role": documenso_sdk.RecipientCreateTemplateRecipientRoleRequest.SIGNER,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                 | *float*                                                                                                       | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `recipient`                                                                                                   | [models.RecipientCreateTemplateRecipientRecipient](../../models/recipientcreatetemplaterecipientrecipient.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.RecipientCreateTemplateRecipientResponse](../../models/recipientcreatetemplaterecipientresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.RecipientCreateTemplateRecipientBadRequestError     | 400                                                        | application/json                                           |
| models.RecipientCreateTemplateRecipientInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## create_many

Create multiple recipients for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-createTemplateRecipients" method="post" path="/template/recipient/create-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.create_many(template_id=5642.48, recipients=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                                       | *float*                                                                                                                             | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `recipients`                                                                                                                        | List[[models.RecipientCreateTemplateRecipientsRecipientRequest](../../models/recipientcreatetemplaterecipientsrecipientrequest.md)] | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.RecipientCreateTemplateRecipientsResponse](../../models/recipientcreatetemplaterecipientsresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.RecipientCreateTemplateRecipientsBadRequestError     | 400                                                         | application/json                                            |
| models.RecipientCreateTemplateRecipientsInternalServerError | 500                                                         | application/json                                            |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## update

Update a single recipient for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-updateTemplateRecipient" method="post" path="/template/recipient/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.update(template_id=2984.61, recipient={
        "id": 8617.99,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                 | *float*                                                                                                       | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `recipient`                                                                                                   | [models.RecipientUpdateTemplateRecipientRecipient](../../models/recipientupdatetemplaterecipientrecipient.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.RecipientUpdateTemplateRecipientResponse](../../models/recipientupdatetemplaterecipientresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.RecipientUpdateTemplateRecipientBadRequestError     | 400                                                        | application/json                                           |
| models.RecipientUpdateTemplateRecipientInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## update_many

Update multiple recipients for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-updateTemplateRecipients" method="post" path="/template/recipient/update-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.update_many(template_id=5597.58, recipients=[
        {
            "id": 1630.42,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                                       | *float*                                                                                                                             | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `recipients`                                                                                                                        | List[[models.RecipientUpdateTemplateRecipientsRecipientRequest](../../models/recipientupdatetemplaterecipientsrecipientrequest.md)] | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.RecipientUpdateTemplateRecipientsResponse](../../models/recipientupdatetemplaterecipientsresponse.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.RecipientUpdateTemplateRecipientsBadRequestError     | 400                                                         | application/json                                            |
| models.RecipientUpdateTemplateRecipientsInternalServerError | 500                                                         | application/json                                            |
| models.APIError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## delete

Delete template recipient

### Example Usage

<!-- UsageSnippet language="python" operationID="recipient-deleteTemplateRecipient" method="post" path="/template/recipient/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.delete(recipient_id=312.69)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `recipient_id`                                                      | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RecipientDeleteTemplateRecipientResponse](../../models/recipientdeletetemplaterecipientresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.RecipientDeleteTemplateRecipientBadRequestError     | 400                                                        | application/json                                           |
| models.RecipientDeleteTemplateRecipientInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |