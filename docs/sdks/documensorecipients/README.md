# DocumensoRecipients
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

**[models.RecipientGetTemplateRecipientResponseBody](../../models/recipientgettemplaterecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientGetTemplateRecipientTemplatesRecipientsResponseBody            | 400                                                                            | application/json                                                               |
| models.RecipientGetTemplateRecipientTemplatesRecipientsResponseResponseBody    | 404                                                                            | application/json                                                               |
| models.RecipientGetTemplateRecipientTemplatesRecipientsResponse500ResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

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
        "role": documenso_sdk.RecipientCreateTemplateRecipientRole.CC,
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

**[models.RecipientCreateTemplateRecipientResponseBody](../../models/recipientcreatetemplaterecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientCreateTemplateRecipientTemplatesRecipientsResponseBody         | 400                                                                            | application/json                                                               |
| models.RecipientCreateTemplateRecipientTemplatesRecipientsResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

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
            "role": documenso_sdk.RecipientCreateTemplateRecipientsRole.VIEWER,
        },
        {
            "email": "Lyla50@yahoo.com",
            "name": "<value>",
            "role": documenso_sdk.RecipientCreateTemplateRecipientsRole.APPROVER,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                           | *float*                                                                                                                 | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `recipients`                                                                                                            | List[[models.RecipientCreateTemplateRecipientsRecipients](../../models/recipientcreatetemplaterecipientsrecipients.md)] | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.RecipientCreateTemplateRecipientsResponseBody](../../models/recipientcreatetemplaterecipientsresponsebody.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.RecipientCreateTemplateRecipientsTemplatesRecipientsResponseBody         | 400                                                                             | application/json                                                                |
| models.RecipientCreateTemplateRecipientsTemplatesRecipientsResponseResponseBody | 500                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

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

**[models.RecipientUpdateTemplateRecipientResponseBody](../../models/recipientupdatetemplaterecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientUpdateTemplateRecipientTemplatesRecipientsResponseBody         | 400                                                                            | application/json                                                               |
| models.RecipientUpdateTemplateRecipientTemplatesRecipientsResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

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

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                           | *float*                                                                                                                 | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `recipients`                                                                                                            | List[[models.RecipientUpdateTemplateRecipientsRecipients](../../models/recipientupdatetemplaterecipientsrecipients.md)] | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.RecipientUpdateTemplateRecipientsResponseBody](../../models/recipientupdatetemplaterecipientsresponsebody.md)**

### Errors

| Error Type                                                                      | Status Code                                                                     | Content Type                                                                    |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| models.RecipientUpdateTemplateRecipientsTemplatesRecipientsResponseBody         | 400                                                                             | application/json                                                                |
| models.RecipientUpdateTemplateRecipientsTemplatesRecipientsResponseResponseBody | 500                                                                             | application/json                                                                |
| models.APIError                                                                 | 4XX, 5XX                                                                        | \*/\*                                                                           |

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

**[models.RecipientDeleteTemplateRecipientResponseBody](../../models/recipientdeletetemplaterecipientresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.RecipientDeleteTemplateRecipientTemplatesRecipientsResponseBody         | 400                                                                            | application/json                                                               |
| models.RecipientDeleteTemplateRecipientTemplatesRecipientsResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |