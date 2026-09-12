# ~~Documents.Attachments~~

> [!WARNING]
> This SDK is **DEPRECATED**

## Overview

### Available Operations

* [~~create~~](#create) - Create attachment :warning: **Deprecated**
* [~~update~~](#update) - Update attachment :warning: **Deprecated**
* [~~delete~~](#delete) - Delete attachment :warning: **Deprecated**
* [~~find~~](#find) - Find attachments :warning: **Deprecated**

## ~~create~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Create a new attachment for a document

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-create" method="post" path="/document/attachment/create" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.create(document_id=7014.36, data={
        "label": "<value>",
        "data": "https://cheerful-bourgeoisie.org/",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `document_id`                                                                       | *float*                                                                             | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `data`                                                                              | [models.DocumentAttachmentCreateData](../../models/documentattachmentcreatedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.DocumentAttachmentCreateResponse](../../models/documentattachmentcreateresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DocumentAttachmentCreateBadRequestError     | 400                                                | application/json                                   |
| models.DocumentAttachmentCreateUnauthorizedError   | 401                                                | application/json                                   |
| models.DocumentAttachmentCreateForbiddenError      | 403                                                | application/json                                   |
| models.DocumentAttachmentCreateInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## ~~update~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Update an existing attachment

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-update" method="post" path="/document/attachment/update" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.update(id="<id>", data={
        "label": "<value>",
        "data": "https://tinted-ceramics.biz",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `data`                                                                              | [models.DocumentAttachmentUpdateData](../../models/documentattachmentupdatedata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.DocumentAttachmentUpdateResponse](../../models/documentattachmentupdateresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DocumentAttachmentUpdateBadRequestError     | 400                                                | application/json                                   |
| models.DocumentAttachmentUpdateUnauthorizedError   | 401                                                | application/json                                   |
| models.DocumentAttachmentUpdateForbiddenError      | 403                                                | application/json                                   |
| models.DocumentAttachmentUpdateInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## ~~delete~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Delete an attachment from a document

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-delete" method="post" path="/document/attachment/delete" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentAttachmentDeleteResponse](../../models/documentattachmentdeleteresponse.md)**

### Errors

| Error Type                                         | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| models.DocumentAttachmentDeleteBadRequestError     | 400                                                | application/json                                   |
| models.DocumentAttachmentDeleteUnauthorizedError   | 401                                                | application/json                                   |
| models.DocumentAttachmentDeleteForbiddenError      | 403                                                | application/json                                   |
| models.DocumentAttachmentDeleteInternalServerError | 500                                                | application/json                                   |
| models.APIError                                    | 4XX, 5XX                                           | \*/\*                                              |

## ~~find~~

Deprecated: this endpoint is being replaced by the Envelope API. See https://docs.documenso.com/docs/developers/api/migrate-to-envelopes for the migration guide. Find all attachments for a document

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

<!-- UsageSnippet language="python" operationID="document-attachment-find" method="get" path="/document/attachment" -->
```python
from documenso_sdk import Documenso
import os


with Documenso(
    api_key=os.getenv("DOCUMENSO_API_KEY", ""),
) as documenso:

    res = documenso.documents.attachments.find(document_id=965.17)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `document_id`                                                       | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DocumentAttachmentFindResponse](../../models/documentattachmentfindresponse.md)**

### Errors

| Error Type                                       | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| models.DocumentAttachmentFindBadRequestError     | 400                                              | application/json                                 |
| models.DocumentAttachmentFindUnauthorizedError   | 401                                              | application/json                                 |
| models.DocumentAttachmentFindForbiddenError      | 403                                              | application/json                                 |
| models.DocumentAttachmentFindNotFoundError       | 404                                              | application/json                                 |
| models.DocumentAttachmentFindInternalServerError | 500                                              | application/json                                 |
| models.APIError                                  | 4XX, 5XX                                         | \*/\*                                            |