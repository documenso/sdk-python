# DirectLink
(*templates.direct_link*)

## Overview

### Available Operations

* [create](#create) - Create direct link
* [delete](#delete) - Delete direct link
* [toggle](#toggle) - Toggle direct link

## create

Create a direct link for a template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.direct_link.create(template_id=4865.89)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                                   | *float*                                                                                                         | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `direct_recipient_id`                                                                                           | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | The of the recipient in the current template to transform into the primary recipient when the template is used. |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.TemplateCreateTemplateDirectLinkResponseBody](../../models/templatecreatetemplatedirectlinkresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.TemplateCreateTemplateDirectLinkTemplatesDirectLinkResponseBody         | 400                                                                            | application/json                                                               |
| models.TemplateCreateTemplateDirectLinkTemplatesDirectLinkResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

## delete

Delete a direct link for a template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.direct_link.delete(template_id=5459.07)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateDeleteTemplateDirectLinkResponseBody](../../models/templatedeletetemplatedirectlinkresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.TemplateDeleteTemplateDirectLinkTemplatesDirectLinkResponseBody         | 400                                                                            | application/json                                                               |
| models.TemplateDeleteTemplateDirectLinkTemplatesDirectLinkResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |

## toggle

Enable or disable a direct link for a template

### Example Usage

```python
from documenso_sdk import Documenso
import os

with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.direct_link.toggle(template_id=722.9, enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateToggleTemplateDirectLinkResponseBody](../../models/templatetoggletemplatedirectlinkresponsebody.md)**

### Errors

| Error Type                                                                     | Status Code                                                                    | Content Type                                                                   |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| models.TemplateToggleTemplateDirectLinkTemplatesDirectLinkResponseBody         | 400                                                                            | application/json                                                               |
| models.TemplateToggleTemplateDirectLinkTemplatesDirectLinkResponseResponseBody | 500                                                                            | application/json                                                               |
| models.APIError                                                                | 4XX, 5XX                                                                       | \*/\*                                                                          |