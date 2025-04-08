# TemplatesFields
(*templates.fields*)

## Overview

### Available Operations

* [create](#create) - Create template field
* [get](#get) - Get template field
* [create_many](#create_many) - Create template fields
* [update](#update) - Update template field
* [update_many](#update_many) - Update template fields
* [delete](#delete) - Delete template field

## create

Create a single field for a template.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.create(template_id=4865.89, field={
        "type": documenso_sdk.FieldCreateTemplateFieldTypeNumberRequestBody1.NUMBER,
        "recipient_id": 4174.58,
        "page_number": 1343.65,
        "page_x": 690.25,
        "page_y": 7964.74,
        "width": 9510.62,
        "height": 0.86,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `template_id`                                                                                   | *float*                                                                                         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `field`                                                                                         | [models.FieldCreateTemplateFieldFieldUnion](../../models/fieldcreatetemplatefieldfieldunion.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FieldCreateTemplateFieldResponse](../../models/fieldcreatetemplatefieldresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.FieldCreateTemplateFieldBadRequestError     | 400                                                | application/json                                   |
| models.FieldCreateTemplateFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## get

Returns a single field. If you want to retrieve all the fields for a template, use the "Get Template" endpoint.

### Example Usage

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.get(field_id=7003.47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldGetTemplateFieldResponse](../../models/fieldgettemplatefieldresponse.md)**

### Errors

| Error Type                                      | Status Code                                     | Content Type                                    |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| models.FieldGetTemplateFieldBadRequestError     | 400                                             | application/json                                |
| models.FieldGetTemplateFieldNotFoundError       | 404                                             | application/json                                |
| models.FieldGetTemplateFieldInternalServerError | 500                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## create_many

Create multiple fields for a template.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.create_many(template_id=5158.41, fields=[
        {
            "type": documenso_sdk.FieldCreateTemplateFieldsTypeCheckboxRequestBody1.CHECKBOX,
            "recipient_id": 2516.72,
            "page_number": 2304.17,
            "page_x": 7760.32,
            "page_y": 3376.66,
            "width": 3566.94,
            "height": 2768.94,
        },
        {
            "type": documenso_sdk.FieldCreateTemplateFieldsTypeNumberRequestBody1.NUMBER,
            "recipient_id": 5689.64,
            "page_number": 6483.69,
            "page_x": 7271.79,
            "page_y": 1891.56,
            "width": 7263.21,
            "height": 5043.41,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                           | *float*                                                                                                 | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `fields`                                                                                                | List[[models.FieldCreateTemplateFieldsFieldUnion](../../models/fieldcreatetemplatefieldsfieldunion.md)] | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.FieldCreateTemplateFieldsResponse](../../models/fieldcreatetemplatefieldsresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.FieldCreateTemplateFieldsBadRequestError     | 400                                                 | application/json                                    |
| models.FieldCreateTemplateFieldsInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## update

Update a single field for a template.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.update(template_id=8574.78, field={
        "type": documenso_sdk.FieldUpdateTemplateFieldTypeTextRequestBody1.TEXT,
        "id": 3446.2,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `template_id`                                                                                   | *float*                                                                                         | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `field`                                                                                         | [models.FieldUpdateTemplateFieldFieldUnion](../../models/fieldupdatetemplatefieldfieldunion.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.FieldUpdateTemplateFieldResponse](../../models/fieldupdatetemplatefieldresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.FieldUpdateTemplateFieldBadRequestError     | 400                                                | application/json                                   |
| models.FieldUpdateTemplateFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## update_many

Update multiple fields for a template.

### Example Usage

```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.update_many(template_id=4057.69, fields=[
        {
            "type": documenso_sdk.FieldUpdateTemplateFieldsTypeDateRequestBody1.DATE,
            "id": 8982.15,
        },
        {
            "type": documenso_sdk.FieldUpdateTemplateFieldsTypeNameRequestBody1.NAME,
            "id": 310.19,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                           | *float*                                                                                                 | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `fields`                                                                                                | List[[models.FieldUpdateTemplateFieldsFieldUnion](../../models/fieldupdatetemplatefieldsfieldunion.md)] | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.FieldUpdateTemplateFieldsResponse](../../models/fieldupdatetemplatefieldsresponse.md)**

### Errors

| Error Type                                          | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| models.FieldUpdateTemplateFieldsBadRequestError     | 400                                                 | application/json                                    |
| models.FieldUpdateTemplateFieldsInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## delete

Delete template field

### Example Usage

```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.delete(field_id=5459.07)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `field_id`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FieldDeleteTemplateFieldResponse](../../models/fielddeletetemplatefieldresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.FieldDeleteTemplateFieldBadRequestError     | 400                                                | application/json                                   |
| models.FieldDeleteTemplateFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |