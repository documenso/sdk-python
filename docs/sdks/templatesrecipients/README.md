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

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.get(recipient_id=7003.47)

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

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.create(template_id=4865.89, recipient={
        "email": "Haylie_Bernhard95@yahoo.com",
        "name": "<value>",
        "role": documenso_sdk.RecipientCreateTemplateRecipientRoleRequestBody.CC,
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

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.create_many(template_id=5158.41, recipients=[
        {
            "email": "Demetrius.Sanford35@hotmail.com",
            "name": "<value>",
            "role": documenso_sdk.RecipientCreateTemplateRecipientsRoleRequestBody.APPROVER,
        },
        {
            "email": "Lyla50@yahoo.com",
            "name": "<value>",
            "role": documenso_sdk.RecipientCreateTemplateRecipientsRoleRequestBody.APPROVER,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                                               | *float*                                                                                                                                     | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `recipients`                                                                                                                                | List[[models.RecipientCreateTemplateRecipientsRecipientRequestBody](../../models/recipientcreatetemplaterecipientsrecipientrequestbody.md)] | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

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

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.update(template_id=8574.78, recipient={
        "id": 5971.29,
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

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.update_many(template_id=4057.69, recipients=[
        {
            "id": 5359.16,
        },
        {
            "id": 8982.15,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                                               | *float*                                                                                                                                     | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `recipients`                                                                                                                                | List[[models.RecipientUpdateTemplateRecipientsRecipientRequestBody](../../models/recipientupdatetemplaterecipientsrecipientrequestbody.md)] | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

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

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.recipients.delete(recipient_id=5459.07)

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