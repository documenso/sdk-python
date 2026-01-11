# Envelopes.Attachments

## Overview

### Available Operations

* [find](#find) - Find attachments
* [create](#create) - Create attachment
* [update](#update) - Update attachment
* [delete](#delete) - Delete attachment

## find

Find all attachments for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-attachment-find" method="get" path="/envelope/attachment" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.attachments.find(envelope_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `envelope_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `token`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeAttachmentFindResponse](../../models/envelopeattachmentfindresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.EnvelopeAttachmentFindBadRequestError     | 400                                              | application/json                                 |
| models.EnvelopeAttachmentFindUnauthorizedError   | 401                                              | application/json                                 |
| models.EnvelopeAttachmentFindForbiddenError      | 403                                              | application/json                                 |
| models.EnvelopeAttachmentFindNotFoundError       | 404                                              | application/json                                 |
| models.EnvelopeAttachmentFindInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |

## create

Create a new attachment for an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-attachment-create" method="post" path="/envelope/attachment/create" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.attachments.create(envelope_id="<id>", data={
        "label": "<value>",
        "data": "https://lustrous-skeleton.info",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `envelope_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `data`                                                                              | [models.EnvelopeAttachmentCreateData](../../models/envelopeattachmentcreatedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EnvelopeAttachmentCreateResponse](../../models/envelopeattachmentcreateresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.EnvelopeAttachmentCreateBadRequestError     | 400                                                | application/json                                   |
| models.EnvelopeAttachmentCreateUnauthorizedError   | 401                                                | application/json                                   |
| models.EnvelopeAttachmentCreateForbiddenError      | 403                                                | application/json                                   |
| models.EnvelopeAttachmentCreateInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## update

Update an existing attachment

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-attachment-update" method="post" path="/envelope/attachment/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.attachments.update(id="<id>", data={
        "label": "<value>",
        "data": "https://tough-premier.biz",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `data`                                                                              | [models.EnvelopeAttachmentUpdateData](../../models/envelopeattachmentupdatedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EnvelopeAttachmentUpdateResponse](../../models/envelopeattachmentupdateresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.EnvelopeAttachmentUpdateBadRequestError     | 400                                                | application/json                                   |
| models.EnvelopeAttachmentUpdateUnauthorizedError   | 401                                                | application/json                                   |
| models.EnvelopeAttachmentUpdateForbiddenError      | 403                                                | application/json                                   |
| models.EnvelopeAttachmentUpdateInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## delete

Delete an attachment from an envelope

### Example Usage

<!-- UsageSnippet language="python" operationID="envelope-attachment-delete" method="post" path="/envelope/attachment/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.envelopes.attachments.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EnvelopeAttachmentDeleteResponse](../../models/envelopeattachmentdeleteresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.EnvelopeAttachmentDeleteBadRequestError     | 400                                                | application/json                                   |
| models.EnvelopeAttachmentDeleteUnauthorizedError   | 401                                                | application/json                                   |
| models.EnvelopeAttachmentDeleteForbiddenError      | 403                                                | application/json                                   |
| models.EnvelopeAttachmentDeleteInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |