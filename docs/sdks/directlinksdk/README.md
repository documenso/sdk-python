# DirectLinkSDK
(*templates.direct_link*)

## Overview

### Available Operations

* [create](#create) - Create direct link
* [delete](#delete) - Delete direct link
* [toggle](#toggle) - Toggle direct link

## create

Create a direct link for a template

### Example Usage

<!-- UsageSnippet language="python" operationID="template-createTemplateDirectLink" method="post" path="/template/direct/create" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.direct_link.create(template_id=5094.31)

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

**[models.TemplateCreateTemplateDirectLinkResponse](../../models/templatecreatetemplatedirectlinkresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.TemplateCreateTemplateDirectLinkBadRequestError     | 400                                                        | application/json                                           |
| models.TemplateCreateTemplateDirectLinkInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## delete

Delete a direct link for a template

### Example Usage

<!-- UsageSnippet language="python" operationID="template-deleteTemplateDirectLink" method="post" path="/template/direct/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.direct_link.delete(template_id=9950.03)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TemplateDeleteTemplateDirectLinkResponse](../../models/templatedeletetemplatedirectlinkresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.TemplateDeleteTemplateDirectLinkBadRequestError     | 400                                                        | application/json                                           |
| models.TemplateDeleteTemplateDirectLinkInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |

## toggle

Enable or disable a direct link for a template

### Example Usage

<!-- UsageSnippet language="python" operationID="template-toggleTemplateDirectLink" method="post" path="/template/direct/toggle" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.templates.direct_link.toggle(template_id=6583.54, enabled=False)

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

**[models.TemplateToggleTemplateDirectLinkResponse](../../models/templatetoggletemplatedirectlinkresponse.md)**

### Errors

| Error Type                                                 | Status Code                                                | Content Type                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| models.TemplateToggleTemplateDirectLinkBadRequestError     | 400                                                        | application/json                                           |
| models.TemplateToggleTemplateDirectLinkInternalServerError | 500                                                        | application/json                                           |
| models.APIError                                            | 4XX, 5XX                                                   | \*/\*                                                      |