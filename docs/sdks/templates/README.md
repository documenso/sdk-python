# Templates
(*templates*)

## Overview

### Available Operations

* [find](#find) - Find templates
* [get](#get) - Get template
* [update](#update) - Update template
* [duplicate](#duplicate) - Duplicate template
* [delete](#delete) - Delete template
* [use](#use) - Use template
* [move_to_team](#move_to_team) - Move template

## find

Find templates based on a search criteria

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.find()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The search query.                                                   |
| `page`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | The pagination page number, starts at 1.                            |
| `per_page`                                                          | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | The number of items per page.                                       |
| `type`                                                              | [Optional[models.QueryParamType]](../../models/queryparamtype.md)   | :heavy_minus_sign:                                                  | Filter templates by type.                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateFindTemplatesResponseBody](../../models/templatefindtemplatesresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ErrorNOTFOUND            | 404                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## get

Get template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.get(template_id=7003.47)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateGetTemplateByIDResponseBody](../../models/templategettemplatebyidresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ErrorNOTFOUND            | 404                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update

Update template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.update(template_id=8574.78)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `template_id`                                                                             | *float*                                                                                   | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `data`                                                                                    | [Optional[models.TemplateUpdateTemplateData]](../../models/templateupdatetemplatedata.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `meta`                                                                                    | [Optional[models.TemplateUpdateTemplateMeta]](../../models/templateupdatetemplatemeta.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.TemplateUpdateTemplateResponseBody](../../models/templateupdatetemplateresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## duplicate

Duplicate template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.duplicate(template_id=3523.11)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateDuplicateTemplateResponseBody](../../models/templateduplicatetemplateresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## delete

Delete template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.delete(template_id=5459.07)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateDeleteTemplateResponseBody](../../models/templatedeletetemplateresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## use

Use the template to create a document

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.use(template_id=6626.9, recipients=[
        {
            "id": 6473.53,
            "email": "August_Schmeler68@yahoo.com",
        },
        {
            "id": 3772.31,
            "email": "Angeline.Purdy@gmail.com",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `template_id`                                                                                                                        | *float*                                                                                                                              | :heavy_check_mark:                                                                                                                   | N/A                                                                                                                                  |
| `recipients`                                                                                                                         | List[[models.TemplateCreateDocumentFromTemplateRecipients](../../models/templatecreatedocumentfromtemplaterecipients.md)]            | :heavy_check_mark:                                                                                                                   | The information of the recipients to create the document with.                                                                       |
| `distribute_document`                                                                                                                | *Optional[bool]*                                                                                                                     | :heavy_minus_sign:                                                                                                                   | Whether to create the document as pending and distribute it to recipients.                                                           |
| `custom_document_data_id`                                                                                                            | *Optional[str]*                                                                                                                      | :heavy_minus_sign:                                                                                                                   | The data ID of an alternative PDF to use when creating the document. If not provided, the PDF attached to the template will be used. |
| `retries`                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                     | :heavy_minus_sign:                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                  |

### Response

**[models.TemplateCreateDocumentFromTemplateResponseBody](../../models/templatecreatedocumentfromtemplateresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## move_to_team

Move a template to a team

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.move_to_team(template_id=8301.72, team_id=6724.78)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | The ID of the template to move to.                                  |
| `team_id`                                                           | *float*                                                             | :heavy_check_mark:                                                  | The ID of the team to move the template to.                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateMoveTemplateToTeamResponseBody](../../models/templatemovetemplatetoteamresponsebody.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.ErrorBADREQUEST          | 400                             | application/json                |
| models.ERRORINTERNALSERVERERROR | 500                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |