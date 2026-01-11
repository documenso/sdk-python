# Template

## Overview

### Available Operations

* [template_get_many](#template_get_many) - Get multiple templates
* [template_create_template_temporary](#template_create_template_temporary) - Create template

## template_get_many

Retrieve multiple templates by their IDs

### Example Usage

<!-- UsageSnippet language="python" operationID="template-getMany" method="post" path="/template/get-many" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.template.template_get_many(template_ids=[
        618.65,
        1418.73,
        1001.18,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_ids`                                                      | List[*float*]                                                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateGetManyResponse](../../models/templategetmanyresponse.md)**

### Errors

| Error Type                                | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| models.TemplateGetManyBadRequestError     | 400                                       | application/json                          |
| models.TemplateGetManyUnauthorizedError   | 401                                       | application/json                          |
| models.TemplateGetManyForbiddenError      | 403                                       | application/json                          |
| models.TemplateGetManyInternalServerError | 500                                       | application/json                          |
| models.APIError                           | 4XX, 5XX                                  | \*/\*                                     |

## template_create_template_temporary

You will need to upload the PDF to the provided URL returned. Note: Once V2 API is released, this will be removed since we will allow direct uploads, instead of using an upload URL.

### Example Usage

<!-- UsageSnippet language="python" operationID="template-createTemplateTemporary" method="post" path="/template/create/beta" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.template.template_create_template_temporary(title="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`                                                                                                                                       | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | N/A                                                                                                                                           |
| `folder_id`                                                                                                                                   | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `external_id`                                                                                                                                 | *OptionalNullable[str]*                                                                                                                       | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `visibility`                                                                                                                                  | [Optional[models.TemplateCreateTemplateTemporaryVisibilityRequest]](../../models/templatecreatetemplatetemporaryvisibilityrequest.md)         | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `global_access_auth`                                                                                                                          | List[[models.TemplateCreateTemplateTemporaryGlobalAccessAuthRequest](../../models/templatecreatetemplatetemporaryglobalaccessauthrequest.md)] | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `global_action_auth`                                                                                                                          | List[[models.TemplateCreateTemplateTemporaryGlobalActionAuthRequest](../../models/templatecreatetemplatetemporaryglobalactionauthrequest.md)] | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `public_title`                                                                                                                                | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `public_description`                                                                                                                          | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `type`                                                                                                                                        | [Optional[models.TemplateCreateTemplateTemporaryTypeRequest]](../../models/templatecreatetemplatetemporarytyperequest.md)                     | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `meta`                                                                                                                                        | [Optional[models.TemplateCreateTemplateTemporaryMeta]](../../models/templatecreatetemplatetemporarymeta.md)                                   | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `attachments`                                                                                                                                 | List[[models.TemplateCreateTemplateTemporaryAttachment](../../models/templatecreatetemplatetemporaryattachment.md)]                           | :heavy_minus_sign:                                                                                                                            | N/A                                                                                                                                           |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |

### Response

**[models.TemplateCreateTemplateTemporaryResponse](../../models/templatecreatetemplatetemporaryresponse.md)**

### Errors

| Error Type                                                | Status Code                                               | Content Type                                              |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| models.TemplateCreateTemplateTemporaryBadRequestError     | 400                                                       | application/json                                          |
| models.TemplateCreateTemplateTemporaryUnauthorizedError   | 401                                                       | application/json                                          |
| models.TemplateCreateTemplateTemporaryForbiddenError      | 403                                                       | application/json                                          |
| models.TemplateCreateTemplateTemporaryInternalServerError | 500                                                       | application/json                                          |
| models.APIError                                           | 4XX, 5XX                                                  | \*/\*                                                     |