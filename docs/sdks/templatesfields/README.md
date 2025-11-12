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

<!-- UsageSnippet language="python" operationID="field-createTemplateField" method="post" path="/template/field/create" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.create(template_id=1203.71, field={
        "type": documenso_sdk.FieldCreateTemplateFieldTypeDateRequest1.DATE,
        "recipient_id": 2738.54,
        "page_number": 5735.12,
        "page_x": 2936.28,
        "page_y": 8594.41,
        "width": 7589.39,
        "height": 3122.23,
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
| models.FieldCreateTemplateFieldUnauthorizedError   | 401                                                | application/json                                   |
| models.FieldCreateTemplateFieldForbiddenError      | 403                                                | application/json                                   |
| models.FieldCreateTemplateFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## get

Returns a single field. If you want to retrieve all the fields for a template, use the "Get Template" endpoint.

### Example Usage

<!-- UsageSnippet language="python" operationID="field-getTemplateField" method="get" path="/template/field/{fieldId}" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.get(field_id=1152.82)

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
| models.FieldGetTemplateFieldUnauthorizedError   | 401                                             | application/json                                |
| models.FieldGetTemplateFieldForbiddenError      | 403                                             | application/json                                |
| models.FieldGetTemplateFieldNotFoundError       | 404                                             | application/json                                |
| models.FieldGetTemplateFieldInternalServerError | 500                                             | application/json                                |
| models.APIError                                 | 4XX, 5XX                                        | \*/\*                                           |

## create_many

Create multiple fields for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="field-createTemplateFields" method="post" path="/template/field/create-many" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.create_many(template_id=586.2, fields=[
        {
            "type": documenso_sdk.FieldCreateTemplateFieldsTypeSignatureRequest1.SIGNATURE,
            "recipient_id": 6990.12,
            "page_number": 3472.45,
            "page_x": 4747.87,
            "page_y": 1673.94,
            "width": 7215.37,
            "height": 9417.43,
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
| models.FieldCreateTemplateFieldsUnauthorizedError   | 401                                                 | application/json                                    |
| models.FieldCreateTemplateFieldsForbiddenError      | 403                                                 | application/json                                    |
| models.FieldCreateTemplateFieldsInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## update

Update a single field for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="field-updateTemplateField" method="post" path="/template/field/update" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.update(template_id=5083.07, field={
        "type": documenso_sdk.FieldUpdateTemplateFieldTypeTextRequest1.TEXT,
        "id": 1792.29,
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
| models.FieldUpdateTemplateFieldUnauthorizedError   | 401                                                | application/json                                   |
| models.FieldUpdateTemplateFieldForbiddenError      | 403                                                | application/json                                   |
| models.FieldUpdateTemplateFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## update_many

Update multiple fields for a template.

### Example Usage

<!-- UsageSnippet language="python" operationID="field-updateTemplateFields" method="post" path="/template/field/update-many" -->
```python
import documenso_sdk
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.update_many(template_id=3969.1, fields=[
        {
            "type": documenso_sdk.FieldUpdateTemplateFieldsTypeDropdownRequest1.DROPDOWN,
            "id": 2460.72,
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
| models.FieldUpdateTemplateFieldsUnauthorizedError   | 401                                                 | application/json                                    |
| models.FieldUpdateTemplateFieldsForbiddenError      | 403                                                 | application/json                                    |
| models.FieldUpdateTemplateFieldsInternalServerError | 500                                                 | application/json                                    |
| models.APIError                                     | 4XX, 5XX                                            | \*/\*                                               |

## delete

Delete template field

### Example Usage

<!-- UsageSnippet language="python" operationID="field-deleteTemplateField" method="post" path="/template/field/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.fields.delete(field_id=7996.49)

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
| models.FieldDeleteTemplateFieldUnauthorizedError   | 401                                                | application/json                                   |
| models.FieldDeleteTemplateFieldForbiddenError      | 403                                                | application/json                                   |
| models.FieldDeleteTemplateFieldInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |